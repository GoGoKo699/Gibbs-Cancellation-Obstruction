#!/usr/bin/env python3
"""Certify an intrinsic local-evaluation lower bound with Arb ball arithmetic.

Dependencies: python-flint (ordinary import; no local binary paths).
Inputs: a Pauli-coefficient JSON and row/column indices of a 923-minor.
The selected minor is verified at the requested exact rational temperature.
No numerical rank threshold, eigenvectors, or saved floating-point matrix is
used. See README.md for the intrinsic-norm argument.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import time

import flint
from flint import acb, acb_mat, arb, arb_mat, ctx, fmpq


N, D = 5, 32
LABELS = list(itertools.product(range(4), repeat=N))
RAW = [(edge, mu, nu) for edge in range(4)
       for mu in itertools.product(range(4), repeat=2) if mu != (0, 0)
       for nu in itertools.product(range(4), repeat=2)]


def decimal_bound(value, *, upper, digits=16):
    """Return a decimal string whose direction is checked again with Arb."""
    with localcontext() as context:
        context.prec = digits + 20
        candidate = Decimal(f"{float(value):.{digits - 1}e}")
        unit = Decimal(1).scaleb(candidate.adjusted() - digits + 1)
        while not (arb(str(candidate)) > value if upper else arb(str(candidate)) < value):
            candidate += unit if upper else -unit
        return str(candidate)


def pauli_action(label, x):
    flip = sum(1 << (N - 1 - j) for j, a in enumerate(label) if a in (1, 2))
    parity = sum(((x >> (N - 1 - j)) & 1) for j, a in enumerate(label) if a in (2, 3))
    phase = sum(a == 2 for a in label) % 4
    real, imag = [(1, 0), (0, 1), (-1, 0), (0, -1)][phase]
    sign = -1 if parity % 2 else 1
    return x ^ flip, sign * real, sign * imag


def exact_hamiltonian(path):
    coefficients = json.loads(path.read_text())
    real = [[0] * D for _ in range(D)]
    imag = [[0] * D for _ in range(D)]
    for key, value in coefficients.items():
        label = tuple(json.loads(key))
        assert len(label) == N and all(a in range(4) for a in label)
        assert isinstance(value, int)
        support = [j for j, a in enumerate(label) if a]
        assert len(support) in (1, 2)
        assert len(support) == 1 or support[1] == support[0] + 1
        for x in range(D):
            y, phase_real, phase_imag = pauli_action(label, x)
            real[y][x] += value * phase_real
            imag[y][x] += value * phase_imag
    assert sum(real[j][j] for j in range(D)) == 0
    assert all(real[i][j] == real[j][i] and imag[i][j] == -imag[j][i]
               for i in range(D) for j in range(D))
    assert any(value != 0 for row in real + imag for value in row)
    return acb_mat(D, D, [acb(real[i][j], imag[i][j]) for i in range(D) for j in range(D)])


def gibbs_coefficients(h, beta):
    sigma = (-beta * h).exp()
    # Hermiticity makes the trace exactly real, so the real enclosure suffices.
    partition = sigma.trace().real
    assert partition > 0
    rho = sigma / partition
    result = []
    for label in LABELS:
        value = acb(0)
        for x in range(D):
            y, phase_real, phase_imag = pauli_action(label, x)
            value += acb(phase_real, phase_imag) * rho[x, y]
        # Both factors in the trace are Hermitian: its exact imaginary part is0.
        assert value.imag.contains(0)
        result.append(value.real)
    result[0] = arb(1)  # Tr(rho)=1 exactly, independently of its enclosure.
    return result


def evaluation_minor(coefficients, data):
    rows, columns = data["rows"], data["columns"]
    assert len(rows) == len(set(rows)) == 923
    assert len(columns) == len(set(columns)) == 923
    assert all(0 <= row < 1023 for row in rows)
    assert all(0 <= column < 960 for column in columns)
    lookup = {label: i for i, label in enumerate(LABELS)}
    entries = []
    for row in rows:
        output = LABELS[row + 1]
        for column in columns:
            edge, mu, nu = RAW[column]
            if output[edge:edge + 2] == mu:
                source = output[:edge] + nu + output[edge + 2:]
                entries.append(coefficients[lookup[source]])
            else:
                entries.append(arb(0))
    return arb_mat(923, 923, entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beta", default="3/1000", help="Exact positive rational, e.g.3/1000 or1/100")
    parser.add_argument("--precision", type=int, default=256, help="Arb working precision in bits")
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent / "data")
    parser.add_argument("--output", type=Path, help="Optional JSON report path; otherwise print only")
    args = parser.parse_args()
    start = time.monotonic()
    rational_beta = Fraction(args.beta)
    assert rational_beta > 0 and args.precision >= 64
    ctx.prec = args.precision
    beta = arb(fmpq(rational_beta.numerator, rational_beta.denominator))
    hpath = args.data_dir / "hamiltonian.json"
    mpath = args.data_dir / "quantitative-minor.json"
    h = exact_hamiltonian(hpath)
    coefficients = gibbs_coefficients(h, beta)
    minor = evaluation_minor(coefficients, json.loads(mpath.read_text()))
    inverse = minor.inv()  # Certified Arb inverse; raises if not certified.
    squares, radius_max = arb(0), arb(0)
    for entry in inverse.entries():
        assert entry.is_finite()
        absolute_upper = entry.abs_upper()
        squares += absolute_upper * absolute_upper
        if entry.rad() > radius_max:
            radius_max = entry.rad()
    inverse_frobenius_upper = squares.sqrt().upper()
    denominator = 16 * arb(32).sqrt() * inverse_frobenius_upper
    s_lower = (1 / denominator).lower()
    gap_coefficient_upper = (2 * denominator).upper()
    report = {
        "beta_exact": str(rational_beta),
        "precision_bits": args.precision,
        "python_flint_version": flint.__version__,
        "hamiltonian_sha256": hashlib.sha256(hpath.read_bytes()).hexdigest(),
        "minor_indices_sha256": hashlib.sha256(mpath.read_bytes()).hexdigest(),
        "minor_order": 923,
        "inverse_certified": True,
        "inverse_frobenius_upper_ball": inverse_frobenius_upper.str(30),
        "inverse_max_entry_radius_ball": radius_max.str(30),
        "intrinsic_s_lower_decimal": decimal_bound(s_lower, upper=False),
        "gap_over_J_half_trace_error_upper_decimal": decimal_bound(gap_coefficient_upper, upper=True),
        "intrinsic_s_lower_ball": s_lower.str(30),
        "gap_coefficient_upper_ball": gap_coefficient_upper.str(30),
        "statement": "gap(L) <= coefficient * ||L||_(2->2) * half_trace_distance(stationary_state, Gibbs_target)",
        "basis_normalization": "Global normalized Pauli basis; raw synthesis norm<=16; Pauli traces divided bysqrt32",
        "numerical_svd_used": False,
        "elapsed_seconds": time.monotonic() - start,
    }
    text = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()

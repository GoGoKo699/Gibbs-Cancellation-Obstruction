#!/usr/bin/env python3
"""Rigorous ground marginal and Gibbs-deficit certificate for fixed H0.

Requires python-flint==0.9.0. Every accepted inequality is checked using
256-bit Arb/Acb ball arithmetic. Rump's eigenvalue/eigenvector enclosures
certify the simple spectrum and the normalized ground vector; floating
midpoints are used only to order already disjoint real eigenvalue balls.
No floating-point eigenvalue or rank threshold is accepted as evidence.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import math
from flint import arb, acb, acb_mat, fmpq, ctx

HERE = Path(__file__).resolve().parent


def require(condition, message):
    """Mandatory certificate check, retained under python -O."""
    if not condition:
        raise ArithmeticError(message)


def pauli_string(labels):
    n = 2**len(labels)
    result = acb_mat(n, n)
    for column in range(n):
        row = column
        phase = acb(1)
        for site, label in enumerate(labels):
            bit = (column >> (len(labels)-1-site)) & 1
            if label in (1, 2):
                row ^= 1 << (len(labels)-1-site)
            if label == 2:
                phase *= acb(0, 1 if bit == 0 else -1)
            if label == 3 and bit:
                phase = -phase
        result[row, column] = phase
    return result


def marginal(vector, support):
    rest = tuple(site for site in range(5) if site not in support)
    def index(local, outside):
        bits = [0]*5
        for j, site in enumerate(support):
            bits[site] = (local >> (len(support)-1-j)) & 1
        for j, site in enumerate(rest):
            bits[site] = (outside >> (len(rest)-1-j)) & 1
        return sum(bit << (4-site) for site, bit in enumerate(bits))
    n = 2**len(support)
    rho = acb_mat(n, n)
    for a in range(n):
        for b in range(n):
            rho[a, b] = sum((vector[index(a, z)] * vector[index(b, z)].conjugate()
                             for z in range(2**len(rest))), acb(0))
    return rho


def eigenvalues(matrix):
    values = sorted((v.real for v in matrix.eig(algorithm="rump")),
                    key=lambda x: float(x.mid()))
    if not all(values[j+1] > values[j] for j in range(len(values)-1)):
        raise ArithmeticError("Real eigenvalue balls are not disjoint.")
    return values


def enclosure(x, denominator=10**12):
    """Return and verify a convenient enclosing rational decimal interval."""
    numerator = math.floor(float(x.mid()) * denominator)
    lo, hi = arb(fmpq(numerator, denominator)), arb(fmpq(numerator+1, denominator))
    if not (x > lo and x < hi):
        raise ArithmeticError("Suggested decimal enclosure was not verified.")
    return {"lower_numerator": numerator, "upper_numerator": numerator+1,
            "denominator": denominator, "ball": x.str(55)}


def deficit(energies, beta):
    q = sum(((-beta*(e-energies[0])).exp() for e in energies[1:]), arb(0))
    return q/(1+q)


def ldl_positive(matrix):
    """Interval LDL* verifies positive definiteness of exact Hermitian input."""
    n = matrix.nrows()
    L = acb_mat(n, n)
    pivots = []
    for j in range(n):
        pivot = matrix[j, j].real
        for k in range(j):
            pivot -= abs(L[j, k])**2*pivots[k]
        if not pivot > 0:
            raise ArithmeticError("LDL* failed to certify strict positivity")
        pivots.append(pivot)
        L[j, j] = 1
        for i in range(j+1, n):
            entry = matrix[i, j]
            for k in range(j):
                entry -= L[i, k]*L[j, k].conjugate()*pivots[k]
            L[i, j] = entry/pivot
    return pivots


def population_forms(H, ground_energy, vector):
    """Certify full population-balance form for all four 2-site jump spaces.

    A=sum_u c_u F_u, with 15 nonidentity Hermitian two-site Paulis, allows
    arbitrary complex c. Q_uv=<g|F_v W F_u|g>-<g|F_u F_v|g>, so q(A)=c*Qc.
    Identity contributions cancel, so omission of the scalar direction loses
    no genuinely dissipative jump. W=exp[-beta(H-E0)].
    """
    beta = arb(fmpq(12, 5))
    W = ((-beta)*H).exp() * (beta*ground_energy).exp()
    output = []
    for bond in range(4):
        F = []
        for u in range(1, 16):
            labels = [0]*5
            labels[bond], labels[bond+1] = divmod(u, 4)
            F.append(pauli_string(labels))
        V = acb_mat(32, 15)
        for u, matrix in enumerate(F):
            for i in range(32):
                V[i, u] = sum((matrix[i, j]*vector[j] for j in range(32)), acb(0))
        adjoint = V.transpose().conjugate()
        C, G = adjoint * W * V, adjoint * V
        Q = C.transpose()-G
        # Each candidate is checked rigorously by the ensuing interval LDL*.
        candidates = ["0.00008", "0.029", "0.013", "0.00029"]
        margin = arb(candidates[bond])
        identity = acb_mat([[int(i == j) for j in range(15)] for i in range(15)])
        pivots = ldl_positive(-Q-margin*identity)
        output.append({"support": [bond+1, bond+2], "dimension": 15,
                       "minus_Q_strictly_exceeds_margin_identity": candidates[bond],
                       "ldl_positive_pivot_balls": [p.str(55) for p in pivots]})
    return {"inverse_temperature": "12/5", "basis": "15 unnormalized nonidentity bond Paulis",
            "criterion": "Q is strictly negative definite on all nonscalar bond operators",
            "conclusion": "No genuine bond/on-site dissipation can fix rho_beta for any beta >= 12/5; arbitrary global coherent control is allowed",
            "bonds": output}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hamiltonian", type=Path, default=HERE.parent/"data"/"hamiltonian.json")
    parser.add_argument("--output", type=Path, default=HERE/"ground_thermal_certificate.json")
    args = parser.parse_args()
    ctx.prec = 256
    raw_bytes = args.hamiltonian.read_bytes()
    raw = json.loads(raw_bytes)
    H = acb_mat(32, 32)
    for key, coefficient in raw.items():
        H += int(coefficient) * pauli_string(json.loads(key))
    evals, vectors = H.eig(algorithm="rump", right=True)
    order = sorted(range(32), key=lambda j: float(evals[j].real.mid()))
    energies = [evals[j].real for j in order]
    require(all(energies[j+1] > energies[j] for j in range(31)),
            "The exact 32-level spectrum was not certified simple.")
    col = order[0]
    norm_sq = sum((abs(vectors[j, col])**2 for j in range(32)), arb(0))
    require(norm_sq > 0, "The enclosed ground eigenvector norm may vanish.")
    vector = [vectors[j, col]/norm_sq.sqrt() for j in range(32)]
    supports = [(j,) for j in range(5)] + [(j, j+1) for j in range(4)]
    spectra = [eigenvalues(marginal(vector, support)) for support in supports]
    require(all(values[0] > 0 for values in spectra),
            "An allowed ground-state marginal was not certified positive definite.")
    minimum = min(range(9), key=lambda j: float(spectra[j][0].mid()))
    mu = spectra[minimum][0]
    require(all(spectra[j][0] > mu for j in range(9) if j != minimum),
            "The unique mu-minimizing support was not certified.")
    ratios = [values[0]/values[-1] for values in spectra]
    ratio_index = min(range(9), key=lambda j: float(ratios[j].mid()))
    r = ratios[ratio_index]
    require(all(ratios[j] > r for j in range(9) if j != ratio_index),
            "The unique ratio-minimizing support was not certified.")
    gap = energies[1]-energies[0]
    beta_ratio = -r.log()/gap
    # These are the unique positive crossings of the indicated sufficient
    # obstruction tests, not claimed exact physical feasibility thresholds.
    crossing_brackets = {
        "inherited_mu_over_two": ("3.41147195216", "3.41147195217", mu/2),
        "fixed_ground_vector_mu": ("3.18245872502", "3.18245872503", mu),
    }
    crossings = {}
    for name, (lo, hi, target) in crossing_brackets.items():
        blo, bhi = arb(lo), arb(hi)
        require(deficit(energies, blo) > target,
                f"The lower crossing endpoint was not certified: {name}")
        require(deficit(energies, bhi) < target,
                f"The upper crossing endpoint was not certified: {name}")
        crossings[name] = {"beta_lower": lo, "beta_upper": hi,
                           "criterion_target_ball": target.str(55)}
    thermal = {}
    for num, den in [(12,5), (3,1), (16,5), (13,4), (7,2), (4,1)]:
        beta = arb(fmpq(num, den))
        delta = deficit(energies, beta)
        thermal[f"{num}/{den}"] = {
            "deficit": enclosure(delta, 10**15),
            "mu_minus_deficit": enclosure(mu-delta, 10**15),
            "mu_over_two_minus_deficit": enclosure(mu/2-delta, 10**15),
            "r_minus_first_boltzmann_ratio": enclosure(r-(-beta*gap).exp(), 10**15),
        }
    result = {
        "precision_bits": ctx.prec,
        "arithmetic": "python-flint 0.9.0 / Arb Acb; Rump eigen enclosures",
        "hamiltonian_sha256": sha256(raw_bytes).hexdigest(),
        "dimension": 32,
        "support_numbering": "One-based site labels; computational site 1 is the most significant bit",
        "spectrum": [enclosure(e) for e in energies],
        "first_gap": enclosure(gap),
        "ground_marginal_spectra": [
            {"support": [j+1 for j in support],
             "eigenvalues": [enclosure(e) for e in values],
             "min_over_max": enclosure(ratio, 10**15)}
            for support, values, ratio in zip(supports, spectra, ratios)],
        "mu": enclosure(mu, 10**15),
        "mu_attaining_support": [j+1 for j in supports[minimum]],
        "r": enclosure(r, 10**15),
        "r_attaining_support": [j+1 for j in supports[ratio_index]],
        "ratio_obstruction_beta": enclosure(beta_ratio),
        "thermal_deficit": thermal,
        "full_ground_population_form": population_forms(H, energies[0], vector),
        "crossings": crossings,
        "accepted_checks": {
            "all_32_energy_balls_disjoint": True,
            "normalized_ground_eigenvector_enclosed": True,
            "all_nine_ground_marginals_positive_definite": True,
            "mu_and_ratio_minimizing_supports_certified": True,
            "thermal_crossing_brackets_certified": True,
            "all_four_population_forms_strictly_negative": True,
        },
    }
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ["first_gap", "mu", "r", "ratio_obstruction_beta", "crossings"]}, indent=2))


if __name__ == "__main__":
    main()

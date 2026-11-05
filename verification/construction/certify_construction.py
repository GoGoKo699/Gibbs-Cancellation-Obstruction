#!/usr/bin/env python3
"""Certified local GKLS design for the five-qubit Gibbs witness.

All displayed inequalities are proved by Arb ball comparisons. Floating point
eigenvalues choose rational interpolation nodes only; a rational approximate
right inverse is merely a witness whose validity is subsequently checked.
Neither is accepted as a spectral or linear-system certificate.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import time

import numpy as np

from flint import arb, acb, arb_mat, acb_mat, fmpq, ctx

HERE = Path(__file__).resolve().parent


def real_matrix(a: acb_mat) -> arb_mat:
    return arb_mat(a.nrows(), a.ncols(),
                   [a[i, j].real for i in range(a.nrows()) for j in range(a.ncols())])


def frob(a) -> arb:
    return sum((abs(a[i, j]).upper() ** 2 for i in range(a.nrows())
                for j in range(a.ncols())), arb(0)).sqrt()


def infinity_norm(a) -> arb:
    bounds = [sum((abs(a[i, j]) for j in range(a.ncols())), arb(0)).upper()
              for i in range(a.nrows())]
    return max(bounds)


def certified_hermitian_norm(a):
    """Upper bounds using row sums, Frobenius, and even spectral moments.

    The represented exact matrix must be Hermitian. Its eigenvalues are real,
    so ||a|| <= Tr(a**(2k))**(1/(2k)). Interval arithmetic encloses each trace.
    This avoids trusting floating point eigenvectors or eigenvalues.
    """
    bounds = [infinity_norm(a), frob(a).upper()]
    power = a
    for exponent in [2, 4, 8, 16]:
        power = power*power
        moment = power.trace().real.upper()
        if moment >= 0:
            bounds.append(moment.root(exponent).upper())
    return min(bounds)


def ldl_positive(a):
    """Verified LDL* test for a represented Hermitian matrix."""
    n = a.nrows()
    L = acb_mat(n, n)
    ds = []
    for j in range(n):
        pivot = a[j, j].real
        for k in range(j):
            pivot -= abs(L[j, k])**2*ds[k]
        if not pivot > 0:
            return False, ds
        ds.append(pivot)
        L[j, j] = 1
        for i in range(j+1, n):
            value = a[i, j]
            for k in range(j):
                value -= L[i, k]*L[j, k].conjugate()*ds[k]
            L[i, j] = value/pivot
    return True, ds


def certified_psd_margin(blocks, gershgorin):
    """Use a numerical margin only as a candidate for a rigorous LDL* test."""
    mins = []
    for C in blocks:
        cmid = np.array([[complex(C[i, j].mid()) for j in range(15)]
                        for i in range(15)])
        mins.append(float(np.linalg.eigvalsh(cmid)[0]))
    candidate = math.floor(max(0, min(mins))*0.95*10**6)
    I = acb_mat(np.eye(15, dtype=int).tolist())
    for _ in range(10):
        mu = arb(fmpq(candidate, 10**6))
        if candidate > 0 and all(ldl_positive(C-mu*I)[0] for C in blocks):
            return max(mu.lower(), gershgorin), candidate
        candidate //= 2
    return gershgorin, None


def out(x, digits=30):
    return x.str(digits)


def kron_pauli(label):
    p = [np.eye(2), np.array([[0, 1], [1, 0]]),
         np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    a = np.ones((1, 1))
    for j in label:
        a = np.kron(a, p[j])
    return acb_mat([[acb(int(round(z.real)), int(round(z.imag))) for z in row] for row in a])


class Model:
    def __init__(self, precision=256):
        ctx.prec = precision
        self.n = 5
        self.d = 32
        self.labels = []
        self.coeffs = []
        h_path = HERE / "hamiltonian.json"
        raw = json.loads(h_path.read_text())
        witness_path = HERE / "design_witness.json"
        witness = json.loads(witness_path.read_text())
        self.I = acb_mat(np.eye(32, dtype=int).tolist())
        self.H = acb_mat(32, 32)
        self.paulis = []
        for key, value in raw.items():
            label = json.loads(key)
            pauli = kron_pauli(label)
            self.labels.append(label)
            self.coeffs.append(value)
            self.paulis.append(pauli)
            self.H += value * pauli
        self.Fs = []
        for b in range(4):
            self.Fs.append([kron_pauli([0]*b + [a//4, a % 4] + [0]*(3-b))
                            for a in range(1, 16)])
        self.directions = []
        self.y = []
        for label, h, P in zip(self.labels, self.coeffs, self.paulis):
            first = next(i for i, v in enumerate(label) if v)
            b = min(first, 3)
            local = label[b:b+2]
            j = 0 if local[0] else 1
            f, g = [0, 0], local.copy()
            f[j] = local[j] % 3 + 1
            g[j] = (local[j]+1) % 3 + 1
            fi, gi = 4*f[0]+f[1]-1, 4*g[0]+g[1]-1
            F, G = self.Fs[b][fi], self.Fs[b][gi]
            if not (F*G-acb(0, 1)*P).contains(acb_mat(32, 32)):
                raise ArithmeticError('The exact Pauli direction identity failed.')
            self.directions.append((b, fi, gi, F, G, P))
            touched = sum(bool(label[k] or label[k+1]) for k in range(4))
            self.y.append(-16*touched*h)

        # Exact rational interpolation nodes. Their proximity to energies only
        # improves conditioning; polynomial independence is exact for distinct nodes.
        node_den = witness['nodes']['denominator']
        nodes = witness['nodes']['numerators']
        if len(nodes) != 32 or len(set(nodes)) != 32:
            raise ValueError('The 32 rational interpolation nodes must be distinct.')
        self.nodes = {"denominator": node_den, "numerators": nodes}
        powers = [self.I]
        for _ in range(31):
            powers.append(powers[-1]*self.H)
        self.Bs = []
        for j in range(31):
            coeff = [1]
            den = 1
            for k in range(32):
                if k == j:
                    continue
                nxt = [0]*(len(coeff)+1)
                for r, c in enumerate(coeff):
                    nxt[r] -= nodes[k]*c
                    nxt[r+1] += node_den*c
                coeff = nxt
                den *= nodes[j]-nodes[k]
            B = acb_mat(32, 32)
            for c, power in zip(coeff, powers):
                B += power*arb(fmpq(c, den))
            self.Bs.append(B)
        self.Bflat = acb_mat(31, 1024,
             [B[j, i] for B in self.Bs for i in range(32) for j in range(32)])
        A0, _ = self.balance(self.I)
        r_den = witness['right_inverse_denominator']
        self.r_nums = witness['right_inverse_numerators']
        self.r_den = r_den
        self.R = arb_mat(51, 31, [arb(fmpq(v, r_den)) for row in self.r_nums for v in row])
        self.right_inverse_residual = infinity_norm(A0*self.R-arb_mat(np.eye(31, dtype=int).tolist()))
        if not self.right_inverse_residual < arb("1/1000000"):
            raise ArithmeticError('The rational right-inverse residual failed verification.')

    def delta(self, X, direction):
        _, _, _, F, G, P = direction
        return (acb(0, 1)*(G*X*F-F*X*G) + P*X+X*P)/4

    def depolarizer(self, X):
        result = -60*X
        for fs in self.Fs:
            for F in fs:
                result += F*X*F
        return result

    def balance(self, X):
        deltas = [self.delta(X, d) for d in self.directions]
        columns = acb_mat(1024, 51,
                 [D[i, j] for i in range(32) for j in range(32) for D in deltas])
        A = real_matrix(self.Bflat*columns)
        D0 = self.depolarizer(X)
        fvec = acb_mat(1024, 1, [D0[i, j] for i in range(32) for j in range(32)])
        f = real_matrix(self.Bflat*fvec)
        return A, f

    def certify(self, beta):
        # Unnormalized exp is sufficient for secular balance.
        X = (-beta*self.H).exp()
        A, f = self.balance(X)
        M = A*self.R
        xlin = arb_mat(51, 1, [beta*y for y in self.y])
        residual = f+A*xlin
        correction = M.solve(-residual, algorithm="precond")
        x = xlin+self.R*correction
        result, bounds = self.coefficient_bounds(x)
        rho = X/X.trace()
        drift = self.depolarizer(rho)
        for a, direction in enumerate(self.directions):
            drift += x[a, 0]*self.delta(rho, direction)
        drift_norm = frob(drift).upper()
        result.update({"beta_ball": out(beta),
                       "drift_hilbert_schmidt_upper": out(drift_norm),
                       "balance_inverse_frobenius_upper": out(frob(M.inv()).upper())})
        return result, (*bounds, drift_norm)

    def coefficient_bounds(self, x):
        if not all(x[i, 0].is_finite() for i in range(51)):
            raise ArithmeticError('The coefficient solve did not produce finite enclosures.')
        absx = [abs(x[i, 0]).upper() for i in range(51)]
        Crows = [[[arb(0) for _ in range(15)] for _ in range(15)] for _ in range(4)]
        Cs = [acb_mat(np.eye(15, dtype=int).tolist()) for _ in range(4)]
        K = acb_mat(32, 32)
        for a, direction in enumerate(self.directions):
            b, fi, gi, _, _, P = direction
            Crows[b][fi][gi] += absx[a]/4
            Crows[b][gi][fi] += absx[a]/4
            Cs[b][fi, gi] -= acb(0, 1)*x[a, 0]/4
            Cs[b][gi, fi] += acb(0, 1)*x[a, 0]/4
            K += x[a, 0]*P
        rowmax = max(sum(row, arb(0)).upper() for block in Crows for row in block)
        gershgorin = (1-rowmax).lower()
        cp_margin, ldl_numerator = certified_psd_margin(Cs, gershgorin)
        xnorm = sum((v*v for v in absx), arb(0)).sqrt().upper()
        xone = sum(absx, arb(0)).upper()
        K_norm = certified_hermitian_norm(K)
        coercivity = (16-K_norm/2).lower()
        Dnorm = (64+xone).upper()
        return {
            "cp_margin_lower": out(cp_margin),
            "cp_gershgorin_margin": out(gershgorin),
            "ldl_test_margin_numerator": ldl_numerator,
            "ldl_test_margin_denominator": 10**6,
            "K_operator_norm_upper": out(K_norm),
            "coercivity_lower": out(coercivity),
            "dissipator_norm_upper": out(Dnorm),
            "coefficient_l2_upper": out(xnorm),
            "coefficient_l1_upper": out(xone),
            "coefficients": [out(x[i, 0], 50) for i in range(51)],
            "passed": bool(cp_margin > 0 and coercivity > 0),
        }, (cp_margin, coercivity, Dnorm)

    def spectrum_certificate(self):
        eigs = sorted((z.real for z in self.H.eig(algorithm="rump")),
                      key=lambda z: float(z.mid()))
        gap = min((eigs[j+1]-eigs[j]).lower() for j in range(31))
        spread = (eigs[-1]-eigs[0]).upper()
        if not gap > 0:
            raise ArithmeticError('The energy spectrum was not certified simple.')
        return {"energy_balls": [out(e, 50) for e in eigs],
                "minimum_energy_gap_lower": out(gap),
                "hamiltonian_commutator_norm_upper": out(spread)}, (gap, spread)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", default="3/1000")
    parser.add_argument("--radius", default="0")
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", default="construction_point_certificate.json")
    args = parser.parse_args()
    start = time.time()
    model = Model(args.precision)
    beta = arb(args.beta, args.radius)
    result, bounds = model.certify(beta)
    spectrum, (gap, spread) = model.spectrum_certificate()
    cp, delta, D, drift = bounds
    if result["passed"]:
        factor = (1+D/delta).upper()
        eta_max = (gap/(2*D*factor)).lower()
        trace_error_slope = (arb(32).sqrt()*factor*drift/gap).upper()
        result["eta_max_for_error_bound"] = out(eta_max)
        result["half_trace_error_slope_upper"] = out(trace_error_slope)
        result["generator_norm_for_eta_le_one_upper"] = out((spread+D).upper())
    result.update({"precision_bits": args.precision,
                   "nodes": model.nodes,
                   "right_inverse_denominator": model.r_den,
                   "right_inverse_numerators": model.r_nums,
                   "right_inverse_residual_at_zero_upper": out(model.right_inverse_residual),
                   "spectrum_certificate": spectrum,
                   "elapsed_seconds": time.time()-start})
    path = HERE/args.output
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in
          {"coefficients", "nodes", "right_inverse_numerators", "spectrum_certificate"}}, indent=2))


if __name__ == "__main__":
    main()

"""Independent reconstruction from the authoritative Pauli-coefficient JSON.

No saved matrix, NumPy archive, or matrix-construction routine is imported.
The rank witness is checked by a selected exact minor using vectorized field
elimination; the characteristic polynomial is recomputed symbolically.
"""
import itertools
import json
from pathlib import Path
import time
import sys
import numpy as np
import os
# Keep exact SymPy arithmetic independent of the optional Arb/FLINT backend.
# SymPy 1.14 with python-flint 0.9 cannot order repeated-degree nmod factors.
os.environ["SYMPY_GROUND_TYPES"] = "python"
import sympy as sp

base = Path(__file__).resolve().parent / 'data'
p, imaginary_unit, n = 65537, 256, 5

def require(condition, message):
    if not condition:
        raise RuntimeError(message)
local = [np.eye(2, dtype=np.int64),
         np.array([[0, 1], [1, 0]], dtype=np.int64),
         np.array([[0, -imaginary_unit], [imaginary_unit, 0]], dtype=np.int64) % p,
         np.diag([1, -1]).astype(np.int64) % p]
exact_local = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]),
               sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]
coeff = [(tuple(json.loads(k)), int(v)) for k, v in
         json.loads((base / 'hamiltonian.json').read_text()).items()]

allowed_labels = set()
for site in range(n):
    for a in range(1, 4):
        q = [0] * n; q[site] = a; allowed_labels.add(tuple(q))
for site in range(n - 1):
    for a, b in itertools.product(range(1, 4), repeat=2):
        q = [0] * n; q[site:site + 2] = [a, b]; allowed_labels.add(tuple(q))
require({label for label, _ in coeff} == allowed_labels, 'Hamiltonian must list exactly the 51 allowed local Pauli slots')
require(sp.isprime(p) and imaginary_unit**2 % p == p - 1, 'Invalid exact field')

def pauli(label):
    result = np.ones((1, 1), dtype=np.int64)
    for digit in label:
        result = np.kron(result, local[digit]) % p
    return result

H = np.zeros((32, 32), dtype=np.int64)
H_exact = sp.zeros(32)
for label, value in coeff:
    H = (H + value * pauli(label)) % p
    if value:
        H_exact += value * sp.kronecker_product(*(exact_local[a] for a in label))
require(H_exact == H_exact.conjugate().T, "Exact certificate check failed: H_exact == H_exact.conjugate().T")
require(sp.trace(H_exact) == 0, "Exact certificate check failed: sp.trace(H_exact) == 0")

# Multiply 31 times, independently of the binary-power construction.
sigma = np.eye(32, dtype=np.int64)
for _ in range(31):
    sigma = (sigma @ H) % p
labels = list(itertools.product(range(4), repeat=n))
r = np.array([np.sum(pauli(q) * sigma.T) % p for q in labels], dtype=np.int64)
lookup = {q: i for i, q in enumerate(labels)}
A = np.zeros((1023, 960), dtype=np.int64)
col = 0
for edge in range(4):
    for mu in itertools.product(range(4), repeat=2):
        if mu == (0, 0):
            continue
        for nu in itertools.product(range(4), repeat=2):
            for outside in itertools.product(range(4), repeat=3):
                q = list(outside[:edge]) + list(mu) + list(outside[edge:])
                z = list(outside[:edge]) + list(nu) + list(outside[edge:])
                A[lookup[tuple(q)] - 1, col] = r[lookup[tuple(z)]]
            col += 1
require(col == 960, "Exact certificate check failed: col == 960")

def determinant_mod(M):
    M = M.copy() % p
    size = M.shape[0]
    answer = 1
    for k in range(size):
        nonzero = np.flatnonzero(M[k:, k])
        if not len(nonzero):
            return 0
        pivot_row = k + int(nonzero[0])
        if pivot_row != k:
            M[[k, pivot_row]] = M[[pivot_row, k]]
            answer = -answer
        pivot = int(M[k, k])
        answer = (answer * pivot) % p
        if k + 1 < size:
            factors = (M[k + 1:, k] * pow(pivot, -1, p)) % p
            M[k + 1:, k + 1:] = (M[k + 1:, k + 1:] -
                factors[:, None] * M[k, k + 1:][None, :]) % p
            M[k + 1:, k] = 0
    return answer

certificate = json.loads((base / 'evaluation-minor.json').read_text())
t0 = time.monotonic()
minor_det = determinant_mod(A[np.ix_(certificate['rows'], certificate['columns'])])
require(len(certificate['rows']) == len(certificate['columns']) == 923, "Exact certificate check failed: len(certificate['rows']) == len(certificate['columns']) == 923")
require(minor_det == 12689, "Exact certificate check failed: minor_det == 12689")
print('Independent 923-minor determinant:', minor_det, file=sys.stderr, flush=True)

x = sp.symbols('x')
f = sp.Poly(H_exact.charpoly(x).as_expr(), x, domain=sp.ZZ)
galois = json.loads((base / 'galois.json').read_text())
require([int(v) for v in f.all_coeffs()] == galois['charpoly_coefficients'], "Exact certificate check failed: [int(v) for v in f.all_coeffs()] == galois['charpoly_coefficients']")
factor_report = []
expected_degrees = {19: [1, 31], 43: [1, 2, 7, 11, 11], 373: [32]}
for prime in [19, 43, 373]:
    factors = sp.factor_list(f, modulus=prime)[1]
    require(all(multiplicity == 1 for _, multiplicity in factors), "Exact certificate check failed: all(multiplicity == 1 for _, multiplicity in factors)")
    degrees = sorted(factor.degree() for factor, _ in factors)
    require(degrees == expected_degrees[prime], "Exact certificate check failed: degrees == expected_degrees[prime]")
    factor_report.append({'prime': prime, 'degrees': degrees, 'squarefree': True})
    print('Independent factors:', prime, degrees, file=sys.stderr, flush=True)

# Independent full-rank diagonal-expectation witness, using direct traces.
local_paulis = [pauli(label) for label, _ in coeff]
moments = []
power = np.eye(32, dtype=np.int64)
for _ in range(31):
    power = (power @ H) % p
    moments.append([int(np.sum(P * power.T) % p) for P in local_paulis])
moments = np.array(moments, dtype=np.int64)
diag_cert = json.loads((base / 'diagonal-minor.json').read_text())
diagonal_det = determinant_mod(moments[np.ix_(diag_cert['rows'], diag_cert['columns'])])
require(len(diag_cert['rows']) == 31 and diagonal_det == 48876, "Exact certificate check failed: len(diag_cert['rows']) == 31 and diagonal_det == 48876")
print('Independent 31-minor determinant:', diagonal_det, file=sys.stderr, flush=True)

report = {'source': 'Pauli coefficient JSON only', 'prime': p,
          'evaluation_minor_order': 923, 'evaluation_minor_determinant': minor_det,
          'characteristic_polynomial_recomputed_and_matched': True,
          'factorizations': factor_report,
          'diagonal_span_minor_order': 31, 'diagonal_span_minor_determinant': diagonal_det,
          'elapsed_seconds': time.monotonic() - t0}

print(json.dumps(report), flush=True)

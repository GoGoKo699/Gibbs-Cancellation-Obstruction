# Certified intrinsic evaluation bounds

This small verifier supplies conservative, rigorously enclosed constants for
the five-qubit local Gibbs obstruction. It does not estimate a matrix rank by
thresholding floating-point singular values.

## Reproduce

Use Python3 with `python-flint==0.9.0`:

```sh
python -m pip install -r requirements.txt
python verify_gap_bound.py --beta 3/1000 --output result-beta003.json
python verify_gap_bound.py --beta 1/100 --output result-beta01.json
```

The default input directory is `data` beside the script. `--data-dir` accepts
another directory containing the same two input filenames. `--output` is
optional; without it the report is printed without writing a file. The
standard import is `from flint import ...`; no workspace-specific paths,
NumPy archives, numerical eigenvectors, or SciPy routines are required.

The input `hamiltonian.json` specifies the51 onsite/nearest-neighbor Pauli
coefficients. The input `quantitative-minor.json` specifies923 output rows
and923 raw map columns. Rows were selected using a numerical heuristic for
conditioning, but their validity is established anew by a certified Arb
inverse at each requested temperature. A numerical choice of a witness is
not accepted as its verification.

At256 bits the two recorded runs certify the safe rounded inequalities

| Exact inverse temperature | Lower bound on intrinsic s_rho | Coefficient C in gap <= C J epsilon |
| --- | ---: | ---: |
| 3/1000 | 9.7410e-22 | 2.0532e21 |
| 1/100 | 4.1512e-18 | 4.8179e17 |

Here J is the induced Hilbert-Schmidt norm of the entire generator and
epsilon is half trace distance to the target. The JSON results retain more
digits and explicitly directed decimal bounds. These constants are very
loose and large. They certify the asymptotic obstruction, not a useful
finite-error experimental penalty or an efficient sampler.

## Why the normalization is intrinsic

Let B_j be a raw column superoperator: one local two-qubit Pauli matrix unit
on a chosen bond, extended by the identity superoperator on the other three
qubits. In the normalized global Pauli basis P/sqrt32, a single B_j has64
unit entries and Frobenius norm8. Within each bond, the240 such maps are
orthogonal. Maps on different bonds need not be orthogonal, even when the
bonds are disjoint.

Let R synthesize a superoperator from its960 raw coefficients. Grouping
coefficients by bond and applying Cauchy-Schwarz gives exactly

    ||R c||_F <= sum_b 8 ||c_b||_2 <= 16 ||c||_2.

Thus the raw frame operator has upper bound256. A raw evaluation matrix T
uses the coordinates Tr(P L(rho)), whose Euclidean norm is sqrt32 times
the Hilbert-Schmidt norm of L(rho). Neither normalization may be omitted.

For comparison, if G=R^dagger R=Q Lambda Q^T on its924-dimensional positive
range, an orthonormal intrinsic evaluation matrix is

    E_intrinsic = T Q Lambda^(-1/2) / sqrt32.

Its least positive singular value is s_rho. The verifier avoids computing
this ill-conditioned singular value or the whitening matrix.

## Why a minor inverse gives a lower bound

The local map space V has dimension924. The nonzero Hamiltonian
commutator D_H is in the evaluation kernel. Suppose M is a923-by923 minor
of T, using selected raw maps B_C. A certified inverse proves rank at
least923. The commutator gives rank at most923, so the kernel in V is
exactly span(D_H), and the selected columns span the evaluation image.

For A in V perpendicular to D_H, solve

    c = M^(-1) [selected raw coordinates of A(rho)].

Then B_C c and A have the same full evaluation: their evaluations lie in
the923-dimensional image on which the selected rows are injective. Their
difference is a Hamiltonian commutator. Orthogonal projection therefore
gives

    ||A||_F <= ||B_C c||_F
             <= 16 sqrt32 ||M^(-1)||_2 ||A(rho)||_2.

Consequently

    s_rho >= 1 / (16 sqrt32 ||M^(-1)||_2)
           >= 1 / (16 sqrt32 ||M^(-1)||_F).

The verifier encloses every entry of M^(-1), sums squares of absolute
entry upper bounds, and rounds the resulting Frobenius bound upward.
It then rounds the reciprocal lower bound downward. Combining this with
the independently proved stability inequality yields

    gap(L) <= (2/s_rho) J epsilon.

## Interval and provenance checks

The Hamiltonian is reconstructed using integer bit operations for Pauli
actions. Its Hermiticity, tracelessness, nonzero value, and allowed support
are checked. The inverse temperature is parsed as an exact rational.
Arb encloses the32-by32 matrix exponential and positive partition
function, so the evaluation entries enclose the true Gibbs values.
Hermiticity makes each Pauli trace exactly real; its imaginary enclosure
is checked to contain zero. Normalization fixes the identity coefficient
to exactly one.

`arb_mat.inv()` must certify the selected inverse, and every inverse
entry must be finite. Failure raises an exception rather than issuing a
rank claim. All subsequent norm operations retain Arb enclosures. The
reported short decimal bounds are checked in the stated direction with
Arb before printing. Input SHA256 hashes, working precision, and
python-flint version are retained in each report.

The public verifier concerns two finite-temperature instances. The
Galois/Lindemann-Weierstrass proof, analytic genericity, positivity of the
matching baths, and the all-sufficiently-small-temperature quantifier are
separate analytical parts of the full account. No arbitrary-size or
uniform-temperature conclusion follows from these two runs.

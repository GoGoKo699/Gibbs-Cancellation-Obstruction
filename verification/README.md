# Reproducing the scientific certificates

The repository separates three kinds of evidence: exact integer/finite-field certificates, rigorous Arb enclosures, and the analytical arguments that turn those calculations into generic and asymptotic theorems. Floating-point rank estimates are not used as proof.

## Run the complete computational verification

From the repository root, with Python 3.12 and the pinned package versions:

```sh
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python verification/run_all.py
```

The runner writes reports and logs under the ignored directory `verification/local-output/`. It fails if any subprocess fails, any reported certificate fails, or the three Hamiltonian inputs differ. A successful result checks the finite certificates; it does not mechanically prove the analytical Galois, transcendence, genericity, or physical arguments.

The full run typically takes a few minutes or less on a modern CPU. No GPU, proprietary solver, cloud service, saved eigenbasis or network connection is needed after installing dependencies. The recorded environment used Python 3.12.14, NumPy 2.3.5, SymPy 1.14.0 and python-flint 0.9.0. Runtime is informational and is not a scientific performance claim.

## Exact algebraic inputs

```sh
python verification/exact_certificate.py
```

This independently reconstructs the 32-by-32 integer Hamiltonian from its Pauli coefficients. It recomputes the selected 923-minor at the polynomial state $`H_0^{31}`$, the full integer characteristic polynomial, its modular factor patterns, and the 31-dimensional population-control minor.

| Certificate | Reproduced value | Role |
|---|---|---|
| Selected evaluation minor modulo 65537 | 12689 | Nonzero homogeneous polynomial on spectral weights |
| Characteristic polynomial modulo 19 | Factor degrees 1, 31 | A 31-cycle in the Galois group |
| Characteristic polynomial modulo 43 | Factor degrees 1, 2, 7, 11, 11 | A power is a transposition |
| Characteristic polynomial modulo 373 | Irreducible of degree 32 | Transitivity of the Galois action |
| Selected population-control minor modulo 65537 | 48876 | All 31 trace-zero population directions are accessible |

The [written proof](../science/gibbs-certificate.md) supplies the indispensable steps from these exact facts to an exact Gibbs kernel and genericity. `data/` contains the authoritative Hamiltonian, selected indices and expected algebraic data. Saved expected data are recomputed and compared, not trusted as premises.

## Intrinsic gap/error constants

```sh
python verification/gap/verify_gap_bound.py --beta 3/1000 --output verification/local-output/gap-beta003.json
python verification/gap/verify_gap_bound.py --beta 1/100 --output verification/local-output/gap-beta01.json
```

The [gap package](gap/README.md) reconstructs the true Gibbs evaluation minor and certifies its inverse with Arb. The frame bound and Pauli normalization convert that inverse into a lower bound on the intrinsic evaluation singular value. It records input hashes and directed decimal bounds. `gap/data/result-*.json` retains the independently rerun reference outputs.

## Positive reservoirs and a continuous construction interval

```sh
python verification/construction/certify_construction.py --beta 3/1000 --output verification/local-output/construction-beta003.json
python verification/construction/certify_construction.py --beta 1/100 --output verification/local-output/construction-beta01.json
python verification/construction/certify_interval.py --cells 128 --output verification/local-output/construction-interval.json
```

The [construction package](construction/README.md) gives the full exact coefficient prescription and its derivation. Rational polynomial test matrices impose exact population balance without numerical energy eigenvectors. Interval linear solves, positive coefficient matrices, dissipative coercivity and spectral enclosures prove the stated error and gap bounds. The interval run covers every rational cell from zero to $`1/100`$ with a rigorous exponential Taylor remainder.

The continuous interval concerns the construction and coercivity. It does not certify full evaluation rank at every real temperature in that interval. The two rational point examples separately satisfy the exact obstruction theorem.

## Ground-state marginals, thermal deficit and cold population forms

```sh
python verification/ground-thermal/certify_ground_thermal.py --output verification/local-output/ground-thermal.json
```

The [ground/thermal package](ground-thermal/README.md) uses the authoritative `data/hamiltonian.json` directly. Verified 256-bit Rump eigenvalue/eigenvector enclosures certify all 32 energies and all nine complete marginal spectra. Arb Boltzmann sums give thermal deficits and the inherited stationary error floor. Interval LDL* certifies four strictly negative bond-population forms at $`\beta=12/5`$; the written monotonicity argument extends exact exclusion to every real colder inverse temperature. All load-bearing checks remain active under `python -O`.

The runner includes this as its seventh named check and records the result's SHA256, acceptance conditions and input hash. The [full mathematical account](../science/finite-temperature-feasibility.md) distinguishes this cold witness, the inherited pure-target approximation bound, the existing exact evaluation-rank certificate and the positive high-temperature reservoir interval. The sufficient exclusion endpoint is not an exact transition.

## Reading and modifying reports

The construction reports use Arb's midpoint-plus-radius notation. A printed ball encloses a value; it is not a decimal equality. Use the safely rounded bounds in the [quantitative account](../science/quantitative-witness.md), or inspect the directed endpoints in the code. An enclosure failure should remain a failure until precision or the mathematical bound is improved.

The Hamiltonian and rational design witnesses are sufficient to reproduce all results. Exploratory arrays, numerical searches, full literature PDFs and private research records are not dependencies. When changing a mathematical input, rerun the affected certificate and update both the account and its recorded output. A previous passing report does not validate changed bytes.

## Actual hosted mathematics

The separate [hosted rendering check](hosted/README.md) compares every expression on the commit-pinned GitHub pages with its source at wide and narrow viewports, and retains screenshots for visual review. It is independent of the seven scientific certificate checks. A rendering pass does not establish a mathematical theorem; a certificate pass does not establish readable rendering.

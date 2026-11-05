# Explicit, certified local reservoir construction

This directory makes the high-temperature matching construction quantitative
for the fixed five-qubit Hamiltonian in `hamiltonian.json`. All operations are
on the original five qubits. Every individual jump is supported on one of the
four adjacent bonds. No auxiliary sites, detailed-balance condition, or
termwise stationarity is used.

The calculations certify a positive local reservoir throughout
**0 ≤ β ≤ 1/100**. They also give explicit stationary-error and relaxation-rate
bounds at **β = 3/1000** and **β = 1/100**. The interval is a certificate of the
construction only. The separate Gibbs evaluation-rank theorem applies to
these two rational temperatures, but this directory does **not** certify that
rank on the entire real interval.

## 1. Certified conclusions

Write

```math
\rho_\beta=\frac{e^{-\beta H_0}}{\mathrm{Tr}e^{-\beta H_0}},\qquad
\mathcal L_{\beta,\eta}=-i[H_0,\cdot]+\eta\mathcal D_\beta.
```

The construction below specifies every coefficient of
$`\mathcal D_\beta`$. Let $`\sigma_{\beta,\eta}`$ be its full generator's
stationary state, and let

```math
\gamma(\mathcal L)=\min_{\lambda\in\mathrm{spec}\mathcal L,\lambda\ne0}
(-\mathrm{Re}\lambda).
```

The following numbers are deliberately rounded **outward** from the Arb
certificates. Operator norms of matrices are denoted $`\lVert\cdot\rVert_\infty`$;
$`\lVert\mathcal A\rVert_{2\to2}`$ is the norm induced by the unnormalized
Hilbert–Schmidt norm $`\lVert X\rVert_2=\sqrt{\mathrm{Tr}X^\dagger X}`$.
Trace distance means $`\tfrac12\lVert\sigma-\rho\rVert_1`$.

| Certified quantity | β = 0.003 | β = 0.01 |
|---|---:|---:|
| Each bond coefficient matrix $`C_b\succeq\mu I_{15}`$ | $`\mu\ge0.7234`$ | $`\mu\ge0.2019`$ |
| HS coercivity $`\delta`$ on traceless matrices | $`\delta\ge13.900`$ | $`\delta\ge8.859`$ |
| $`\lVert \mathcal D_\beta\rVert_{2\to2}\le M`$ | $`M\le75.580`$ | $`M\le102.952`$ |
| $`\lVert \mathcal D_\beta(\rho_\beta)\rVert_2\le r`$ | $`r\le0.014963`$ | $`r\le0.174897`$ |
| Range of $`\eta`$ for the error bound | $`0<\eta\le0.000548`$ | $`0<\eta\le0.000205`$ |
| Stationary error | $`\tfrac12\lVert \sigma-\rho\rVert_1\le1.022\eta`$ | $`\tfrac12\lVert \sigma-\rho\rVert_1\le23.411\eta`$ |
| Gap for every $`\eta>0`$ | $`\gamma\ge13.900\eta`$ | $`\gamma\ge8.859\eta`$ |
| $`\lVert \mathcal L_{\beta,\eta}\rVert_{2\to2}`$ for $`0<\eta\le1`$ | $`\le142.470`$ | $`\le169.843`$ |

For every real $`0\le\beta\le0.01`$, the interval certificate gives the
uniform, conservatively rounded bounds

```math
C_b(\beta)\succeq0.0512 I_{15},\qquad
\mathrm{Re}\langle X,\mathcal D_\beta X\rangle
\le-4.12\lVert X\rVert_2^2\quad(\mathrm{Tr}X=0),\qquad
\lVert\mathcal D_\beta\rVert_{2\to2}\le109.645.
```

The finite-dimensional certificates are computational proofs conditional on
the correctness of Python, NumPy's exact small-integer Pauli construction,
and the FLINT/Arb ball-arithmetic implementation. Floating-point eigenvalues
and pseudoinverses are **not** accepted as proof. They only proposed exact
rational conditioning data or a candidate positivity margin. Every
load-bearing matrix solve, inequality, and positivity test is verified with
outward-rounded balls at 256-bit working precision.

## 2. Exact coefficient prescription

### 2.1 Bases and local dissipators

The Hamiltonian file lists the 51 onsite and adjacent-pair Pauli strings
$`P_a`$, with integer coefficients $`h_a`$, in the order used by the code:

```math
H_0=\sum_{a=1}^{51}h_aP_a.
```

On each bond $`b`$, use the 15 nonidentity two-qubit Paulis
$`F_{b,u}`$, ordered by the integer $`4p+q`$, with
$`p,q\in\{0,1,2,3\}`$ representing $`I,X,Y,Z`$. Define

```math
\mathcal D_C(X)=\sum_{b=0}^{3}\sum_{u,v=1}^{15}
C_{b,uv}\left(F_{b,u}XF_{b,v}
-\frac12\{F_{b,v}F_{b,u},X\}\right).
```

For each $`P_a`$, pick its leftmost nonidentity site $`s`$ and bond
$`b=\min(s,3)`$. Within that bond choose Paulis $`F_a,G_a`$ with
$`F_aG_a=iP_a`$: at the first nonidentity local site, replace the Pauli
index $`p`$ by $`p\bmod3+1`$ in $`F_a`$, and by
$`(p+1)\bmod3+1`$ in $`G_a`$. The other local factor of $`F_a`$ is
identity and that of $`G_a`$ is retained from $`P_a`$.

Add $`-ix_a/4`$ to the $`(F_a,G_a)`$ coefficient and $`+ix_a/4`$ to
the $`(G_a,F_a)`$ coefficient, starting from $`C_b=I_{15}`$. The resulting
direction is

```math
\Delta_a(X)=\frac i4(G_aXF_a-F_aXG_a)+\frac14(P_aX+XP_a),
\qquad \Delta_a(I)=P_a.
```

Thus the reservoir is the explicit 51-parameter family

```math
\mathcal D_x=\mathcal D_0+\sum_a x_a\Delta_a,
\qquad \mathcal D_0=\sum_{b,u}\mathcal D[F_{b,u}].
```

If desired, conventional jump operators follow from any positive
factorization of each $`C_b`$: for an eigendecomposition
$`C_b=\sum_j\lambda_{bj}v_{bj}v_{bj}^\dagger`$, take
$`J_{bj}=\sqrt{\lambda_{bj}}\sum_u(v_{bj})_uF_{b,u}`$.
This step is a representation change, not an additional existence condition.

### 2.2 Secular equations without numerical eigenvectors

The exact rational numbers $`q_0,\ldots,q_{31}`$ in
`design_witness.json` are distinct. Define degree-31 Lagrange polynomials

```math
B_j(H_0)=\prod_{k\ne j}\frac{H_0-q_kI}{q_j-q_k},\qquad 0\le j<31.
```

The nodes approximate the energy eigenvalues only to improve conditioning.
Their proximity is not used in the proof. Since the spectrum of $`H_0`$ is
simple, the 32 matrices $`I,B_0,\ldots,B_{30}`$ form a basis of its
commutant: the full 32 Lagrange polynomials form a basis of degree-at-most-31
polynomials and sum to one, and evaluation at a simple 32-point spectrum is
injective on that polynomial space.

Let $`X_\beta=e^{-\beta H_0}`$, and define the real matrices

```math
A_{ja}(\beta)=\mathrm{Tr}[B_j\Delta_a(X_\beta)],\qquad
f_j(\beta)=\mathrm{Tr}[B_j\mathcal D_0(X_\beta)].
```

These traces are exactly real because both factors are Hermitian. Taking
the real component of an enclosing complex ball therefore loses no relevant
information. The 31 equations $`A(\beta)x+f(\beta)=0`$, together with
automatic trace preservation, are equivalent to

```math
\mathsf P\mathcal D_x(\rho_\beta)=0,
```

where $`\mathsf P`$ is dephasing in the exact energy eigenbasis.

The exact rational $`51\times31`$ matrix $`R`$ is also stored in
`design_witness.json`. Its infinite-temperature residual is certified as

```math
\lVert A(0)R-I_{31}\rVert_\infty<3.351\times10^{-11}.
```

Here this one norm is the maximum absolute row-sum norm. At each desired
$`\beta`$, invertibility of $`M(\beta)=A(\beta)R`$ is independently
verified; the small residual at zero is not extrapolated without proof.

Let $`w_a`$ be the number of chain bonds meeting the support of $`P_a`$,
and set $`y_a=-16w_ah_a`$. The exact coefficient formula is

```math
\boxed{\quad
x(\beta)=\beta y-R\,[A(\beta)R]^{-1}
\big[f(\beta)+\beta A(\beta)y\big].
\quad}
```

This is an explicit analytic finite-dimensional prescription, with no
optimization left unspecified. In particular,

```math
A(\beta)x(\beta)+f(\beta)=0
```

holds exactly. The stored coefficient balls enclose the real coefficients
defined by this formula; arbitrary choices of numbers inside those balls
need not satisfy exact secular balance.

The linear term $`\beta y`$ is useful. Since
$`\mathcal D_0(P_a)=-16w_aP_a`$,

```math
\mathcal D_0(e^{-\beta H_0})+
\beta\sum_a y_a\Delta_a(e^{-\beta H_0})=O(\beta^2).
```

The correction is therefore $`O(\beta^2)`$. This reduces the full drift
$`\lVert\mathcal D_\beta\rho_\beta\rVert_2`$, which controls the constructive
error bound below.

## 3. Positivity, coercivity, and primitive dynamics

### 3.1 Complete positivity

The code first obtains a simple Gershgorin lower bound for all $`C_b`$.
When this is weak, floating-point diagonalization proposes a rational
$`\mu`$. A fully interval-verified $`LDL^\dagger`$ factorization of
$`C_b-\mu I`$ then checks that every pivot is strictly positive. Only a
successful verified factorization permits the claim $`C_b\succeq\mu I`$.

All physical jumps remain on one bond after diagonalizing $`C_b`$.

### 3.2 Coercivity from a 32-dimensional matrix

Pauli twirling on a bond gives

```math
\mathcal D_0=16\sum_{b=0}^{3}(\mathcal R_b-\mathrm{id}),
\qquad
\mathcal R_b(X)=\frac{I_b}{4}\otimes\mathrm{Tr}_bX.
```

In the global Pauli basis this is diagonal. Every nonidentity Pauli meets at
least one bond, so $`\mathcal D_0`$ has HS coercivity 16 on traceless
matrices and induced norm 64.

The sandwich part of $`\Delta_a`$ is HS skew-adjoint. With
$`K_x=\sum_ax_aP_a`$,

```math
\frac{\mathcal D_x+\mathcal D_x^\dagger}{2}
=\mathcal D_0+\frac14\{K_x,\cdot\}.
```

Consequently

```math
\delta=16-\frac12\lVert K_x\rVert_\infty>0
```

is a valid coercivity lower bound. The script bounds $`\lVert K_x\rVert_\infty`$
by the minimum of row sums, the Frobenius norm, and

```math
\big(\mathrm{Tr}K_x^{2k}\big)^{1/(2k)},
\qquad 2k=2,4,8,16.
```

Each is rigorous because $`K_x`$ is Hermitian. Even powers and traces are
evaluated with enclosing balls. The upper endpoint is taken before a root;
the Frobenius bound sums squared entrywise absolute **upper** bounds.
Finally, $`\lVert\Delta_a\rVert_{2\to2}\le1`$, giving

```math
M=64+\sum_a|x_a|\ge\lVert\mathcal D_x\rVert_{2\to2}.
```

### 3.3 Existence, uniqueness, faithfulness, and rates

The positive $`C_b`$'s make $`\mathcal L_{\beta,\eta}`$ a GKLS
generator for every $`\eta>0`$, so it has a density-matrix stationary
state. Coercivity gives

```math
\mathrm{Re}\langle X,\mathcal L_{\beta,\eta}X\rangle
\le-\eta\delta\lVert X\rVert_2^2\qquad(\mathrm{Tr}X=0).
```

Hence the stationary state is unique, all other eigenvalues have strictly
negative real part, and

```math
\eta\delta\le\gamma(\mathcal L_{\beta,\eta})\le\eta M.
```

It is faithful. If a stationary state $`\sigma`$ had a kernel vector
$`v`$, stationarity evaluated in that vector would give
$`\sum_j\langle J_j^\dagger v,\sigma J_j^\dagger v\rangle=0`$.
The kernel would be invariant under every jump adjoint. Strict positivity
of each $`C_b`$ means the jump span contains every bond Pauli and hence all
onsite $`X`$ and $`Z`$ matrices. These generate the full matrix algebra,
which has no proper nonzero invariant subspace. This contradicts
$`\mathrm{Tr}\sigma=1`$. No extra small-$`\eta`$ restriction is
needed for faithfulness or the rate bounds.

## 4. Explicit stationary-error bound

Let $`\mathsf Q=\mathrm{id}-\mathsf P`$, and write the stationary state
as $`\sigma=\rho_\beta+u+q`$, where $`u`$ is diagonal and traceless,
and $`q`$ is off diagonal. On these two subspaces write

```math
A=\mathsf P\mathcal D_\beta\mathsf P,\quad
B=\mathsf P\mathcal D_\beta\mathsf Q,\quad
C=\mathsf Q\mathcal D_\beta\mathsf P,\quad
E=\mathsf Q\mathcal D_\beta\mathsf Q,
```

and $`D_Q=\mathsf Q(-i[H_0,\cdot])\mathsf Q`$.
Here $`A^{-1}`$ denotes only the inverse on diagonal trace-zero matrices.
Coercivity gives $`\lVert A^{-1}\rVert\le1/\delta`$. The simple spectrum gives

```math
\lVert D_Q^{-1}\rVert=\nu^{-1},\qquad
\nu=\min_{m\ne n}|E_m-E_n|.
```

Certified Rump eigenvalue enclosures for the exact integer Hamiltonian give

```math
\nu>0.5333458496,\qquad
\lVert-i[H_0,\cdot]\rVert_{2\to2}=E_{\max}-E_{\min}<66.890379.
```

Exact secular balance yields the stationary equations

```math
u=-A^{-1}Bq,\qquad
[D_Q+\eta(E-CA^{-1}B)]q=-\eta C\rho_\beta.
```

Define $`F=1+M/\delta`$ and
$`r=\lVert\mathcal D_\beta\rho_\beta\rVert_2`$. Then

```math
\lVert E-CA^{-1}B\rVert\le MF,\qquad \lVert C\rho_\beta\rVert_2=r.
```

For

```math
0<\eta\le\eta_*:=\frac{\nu}{2MF},
```

the Neumann-series inverse has norm at most $`2/\nu`$. Therefore

```math
\boxed{\quad
\frac12\lVert\sigma_{\beta,\eta}-\rho_\beta\rVert_1
\le a\eta,\qquad
a:=\frac{\sqrt{32}\,F r}{\nu}.
\quad}
```

The $`\sqrt{32}`$ factor converts HS norm to trace norm. No condition on
nonzero Bohr-frequency degeneracies is used: only distinct energies matter.

The point certificates evaluate all these bounds. For example, choosing
$`\eta=\epsilon/1.022`$ at $`\beta=0.003`$, and dividing the generator
by 142.470, gives an explicitly local generator with

```math
\lVert\mathcal L\rVert_{2\to2}\le1,\qquad
\frac12\lVert\sigma-\rho_{0.003}\rVert_1\le\epsilon,\qquad
\gamma(\mathcal L)\ge0.0954\epsilon
```

for $`0<\epsilon\le0.00056`$. At $`\beta=0.01`$, the analogous
constants give $`\gamma\ge0.0022\epsilon`$ for
$`0<\epsilon\le0.00479`$. These are constructive lower bounds on an
optimal gap, not estimates of the actual optimal prefactor.

## 5. Continuous interval certification

Passing a wide interval directly to a dense matrix exponential gives poor
enclosures. `certify_interval.py` instead expands at zero with
$`t=64\beta`$ and $`T=-H_0/64`$, and contracts every Taylor coefficient
with $`R`$ before interval evaluation. Let

```math
A_k=A[T^k],\qquad f_k=f[T^k],
```

where the square brackets mean the same linear maps of an arbitrary input
matrix used above. The degree-20 exponential approximation gives

```math
M(t)=\sum_{k=0}^{20}\frac{t^k}{k!}A_kR+\text{remainder},
```

```math
q(t)=\sum_{k=0}^{20}\frac{t^k}{k!}f_k
+\frac{t}{64}\sum_{k=0}^{20}\frac{t^k}{k!}A_ky
+\text{remainder}.
```

The degree-21 term in the second expression is retained. A certified
Hamiltonian norm bound is $`h<37.862013`$. With
$`z=0.01h`$, the uniform exponential remainder obeys

```math
\left\lVert e^{-\beta H_0}-\sum_{k=0}^{20}\frac{(-\beta H_0)^k}{k!}\right\rVert_2
\le\sqrt{32}\,e^z\frac{z^{21}}{21!}
<2.244\times10^{-28}=:\tau.
```

For $`b_i=\lVert B_i\rVert_2`$, rigorous entrywise remainder radii are

```math
|(\Delta M)_{ij}|\le b_i\tau\sum_a|R_{aj}|,\qquad
|(\Delta q)_i|\le b_i\tau(64+0.01\lVert y\rVert_1).
```

The code covers the entire interval with the 128 exact rational cells
$`[j/12800,(j+1)/12800]`$. It explicitly verifies that each input ball
contains its rational endpoints, encloses $`M,q`$ by Horner evaluation plus
the above tails, and uses the verified preconditioned solve for both
$`M^{-1}q`$ and $`M^{-1}`$. It then verifies positivity and coercivity
for the enclosing coefficient box. Every cell passed.

The interval calculation provides a single analytic family, defined by the
same exact formula in Section 2. It does not splice different reservoirs
between cells.

## 6. Reproduction and audit status

Required packages: Python 3, NumPy, and `python-flint==0.9.0`. With those
installed, from this directory run:

```bash
OPENBLAS_NUM_THREADS=1 python certify_construction.py --beta 3/1000 --output construction_beta003_certificate.json
OPENBLAS_NUM_THREADS=1 python certify_construction.py --beta 1/100 --output construction_beta001_certificate.json
OPENBLAS_NUM_THREADS=1 python certify_interval.py --cells 128 --output construction_interval_certificate.json
python make_summary.py
```

The scripts require ordinary installed imports and the bundled
`hamiltonian.json` and `design_witness.json` files. Typical measured runtime
was about two seconds per point and eleven seconds for the 128-cell
interval on this environment; runtime is not part of the certificate.

Files:

- `hamiltonian.json`: exact integer Pauli coefficients, copied unchanged from
  the original witness.
- `design_witness.json`: exact rational interpolation nodes and conditioning
  matrix; loaded on reproduction, so NumPy eigenvalue heuristics are not
  needed to regenerate these data.
- `certify_construction.py`: point construction, positivity, coercivity,
  spectral enclosures, and error/rate constants.
- `certify_interval.py`: continuous construction interval.
- `make_summary.py`: checks all conservatively rounded headline constants,
  the rational interval cover, and the normalized strength-one examples.
- `construction_beta003_certificate.json` and
  `construction_beta001_certificate.json`: point balls and complete exact
  conditioning data.
- `construction_interval_certificate.json`: all 128 cell enclosures,
  coefficient balls, margins, and exact cell endpoints.
- `summary.json`: machine-readable conservative headline constants and file
  hashes.

The independent audit agent checked the exact coefficient signs, Lagrange
basis logic, real-trace projection, matrix indexing, rational conditioning,
LDL positivity proof, Hermitian-part identity, even-moment norm bounds,
Taylor scaling and tail radii, faithfulness, and stationary-error estimate.
It reported no mathematical gap in these steps. The audit is independent
of the construction implementation, but it is not a separate clean-room
reimplementation of the entire interval calculation.

Primary numerical-method documentation:

- [python-flint real matrix operations](https://python-flint.readthedocs.io/en/latest/arb_mat.html)
- [python-flint complex matrices and certified eigenvalue isolation](https://python-flint.readthedocs.io/en/latest/acb_mat.html)

## 7. Scope and limitations

This record certifies a concrete construction on the fixed five-qubit
Hamiltonian. It does not extend the theorem to arbitrary chain lengths or
larger allowed jump supports. The no-go rank certificate, its genericity
argument, and the resulting converse rate bound are established elsewhere
in the project. The construction interval alone cannot substitute for that
rank certificate. At the two rational positive temperatures used here, the
algebraic-temperature argument supplies the required exact obstruction.

Together with that obstruction and its finite-dimensional converse, these
constructions give the asymptotic order $`\Theta(\epsilon)`$ for optimal
gap at bounded total induced HS strength at those two points. They do not
make the converse prefactor practically sharp. Independent calculations
find severe conditioning of the evaluation map; no favorable universal
constant or large-system scaling is claimed.

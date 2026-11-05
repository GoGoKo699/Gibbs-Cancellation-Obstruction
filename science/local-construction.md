# A matching construction with positive local baths

The exact obstruction leaves open whether approximate thermal states remain reachable by the same local controls. This construction answers that question at sufficiently high temperature and attains the linear accuracy–relaxation exponent.

Fix a nondegenerate five-qubit Hamiltonian $H$ and write $\Pi$ for dephasing in its energy basis. The reference witness and a generic set of nearby or unrelated Hamiltonians satisfy the diagonal-surjectivity condition below.

## Local observables control every population direction

Let $P_a$, $a=1,\ldots,51$, be the distinct on-site and adjacent-pair Pauli strings in the Hamiltonian family. Form

$$
M_{k,a}=\operatorname{Tr}(H^kP_a),\qquad k=1,\ldots,31.
$$

For $H_0$, [diagonal-minor.json](../verification/data/diagonal-minor.json) selects a 31-minor with determinant 48876 modulo 65537. Thus $M$ has rank31 over the reals.

For $H=\sum_m E_m|m\rangle\langle m|$, put $O_{m,a}=\langle m|P_a|m\rangle$. Every column sums to zero. Multiplying $O$ by the invertible 32-by-32 Vandermonde matrix of the distinct energies gives a zero first row and the matrix $M$ in its remaining rows. Hence

$$
\operatorname{rank}O=\operatorname{rank}M=31.
$$

Equivalently, $\{\Pi(P_a)\}$ spans the whole trace-zero diagonal subspace. This is a finite-dimensional controllability condition on populations, not a claim that all diagonal operators are themselves local.

## Positive coefficient matrices

For each bond $b$, take the 15 nonidentity Hermitian two-qubit Paulis $F_{b,a}$. A Hermitian positive semidefinite coefficient matrix $C_b$ defines

$$
\mathcal D_C(A)
=\sum_b\sum_{a,c}(C_b)_{ac}
\left(
F_{b,a}AF_{b,c}
-\frac12\{F_{b,c}F_{b,a},A\}
\right).
$$

Diagonalizing each $C_b$ produces jump operators supported on that bond. Take the interior reference point $C_{0,b}=I_{15}$. Its dissipator is a sum of local Pauli depolarizers and satisfies $\mathcal D_0(I)=0$.

Every local Pauli direction can be produced as a first-order drift at the maximally mixed state. To see this, choose anticommuting bond Paulis $F,G$ with $FG=iP$. Set

$$
(\delta C)_{FG}=-i/4,\qquad
(\delta C)_{GF}=i/4.
$$

Then

$$
\mathcal D_{\delta C}(I)
=\sum_{a,c}(\delta C)_{ac}[F_a,F_c]=P.
$$

The perturbation $\delta C$ is not required to be positive by itself. A sufficiently small perturbation of the strictly positive $C_0$ remains positive.

## Exact secular balance

Choose 31 coefficient perturbations $C^{(r)}$ whose dephased drifts at $I/32$ form a basis of the trace-zero diagonal subspace. Define

$$
F_\beta(C)=\Pi\mathcal D_C(\rho_\beta),\qquad
A_\beta x=F_\beta\left(\sum_{r=1}^{31}x_rC^{(r)}\right).
$$

The matrix $A_0$ is invertible by diagonal surjectivity. Both $A_\beta$ and $F_\beta(C_0)$ are analytic in $\beta$. Therefore, for sufficiently small $|\beta|$,

$$
x(\beta)=-A_\beta^{-1}F_\beta(C_0),\qquad
C_\beta=C_0+\sum_rx_r(\beta)C^{(r)}
$$

are well defined and obey

$$
\Pi\mathcal D_\beta(\rho_\beta)=0,
\qquad C_\beta=C_0+O(\beta)>0.
$$

Here $\mathcal D_\beta=\mathcal D_{C_\beta}$. The equation fixes the populations in the energy basis. It does not impose $\mathcal D_\beta(\rho_\beta)=0$; an off-diagonal drift remains and causes the finite-dissipation bias.

The population-balance approach uses the established weak-coupling thermalization condition of [Tupkary et al.](../references/related-work.md#boundary-thermalization-and-weak-coupling-limits). The present argument supplies a generic high-temperature positive solution under the stated diagonal-rank condition.

## Irreducibility of the population dynamics

The restriction $\Pi\mathcal D_\beta\Pi$ is a classical rate generator. If $C_{\beta,b}\ge cI$ for all bonds, its off-diagonal rates satisfy

$$
W_{m\leftarrow n}
\ge c\sum_{b,a}|\langle m|F_{b,a}|n\rangle|^2
\quad(m\ne n).
$$

The graph of the lower-bound rates is undirected. A disconnected component would span a nontrivial invariant subspace for every bond Pauli, hence for every on-site $X$ and $Z$. These operators generate the full matrix algebra, which has no such invariant subspace. The graph is connected.

Thus the classical generator is irreducible. Its exact stationary distribution is the Gibbs population vector, and its kernel is one dimensional.

## Adding weak local dissipation

Set

$$
\mathcal L_\eta=\mathcal D_H+\eta\mathcal D_\beta,
\qquad \eta>0.
$$

Let $P=\Pi$ and $Q=1-P$. The off-diagonal commutator block $D_Q=Q\mathcal D_HQ$ is invertible because the energy spectrum is simple. Writing

$$
A=P\mathcal D_\beta P,\quad B=P\mathcal D_\beta Q,\quad
C=Q\mathcal D_\beta P,\quad E=Q\mathcal D_\beta Q,
$$

the stationary equation for diagonal and off-diagonal components $p,q$ becomes

$$
q=-\eta(D_Q+\eta E)^{-1}Cp,
$$

$$
\left[A-\eta B(D_Q+\eta E)^{-1}C\right]p=0,
\qquad\operatorname{Tr}p=1.
$$

The classical block $A$ is invertible on trace-zero diagonal operators. Analytic perturbation around its unique faithful stationary state therefore gives

$$
p=\rho_\beta+O(\eta),\qquad q=O(\eta),\qquad
\sigma_\eta=\rho_\beta+O(\eta).
$$

This argument inverts the Hamiltonian commutator only on its off-diagonal space. It does not incorrectly invert its degenerate zero-energy population block. All norms are equivalent in fixed dimension, so the error estimate includes trace norm. Faithfulness persists for sufficiently small $\eta$.

## A direct relaxation bound

The reference depolarizer obeys, on each bond,

$$
\sum_{a=1}^{15}\mathcal D[F_{b,a}]
=16(\mathcal R_b-\mathrm{id}),
$$

where $\mathcal R_b$ traces out that bond and replaces it by its maximally mixed state. Every nonidentity five-site Pauli intersects at least one bond. Consequently

$$
\operatorname{Re}\langle A,\mathcal D_0(A)\rangle
\le-16\|A\|_2^2
\qquad(\operatorname{Tr}A=0).
$$

Since $\|\mathcal D_\beta-\mathcal D_0\|_{2\to2}=O(\beta)$, a smaller high-temperature interval retains a positive constant $\delta$ with

$$
\operatorname{Re}\langle A,\mathcal D_\beta(A)\rangle
\le-\delta\|A\|_2^2
\qquad(\operatorname{Tr}A=0).
$$

The coherent part is skew-adjoint. The resulting semigroup contracts trace-zero differences in Hilbert–Schmidt norm at least as fast as $e^{-\eta\delta t}$. Every nonzero eigenvalue satisfies

$$
\eta\delta\le-\operatorname{Re}\lambda(\mathcal L_\eta)
\le\eta\|\mathcal D_\beta\|_{2\to2}.
$$

Thus the stationary state is unique and attracting, with

$$
\gamma(\mathcal L_\eta)=\Theta(\eta).
$$

No nondegeneracy of nonzero Bohr frequencies is required. Only simplicity of the Hamiltonian spectrum entered the stationary Schur complement.

## Fixed strength and the matching law

For $0<\eta\le1$,

$$
\|\mathcal L_\eta\|_{2\to2}
\le \|\mathcal D_H\|_{2\to2}
+\|\mathcal D_\beta\|_{2\to2}=:J_0.
$$

Multiplying the entire generator by $J/J_0$ enforces any prescribed $J>0$, preserves its stationary state, and rescales the gap by a fixed factor.

The construction has error at most $a\eta$ and gap at least $b\eta$ for fixed positive constants. Choosing $\eta=\varepsilon/a$ gives an admissible gap proportional to $\varepsilon$. The [universal upper bound](accuracy-relaxation.md) gives the reverse inequality. Applied to this same family, it also forces its actual error to be $\Omega(\eta)$.

The high-temperature frontier is therefore genuinely $\Theta(\varepsilon)$ in stationary error, rather than only a parametric $O(\eta)$ approximation statement.

## Generic Hamiltonians and temperature quantifiers

Impose three conditions on $H$: a simple spectrum; rank31 of the local moment matrix; and a nonzero fixed Gibbs evaluation minor at $\beta=1$. Each is open dense and full measure because its defining polynomial or real-analytic function is nonzero at $H_0$.

For each $H$ in their intersection, the [isolated-zero argument](gibbs-certificate.md#one-high-temperature-interval-for-a-fixed-hamiltonian) gives a punctured high-temperature interval where the obstruction holds. The population inverse, coefficient positivity and dissipative coercivity supply another such interval. Their intersection proves Theorem 3.

The generic statement is: for each such $H$, some $\beta_*(H)>0$ exists, and every fixed $0<\beta<\beta_*(H)$ has the stated error–gap law. It contains no common temperature window or common conditioning constant.

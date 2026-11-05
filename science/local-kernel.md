# Local superoperators and physical rigidity

## Dimension of the local space

Use a Hermitian Pauli basis for one-qubit operator space. A Hermiticity-preserving linear map is a real $`4\times4`$ matrix in this basis. Trace annihilation sets its output-identity row to zero, leaving 12 independent entries.

At one site, decompose the 16-dimensional map space as

```math
\mathrm{End}(\mathbb R^4)
=\mathrm{span}\{\mathrm{id}\}\oplus\mathcal A\oplus\mathcal B,
\qquad
\dim\mathcal A=12,\quad \dim\mathcal B=3,
```

where $`\mathcal A`$ is the trace-annihilating space and $`\mathcal B`$ complements it and the identity. The trace functional composed with the four-dimensional identity-plus-$`\mathcal B`$ space is an isomorphism onto one-site row functionals.

Thus a two-site trace-annihilating map is spanned by

```math
\mathrm{id}\otimes\mathcal A,\quad
\mathcal A\otimes\mathrm{id},\quad
\mathcal A\otimes\mathcal A,\quad
\mathcal A\otimes\mathcal B,\quad
\mathcal B\otimes\mathcal A.
```

The dimensions are $`12+12+144+36+36=240`$. After extracting the one-site parts, a genuine bond contributes 216 dimensions. Distinct tensor-support patterns in this decomposition are independent, so for an open $`n`$-site chain

```math
\dim\mathcal V_n=12n+216(n-1).
```

At $`n=5`$ this equals 924. The raw four-bond basis has $`4\times240=960`$ columns and 36 representation redundancies. These redundancies must not be mistaken for physical stationary directions.

## Evaluation matrix

On each bond, use local matrix units that send one Pauli $`P_\nu`$ to a traceless Pauli $`P_\mu`$, for $`\nu=0,\ldots,15`$ and $`\mu=1,\ldots,15`$, while annihilating the other basis elements. Extend each map by the identity on the remaining sites.

For an operator $`\sigma`$, let $`T_\sigma`$ be the $`1023\times960`$ matrix whose columns contain the nonidentity global Pauli coordinates of these maps applied to $`\sigma`$. Using $`\mathrm{Tr}(P\sigma)`$ instead of normalized coordinates changes all output coordinates by a common factor and does not change rank.

The raw coefficient-to-superoperator map has image $`\mathcal V`$ and a fixed 36-dimensional kernel. Therefore

```math
\mathrm{rank}T_\sigma
=\mathrm{rank}E_\sigma.
```

For $`\sigma=f(H)`$ and $`H\ne0`$, the Hamiltonian commutator is a nonzero stationary element. Hence the rank is at most $`924-1=923`$. A single nonzero 923-minor suffices to establish the one-dimensional intrinsic kernel.

The [certificate](gibbs-certificate.md) supplies such a minor for an exact Gibbs state. Floating-point singular values are not used to certify this rank.

## Why a Hamiltonian generator cannot conceal dissipation

Suppose a GKLS representation of a superoperator equals a Hamiltonian commutator. For any pure state $`P=|\psi\rangle\langle\psi|`$,

```math
\mathrm{Tr}\bigl(P\mathcal L(P)\bigr)
=-\sum_\alpha
\left(
\langle\psi|L_\alpha^\dagger L_\alpha|\psi\rangle
-|\langle\psi|L_\alpha|\psi\rangle|^2
\right).
```

The coherent part contributes zero. Each summand is a nonnegative variance, including for non-Hermitian jumps. If the total superoperator is Hamiltonian, the left side is zero for every $`|\psi\rangle`$, and therefore every jump has zero variance on every pure state.

Equivalently, $`L_\alpha|\psi\rangle`$ is proportional to $`|\psi\rangle`$ for every vector. Applying this to basis vectors and their pairwise sums shows that $`L_\alpha`$ is a scalar multiple of the identity. Its dissipator vanishes.

Consequently no cancellation among positive dissipative terms can hide a nonzero dissipator inside a purely Hamiltonian superoperator. This conclusion permits arbitrary numbers of jumps and all GKLS representation freedoms.

## Why the termwise obstruction is insufficient

Even when each proper-support Gibbs-preserving physical update is trivial, stationarity of a sum is a different condition. For example,

```math
\sum_b-i[h_b,\rho_\beta(H)]=-i[H,\rho_\beta(H)]=0
```

need not hold term by term. Local coherent disturbances already exhibit cancellation.

The present argument studies the total evaluation kernel. It shows that, generically in the stated five-qubit family, the commutator direction accounts for every such cancellation in the larger linear map space. Complete positivity is needed only for the physical interpretation, not for the rank theorem itself.

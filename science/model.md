# Model and main theorems

## Thermal target

Consider an open chain of five qubits, with Hilbert space dimension $`d=32`$. Let $`P_a\in\{X,Y,Z\}`$ denote a one-qubit Pauli matrix. The Hamiltonian family consists of all

```math
H=\sum_{j=1}^{5}\sum_{a=1}^{3}h_{j,a}P_a^{(j)}
+\sum_{j=1}^{4}\sum_{a,b=1}^{3}J_{j,ab}P_a^{(j)}P_b^{(j+1)},
```

with arbitrary real coefficients. It has 51 parameters. An additive scalar is immaterial and is omitted. For inverse temperature $`\beta>0`$, the target is

```math
\rho_\beta(H)=\frac{e^{-\beta H}}{\mathrm{Tr}e^{-\beta H}}.
```

No translational symmetry, reality in a fixed computational basis, conserved charge, commuting interaction structure or integrability assumption is imposed.

## Allowed autonomous controls

The physical generator is time independent and has GKLS form

```math
\mathcal L(A)=-i[K,A]
+\sum_\alpha\left(
L_\alpha A L_\alpha^\dagger
-\frac12\{L_\alpha^\dagger L_\alpha,A\}
\right).
```

Each coherent term in $`K`$ and each individual jump $`L_\alpha`$ is supported on one site or one adjacent pair. The number of jumps and their coefficients are unrestricted. Their coefficients may depend on $`H`$ and $`\beta`$. The controlled Hamiltonian $`K`$ need not equal $`H`$.

Only the total stationarity equation $`\mathcal L(\rho_\beta)=0`$ is imposed. A bond contribution may disturb the target and be cancelled by other contributions. Neither quantum detailed balance nor frustration freeness is assumed.

A jump that is a coherent sum of operators on separated bonds generally creates cross terms with larger support in its dissipator and is not automatically in this class. The model acts on the original five qubits; retained auxiliaries and time-periodic preparation protocols define different models.

## A larger linear space

Let $`\mathcal V`$ be the real vector space of sums of bond-supported Hermiticity-preserving, trace-annihilating linear maps. A generator map is trace annihilating when

```math
\mathrm{Tr}\mathcal A(B)=0
\quad\text{for every }B.
```

This is the generator condition; it should not be confused with a trace-preserving channel. Every allowed GKLS generator belongs to $`\mathcal V`$. Many elements of $`\mathcal V`$ are not physical generators, making the linear theorem stronger than a positivity-constrained search.

Define the evaluation map and Hamiltonian commutator

```math
E_\rho:\mathcal V\longrightarrow\mathrm{Herm}_0,\qquad
E_\rho(\mathcal A)=\mathcal A(\rho),
\qquad
\mathcal D_H=-i[H,\cdot].
```

The [local-space calculation](local-kernel.md) gives $`\dim\mathcal V=924`$. Since $`[H,\rho_\beta]=0`$, the nonzero direction $`\mathcal D_H`$ is always in the kernel when $`H\ne0`$.

## Theorem 1: generic cancellation obstruction

For every fixed $`\beta>0`$, an open dense full-measure subset of the real 51-dimensional Hamiltonian family satisfies

```math
\ker E_{\rho_\beta(H)}
=\mathrm{span}_{\mathbb R}\{\mathcal D_H\}.
```

Consequently, every allowed GKLS generator fixing this Gibbs state is purely Hamiltonian. It has no genuine dissipative jump and cannot make the Gibbs state the unique globally attracting equilibrium.

Here generic means that the exceptional set is contained in the zero set of a nonzero real-analytic function. The theorem fixes $`\beta`$ before taking the generic set of $`H`$. It does not assert a common generic set working at every positive real $`\beta`$ simultaneously.

The proof combines an [exact finite certificate and analytic genericity](gibbs-certificate.md) with the [physical rigidity argument](local-kernel.md). It excludes nontrivial dissipation even if uniqueness or attraction is not requested.

## Theorem 2: stability of the obstruction

Equip operator space with the Hilbert–Schmidt norm and superoperators with its associated Frobenius inner product. For a target satisfying Theorem 1, define

```math
s_\rho=
\min_{\substack{\mathcal A\in\mathcal V,\ \mathcal A\perp\mathcal D_H\\
\lVert\mathcal A\rVert_{\mathrm F}=1}}
\lVert\mathcal A(\rho)\rVert_2>0.
```

Let an allowed generator have stationary state $`\sigma`$, induced Hilbert–Schmidt norm $`\lVert\mathcal L\rVert_{2\to2}\le J`$, and half-trace-distance error

```math
\frac12\lVert\sigma-\rho\rVert_1\le\varepsilon.
```

Every eigenvalue of $`\mathcal L`$ obeys

```math
|\mathrm{Re}\lambda(\mathcal L)|
\le\frac{2J\varepsilon}{s_\rho}.
```

In particular, its relaxation gap is at most this bound. This is a target-dependent statement; the positivity of $`s_\rho`$ is exact, while its size may be very small. The norm cap charges coherent control as well as dissipation.

## Theorem 3: matching high-temperature frontier

There is an open dense full-measure set of Hamiltonians $`H`$ such that each has a number $`\beta_*(H)>0`$ with the following property. Fix $`0<\beta<\beta_*(H)`$ and $`J>0`$. Among allowed GKLS generators with a unique faithful attracting stationary state, define

```math
\Gamma_{H,\beta,J}(\varepsilon)
=\sup_{\substack{\lVert\mathcal L\rVert_{2\to2}\le J\\
\frac12\lVert\sigma_{\mathcal L}-\rho_\beta(H)\rVert_1\le\varepsilon}}
\gamma(\mathcal L),
```

where $`\gamma(\mathcal L)`$ is the minimum positive decay rate $`-\mathrm{Re}\lambda`$ over its nonzero eigenvalues. Then

```math
\Gamma_{H,\beta,J}(\varepsilon)
=\Theta_{H,\beta,J}(\varepsilon)
\qquad (\varepsilon\downarrow0).
```

The [construction](local-construction.md) supplies positive local baths with stationary error $`O(\eta)`$ and relaxation gap $`\Theta(\eta)`$. Theorem 2 proves both the matching converse and an $`\Omega(\eta)`$ lower bound on that family's actual error.

The temperature interval and comparison constants may depend on $`H`$. No uniform size, temperature or finite-error advantage is claimed by this asymptotic notation.

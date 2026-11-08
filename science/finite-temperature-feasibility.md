# Finite-temperature feasibility with strict local jumps

Strict support of the reservoirs and strict support of coherent control impose different restrictions. For the explicit integer Hamiltonian $`H_0`$ used in this project, the following comparison is rigorously certified on the original five qubits.

| Controlled Hamiltonian $`K`$ | Gibbs preparation with individual on-site/adjacent-pair jumps |
|---|---|
| Unrestricted global $`K`$ | An exact unique globally attracting Gibbs state exists for $`0\le\beta\le1/100`$. |
| Unrestricted global $`K`$ | Every genuinely dissipative stationary realization is excluded for every real $`\beta\ge12/5`$. |
| On-site/adjacent-pair terms in $`K`$ | The original cancellation obstruction applies to $`H_0`$ at every positive algebraic $`\beta`$, including $`3/1000`$ and $`1/100`$. |

The interval $`1/100\lt \beta\lt 12/5`$ remains unresolved in the global-control model. These results give certified feasible and forbidden regions, rather than an exact transition or a proof that the whole feasible set is an interval. A purely Hamiltonian generator can still fix any Gibbs state; the exclusion concerns genuine dissipation and therefore excludes unique attractive preparation.

## Two coherent-control models

The target Hamiltonian $`H_0`$ is the nearest-neighbor Pauli sum in [the authoritative coefficient file](../verification/data/hamiltonian.json). The controlled Hamiltonian $`K`$ is a separate object. In both models the time-independent generator is

```math
\mathcal L(A)=-i[K,A]+\sum_a\mathcal D[J_a](A),
\qquad
\mathcal D[J](A)=JAJ^\dagger-\frac12\{J^\dagger J,A\}.
```

Each effective jump individually acts on one site or an adjacent pair. Scalar jumps have zero dissipator; **genuine dissipation** means that an admissible representation contains a nonscalar jump. Positive dissipative terms cannot hide a nonzero dissipator inside a Hamiltonian commutator, by the [purity argument](local-kernel.md#why-a-hamiltonian-generator-cannot-conceal-dissipation).

The original [local-control model](model.md#allowed-autonomous-controls) also restricts every coherent term of $`K`$ to those supports. The comparison model permits arbitrary global $`K`$ while retaining the same jump supports. Neither model supplies retained auxiliaries, extra physical levels, time-dependent controls or feedback. A coherent sum of separated local operators is not automatically an individual allowed jump.

Let the simple spectrum, normalized ground vector and Gibbs weights be

```math
H_0|j\rangle=E_j|j\rangle,\qquad
E_0\lt E_1\lt \cdots\lt E_{31},\qquad |g\rangle=|0\rangle,
```

```math
\rho_\beta=\frac{e^{-\beta H_0}}{\mathrm{Tr}e^{-\beta H_0}}
=\sum_{j=0}^{31}p_j(\beta)|j\rangle\langle j|,
\qquad \delta_\beta=1-p_0(\beta).
```

All one-site and adjacent-pair supports form $`\mathcal N`$. Define

```math
\mu=\min_{S\in\mathcal N}\lambda_{\min}(g_S),
\qquad g_S=\mathrm{Tr}_{S^c}|g\rangle\langle g|,
\qquad
r=\min_{S\in\mathcal N}
\frac{\lambda_{\min}(g_S)}{\lambda_{\max}(g_S)}.
```

The eigenvalue minima include zeros on the entire local Hilbert space. The [ground/thermal certificate](../verification/ground-thermal/README.md) proves that all nine marginals here are positive definite.

## Certified ground marginals and thermal deficit

The certificate reconstructs the exact Gaussian-integer matrix from the coefficient JSON and uses 256-bit Arb/Acb Rump eigenvalue/eigenvector enclosures. It isolates all 32 energies, normalizes an enclosed true ground vector, takes partial traces and encloses each marginal's complete spectrum. Midpoints propose an order only; strict ball inequalities verify separation, positivity and the minimizing supports. No floating-point rank threshold is accepted.

| Support | Smallest ground-marginal eigenvalue, approximately |
|---|---:|
| 1 | 0.13713054610879 |
| 2 | 0.14664888547302 |
| 3 | 0.04376053329132 |
| 4 | 0.11233704096910 |
| 5 | 0.08221071874401 |
| 1,2 | 0.00007169677522711 |
| 2,3 | 0.00727163917899 |
| 3,4 | 0.00325615601118 |
| 4,5 | 0.00009112293656877 |

The table is illustrative. The [machine certificate](../verification/ground-thermal/ground_thermal_certificate.json) supplies outward rational enclosures for every eigenvalue and proves

```math
0.000071696775227\lt \mu\lt 0.000071696775228,
```

```math
\begin{aligned}
0.000072889471412&\lt r\lt 0.000072889471413,\\
3.005072939810&\lt E_1-E_0\lt 3.005072939811.
\end{aligned}
```

Both minima are uniquely attained on bond $`(1,2)`$. The thermal deficit is evaluated from the certified energy balls through the exact expression

```math
\delta_\beta=
\frac{\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}
{1+\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}.
```

At $`\beta=4`$ the certified enclosure is

```math
0.000006066710605253\lt \delta_4\lt 0.000006066710605254.
```

## An inherited stationary approximation floor

[Dissipative-Locality-Accuracy's stationary-state converse](https://github.com/GoGoKo699/Dissipative-Locality-Accuracy/blob/007749711a769111b86c0413ef9f5b91e2b88cac/science/converse.md) already proves that every stationary output $`\sigma`$ of a generator with a nonscalar allowed jump satisfies

```math
1-\langle g|\sigma|g\rangle\ge\frac\mu2.
```

It allows arbitrary global $`K`$, arbitrary channel strengths and mixed stationary outputs with eigenvectors different from the target. This pure-target bound is inherited. Applying the ground-projector measurement to half trace distance gives its direct Gibbs corollary:

```math
\boxed{
\frac12\|\sigma-\rho_\beta\|_1
\ge\left[\frac\mu2-\delta_\beta\right]_+.
}
```

Indeed, trace distance is at least the difference between the two probabilities of that measurement outcome, and $`\langle g|\rho_\beta|g\rangle=1-\delta_\beta`$. The positive-part convention is $`[x]_+=\max\{x,0\}`$.

For the explicit witness,

```math
\frac12\|\sigma-\rho_4\|_1
>0.000029781677008303.
```

This is a stationary accuracy floor, independent of coherent or dissipative strengths. The sufficient test $`\delta_\beta\lt \mu/2`$ starts after its unique crossing in $`(3.41147195216,3.41147195217)`$. Uniqueness follows because each positive-gap Boltzmann factor decreases strictly with $`\beta`$. That crossing is a threshold for this inherited test, not the physical feasibility boundary.

## Exact-target population balance is stronger

For exact Gibbs stationarity the ground vector is already an eigenvector of the stationary state. The moving-eigenvector step of the inherited ordinary-fidelity theorem is unnecessary. Center each admissible jump by

```math
L_a=J_a-\langle g|J_a|g\rangle I,
\qquad R=\rho_\beta-p_0|g\rangle\langle g|.
```

Scalar subtraction preserves support. The coherent commutator has zero ground diagonal for every $`K`$ because $`|g\rangle`$ is a Gibbs eigenvector. Thus stationarity implies the established spectral population-balance identity

```math
p_0\sum_a\|L_ag\|^2
=\sum_a\langle g|L_aRL_a^\dagger|g\rangle
\le p_1\sum_a\|L_a^\dagger g\|^2,
```

where $`0\preceq R\preceq p_1I`$. For a jump on $`S`$, put $`\alpha_S=\lambda_{\min}(g_S)`$ and $`b_S=\lambda_{\max}(g_S)`$. Its local matrix obeys

```math
\|L_ag\|^2\ge\alpha_S\|L_{a,S}\|_F^2,
\qquad
\|L_a^\dagger g\|^2\le b_S\|L_{a,S}\|_F^2.
```

At least one centered matrix is nonzero when a nonscalar jump is present. Summing gives the necessary condition

```math
\boxed{e^{-\beta(E_1-E_0)}=\frac{p_1}{p_0}\ge r.}
```

The certificate brackets its sufficient exclusion threshold as

```math
3.170161438761\lt \frac{\log(1/r)}{E_1-E_0}
\lt 3.170161438762.
```

Using $`R\preceq\delta_\beta I`$ in the same identity also gives $`\delta_\beta\ge\mu`$ by the inherited marginal argument. Its crossing is in $`(3.18245872502,3.18245872503)`$. These are sharper applications of inherited balance to this fixed Gibbs eigenvector; neither condition is a sufficiency theorem for preparation.

## A full ground-population form excludes every colder target

Keep all excitation weights rather than replacing them by $`p_1`$. Define

```math
W_\beta=e^{-\beta(H_0-E_0I)}=\frac{\rho_\beta}{p_0},
\qquad
q_\beta(A)=\langle g|A W_\beta A^\dagger-A^\dagger A|g\rangle.
```

The ground diagonal of $`\mathcal D[A](\rho_\beta)`$ is $`p_0q_\beta(A)`$. Since $`W_\beta|g\rangle=|g\rangle`$, adding any scalar multiple of $`I`$ leaves this form unchanged, including all scalar cross terms.

On bond $`b`$ use the 15 nonidentity Hermitian two-qubit Paulis $`F_{b,u}`$, extended by identity outside the bond. An arbitrary nonscalar, possibly non-Hermitian supported operator has a nonzero complex coefficient vector $`c`$ modulo scalars:

```math
A=\sum_{u=1}^{15}c_uF_{b,u},
\qquad q_\beta(A)=c^\dagger Q_b(\beta)c,
```

```math
(Q_b)_{uv}
=\langle g|F_{b,v}W_\beta F_{b,u}|g\rangle
-\langle g|F_{b,u}F_{b,v}|g\rangle.
```

This exact matrix is Hermitian. If $`V`$ has columns $`F_{b,u}|g\rangle`$, its implemented form is $`Q_b=(V^\dagger W_\beta V)^{\mathsf T}-V^\dagger V`$. The transpose in the first term is essential for arbitrary complex coefficients.

The new interval certificate computes the enclosed matrix exponential and proves strict positivity of $`-Q_b-m_bI`$ by interval LDL* at $`\beta=12/5`$:

| Bond $`b`$ | Certified margin $`-Q_b(12/5)\succ m_bI_{15}`$ |
|---|---:|
| 1,2 | $`m_b=0.00008`$ |
| 2,3 | $`m_b=0.029`$ |
| 3,4 | $`m_b=0.013`$ |
| 4,5 | $`m_b=0.00029`$ |

These margins use the stated unnormalized Pauli coefficient metric. All 60 positive pivot balls are retained. On-site jump spaces are subspaces of these bond spaces. Every nonscalar allowed jump therefore contributes strictly negative ground-population drift, and no positive sum of those contributions can vanish. Arbitrary global $`K`$ cannot cancel a Gibbs eigenvector's diagonal drift.

Finally, $`H_0-E_0I\succeq0`$ and its exponential commutes with itself at different temperatures, so

```math
\beta'\ge\beta
\quad\Longrightarrow\quad
W_{\beta'}\preceq W_\beta,
\qquad Q_b(\beta')\preceq Q_b(\beta).
```

Hence the same strict negative-form certificate excludes genuine dissipative stationarity for **every real** $`\beta\ge12/5`$. This witness is monotone; no monotonicity of the full physical feasible set follows. Its exact-target proof does not itself establish a finite-accuracy robustness bound; the inherited trace-distance corollary supplies that separate result above.

## Exact high-temperature preparation with global coherent control

The [existing positive reservoir prescription](local-construction.md#exact-secular-balance) and its [continuous interval certificate](quantitative-witness.md#an-explicit-positive-reservoir) supply $`\mathcal D_\beta`$ for $`0\le\beta\le1/100`$ such that

```math
\Pi\mathcal D_\beta(\rho_\beta)=0,
\qquad C_b(\beta)\succeq0.0512I_{15},
```

```math
\mathrm{Re}\langle A,\mathcal D_\beta(A)\rangle_{\mathrm{HS}}
\le-4.12\|A\|_2^2
\qquad(\mathrm{Tr}A=0).
```

Here $`\Pi`$ dephases in the exact energy basis. The bath fixes the desired populations but generally leaves an off-diagonal drift. These positive reservoirs and their population-balance construction are inherited project results, with the [weak-coupling antecedents already credited](../references/related-work.md#boundary-thermalization-and-weak-coupling-limits).

For $`\beta>0`$ the Gibbs spectrum is simple. Put $`B=\mathcal D_\beta(\rho_\beta)`$ and choose, in that basis,

```math
K_{mn}=-i\frac{B_{mn}}{p_n-p_m}\quad(m\ne n),
\qquad K_{mm}\in\mathbb R.
```

Hermiticity of $`B`$ implies Hermiticity of $`K`$, and direct substitution gives

```math
-i[K,\rho_\beta]=-B,
\qquad
\bigl(-i[K,\cdot]+\mathcal D_\beta\bigr)(\rho_\beta)=0.
```

This off-diagonal completion is the established spectral-stabilizability construction of [Linowski, Rudnicki and Gneiting (2023), Proposition 1 and Eq. (5)](https://arxiv.org/abs/2212.12245v2), including antecedents credited there. It is not a new bath construction.

The arbitrary commutator is Hilbert–Schmidt skew-adjoint. The full generator retains the same coercivity on traceless differences, giving

```math
\|e^{t\mathcal L}(\sigma)-\rho_\beta\|_2
\le e^{-4.12t}\|\sigma-\rho_\beta\|_2.
```

This proves uniqueness and global attraction in finite dimension, as well as a positive unscaled relaxation gap. At $`\beta=0`$ use the local depolarizer directly with $`K=0`$; division by degenerate Gibbs eigenvalues is unnecessary.

The resulting $`K`$ generally acts globally and depends on the target. For each fixed positive $`\beta`$ it is finite, so rescaling the entire generator meets any positive total-strength budget while preserving exactness and rescaling the positive gap. The constant 4.12 is an unscaled coercivity statement, not a useful gap at a specified budget without a bound on the complete generator. No efficient global-Hamiltonian synthesis is established.

At $`\beta=3/1000`$ and $`1/100`$ the [inherited algebraic local-control obstruction](gibbs-certificate.md#transfer-to-the-exact-gibbs-state) simultaneously excludes genuine dissipation with local $`K`$. These exact rational examples separate local and global coherent control without changing individual jump support. The positive reservoir interval must not be relabeled as a continuous local-evaluation-rank certificate.

## An exact stationarity feasibility problem

For $`\beta>0`$ with simple spectrum, introduce a Hermitian positive semidefinite Kossakowski block $`C_b`$ on each bond's 15 traceless Paulis and its associated dissipator $`\mathcal D_C`$. The constraints

```math
C_b\succeq0,
\qquad \sum_b\mathrm{Tr}C_b=1,
\qquad \Pi\mathcal D_C(\rho_\beta)=0
```

are a semidefinite feasibility problem equivalent to existence of a genuinely dissipative stationary realization with unrestricted $`K`$. For necessity, remove each jump's scalar part, absorb its Hamiltonian gauge into $`K`$, group the remaining supported jumps into positive bond blocks, and normalize their nonzero total trace. For sufficiency, factor the positive blocks into allowed jumps and use the preceding off-diagonal completion. Rate normalization removes an irrelevant common scale and is not a physical implementation budget.

Feasibility alone certifies stationarity, not uniqueness or attraction. The coercive family above supplies those additional properties in its certified interval. Restricting $`K`$ to local terms requires the full local stationarity constraints; diagonal balance is insufficient. At $`\beta=0`$ degeneracy also makes diagonal-only completion insufficient, although local depolarization explicitly prepares the maximally mixed state.

## Attribution and boundaries

The [related-work comparison](../references/related-work.md#finite-temperature-feasibility-and-coherent-control) credits the inherited pure-target bound, population balance, positive secular bath and global coherent completion. Nonzero local-cooling temperature floors already occur in [Žnidarič (2015)](https://arxiv.org/abs/1501.03453). The additional result here is the explicit rigorous five-qubit ground/thermal/form certificate and the resulting model-separated feasibility regions.

No exact transition, arbitrary-chain-length theorem, larger-neighborhood no-go, necessary quasi-local tails, retained-ancilla limitation or time-dependent preparation obstruction follows. The original local-control theorem and its fixed-temperature/generic-Hamiltonian quantifiers remain intact. The two coherent-control models answer different questions about the same strictly supported reservoirs.

# Physical interpretation and boundaries

## What cancellation can accomplish

Individual local pieces of a Hamiltonian generally disturb its Gibbs state. Their sum nevertheless commutes with it. This familiar cancellation makes a termwise no-go theorem insufficient to decide whether several carefully designed baths can jointly stabilize the exact thermal target.

The five-qubit result resolves that possibility for on-site and adjacent-pair generator terms. It finds the entire stationary local linear space, even before imposing complete positivity. The only surviving direction is the total Hamiltonian commutator. Therefore an exact stationary local generator can preserve populations but cannot thermalize them.

The result concerns a prescribed Gibbs state of a prescribed interacting Hamiltonian. Local dissipators can certainly have unique steady states. Those states generally have an effective modular Hamiltonian $-\log\rho$ containing interactions beyond the desired nearest-neighbor family.

## Why five qubits appear

For an open chain, the local trace-annihilating map space has dimension $12n+216(n-1)$. Its evaluation target has dimension $4^n-1$.

| Sites | Local map-space dimension | Traceless state-space dimension |
|---:|---:|---:|
| 3 | 468 | 63 |
| 4 | 696 | 255 |
| 5 | 924 | 1023 |

Five is the first size at which this larger linear map space can have only the one compulsory commutator direction in its kernel. Below that size, dimension counting forces many additional linear stationary directions. This observation does not establish physical Gibbs thermalizers on smaller chains: the extra directions need not be GKLS generators.

Five sites therefore provide a finite setting where a universal cancellation obstruction can be certified without assuming positivity during the linear analysis. They do not establish a theorem for arbitrary chain length.

## Accuracy and time

For a fixed generic target and bounded total generator strength, exact stationary accuracy is a singular limit: every dissipative decay rate must vanish. At sufficiently high temperature the weak-bath construction realizes this limit with optimal linear scaling of the relaxation gap in the error.

The Hamiltonian spectrum and the Lindbladian relaxation gap play different roles. Energy differences control the off-diagonal perturbative response; real parts of generator eigenvalues control damping. A nonzero energy gap alone does not guarantee rapid thermalization.

The constants can be poorly conditioned. The [quantitative witness](quantitative-witness.md) makes this visible. The asymptotic exponent does not by itself establish an efficient practical sampler, a useful finite-error lower bound on running time, or a large experimental separation.

## Consistent exceptions

At $\beta=0$, the target is maximally mixed. Local depolarization fixes it and mixes rapidly. The theorem excludes that endpoint, and its conditioning deteriorates on approach to it.

Commuting Hamiltonians also lie in exceptional subfamilies. For a Hamiltonian diagonal in a product basis, local dephasing is genuine dissipation that leaves the Gibbs state invariant, although it need not select its populations uniquely. This does not conflict with a generic statement over all 51 Hamiltonian parameters.

With global support, the reset generator

$$
\mathcal L(A)=\operatorname{Tr}(A)\rho-A
$$

has the exact Gibbs target as its unique equilibrium and a constant relaxation rate. It is outside the allowed support class for a correlated target. The obstruction is therefore about simultaneous locality and exact stationary thermalization.

## Larger neighborhoods remain open

A nearest-neighbor Hamiltonian does not imply that a thermal update should act on only an adjacent pair. Classical Gibbs updates can already require a site and both neighbors. The present result excludes the stated two-site generator support; it does not prove that three-site or four-site baths fail, that an interaction radius must grow with chain size, or that infinite quasi-local tails are necessary.

Exact quantum Gibbs samplers with quasi-local terms are an important positive comparison. Their existence and the effect of truncating their tails motivate the locality question, but this finite theorem does not identify a minimal sufficient larger support.

## Other preparation models

Time-dependent controls, repeated bath resets, persistent auxiliary systems, measurement and feedback with enlarged support, or preparation through a sequence of intermediate states need separate analysis. A system can reach a desired state at a selected time without that state being the stationary state of a single fixed local generator.

The [related-work account](../references/related-work.md) compares those models explicitly. The current contribution is a precise autonomous local limit, with an attainable approximation law inside that same model.

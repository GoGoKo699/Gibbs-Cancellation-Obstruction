# Gibbs Cancellation Obstruction

**Can overlapping nearest-neighbor dissipators stabilize the exact Gibbs state of a generic interacting quantum chain?**

For five qubits on an open chain, the supported result excludes genuine dissipation even when the contributions of different local terms are allowed to cancel. At each fixed positive inverse temperature, a generic nearest-neighbor Hamiltonian has a one-dimensional stationary local-superoperator kernel, spanned by its Hamiltonian commutator. Individual jump operators and coherent-control terms are restricted to one site or one adjacent pair.

At sufficiently high temperature, the associated optimal relaxation gap under a fixed total generator-strength budget is proportional to the allowed stationary trace-distance error as that error tends to zero. The temperature interval and constants depend on the target Hamiltonian. The result does not establish a theorem for arbitrary chain lengths or larger fixed neighborhoods.

The proof combines a local-superoperator dimension calculation, an exact finite-field/Galois certificate and analytic genericity. A positive local construction matches the accuracy–relaxation exponent. For the explicit witness, rigorous interval arithmetic also certifies positive reservoirs throughout $`0\le\beta\le0.01`$ and finite-error bounds at two rational temperatures. The continuous construction interval is separate from the evaluation-rank claim. The certified converse constants are extremely large, so a useful finite-error speed penalty remains unestablished.

## Strict local jumps with global coherent control

The sister project [Dissipative-Locality-Accuracy](https://github.com/GoGoKo699/Dissipative-Locality-Accuracy) supplies an inherited pure-target stationary-fidelity bound. Applied to this project's explicitly certified five-qubit ground state, it gives a finite-temperature stationary trace-distance floor. The [full feasibility account](science/finite-temperature-feasibility.md) also keeps the support of the controlled Hamiltonian $`K`$ separate from the support of each jump: with unrestricted global $`K`$, the existing positive reservoir prepares the exact Gibbs state attractively for $`0\le\beta\le1/100`$, while a new rigorous ground-population certificate excludes genuine dissipative stationarity for every real $`\beta\ge12/5`$, even with global $`K`$.

The middle interval remains unresolved. These are certified feasible and forbidden regions, not an exact crossover. The original local-$`K`$ cancellation theorem remains unchanged; at $`\beta=3/1000`$ and $`1/100`$ it gives an explicit separation from the global-control construction. The [ground/thermal certificate](verification/ground-thermal/README.md) encloses all nine allowed ground-state marginal spectra and the thermal deficit. The pure-target bound, spectral population balance and global coherent completion retain their [inherited attribution](references/related-work.md#finite-temperature-feasibility-and-coherent-control).

## Read the result

| Start here | What it provides |
|---|---|
| [Scientific account](science/README.md) | A connected route through the model, proofs, construction and interpretation |
| [Model and theorems](science/model.md) | Exact support restrictions, genericity quantifiers, strength budget and error convention |
| [Quantitative witness](science/quantitative-witness.md) | Certified constants, a positive reservoir and explicit finite-error ranges |
| [Finite-temperature feasibility](science/finite-temperature-feasibility.md) | Certified ground marginals, a thermal accuracy floor and local/global coherent-control comparison |
| [Related work](references/related-work.md) | The contribution and its boundaries relative to existing results |
| [Verification](verification/README.md) | Portable commands and exact/rational inputs for reproducing the certificates |

## Contribution and boundaries

Stationarity constraint and null-space methods are inherited from [Bairey et al. (2020)](https://arxiv.org/abs/1907.11154) and [Souza and Iemini (2026)](https://arxiv.org/abs/2408.05302). Weak-coupling population balance is inherited from [Tupkary et al. (2023)](https://arxiv.org/abs/2301.02146). The result here establishes the generic Gibbs-family kernel and a matching bounded-strength accuracy–relaxation law in the stated five-qubit model.

The distinction from [Gibbs-Locality-Obstruction](https://github.com/GoGoKo699/Gibbs-Locality-Obstruction) is that local terms need not preserve the target separately. This theorem allows cancellation among all overlapping local contributions. It does not cover arbitrary chain lengths, larger fixed neighborhoods, quasi-local tails, retained auxiliary systems, or general time-dependent preparation protocols. Commuting and other exceptional Hamiltonians may admit exact local thermalizers.

## Learn the project

The single educational anchor is **Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction* (first edition, 2012)**. The [learning route](learning/README.md) uses the freely available author preprint, version 2. Its section numbering differs from the published book; the [source-to-project bridge](learning/bridge.md) gives both reading routes, translates the notation, and supplies the missing steps to this project's result.

The [30-milestone map](learning/milestones.md) has 12 background/preliminaries targets and 18 narrative/innovation targets. The first phase builds from states and generators to the complete thermalization model. The second connects the cancellation kernel, exact certificate, stability bound and positive construction into the accuracy–relaxation law. The map is a common guide to the project, independent of a particular reader's prior study or assessment history.

The [LLM reading guide](llms.txt) provides direct routes for studying the story, inspecting the theorems, or reproducing the calculations.

## Reproduce the finite certificates

```sh
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python verification/run_all.py
```

The exact checks and interval enclosures have different roles. The [verification guide](verification/README.md) explains both and identifies the analytical steps that a computational pass does not replace.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).


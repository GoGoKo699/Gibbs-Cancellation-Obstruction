# Gibbs Cancellation Obstruction

**Can overlapping nearest-neighbor dissipators stabilize the exact Gibbs state of a generic interacting quantum chain?**

For five qubits on an open chain, the supported result excludes genuine dissipation even when the contributions of different local terms are allowed to cancel. At each fixed positive inverse temperature, a generic nearest-neighbor Hamiltonian has a one-dimensional stationary local-superoperator kernel, spanned by its Hamiltonian commutator. Individual jump operators and coherent-control terms are restricted to one site or one adjacent pair.

At sufficiently high temperature, the associated optimal relaxation gap under a fixed total generator-strength budget is proportional to the allowed stationary trace-distance error as that error tends to zero. The temperature interval and constants depend on the target Hamiltonian. The result does not establish a theorem for arbitrary chain lengths or larger fixed neighborhoods.

The proof combines a local-superoperator dimension calculation, an exact finite-field/Galois certificate and analytic genericity. A positive local construction matches the accuracy–relaxation exponent. For the explicit witness, rigorous interval arithmetic also certifies positive reservoirs throughout $0\le\beta\le0.01$ and finite-error bounds at two rational temperatures. The continuous construction interval is separate from the evaluation-rank claim. The certified converse constants are extremely large, so a useful finite-error speed penalty remains unestablished.

## Read the result

| Start here | What it provides |
|---|---|
| [Scientific account](science/README.md) | A connected route through the model, proofs, construction and interpretation |
| [Model and theorems](science/model.md) | Exact support restrictions, genericity quantifiers, strength budget and error convention |
| [Quantitative witness](science/quantitative-witness.md) | Certified constants, a positive reservoir and explicit finite-error ranges |
| [Related work](references/related-work.md) | The contribution and its boundaries relative to existing results |
| [Verification](verification/README.md) | Portable commands and exact/rational inputs for reproducing the certificates |

## Contribution and boundaries

Stationarity constraint and null-space methods are inherited from [Bairey et al. (2020)](https://arxiv.org/abs/1907.11154) and [Souza and Iemini (2026)](https://arxiv.org/abs/2408.05302). Weak-coupling population balance is inherited from [Tupkary et al. (2023)](https://arxiv.org/abs/2301.02146). The result here establishes the generic Gibbs-family kernel and a matching bounded-strength accuracy–relaxation law in the stated five-qubit model.

The distinction from [Gibbs-Locality-Obstruction](https://github.com/GoGoKo699/Gibbs-Locality-Obstruction) is that local terms need not preserve the target separately. This theorem allows cancellation among all overlapping local contributions. It does not cover arbitrary chain lengths, larger fixed neighborhoods, quasi-local tails, retained auxiliary systems, or general time-dependent preparation protocols. Commuting and other exceptional Hamiltonians may admit exact local thermalizers.

## Reproduce the finite certificates

```sh
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python verification/run_all.py
```

The exact checks and interval enclosures have different roles. The [verification guide](verification/README.md) explains both and identifies the analytical steps that a computational pass does not replace.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).


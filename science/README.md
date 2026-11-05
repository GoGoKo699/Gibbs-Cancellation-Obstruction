# Scientific account

The question is whether a thermal state of a nearest-neighbor quantum Hamiltonian can be the exact equilibrium of strictly neighboring dissipative controls when local disturbances may cancel.

For a generic five-qubit chain, the answer is negative: every stationary nearest-neighbor generator in a larger linear class is a Hamiltonian commutator. This excludes all genuine local dissipation. At sufficiently high temperature, the best bounded-strength relaxation gap is nevertheless proportional to the allowed stationary-state error, and a positive local construction attains that order.

## Reading route

| Question | Account |
|---|---|
| Which dynamics, Hamiltonians, errors and genericity statements are covered? | [Model and theorems](model.md) |
| Why does a one-dimensional stationarity kernel exclude every dissipative representation? | [Local superoperators and physical rigidity](local-kernel.md) |
| How can a finite integer computation certify an exact exponential Gibbs state? | [The algebraic Gibbs certificate](gibbs-certificate.md) |
| Why must accurate stationary preparation slow down at bounded strength? | [Accuracy and relaxation](accuracy-relaxation.md) |
| How is the upper-bound exponent attained with positive bond-local baths? | [The high-temperature construction](local-construction.md) |
| What can be quantified for the explicit witness? | [Quantitative witness](quantitative-witness.md) |
| What changes if support, temperature or the preparation model changes? | [Physical interpretation](interpretation.md) |

The [related-work account](../references/related-work.md) distinguishes the new Gibbs-family result from inherited inverse-Lindblad and weak-coupling methods. [Verification](../verification/README.md) separates exact finite certificates, rigorous interval bounds and numerical illustrations.

The principal scope is five qubits with one-site and adjacent-pair generator terms. An all-chain theorem and impossibility for larger neighborhoods are not part of the result.

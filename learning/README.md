# Learning route

The educational question is how the familiar theory of quantum Markov semigroups leads to a spatial obstruction: a generic five-qubit Gibbs state cannot be stationary under any genuinely dissipative generator whose individual jumps and coherent terms act on one site or one adjacent pair. The approximation result then asks how quickly such a generator can relax when a small stationary-state error is allowed.

This route develops the mathematical and physical connections behind the [scientific account](../science/README.md). It contains one selected educational anchor, a worked bridge, and exactly 30 project-specific milestones.

## Selected anchor

Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, first edition, SpringerBriefs in Physics, Springer, 2012. [Publisher and DOI](https://doi.org/10.1007/978-3-642-23354-8); [author's book page](https://sites.google.com/site/angelrivasphysicist/book).

The open reading version is the authors' [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), dated 9 February 2012; [full PDF](https://arxiv.org/pdf/1104.5242v2). **Every section, definition, theorem and equation number in this learning route refers to that version.** Its section numbering differs from the published book's chapter numbering because the preprint has a separate introductory section.

| Topic | Published book | Open preprint v2 |
|---|---|---|
| Mathematical tools | Chapter 1 | Section 2 |
| Closed-system dynamics | Chapter 2 | Section 3 |
| Open-system dynamical maps | Chapter 3 | Section 4 |
| Structure of quantum Markov processes | Chapter 4 | Section 5 |
| Microscopic Markovian descriptions | Chapter 5 | Section 6 |

The main route uses §§2.1–2.3, 4.2–4.3, 5.2, 5.4, 6.2.1, 6.2.8 and 6.4.1. The bridge identifies the particular definitions and equations at each step. The local evaluation kernel, finite-field/Galois certificate and matching accuracy law are project material developed beyond the anchor. Primary research attribution remains in [related work](../references/related-work.md).

## Two phases, thirty milestones

The [milestone map](milestones.md) uses a **12/18 split** suited to this proof.

**Phase I, M01–M12: background and preliminaries.** The route starts with one qubit, its states and dynamical maps. It then builds positive generators, distinguishes stationarity from attraction, examines cancellation and spatial support, and connects Gibbs balance to the full five-qubit model and its strength budget.

**Phase II, M13–M30: narrative and innovation.** The obstruction branch starts with local map dimensions and reaches an exact, generic system-level theorem. The approximation branch starts with local population-control directions and reaches positive baths, stationary perturbation, the optimal bounded-strength gap, and the limits of the certified constants. Each milestone states a central question, an understanding target, dependencies and story role, a conceptual connection, and precise source pointers.

The ordering follows mathematical dependencies. The map is a shared description of the project; its contents do not depend on any individual's previous study or progress.

## Reading navigation

| Route | Purpose |
|---|---|
| [Bridge: states, maps and generators](bridge.md#states-maps-and-generators) | Establish the conventions used by the proof |
| [Bridge: cancellation in a thermal qubit](bridge.md#worked-example-exact-cancellation-in-a-thermal-qubit) | See why individual jumps need not preserve the target |
| [Bridge: the algebraic certificate](bridge.md#how-an-exact-finite-certificate-reaches-a-gibbs-state) | Connect finite calculations to the actual exponential state |
| [Bridge: a weak reset bath](bridge.md#worked-example-a-weak-reset-bath) | Calculate stationary bias and relaxation together |
| [Bridge: the five-qubit construction](bridge.md#from-local-bath-directions-to-the-five-qubit-frontier) | Follow positivity, secular balance and the stationary Schur complement |
| [Milestones M01–M12](milestones.md#phase-i-background-and-preliminaries) | Build the common vocabulary from local examples to the full model |
| [Milestones M13–M30](milestones.md#phase-ii-narrative-and-innovation) | Follow the exact obstruction and the matching approximation argument |
| [Scientific model](../science/model.md) and [verification guide](../verification/README.md) | Consult authoritative theorem statements and reproducible evidence |

## Scope carried through the route

The exact result fixes a positive inverse temperature before taking a generic set of five-qubit Hamiltonians. The matching theorem gives each Hamiltonian in another generic set its own sufficiently high-temperature interval. It supplies no uniform interval or system-size bound. The limit of vanishing stationary error holds the Hamiltonian, inverse temperature and total generator-strength budget fixed.

The worked one-qubit models explain mechanisms; they do not satisfy the five-qubit obstruction theorem. The theorem allows total cancellation and imposes no detailed-balance or termwise stationarity condition. Exact algebraic certificates, rigorous interval enclosures and exploratory numerical calculations have different logical roles. The finite converse constants are extremely loose, so the sharp asymptotic exponent alone establishes no practical sampling advantage or substantial finite-error penalty.

## A shared finite-temperature application

The [finite-temperature comparison](../science/finite-temperature-feasibility.md) connects this project to [Dissipative-Locality-Accuracy](https://github.com/GoGoKo699/Dissipative-Locality-Accuracy) under the same Rivas–Huelga source. Its inherited pure-target fidelity bound turns certified ground marginals and a thermal deficit into a stationary accuracy floor. The existing secular bath also permits exact high-temperature preparation when coherent control becomes global; a rigorous ground-population form excludes cold targets even with that resource.

The [finite-temperature bridge](bridge.md#from-ground-marginals-to-finite-temperature-feasibility) connects M12, M20, M25, M27, M29 and M30 within the 12/18 split and exactly 30 milestones. This route distinguishes the target Hamiltonian from controlled $`K`$, the inherited corollary from the explicit certificate, and a sufficient feasibility bracket from an exact transition.

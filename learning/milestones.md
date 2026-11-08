# Thirty milestones through the Gibbs cancellation obstruction

The map has two phases: **M01–M12, background and preliminaries**, and **M13–M30, narrative and innovation**. The first phase grows from individual states and local generators to the complete five-qubit question. The second builds the obstruction from local linear structure to a generic theorem, then builds the approximation result from local bath directions to a system-level accuracy–relaxation law.

The sole educational anchor is Rivas–Huelga, *Open Quantum Systems: An Introduction*, first edition (2012), read through [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2). All section, equation and theorem numbers below refer to that version. The [bridge](bridge.md) develops the connections explicitly. Research citations in [related work](../references/related-work.md) support attribution and project-specific mathematics; they are not additional educational anchors.

Each milestone describes an intrinsic understanding target and its place in the proof. Dependencies indicate which earlier ideas are used, rather than personal progress or an assessment requirement.

## Phase I: background and preliminaries

### M01

**A thermal qubit in Pauli coordinates**

**Central question.** What does a Gibbs target look like as a point in a finite-dimensional operator space?

**Understanding target.** Connect $`\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2`$ with positivity, trace one, and the Gibbs state of $`H=\omega Z/2`$, whose Bloch coordinate is $`z_\beta=-\tanh(\beta\omega/2)`$. Distinguish the physical state set from the linear space containing it. This distinction later permits algebraic evaluation at $`H^{31}`$ without pretending that it is a state.

**Dependencies and story role.** Starts from finite-dimensional quantum states and matrix multiplication. It supplies the concrete local object from which both worked examples and the Pauli evaluation matrix grow.

**Conceptual connection.** Thermal probabilities are spectral weights; Pauli coordinates are a linear representation of the same operator. The proof eventually exploits both descriptions.

**Source pointers.** Rivas–Huelga [§4.3, p. 29](https://arxiv.org/pdf/1104.5242v2#page=29) for the state set and [§6.2.8, p. 73](https://arxiv.org/pdf/1104.5242v2#page=73) for the Gibbs target; [bridge: states and maps](bridge.md#states-maps-and-generators); [model: thermal target](../science/model.md#thermal-target).

### M02

**A physical map must remain physical beside another system**

**Central question.** Why is positivity on isolated states insufficient to define an allowed quantum evolution?

**Understanding target.** Identify a channel by its Kraus form and trace constraint, and interpret complete positivity through an untouched ancillary system. Understand why a linear description must work on the entire state space, including entangled extensions, rather than only on the intended Gibbs input.

**Dependencies and story role.** Uses [M01](#m01). It establishes the physical meaning of the positivity condition that will later constrain each local bath.

**Conceptual connection.** A support restriction and complete positivity are independent requirements: a map may have the right locality while failing to be physical, or be physical while acting on too many sites.

**Source pointers.** Rivas–Huelga [§4.2, Eqs. (35)–(36), pp. 26–29](https://arxiv.org/pdf/1104.5242v2#page=26); [bridge: states, maps and generators](bridge.md#states-maps-and-generators); [model: allowed controls](../science/model.md#allowed-autonomous-controls).

### M03

**A generator is an infinitesimal change, not a channel**

**Central question.** Which normalization condition survives when a channel is differentiated at time zero?

**Understanding target.** Relate the semigroup $`e^{t\mathcal L}`$ to its GKLS generator and derive $`\mathrm{Tr}\mathcal L(A)=0`$ from trace preservation. Distinguish a trace-preserving channel from a trace-annihilating generator. Recognize that the generator need not send positive operators to positive operators, although its exponential does.

**Dependencies and story role.** Uses [M01](#m01)–[M02](#m02). It prevents an incorrect dimension count or positivity constraint when the research argument passes from dynamics to a linear space of generators.

**Conceptual connection.** Tangent directions to a normalized state set have zero trace. The local stationarity problem lives in those directions, not in the set of channels.

**Source pointers.** Rivas–Huelga [§2.3, Definition 2.5, p. 8](https://arxiv.org/pdf/1104.5242v2#page=8), and [§5.2, Eqs. (45)–(46), p. 37; Eq. (51), p. 41](https://arxiv.org/pdf/1104.5242v2#page=37); [model: the larger linear space](../science/model.md#a-larger-linear-space).

### M04

**Positive coefficient matrices create physical bond baths**

**Central question.** How can a continuous family of dissipative controls be parametrized without losing complete positivity?

**Understanding target.** Express a bond dissipator in the 15 traceless Hermitian two-qubit Paulis with a Hermitian coefficient matrix $`C_b`$. Understand why $`C_b\succeq0`$ yields supported jump operators after diagonalization, and why small Hermitian perturbations of $`C_b=I_{15}`$ preserve positivity even when the perturbation alone is indefinite.

**Dependencies and story role.** Uses [M02](#m02)–[M03](#m03). It introduces the positive interior point around which the matching bath will be designed.

**Conceptual connection.** The physical generators form a constrained cone inside a larger real linear space. The obstruction can be proved in the larger space; the constructive result must return to the cone.

**Source pointers.** Rivas–Huelga [§5.2, proof of Theorem 5.1, pp. 38–40](https://arxiv.org/pdf/1104.5242v2#page=38); [construction: positive coefficient matrices](../science/local-construction.md#positive-coefficient-matrices); [bridge: positive perturbations](bridge.md#positivity-survives-a-small-carefully-chosen-perturbation).

### M05

**Preservation, uniqueness and relaxation are separate properties**

**Central question.** What is missing when a dissipator merely leaves a Gibbs state unchanged?

**Understanding target.** Analyze qubit dephasing as a generator that preserves every energy-diagonal state while failing to select the Gibbs populations. Connect stationarity to the zero eigenvalue and relaxation to a unique stationary mode with negative real parts for all other modes. Distinguish the Hamiltonian's energy differences from dissipative decay rates.

**Dependencies and story role.** Uses [M01](#m01) and [M03](#m03). It fixes the operational meaning of the exact obstruction and of the later spectral gap.

**Conceptual connection.** A Gibbs-preserving process can have extensive memory of its initial condition. Thermal preparation requires attraction, whereas the exact theorem excludes genuine dissipation even without demanding attraction.

**Source pointers.** Rivas–Huelga [§5.4, Definition 5.3, Eq. (63), Theorem 5.4, pp. 45–47](https://arxiv.org/pdf/1104.5242v2#page=45); [bridge: states, maps and generators](bridge.md#states-maps-and-generators); [interpretation: accuracy and time](../science/interpretation.md#accuracy-and-time).

### M06

**Thermal balance can require cancellation between jumps**

**Central question.** Can two completely positive dissipative contributions each disturb a target while their sum preserves it?

**Understanding target.** Follow the excitation/decay qubit example: the downward and upward drifts cancel when $`\gamma_\downarrow p_e=\gamma_\uparrow p_g`$. Neither drift vanishes separately. Understand why the analogous distinction between total and termwise stationarity remains essential for overlapping bond generators.

**Dependencies and story role.** Uses [M01](#m01), [M03](#m03) and [M05](#m05). It identifies the escape that a termwise locality obstruction leaves open and that the present evaluation-kernel theorem closes in its five-qubit model.

**Conceptual connection.** Detailed flux balance constrains a sum. Positivity of each dissipative term does not give a common sign for its action on an arbitrary mixed target.

**Source pointers.** Rivas–Huelga [§6.2.8, Eqs. (109)–(111), pp. 73–74](https://arxiv.org/pdf/1104.5242v2#page=73); [worked thermal-qubit example](bridge.md#worked-example-exact-cancellation-in-a-thermal-qubit); [why a termwise obstruction is insufficient](../science/local-kernel.md#why-the-termwise-obstruction-is-insufficient).

### M07

**Support belongs to the full jump and its induced map**

**Central question.** What exactly makes a dissipative term local to one bond?

**Understanding target.** Interpret a bond superoperator as a local map tensored with identity elsewhere. Expand the dissipator of $`L_1+L_2`$ to see why coherent sums of jumps on different bonds can create larger-support cross terms. Understand why diagonalizing $`C_b`$ within one bond preserves locality while mixing supports need not.

**Dependencies and story role.** Uses [M02](#m02)–[M04](#m04) and [M06](#m06). It converts an informal local-bath idea into the support class used by the theorem.

**Conceptual connection.** Locality is a statement about the action of a linear map on the full tensor product, not about whether each ingredient in a formal expression has a familiar local name.

**Source pointers.** Rivas–Huelga [§5.2, Eq. (51), p. 41](https://arxiv.org/pdf/1104.5242v2#page=41), with the project's support restriction in [the model](../science/model.md#allowed-autonomous-controls); [bridge: spatial support](bridge.md#spatial-support-and-energy-resolution-are-different-notions).

### M08

**Energy populations form the commutator's zero sector**

**Central question.** Which operators are slow when a weak bath is added to Hamiltonian dynamics?

**Understanding target.** Use $`\mathcal D_H(\lvert m\rangle\langle n\rvert)=-i(E_m-E_n)\lvert m\rangle\langle n\rvert`$ to separate energy populations from coherences. For a simple spectrum, identify the 32-dimensional diagonal kernel and the invertible off-diagonal block. Recognize that $`\Pi`$ is a Hilbert–Schmidt projection onto energy-diagonal operators, generally not a spatially local physical update.

**Dependencies and story role.** Uses [M03](#m03), [M05](#m05) and [M07](#m07). It supplies the block structure required by the later singular stationary perturbation.

**Conceptual connection.** The small dissipation limit has a degenerate stationary manifold. An ordinary inverse of the entire Hamiltonian commutator is unavailable; the population block must be treated separately.

**Source pointers.** Rivas–Huelga [§6.2.1, eigenoperator decomposition, p. 58](https://arxiv.org/pdf/1104.5242v2#page=58); [construction: adding weak dissipation](../science/local-construction.md#adding-weak-local-dissipation); [bridge: stationary Schur complement](bridge.md#the-stationary-schur-complement-handles-the-degenerate-limit).

### M09

**Exact Gibbs balance is stronger than population balance**

**Central question.** Which thermal condition is needed for exact stationarity, and which suffices for the weak-bath limit?

**Understanding target.** Connect the KMS relation and frequency-resolved Gibbs identities in the anchor to cancellation of the complete thermal generator. Distinguish $`\mathcal D(\rho_\beta)=0`$ from $`\Pi\mathcal D(\rho_\beta)=0`$. The latter fixes energy-population drift while permitting coherences that bias the finite-strength stationary state.

**Dependencies and story role.** Uses [M06](#m06) and [M08](#m08). It states exactly what the constructive proof will solve and why doing so does not contradict the exact obstruction.

**Conceptual connection.** The order of limits matters: long-time convergence followed by vanishing bath strength can recover the target even when no finite-strength member has it as an exact fixed point.

**Source pointers.** Rivas–Huelga [§6.2.8, pp. 73–74](https://arxiv.org/pdf/1104.5242v2#page=73); [worked weak-reset example](bridge.md#worked-example-a-weak-reset-bath); [Tupkary attribution and weak-coupling distinction](../references/related-work.md#boundary-thermalization-and-weak-coupling-limits).

### M10

**A local system–bath coupling can produce global effective jumps**

**Central question.** Why does ordinary weak-coupling thermalization not immediately refute a strictly local-generator obstruction?

**Understanding target.** Track a coupling operator through $`A(\omega)=\sum_{E_n-E_m=\omega}Q_mAQ_n`$. Understand that the projectors of an interacting system Hamiltonian generally spread its effective support. Separate microscopic coupling locality, the effective jump support, and the locality of the target Hamiltonian.

**Dependencies and story role.** Uses [M07](#m07)–[M09](#m09). It places the precise support model within the thermal-bath framework rather than presenting the theorem as a failure of thermalization in general.

**Conceptual connection.** Resolving energy transfers uses global information about an interacting spectrum. A spatially short coupling is not automatically short after that resolution.

**Source pointers.** Rivas–Huelga [§6.2.1, pp. 57–59](https://arxiv.org/pdf/1104.5242v2#page=57) and [§6.4.1, pp. 77–79](https://arxiv.org/pdf/1104.5242v2#page=77); [bridge: support and resolution](bridge.md#spatial-support-and-energy-resolution-are-different-notions); [related Gibbs samplers](../references/related-work.md#positive-gibbs-sampler-constructions-and-locality).

### M11

**Accuracy and speed require an explicit strength budget**

**Central question.** What makes a stationary-error versus relaxation-rate comparison invariant under a change of clock speed?

**Understanding target.** Fix half trace distance as the error, the induced Hilbert–Schmidt norm of the entire generator as its strength, and the smallest nonzero decay rate as the relaxation gap for an attracting generator. Understand why scaling $`\mathcal L`$ preserves its stationary state and scales its gap, and why coherent control must be charged alongside dissipation.

**Dependencies and story role.** Uses [M03](#m03), [M05](#m05) and [M08](#m08). It prepares the resource convention before any asymptotic rate claim is introduced.

**Conceptual connection.** Norm equivalence at fixed dimension can translate budgets, but the constants matter. A spectral gap controls asymptotic decay; general finite-time mixing also depends on prefactors and nonnormal behavior.

**Source pointers.** Rivas–Huelga [§2.1, induced norm and Eq. (1), pp. 4–5](https://arxiv.org/pdf/1104.5242v2#page=4), and [§5.4, Theorem 5.4 and Jordan discussion, pp. 46–47](https://arxiv.org/pdf/1104.5242v2#page=46); [accuracy account](../science/accuracy-relaxation.md#why-strength-must-be-charged).

### M12

**The complete five-qubit research question**

**Central question.** Which claim is being made about which family of states and controls?

**Understanding target.** Assemble the 51-parameter Hamiltonian family, $`d=32`$, the arbitrary one-site and adjacent-pair coherent and jump terms, and the single total stationarity equation. Distinguish the target $`H`$ from the controlled $`K`$. State the fixed-positive-temperature genericity quantifier and the separately Hamiltonian-dependent high-temperature approximation claim.

**Dependencies and story role.** Integrates [M01](#m01)–[M11](#m11). It is the system-level endpoint of the preliminary phase and fixes the question before the proof is reconstructed.

**Conceptual connection.** The result combines exact target specification, restricted support and autonomous stationary dynamics. Changing the neighborhood size, adding retained auxiliaries, or allowing general time dependence changes the question.

**Source pointers.** [Model and all three theorems](../science/model.md); [physical scope](../science/interpretation.md); [bridge: five-qubit evaluation map](bridge.md#from-one-bond-to-the-five-qubit-evaluation-map). The anchor's relevant framework is [§5.2, Eq. (51)](https://arxiv.org/pdf/1104.5242v2#page=41); the particular support model and theorem are project material.

**Finite-temperature comparison.** Keep the target Hamiltonian $`H_0`$ distinct from the controlled Hamiltonian $`K`$. The original theorem restricts both coherent terms and individual jumps; the comparison keeps strict local jumps but permits global $`K`$. Retain the 51-parameter, fixed-temperature/generic-Hamiltonian quantifiers. [Comparison model](../science/finite-temperature-feasibility.md#two-coherent-control-models).

## Phase II: narrative and innovation

### M13

**Local map directions must be counted without duplication**

**Central question.** Why does the physical local linear space have 924 dimensions rather than 960?

**Understanding target.** Derive 12 one-site and 240 two-site Hermiticity-preserving, trace-annihilating map directions. Separate the two one-site pieces from a bond to obtain 216 genuine bond directions, and use the tensor-support decomposition to obtain $`12n+216(n-1)`$. Identify the 36 redundant coordinates in the four-bond raw representation.

**Dependencies and story role.** Uses [M03](#m03), [M07](#m07) and [M12](#m12). It starts the proof from local structure and establishes the intrinsic dimension against which rank must be measured.

**Conceptual connection.** Parameter redundancy is a kernel of the representation map, present before any state is evaluated. It is not evidence of multiple stationary physical generators.

**Source pointers.** [Local-space dimension proof](../science/local-kernel.md#dimension-of-the-local-space); [bridge: the evaluation space](bridge.md#from-one-bond-to-the-five-qubit-evaluation-map). Rivas–Huelga [§5.4, Hilbert–Schmidt matrix representation, p. 46](https://arxiv.org/pdf/1104.5242v2#page=46) supplies the ambient representation language; the local count is project-specific.

### M14

**Stationarity becomes one evaluation kernel**

**Central question.** What single linear statement would rule out every possible cancellation except Hamiltonian evolution?

**Understanding target.** Form $`E_\rho(\mathcal A)=\mathcal A(\rho)`$ on $`\mathcal V`$, represent it by a $`1023\times960`$ raw matrix, and identify the compulsory direction $`\mathcal D_H=-i[H,\cdot]`$. Understand why rank 923 implies a one-dimensional intrinsic kernel even though the raw matrix has 37 null directions.

**Dependencies and story role.** Uses [M06](#m06), [M08](#m08) and [M13](#m13). It turns the physical question into the exact rank claim that all subsequent certificate steps must justify.

**Conceptual connection.** Dropping complete positivity strengthens the obstruction: absence of additional stationary maps in the larger linear space excludes all additional physical generators inside it.

**Source pointers.** Rivas–Huelga [§5.4, Eq. (63), p. 45](https://arxiv.org/pdf/1104.5242v2#page=45); [evaluation matrix](../science/local-kernel.md#evaluation-matrix); [inherited inverse-Lindblad methods](../references/related-work.md#established-stationarity-and-reconstruction-methods).

### M15

**A polynomial input gives a finite exact rank witness**

**Central question.** What useful fact can be established at $`H_0^{31}`$ even though it need not be a state?

**Understanding target.** Follow reconstruction of the integer Hamiltonian and the selected 923-minor modulo 65537, including $`i\mapsto256`$. Interpret its nonzero residue 12689 as an exact nonzero integer determinant. Understand why a polynomial input establishes a nonzero polynomial in spectral weights but does not, by itself, establish rank at Gibbs weights.

**Dependencies and story role.** Uses [M01](#m01) and [M14](#m14). It supplies the first finite input while preserving the logical gap that the algebraic transfer must still close.

**Conceptual connection.** A numerical search may discover a witness, but the proof is the independently checked exact object. A floating-point rank threshold plays no role in the conclusion.

**Source pointers.** [Certificate A](../science/gibbs-certificate.md#finite-certificate-a-a-polynomial-state-minor); [authoritative Hamiltonian](../verification/data/hamiltonian.json); [exact verification description](../verification/README.md#exact-algebraic-inputs). These are project-specific certificate ingredients beyond the anchor.

### M16

**Modular factorizations identify the eigenvalue symmetry**

**Central question.** How can three small-prime factorizations control rational relations among 32 energies?

**Understanding target.** Connect square-free modular factor degrees to Galois cycle types. Follow the roles of a transitive degree-32 action, a 31-cycle, and the transposition obtained by raising the $`(1,2,7,11,11)`$ permutation to power 77. Understand why these imply $`S_{32}`$ and why swapping two roots forces every rational relation to have equal coefficients.

**Dependencies and story role.** Uses [M15](#m15). It supplies the spectral independence information that a nonzero polynomial minor alone cannot provide.

**Conceptual connection.** The relevant symmetry is an algebraic symmetry of possible root labels, not a physical symmetry or degeneracy of the Hamiltonian. It is compatible with a simple, otherwise generic spectrum.

**Source pointers.** [Certificate B and the root-relation proof](../science/gibbs-certificate.md#finite-certificate-b-the-galois-group); [exact factor data](../verification/data/galois.json); [bridge: exponent collisions](bridge.md#symmetry-of-the-eigenvalues-prevents-exponent-collisions). This algebraic step is outside Rivas–Huelga's subject matter.

### M17

**Homogeneity removes the trace relation**

**Central question.** Why can two different determinant monomials not acquire the same Gibbs exponential?

**Understanding target.** Express the selected minor as $`P(w)`$ for $`\sigma(w)=\sum_jw_jQ_j`$. Use its homogeneous degree 923, its nonzero value at $`w_j=E_j^{31}`$, and the root relations from M16. Show that equal energy sums for two equal-degree monomials force all exponent differences to vanish, despite $`\sum_jE_j=0`$.

**Dependencies and story role.** Combines [M15](#m15) and [M16](#m16). It is the central noncancellation step before invoking exponential independence.

**Conceptual connection.** The trace-zero relation does not disappear. Homogeneity confines all competing monomials to one degree, where that relation cannot identify distinct exponent vectors.

**Source pointers.** [Nonzero homogeneous polynomial](../science/gibbs-certificate.md#a-nonzero-homogeneous-polynomial); [bridge: nonzero polynomial](bridge.md#a-finite-calculation-supplies-a-nonzero-polynomial) and [exponent collisions](bridge.md#symmetry-of-the-eigenvalues-prevents-exponent-collisions). The source for this project-specific inference is the written certificate argument.

### M18

**The exact Gibbs state inherits the nonzero minor**

**Central question.** What theorem transfers the polynomial witness to exponential thermal weights?

**Understanding target.** Apply the linear-independence form of Lindemann–Weierstrass to the distinct algebraic arguments $`-\beta\sum_jk_jE_j`$ for nonzero algebraic $`\beta`$. Track normalization by the partition function and conclude exact rank 923. Understand why the algebraicity restriction concerns the witness construction and does not restrict unknown Lindbladian coefficients to algebraic numbers.

**Dependencies and story role.** Uses [M14](#m14) and [M17](#m17). It closes the gap from a finite polynomial calculation to the actual Gibbs evaluation map.

**Conceptual connection.** The certificate proves nonvanishing through independence of exponentials, not by approximating the Gibbs state until a numerical rank appears stable.

**Source pointers.** [Transfer to the exact Gibbs state](../science/gibbs-certificate.md#transfer-to-the-exact-gibbs-state); [mathematical attribution, including the stated Lindemann–Weierstrass form](../references/related-work.md#mathematical-ingredients); [bridge: Gibbs witness](bridge.md#exponential-independence-supplies-the-actual-gibbs-witness).

### M19

**One witness becomes a generic theorem with precise quantifiers**

**Central question.** How does an exact example imply an open dense full-measure statement without claiming all Hamiltonians or all temperatures?

**Understanding target.** For a fixed real $`\beta>0`$, scale the witness to $`H_0/\beta`$ and apply the nontrivial real-analytic minor argument in 51 Hamiltonian parameters. Separately, fix a generic $`H`$ whose minor is nonzero at $`\beta=1`$ and use isolated zeros to obtain an $`H`$-dependent punctured interval near zero.

**Dependencies and story role.** Uses [M12](#m12) and [M18](#m18). It promotes the witness to the stated system-level conclusion and prepares the temperature interval needed by the matching construction.

**Conceptual connection.** “For each fixed temperature, generic in $`H`$” and “for each generic $`H`$, all sufficiently small positive temperatures” are different quantified statements. Neither supplies a uniform window or an all-temperature theorem.

**Source pointers.** [Fixed-temperature genericity](../science/gibbs-certificate.md#fixed-temperature-genericity); [one high-temperature interval](../science/gibbs-certificate.md#one-high-temperature-interval-for-a-fixed-hamiltonian); [analytic-zero-set attribution](../references/related-work.md#mathematical-ingredients).

### M20

**A Hamiltonian superoperator cannot hide physical dissipation**

**Central question.** Why does a one-dimensional linear kernel exclude every dissipative GKLS representation?

**Understanding target.** Evaluate the purity derivative on an arbitrary pure projector after the full generator has been identified as a commutator. Each jump contributes a nonnegative variance with an overall minus sign. Vanishing on every pure input forces each jump to be scalar, hence to have zero dissipator.

**Dependencies and story role.** Uses [M03](#m03), [M06](#m06) and [M19](#m19). It turns the linear theorem into a physical impossibility statement, allowing arbitrary numbers of jumps and representation freedoms.

**Conceptual connection.** The argument concerns equality of superoperators on all inputs. Applying the same inference only to the mixed target would be invalid, as the thermal-qubit cancellation example demonstrates.

**Source pointers.** Rivas–Huelga [§5.2, Eq. (51), p. 41](https://arxiv.org/pdf/1104.5242v2#page=41) for the GKLS form; [physical rigidity](../science/local-kernel.md#why-a-hamiltonian-generator-cannot-conceal-dissipation); [bridge: linear kernel to obstruction](bridge.md#from-a-linear-kernel-to-a-physical-obstruction).

**Ground-population connection.** A Gibbs eigenvector has zero diagonal commutator for every $`K`$, including a global one. Strict negativity of every allowed nonscalar jump's ground-population form prevents cancellation in that single diagonal equation. This is distinct from the full-map purity argument above. [Cold exclusion](../science/finite-temperature-feasibility.md#a-full-ground-population-form-excludes-every-colder-target).

### M21

**Exact rank and quantitative conditioning are different information**

**Central question.** What additional quantity controls how close an approximately stationary generator must be to Hamiltonian evolution?

**Understanding target.** Define $`s_\rho`$ on the Frobenius-orthogonal complement of $`\mathcal D_H`$. Distinguish this intrinsic singular value from singular values of the redundant raw matrix. Track the synthesis Gram matrix and the factor $`\sqrt{32}`$ that converts unnormalized Pauli traces to Hilbert–Schmidt coordinates.

**Dependencies and story role.** Uses [M11](#m11), [M13](#m13) and [M20](#m20). It introduces the conditioning parameter needed for a valid quantitative bound rather than mistaking a rank certificate for a useful numerical constant.

**Conceptual connection.** Injectivity on a quotient guarantees a positive minimum singular value in finite dimension, but says nothing favorable about its size. Coordinate choices cannot change the physical budget without an explicit conversion.

**Source pointers.** Rivas–Huelga [§2.1, pp. 4–5](https://arxiv.org/pdf/1104.5242v2#page=4) and [§5.4, matrix representation, p. 46](https://arxiv.org/pdf/1104.5242v2#page=46); [intrinsic versus raw matrices](../science/accuracy-relaxation.md#the-raw-matrix-is-not-an-orthonormal-superoperator-basis); [minor-inverse conversion](../verification/gap/README.md#why-a-minor-inverse-gives-a-lower-bound).

### M22

**Stationary error bounds every dissipative decay rate**

**Central question.** How does a small error in the stationary state constrain the whole spectrum of an allowed generator?

**Understanding target.** Decompose $`\mathcal L=c\mathcal D_H+\mathcal R`$ intrinsically and use $`\mathcal L(\sigma)=0`$ to bound the residual at $`\rho`$. Combine induced-norm control with $`s_\rho`$ and the skew-adjoint Hamiltonian part to obtain $`|\mathrm{Re}\lambda|\le2J\varepsilon/s_\rho`$ for every eigenvalue.

**Dependencies and story role.** Uses [M11](#m11) and [M21](#m21). It completes the converse branch by converting exact rigidity into a uniform bound over the entire allowed generator class.

**Conceptual connection.** The proof uses right eigenoperators and a quadratic-form bound, so it does not assume normality or diagonalizability. Small stationary error suppresses all decay rates, while a general mixing-time statement would require further control.

**Source pointers.** Rivas–Huelga [§2.1, Eq. (1), p. 5](https://arxiv.org/pdf/1104.5242v2#page=5); [residual estimate](../science/accuracy-relaxation.md#evaluation-controls-the-dissipative-remainder); [spectral consequence](../science/accuracy-relaxation.md#spectral-consequence); [bridge: small error](bridge.md#why-small-stationary-error-forces-small-decay-rates).

### M23

**Local observables control all 31 population directions**

**Central question.** How can 51 local Pauli observables supply every infinitesimal population correction in a 32-level energy basis?

**Understanding target.** Form $`M_{k,a}=\mathrm{Tr}(H^kP_a)`$ and use its certified rank 31. Relate it through a Vandermonde matrix to $`O_{m,a}=\langle m\rvert P_a\lvert m\rangle`$, whose columns sum to zero. Conclude that the dephased local observables span all trace-zero diagonal directions.

**Dependencies and story role.** Uses [M08](#m08), [M12](#m12) and [M15](#m15). It starts the constructive branch with a local controllability fact, independently of the positivity problem.

**Conceptual connection.** Full control of energy diagonals does not imply that the corresponding energy projectors have local spatial support. Only their projected response is being spanned.

**Source pointers.** [Population-direction proof](../science/local-construction.md#local-observables-control-every-population-direction); [exact 31-minor data](../verification/data/diagonal-minor.json); [bridge: population span](bridge.md#local-observables-span-all-population-directions). Rivas–Huelga [§6.2.1, p. 58](https://arxiv.org/pdf/1104.5242v2#page=58) supplies the energy-basis language.

### M24

**Small positive-bath perturbations generate the needed drifts**

**Central question.** Can the population directions be generated inside a neighborhood of physical bond dissipators?

**Understanding target.** For anticommuting Paulis with $`FG=iP`$, calculate the drift from $`(\delta C)_{FG}=-i/4`$ and $`(\delta C)_{GF}=i/4`$ and obtain $`\mathcal D_{\delta C}(I)=P`$. Combine these directions with the strictly positive baseline $`C_{0,b}=I_{15}`$ rather than requiring each perturbation to be physical by itself.

**Dependencies and story role.** Uses [M04](#m04) and [M23](#m23). It connects the unconstrained diagonal-span certificate to actual admissible dissipators.

**Conceptual connection.** The interior of the positive cone provides room for signed linear correction directions. Complete positivity constrains the final coefficient matrix, not every tangent direction separately.

**Source pointers.** Rivas–Huelga [§5.2, positive coefficient-matrix derivation, pp. 38–39](https://arxiv.org/pdf/1104.5242v2#page=38); [local positive matrices and the Pauli drift identity](../science/local-construction.md#positive-coefficient-matrices); [bridge: positive perturbations](bridge.md#positivity-survives-a-small-carefully-chosen-perturbation).

### M25

**An analytic local bath balances Gibbs populations exactly**

**Central question.** How can the population equation be solved while positivity survives at nonzero temperature?

**Understanding target.** Select 31 independent drift directions, invert their population-response matrix at $`\beta=0`$, and continue the linear solve analytically to obtain $`C_\beta=C_0+O(\beta)>0`$. Understand the exact equation $`\Pi\mathcal D_\beta(\rho_\beta)=0`$ and why its off-diagonal residual is allowed to remain nonzero.

**Dependencies and story role.** Uses [M09](#m09), [M23](#m23) and [M24](#m24). It gives the desired population target to a positive local reservoir and identifies the high-temperature restriction of the construction.

**Conceptual connection.** The unknown coefficients are solved collectively across bonds; individual jumps or bond terms need not preserve the Gibbs state. The population-balance mechanism is inherited weak-coupling physics, while the certified local positive realization is the project's construction.

**Source pointers.** [Exact secular balance](../science/local-construction.md#exact-secular-balance); [weak-coupling attribution](../references/related-work.md#boundary-thermalization-and-weak-coupling-limits); [bridge: population balance](bridge.md#exact-population-balance-leaves-an-admissible-coherence-drift); Rivas–Huelga [§6.2.8](https://arxiv.org/pdf/1104.5242v2#page=73) for the stronger exact thermal condition used for comparison.

**Global-control consequence.** For simple Gibbs spectrum, zero energy diagonal of $`B=\mathcal D_\beta(\rho_\beta)`$ permits exact off-diagonal cancellation by $`K_{mn}=-iB_{mn}/(p_n-p_m)`$. Verify the sign directly and explain why this generally global $`K`$ need not belong to the original local class. [Exact completion](../science/finite-temperature-feasibility.md#exact-high-temperature-preparation-with-global-coherent-control).

### M26

**The singular stationary problem has the right restricted inverses**

**Central question.** Why does adding the weak bath produce a stationary state close to the Gibbs target despite the large Hamiltonian zero eigenspace?

**Understanding target.** Use positivity of the bond coefficients and the full Pauli algebra to establish irreducibility of the population graph. Separate populations and coherences, invert $`D_Q+\eta E`$ on the off-diagonal sector, and form the stationary Schur complement on the population sector. The trace-zero classical block is invertible, giving $`\sigma_\eta=\rho_\beta+O(\eta)`$.

**Dependencies and story role.** Uses [M08](#m08), [M23](#m23) and [M25](#m25). It lifts exact secular balance to a nearby full stationary state without inverting the singular total commutator.

**Conceptual connection.** The weak-reset example makes the same mechanism visible in three Bloch equations. Distinct energy levels suffice; distinct values of every nonzero Bohr frequency are unnecessary.

**Source pointers.** [Population irreducibility](../science/local-construction.md#irreducibility-of-the-population-dynamics); [stationary block elimination](../science/local-construction.md#adding-weak-local-dissipation); [worked reset bath](bridge.md#worked-example-a-weak-reset-bath); [bridge: Schur complement](bridge.md#the-stationary-schur-complement-handles-the-degenerate-limit).

### M27

**Local depolarization supplies a global contraction margin**

**Central question.** What ensures that the constructed stationary state attracts every initial state at rate proportional to bath strength?

**Understanding target.** Derive $`\mathcal D_0=16\sum_b(\mathcal R_b-\mathrm{id})`$ from bond Pauli twirling. Every nonidentity global Pauli meets a bond, so the reference dissipator has Hilbert–Schmidt coercivity 16 on traceless operators. Preserve a positive margin under the small temperature perturbation and combine it with the skew-adjoint Hamiltonian part to obtain a contraction rate $`\eta\delta`$ and gap $`\Theta(\eta)`$.

**Dependencies and story role.** Uses [M04](#m04), [M11](#m11) and [M26](#m26). It turns the stationary construction into a relaxing physical process with a direct rate estimate.

**Conceptual connection.** This Hilbert–Schmidt contraction is proved for the constructed family. It is not inferred from complete positivity alone, and negative numerical range is used as a sufficient condition rather than as a general characterization of spectral stability.

**Source pointers.** [Direct relaxation bound](../science/local-construction.md#a-direct-relaxation-bound); [bridge: contraction estimate](bridge.md#a-direct-contraction-estimate-supplies-the-rate); Rivas–Huelga [§4.3](https://arxiv.org/pdf/1104.5242v2#page=29) for trace-norm contraction and [§5.4, Theorem 5.4](https://arxiv.org/pdf/1104.5242v2#page=46) for the distinct spectral relaxation criterion.

**Coherent-control comparison.** An arbitrary global Hermitian commutator is also Hilbert–Schmidt skew-adjoint. Exact global-$`K`$ cancellation therefore retains the same bath coercivity and proves uniqueness and attraction. Distinguish this unscaled margin from a gap after a norm budget on the full generator. [Global-control proof](../science/finite-temperature-feasibility.md#exact-high-temperature-preparation-with-global-coherent-control).

### M28

**Converse and construction determine the same error exponent**

**Central question.** How do the two proof branches establish an optimum over all allowed generators rather than a property of one family?

**Understanding target.** Rescale the complete constructed generator to a fixed budget $`J`$ while preserving its stationary state, choose $`\eta`$ proportional to the error tolerance, and combine its gap lower bound with M22. Obtain $`\Gamma_{H,\beta,J}(\varepsilon)=\Theta(\varepsilon)`$ at fixed $`H`$, $`\beta`$ and $`J`$. Use the converse again to infer that the family's actual error is $`\Omega(\eta)`$.

**Dependencies and story role.** Combines [M19](#m19), [M22](#m22), [M26](#m26) and [M27](#m27). It is the global endpoint of the constructive argument and states its exact high-temperature quantifier.

**Conceptual connection.** The control Hamiltonian may be rescaled because $`K`$ need not equal the target Hamiltonian $`H`$. Constants and the admissible temperature interval depend on $`H`$; the theorem is an accuracy asymptotic at fixed parameters.

**Source pointers.** [Fixed strength and the matching law](../science/local-construction.md#fixed-strength-and-the-matching-law); [generic temperature quantifiers](../science/local-construction.md#generic-hamiltonians-and-temperature-quantifiers); [Theorem 3](../science/model.md#theorem-3-matching-high-temperature-frontier).

### M29

**Rigorous finite constants have a separate evidential role**

**Central question.** What does an interval certificate add to the exact theorem, and what does it leave unresolved?

**Understanding target.** Distinguish the algebraic rank proof, Arb inverse-minor bounds, positive coefficient enclosures, and the continuous construction interval. Read the explicit two rational-temperature examples as directed inequalities. Understand that coefficient balls enclose an exact analytic prescription; arbitrary rounded numbers inside them need not satisfy secular balance exactly.

**Dependencies and story role.** Uses [M15](#m15), [M18](#m18), [M21](#m21) and [M28](#m28). It connects the theorem to reproducible finite examples without replacing analytical inference by a numerical success flag.

**Conceptual connection.** Certified does not mean sharp. At $`\beta=3/1000`$, the constructive prefactor is at least $`0.0954`$, while the converse prefactor is $`2.0532\times10^{21}`$. The positivity interval $`0\le\beta\le0.01`$ certifies the bath construction, not full evaluation rank throughout that real interval.

**Source pointers.** [Quantitative witness](../science/quantitative-witness.md); [verification guide](../verification/README.md); [exact reservoir prescription](../verification/construction/README.md); [bridge: practical constants](bridge.md#what-the-certified-constants-do-and-do-not-say).

**Ground/thermal evidence.** Read the complete certified energy spectrum, nine marginal spectra, thermal deficit and four positive-LDL margins in the [ground/thermal certificate](../verification/ground-thermal/README.md). Explain why the inherited $`\mu/2`$ theorem supplies the approximation floor, while monotonicity of the exact population forms extends a single endpoint certificate to every real $`\beta\ge12/5`$. Neither role changes the distinction between the reservoir interval and evaluation rank, nor makes the original loose gap constants sharp.

### M30

**The physical conclusion and its boundaries fit together**

**Central question.** What has been established about local thermalization, and which nearby questions remain distinct?

**Understanding target.** Synthesize total cancellation, generic five-qubit rigidity, the bounded-strength accuracy frontier, and the limits of its constants. Explain why five is the first size permitted by the dimension count but supplies no induction to larger chains. Keep the maximally mixed endpoint, commuting targets, larger neighborhoods, quasi-local jumps, retained auxiliaries and time-dependent preparation separate from the proved model.

**Dependencies and story role.** Integrates [M12](#m12), [M19](#m19), [M20](#m20) and [M28](#m28)–[M29](#m29). It closes the narrative at the level of the complete physical claim and its comparison with existing thermalization methods.

**Conceptual connection.** An exact finite-system obstruction and a sharp asymptotic exponent can be meaningful without demonstrating a thermodynamic theorem, necessary quasi-local tails, or a practically large speed separation. The order of the fixed-temperature and vanishing-error limits remains part of the conclusion.

**Source pointers.** [Physical interpretation and boundaries](../science/interpretation.md); [related work and attribution](../references/related-work.md); [all main theorem statements](../science/model.md); [bridge: final quantitative interpretation](bridge.md#what-the-certified-constants-do-and-do-not-say).

**Finite-temperature synthesis.** Also combine [M25](#m25) and [M27](#m27) for exact attractive global-$`K`$ preparation on $`0\le\beta\le1/100`$, and [M20](#m20) and [M29](#m29) for global-$`K`$ exclusion of genuine dissipation on every real $`\beta\ge12/5`$. State the inherited stationary thermal accuracy floor and the local/global coherent-control separation. The intervening feasibility and exact transition remain unresolved; monotone witness forms do not prove a monotone complete feasible set. [Full comparison](../science/finite-temperature-feasibility.md).

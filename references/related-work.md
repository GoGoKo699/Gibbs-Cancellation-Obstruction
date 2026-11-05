# Related work and attribution

## Question and scope

The question here is whether a prescribed Gibbs state of a nearest-neighbor Hamiltonian can be stationary under a time-independent generator built from nearest-neighbor terms, allowing different terms to cancel. The system is an open chain of five qubits. Both the coherent terms and each individual jump operator are restricted to an adjacent pair or a single site. Detailed balance and stationarity of each summand are not assumed.

For each fixed inverse temperature $\beta>0$, the result identifies an open dense, full-measure set of Hamiltonians for which the only local Hermiticity-preserving, trace-annihilating superoperators annihilating the Gibbs state are multiples of the Hamiltonian commutator. It therefore excludes dissipative exact stabilization in this model. With a fixed bound on the total generator's induced Hilbert–Schmidt norm, the spectral relaxation gap is at most proportional to stationary half-trace-distance error. At sufficiently high temperature, a positive local dissipator gives a matching linear dependence. The temperature interval and constants may depend on the Hamiltonian; no uniform temperature or system-size bound is asserted.

These are finite-system results. They do not establish an all-size obstruction, exclude larger fixed neighborhoods, or prove that quasi-local tails are necessary.

## Established stationarity and reconstruction methods

The GKLS form is the established characterization of generators of completely positive, trace-preserving Markov semigroups [GKS76, L76]. Expressing stationarity as linear equations in generator coefficients is also established. Bairey et al. [B20, Eq. (6)] use local expectation values to reconstruct local Lindbladians from steady states. Souza and Iemini [SI26, Sec. II, Eq. (10)] construct a Gram matrix whose kernel solves the linear inverse-Lindblad problem, and explicitly explain how an empty kernel can certify that a chosen ansatz cannot preserve a target. Complete positivity requires an additional constraint on the dissipative coefficients.

Those methods are antecedents of the evaluation map used here. The additional result is a certified maximal-rank statement for the **Gibbs family of generic five-qubit nearest-neighbor Hamiltonians**, despite its obligatory Hamiltonian-commutator kernel. The constraint-matrix construction itself is not a new contribution.

## Local stabilization and frustration freeness

Johnson, Ticozzi and Viola [JTV16] give a necessary and sufficient criterion for frustration-free local stabilization of full-rank mixed states. Their neighborhood terms individually preserve the target. Section 5.3 explains why even commuting Gibbs states may require generator neighborhoods larger than the Hamiltonian interactions; Section 5.4.2 studies noncommuting finite-chain Gibbs examples. Their result therefore establishes an important part of the locality problem while retaining a termwise invariance assumption.

The related [Gibbs-Locality-Obstruction](https://github.com/GoGoKo699/Gibbs-Locality-Obstruction) project studies exact local updates that individually preserve a Gibbs state. The present question allows the actions of different local generator terms to cancel. The generic one-dimensional evaluation kernel rules out that escape within the stated five-qubit, adjacent-pair model.

Guo et al. [G25] develop stationary-state engineering beyond Davies generators, including time-reversal-breaking dynamics. Their general eigenbasis construction need not be local. Their explicit local construction in Sec. 3.2 assumes a commuting local modular Hamiltonian. Thus the present work does not introduce the idea of engineering dynamics beyond detailed balance; it establishes an obstruction for a generic noncommuting target under a specified support constraint.

## Boundary thermalization and weak-coupling limits

Carlen, Huse and Lebowitz [CHL25, Theorem 1 and Corollary 2] prove an exact Gibbs-state obstruction when an ergodic dissipator acts on one proper subsystem. A stationary state commuting with the system Hamiltonian must then factor across the dissipative subsystem and its complement. Here dissipators may overlap and cover every bond, so that boundary-versus-bulk factorization argument does not apply directly.

Tupkary et al. [T23, Sec. IV and Appendix D] formulate a thermalization optimization problem for boundary-supported Lindblad dynamics. Their thermalization condition takes the long-time limit and then the vanishing-coupling limit. It imposes energy-population balance, $\langle E_j|\mathcal D(\rho_\beta)|E_j\rangle=0$, rather than exact finite-coupling stationarity, $\mathcal D(\rho_\beta)=0$.

This distinction is central to the matching construction here. A local dissipator is chosen so its secular population dynamics preserves the Gibbs weights; the full stationary state then differs from the Gibbs state by order of the dissipative strength. The weak-coupling mechanism and population-balance condition are established ideas. The contribution is their completely positive realization for the certified Hamiltonian family and the matching upper bound on the relaxation gap over all generators in the stated class.

## Positive Gibbs-sampler constructions and locality

Chen, Kastoryano and Gilyén [CKG25] construct exact noncommuting Gibbs samplers with quasi-local terms. Their spatial tails allow behavior outside the adjacent-pair model; truncating those tails can spoil exact balance. Bertoni and De Palma [BDP26, Definition 3.5] similarly use dressed jumps $A_P=\rho_\beta^{1/4}P\rho_\beta^{-1/4}$. A local proposal $P$ does not make the dressed jump strictly local for a general noncommuting Hamiltonian.

Arad, Firanko and Gurevich [AFG26, Theorem 3.1] study the converse direction: the effective Gibbs Hamiltonian generated by local channels. Its order-$k$ perturbative coefficient has geometrical support at most $k+1$. Their general exponential bound on the coefficient norms is an additional conjectural condition, not part of that support theorem. This is compatible with longer-range effective interactions arising from local dynamics and does not settle exact realizability of a prescribed nearest-neighbor Gibbs target.

Ding, Li and Zhang [DLZ26] prepare one-dimensional Gibbs states using resettable bath ancillas at every site and randomized interaction times. Their approximate preparation result concerns a different operational model. It neither contradicts the present same-system autonomous-generator obstruction nor establishes that ancillas are necessary.

## Mathematical ingredients

The certification uses standard finite-field rank tests, elementary Galois-group arguments, the classical Lindemann–Weierstrass theorem, and real-analytic genericity. The needed form of Lindemann–Weierstrass is linear independence, over algebraic coefficients, of exponentials at distinct algebraic arguments; see [BR89]. The measure-zero property of a nontrivial real-analytic zero set is recorded in [M20]. These ingredients establish a Gibbs witness and then genericity; they do not require the unknown generator coefficients to be algebraic.

The high-temperature continuation uses finite-dimensional positivity, a Schur complement, analytic inversion and dissipative coercivity. It does not require nondegeneracy of all Bohr frequencies. Neither the elementary perturbation tools nor the inherited inverse-Lindblad framework are claimed as new methods.

## References

- **[GKS76]** V. Gorini, A. Kossakowski and E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, Journal of Mathematical Physics **17**, 821–825 (1976). [DOI](https://doi.org/10.1063/1.522979).
- **[L76]** G. Lindblad, *On the generators of quantum dynamical semigroups*, Communications in Mathematical Physics **48**, 119–130 (1976). [DOI](https://doi.org/10.1007/BF01608499).
- **[B20]** E. Bairey, C. Guo, D. Poletti, N. H. Lindner and I. Arad, *Learning the dynamics of open quantum systems from their steady states*, New Journal of Physics **22**, 032001 (2020). [DOI](https://doi.org/10.1088/1367-2630/ab73cd); [preprint](https://arxiv.org/abs/1907.11154).
- **[SI26]** L. da Silva Souza and F. Iemini, *Lindbladian reverse engineering for general non-equilibrium steady states: A scalable null-space approach*, SciPost Physics **20**, 009 (2026). [DOI](https://doi.org/10.21468/SciPostPhys.20.1.009); [preprint v2](https://arxiv.org/abs/2408.05302v2).
- **[JTV16]** P. D. Johnson, F. Ticozzi and L. Viola, *General fixed points of quasi-local frustration-free quantum semigroups: from invariance to stabilization*, Quantum Information and Computation **16**, 657–699 (2016). [DOI](https://doi.org/10.26421/QIC16.7-8-5); [preprint v2](https://arxiv.org/abs/1506.07756v2).
- **[G25]** J. Guo, O. Hart, C.-F. Chen, A. J. Friedman and A. Lucas, *Designing open quantum systems with known steady states: Davies generators and beyond*, Quantum **9**, 1612 (2025). [DOI](https://doi.org/10.22331/q-2025-01-28-1612); [preprint v2](https://arxiv.org/abs/2404.14538v2).
- **[CHL25]** E. A. Carlen, D. A. Huse and J. L. Lebowitz, *Stationary states of boundary-driven quantum systems: Some exact results*, Physical Review A **111**, 012210 (2025). [DOI](https://doi.org/10.1103/PhysRevA.111.012210); [preprint v2](https://arxiv.org/abs/2408.06887v2).
- **[T23]** D. Tupkary, A. Dhar, M. Kulkarni and A. Purkayastha, *Searching for Lindbladians obeying local conservation laws and showing thermalization*, Physical Review A **107**, 062216 (2023). [DOI](https://doi.org/10.1103/PhysRevA.107.062216); [preprint](https://arxiv.org/abs/2301.02146).
- **[CKG25]** C.-F. Chen, M. J. Kastoryano and A. Gilyén, *Efficient quantum thermal simulation*, Nature **646**, 561–566 (2025). [DOI](https://doi.org/10.1038/s41586-025-09583-x); [preprint](https://arxiv.org/abs/2311.09207).
- **[BDP26]** N. Bertoni and G. De Palma, *Rapid mixing for Gibbs samplers for quantum spin systems with all-to-all interactions*, arXiv:2610.40361v1 (2026). [Preprint](https://arxiv.org/abs/2610.40361v1).
- **[AFG26]** I. Arad, R. Firanko and O. Gurevich, *Local quantum channels giving rise to quasi-local Gibbs states*, Journal of Mathematical Physics **67**, 101902 (2026). [DOI](https://doi.org/10.1063/5.0274879); [preprint](https://arxiv.org/abs/2408.08672).
- **[DLZ26]** Z. Ding, B. Li and R. Zhang, *Efficient thermalization of one-dimensional noncommuting Hamiltonians via system-bath interactions with $\Theta(n)$ ancilla qubits*, arXiv:2611.03422v1 (2026). [Preprint](https://arxiv.org/abs/2611.03422v1).
- **[BR89]** J.-P. Bézivin and P. Robba, *A new p-adic method for proving irrationality and transcendence results*, Annals of Mathematics **129**, 151–160 (1989). [DOI](https://doi.org/10.2307/1971488); [publisher statement](https://annals.math.princeton.edu/1989/129-1/p05).
- **[M20]** B. S. Mityagin, *The Zero Set of a Real Analytic Function*, Mathematical Notes **107**, 529–530 (2020). [DOI](https://doi.org/10.1134/S0001434620030189); [preprint](https://arxiv.org/abs/1512.07276).

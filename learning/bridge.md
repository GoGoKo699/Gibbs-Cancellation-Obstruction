# From quantum Markov semigroups to a Gibbs cancellation obstruction

The central issue is spatial. A Gibbs state is stationary under its own Hamiltonian, and many quantum Markov generators have unique thermal fixed points. The question here is whether **strictly adjacent-pair controls on the original five qubits** can have the prescribed interacting Gibbs state as a stationary state when all local contributions are allowed to cancel.

For a generic Hamiltonian at a fixed positive inverse temperature, the only stationary generator in a much larger local linear space is a multiple of the Hamiltonian commutator. This excludes genuine dissipation. At sufficiently high temperature, approximate stationary preparation remains possible, with optimal relaxation gap proportional to the allowed error under a fixed bound on the entire generator.

This bridge connects those statements to Rivas and Huelga, *Open Quantum Systems: An Introduction*, first edition (2012), using the authors' [open preprint v2](https://arxiv.org/abs/1104.5242v2). All source numbers below refer to that preprint. The [milestones](milestones.md) organize the same argument into 12 background and 18 research-narrative targets; the [scientific account](../science/README.md) contains the authoritative statements and certificates.

## What the selected anchor supplies

Rivas–Huelga develops the passage from linear maps to continuous quantum dynamics, complete positivity, generator structure, steady states, and thermal weak-coupling dynamics. The project uses that passage, then adds spatial support constraints and a particular exact certificate.

| Needed connection | Precise anchor location | Project use |
|---|---|---|
| Norms and induced map norms | §2.1, pp. 4–5, Eq. (1) | Convert a small state error into a small stationarity residual |
| Exponentials and semigroups | §§2.2–2.3, pp. 6–10, Definition 2.5 | Interpret a time-independent generator through its full dynamics |
| Completely positive, trace-preserving maps | §4.2, pp. 26–29, Eqs. (35)–(36) | Specify physical evolutions on a system that may be entangled with another |
| Generator structure and positive coefficient matrices | §5.2, pp. 37–41, Theorem 5.1 and Eq. (51) | Construct physical local baths and identify their linear ambient space |
| Stationarity and relaxation | §5.4, pp. 45–50, Definition 5.3, Eq. (63), Theorem 5.4 | Separate preserving the target from attracting other states |
| Frequency components of a coupling | §6.2.1, pp. 57–59 | Explain why microscopic local coupling need not yield local effective jumps |
| Thermal balance | §6.2.8, pp. 73–74, Eqs. (109)–(111) | Compare exact Davies balance with the weaker population condition used here |
| Coupled subsystems | §6.4.1, pp. 77–79 | Keep the system Hamiltonian and coupling regime explicit |

Several conventions require translation. The project uses $`H`$ for the Hamiltonian defining the thermal target and $`K`$ for the independently chosen coherent part of a generator. Here $`\beta`$ always means inverse temperature; the symbol $`\beta`$ in the anchor's §6.4.1 instead denotes an intersystem coupling strength. The parameter $`\eta`$ below multiplies a dissipator in the effective generator. It is a rate parameter, not automatically the microscopic coupling amplitude whose square appears in a weak-coupling derivation. Units satisfy $`\hbar=k_B=1`$.

## States, maps and generators

A density operator is positive semidefinite and has trace one. For a qubit,

```math
\rho=\frac12(I+xX+yY+zZ),\qquad x^2+y^2+z^2\le1.
```

The Pauli coordinates make state differences and linear maps concrete. On five qubits, the 1024 Pauli strings similarly form a basis of operator space. With $`d=32`$, the normalized strings $`P_\mu/\sqrt d`$ are orthonormal for

```math
\langle A,B\rangle_{\mathrm{HS}}=\mathrm{Tr}(A^\dagger B).
```

Hermiticity-preserving maps have real matrices in a Hermitian Pauli basis. This allows the stationarity problem to become real linear algebra without assuming that the Hamiltonian itself has real entries in the computational basis.

A physical channel $`\Phi`$ has a Kraus representation

```math
\Phi(A)=\sum_\alpha K_\alpha A K_\alpha^\dagger,
\qquad \sum_\alpha K_\alpha^\dagger K_\alpha=I.
```

These are the conditions in [Rivas–Huelga §4.2, Eqs. (35)–(36)](https://arxiv.org/pdf/1104.5242v2#page=26). Complete positivity means that $`\Phi\otimes\mathrm{id}`$ remains positive on any larger system, including entangled inputs.

A time-independent Markov semigroup has $`\Phi_t=e^{t\mathcal L}`$. Differentiating trace preservation gives

```math
\mathrm{Tr}\mathcal L(A)=0
\quad\text{for every }A.
```

Thus $`\mathcal L`$ is **trace annihilating**, while $`e^{t\mathcal L}`$ is trace preserving. The generator itself is generally not a positive map. The [GKLS form in §5.2, Eq. (51)](https://arxiv.org/pdf/1104.5242v2#page=41) is

```math
\mathcal L(A)=-i[K,A]+\sum_\alpha\mathcal D[L_\alpha](A),
```

```math
\mathcal D[L](A)=LAL^\dagger-\frac12\{L^\dagger L,A\}.
```

For a prescribed state $`\rho`$, stationarity is the single linear equation $`\mathcal L(\rho)=0`$. A relaxing semigroup additionally converges to one stationary state from every initial density operator. Rivas–Huelga makes that distinction in [§5.4, Definition 5.3 and Eq. (63)](https://arxiv.org/pdf/1104.5242v2#page=45).

For example, $`\mathcal D[Z](\rho)=Z\rho Z-\rho`$ removes a qubit's $`X`$ and $`Y`$ components but leaves its $`Z`$ component unchanged. Every state diagonal in $`Z`$ is stationary. A diagonal Gibbs state is preserved, yet its populations are not selected. This is why finding a stationary state alone does not establish thermalization.

## Worked example: exact cancellation in a thermal qubit

Let $`H=(\omega/2)Z`$ with $`\omega>0`$, and label its ground and excited states by $`\lvert g\rangle`$ and $`\lvert e\rangle`$. Their energies are $`-\omega/2`$ and $`+\omega/2`$. The Gibbs state has populations

```math
\rho_\beta=p_g\lvert g\rangle\langle g\rvert
+p_e\lvert e\rangle\langle e\rvert,
\qquad
\frac{p_e}{p_g}=e^{-\beta\omega},
\qquad p_g+p_e=1.
```

Use the two physical jumps

```math
L_- =\sqrt{\gamma_\downarrow}\lvert g\rangle\langle e\rvert,
\qquad
L_+ =\sqrt{\gamma_\uparrow}\lvert e\rangle\langle g\rvert,
\qquad \gamma_\uparrow,\gamma_\downarrow>0.
```

In this example choose the coherent control $`K=H`$, so the full generator is

```math
\mathcal L=-i[H,\cdot]+\mathcal D[L_-]+\mathcal D[L_+].
```

Writing $`P_g=\lvert g\rangle\langle g\rvert`$ and $`P_e=\lvert e\rangle\langle e\rvert`$ gives

```math
\mathcal D[L_-](\rho_\beta)
=\gamma_\downarrow p_e(P_g-P_e),
```

```math
\mathcal D[L_+](\rho_\beta)
=\gamma_\uparrow p_g(P_e-P_g).
```

Each jump disturbs the thermal state. Their sum vanishes precisely when

```math
\gamma_\downarrow p_e=\gamma_\uparrow p_g,
\qquad
\frac{\gamma_\uparrow}{\gamma_\downarrow}=e^{-\beta\omega}.
```

The population equation is

```math
\dot p_e=-\gamma_\downarrow p_e+\gamma_\uparrow(1-p_e).
```

It has the unique equilibrium $`p_e=\gamma_\uparrow/(\gamma_\uparrow+\gamma_\downarrow)`$. Coherences decay at rate $`(\gamma_\uparrow+\gamma_\downarrow)/2`$ while rotating at frequency $`\omega`$. The complete generator is therefore relaxing, with the exact Gibbs state and gap $`(\gamma_\uparrow+\gamma_\downarrow)/2`$.

This elementary calculation expresses the balance mechanism behind [§6.2.8](https://arxiv.org/pdf/1104.5242v2#page=73). It also establishes an essential point for the project: complete positivity does not force the contribution of each jump to vanish on a mixed stationary state. Cancellation can occur among positive dissipative terms. The five-qubit theorem must exclude that possibility through the total generator; a termwise argument would not suffice. The qubit example is an allowed small-system thermalizer, outside the five-qubit theorem's scope.

## Spatial support and energy resolution are different notions

A local map on a bond acts as the identity superoperator on all other sites. A jump on that bond therefore produces a bond-supported dissipator. Diagonalizing a positive coefficient matrix within one bond preserves this support.

By contrast, combining jumps from distinct supports coherently can change the model. For $`L=L_1+L_2`$, the term $`LAL^\dagger`$ contains $`L_1AL_2^\dagger`$ and $`L_2AL_1^\dagger`$. These cross terms generally act on the union of the two supports. The support restriction applies to each **individual jump**, as well as to each term of $`K`$; it is not merely a restriction on a list of ingredients from which a larger jump is assembled.

Thermal weak-coupling generators raise a second locality issue. In [Rivas–Huelga §6.2.1](https://arxiv.org/pdf/1104.5242v2#page=58), a system coupling operator $`A`$ is decomposed as

```math
A(\omega)=\sum_{E_n-E_m=\omega}Q_m A Q_n,
\qquad [H,A(\omega)]=-\omega A(\omega),
```

where $`Q_m`$ are spectral projectors of the **whole system**. The frequency components enter the thermal generator. Even if $`A`$ initially acts on one site, the projectors of a generic interacting $`H`$ are global, and $`A(\omega)`$ need not retain the original spatial support.

The thermal identities in [§6.2.8, Eqs. (109)–(111)](https://arxiv.org/pdf/1104.5242v2#page=74) then balance the full frequency-resolved dissipator. They do not establish the existence of a strictly adjacent-pair generator. The coupled-system discussion in [§6.4.1](https://arxiv.org/pdf/1104.5242v2#page=77) makes the choice of system Hamiltonian and coupling regime explicit. This resolves the apparent tension between ordinary thermal-bath constructions and the support restriction studied here.

## From one bond to the five-qubit evaluation map

The target Hamiltonians have arbitrary real one-site and nearest-neighbor Pauli coefficients:

```math
H=\sum_{j=1}^{5}\sum_{a=1}^{3}h_{j,a}P_a^{(j)}
+\sum_{j=1}^{4}\sum_{a,b=1}^{3}J_{j,ab}P_a^{(j)}P_b^{(j+1)}.
```

There are $`5\cdot3+4\cdot9=51`$ parameters. The prescribed state is $`\rho_\beta(H)=e^{-\beta H}/\mathrm{Tr}e^{-\beta H}`$. The allowed coherent Hamiltonian $`K`$ may be chosen independently, with the same support restriction. No detailed balance or termwise Gibbs preservation is required. See the [complete model](../science/model.md).

It is useful first to discard positivity and work in the larger real vector space $`\mathcal V`$ of all sums of local Hermiticity-preserving, trace-annihilating maps. On one qubit, a map is a real $`4\times4`$ matrix. Trace annihilation removes its identity-output row, leaving $`3\cdot4=12`$ dimensions. On a pair, the analogous count is $`15\cdot16=240`$.

The one-site directions must be counted only once when neighboring bonds overlap. Separating each bond's two one-site pieces leaves $`240-2\cdot12=216`$ genuine two-site directions. The tensor-support decomposition in [the local-space proof](../science/local-kernel.md#dimension-of-the-local-space) establishes their independence, giving

```math
\dim\mathcal V_n=12n+216(n-1),
\qquad \dim\mathcal V_5=924.
```

The target of evaluation is the 1023-dimensional space of traceless Hermitian operators:

```math
E_\rho:\mathcal V\longrightarrow\mathrm{Herm}_0,
\qquad E_\rho(\mathcal A)=\mathcal A(\rho).
```

The commutator $`\mathcal D_H=-i[H,\cdot]`$ belongs to $`\mathcal V`$ and annihilates every function of $`H`$. For $`H\ne0`$, the evaluation kernel therefore has dimension at least one. The desired statement is that it has **exactly** one dimension.

Four raw bond bases give $`4\cdot240=960`$ columns. They contain 36 representation redundancies, so a 37-dimensional raw null space would correspond to a one-dimensional intrinsic kernel. The certificate accordingly seeks rank 923, not rank 959. Different raw coefficient vectors can represent the same physical map; a nonzero gauge vector can represent the zero superoperator. That freedom is unrelated to an additional stationary generator.

The inverse-Lindblad use of linear stationarity constraints is established in earlier work. The [attribution account](../references/related-work.md#established-stationarity-and-reconstruction-methods) distinguishes that framework from the present Gibbs-family rank theorem.

## How an exact finite certificate reaches a Gibbs state

The main difficulty is not forming a matrix. It is proving its rank at an exponential state, where very small numerical singular values can conceal exact dependencies. The proof has two finite inputs that feed a single analytical argument.

| Proof stage | Evidence used | What follows |
|---|---|---|
| Local-map branch | A nonzero finite-field minor at a polynomial input | The selected homogeneous polynomial on spectral weights is nonzero |
| Spectral branch | Modular factorizations determine the full symmetric Galois group | The only rational energy relation is the trace relation |
| Join the branches | Equal monomial degrees and the energy-relation constraint | Different determinant monomials have distinct energy sums |
| Transfer to Gibbs weights | Lindemann–Weierstrass independence of exponentials | At a nonzero algebraic inverse temperature, the selected Gibbs evaluation minor is nonzero |
| Pass to generic Hamiltonians | Witness scaling and real-analytic genericity | At each fixed positive inverse temperature, the generic local stationarity kernel is one dimensional |

### A finite calculation supplies a nonzero polynomial

The [integer Hamiltonian witness](../verification/data/hamiltonian.json) is a particular member $`H_0`$ of the 51-parameter family. The raw evaluation matrix at $`H_0^{31}`$ has a selected $`923\times923`$ minor equal to $`12689`$ modulo the prime $`65537`$. Gaussian-integer arithmetic is reduced by sending $`i`$ to $`256`$, whose square is $`-1`$ in that field. A nonzero residue proves that the corresponding integer determinant is nonzero.

The input $`H_0^{31}`$ is not asserted to be a density operator. Its role is algebraic. Write

```math
H_0=\sum_{j=1}^{32}E_jQ_j,
\qquad \sigma(w)=\sum_{j=1}^{32}w_jQ_j.
```

The same selected minor evaluated at $`\sigma(w)`$ is a homogeneous polynomial $`P(w)`$ of degree 923 with algebraic coefficients. The finite calculation proves

```math
P(E_1^{31},\ldots,E_{32}^{31})\ne0,
```

so $`P`$ is not identically zero. This is all that the nonphysical polynomial input needs to establish.

### Symmetry of the eigenvalues prevents exponent collisions

The characteristic polynomial of $`H_0`$ has square-free irreducible-factor degrees $`(1,31)`$ modulo 19, $`(1,2,7,11,11)`$ modulo 43, and $`(32)`$ modulo 373. These exact patterns certify that its Galois group is $`S_{32}`$.

The argument can be read as a permutation calculation. Irreducibility gives transitivity. A 31-cycle fixes one root and permutes all the others transitively, so its point stabilizer is transitive and the full action is doubly transitive. Raising a permutation of type $`(1,2,7,11,11)`$ to the 77th power leaves just a transposition. Conjugating that transposition by a doubly transitive group gives every transposition, hence the whole symmetric group.

Consequently, the only rational linear relations among the eigenvalues are multiples of their trace-zero relation. If $`\sum_jq_jE_j=0`$, apply the Galois automorphism interchanging $`E_i`$ and $`E_j`$ and subtract. Distinct eigenvalues imply $`q_i=q_j`$ for every pair.

Now consider two different monomials $`w^k`$ and $`w^\ell`$ of the same degree 923. Equality of their energy sums would give

```math
\sum_j(k_j-\ell_j)E_j=0.
```

All coefficients would have to be equal. Their sum is zero because the monomials have equal degree, so each coefficient would be zero. This contradicts $`k\ne\ell`$. **Homogeneity removes the one trace relation that otherwise remains.**

### Exponential independence supplies the actual Gibbs witness

For nonzero algebraic $`\beta`$, the distinct numbers $`-\beta\sum_jk_jE_j`$ are algebraic. The linear-independence form of Lindemann–Weierstrass gives

```math
P(e^{-\beta E_1},\ldots,e^{-\beta E_{32}})
=\sum_k a_k e^{-\beta\sum_jk_jE_j}\ne0.
```

Normalizing the Gibbs weights divides this homogeneous determinant by a positive power of the partition function and cannot change whether it vanishes. The selected Gibbs minor is therefore nonzero. The compulsory commutator direction gives the matching upper rank bound, so the intrinsic kernel is exactly one dimensional.

This argument constrains the chosen witness, not the coefficients of a proposed physical generator. Once the real evaluation matrix has rank 923, its kernel statement applies to arbitrary real generator coefficients, including coefficients chosen with full knowledge of the target.

### One witness yields the correct genericity statement

For any prescribed real $`\beta>0`$, the Hamiltonian $`H_0/\beta`$ has

```math
\rho_\beta(H_0/\beta)=\rho_1(H_0).
```

The same selected minor, as a function of the 51 real Hamiltonian coefficients at that fixed temperature, is real analytic and nonzero somewhere. Its zero set has measure zero and empty interior. The nonzero set is open, dense and full measure.

This proves the fixed-temperature generic theorem. For the high-temperature construction, one instead fixes a generic $`H`$ whose minor is nonzero at $`\beta=1`$. The minor is then a nontrivial analytic function of $`\beta`$. Its zero at $`\beta=0`$ has finite order, so it is nonzero on some punctured interval near zero. The interval depends on $`H`$; a common generic set for all positive temperatures is not being asserted.

The [certificate proof](../science/gibbs-certificate.md) supplies these steps in full. The [mathematical references](../references/related-work.md#mathematical-ingredients) credit the transcendence and analytic-zero-set facts. The [verifier](../verification/README.md#exact-algebraic-inputs) checks finite inputs; it does not replace the written transfer and genericity arguments.

## From a linear kernel to a physical obstruction

The rank theorem gives an identity of superoperators,

```math
\mathcal L=c\mathcal D_H
```

for every allowed stationary generator, with $`c\in\mathbb R`$. It remains to show that a GKLS representation cannot hide a genuine dissipator inside that identity.

For an arbitrary pure projector $`P=\lvert\psi\rangle\langle\psi\rvert`$,

```math
\mathrm{Tr}\bigl(P\mathcal L(P)\bigr)
=-\sum_\alpha\left(
\langle\psi\rvert L_\alpha^\dagger L_\alpha\lvert\psi\rangle
-\left|\langle\psi\rvert L_\alpha\lvert\psi\rangle\right|^2
\right).
```

Each bracket is nonnegative by Cauchy–Schwarz. A Hamiltonian commutator makes the left-hand side zero for every pure input. Therefore each jump maps every vector to a multiple of itself. Comparing basis vectors and their sums forces each jump to be a scalar multiple of $`I`$, whose dissipator is zero.

The order of this argument matters. It does not infer trivial jumps from the vanishing drift of the mixed Gibbs state. The thermal-qubit example already rules out that inference. It first identifies the **entire superoperator** as Hamiltonian, then uses its action on every pure state. The [physical-rigidity proof](../science/local-kernel.md#why-a-hamiltonian-generator-cannot-conceal-dissipation) makes this final positivity step explicit.

## Why small stationary error forces small decay rates

The exact result becomes quantitative through conditioning of evaluation. Use the Hilbert–Schmidt norm on operators, its induced norm on generators, and the associated Frobenius metric on superoperator matrices. Let $`s_\rho>0`$ be the least singular value of $`E_\rho`$ on the Frobenius-orthogonal complement of $`\mathcal D_H`$.

Decompose an allowed generator as

```math
\mathcal L=c\mathcal D_H+\mathcal R,
\qquad \mathcal R\perp\mathcal D_H.
```

For a stationary state $`\sigma`$, a strength bound $`\lVert\mathcal L\rVert_{2\to2}\le J`$, and half-trace-distance error $`\tfrac12\lVert\sigma-\rho\rVert_1\le\varepsilon`$,

```math
\begin{aligned}
\lVert\mathcal R\rVert_{2\to2}
&\le\lVert\mathcal R\rVert_{\mathrm F}\\
&\le\frac{\lVert\mathcal L(\rho)\rVert_2}{s_\rho}\\
&=\frac{\lVert\mathcal L(\rho-\sigma)\rVert_2}{s_\rho}\\
&\le\frac{2J\varepsilon}{s_\rho}.
\end{aligned}
```

This is the induced-norm inequality from [Rivas–Huelga §2.1](https://arxiv.org/pdf/1104.5242v2#page=5), combined with the project's evaluation-kernel geometry. The real multiple $`c\mathcal D_H`$ is Hilbert–Schmidt skew-adjoint. A normalized right eigenoperator of $`\mathcal L`$ therefore gives

```math
\left|\mathrm{Re}\lambda(\mathcal L)\right|
\le\lVert\mathcal R\rVert_{2\to2}
\le\frac{2J\varepsilon}{s_\rho}.
```

No diagonalizability or normality of $`\mathcal L`$ is needed. Every decay rate tends to zero with the error, including the relaxation gap. The norm cap is essential because multiplying a generator by a constant preserves its stationary state and multiplies all rates. Charging the whole generator also prevents unbounded coherent control from being supplied freely.

Two distinctions remain important. First, raw coefficient vectors are neither unique nor orthonormal superoperator coordinates; their singular values are not automatically $`s_\rho`$. Second, complete positivity ensures trace-distance contraction, but it does not make every quantum channel a Hilbert–Schmidt contraction. The project's direct Hilbert–Schmidt coercivity estimate for its particular constructed bath is an additional result. Negative numerical range is a sufficient contraction condition, not a general equivalent of having eigenvalues in the left half-plane. See [the norm and spectral account](../science/accuracy-relaxation.md) and the anchor's [§4.3](https://arxiv.org/pdf/1104.5242v2#page=29) and [§5.4](https://arxiv.org/pdf/1104.5242v2#page=45).

## Worked example: a weak reset bath

An exactly soluble qubit illustrates how an off-diagonal dissipative drift can produce an $`O(\eta)`$ stationary bias while the damping is also $`O(\eta)`$. This example describes one fixed bath family. It makes no universal claim about qubit thermalizers.

Again take $`H=(\omega/2)Z`$, $`\omega>0`$, and put

```math
z_\beta=-\tanh(\beta\omega/2),
\qquad \rho_\beta=\frac12(I+z_\beta Z).
```

Choose a real $`a\ne0`$ with $`a^2+z_\beta^2<1`$, and define the faithful reset state and generator

```math
\tau=\frac12(I+aX+z_\beta Z),
\qquad \mathcal D_\tau(A)=\mathrm{Tr}(A)\tau-A,
```

```math
\mathcal L_\eta=-i[H,\cdot]+\eta\mathcal D_\tau,
\qquad \eta>0.
```

The reset term is genuinely GKLS. If $`\tau=\sum_s p_s\lvert s\rangle\langle s\rvert`$, choose jumps $`J_{sj}=\sqrt{p_s}\lvert s\rangle\langle j\rvert`$ for any orthonormal input basis $`\{\lvert j\rangle\}`$. Then

```math
\sum_{s,j}J_{sj}AJ_{sj}^\dagger=\mathrm{Tr}(A)\tau,
\qquad \sum_{s,j}J_{sj}^\dagger J_{sj}=I.
```

Their dissipators sum to $`\mathcal D_\tau`$. Scaling the jumps by $`\sqrt\eta`$ gives the stated rate.

Let $`\Pi`$ dephase in the $`Z`$ basis. At the desired thermal state,

```math
\mathcal D_\tau(\rho_\beta)=\frac a2X\ne0,
\qquad \Pi\mathcal D_\tau(\rho_\beta)=0.
```

The populations have the right balance; the bath still creates coherence. For $`\rho(t)=(I+xX+yY+zZ)/2`$, the equations are

```math
\dot x=-\omega y+\eta(a-x),\qquad
\dot y=\omega x-\eta y,\qquad
\dot z=\eta(z_\beta-z).
```

Solving all three stationary equations gives

```math
x_\eta=\frac{a\eta^2}{\omega^2+\eta^2},\qquad
y_\eta=\frac{a\omega\eta}{\omega^2+\eta^2},\qquad
z_\eta=z_\beta.
```

The stationary state is faithful because its squared Bloch-vector length is $`z_\beta^2+a^2\eta^2/(\omega^2+\eta^2)<1`$. Its off-diagonal components allow Hamiltonian precession to cancel the bath's drift. The qubit trace-distance formula gives the exact error

```math
\frac12\lVert\sigma_\eta-\rho_\beta\rVert_1
=\frac12\sqrt{x_\eta^2+y_\eta^2}
=\frac{|a|\eta}{2\sqrt{\omega^2+\eta^2}}
=\frac{|a|}{2\omega}\eta+O(\eta^3).
```

On traceless operators the three generator eigenvalues are $`-\eta`$ and $`-\eta\pm i\omega`$. Thus

```math
\gamma(\mathcal L_\eta)=\eta.
```

Differences from the stationary Bloch vector rotate and contract by exactly $`e^{-\eta t}`$. This explicitly exhibits simultaneous linear bias and relaxation. Taking $`a=0`$ would instead give an exact qubit Gibbs resetter with finite damping, confirming why this example cannot prove the five-qubit obstruction.

The relevant bridge to the research construction is the condition $`\Pi\mathcal D(\rho_\beta)=0`$ together with a nonzero off-diagonal drift. Its weak-coupling use is credited to [Tupkary et al. in the related-work account](../references/related-work.md#boundary-thermalization-and-weak-coupling-limits). The elementary qubit calculation above is a direct illustration of the mechanism, not an additional educational anchor or a microscopic bath derivation.

## From local bath directions to the five-qubit frontier

The qubit calculation has only one population difference. The five-qubit system has 31. The construction must show that allowed local controls can balance all of them while keeping their coefficient matrices positive.

### Local observables span all population directions

For a simple-spectrum Hamiltonian, let $`\Pi`$ dephase in its energy basis, and let $`P_a`$, $`a=1,\ldots,51`$, be the allowed local Pauli strings. The exact moment matrix

```math
M_{k,a}=\mathrm{Tr}(H^kP_a),\qquad k=1,\ldots,31,
```

has rank 31 for the integer witness, as certified by a nonzero minor modulo 65537. Write $`O_{m,a}=\langle m\rvert P_a\lvert m\rangle`$. Its columns sum to zero. Multiplication by the Vandermonde matrix of the distinct energies gives a zero first row followed by $`M`$, so $`O`$ also has rank 31.

Therefore the dephased local observables $`\Pi(P_a)`$ span every trace-zero diagonal operator. This is a statement about their **diagonals**. The diagonal projectors of $`H`$ do not become local operators.

### Positivity survives a small, carefully chosen perturbation

On each bond, take the 15 nonidentity Hermitian Paulis $`F_{b,u}`$. A positive matrix $`C_b`$ defines

```math
\mathcal D_C(A)=\sum_{b,u,v}(C_b)_{uv}
\left(F_{b,u}AF_{b,v}-\frac12\{F_{b,v}F_{b,u},A\}\right).
```

This is the coefficient-matrix structure in the proof of [Rivas–Huelga Theorem 5.1](https://arxiv.org/pdf/1104.5242v2#page=38), restricted separately to each bond. Start at $`C_{0,b}=I_{15}`$, a strictly positive local depolarizer.

For anticommuting bond Paulis $`F,G`$ with $`FG=iP`$, set $`(\delta C)_{FG}=-i/4`$ and $`(\delta C)_{GF}=i/4`$. Direct substitution gives

```math
\mathcal D_{\delta C}(I)=P.
```

Thus coefficient perturbations can produce every local Pauli drift. The perturbation itself need not be positive: $`C_0+\delta C`$ remains positive for sufficiently small perturbations because $`C_0`$ is an interior point of the positive cone.

### Exact population balance leaves an admissible coherence drift

Select 31 perturbations whose dephased drifts are independent. At $`\beta=0`$, their population-balance matrix is invertible. Its entries depend analytically on $`\beta`$, as does the baseline drift. Solving the finite linear system gives

```math
C_\beta=C_0+O(\beta)>0,
\qquad \Pi\mathcal D_\beta(\rho_\beta)=0
```

for sufficiently small $`\beta`$. This imposes exact secular population balance, not $`\mathcal D_\beta(\rho_\beta)=0`$. The latter would contradict the obstruction in the generic regime.

The population generator is irreducible. Strict positivity of the bond coefficient matrices gives transition rates bounded below by sums of squared matrix elements of bond Paulis. A disconnected population graph would define a proper invariant subspace for all those Paulis, hence for every one-site $`X`$ and $`Z`$. They generate the full matrix algebra, so no such subspace exists. The balanced Gibbs population vector is therefore the unique classical stationary distribution.

### The stationary Schur complement handles the degenerate limit

Set $`\mathcal L_\eta=\mathcal D_H+\eta\mathcal D_\beta`$. The zero eigenspace of $`\mathcal D_H`$ contains every energy-diagonal operator, so the full commutator cannot be inverted. Use the projectors $`\Pi`$ and $`Q=\mathrm{id}-\Pi`$ instead. Write $`D_Q=Q\mathcal D_HQ`$, which is invertible on coherences because the energies are distinct, and define

```math
A=\Pi\mathcal D_\beta\Pi,\quad B=\Pi\mathcal D_\beta Q,\quad
C=Q\mathcal D_\beta\Pi,\quad E=Q\mathcal D_\beta Q.
```

For diagonal and off-diagonal stationary components $`p`$ and $`q`$, elimination gives

```math
q=-\eta(D_Q+\eta E)^{-1}Cp,
```

```math
\left[A-\eta B(D_Q+\eta E)^{-1}C\right]p=0,
\qquad\mathrm{Tr}p=1.
```

The irreducible classical block $`A`$ is invertible on trace-zero diagonal perturbations. Analytic inversion on the two appropriate subspaces yields $`p=\rho_\beta+O(\eta)`$ and $`q=O(\eta)`$. Hence the full faithful stationary state has trace-distance error $`O(\eta)`$. No assumption that all nonzero Bohr frequencies are distinct is required.

### A direct contraction estimate supplies the rate

On each bond, Pauli twirling gives

```math
\sum_{u=1}^{15}\mathcal D[F_{b,u}]
=16(\mathcal R_b-\mathrm{id}),
```

where $`\mathcal R_b`$ replaces that bond by its maximally mixed state after tracing it out. Every nonidentity five-qubit Pauli meets at least one bond, so

```math
\mathrm{Re}\langle A,\mathcal D_0(A)\rangle_{\mathrm{HS}}
\le-16\lVert A\rVert_2^2
\qquad(\mathrm{Tr}A=0).
```

A sufficiently small high-temperature perturbation preserves a positive coercivity constant $`\delta`$. The Hamiltonian part has zero real quadratic form, so

```math
\lVert e^{t\mathcal L_\eta}(A)\rVert_2
\le e^{-\eta\delta t}\lVert A\rVert_2
\qquad(\mathrm{Tr}A=0).
```

This proves attraction and a gap lower bound of order $`\eta`$ directly. The induced norm of the fixed dissipator supplies an upper bound of the same order.

Finally, rescale the **whole** generator by a fixed factor to satisfy a prescribed budget $`J`$. Its stationary state is unchanged. This is allowed because the coherent-control Hamiltonian $`K`$ need not equal the target Hamiltonian $`H`$; rescaling the dynamics does not redefine the target state. Taking $`\eta`$ proportional to the allowed error gives a gap of order $`\varepsilon`$. The universal stability bound proves the reverse inequality:

```math
\Gamma_{H,\beta,J}(\varepsilon)
=\Theta_{H,\beta,J}(\varepsilon)
\quad\text{as }\varepsilon\downarrow0.
```

The same converse forces the construction's actual error to be $`\Omega(\eta)`$, so the matching exponent concerns stationary error rather than just a chosen rate parameter. The [full construction](../science/local-construction.md) supplies the precise genericity intersection and the Hamiltonian-dependent temperature interval.

## What the certified constants do and do not say

The exact rank certificate establishes positivity of $`s_\rho`$ without estimating a useful size. The quantitative certificate uses rigorously enclosed inverse minors and the raw-to-intrinsic metric conversion to give explicit, conservative bounds. For the particular integer witness, the [quantitative account](../science/quantitative-witness.md) proves, for example,

```math
\begin{aligned}
\Gamma_{H_0,3/1000,J}(\varepsilon)&\ge0.0954\,J\varepsilon,\\
\Gamma_{H_0,3/1000,J}(\varepsilon)&\le2.0532\times10^{21}J\varepsilon,\\
0&<\varepsilon\le0.00056.
\end{aligned}
```

Both inequalities are certified. Their constants are separated by more than 22 orders of magnitude. The upper bound only improves on the elementary bound $`\gamma\le J`$ at errors below roughly $`4.9\times10^{-22}`$. It therefore establishes the asymptotic restriction without demonstrating a useful finite-error speed penalty.

The same witness has a certified positive, coercive bath family on the continuous interval $`0\le\beta\le0.01`$. That interval certifies the **construction**, not the evaluation rank at every real temperature in the interval. The algebraic argument covers positive algebraic temperatures for $`H_0`$, and a separate analytic argument supplies an unspecified punctured interval of full rank near zero. The two displayed rational-temperature instances have rigorous finite constants of their own.

At exactly $`\beta=0`$, local depolarization fixes the maximally mixed target and relaxes rapidly. There is no contradiction: the accuracy limit holds $`\beta>0`$ fixed, and the conditioning can deteriorate as $`\beta\downarrow0`$. These limits cannot be exchanged without further estimates.

Finally, the theorem concerns five qubits and adjacent-pair terms. Five is the first chain length at which the dimension of this larger local map space even permits a one-dimensional evaluation kernel. The finite certificate does not imply an all-chain theorem. It does not exclude three-site or four-site baths, prove that quasi-local tails are necessary, or cover retained ancillas and arbitrary time-dependent state preparation. The [interpretation page](../science/interpretation.md) and [related-work account](../references/related-work.md) keep those boundaries explicit.

## From ground marginals to finite-temperature feasibility

The same stationary-state framework has a second use when only individual jump support remains local. Rivas–Huelga [§5.2](https://arxiv.org/pdf/1104.5242v2#page=37) supplies the GKLS form and [§5.4](https://arxiv.org/pdf/1104.5242v2#page=45) distinguishes stationarity from relaxation. The energy-basis language in [§6.2.1](https://arxiv.org/pdf/1104.5242v2#page=57) and thermal balance in [§6.2.8](https://arxiv.org/pdf/1104.5242v2#page=73) connect the generator to its Gibbs target. Ground-marginal invariants and the finite interval certificates below are project material beyond the anchor.

Let $`|g\rangle`$ be the unique ground vector and $`\delta_\beta=1-\langle g|\rho_\beta|g\rangle`$. The [inherited pure-target theorem](https://github.com/GoGoKo699/Dissipative-Locality-Accuracy/blob/007749711a769111b86c0413ef9f5b91e2b88cac/science/converse.md) states that a stationary $`\sigma`$ with a nonscalar supported jump has $`1-\langle g|\sigma|g\rangle\ge\mu/2`$, where $`\mu`$ is the least allowed ground-marginal eigenvalue. Measuring $`|g\rangle\langle g|`$ therefore yields

```math
\frac12\|\sigma-\rho_\beta\|_1
\ge\left[\frac\mu2-\delta_\beta\right]_+.
```

The [new certificate](../verification/ground-thermal/README.md) proves all nine marginals full rank and makes that floor positive at $`\beta=4`$. For exact Gibbs stationarity, the ground vector is fixed rather than moving with the output. Its diagonal commutator vanishes for every controlled $`K`$; keeping the exact Boltzmann weights gives a quadratic form for each supported jump. Strict negativity of all four bond forms at $`\beta=12/5`$ prevents dissipative cancellation. Their monotonicity extends the exclusion to every real $`\beta\ge12/5`$, including global coherent control.

The high-temperature side uses the existing secular balance differently. Put $`B=\mathcal D_\beta(\rho_\beta)`$. Its energy diagonal is zero. For distinct Gibbs weights choose the Hermitian controlled Hamiltonian

```math
K_{mn}=-i\frac{B_{mn}}{p_n-p_m}\quad(m\ne n),
\qquad K_{mm}\in\mathbb R.
```

The $`mn`$ entry of $`-i[K,\rho_\beta]`$ is $`-iK_{mn}(p_n-p_m)=-B_{mn}`$. The exact Gibbs target is therefore stationary. The same coercivity proves global attraction because this arbitrary commutator is Hilbert–Schmidt skew-adjoint. Use depolarization directly at $`\beta=0`$. This is the inherited spectral-stabilizability completion, not a new reservoir prescription.

The resulting $`K`$ is generally global. Its exact construction on $`0\le\beta\le1/100`$ does not contradict the local-$`K`$ obstruction. The middle interval remains unresolved, and the unscaled contraction margin does not price global control or prove efficient synthesis. The [full account](../science/finite-temperature-feasibility.md) supplies the proofs, exact-source ownership and all temperature quantifiers.

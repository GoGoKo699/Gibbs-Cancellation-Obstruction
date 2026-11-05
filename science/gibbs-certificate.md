# An exact algebraic certificate for Gibbs stationarity

The Gibbs state contains matrix exponentials. A floating-point rank estimate, especially near infinite temperature, cannot certify that its local stationarity kernel has exactly one dimension. The proof below reduces this question to two finite integer computations and a transcendence theorem.

## Explicit Hamiltonian

The authoritative witness $`H_0`$ is the integer Pauli sum in [hamiltonian.json](../verification/data/hamiltonian.json). Labels use $`0,1,2,3`$ for $`I,X,Y,Z`$, with sites ordered from left to right. Every nonzero coefficient has magnitude at most four. All 51 allowed coefficient slots are listed, including zeros.

The witness is Hermitian and traceless. Its full characteristic polynomial is retained in [galois.json](../verification/data/galois.json); the file is data to verify, not an assumed theorem.

## Finite certificate A: a polynomial-state minor

Evaluate the raw local-superoperator matrix on

```math
\sigma=H_0^{31}.
```

This operator need not be positive. Its sole purpose is to show that a polynomial on the spectral weights is nonzero.

The selected rows and columns in [evaluation-minor.json](../verification/data/evaluation-minor.json) give a 923-by-923 minor with determinant

```math
12689\pmod{65537}.
```

The calculation is exact. Gaussian-integer matrix entries are reduced through $`i\mapsto256`$ in $`\mathbb F_{65537}`$, since $`256^2=-1`$ in that field. The unnormalized Pauli traces $`\mathrm{Tr}(PH_0^{31})`$ are integers: both matrices are Hermitian with Gaussian-integer entries, so their trace product is a real Gaussian integer. A nonzero modular determinant therefore certifies a nonzero ordinary integer determinant.

The [verifier](../verification/exact_certificate.py) reconstructs $`H_0`$ directly from the coefficient JSON, computes the Pauli traces, forms the selected minor and performs field elimination. It does not load a saved floating-point Hamiltonian or an eigenbasis.

## Finite certificate B: the Galois group

Exact factorization of the characteristic polynomial modulo three primes gives:

| Prime | Degrees of distinct irreducible factors |
|---|---|
| 19 | 1, 31 |
| 43 | 1, 2, 7, 11, 11 |
| 373 | 32 |

All three factorizations are square free. Irreducibility modulo 373 implies irreducibility over $`\mathbb Q`$ and a transitive Galois action on the 32 roots. Square-free modular factor degrees give permutations with the corresponding cycle types.

The 31-cycle fixes one point and acts transitively on the other 31. Its stabilizer is therefore transitive on the remaining points, and transitivity of the whole group makes the action doubly transitive. The permutation of cycle type $`(1,2,7,11,11)`$ raised to the 77th power is a transposition. Conjugating it using double transitivity gives every transposition. The Galois group is thus $`S_{32}`$.

Let the eigenvalues be $`E_1,\ldots,E_{32}`$. They are distinct algebraic numbers. Their only rational linear relations are multiples of

```math
\sum_j E_j=\mathrm{Tr}H_0=0.
```

Indeed, suppose $`\sum_jq_jE_j=0`$. Apply the Galois transposition interchanging $`E_i`$ and $`E_j`$ and subtract the two relations. Distinct roots give $`q_i=q_j`$. This holds for every pair.

## A nonzero homogeneous polynomial

Write $`H_0=\sum_jE_jQ_j`$, with algebraic spectral projectors $`Q_j`$. Evaluate the selected 923-minor on the operator

```math
\sigma(w)=\sum_{j=1}^{32}w_jQ_j.
```

Each matrix entry is linear in $`w`$, so its determinant $`P(w)`$ is a homogeneous polynomial of degree 923 with algebraic coefficients. Certificate A shows

```math
P(E_1^{31},\ldots,E_{32}^{31})\ne0.
```

Therefore $`P`$ is not the zero polynomial.

After combining equal monomials, write $`P(w)=\sum_k a_kw^k`$. If $`k\ne\ell`$ have the same total degree, then

```math
\sum_jk_jE_j\ne\sum_j\ell_jE_j.
```

Equality would yield a rational relation among the roots. All coefficients $`k_j-\ell_j`$ would be equal, and their zero sum would force all of them to vanish.

## Transfer to the exact Gibbs state

Fix a nonzero algebraic $`\beta`$. The numbers

```math
-\beta\sum_jk_jE_j
```

appearing in the polynomial expansion are distinct algebraic numbers. The [linear-independence form of the Lindemann–Weierstrass theorem](../references/related-work.md#mathematical-ingredients) implies

```math
P(e^{-\beta E_1},\ldots,e^{-\beta E_{32}})
=\sum_k a_k e^{-\beta\sum_jk_jE_j}\ne0.
```

Normalization by the positive partition function only rescales this degree-923 minor. Thus the true Gibbs evaluation map of $`H_0`$ has rank at least 923. The commutator direction gives the matching upper bound, so its intrinsic kernel is exactly one dimensional.

This argument restricts the witness Hamiltonian and the chosen witness temperature, not the coefficients of a prospective Lindbladian. Arbitrary real, target-dependent generator coefficients are excluded by the full real-linear rank statement.

## Fixed-temperature genericity

For any prescribed real $`\beta>0`$, use $`H_0/\beta`$. Its Gibbs state at inverse temperature $`\beta`$ equals that of $`H_0`$ at inverse temperature one, where the preceding argument applies.

At the prescribed $`\beta`$, the same selected minor is a real-analytic function of the 51 real Hamiltonian coefficients. It is nonzero at $`H_0/\beta`$, hence not identically zero. The zero set of a nonzero real-analytic function has measure zero and empty interior. Outside that set the rank is 923, proving Theorem 1 in the [model](model.md).

## One high-temperature interval for a fixed Hamiltonian

For $`H_0`$, the selected minor is an analytic function of $`\beta`$, nonzero at one. Its zero at $`\beta=0`$ has finite order. There is therefore a punctured interval $`0<\beta<\beta_0`$ on which it never vanishes.

For generic $`H`$, impose the nonzero-minor condition at $`\beta=1`$. The same argument supplies an $`H`$-dependent interval near zero. Intersecting it with the positive-construction interval proves the high-temperature quantifier in Theorem 3. This does not assert a common interval for all $`H`$ or absence of exceptional temperatures away from zero.

## What the certificate does and does not establish

The finite calculations verify one Hamiltonian, one polynomial-state evaluation minor, and modular factor patterns. The written Galois, transcendence and analytic arguments are essential for the exact Gibbs and generic conclusions. No finite sampling of Hamiltonians or temperatures substitutes for those arguments.

The certificate is tailored to five qubits and adjacent-pair maps. Increasing the number of sites changes both the matrix and the spectrum; the present certificate alone gives no induction in system size.

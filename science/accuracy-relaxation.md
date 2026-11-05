# Accuracy and relaxation at bounded strength

Fix a target $\rho=\rho_\beta(H)$ satisfying the one-dimensional-kernel theorem. The Hamiltonian $H$ and inverse temperature are held fixed throughout the accuracy limit.

## Evaluation controls the dissipative remainder

Use the intrinsic superoperator Frobenius norm on the local map space $\mathcal V$, and let $s_\rho>0$ be the least singular value of evaluation on the orthogonal complement of $\mathcal D_H$. Decompose any $\mathcal L\in\mathcal V$ as

$$
\mathcal L=c\mathcal D_H+\mathcal R,\qquad
\mathcal R\perp\mathcal D_H.
$$

Since $\mathcal D_H(\rho)=0$,

$$
\|\mathcal R\|_{2\to2}
\le\|\mathcal R\|_{\mathrm F}
\le \frac{\|\mathcal L(\rho)\|_2}{s_\rho}.
$$

If $\mathcal L(\sigma)=0$, $\|\mathcal L\|_{2\to2}\le J$, and $\frac12\|\sigma-\rho\|_1\le\varepsilon$, then

$$
\|\mathcal L(\rho)\|_2
=\|\mathcal L(\rho-\sigma)\|_2
\le J\|\rho-\sigma\|_2
\le2J\varepsilon.
$$

Consequently,

$$
\operatorname{dist}_{\mathrm F}
\bigl(\mathcal L,\operatorname{span}\{\mathcal D_H\}\bigr)
\le \frac{2J\varepsilon}{s_\rho}.
$$

The statement is uniform over all allowed generators with that norm cap, including coherent terms chosen as a function of the target and accuracy.

## Spectral consequence

The commutator $c\mathcal D_H$ is skew-adjoint for the Hilbert–Schmidt inner product. For any normalized right eigenoperator $A$ of $\mathcal L$,

$$
\operatorname{Re}\lambda
=\operatorname{Re}\langle A,\mathcal R(A)\rangle,
$$

and therefore

$$
|\operatorname{Re}\lambda|
\le\|\mathcal R\|_{2\to2}
\le\frac{2J\varepsilon}{s_\rho}.
$$

No normality or diagonalizability of the full Lindbladian is assumed. In particular, a primitive generator has relaxation gap

$$
\gamma(\mathcal L)\le\frac{2J\varepsilon}{s_\rho}.
$$

All dissipative decay rates approach zero, not only the slowest one. The gap describes asymptotic exponential decay; a uniform finite-time mixing guarantee would also need control of prefactors or nonnormal transients. The matching construction supplies a direct contraction bound of its own.

## Why strength must be charged

Multiplying a generator by an arbitrary constant preserves its stationary state while multiplying its gap. An unnormalized comparison between accuracy and speed would therefore have no content.

The cap here is the induced Hilbert–Schmidt norm of the entire generator. It includes coherent control. Holding only dissipative amplitudes fixed while allowing coherent amplitudes to diverge is a different resource model and does not satisfy this cap.

At fixed finite system size, many other reasonable norm budgets are equivalent up to constants. Those constants should be included before translating a numerical bound into another convention.

## The raw matrix is not an orthonormal superoperator basis

The 960 bond matrix units used for the exact rank certificate have a representation gauge and nontrivial mutual inner products. Their raw singular values cannot be identified with $s_\rho$.

Let $R$ map raw coefficient vectors to superoperators and $G=R^\dagger R$. Let $Q\Lambda Q^\mathsf T$ be the spectral decomposition of $G$ restricted to its positive 924-dimensional range. If $T_\rho$ contains output coordinates $\operatorname{Tr}(P\,\mathcal L(\rho))$, the intrinsic evaluation matrix is

$$
B_\rho=\frac1{\sqrt{32}}\,
T_\rho Q\Lambda^{-1/2}.
$$

Its single exact zero direction is the normalized Hamiltonian commutator; its least positive singular value is $s_\rho$. The factor $\sqrt{32}$ converts unnormalized Pauli traces to Hilbert–Schmidt coordinates.

This distinction does not affect ranks or the exact modular proof. It matters for quantitative constants. The [quantitative witness](quantitative-witness.md) reports the precision and normalization of every numerical or certified bound.

## Conditioning and interpretation

At infinite temperature, the target is maximally mixed and many local unital dissipators fix it. The stationarity kernel grows sharply. It is therefore natural for the conditioning constant to become small as $\beta$ approaches zero.

The theorem says that exact accuracy is inaccessible to dissipative adjacent-pair generators and that approaching it at bounded strength eventually slows relaxation. It does not claim a large useful error floor or a uniform speed penalty at every finite error. Those stronger practical claims require the actual target-dependent constants.

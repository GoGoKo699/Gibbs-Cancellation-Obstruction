# Quantitative bounds for the five-qubit witness

The [exact algebraic certificate](gibbs-certificate.md) proves the cancellation obstruction without relying on numerical tolerances. The calculations here add explicit constants for the same integer Hamiltonian $`H_0`$. They also specify positive bond-local reservoirs, verify a continuous temperature interval for their construction, and give finite-error bounds at two exact rational temperatures.

The distinction matters: the exponent in the accuracy–relaxation law is sharp, but the available converse constants are extremely loose. These results do not establish a practically significant speed penalty at a typical experimental error.

## Norms and reproducible inputs

Throughout, $`d=32`$, operator space carries the Hilbert–Schmidt norm, $`J`$ bounds the induced norm of the entire generator, and error means $`\varepsilon=\frac12\lVert\sigma-\rho_\beta\rVert_1`$. The intrinsic constant $`s_\rho`$ uses the superoperator Frobenius metric defined in the [stability theorem](accuracy-relaxation.md).

The authoritative input is [the integer Pauli coefficient file](../verification/data/hamiltonian.json). The two computational packages reconstruct it from text. Their copies are checked to agree. Exact rational interpolation nodes, a rational conditioning matrix, and selected minor indices are witnesses to verify; their numerical discovery is not used as a proof.

All bounds below are rounded outward from 256-bit Arb enclosures. The [verification guide](../verification/README.md) gives the commands, dependencies, input hashes and recorded results. The computational claims depend on the correctness of the finite algorithms and the underlying exact/ball-arithmetic libraries, not on a floating-point rank threshold.

## Certified intrinsic evaluation constants

The raw local map representation has 960 columns, while the actual map space has dimension 924. Its representation gauge and metric must be removed or bounded before reporting a singular-value constant.

Let $`R`$ synthesize a superoperator from raw coefficients. A raw bond matrix unit, extended by the identity map on the other three qubits, has global Frobenius norm 8. The 240 columns within one bond are orthogonal, so Cauchy–Schwarz over four bonds gives

```math
\lVert Rc\rVert_{\mathrm F}\le\sum_{b=1}^{4}8\lVert c_b\rVert_2
\le16\lVert c\rVert_2.
```

Let $`M`$ be an invertible 923-by-923 minor of the raw evaluation matrix, whose output coordinates are $`\mathrm{Tr}(P\mathcal A(\rho))`$. Its inverse determines a right inverse on the full evaluation image. Orthogonal projection away from the Hamiltonian kernel and conversion from Pauli traces to Hilbert–Schmidt coordinates yield

```math
s_\rho\ge
\frac{1}{16\sqrt{32}\,\lVert M^{-1}\rVert_{\mathrm F}}.
```

The [minor verifier](../verification/gap/verify_gap_bound.py) encloses the true Gibbs exponential and every inverse entry, then bounds the inverse Frobenius norm upward. Its [derivation](../verification/gap/README.md#why-a-minor-inverse-gives-a-lower-bound) explains why restricting to selected rows loses no evaluation direction.

| Exact inverse temperature | Certified lower bound on $`s_\rho`$ | Certified relaxation bound |
|---|---:|---|
| $`3/1000`$ | $`9.7410\times10^{-22}`$ | $`\gamma\le2.0532\times10^{21}J\varepsilon`$ |
| $`1/100`$ | $`4.1512\times10^{-18}`$ | $`\gamma\le4.8179\times10^{17}J\varepsilon`$ |

The bounds apply to every allowed generator with a stationary state at the stated error. They are conservative certified inequalities, not estimates of the actual optimal prefactor. Their enormous size limits what the converse says at finite error.

## An explicit positive reservoir

For each bond use its 15 nonidentity Hermitian Paulis $`F_{b,u}`$ and a positive coefficient matrix $`C_b`$. Start at $`C_b=I_{15}`$, the local depolarizer. For each of the 51 local Pauli strings $`P_a`$, choose anticommuting bond Paulis $`F_a,G_a`$ with $`F_aG_a=iP_a`$, and use

```math
\Delta_a(X)=\frac{i}{4}(G_aXF_a-F_aXG_a)
+\frac14(P_aX+XP_a),\qquad \Delta_a(I)=P_a.
```

Then $`\mathcal D_x=\mathcal D_0+\sum_ax_a\Delta_a`$ has coefficient matrices obtained by adding $`-ix_a/4`$ and $`+ix_a/4`$ in the corresponding off-diagonal positions. Positivity of the resulting matrices produces physical jumps on single bonds.

Choose 31 rational Lagrange polynomials $`B_j(H_0)`$ such that these matrices together with $`I`$ span the energy-diagonal commutant. The nodes only improve conditioning; they need not equal any energy. Define

```math
A_{ja}(\beta)=\mathrm{Tr}[B_j\Delta_a(e^{-\beta H_0})],
\qquad
f_j(\beta)=\mathrm{Tr}[B_j\mathcal D_0(e^{-\beta H_0})].
```

Let $`R_0`$ be the bundled rational 51-by-31 conditioning matrix. If $`w_a`$ counts chain bonds meeting the support of $`P_a`$ and $`h_a`$ is its Hamiltonian coefficient, put $`y_a=-16w_ah_a`$. The exact prescription is

```math
x(\beta)=\beta y-R_0[A(\beta)R_0]^{-1}
\bigl[f(\beta)+\beta A(\beta)y\bigr].
```

Whenever the indicated inverse exists, $`Ax+f=0`$ exactly. Thus dephasing $`\Pi`$ in the exact energy basis gives $`\Pi\mathcal D_x(\rho_\beta)=0`$. The coefficient balls enclose this prescribed vector; arbitrary rounded coefficients inside those balls need not solve the exact equation. No numerical eigenbasis is used to impose balance.

The [construction record](../verification/construction/README.md) specifies all bases and rational inputs, proves positivity and the norm bounds, and explains the verified linear solves. In particular, it certifies a single analytic family throughout

```math
0\le\beta\le\frac1{100},\qquad
C_b(\beta)\succeq0.0512I_{15}.
```

Its dissipator has Hilbert–Schmidt coercivity at least 4.12 on traceless matrices throughout this interval. The interval is covered by 128 rational cells, using a degree-20 Taylor expansion and a uniform exponential remainder below $`2.244\times10^{-28}`$.

**This continuous interval certifies the positive construction and coercivity. It does not certify full Gibbs evaluation rank at every real temperature in that interval.** The exact rank theorem applies at the two rational temperatures in the table; the separate analytic argument supplies an unspecified punctured interval near zero.

## Finite stationary-error and gap bounds

Write

```math
\mathcal L_{\beta,\eta}=-i[H_0,\cdot]+\eta\mathcal D_\beta,
\qquad \eta>0.
```

Suppose $`\mathcal D_\beta`$ has coercivity $`\delta>0`$ on traceless matrices, induced norm at most $`M`$, and $`r\ge\lVert\mathcal D_\beta(\rho_\beta)\rVert_2`$. Let $`\nu`$ be the smallest nonzero energy difference, and put $`F=1+M/\delta`$. A certified spectral enclosure gives $`\nu>0.5333458496`$ for $`H_0`$.

The generator has a unique faithful stationary state and obeys $`\gamma\ge\eta\delta`$. Splitting its stationary equation into energy-diagonal and off-diagonal parts gives

```math
0\lt \eta\le\frac{\nu}{2MF}
\quad\Longrightarrow\quad
\frac12\lVert\sigma_{\beta,\eta}-\rho_\beta\rVert_1
\le\frac{\sqrt{32}Fr}{\nu}\,\eta.
```

This bound controls the full remainder by an inverse estimate; it is not a fit to a perturbative plot. The positive coefficient matrices ensure faithfulness, and coercivity gives uniqueness and contraction directly.

| Certified quantity | $`\beta=3/1000`$ | $`\beta=1/100`$ |
|---|---:|---:|
| Bond positivity margin $`C_b\succeq\mu I`$ | $`\mu\ge0.7234`$ | $`\mu\ge0.2019`$ |
| Coercivity $`\delta`$ | $`\delta\ge13.900`$ | $`\delta\ge8.859`$ |
| Dissipator norm bound $`M`$ | $`M\le75.580`$ | $`M\le102.952`$ |
| Allowed range for the error bound | $`0\lt \eta\le0.000548`$ | $`0\lt \eta\le0.000205`$ |
| Stationary error | $`\varepsilon\le1.022\eta`$ | $`\varepsilon\le23.411\eta`$ |
| Full generator norm for $`\eta\le1`$ | $`\lVert \mathcal L\rVert_{2\to2}\le142.470`$ | $`\lVert \mathcal L\rVert_{2\to2}\le169.843`$ |

Rescaling the full generator to a prescribed budget $`J`$ preserves its stationary state. Taking $`\eta=\varepsilon/1.022`$ in the first example, or $`\eta=\varepsilon/23.411`$ in the second, gives the following explicit bounds on the optimal gap from the [model](model.md):

```math
0.0954\,J\varepsilon
\le\Gamma_{H_0,3/1000,J}(\varepsilon)
\le2.0532\times10^{21}J\varepsilon,
\qquad 0\lt \varepsilon\le0.00056,
```

```math
0.0022\,J\varepsilon
\le\Gamma_{H_0,1/100,J}(\varepsilon)
\le4.8179\times10^{17}J\varepsilon,
\qquad 0\lt \varepsilon\le0.00479.
```

These inequalities certify both the matching exponent and a constructive finite-error range. The large separation between their two constants remains unresolved. They establish neither a useful estimate of the optimum nor a scalable thermalization algorithm.

## Certified ground state and a cold feasibility exclusion

The same authoritative $`H_0`$ has a unique ground vector $`|g\rangle`$ whose five on-site and four adjacent-pair marginals are all positive definite. The [ground/thermal package](../verification/ground-thermal/README.md) encloses all 32 energies, every marginal eigenvalue and the true Boltzmann deficit. Define $`\mu=\min_S\lambda_{\min}(g_S)`$ and $`\delta_\beta=1-\langle g|\rho_\beta|g\rangle`$.

| Quantity | Certified directed bounds |
|---|---|
| First energy gap | $`3.005072939810\lt E_1-E_0\lt 3.005072939811`$ |
| Least allowed ground-marginal eigenvalue, on bond $`(1,2)`$ | $`0.000071696775227\lt \mu\lt 0.000071696775228`$ |
| Thermal deficit at $`\beta=4`$ | $`0.000006066710605253\lt \delta_4\lt 0.000006066710605254`$ |
| Inherited stationary approximation floor | $`\frac12\lVert\sigma-\rho_4\rVert_1>0.000029781677008303`$ |

The last row is the direct Gibbs corollary of Dissipative-Locality-Accuracy's inherited $`\mu/2`$ pure-target bound for any stationary $`\sigma`$ with a nonscalar allowed jump. It permits unrestricted global coherent control. It is separate from the stronger exact-target exclusion: four rigorous negative ground-population forms at $`\beta=12/5`$ have certified margins $`0.00008`$, $`0.029`$, $`0.013`$ and $`0.00029`$ in their unnormalized Pauli coefficient bases. Their analytic monotonicity excludes genuine dissipative stationarity for every real $`\beta\ge12/5`$, even with global $`K`$.

The [full proof and comparison](finite-temperature-feasibility.md) also turns the existing positive secular bath into exact attractive Gibbs preparation for $`0\le\beta\le1/100`$ when global $`K`$ is supplied. These bounds do not locate an exact crossover or settle the intervening interval. They do not change the original local-control finite-error constants above.

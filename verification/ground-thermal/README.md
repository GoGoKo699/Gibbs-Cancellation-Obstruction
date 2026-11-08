# Rigorous five-qubit ground-state and thermal certificate

This certificate uses the fixed integer Hamiltonian in the authoritative
[Pauli coefficient file](../data/hamiltonian.json). Its exact input bytes are
identified by SHA-256 in the [certificate output](ground_thermal_certificate.json). It makes no genericity claim
and does not extend the five-qubit model to larger systems.

Run from the repository root:

```sh
python3 -m pip install python-flint==0.9.0
python3 verification/ground-thermal/certify_ground_thermal.py
```

The program uses 256-bit Arb/Acb ball arithmetic and verified Rump
eigenvalue/eigenvector enclosures. It reconstructs the exact Gaussian-integer
Hamiltonian, isolates all 32 energies, normalizes an enclosed ground vector,
traces out complementary sites, and isolates all nine allowed marginal
spectra. Ordering uses midpoints only after the real eigenvalue balls are
proved disjoint. Every displayed decimal interval is checked against its
exact rational endpoints. Numerical rank thresholds are never used.

The ground state is unique. Its first gap is strictly between
3.005072939810 and 3.005072939811. The marginal least eigenvalues are listed
below as decimal illustrations; the accompanying JSON has rigorously checked
rational enclosures for every eigenvalue, including the largest ones.

| Support | Least eigenvalue |
| --- | ---: |
| 1 | 0.13713054610879 |
| 2 | 0.14664888547302 |
| 3 | 0.04376053329132 |
| 4 | 0.11233704096910 |
| 5 | 0.08221071874401 |
| 1,2 | 0.00007169677522711 |
| 2,3 | 0.00727163917899 |
| 3,4 | 0.00325615601118 |
| 4,5 | 0.00009112293656877 |

Thus all allowed ground-state marginals are positive definite, and

```math
0.000071696775227<\mu<0.000071696775228.
```

The minimum is uniquely attained on bond 1,2. With
$`r=\min_S\lambda_{\min}(g_S)/\lambda_{\max}(g_S)`$, the same bond uniquely
attains the minimum, and

```math
0.000072889471412<r<0.000072889471413.
```

## Thermal deficit and inherited bound

For the exact Gibbs state, let

```math
\delta_\beta=1-\langle g|\rho_\beta|g\rangle
=\frac{\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}
{1+\sum_{j=1}^{31}e^{-\beta(E_j-E_0)}}.
```

Each value is evaluated with the certified energy balls, not a floating-point
partition function. At beta=4, the output certifies

```math
0.000006066710605253<\delta_4<0.000006066710605254,
\qquad
0.000029781677008303<\mu/2-\delta_4<0.000029781677008304.
```

The universal pure-target stationary bound $`1-\langle g|\sigma|g\rangle \ge\mu/2`$ is inherited from [Dissipative-Locality-Accuracy, stationary-state converse](https://github.com/GoGoKo699/Dissipative-Locality-Accuracy/blob/007749711a769111b86c0413ef9f5b91e2b88cac/science/converse.md). Therefore any
stationary output of a generator with at least one genuinely dissipative
allowed jump has half trace distance from $`\rho_4`$ at least the latter
positive difference. This corollary credits the existing bound; the certificate
supplies its explicit Hamiltonian-dependent inputs. The output also brackets
the unique crossing $`\delta_\beta=\mu/2`$ between beta=3.41147195216 and
3.41147195217. It is a threshold for this sufficient test, not the exact
physical feasibility boundary.

If the target itself is Gibbs, its ground vector is an exact stationary
eigenvector. The existing population balance argument then gives the stronger
necessary conditions $`\delta_\beta\ge\mu`$ and
$`e^{-\beta(E_1-E_0)}\ge r`$. The output brackets the first crossing between
3.18245872502 and 3.18245872503 and certifies

```math
3.170161438761<\frac{\log(1/r)}{E_1-E_0}<3.170161438762.
```

These sharpened exact-target tests still do not assert a feasible region on
their other side.

## Full ground-population form

Let $`W_\beta=e^{-\beta(H-E_0)}=\rho_\beta/p_0`$, with
$`p_0=\langle g|\rho_\beta|g\rangle`$. The diagonal stationarity equation
for an individual jump A contributes

```math
\langle g|\mathcal D[A](\rho_\beta)|g\rangle
=p_0q_\beta(A),\qquad
q_\beta(A)=\langle g|A W_\beta A^\dagger|g\rangle
-\langle g|A^\dagger A|g\rangle.
```

The coherent commutator contributes zero for every Hamiltonian K, including a
global one. The form is invariant under adding any scalar multiple of I to A.
On each bond write $`A=\sum_{u=1}^{15}c_uF_u`$ in its unnormalized
nonidentity Pauli basis. Then $`q_\beta(A)=c^\dagger Q_\beta c`$, where

```math
(Q_\beta)_{uv}=\langle g|F_vW_\beta F_u|g\rangle
-\langle g|F_uF_v|g\rangle.
```

The program constructs W using the rigorously enclosed matrix exponential and
certifies strict positivity of $`-Q-mI`$ by interval LDL*. At beta=12/5 the
four certified rational margins are:

| Bond | $`-Q\succ mI_{15}`$ |
| --- | ---: |
| 1,2 | m=0.00008 |
| 2,3 | m=0.029 |
| 3,4 | m=0.013 |
| 4,5 | m=0.00029 |

The output records all 60 verified positive LDL* pivot balls. Since the
matrices are exact Hermitian forms, real diagonal pivots and complex
off-diagonal interval operations certify positive definiteness. The positive
matrix inequalities apply to arbitrary complex coefficient vectors c, hence
to non-Hermitian jumps as well as Hermitian ones. On-site jumps form subspaces
of these bond spaces and are included.

For beta'>=beta, $`W_{\beta'}\preceq W_\beta`$, so
$`q_{\beta'}(A)\le q_\beta(A)`$. Therefore every nonscalar allowed jump has
strictly negative ground-population contribution for every beta>=12/5.
Their sum cannot vanish. The fixed Gibbs state admits no genuine dissipation
in this strict-jump model, even with unrestricted global coherent control,
throughout that entire cold interval. Purely Hamiltonian stationarity remains
possible but cannot provide a unique attracting Gibbs equilibrium.

This stronger sufficient exclusion does not claim that beta=12/5 is the exact
transition. It also does not claim finite-accuracy robustness of the full-form
test. The inherited mu/2 estimate above separately supplies a rigorous
stationary trace-distance floor at beta=4.

The [finite-temperature scientific account](../../science/finite-temperature-feasibility.md) gives the local-H/global-H comparison, the complete stationarity argument and the high-temperature positive side. This certificate supplies finite inputs and inequalities; it does not certify an exact crossover temperature or feasible-set connectedness.

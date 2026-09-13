# Erdős #142 — audited AP-free theorem and barrier bank

**Source audit:** 2026-08-10  
**Campaign source:** 124 raw JSONL records, rounds 1–53  
**Court:** **NO SOLVE EXTRACTED.** The source problem asks for asymptotic information on

\[
r_k(N)=\max\{|A|:A\subseteq\{1,\ldots,N\}\text{ has no nontrivial }k\text{-term AP}\}.
\]

The raw campaign suffered severe target drift. This file releases only the mathematics that survived independent re-derivation: exact-level constructions, carry-free transfer, barriers to several proposed generalizations, a dyadic implication to the reciprocal-sum problem, and a finite certificate target. **Historical novelty is not claimed.**

## A. Strictly convex level sets are 3-AP-free

Let `D` be convex, `F:D→R` strictly convex, and

\[
L_c=\{x\in D:F(x)=c\}.
\]

Then `L_c` contains no nontrivial three-term arithmetic progression.

Indeed, if `x≠z` lie on the level and `y=(x+z)/2`, strict convexity gives

\[
F(y)<\frac{F(x)+F(z)}2=c.
\]

Thus `y` is not on the same level.

In particular, for every finite `p>1`, an **exact** level

\[
\sum_i |x_i|^p=c
\]

is 3-AP-free. This does **not** justify thick shells, and it does not extend to the `p=∞` sphere, whose boundary is not strictly convex.

## B. Carry-free mixed-radix transfer

Let digit caps `m_i≥1` and radices `B_i` satisfy

\[
B_i\ge 2m_i-1.
\]

Put

\[
Q_1=1,
\qquad
Q_i=\prod_{j<i}B_j,
\qquad
E(x)=\sum_{i=1}^d x_iQ_i,
\]

for `0≤x_i<m_i`.

If

\[
E(x)+E(z)=2E(y),
\]

then

\[
x_i+z_i=2y_i
\]

for every coordinate.

### Proof

Let `c_i=x_i+z_i-2y_i`. Then

\[
\sum_i c_iQ_i=0,
\qquad
|c_i|\le2(m_i-1)<B_i.
\]

Reduce modulo `B_1` to obtain `c_1=0`; divide by `B_1` and iterate.

### Corollary — convex-level mixed-radix construction

Under the same radix condition, if `F` is strictly convex on the digit box then

\[
A=\{E(x):F(x)=c\}
\]

is an integer 3-AP-free set.

This is the correct reusable core behind several otherwise-invalid campaign proposals.

## C. Monomial-level pigeonhole bound and the `p>2` barrier

Take uniform digit cap `m`, base

\[
B=2m-1,
\]

integer `p≥2`, and

\[
F_p(x)=\sum_{i=1}^d x_i^p,
\qquad
x_i\in\{0,\ldots,m-1\}.
\]

There is a level `c` satisfying

\[
|F_p^{-1}(c)|
\ge
\frac{m^d}{d(m-1)^p+1}.
\]

After carry-free encoding this gives a 3-AP-free subset of `[0,B^d)` of at least that size.

Optimizing this **crude exact-level+pigeonhole certificate** gives leading natural-log loss

\[
|A|
\ge
N\exp\left(-(2\sqrt{p\log2}+o(1))\sqrt{\log N}\right),
\]

or in base-two notation

\[
|A|
\ge
N\,2^{-(2\sqrt p+o(1))\sqrt{\log_2N}}.
\]

Hence, **within this specific certificate architecture**, `p=2` is optimal among integer `p≥2`. Raising the monomial exponent cannot improve the leading constant by this route.

This is an architecture-specific negative theorem, not a statement that all `L^p` constructions fail.

## D. Coarse anisotropic-weight barrier

For

\[
F(x)=\sum_i w_ix_i^2,
\qquad
w_i\in\mathbb Z_{>0},
\]

on fixed digit caps, the number of integer values is at most

\[
1+\sum_i w_i(m_i-1)^2.
\]

Therefore the elementary pigeonhole certificate guarantees only

\[
\max_c|F^{-1}(c)|
\ge
\frac{\prod_i m_i}{1+\sum_iw_i(m_i-1)^2}.
\]

Within this certificate, increasing positive integer weights only worsens the guaranteed lower bound. Weighted ellipsoids would need a sharper lattice-concentration theorem to beat the unweighted value-range argument.

## E. Nonstationary-digit barrier for the crude certificate

For varying digit caps, the same quadratic-level method gives schematically

\[
|A|\gtrsim\frac{\prod_i m_i}{\sum_i m_i^2},
\qquad
N\asymp\prod_i(2m_i).
\]

At fixed dimension and fixed product, AM–GM gives

\[
\sum_i m_i^2
\ge
 d\left(\prod_i m_i\right)^{2/d},
\]

with equality at equal digit caps. Thus **nonuniform digit ranges do not improve this crude certificate at fixed ambient product**.

Again, this kills the naive certificate, not every nonstationary-base construction.

## F. Naive product-recursion barrier

Suppose a construction at scale `M` has density

\[
\delta(M)\approx\exp(-c\sqrt{\log M}).
\]

A direct product at scales `N_1,N_2`, carry-free encoded into `N=N_1N_2`, has density loss

\[
\exp\left[-c\left(\sqrt{\log N_1}+\sqrt{\log N_2}\right)\right].
\]

Because

\[
\sqrt a+\sqrt b\ge\sqrt{a+b},
\]

this is no better than using the construction once at the total scale and is strictly worse when both factors are nontrivial. Therefore naive “Behrend of Behrend” direct products cannot change the `sqrt(log N)` exponent shape.

## G. Dyadic AP-free → reciprocal-sum transfer

For fixed `k`, suppose

\[
\sum_{j\ge1}\frac{r_k(2^j)}{2^j}<\infty.
\]

Then every `k`-AP-free set `A⊂N` has convergent reciprocal sum.

### Proof

Partition `A` into dyadic blocks

\[
A_j=A\cap[2^{j-1},2^j).
\]

Each `A_j` is `k`-AP-free, so

\[
|A_j|\le r_k(2^j).
\]

Every `n∈A_j` satisfies `1/n≤2^{1-j}`, hence

\[
\sum_{n\in A_j}\frac1n
\le
2\frac{r_k(2^j)}{2^j}.
\]

Summing over `j` proves convergence.

This is an exact cross-problem implication: sufficiently strong fixed-`k` upper bounds in the AP-free extremal problem imply the corresponding reciprocal-sum statement.

## H. Explicitly killed raw-campaign claims

The audit rejects the following as mathematical routes to the source problem:

- ordinary Sidon misidentification and the false formula `|A+A|=|A|^2`;
- a blanket `O(sqrt N)` Fourier-coefficient claim, which already fails at zero frequency;
- a density increment asking for a subprogression larger than the ambient interval;
- invalid ILP symmetry breaking such as fixing `x_1=1` by a translation that need not stay inside `[N]`;
- the incorrect AP constraint `x_i+x_j-2x_k≤1`; the binary hyperedge constraint is `x_i+x_j+x_k≤2`;
- using one finite AP-free example to refute a genuinely asymptotic bound without controlling constants/thresholds or producing an infinite family;
- claiming a **thick** strictly-convex shell is AP-free;
- confusing arbitrary full digit ranges with a carry-free radix encoding;
- treating the `L^∞` sphere as strictly convex.

These negative assets are part of the public theorem bank because they remove entire false search families.

## I. Frontier-aligned finite certificate target from the 2026-08-10 audit

The source audit compared the campaign to the then-relevant lower-bound architecture of Elsholtz–Hunter–Proske–Sauermann and isolated the following finite mathematical target.

Seek a measurable

\[
T\subset[0,1)^2
\]

with area

\[
\rho>7/24
\]

and a bounded function `f:T→R` such that whenever

\[
x,y,z\in T,
\qquad
x+z\equiv2y\pmod1,
\]

one has

\[
f(x)+f(z)
\ge
2f(y)+\|x-z\|_2^2.
\]

Within that published lifting architecture, the source audit records the exponent constant

\[
C(\rho)=2\sqrt{\log_2(1/\rho)}.
\]

The estate's proposed certificate program is:

1. partition the two-torus into rational polygonal cells;
2. represent `T` as a selected union of cells;
3. choose `f` in a finite exact family (piecewise affine/quadratic, or the known construction's ansatz);
4. for every relevant cell triple and wrap vector `q∈{-1,0,1}^2`, eliminate the midpoint by
   \[
   y=(x+z-q)/2;
   \]
5. certify exactly on the resulting rational polytope that
   \[
   \Phi_q(x,z)=f(x)+f(z)-2f((x+z-q)/2)-\|x-z\|_2^2\ge0;
   \]
6. certify the area `rho>7/24` by a rational margin.

Heuristic MILP/MINLP/SMT is acceptable only for discovery. The final object should carry exact rational area and exact per-cell inequality certificates.

**No such improved block is claimed by this release.** The point of preserving the target is that it is a finite certificate-producing attack aligned to the actual source problem, unlike most of the raw campaign.

## Court

Erdős #142 is **not solved** by this estate. The public assets are the exact-level mechanism, mixed-radix transfer, three architecture-specific barriers, a dyadic implication to reciprocal sums, a durable false-route bank, and a finite certificate target for improving a lower-bound construction.
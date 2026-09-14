# Erdős #142 — progression-free sets

**Author:** Jared Wilder  
**Status:** construction / barrier / finite-envelope research program; no claim that the full asymptotic problem is closed.

This repository is the canonical public home for the estate's #142 work on 3-term-progression-free sets. It consolidates the exact convex-level construction, carry-free mixed-radix transfer, architecture-specific barriers, dyadic reciprocal-sum implication, false-route bank, and finite `r_3` envelope/certificate work.

## Program scale

The audited campaign reconstructed **124 raw records across 53 rounds**. Its useful content is a structured package of exact mechanisms, negative theorems, finite data, and explicit obligations rather than a claimed solution of the asymptotic problem.

## Main structural endpoint

A strictly convex exact level is 3-AP-free. Combined with a carry-free mixed-radix encoding (`B_i >= 2m_i-1`), this gives an exact integer construction framework.

For the elementary monomial-level certificate

\[
F_p(x)=\sum_i x_i^p,
\qquad p\in\mathbb Z,\ p\ge2,
\]

with uniform digit cap and the crude value-range pigeonhole step, the resulting lower bound has leading natural-log loss

\[
|A|\ge
N\exp\!\left(-(2\sqrt{p\log 2}+o(1))\sqrt{\log N}\right).
\]

Therefore **within this specific exact-level + value-range + carry-free certificate architecture**, `p=2` is optimal among integer `p>=2`. The same audit proves that positive anisotropic integer weights and nonuniform digit caps do not improve their corresponding coarse pigeonhole certificates, and that naive products of Behrend-type constructions do not improve the `sqrt(log N)` exponent shape.

These are **architecture-specific barrier theorems**, not global impossibility theorems.

The audit also contains the exact cross-problem implication

\[
\sum_{j\ge1}\frac{r_k(2^j)}{2^j}<\infty
\quad\Longrightarrow\quad
\sum_{n\in A}\frac1n<\infty
\]

for every fixed `k` and every `k`-AP-free `A subset N`.

## Current literature boundary

Classical Behrend uses a quadratic sphere / carry-free digit construction. Modern work by Elsholtz–Hunter–Proske–Sauermann improves Behrend's integer lower-bound constant using a different torus-lifting architecture. Accordingly, the `p=2` optimization above should be read only as a **death certificate for that elementary monomial/pigeonhole route**, not as a claim that Behrend's classical constant is globally optimal.

The source audit's finite target with area `rho > 7/24` is intentionally aligned with the modern torus-lifting direction. No improved block is claimed by this repository.

Historical novelty of the estate's barrier refinements and transfer lemmas remains a separate literature question.

## Source layout

Exact public source bytes are migrated under:

- `structural/` — theorem/construction/barrier package from `erdos-theorems/erdos142-ap-free/`;
- `finite-envelope/` — the #142 finite envelope from `ck-gold-and-r3-envelope/erdos142-envelope/`.

The structural and finite lanes are intentionally separate so finite computation is not promoted into an asymptotic theorem.

# Erdős #142 — Progression-Free Sets

**Jared Wilder**

Construction, barrier, and finite-envelope work on 3-term-progression-free sets.

The project combines exact convex-level constructions, carry-free mixed-radix transfer, architecture-specific optimization barriers, finite `r_3` computation, and a reciprocal-sum implication for progression-free sets.

## Main structural result

A strictly convex exact level is 3-AP-free. With a carry-free mixed-radix encoding (`B_i >= 2m_i - 1`), this yields an exact integer construction framework.

For the monomial level

\[
F_p(x)=\sum_i x_i^p,\qquad p\in\mathbb Z,\ p\ge2,
\]

using uniform digit caps and the direct value-range pigeonhole step, the resulting lower bound has leading natural-log loss

\[
|A|\ge N\exp\!\left(-(2\sqrt{p\log 2}+o(1))\sqrt{\log N}\right).
\]

Within this certificate architecture, `p=2` is optimal among integers `p >= 2`. The same analysis shows that positive anisotropic integer weights, nonuniform digit caps, and naive products do not improve the corresponding coarse certificate at the `sqrt(log N)` scale.

These are route-specific optimization theorems: they identify what this construction architecture can and cannot deliver.

## Reciprocal-sum implication

The repository also records the exact implication

\[
\sum_{j\ge1}\frac{r_k(2^j)}{2^j}<\infty
\quad\Longrightarrow\quad
\sum_{n\in A}\frac1n<\infty
\]

for every fixed `k` and every `k`-AP-free set `A \subset \mathbb N`.

## Repository map

- `structural/` — construction, transfer, and barrier theorems
- `finite-envelope/` — finite `r_3` envelope and certificate work

The finite and asymptotic lanes are kept separate so their evidence can be inspected independently.
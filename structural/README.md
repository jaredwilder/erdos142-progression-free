# Erdős #142 — progression-free-set research program

This directory is a **research-program mirror** for work around Erdős Problem #142, the extremal size of subsets of `[1,N]` avoiding nontrivial arithmetic progressions. It is not part of the 79-declaration kernel-verified Lean corpus unless a file also appears under `theorems/` and is listed in the formal manifest.

The main audited mathematical record is:

- `AUDITED-GOLD-AND-BARRIERS-2026-08-10.md`

That audit reconstructs **124 raw records from rounds 1–53** and keeps only statements that survived re-derivation or are explicitly marked as finite targets / rejected routes.

## Mathematical content

The surviving program has several coherent parts.

### Exact convex-level construction

A level set of a strictly convex function contains no nontrivial three-term arithmetic progression. This gives a reusable source of 3-AP-free sets and clarifies exactly why thick shells or non-strictly-convex boundaries require separate arguments.

### Carry-free mixed-radix transfer

For digit caps `m_i` and radices `B_i >= 2m_i-1`, equality

`E(x)+E(z)=2E(y)`

forces coordinatewise equality

`x_i+z_i=2y_i`.

This converts suitable progression-free subsets of a digit box into progression-free sets of integers.

### Three architecture-specific barriers

The audit proves that, within the corresponding elementary certificate architectures:

- increasing the monomial exponent beyond `p=2` does not improve the leading constant of the exact-level pigeonhole construction;
- anisotropic positive integer weights do not improve the coarse value-range certificate;
- nonuniform digit ranges do not improve the same crude certificate at fixed ambient product.

A separate calculation shows that naive direct products of Behrend-type constructions do not improve the `sqrt(log N)` exponent shape.

These are **route-specific negative theorems**, not global impossibility claims.

### Cross-problem implication

For fixed `k`, if

`sum_j r_k(2^j)/2^j < infinity`,

then every `k`-AP-free set of positive integers has convergent reciprocal sum. This is an exact dyadic transfer from progression-free extremal bounds to a reciprocal-sum problem.

### Exact finite certificate target

The audit isolates a finite certificate problem in the two-torus: construct a measurable `T subset [0,1)^2` with area greater than `7/24` and a bounded function satisfying a specified midpoint-convexity inequality. A rational cell decomposition and exact per-cell inequalities would give a replayable certificate.

No such improved block is asserted here; the target is preserved because it is aligned with the actual lower-bound architecture rather than with discarded campaign heuristics.

## What was rejected

The audit also records and removes several false or irrelevant routes: Sidon misidentification, an invalid Fourier claim, impossible density-increment geometry, invalid ILP symmetry breaking, an incorrect AP constraint, misuse of one finite example against an asymptotic statement, thick-shell overreach, carry errors, and misuse of the `L^infinity` sphere.

Those failures are included because they delimit the research program; they are not the headline result.

## Repository status

This program is large enough to warrant a dedicated Erdős #142 repository. Until that home exists, this directory is a **transitional mirror** and the audit above is the byte-complete research record.

The separate repository `ck-gold-and-r3-envelope` contains a large finite table of Roth-number bounds. That is an important computational lane of the subject, but it is not the canonical home for the full #142 research program.

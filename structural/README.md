# Erdős #142 — progression-free-set research program

This directory is the structural theorem / construction / barrier layer of the canonical public repository `jaredwilder/erdos142-progression-free`. It is not part of the 79-declaration kernel-verified Lean corpus unless a file also appears under `theorems/` and is listed in the formal manifest.

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

### Architecture-specific barriers

The audit proves that, within the corresponding elementary certificate architectures:

- increasing the monomial exponent beyond `p=2` does not improve the leading constant of the exact-level value-range/pigeonhole construction;
- anisotropic positive integer weights do not improve the coarse value-range certificate;
- nonuniform digit ranges do not improve the same crude certificate at fixed ambient product;
- naive direct products of Behrend-type constructions do not improve the `sqrt(log N)` exponent shape.

These are **route-specific negative theorems**, not global impossibility claims. Modern torus-lifting constructions improve the classical Behrend constant by leaving this restricted architecture.

### Cross-problem implication

For fixed `k`, if

`sum_j r_k(2^j)/2^j < infinity`,

then every `k`-AP-free set of positive integers has convergent reciprocal sum. This is an exact dyadic transfer from progression-free extremal bounds to a reciprocal-sum problem.

### Exact finite certificate target

The audit isolates a finite certificate problem in the two-torus: construct a measurable `T subset [0,1)^2` with area greater than `7/24` and a bounded function satisfying a specified midpoint-convexity inequality. A rational cell decomposition and exact per-cell inequalities would give a replayable certificate.

No such improved block is asserted here; the target is preserved because it is aligned with the modern lower-bound architecture rather than with discarded campaign heuristics.

## What was rejected

The audit also records and removes several false or irrelevant routes: Sidon misidentification, an invalid Fourier claim, impossible density-increment geometry, invalid ILP symmetry breaking, an incorrect AP constraint, misuse of one finite example against an asymptotic statement, thick-shell overreach, carry errors, and misuse of the `L^infinity` sphere.

Those failures are included because they delimit the research program; they are not the headline result.

## Repository status

This directory is now a **canonical sub-surface of the dedicated Erdős #142 repository**, not a transitional mirror. The separate `finite-envelope/` directory carries the large finite Roth-number lane; finite computation remains intentionally separated from the asymptotic structural program.

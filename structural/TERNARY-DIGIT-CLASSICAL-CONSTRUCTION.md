# Classical ternary-digit construction for 3-AP-free sets

**Status:** unconditional elementary theorem; classical construction, not a novelty claim.  
**Purpose here:** consolidate three internally scattered lower-bound fragments into the correct parameterized statement.

Let

\[
A_d=\left\{1+\sum_{i=0}^{d-1}\varepsilon_i3^i:\varepsilon_i\in\{0,1\}\right\}.
\]

Then for every integer `d>=1`:

1. `|A_d|=2^d`;
2. `A_d` is contained in
   \[
   \left[1,\frac{3^d+1}{2}\right];
   \]
3. `A_d` contains no nontrivial three-term arithmetic progression.

Consequently

\[
r_3\!\left(\frac{3^d+1}{2}\right)\ge 2^d,
\]

and by monotonicity also

\[
r_3(3^d)\ge2^d.
\]

In particular the internally referenced statements

\[
r_3(243)\ge32,\qquad r_3(729)\ge64,\qquad r_3(2187)\ge128
\]

are immediate corollaries for `d=5,6,7`. They are therefore not three independent theorem assets and do not require separate source authority once this general construction is recorded.

## Proof

The size and endpoint are immediate. There are `2^d` binary digit strings, and the largest encoded value is

\[
1+\sum_{i=0}^{d-1}3^i
=1+\frac{3^d-1}{2}
=\frac{3^d+1}{2}.
\]

Suppose `x,z,y in A_d` satisfy

\[
x+z=2y.
\]

Subtract the common shift `1` and write the three resulting integers in base 3 using only digits `0,1`. Addition of the two endpoint strings produces no carry, because each coordinate sum is at most `2`. Likewise doubling a `0/1` digit produces `0` or `2`, again with no carry. Hence equality is coordinatewise:

\[
\alpha_i+\gamma_i=2\beta_i,
\qquad \alpha_i,\beta_i,\gamma_i\in\{0,1\}.
\]

The only solutions are `(0,0,0)` and `(1,1,1)`. Thus every coordinate agrees, so `x=y=z`. No nontrivial 3-term progression exists.

## Historical collision

This construction is classical. Erdős and Turán's 1936 paper *On Some Sequences of Integers* records the lower bound underlying the old Szekeres conjecture

\[
r_3\!\left(\frac{3^d+1}{2}\right)\ge2^d.
\]

It is also the familiar ternary `0/1` Stanley/Salem–Spencer construction. This file therefore makes **no historical novelty claim**.

Primary bibliographic reference:

- P. Erdős and P. Turán, *On Some Sequences of Integers*, J. London Math. Soc. 11 (1936), 261–264, DOI `10.1112/jlms/s1-11.4.261`.

## Estate disposition

The release-day source audit had separately listed `r_3(243)>=32`, `r_3(729)>=64`, and `r_3(2187)>=128` as `RECONSTRUCT_FIRST` because their original witness bytes were not recovered.

That debt is now mathematically **SUBSUMED**: the stronger parameterized theorem above independently reconstructs all three values with a transparent proof. The missing historical bytes may still be preserved if found, but they are no longer load-bearing for these lower bounds.

`verify_ternary_digit_construction.py` replays the finite instances through `d=9`, including the three previously isolated values.

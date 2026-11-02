# Tight fibers over Z/32: necessary conditions and actual diagnostics

The tight-fiber sum condition is **inhomogeneous**:

`(sum c_i) dot x = 16 - sum d_i (mod32)`.

Applied jointly to the already saved exact-32 fibers, it rejects no further phase mask in this batch. It does impose useful exact linear congruences on 792 D64 masks and 60 Q64 masks. It does not establish that any mask admits a diameter-three lift.

## Scope and conventions

The four-vertex base has multiplicities `01:3, 02:3, 03:2, 12:2, 13:3, 23:3`, hence degree 8 and 16 undirected base edges. Edge indices follow that order. Tree edges `[0,3,6]` have identity voltage; the free-edge order is `[1,2,4,5,7,8,9,10,11,12,13,14,15]`. The 13 parity bits and rotation coordinates use this same order. No additional normalization is imposed here.

For D64,

`(x,s)(y,t)=(x+(-1)^s y,s+t)`.

For Q64 the rotation coordinate has the additional term `16*s*t`. Here `x,y` are in Z/32 and `s,t` are in C2. Inverses are `(-x,0)` in the rotation layer, `(x,1)` in the D64 reflection layer, and `(x+16,1)` in the Q64 odd layer. Fixing a phase mask makes every short path an affine form `L_i(x)=c_i dot x+d_i`, with D64 constants zero and Q64 constants in `{0,16}`.

This task reads only the existing capacity results and `d64/forms_tight.jsonl`, `q64/forms_tight.jsonl`. It does not regenerate the 8,192 phase masks, enumerate rotation assignments, construct graphs, or run BFS. The separate capacity calculation remains the source for the path forms and candidate coverage.

## Why the right-hand side is 16

If a fiber has exactly 32 distinct affine forms and its evaluated values cover all of Z/32, those 32 values must be a permutation. Their sum is

`0+1+...+31 = 496 = 16 (mod32)`.

Therefore the sum of **all** 32 forms gives the displayed equation. It is incorrect to replace the right-hand side by zero, or to choose an arbitrary 32-element subset of a larger fiber. The equation is only necessary: collisions may remain even after it holds.

For D64 the right-hand side is always 16. For Q64 it is 16 or 0 according to the parity of the number of constant-16 forms. This distinction occurs in the saved data, not merely hypothetically.

## Correct ring linear algebra

For one equation `a dot x=b (mod32)`, solvability is equivalent to

`gcd(32,a_0,...,a_12) divides b`.

An all-even coefficient row is not an obstruction when `b=16`: 2 divides 16. Indeed, for this particular right-hand side, a single row is inconsistent only when every coefficient is zero modulo 32. A row with all coefficients divisible by 16 can still impose a nontrivial parity equation. A row with right-hand side zero is always individually consistent.

For several equations, individual row checks are insufficient. The implementation diagonalizes `A` with invertible row and column operations over Z/32. In each remaining submatrix it chooses a nonzero entry with minimum 2-adic valuation, swaps it to the pivot, and multiplies its row only by the inverse of its odd unit factor. The pivot is then `d=2^v`. Every other entry in that row or column is divisible by d; integer quotients give ordinary row or column subtractions that clear them modulo 32. No even element is inverted.

The saved matrices R and C satisfy `R*A*C=D` and the saved transformed right-hand side is `b'=R*b`. These identities are explicitly checked. The system is consistent exactly when each nonzero diagonal `d_i` divides `b'_i` and each zero row has `b'_i=0`. An inconsistent row yields an explicit vector w with `w*A=0` but `w*b!=0`; for a nonzero diagonal multiply its row of R by `32/d_i` to obtain that witness.

When consistent, write `x=C*y`. The exact parameterization is

`y_i=b'_i/d_i + (32/d_i)*t_i`, with `0<=t_i<d_i`,

for pivot coordinates, and arbitrary residues for the remaining coordinates. Division here is integer division **after** the divisibility check and corresponds to a congruence modulo `32/d_i`; it is not inversion of a nonunit in Z/32. The solution count of this necessary linear system is `32^(13-r) product d_i`. Generator distinctness and exact route coverage still have to be checked later.

Reducing all original equations modulo 2, 4, 8, or 16 is valid and can constrain candidate residues. Since every original right-hand side here is 0 or 16, each such lower-modulus system has the zero solution and cannot alone exclude a phase mask before further conditions are imposed. The modulo-32 system retains the essential inhomogeneous information.

## What reversing paths does and does not imply

For a closed path at the same base vertex, reversing the path takes its group voltage to its inverse.

- In D64, a reflection voltage is its own inverse. A reversed self-reflection path therefore gives the **same** affine form, already removed by symbolic deduplication. This does not pair two distinct forms and does not force their coefficient sum to be even.
- In Q64, reversing an odd voltage sends `(L,1)` to `(L+16,1)`. Distinct affine forms pair as `(c,d)` and `(c,d+16)`. If a self-odd fiber were tight, its 32 forms would form 16 such pairs. Their constants sum to zero modulo 32 and their coefficient sum is `2*sum(c_representative)`. Its tight condition would be `sum(c_representative) dot x=8 (mod16)`. This is a valid reduced-modulus equation, not an automatic contradiction. There are **no** self-odd tight fibers among the saved Q64 survivors, so this special condition was not needed in the actual diagnostic.
- A same-base rotation fiber is invariant under affine negation. For this loopless base and paths of length at most three, every nonempty reduced closed path uses distinct base edges, so each nonzero free-variable coefficient is ±1. Such a coefficient vector cannot equal its own negative modulo 32. The empty path gives the sole zero-coefficient form. Thus these self-rotation form sets have odd cardinality and cannot be exactly 32. The saved tight tables contain no such fiber, as expected.

The last statement uses the present three-step, loopless topology. It is not asserted for arbitrary longer words, where coefficients equal to 16 or additional constant-only paths could occur.

## Actual saved-table results

The single worker read 3,024 D64 tight fibers over 792 masks and 144 Q64 tight fibers over 60 masks. The actual modular diagonal types were:

| Group | Masks | Nonzero diagonal entries | Reduction of the unconstrained rotation tuple count |
|---|---:|---|---:|
| D64 | 36 | 1,1,4 | 2^13 |
| D64 | 108 | 1,1 | 2^10 |
| D64 | 324 | 1,1,1,4 | 2^18 |
| D64 | 324 | 1,1,1,1 | 2^20 |
| Q64 | 48 | 1 | 2^5 |
| Q64 | 12 | 1,2 | 2^9 |

All systems were consistent. Thus the capacity survivors remain 1,953 for D64 and 7,930 for Q64; masks without an exact-32 fiber were not subjected to this linear diagnostic. The saved parity projection of each consistent linear solution set also leaves a possible connected mod-2 quotient: no extra rejection arises there. Specifically, the fixed phase vector p and rotation-parity vector must span C2^2; a solution parity vector in `{0,p}` would fail this necessary connectivity condition, but none of the saved linear systems forces all solutions into those two vectors.

Two concrete checks illustrate the implementation requirements:

1. **D64 phase mask 237, root=target=0, odd fiber.** The summed coefficient row is
   `[10,5,9,9,10,0,0,4,30,30,28,28,28]` with right-hand side 16. The odd entries 5 and 9 directly disprove a blanket claim that self-reflection reversal forces an even coefficient row.
2. **Q64 phase mask 19, root 1 to target 2, odd fiber.** The summed row is
   `[10,10,27,27,12,28,28,3,3,3,3,3,3]`. Its constants sum to 16, so the correct right-hand side is **0**. Its reverse-endpoint equation is identical. The combined system has one unit diagonal; substituting a right-hand side of 16 would impose a different and potentially candidate-losing constraint.

As an example with a nonunit diagonal, D64 mask 111 has joint diagonal `[1,1,4]` and transformed right-hand side `[16,16,16,0,0,0]`. The third pivot means `4*y_2=16 (mod32)`, equivalently `y_2=4 (mod8)`, with four lifts modulo 32. It must not be treated as a unique field solution.

## Suggested use and boundary

Use the saved congruences as a cheap necessary check for any actual proposal in a tight mask, or use the saved invertible column matrix to construct proposals satisfying them exactly. Preserve every torsion choice `t_i` in a complete enumeration. For masks with minimum capacity greater than 32—including the best-capacity patterns of both groups—this particular condition supplies no equation and should not be advertised as a filter.

Only multiplication by an **odd unit** can be used as a common rotation-coordinate scaling automorphism. It preserves D64 multiplication; for Q64 it also preserves the central constant since `16*lambda=16 (mod32)` for odd lambda. Arbitrary first-nonzero-to-one or field-projective normalization is invalid, especially for all-even tuples. This diagnostic imposes no additional scaling normalization.

Code: `tight_ring_check.py`. Per-mask equations, R/C transforms, diagonals and right-hand sides: `d64_tight_linear_systems.json`, `q64_tight_linear_systems.json`. Summary: `TIGHT_RING_DIAGNOSTICS.json`. Actual CPU: 0.791802668 seconds, one worker, under the 30-second bound. Phase-capacity reruns, rotation assignments, generated graphs, and BFS calls: all zero. The result is a necessary-filter interface, not an exclusion of the remaining families or a construction.

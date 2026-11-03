# Five actual sixty-vertex seeds with four exact Gram identities

Date: 2026-10-12. Five complete graphs were constructed in the
`d=(1,1,1,1,3,3)` quotient. **Every graph satisfies all four diagonal
Gram identities exactly**, has 60 vertices, 240 edges and degree eight,
and has diameter three. The best seed has 352 bad pairs. No target was
found. The proposed constrained optimizer was compiled but **was never
launched**. A new local hub obstruction, subsequently confirmed by an
independent implementation, closed the local construction obligation
before launch. The root agent cancelled the optimizer. This is the
final state, with no pending launch.

## Exact construction domain

The quotient is orbit 4 from
[SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md](SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md):

```
d = (1,1,1,1,3,3)
Q = 0 0 1 3 1 2
    0 0 3 1 2 1
    1 3 0 2 0 1
    3 1 2 0 1 0
    1 2 0 1 0 1
    2 1 1 0 1 0
```

Vertices are `10*i+x`, with fiber i and local coordinate x. Write
`Z=F03`, `W=F12`, `T=F23`, `Y=F05`, and `V=F14`, with source vertices
indexing rows. Matchings S0,...,S3 are the internal adjacency matrices
of the first four fibers. The four enforced identities are

\[
\begin{aligned}
S_0+YY^T+ZZ^T&=J+4I,\\
S_1+VV^T+WW^T&=J+4I,\\
S_2+TT^T+W^TW&=J+4I,\\
S_3+T^TT+Z^TZ&=J+4I.
\end{aligned}
\]

Z and W come from the actual Grunbaum-numbered configuration data in
[local_interfaces.json](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json).
The first primal leave matching is chosen in each configuration; its
complementary two-factor supplies the ten incidence columns of Y or V.
Those columns receive independently randomized labels.

For S2 and S3 choose dual leave matchings with equal complementary cycle
type. T is the first explicitly generated point-edge incidence alignment
from the complementary dual factor of W to that of Z. The cycle
alignment routine is reused from the earlier preparation code; no result
of the capacity-ten bridge exclusion is imposed on this quotient.

| Core | Z type | W type | Z primal / dual choice | W primal / dual choice | T factor type |
| --- | ---: | ---: | --- | --- | --- |
| 0 | 1 | 4 | 0 / 0 | 0 / 0 | (5,5) |
| 1 | 2 | 3 | 0 / 0 | 0 / 0 | (10) |
| 2 | 5 | 8 | 0 / 5 | 0 / 0 | (4,6) |
| 3 | 6 | 7 | 0 / 1 | 0 / 1 | (3,7) |
| 4 | 9 | 9 | 0 / 1 | 0 / 1 | (3,3,4) |

Choice indices are zero-based in the saved catalogue. All matrices and
the actual column labels are saved, so the fixed core does not depend
on reconstructing an implicit isomorphism.

The seven degree-one interfaces 02,04,13,15,25,34,45 are independent
random permutations in each seed; they are not simultaneously fixed
to an identity tree. Thus normalizing Z and W has not also consumed
these seven independent interface choices. Both internal cubic seeds
are explicit Petersen graphs: outer step-one cycle, inner step-two
cycle, and spokes. Seed RNG values are 2026101200 through 2026101204.
This is five documented cores, not an exhaustive catalogue assembly.

## Actual expansion and verification

The generator wrote every complete 240-edge graph, then the independent
checker read its edge table back. Ordinary queue BFS supplies all
distances and all bad-pair witnesses, independently of the unused C++
optimizer's bitset scoring. The checker verifies simplicity, all sixty
degrees, every vertex's degree into each fiber, every fixed core matrix,
and that Y and V remain column labelings of their specified incidence
matrices. It independently multiplies integer matrices to check all
four displayed identities.

It also saves the entire matrix `B=A^2+A-7I-J`, verifies all row sums
are five, and verifies its block row sums against the actual defect
quotient. Every zero block is explicitly saved as a ten-by-ten matrix;
all four diagonal zero blocks are identically zero.

| Complete seed | Bad pairs | Bad pairs in zero blocks | Diameter |
| --- | ---: | ---: | ---: |
| Core 0 | 383 | 209 | 3 |
| Core 1 | 352 | 205 | 3 |
| Core 2 | 385 | 213 | 3 |
| Core 3 | 392 | 210 | 3 |
| Core 4 | 389 | 209 | 3 |

For the best seed, core 1, the seven off-diagonal zero blocks 01,04,15,
24,25,34,35 have respectively 33,28,31,26,34,27,26 missing pairs.
These sum to 205. Every missing pair has both complete neighbor lists,
distance and common-neighbor intersection recorded. The four exact
same-fiber equations therefore remove their own failures, but do not
supply the cross-fiber coverage equations.

Generation plus all five independent seed checks took 0.093139 process
CPU seconds. A separate preparation wall-time measurement was not
recorded. **Optimizer processes launched: zero; optimizer CPU consumed:
zero.** The planned 27-second combined search was cancelled before launch,
so no search timing, best-search result, or executed-move count is
claimed.

## Prepared moves and the remaining local obstruction

The compiled, unexecuted optimizer permits only: transpositions in one
of the seven matching interfaces; swapping two complete columns of Y
or V; and a simple two-edge switch within cubic fiber 4 or 5. It fixes
Z,W,T,S0,...,S3. Each move preserves the four Gram equations. In addition
to this construction invariant, the source asserts the exact integer
same-fiber route equations after every proposed valid move. A future
saved-graph check would again multiply the matrices independently.
These descriptions specify prepared code; they are not evidence of an
executed optimization. The runner refuses a launch once the saved final
status exists.

The remaining cross equations are given in
[VARIABLE_111133_OBLIGATION.md](VARIABLE_111133_OBLIGATION.md). In
particular, after legitimate tree normalization, block 04 requires
`I+S0+C4+Z+Y=J`, with C4 a simple symmetric cubic adjacency matrix.
With Z and Y instead kept in catalogue coordinates, the corresponding
column permutations must remain free. The local hub screen concerns
precisely that symmetry-and-disjointness obligation. The complete
[71-state C++ screen](../../../computations/dd82/construction/variable_hub_local_run/search.json)
and an [independent Python implementation from the raw configuration triples](../../../computations/dd82/construction/variable_hub_local_run/independent_verification.json)
both found zero witnesses, without connectivity or spectral pruning.
The proof and candidate-preservation argument are separate from this
experiment. The five failures here are actual generated witnesses
accompanying that closure, not by themselves a proof that all completions
fail.

The saved seed data also give the hub obstruction in their actual
coordinates. Writing A=F04, right-multiplying block 04 by A^T yields

\[
I+S_0+C'+ZN+YP=J,
\qquad C'=AC_4A^T,\quad N=F_{34}A^T,\quad P=F_{54}A^T.
\]

C' is symmetric cubic and N,P are permutation matrices. This
normalization relabels only the target coordinates; it does not assume
independent canonical catalogues and an identity tree simultaneously.
The original route matrix was checked directly against the adjacency
sets. For cores 0,...,4, block 04 misses respectively **30,28,31,29,29**
pairs. Every original and normalized matrix, all five summands, every
missing pair and all duplicate-route intermediates are saved in
`hub04_failures.json`. Their row sums are ten, so the total duplicated
route excess equals the number of missing pairs in each core.

## Files

- [Generator, exact integer Gram checker and independent BFS](../../../computations/dd82/construction/variable_fiber_exact_gram_run.py).
- [Compiled but unexecuted constrained optimizer source](../../../computations/dd82/construction/variable_fiber_exact_gram_search.cpp).
- [All explicit fixed cores and seed labels](../../../computations/dd82/construction/variable_fiber_exact_gram_run/cores.json).
- [Five verification summaries](../../../computations/dd82/construction/variable_fiber_exact_gram_run/verification.json).
- [Best seed's full edge table](../../../computations/dd82/construction/variable_fiber_exact_gram_run/core1.seed.edges)
  and [all its bad pairs, integer Gram products and zero blocks](../../../computations/dd82/construction/variable_fiber_exact_gram_run/core1.seed.verification.json).
- [Actual hub-04 matrices and failure witnesses for all five seeds](../../../computations/dd82/construction/variable_fiber_exact_gram_run/hub04_failures.json).
- [Preparation CPU record](../../../computations/dd82/construction/variable_fiber_exact_gram_run/preparation.json)
  and [final cancellation with zero optimizer runs](../../../computations/dd82/construction/variable_fiber_exact_gram_run/launch_status.json).

The same output directory contains full edge tables, complete core
metadata and verification records for cores 0,2,3,4. No new SAT input,
review request, or unconstrained graph search was made in this experiment.

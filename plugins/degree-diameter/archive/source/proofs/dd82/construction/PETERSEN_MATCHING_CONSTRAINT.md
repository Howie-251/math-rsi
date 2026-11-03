# Necessary pair-matching constraint for six Petersen fibers

Date: 2026-10-11. This note concerns six ten-vertex Petersen fibers, with one
perfect matching between every pair of fibers. The full graph is 8-regular
on 60 vertices. The constraint below is necessary, not sufficient for
diameter two.

## Derivation

Use the same labeling as the actual six-fiber source:

    outer edges i--(i+1 mod 5),
    inner edges (5+i)--(5+(i+2 mod 5)),
    spokes i--(i+5),                       0≤i≤4.

Let P be this Petersen graph, and M a permutation defining the matching from
one fiber to another, with M[u] the target label of source u. For a source
vertex u, the length-at-most-two routes into that target fiber have eleven
slots:

- one direct matching endpoint M(u);
- three endpoints M(N_P(u)), using the source fiber internally first;
- three endpoints N_P(M(u)), using the target fiber internally last;
- four endpoints through the four other fibers.

The direct endpoint is disjoint from each of the two triples. The triples
intersect in

    r(u) = |M(N_P(u)) ∩ N_P(M(u))|
         = d_{P∩M(P)}(M(u)).

Thus the eleven slots cover at most 11−r(u) distinct labels. Covering all ten
labels requires r(u)≤1 for every u. Equivalently,

    maximum degree of P∩M(P) ≤ 1.

The intersection is therefore a matching with q∈{0,1,2,3,4,5} edges. This
condition is invariant under inverse permutations and under composing M
on either side with an automorphism of P. Consequently checking A,B,C checks
the same necessary condition for the rotated/inverted pair matchings in the
actual C5-symmetric three-permutation design, because R rotates both cycles
and preserves P.

## Exact finite catalog

[Source](../../../computations/dd82/construction/petersen_matching_catalog.cpp)
uses lexicographic `next_permutation` to process all 10!=3,628,800 permutations.
For each M it scans the fifteen edges of M(P) and collects those also in P;
a repeated endpoint rejects the permutation. Counts and the first accepted
permutation for each q are saved in
[result JSON](../../../computations/dd82/construction/petersen_matching_catalog.json).
The enumeration completed in 0.117415 CPU seconds on one pinned CPU, within
the three-second limit. No graph search or group enumeration was run.

| Intersection edges q | Accepted permutations |
| ---: | ---: |
| 0 | 2,880 |
| 1 | 46,800 |
| 2 | 158,400 |
| 3 | 240,600 |
| 4 | 158,400 |
| 5 | 4,320 |
| Total | 611,400 |

There are 3,017,400 rejected permutations. In particular, edge-disjoint
Petersen images exist. One explicit permutation is

    M = [0,2,4,1,3,6,8,5,7,9].

A separate short Python check rebuilt P from its neighborhood definition and
verified all ten image-neighborhood intersections are empty. This certifies
the stated witness directly; it is not a second exhaustive enumeration.

## Remaining construction obligation

For r(u)=0, the direct endpoint and two triples already cover seven labels.
The four routes through other fibers must cover the three remaining labels.
They have only one total repetition allowance. For r(u)=1, the first seven
slots cover six labels; the four other-fiber endpoints must be exactly the
four remaining labels, all distinct. This is a concrete row-by-row condition
on the simultaneous composed matchings, not an independent choice for each
fiber pair.

The saved best three-permutation candidate was inspected read-only at
iteration 246,611,968, with orbit-missing count 10 (50 expanded bad pairs).
All three of its A,B,C already have q=0, with all ten intersection degrees
zero. Their exact values and this diagnostic are copied into the catalog
JSON. Therefore the present candidate's failure survives the strongest
edge-disjoint version of this single-matching filter. A useful repair must
change the four composed matching endpoints in the missing rows, while
retaining compatibility across all fiber pairs.

No complete 60-vertex diameter-two graph follows from the 611,400 admissible
single matchings or from the 2,880 edge-disjoint ones. No parameter triple
was searched or excluded by this catalog.

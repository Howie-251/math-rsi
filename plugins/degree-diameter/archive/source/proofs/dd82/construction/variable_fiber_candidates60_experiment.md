# Actual candidates for the remaining variable-degree fiber quotients

Date: 2026-10-12. One bounded construction experiment; no SAT or exhaustive
graph search. The best saved graph has **60 vertices, 240 edges, degree eight,
diameter three and 155 unordered pairs at distance greater than two**. Thus
this experiment did not construct a target. Its remaining quotient is open.

## Domains and explicit seeds

The domains are orbits 1 and 4 in the independently verified
[variable-degree quotient screen](../../../computations/dd82/construction/six_fiber_variable_internal_run/verification.json).
Vertices are numbered `10*i+x`, with fiber `i=0,...,5` and local coordinate
`x=0,...,9`. Internal degrees and cross-fiber degrees are prescribed for
every vertex, not merely on average.

For orbit 1,

```
d = (0,0,1,2,2,3)
Q = 0 1 3 0 3 1
    1 0 3 3 0 1
    3 3 0 0 0 1
    0 3 0 0 2 1
    3 0 0 2 0 1
    1 1 1 1 1 0
```

For orbit 4,

```
d = (1,1,1,1,3,3)
Q = 0 0 1 3 1 2
    0 0 3 1 2 1
    1 3 0 2 0 1
    3 1 2 0 1 0
    1 2 0 1 0 1
    2 1 1 0 1 0
```

In each seed, an internal degree-zero fiber is empty; a degree-one fiber
has the five edges `x--(x+5)`; a degree-two fiber is the cycle C10; and a
degree-three fiber is Petersen, with outer five-cycle, inner step-two
five-cycle, and five spokes. Each cross-interface is the union of its
prescribed number of distinct cyclic shifts `x -> x+t mod 10`. The actual
shifts, internal definitions and all 240 edges are saved in each seed JSON;
Python random seeds were 20261013 and 20261016.

Both complete seeds were generated and independently checked. Before any
optimization of orbit 1, the new
[matrix contradiction](VARIABLE_001223_OBLIGATION.md) closed that domain.
Consequently its seed is retained only as an actual construction/failure
record: **zero optimization runs were made in orbit 1**.

## The single bounded run

The orbit-4 run preserves the displayed entire quotient and all internal
degrees. A move is either a simple internal two-edge switch, or a
bipartite two-edge switch wholly within one fixed interface. The latter
preserves each endpoint's degree into that particular fiber. Duplicate
edges and loops are rejected. Internal cubic graphs can change, and the
interfaces need not remain unions of cyclic shifts after initialization.

The score was `4*bad_pairs + bad_pairs_in_zero_defect_blocks`. Simulated
annealing used three-CPU-second epochs, temperatures 2.2 to 0.06 in
bad-pair units, and at each new epoch a return to the best-energy graph
followed by 24 accepted valid-switch perturbations. There were eight such
returns within this one run; no additional search was started.

The RNG seed was 2026101204. The process was pinned to one CPU, with a
30-second process CPU limit, a 27-second internal optimization budget and
a 4 GiB address-space limit. Actual resources were **27.010034 CPU seconds,
27.029751 wall seconds, and 12,112 KiB maximum RSS**. It exited normally
at its budget, after 45,601,792 trials, 39,195,023 valid switches and
830,932 accepted switches. Of the valid switches, 12,442,453 were internal
and 26,752,570 were bipartite. This finite trajectory does not exhaust its
domain.

| Saved complete graph | Bad pairs | Bad pairs in zero blocks | Diameter |
| --- | ---: | ---: | ---: |
| Orbit 1 seed | 472 | 260 | 3 |
| Orbit 4 seed | 482 | 250 | 3 |
| Orbit 4 best total / best energy | 155 | 87 | 3 |
| Orbit 4 best zero-block count | 164 | 84 | 3 |

All rows are simple connected 60-vertex, 240-edge, eight-regular graphs
with their full prescribed internal and cross degrees. The two objectives
save distinct candidates; neither satisfies diameter two.

## Independent expanded-graph verification

The Python checker reads each saved complete edge table and builds fresh
adjacency sets. It uses ordinary queue BFS, independently of the C++
bitset score, to record all distances and every bad pair. Each bad-pair
witness includes both vertices' entire neighbor lists and their common
neighbors. It verifies all 60 individual internal/cross degree vectors.

It also computes the full integer matrix

\[
B=A^2+A-7I-J.
\]

Every row sums to five. For every source vertex, its sums over target
fibers agree with the independently supplied defect quotient
`D=(diag(d)+Q)^2+diag(d)+Q-7I-10J`. The complete matrices and block
histograms are saved. In an unordered block the positive excess minus
the number of missing pairs is `10*D_ij` off the diagonal and `5*D_ii`
on the diagonal. These identities were checked exactly, including in
the failed candidates, where negative entries of B equal minus one.

## Where the best candidate fails

For orbit 4, the four diagonal zero blocks and seven off-diagonal zero
blocks must vanish entrywise in a target. **All eleven still fail in the
best-total candidate.** Their complete missing-pair counts are:

| Block | 00 | 01 | 04 | 11 | 15 | 22 | 24 | 25 | 33 | 34 | 35 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Missing pairs | 3 | 13 | 11 | 2 | 9 | 4 | 8 | 12 | 4 | 11 | 10 |

They account for 87 of the 155 bad pairs: thirteen within the four
matching fibers and seventy-four between fibers. Each zero block has
exactly as much positive route excess as missing coverage. In this
candidate every positive entry in these blocks is one, so these excesses
are double coverage of other pairs. The remaining 68 bad pairs lie in
positive-defect blocks.

One precise obstruction to fixing these data is block 01. With rows in
the source fiber, the exact condition is

\[
F_{02}F_{21}+F_{03}F_{31}+F_{04}F_{41}+F_{05}F_{51}=J_{10}. \tag{1}
\]

There is no direct edge or endpoint-fiber route for this block. The four
summands are individually zero-one biregular matrices, of degrees
3,3,2,2. Thus (1) requires their four supports to partition all 100 cells.
The saved best graph instead has 13 uncovered cells, 74 singly covered
cells and 13 doubly covered cells. For example, vertices 0 and 18 are
uncovered; vertices 0 and 19 have two routes, through vertices 24 and 56.
The overlaps occur between every pair of route families: their counts
for intermediate fiber pairs (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)
are respectively 3,2,2,2,3,1. All four matrices, all missing cells and
all overlap witnesses are recorded in `orbit4.best_bad.zero_block01.json`.

The next mathematical obligation is therefore a **simultaneous labeled
realization of the four exact diagonal Gram equations and the seven
exact cross-block equations**, rather than merely choosing compatible
degrees or improving the aggregate score. In particular, any catalog
assembly must make the four route supports in (1) disjoint while
preserving those same local Gram equations. The explicit tree gauge,
matrix eliminations and remaining inequalities are now stated in
[VARIABLE_111133_OBLIGATION.md](VARIABLE_111133_OBLIGATION.md). The
capacity-eleven interfaces 02 and 13 retain a nonzero defect and cannot
be replaced by the earlier capacity-ten bridge screen.

## One check of the new cubic-hub restriction

The same obligation proves that the two internal cubic graphs must be
connected and have second adjacency eigenvalue at most two. One check
was made on the already saved best-total graph, without another search.
Both cubic fibers are connected. Their numerical second eigenvalues are
approximately 1.5615528128 and 1.6180339887. These are floating-point
observations from `numpy.linalg.eigvalsh`, with tolerance 1e-9, not
certified spectral bounds. Complete cubic edge tables, connected
components and numerical spectra are saved in
`orbit4.best_bad.hub_structure.json`.

Thus this necessary restriction does not discard the saved best. Its
eleven failed exact blocks remain the concrete gap to a local-catalog
construction. No claim of impossibility for orbit 4 follows from this
experiment, and no additional optimization was performed after the
structural check.

## Saved implementation and data

- [C++ bounded optimizer](../../../computations/dd82/construction/variable_fiber_candidates60_search.cpp).
- [Seed generator, resource wrapper and independent BFS/defect checker](../../../computations/dd82/construction/variable_fiber_candidates60_run.py).
- [All saved-graph verification summaries](../../../computations/dd82/construction/variable_fiber_candidates60_run/verification.json).
- [Actual process resource record](../../../computations/dd82/construction/variable_fiber_candidates60_run/resources.json).
- [Best-total complete edge table](../../../computations/dd82/construction/variable_fiber_candidates60_run/orbit4.best_bad.edges)
  and [all 155 bad pairs plus the full defect matrix](../../../computations/dd82/construction/variable_fiber_candidates60_run/orbit4.best_bad.verification.json).
- [Best-zero complete edge table](../../../computations/dd82/construction/variable_fiber_candidates60_run/orbit4.best_zero.edges).
- [Block-01 matrices and witnesses](../../../computations/dd82/construction/variable_fiber_candidates60_run/orbit4.best_bad.zero_block01.json)
  and [one cubic-hub check](../../../computations/dd82/construction/variable_fiber_candidates60_run/orbit4.best_bad.hub_structure.json).

The same output directory contains both complete seeds, their shift
descriptions and complete BFS failure data, the best-energy edge table,
the search log and the accepted best-energy progress record. The runner
refuses an unchanged rerun when its resource record already exists.

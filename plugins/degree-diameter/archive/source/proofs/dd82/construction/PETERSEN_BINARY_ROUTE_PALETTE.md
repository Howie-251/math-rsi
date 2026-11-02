# Complete binary assembly preserving all fifteen seven-route matrices

Date: 2026-10-12. A single complete enumeration of **32,768** expanded
six-Petersen graphs found a minimum of **20 bad pairs** and minimum cycle
energy **50**, attained by exactly four labeled graphs. Every minimum graph
was saved in full and independently checked by BFS. This closes the finite
family defined below; it does not exclude arbitrary six-Petersen graphs,
the whole zero-overlap matching domain, or arbitrary order 60.

## The exact new construction family

Use the actual saved twenty-bad-pair graph with Petersen matrices
\(P_0,\ldots,P_5\) and matching matrices \(M^0_{ij}\). For each of its
fifteen interfaces define the fixed matrix

\[
L^0_{ij}=M^0_{ij}+P_iM^0_{ij}+M^0_{ij}P_j.
\]

It is a zero-one matrix with row and column sums seven. Define its complete
local palette by

\[
\mathcal P_{ij}=\{M\text{ a permutation matrix}:M+P_iM+MP_j=L^0_{ij}\}.
\tag{1}
\]

Every palette has exactly two members: the original matching and one
different matching. The actual local permutations and full seven-route
supports are saved, for all fifteen interfaces, in
[palettes.json](../../../computations/dd82/construction/petersen_binary_palette_run/palettes.json).
Choose either member independently on every interface, retaining the six
internal Petersen graphs. This defines exactly \(2^{15}=32768\) distinct
labeled simple graphs, all on sixty vertices with 240 edges and degree
eight. Two binary assignments differing at a bit have different edges in
that corresponding interface.

This family allows all five interfaces at every possible root and all six
interfaces of the former forty-vertex core to change simultaneously. Its
restriction is the explicit preservation of \(L^0_{ij}\), not a frozen root
or core. The condition preserves every candidate in this defined family;
no reduction of arbitrary six-Petersen targets into this family is claimed.

## Local-palette completeness

For an arrow \(u\mapsto v\), its contribution to (1) consists of the seven
cells

\[
\{(u,v)\}\cup\{(w,v):w\sim_{P_i}u\}
\cup\{(u,w):w\sim_{P_j}v\}.
\]

An arrow can be retained only if these cells lie in the fixed support of
\(L^0_{ij}\). The backtracking enumerator chooses one such arrow in each
row, uses each column once, and rejects overlapping contributions. This
does not remove any solution of (1), because its target entries are all
zero or one. Conversely, ten disjoint seven-cell contributions fill all
seventy support cells, proving that every completed assignment solves (1).
Thus the local enumeration is exact in both directions.

The already completed 01 and 23 domains were reused, rather than searched
again. The other thirteen domains were newly enumerated. All fifteen
returned exactly two solutions, and their matrix equalities were checked
directly. Preparation took 0.005639038 CPU seconds and 0.006041016 wall
seconds.

## Why the earlier fixed-root exclusion does not settle this family

The
[fixed-A normalization](PETERSEN_FIXED_ROOT_CONSTRAINTS.md)
and its
[all-layer-exchanging obstruction](PETERSEN_FIXED_ROOT_LAYER_OBSTRUCTION.md)
require the five other Petersen graphs, pulled back through a chosen root's
matching interfaces, to be the same graph \(Q\). For the original seed,
which belongs to the present family, the numbers of distinct pulled-back
graphs for the six choices of root are

\[
(3,3,3,3,2,2).
\]

The equality or inequality of these pulled-back graphs is unchanged by
coordinate relabeling of any fiber. Hence with this six-fiber partition
the seed has no root satisfying the fixed-A hypothesis. The present family
is therefore not contained in that theorem's stated coordinate-normalized
domain. No unsupported claim about every possible repartition of the graph
is needed or made.

All members do retain the local zero-overlap property, because their seven
route contributions remain disjoint. That shared necessary property does
not make this experiment a repeat of an earlier search: the previous
all-fifteen-matching annealing was not a complete enumeration of (1), and
the fixed-root table experiment did not decide this independently changing
fifteen-interface domain. The present run is a new finite simultaneous
assembly, with no randomized moves and no SAT call.

## Complete expanded-graph enumeration and all minima

The C++ enumerator visits every binary assignment once in Gray-code order.
Changing one bit removes the old ten matching edges and installs the
other ten. It computes every unordered pair's route count directly from
the sixty adjacency bitsets, and records the bad-pair and energy
histograms. No heuristic acceptance rule or early pruning is used.
The actual run examined all 32,768 assignments and reports
`complete=true`.

The bit order is

\[
(01,02,03,04,05,12,13,14,15,23,24,25,34,35,45),
\]

with zero choosing the original palette member. The four and only four
minimum masks are:

| Mask | Interfaces changed from the original | Bad pairs | Energy |
|---:|---|---:|---:|
| 0 | none | 20 | 50 |
| 16384 | 45 only | 20 | 50 |
| 16383 | all fourteen except 45 | 20 | 50 |
| 32767 | all fifteen | 20 | 50 |

The minima for bad-pair count and energy are the same four graphs. Each is
simple, eight-regular, has diameter three, and has all twenty bad pairs
between fibers 4 and 5. The full graphs are separate labeled objects;
no claim that they represent four distinct isomorphism classes is made.

The independent checker reads the saved expanded edge lists, constructs
new adjacency sets, and runs BFS from every vertex. It does not reuse the
enumerator's route-count cache or Gray-code state. Every minimum's full
edge list, vertex degrees, all bad pairs, actual distances, and common
neighbor sets are retained in
[the minima directory](../../../computations/dd82/construction/petersen_binary_palette_run/minima).
The aggregate
[independent verification](../../../computations/dd82/construction/petersen_binary_palette_run/independent_verification.json)
records all four results. These graphs are failed candidates, not target
constructions.

## Scope and actual resources

The finite conclusion is:

> No graph preserving all fifteen matrices \(L^0_{ij}\) of this particular
> labeled seed has diameter at most two. Any successful continuation from
> this representation must alter at least one such seven-route matrix.

This is not a statement that a graph with one changed matrix can succeed,
nor that the general zero-overlap or six-Petersen families are impossible.
The broader paired-core assembly in
[PETERSEN_PAIRED_CORE_EXCHANGE.md](PETERSEN_PAIRED_CORE_EXCHANGE.md)
has a different scope: its six released interfaces need not preserve their
local matrices, while eight others are fixed. Its RAW_UNSAT status is not
upgraded by this binary enumeration.

The one enumeration used 0.116577 child CPU seconds (0.113718 reported
inside C++). The launcher and independent BFS used 0.021836478 parent CPU
seconds, including 0.020183104 seconds specifically for BFS and its saved
outputs. Wall time was 0.272546608 seconds. The combined measured search
and checking CPU was 0.138416259 seconds, below the declared five-second
budget; the separately recorded palette preparation was 0.005639038 CPU
seconds. No SAT process was launched. All processes finished, and the
completed domain was not repeated.

Sources and complete data:

- [Palette preparation](../../../computations/dd82/construction/petersen_binary_palette_prepare.py)
  and [all local palettes](../../../computations/dd82/construction/petersen_binary_palette_run/palettes.json).
- [Enumerator](../../../computations/dd82/construction/petersen_binary_palette_search.cpp),
  [single-run launcher and independent BFS](../../../computations/dd82/construction/petersen_binary_palette_run.py),
  [actual input](../../../computations/dd82/construction/petersen_binary_palette_run/input.txt).
- [Complete search result and histograms](../../../computations/dd82/construction/petersen_binary_palette_run/search.json),
  [all minimum expanded edge lists](../../../computations/dd82/construction/petersen_binary_palette_run/minimum_graphs.edges),
  [resource record](../../../computations/dd82/construction/petersen_binary_palette_run/resources.json).

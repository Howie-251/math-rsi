# Every equitable six-by-ten target reduces to six Petersen fibers

Date: 2026-10-12. This concerns a simple eight-regular diameter-two graph
with an equitable partition into six sets of ten vertices. Equitable
means every vertex in fiber i has the same number q_ij of neighbors in
fiber j, including internal degree d_i. Existence of such a partition
is an additional hypothesis, not a theorem about arbitrary sixty-vertex
graphs.

## Current theorem

Every such target admits a partition into six induced Petersen graphs,
with a perfect matching between each pair. The resulting partition can
differ from the original one. The full six-Petersen model remains OPEN.
No legal graph above57 or arbitrary order60 exclusion follows.

Indeed the original partition can only have uniform internal degree2
or uniform internal degree3. All other uniform degrees and every
nonuniform degree pattern have now been excluded within this model.

## Uniform internal degrees

The [uniform model reduction](SIX_FIBER_UNIFORM_MODEL_REDUCTION.md)
excludes degrees0,1 and at least4. Its degree2 case forces doubled K3,3
interfaces and regroups into six Petersen fibers. Its degree3 case forces
all cross degrees1 and each internal graph to be Petersen.

The degree1 exclusion uses the published complete ten-type combinatorial
(10_3) classification and actual quotient and general bridge enumerations.
Root and C11 reviewed that chain, retaining these dependencies. No Lean
completion is claimed.

## All nonuniform cases are now excluded

The [necessary quotient screen](SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md)
proves each d_i is at most3. Of80 sorted nonconstant degree tuples,40
are ruled out by parity. All79,313 row-compatible symmetric quotients
for the other40 tuples were enumerated, leaving98 matrices in four
relabeling orbits:

| Internal degrees | Labeled quotients | Exclusion |
| --- | ---: | --- |
| (0,0,1,2,2,3) | 2 | [Exact route-matrix contradiction](VARIABLE_001223_OBLIGATION.md) |
| (1,1,1,1,1,3), outer five-cycle | 12 | Odd-cycle determinant contradiction in the screen paper |
| (1,1,1,1,1,3), other orbit | 60 | [Reuse of the independently empty left bridge domain](VARIABLE_D1_FIVE_ONE_BRIDGE_EXCLUSION.md) |
| (1,1,1,1,3,3) | 24 | [Local exact-hub obstruction](VARIABLE_HUB_LOCAL_ASSEMBLY.md) |

The first two are analytic arguments. The third imports the previous
complete local bridge screen; an unused virtual source dual matching
need not equal an actual graph matching. The fourth is a new local
finite obstruction, with the same published ten-configuration dependency.

For the last orbit, the exact diagonal block at0 and cross block04
would supply S,Y,Z,C and permutations M,N,P with

    S + Y Y^T + Z Z^T = J + 4I,
    M + S M + M C + Z N + Y P = J.

After normalizing M=I and eliminating C, each target column chooses one
unused configuration triple and one unused two-factor edge. Disjointness
from each other and from its matched pair leaves exactly the three
neighbors of C. Symmetry is the only unforced adjacency condition.
All71 local catalog states fail this finite obligation completely:
1,818 nodes and zero complete leaves. A separate fixed-order Python set
implementation, starting from the original configuration triples,
reproduced all71 zeros in12,383 nodes. Thus the final24 matrices are
excluded, with no connectivity or spectral pruning involved.

Consequently no nonuniform degree tuple survives. Together with the
uniform reduction this proves the stated six-Petersen conclusion.
The98 raw quotient survivors and their four orbits remain saved unchanged.

## Actual construction feedback and resource records

Before the last obstruction, a [bounded degree-preserving experiment](variable_fiber_candidates60_experiment.md)
generated full60-vertex graphs in the last quotient. One27.010034
CPU-second run ended at155 bad pairs, still diameter3.

The next [exact-Gram construction](variable_fiber_exact_gram_experiment.md)
actually generated five complete graphs satisfying all four required
same-fiber identities. They had352 to392 bad pairs. Their complete
hub04 failure matrices were retained. Generation and independent
BFS/Gram checks used0.093139 CPU seconds. The proposed optimizer was
cancelled before launch when the exact local obstruction closed its
domain; zero optimizer processes were run.

The nonuniform quotient screen used0.129702 process CPU seconds,
with0.070994146 CPU seconds for the saved-survivor/orbit check.
The new local hub search used0.006882 process CPU seconds and0.008374736
wall seconds; its independent check used0.062481497 CPU seconds.
These timings exclude proof writing, reading and model waits.

## Review and global boundary

C11 accepted the uniform model chain. C12 accepted the nonuniform
necessary screen and12/60-orbit exclusions. C13 accepted the2-orbit
analytic exclusion and the then-two-domain frontier. C14 read the full
new local hub proof, both implementations and actual complete results,
and accepted the obstruction and strengthened integration. Its raw
response and root disposition are saved under reviews/dd82/20261012_C14_*.
Reviewer agreement is
not a replacement for the actual proofs and saved computations.

The mathematical interval remains57 <= N(8,2) <= 61. Graphs without the
stated equitable partition are outside this theorem; the remaining full
six-Petersen construction problem is not solved by this reduction.

# Full false-twin58 matching-cover CNF

This encoding covers the entire order-58 false-twin construction, with
all 28 matching interfaces independent before a legitimate root-coordinate
normalization. No C7 action, translation action or relation among distinct
free interfaces is imposed. It is a substantive removal of the symmetry
assumption from the completed f9 experiment, under the same parent run
`dd82-v3-f9-c7-20261013-0749`.

The preparation and independent input check are complete. The sole
authorized solver attempt stopped at its 256 MiB proof-output limit after
87.819016 CPU seconds, with **OUTPUT_LIMIT_UNKNOWN**. It found neither a
reported SAT model nor an UNSAT result. The full false-twin58 family
remains undecided. No new valid graph was found.

## Exact mathematical domain

[FALSE_TWINS58_EIGHT_SIX_FIBERS.md](FALSE_TWINS58_EIGHT_SIX_FIBERS.md),
Sections 1–2, proves the following two-way representation. A degree-eight,
diameter-two graph of order 58 containing false twins consists of twins
u,v, eight independent common neighbours s_i, and eight independent sets
G_i of six vertices. Each s_i is adjacent to u,v and all of G_i. Every
pair of fibres G_i,G_j is joined by a perfect matching. Conversely these
rules construct a simple eight-regular graph of order 58 and 232 edges;
all pairs except different-fibre pairs already have distance at most two.

Choose any fibre G_0 and label its six vertices. Label each vertex of G_j
by its unique matching neighbour in G_0. The seven blocks Q_0j then all
become identity. These are independent coordinate changes on seven
fibres, so the other 21 perfect matchings remain completely arbitrary.
The root gauge loses no graph from this construction up to relabelling.
It asserts no automorphism. Combined with the cited representation, the
CNF therefore covers all order-58 targets containing false twins.

For i<j and a,b∈{0,…,5}, let x_(i,a,j,b) mean the edge between the two
fibre vertices. Reversed references use the same variable, transposed.
Each row and column of each of the 28 blocks has exactly one true entry.
For the seven root blocks, unit clauses set x_(0,a,j,b) true exactly
when a=b. There are no further symmetry restrictions or extra cuts.

For any i<j,a,b, every possible length-two path between the corresponding
vertices has its intermediate point in G_k with k≠i,j. Parents, twins
and vertices within the endpoint fibres cannot serve as such a common
neighbour. Thus the complete coverage requirement is

\[
x_{i,a,j,b}\ \lor\
\bigvee_{k\notin\{i,j\}}\ \bigvee_{c=0}^{5}
\left(x_{i,a,k,c}\land x_{k,c,j,b}\right).\tag{1}
\]

For each of the 36 paths introduce z and use exactly

\[
(\neg z\lor p),\qquad(\neg z\lor q),\qquad
(z\lor\neg p\lor\neg q).
\]

These three clauses are equivalent to z↔(p∧q). The final coverage clause
contains the direct-edge literal and the 36 path literals. Hence an
assignment satisfies the CNF if and only if its 28 perfect matchings
construct a graph of diameter at most two. This converse uses all
Tseitin implications, not merely one-way path witnesses.

## Implemented input and seed migration

The actual generator is
[full_matching58_prepare.py](../../../computations/dd82/construction/full_matching58_prepare.py).
It reuses only the existing `CNFEmitter` and `add_iff_and` functions from
the local archive; none of the archive's old mathematical restrictions
or search routines is run. Perfect matching rows and columns use one
positive clause and the 15 pairwise negative clauses on their six
entries. The exact input sizes are:

| Item | Count |
| --- | ---: |
| Matching-edge variables | 28·36 = 1,008 |
| Path variables | 28·36·36 = 36,288 |
| Total variables | 37,296 |
| Perfect matching clauses | 28·12·16 = 5,376 |
| Root identity units | 7·36 = 252 |
| Tseitin clauses | 3·36,288 = 108,864 |
| Coverage clauses | 28·36 = 1,008 |
| Total clauses | 115,500 |
| Input bytes | 1,839,790 |

Files in
[`full_matching58_run/`](../../../computations/dd82/construction/full_matching58_run/)
include `input.cnf`, `encoding.json`, the complete `variables.json` mapping,
and `coverage.json` with actual clause numbers and original vertex pairs.
The CNF contains the seven root blocks explicitly and leaves unit
propagation to the solver; it does not silently drop any path.

The migrated seed is the best failed f9 graph, with exactly the same
labels and complete edge set. Twins are 0,1, parents are 2,…,9, and
G_i={10+6i,…,15+6i}. Its 28 matchings are extracted from the actual
edge table independently of the old A/B/C parametrization. Their union
with the 64 fixed scaffold edges is checked to equal the source graph.
The seed's seven root interfaces are already identity.

`seed.assignment.txt` gives all 37,296 variable values: actual edge values
and each actual conjunction. A direct evaluation of the saved DIMACS
finds exactly 105 false clauses, all coverage clauses. Matching, gauge
and every Tseitin clause hold. Their vertex pairs agree exactly with the
previous independent BFS result; no repeated BFS was needed for the
unchanged graph. `seed.cnf_check.json` records the clause numbers and
all pairs. The seed constrains no free interface in the CNF.

Preparation used 0.385197468 CPU seconds and 0.502547514 wall seconds.
The separate agent `cyclic_lift58_60` checked the source, actual variable
mapping and seed/DIMACS consistency independently before solver launch.
Its standalone
[checker source](../../../computations/dd82/construction/full_matching58_independent_cnf_check.py)
imports none of the generator. It reconstructs every seed interface and
all variable values, verifies the geometric endpoints of all 36,288 ANDs,
and verifies that the actual 115,500 DIMACS clauses equal the full expected
mathematical clause sequence. Its 105 false clauses and original vertex
pairs agree exactly with the seed assignment and existing independent BFS.
The actual
[independent result](../../../computations/dd82/construction/full_matching58_run/independent_cnf_check.json)
records 0.241846989 CPU seconds and 0.349581100 wall seconds. No new BFS
or solver was invoked by that check. This is local same-family review,
not a replacement for Gemini.

## Authorized solver interface and interpretation

The project already has executable CaDiCaL at
`.tools/lean-4.24.0-linux/bin/cadical` and the independent LRAT checker at
`.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim`. The generated
`interfaces.json` records these actual paths, the SAT model decoder and
the existing full-graph BFS interface. The solver command shape is
`cadical --lrat -t 120 input.cnf proof.lrat`; checking uses
`lrat-trim --no-trim input.cnf proof.lrat`.

After Gemini accepted removing the translation coupling, the parent
authorized a single attempt in
[full_matching58_solve.py](../../../computations/dd82/construction/full_matching58_solve.py):
120 CPU seconds, one pinned CPU, 4 GiB address-space limit and 256 MiB
proof-output cap. No separate solver profile is run: the measured encoding
and seed consistency form the preparation profile. The runner saves its
command, logs, resource usage and outcome. It does not preserve internal
learned-clause state for resumption and does not restart after UNKNOWN.

A SAT model must satisfy the actual saved CNF, be expanded into a full
58-vertex graph, and pass the independent all-source BFS implementation
before it is reported as a target. UNSAT remains RAW until the existing
LRAT checker verifies the exact input and proof. A checked UNSAT result
would exclude the full false-twin58 family, while a timeout or output
limit gives no mathematical exclusion. Neither result alone settles
arbitrary order-58 graphs without false twins.

The parent owns the same-thread Gemini review and shared project state.
This task retains the proof-writer and experiment-bridge V3 mathematical
adaptation used in the preceding f9 phase: exact graph input and coverage,
bounded computation, full failed/valid objects, distinct review evidence,
and no hashes, new dependencies or research-platform expansion.

## Redundant collision constraints derived after preparation

The following necessary conditions have **not been added to the original
CNF**. They follow from its existing matching and coverage conditions;
they do not exclude the full family. The derivation is pure mathematics,
with no further solver run or enumeration. Its full version is
[FULL_MATCHING58_COLLISION_CONSTRAINTS.md](FULL_MATCHING58_COLLISION_CONSTRAINTS.md).

Let H be the adjacency matrix of the 48 fibre vertices and put
D=diag(J6,…,J6), J=J48. Distinct vertices of one fibre have no common
H-neighbour, since their neighbours in each other fibre are distinct.
Thus the diagonal blocks of H² are 7I6. Each off-diagonal block
K_ij=Q_ij+Σ_(k≠i,j)Q_ik Q_kj has row and column sums seven. Coverage
requires K_ij≥J6, so E_ij=K_ij−J6 is a permutation matrix. With E_ii=0,
E is a simple seven-regular matching cover on the same eight fibres and

\[
H^2+H=7I+J-D+E.
\]

The matching blocks give HD=DH=J−D, while regularity gives HJ=JH=7J.
Consequently HE=EH. This E is the actual excess of H, not an independent
graph whose entries may be chosen separately.

Every entry of a cross-fibre block K_ij is one or two. If xy is an H-edge,
its direct route already contributes one, so x,y have at most one common
H-neighbour. Therefore an edge belongs to at most one triangle, and
the graph induced on the seven neighbours of any vertex is a matching.
If xy is a nonedge in different fibres, its common-neighbour count is
one or two. A four-cycle has four distinct fibre indices and no diagonal
edge: repeated opposite fibre indices would give forbidden common
neighbours within one fibre, and a diagonal edge would have two common
neighbours.

For a vertex x, let t_x and q_x count the triangles and four-cycles
containing x. Exactly 2t_x vertices lie in N_H(x)∩N_E(x). Every vertex
in N_E(x)\N_H(x) is the opposite vertex of a unique four-cycle through
x, and every such cycle arises this way. Since E has degree seven,

\[
2t_x+q_x=7,\qquad 3T+2C_4=168,
\]

where the second identity sums the first over all 48 vertices. In
particular, each vertex lies on at least one four-cycle, T is even,
T≤48 and C4≥12. These counts alone give no contradiction.

The existing root normalization makes the neighbour set of x_(0,a)
equal to {x_(i,a):1≤i≤7}. Its induced graph must be a matching. Hence,
for each outer fibre i and coordinate a, the six existing edge literals

\[
\{x_{i,a,j,a}:j\in\{1,\ldots,7\}\setminus\{i\}\}
\]

satisfy at most one. Pairwise encoding adds exactly
7·6·binom(6,2)=630 binary clauses and no variables:

\[
\neg x_{i,a,j,a}\ \lor\ \neg x_{i,a,k,a}
\qquad (j<k,\ j,k\ne i).
\]

Reverse interface references use the existing transposed variable.
These clauses could improve propagation by exposing a consequence of
the six-column coverage requirement directly. Their performance has
not been measured, and the solver attempt already running uses the
unchanged original CNF.

## Completed single attempt

The solver ran once after the independent input check passed. Its exact
[launch record](../../../computations/dd82/construction/full_matching58_run/launch.json),
[solver log](../../../computations/dd82/construction/full_matching58_run/solver.log)
and [result](../../../computations/dd82/construction/full_matching58_run/result.json)
are retained with the original input. The result is:

| Item | Actual value |
| --- | ---: |
| Solver launches | 1 |
| CPU limit | 120 seconds |
| Actual child CPU | 87.819016 seconds |
| Actual wall time | 112.245408591 seconds |
| Process return code | −25, SIGXFSZ |
| LRAT output bytes | 268,435,456 = 256 MiB |
| Status | OUTPUT_LIMIT_UNKNOWN |
| SAT models saved | 0 |
| UNSAT reports | 0 |
| LRAT checker invocations | 0 |
| Retained resumable solver state | none |

The file-size cap ended the attempt before the CPU budget. The truncated
`proof.lrat` is incomplete output, not a certificate of nonexistence.
Without an UNSAT report there was no reason to invoke the certificate
checker. No second attempt, changed seed, increased limit or fallback
solver was launched. The preparation metadata retain their creation-time
`PREPARED_NOT_RUN` status; the run's current state is in `result.json`.

The migrated 105-bad-pair graph is still only the prior failed seed. The
new substantive object is the candidate-preserving full-family CNF and
its bounded, unresolved attempt. Removing all group coupling was actually
implemented; the result provides no further mathematical exclusion and
no evidence of satisfiability. The parent handles Gemini's same-thread
result review and any later research decision; at this writing review of
the stopped solver outcome is pending.

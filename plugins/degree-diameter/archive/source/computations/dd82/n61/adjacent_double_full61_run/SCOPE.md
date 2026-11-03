# Full61 adjacent-double-defect model: source and scope

At initial source delivery, **no prepare, solver, or checker was executed by the
implementation agent**. This is the V3 mathematical adaptation of the project's
`experiment-bridge` skill. The root owns the mathematical review, independent
source review, actual bounded execution, and Gemini discussion. This document
does not attest completion of those stages.

The branch consists of an actual simple degree8 diameter2 graph on61 vertices
whose actual defect `B=A²+A−7I−J` has `A_uv=1,B_uv=2`. Necessary connected
support and `B<=2` are inherited from
[CONNECTED_TRIPLE_EXCLUSION.md](../../../../proofs/dd82/n61/CONNECTED_TRIPLE_EXCLUSION.md).
All new constraints refer to
[ADJACENT_DOUBLE_REPEAT_LOCAL.md](../../../../proofs/dd82/n61/ADJACENT_DOUBLE_REPEAT_LOCAL.md)
and the root's
[ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md](../../../../proofs/dd82/n61/ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md).
The latter proof and source review must be accepted before a checked CNF
contradiction can be transferred to every graph in this branch.

## Labels and coverage of normalizations

| Object | Labels |
|---|---|
| u,v,s,t | 0,1,2,3 |
| U,V | 4–8,9–13 |
| S,T | 14–19,20–25 |
| q,p | 14,20 |
| Z | 26–60, five consecutive groups of7 by U parent |

The local proof gives this disjoint partition, the core neighborhoods, and
the placement `p∈T,q∈S`. Its section5 proves that independent row and column
permutations bring `C=B[U,V]` to `I+P_sigma`. A degree2 bipartite multigraph
decomposes into even cycles, including a doubled edge; its component sizes
are exactly the seven partitions of5. The encoder keeps **all seven** in
one CNF with seven exactly-one selectors:
`5`, `4+1`, `3+2`, `3+1+1`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`.

For each type, the actual `(U_i,V_j)` cell size is `H_ij=1+C_ij`.
Each row has7 points. Assign the seven consecutive Z labels in U row i
to V columns in increasing j, with exactly H_ij labels per cell. Thus
U–Z adjacency is unconditional and V–Z adjacency is conditioned on the
selected type. Every actual graph can receive these labels; label
permutations within each cell are still free.

After selecting these U/V labels, independently label the five ordinary
S points and the five ordinary T points by their unique B-unit endpoint
in U. This uses only the separate S/T label freedoms proved in section5.
Their B matchings to V remain free. The binary interface `K=A[S,T]`
remains free except for its proven row/column degrees. The five Z
neighbors of q are **not** additionally forced to an identity transversal;
the V freedom has already been used for C. No combined or simultaneous
normalization beyond these proved steps is used.

## Exact clauses on the original graph

There is one primary adjacency variable for each of the1830 unordered
pairs of distinct original vertices. No loop variable exists. Every
initially unforced pair remains its own variable.

- The complete core neighborhoods are fixed: `N(u)={v,s,t}∪U`,
  `N(v)={u,s,t}∪V`, `N(s)={u,v}∪S`, and `N(t)={u,v}∪T`.
  U,V,S,T are independent; U–V and U/V–S/T edges are zero. The
  U–Z parent labels are fixed as above. Every fixed pair and its reason
  is saved in `encoding.json`.
- Every vertex has exact degree8 over all60 original possible neighbors.
  Every Z point has one neighbor in each of U,V,S,T and four in Z.
  Every U/V point has seven Z neighbors. In S, q has two T neighbors
  and five Z neighbors; every other point has one and six. The T counts
  are the analogous ones with p. No pattern for the seven S–T edges
  is selected.
- For every original pair a<b and each of the59 genuine third vertices w,
  a fresh auxiliary is equivalent to `A_aw AND A_wb` through all three
  clauses of the AND equivalence. The coverage clause is the direct-edge
  variable or any of these59 auxiliaries. This gives107970 actual path
  auxiliaries and1830 coverage clauses, including for already fixed edges.
- Every pair has `mu(a,b)+A_ab<=3`, equivalent to inherited actual `B_ab<=2`.
  If a proven exact B value is available, an exact count instead imposes
  `mu(a,b)+A_ab=1+B_ab`; since those values are0,1,2, this already implies
  the upper bound. There is no independent B variable or pseudo common
  neighbor. Unary thresholds are equivalences in both directions.
- Exact B counts cover every entry of the four core B rows in equations
  (2),(3); `B[U]=B[V]=0`; `B[U/V,Z]=0`; all U/V entries to p,q zero;
  and the ordinary S/T-to-U matching entries `B(U_i,S_j)=B(U_i,T_j)=delta_ij`.
  The primary labels use S[0]=q,T[0]=p, so here j runs through their
  five ordinary points. Remaining pairs receive only the global bound.
- For propagation, the same proven U-to-S/T common-neighbor counts are
  also imposed directly on the actual seven-point U fibers: p and q
  meet each fiber once, and an ordinary S_j or T_j meets fiber i in
  `1+delta_ij` neighbors. Conditional on each of the seven C selectors,
  p and q each meet each actual V fiber once. These redundant counts
  follow from the exact B values above and actual parent incidences;
  they do not fix which points in a fiber are chosen or impose a
  preferred U-to-V transversal permutation.
- The actual `B[U/V,Z]=0` counts are also imposed directly on Z edges:
  a Z point has no neighbor in its own seven-point U fiber and one
  neighbor in each of the other four U fibers. Conditional on the C
  selector, the same holds for its actual V fibers. For instance
  `N(U_i)={u}∪Z_i` and no Z point is adjacent to u, so
  `mu(U_i,z)=d_Z_i(z)=1-A_Ui,z`. The direct degree constraints are this
  identity, with the source count still retained, not a new restriction
  or a prescribed matching between any two fibers.

The first version intentionally omits explicit constraints for the proven
`P=B[S,T]` permutation matrix, the variable internal B[S]/B[T] edges,
the remaining S/T–Z defect port identities, and the double-defect path
forest. It also omits a B-support-connectivity constraint. Omitting
necessary conditions enlarges the CNF domain; it does not invalidate
an exclusion. All SAT models still determine complete original graphs
and must pass the independent graph check even if a derived condition
needs to be revisited.

Conversely, each actual adjacent-double target admits the documented
labels and chosen selector, then its actual A edges, actual AND paths,
and actual unary thresholds satisfy every emitted clause. This is the
required coverage argument, conditional on the accepted mathematical
proof and independent source check. UNSAT for this model can exclude
adjacent double defects at61; it cannot alone exclude nonadjacent double
defects, triangles with a unit defect, or all61-point graphs.

## Reused code and actual artifact handling

The encoder imports only the generic `CNFEmitter`, `enforce_exact`,
`unary_thresholds`, `enforce_exact_under_condition`, and `add_iff_and`
definitions from the archived n62
helper. It never calls that module's historical ABEncoder or guarded main.
Its constants, branches, old solver runs, and old Lean are not used.

The runner reuses the existing full61 runner with adjacent-branch wording.
Preparation records all actual emitted variable/clause counts, exact degree
constraints, all-pair coverage records, exact/upper actual-B counts, and
seven selector-to-cell assignments. No runtime or counts are fabricated
at source delivery. The emitter's ordinary temporary DIMACS body is
removed on success or a caught exception; a killed preparation is a failed
attempt and may leave an incomplete body.

SAT decoding validates every saved DIMACS clause against the complete
solver assignment, requires exactly one selected C type, and saves that
type, the complete244-edge graph, and the assignment. The runner then calls
the existing independent `construction/verify_hs_candidate.py`. Acceptance
requires61 vertices,244 simple edges, every degree8, no bad pair, and
diameter at most2 from independent all-pairs BFS. The full candidate is
retained even if further research detects a conflict with an inherited lemma.

## Root-owned bounded first execution

Commands for the root after review; the implementation agent did not run them:

```bash
python computations/dd82/n61/adjacent_double_full61_run/runner.py prepare --cpu 1
python computations/dd82/n61/adjacent_double_full61_run/runner.py solve --cpu 1
```

Preparation receives20 CPU/30 wall seconds. One solve receives at most50
CPU/70 wall seconds, with a48-second CaDiCaL soft limit by default.
SAT alone starts decoding and independent BFS, each with5 CPU/10 wall
seconds. Each child uses one available CPU,4 GiB address-space limit;
the solver additionally has a256 MiB per-file cap on proof and log.
There are no automatic restarts, saved internal solver trees, or automatic
certificate checks. Actual signed exit codes, termination signals, child
CPU/wall measurements, input, logs and even partial LRAT are retained.
UNKNOWN, timeout, output limit and process failure do not prove exclusion.

Exit20 is `RAW_UNSAT`. Only then may the root separately run:

```bash
python computations/dd82/n61/adjacent_double_full61_run/runner.py check --cpu 1
```

The existing `lrat-trim --no-trim` checker receives the exact saved
`input.cnf` and `proof.lrat`, with50 CPU/70 wall seconds. Only exit20
together with an actual `s VERIFIED` line changes the status to
`CHECKED_UNSAT_TEMPLATE`. That certifies the saved CNF; transferring it
to the mathematical branch still requires the proof and coverage/source
reviews. No certificate or solver claim is made by these prepared sources.

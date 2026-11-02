# Full61 triple-defect template: prepared encoding and scope

Status: **source prepared, no CNF generated and no solver or checker executed** at delivery. This is implementation under the project's V3 mathematical `experiment-bridge` adaptation. It is not a source review of this implementation. The root is arranging a separate reviewer and the current Gemini thread; the newer layer-interface derivation also remains subject to its root-managed review.

The mathematical target is an actual simple graph on61 vertices, degree8 and diameter at most2, whose actual weighted defect `B=A²+A−7I−J` has connected positive support and an entry3. The inherited derivation is [CONNECTED_TRIPLE_REPEAT_LOCAL.md](../../../../proofs/dd82/n61/CONNECTED_TRIPLE_REPEAT_LOCAL.md); the added interface dependencies are [CONNECTED_TRIPLE_LAYER_INTERFACES.md](../../../../proofs/dd82/n61/CONNECTED_TRIPLE_LAYER_INTERFACES.md). The latter's scope and equations, not the small `(C,σ)` catalogue, justify the layer constraints.

## Labels and necessary normalization

| Object | Vertex labels |
|---|---|
| u,v,w,a,b,c,d | 0,1,2,3,4,5,6 |
| U,V | 7–10,11–14 |
| T_a,T_b | 15–19,20–24 |
| T_c,T_d | 25–30,31–36 |
| Z | 37–60 |
| γ,δ,F | 25,31,{37,38,39,40} |

Every target in this branch admits these labels: the local reduction gives the exact disjoint partition and neighborhoods of u,v,a,b,c,d. The interface lemma identifies the unique w neighbors γ∈T_c and δ∈T_d and four distinct F⊂Z, so they may receive the displayed labels. Their full neighborhoods are fixed exactly as in the root's specification; no additional neighbor of one of those seven vertices is allowed.

The actual U/V perfect matching allows V to be labelled relative to U. Label T_a arbitrarily and T_b by its actual matching to T_a. Each of the T_a→T_c and T_a→T_d maps is a bijection onto the five points other than γ or δ. Independently choose those two sets of five labels so that T_a[i] is adjacent to T_c[i+1] and T_d[i+1]. These choices use disjoint available label freedoms. The T_b→T_c and T_b→T_d permutations are still represented by all25 possible entries in each corresponding non-special5×5 block, with row/column degree1; neither permutation is fixed to identity.

Case I has r,s∈F, distinct. Label them Z[0],Z[1] and label the other two F points arbitrarily. No U/V port label or Z incidence was fixed before this step. Case II instead has r=δ and s=γ, with F arbitrary. A single Boolean selector enables one case or the other in the same CNF; the Tc/Td edge γδ remains variable in both cases. This covers both port cases and both possible γδ adjacencies. No C matrix, σ permutation, equitable quotient, or symmetry of the actual graph is selected.

## Clauses and their meaning

There are1830 primary variables, one per unordered pair of distinct vertices. Thus A is symmetric and binary, and no loop variable exists. Every initially unforced A edge remains its own variable. The preparation record lists every fixed pair and its reason.

- Fixed zeros encode independent U,V and T layers, the absence of U/V–T edges, and the proven full neighborhoods and normalized matching/bijection blocks. The layer lemma's final triangle restriction also fixes F independent and F–{γ,δ} empty; it does not fix γδ.
- Every one of the61 vertices has an exact degree8 constraint over all60 possible neighbors, using the existing exact unary-threshold helper. This is also imposed on vertices whose neighborhoods were already fixed.
- The unconditional interface constraints give each Z point one neighbor in each U,V, the two remaining free T_b bijections, degree4 from every T_a/T_b point into Z, and `d_Ta(z)=d_Tb(z)=1−A_wz`. Their necessity is the displayed layer-degree table, derived from the same actual A and complete S defect rows.
- The case-conditional counts retain the full Tc/Td interface: in Case I it is any perfect matching; in Case II γ's row and δ's column have degree2 and all other rows/columns degree1. Tc/Td-to-Z counts and `d_Z(z)=2+A_wz−[z=r]−[z=s]` use the corresponding case's r,s. Conditional counters are defined equivalently by CNF in both directions; only their exact target is guarded by the case literal.
- For every pair u<v and every actual third vertex k, an auxiliary is equivalent to `A_uk ∧ A_kv` through all three AND clauses. The pair's coverage clause is the disjunction of its direct-edge variable and all59 such auxiliaries. All1830 pairs are covered, including ones already forced adjacent. There is no orbit reduction or hypothetical independently selected path. The total number of path auxiliaries is107970.

Consequently a satisfying assignment directly determines an original degree8 diameter-two graph. Conversely, any actual graph in the connected triple branch, after the justified labels above, supplies a satisfying primary assignment and its actual threshold/path auxiliaries. The case selector is set to its actual port case. This is the coverage needed to connect a later certified contradiction to the entire connected triple branch, conditional on acceptance of the inherited mathematical reduction and this encoding.

B is not an independent CNF object, and no simplicity assumption is imposed on it. Its row4 and nonnegativity follow for a full graph from degree8 and coverage. B connectivity is deliberately not encoded: the CNF is a necessary relaxation of that branch. A model with disconnected defect is still a full target graph and must be retained. Fixed N(u),N(v) give uv a nonedge and exactly four common neighbors, so the actual B_uv is3 in every accepted model. This implementation alone neither excludes all order61 graphs nor addresses the connected branch with no triple entry.

## Existing components and artifacts

`encode.py` imports only callable generic `CNFEmitter`, exact-cardinality/threshold, and three-clause AND definitions from the existing archived helper. It does not call the historical n62 encoder, main routine, branch data, enumeration or solver. The existing CaDiCaL and LRAT checker executables were located; no package was installed. The existing `construction/verify_hs_candidate.py` accepts full61 edge lists and performs an independent all-pairs BFS.

Preparation will write `input.cnf`, `encoding.json`, primary edge mapping, exact-degree records and coverage records. No generated counts or CPU measurements are claimed until that run. The streamed emitter body is its ordinary temporary file, removed on successful completion or a caught encoding exception; a hard-killed preparation may leave an incomplete body and is a failed attempt, not a prepared encoding.

SAT decoding checks every actual DIMACS clause against the complete saved solver assignment, then writes `candidate.json`, the full244-edge `candidate.edges`, and `model.assignment.txt`. The solver log is retained. The runner invokes the existing independent BFS script and accepts a target only when it reports n=61,244 edges, degree8 everywhere, no unreachable or distance>2 pair, and diameter≤2. No checker used to generate CNF substitutes for this graph check.

## Bounded first execution, owned by the root

Prepared commands; **none has been run**:

```bash
python computations/dd82/n61/triple_full61_run/runner.py prepare --cpu 1
python computations/dd82/n61/triple_full61_run/runner.py solve --cpu 1
```

Preparation has its own single-core20 CPU/30 wall second bound and writes the actual process result. The first solve defaults to a50 CPU/70 wall second process cap, with a48-second CaDiCaL soft limit. Only on SAT are decoding and independent BFS added, each at most5 CPU/10 wall seconds; the sum of child budgets is at most60 CPU/90 wall seconds. A shorter first profile can set `--solver-cpu` between3 and50 and `--solver-wall` between5 and70 before the single permitted launch. There is no automatic restart or follow-up search. All child phases use one specified available CPU and4 GiB address-space limits.

The solver writes LRAT with a256 MiB per-file limit applying to its proof and log. The runner saves the actual signed exit code and signal; on wall timeout it kills and waits for the process, retains that real return code, and records the timeout separately. A kill, output limit, zero/UNKNOWN return or other failure is not an exclusion. The original log, possibly partial proof, launch command, resource measurements and result are retained.

Exit20 is only `RAW_UNSAT`. It does not start another job. If that occurs, the root can separately launch the existing checker under its own50 CPU/70 wall bound:

```bash
python computations/dd82/n61/triple_full61_run/runner.py check --cpu 1
```

Only checker exit20 with an actual `s VERIFIED` line changes the result to `CHECKED_UNSAT_TEMPLATE`; timeout or failure leaves it raw. Applying that certificate to the full connected triple branch still requires the independently reviewed necessity and coverage argument above. No certificate for old work is regenerated, no graph is claimed from a quotient, and no runtime evidence or review acceptance is fabricated at preparation time.

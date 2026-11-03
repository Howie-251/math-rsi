# Produced P33 copy family: eight endpoints, fresh acceptance separate

All eight complete edge files were produced from the same immutable160050-vertex,5121600-edge source. This production receipt does not itself accept new graphs. The separate fresh validation has since returned actual `PASS_ALL_EIGHT_P33_ENDPOINT_GRAPHS`; its proof and receipts are in `independent_acceptance/`. Root owns the acceptance ledger.

The source was parsed exactly once. During that parse the1650 supplied centers' actual source neighborhoods were collected and compared with the independently supplied pin lists; every comparison had exactly64 vertices. The105600 source pins have unique base-center owners, including105567 vertices below160000 and33 of the original50 fill vertices. Those original fill vertices are source vertices throughout this construction. No current clone graph is used to define any neighborhood.

For base index b=50*pointIndex+spreadIndex and copy c, clone j=1650*c+b is labeled160050+j and has exactly the source neighborhood of base center b. There are no new-new edges. `ORDERED_CLONE_RECIPE.tsv` contains the maximum13200 clone rows in increasing j; lower endpoints use its initial1650k rows. `PREFIX_LOADS.csv` records the exact source load histogram after every prefix0,...,13200.

## Actual files and degrees

Every file has an `n m` header followed by a strict u<v lexicographic body. The writer emits all retained source edges for each smaller endpoint before that endpoint's new neighbors, whose labels increase with copy. This preserves the entire original5121600-edge set and introduces no repeated edge or new-new edge. Degrees are counted from the actual written records, and every new vertex has degree64.

| k | degree | n | m | degree64 vertices | degree64+k vertices |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 65 | 161700 | 5227200 | 56100 | 105600 |
| 2 | 66 | 163350 | 5332800 | 57750 | 105600 |
| 3 | 67 | 165000 | 5438400 | 59400 | 105600 |
| 4 | 68 | 166650 | 5544000 | 61050 | 105600 |
| 5 | 69 | 168300 | 5649600 | 62700 | 105600 |
| 6 | 70 | 169950 | 5755200 | 64350 | 105600 |
| 7 | 71 | 171600 | 5860800 | 66000 | 105600 |
| 8 | 72 | 173250 | 5966400 | 67650 | 105600 |

Files are `graphs/d65_D3_n161700.edges` through `graphs/d72_D3_n173250.edges`. Per-case production RESULT and TERMINAL files are in `cases/`. Root's actual public scalar gate locates guarantee160000+1650k for these degrees; each produced order is50 larger. This is a bounded located comparison, not global optimality or priority certification. The eight endpoints use one construction rule. The underlying33-point partial ovoid is a reproduction of a published size.

## Source-only path proof for every prefix

Let S be the accepted source and c_j the source center of clone j. Every clone has exactly N_S(c_j), including source fill vertices where appropriate. The source has no isolated vertices and diameter exactly3.

Old-to-old source paths remain. For an old vertex u and clone j, take a source path from u to c_j of length at most3. When its length is positive, replace its final edge w--c_j by w--j; the length stays at most3. If u=c_j, any source neighbor w gives u--w--j of length2.

For two clones i,j, take a source path between their centers. A length3 path c_i--a--b--c_j becomes i--a--b--j. A length2 path uses its middle vertex as a common neighbor of the two clones. If the centers are adjacent, i--c_j--c_i--j is a length3 path. If the centers coincide, any source neighbor is a common clone neighbor. This handles the actual center-induced528 disjoint edges as well as the594 isolates; center independence is not assumed.

The source's non-diameter2 witness is preserved. Any new two-step old-to-old walk u--j--v through a clone can be replaced by u--c_j--v entirely in the source. Thus a pair with no source walk of length at most2 cannot acquire one through clones. This argument works for every subset or prefix of clones and does not infer the smaller graphs from BFS of the largest one.

Disjoint base pin sets imply a source vertex is adjacent to clones of at most one base center. After k complete copies its load is exactly0 or k, giving the actual displayed degree histogram. Every arbitrary prefix has the load histogram recorded by the same copy-major formula.

## Cost and acceptance boundary

The first compilation passed. Compile CPU0.874880seconds, complete production process1.085591, and wrapper/preparation approximately0.191843 give cumulative **2.152313735CPU seconds** within the30-second single-worker budget. No failed attempt or repeat source parse occurred.

Producer work performed no BFS, currentR2 check, Lean, old field/geometry reconstruction, solver, external review or extra k. The separate fresh validation actually parsed the source once for literal binding, validated all eight complete files and all59400clone immutable64-neighborhoods, computed one1650-center sourceR2-only prediction, and ran ordinary BFS only on all13200 new roots of the maximum k8 graph. All those checks passed, with21.419453053CPU seconds. This is not BFS of all59400 new roots across the family. Mathematical prefix coverage above supplies the other endpoints independently of that maximum-case BFS. Production RESULT and TERMINAL preserve the original producer-only pending-acceptance receipt; the later actual fresh PASS is recorded separately rather than attributed to the writer.

The subsequent specific Lean batch also completed all eight original endpoint targets and a separate Audit, with24new modules, no failed attempts and standard three axioms only. See `formalization/FINAL.json`, `CHECKPOINT_B.md` and the actual Audit log. The59400 independent ordered clone rows are externally bound to the compiled label formulas; no Lean ASCII parser theorem is claimed. Root manages the shared external reviews separately. All producer, fresh-validation and local formalization processes are terminal.

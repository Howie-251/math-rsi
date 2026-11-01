# 23-point structural selection: first completed interfaces

Updated 2026-10-13. This work continues T33 in the original aris4math project.

## Current validated endpoint (2026-10-13)

**The entire r=0 branch on 23 points is complete in Lean.**

`Aris4Math.ThirtyThree.TwentyThreeHighComplete.propertyB_of_no_sixes` takes only the actual `Simple5Hypergraph (Fin 23)`, pair covering, exactly33 edges, and zero degree-six vertices, and returns `PropertyB H`. All high-pair, induced-path and cluster branches are assembled. The complete build (`high-complete-build.log`,1038 jobs), independent import, expanded original Bool-coloring caller, and7-export transitive axiom audit (`high-complete-import-audit.log`) pass. Dependencies are only `propext`, `Classical.choice`, `Quot.sound`.

The structural r=1/2/3 selection results below also remain available to the parent. The complete T33 theorem is still the parent's assembly task; this r=0 result does not close the other23-point degree branches. New Grok/Gemini review is coordinated by the parent and is not claimed here.

Detailed integration: `HIGH_BRANCH_HANDOFF.md`. The chronological notes below preserve earlier intermediate states; their “in progress” descriptions are superseded by this paragraph.

## Additional current endpoint: r=1 all-unit interfaces

`TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair` now proves actual Property B when a unit-connected degree-six vertex coexists with a degree-seven pair of codegree at least three (and the actual 17-high-vertex budget). Its catalog and full actual caller have explicit successful builds. `TwentyThreeLowUnitSixSelection.exists_locks` also has an explicit successful build and independent import audit: it constructs six actual locks with a canonical zero-, one-, or two-edge high matching after all seven-degree codegrees have been bounded by two. The local 10-bit classification is complete and tied to the actual selected locks. Integration details and acceptance logs are in `LOW_UNIT_HANDOFF.md`. The parent's six-lock probability caller is the next consumer; these two results do not by themselves claim completion of T33.

## Checked Lean results

`formal/Aris4Math/ThirtyThree/TwentyThreeSelection.lean` defines the seven-degree set from the actual hypergraph and proves:

- `six_seven_budget`: actual pair covering, 23 vertices and 33 edges imply `19 ≤ 2*r+t`.
- `degree_count_cases`: the complete `r≥4`, `r=3,t≥13`, `r=2,t≥15`, `r=1,t≥17`, `r=0,t≥19` partition.
- `six_badPartners_le_two`, `seven_badPartners_le_six` and `six_codegree_le_three`: actual codegree bounds, with no supplied profile.
- `indexed_six_excess_le_two`: any injective finite lock indexing inherits the actual six-degree center's pair-excess sum bound. This is the intended bridge to local pair-budget classification.
- `exists_four_sixes`: four actual distinct six-degree locks whenever `r≥4`.
- `exists_three_sixes_two_sevens_of_count`: for `r=3`, five actual distinct locks with degrees `(6,6,6,7,7)` and every low-high codegree equal to one.
- `exists_two_sixes_three_sevens_of_count`: for `r=2`, five actual distinct locks with degrees `(6,6,7,7,7)` and all pair codegrees one except possibly pairs 01 and 23.

The latter two return a function `f : Fin 5 → V` plus `Function.Injective f`, matching the existing realization API. They do not require a profile or Property B as an input. The general two-low lemma only needs at least 13 seven-degree vertices; the actual `r=2` budget supplies at least 15.

## Executed verification

- `lake env lean Aris4Math/ThirtyThree/TwentyThreeSelection.lean`: exit 0.
- `lake build Aris4Math.ThirtyThree.TwentyThreeSelection`: exit 0, 908 jobs, new module 3.8 seconds; existing dependencies replayed.
- Independent import `ImportAudit.lean`: exit 0. It prints the actual exported types and invokes the two-low branch on an actual `Simple5Hypergraph (Fin 23)`.
- All five audited exports depend only on `propext`, `Classical.choice`, `Quot.sound`.

Commands and logs are adjacent. This is an incremental build and local independent import, not a clean remote rebuild or external human reproduction.

## Next work

The general ten-point colored-graph lemma is being connected to actual common-unit seven-degree neighbors in `TwentyThreeColoredSelection.lean`. The parent agent owns the arbitrary-lock actual trace recovery, local complete classification and final probability callers. Thus none of the selection results alone is a full 23-point Property-B theorem.

Cross-family review is coordinated by the parent agent. This implementation record does not claim a Grok/Gemini approval. Same-family conclusions remain provisional independently of kernel validation.

## Completed colored selection connection

`TwentyThreeColoredSelection.lean` now proves the ten-point colored graph theorem by closed-set counting, then applies it to the actual hypergraph:

1. A degree-six/degree-seven pair of codegree at least two leaves at least ten actual seven-degree common unit neighbors. The two occupied bad-neighbor slots are explicitly removed before the union bound.
2. On those ten points, the actual unit-codegree relation has minimum degree at least three.
3. Each vertex is colored by its actual unique edge with the high partner y. Five-uniformity and y's exclusion from the ten-point set imply each color class has at most four vertices.
4. The general theorem selects a triangle, or an induced two-edge path with endpoint colors different. The latter difference is converted to a genuine absence of any hyperedge containing y and both endpoints.
5. `exists_locks_low_bad_high_of_count` returns an injective five-lock function with actual degrees `(6,7,7,7,7)`, codegree 01 between two and three, all codegrees except 01/23 equal to one, and the actual forbidden triple whenever 23 is nonunit.

The complete module passed `lake env lean` and explicit `lake build` (909 jobs). All four audited main exports have only the standard three logical axioms. `ColoredImportAudit.lean` checks a direct caller on `Fin 23`; its output is separate from the older selection import audit. There is still no local probability/Property-B theorem in these modules.

## Completed all-unit-low selection

`TwentyThreeDefectSelection.lean` now supplies the other r=1 structural mechanism:

- `energy_update_balance` proves the exact change in both orientations of monochromatic edges when one vertex is recolored.
- `exists_four_part_defect_one` minimizes that finite energy. Each vertex then has at most one same-class bad neighbor, since otherwise all four classes would contain at least two neighbors, contradicting maximum degree six.
- `exists_five_with_degree_le_one` chooses five vertices in a class when there are at least seventeen vertices. The proof uses an abstract finite minimum and pigeonhole counting; it does not compute or enumerate possible graphs.
- `exists_six_locks_low_unit_of_count` applies the partition to actual seven-degree vertices and appends the original six-degree vertex. The output is an injective `Fin 6 → V` with degrees `(7,7,7,7,7,6)`, unit low-high codegrees, and an actual matching of bad pairs among the highs.
- `exists_mixed_five_of_high_three` extends an actual codegree-three high pair to the five-lock `(6,7,7,7,7)` pattern used by its numerical exclusion.

The six-lock matching output by itself permits a bad pair to have codegree greater than two. The complete proof must first eliminate high pairs of codegree at least four and the mixed codegree-three pattern using their separate probability callers; only then may its matching pair budgets be set equal to two. This is a live interface obligation, not a missing structural assumption being silently introduced.

Explicit `lake build Aris4Math.ThirtyThree.TwentyThreeDefectSelection` and `DefectImportAudit.lean` both exited 0. The independent import includes a real Fin 23 caller. All five audited declarations use only `propext`, `Classical.choice`, `Quot.sound`. Logs are `defect-lake-build.log` and `defect-import-audit.log`.

## Completed r=0 high-pair and path extensions

`TwentyThreeHighSelection.lean` implements the first two structural exclusions of the at-least-nineteen-sevens branch:

- `seven_outside_bad_budget` charges an arbitrary finite set's actual codegree excess before counting remaining bad partners. This counts actual original vertices rather than an abstract prescribed degree sequence.
- `exists_four_high_of_three` starts from two actual seven-degree points of codegree three. Charging their two units of mutual excess leaves nine high common-unit neighbors; selecting a unit pair there gives four actual locks with only pair 01 having codegree three.
- `exists_five_high_of_path` starts from three actual high points with codegrees 01=12=2 and 02=1. Their outside bad-neighbor budgets are 5,4,5, leaving at least two further high vertices unit to all three. It returns the actual five-lock path configuration; pair 34 remains unrestricted until the high-pair branches are excluded.

These results do not assume the numerical exclusions already succeeded. Their finite classifications and probability callers remain the parent task's responsibility.

## Remaining structural work after this delivery

At the first delivery, the principal unimplemented selection obligation was the r=0 branch after all high pairs of codegree at least three and all induced P3 configurations have been excluded. This obligation is now completed by the two additional modules documented below. The earlier statement of this gap is superseded by their explicit build and import evidence.

For the r=1 all-unit-low branch, the six-lock matching is proved, but its bad-pair codegrees become exactly two only after the separate high-codegree and mixed λ=3 probability exclusions. Normalizing a matching to canonical labelled pair patterns is a classification task; it is not silently included in the current indexing interfaces.

Final verification of the high-selection module: explicit build exited 0 (911 jobs, new module 2.1 seconds); `HighImportAudit.lean` independently imported it and checked an actual Fin 23 path caller, exit 0. Its three audited exports have only the standard three axioms. All four delivered source modules contain no `sorry`, `admit`, new `axiom`, or `native_decide`.

## Completed r=0 cluster partition and actual large-trace selection

`TwentyThreeClusterMoments.lean` (143 lines) proves the incidence identities for actual finite vertex sets, the three-clique moment contradiction, and existence of an actual edge whose clipped intersection sizes sum to at least four.

- `sum_inter_card` double-counts actual vertex-edge incidences for an arbitrary vertex set.
- `sum_inter_product` double-counts ordered pairs in two arbitrary sets, including overlapping sets and the diagonal. `clique_square_moment` therefore correctly counts the diagonal using degree seven and the off-diagonal using codegree two. `cross_moment` uses the actual cross-clique codegree one.
- The local inequality is written without truncated subtraction: if `a+b+c≤5` and `min(a,2)+min(b,2)+min(c,2)≤3`, then `a²+b²+c²+12(ab+ac+bc)≤13(a+b+c)`. Its finite arithmetic checks only the possible counts within a single five-element edge. It does not enumerate hypergraphs.
- Summing the exact identities contradicts the inequality whenever all three clique sizes lie in `[5,7]` and their total is at least nineteen. `exists_large_clipped_trace` concludes existence of an edge of the original `H` with clipped trace at least four; it does not assume a trace certificate.

`TwentyThreeClusterSelection.lean` (384 lines) completes the actual graph-to-lock connection.

1. The existing generic `TwentyTwoSelection.cluster_relations` is reused. `cluster_eq_of_mem`, `clusters_disjoint`, `clusters_cover`, and the new size-seven bound prove the actual partition into nonempty cliques of size at most seven.
2. When there are at least four cliques and one clique has at least two points, choose two actual points there and one in each of three other actual cliques. If every clique is a singleton, choose five actual points from the original set. `FiveCase H` records an injective `Fin 5 → V`, all degrees seven, pair 01 at most two, and every other pair exactly one.
3. In the remaining case, the actual partition has exactly three cliques: the cover and size bound force at least three, while the preceding case excludes four or more. Its three actual sizes are each between five and seven. These facts feed the moment theorem.
4. `exists_retained_pair` chooses two points from an actual clique while retaining at least the minimum of two and its intersection size with the witness edge. Applying it three times gives six distinct original vertices, with the same actual edge meeting their image at least four times.
5. `SixCase H` records an injective `Fin 6 → V`, all degrees seven, pair codegree two exactly on 01, 23, 45, and codegree one on all other distinct pairs, together with an actual `e∈H.edges` and `|(e∩image locks)|≥4`. `indexed_trace_card` equates this intersection cardinality with the number of lock labels lying in the edge.

The main export is

```lean
TwentyThreeClusterSelection.cluster_selection_of_no_sixes
```

It takes an actual pair-covering hypergraph, twenty-three vertices, thirty-three edges, no six-degree vertices, and the explicit high-codegree / induced-P3 exclusion hypotheses. It derives the at-least-nineteen-sevens count internally and returns `FiveCase H ∨ SixCase H`. The hypotheses are graph conditions established by the earlier probability branches; no desired five- or six-lock tuple is supplied as input.

Explicit `lake build Aris4Math.ThirtyThree.TwentyThreeClusterMoments` exited 0 (910 jobs). Explicit `lake build Aris4Math.ThirtyThree.TwentyThreeClusterSelection` exited 0 (913 jobs). `ClusterImportAudit.lean` independently imports the new module and proves an expanded caller on `Fin 23`, including the index-filter form of the large trace. The audit exited 0; all seven audited exports have only `propext`, `Classical.choice`, and `Quot.sound`. Logs are `moments-lake-build.log`, `cluster-lake-build.log`, and `cluster-import-audit.log`. Both new modules contain no `sorry`, `admit`, new `axiom`, or `native_decide`.

The original mathematical cluster/moment obligation is now closed in Lean. The remaining global work is the actual finite-profile classification, probability/avoided-lock callers, and assembly into `twenty_three_propertyB` and T33. In particular the graph exclusion hypotheses above must be discharged by those probability branches. These structural modules are not a proof of Property B by themselves. Same-family mathematical interpretation remains provisional; kernel checks and the future cross-family review are separate evidence.

## Recovery note after coordinator interruption

At completion of the cluster delivery, the 24-point worker reported that the parent coordinator had stopped with `stream disconnected`. No goal was marked complete or paused by this worker. All six 23-point structure modules above and their local audit files are saved and can be imported by a resumed coordinator. The coordinator's interruption does not alter the scope of the verified structural results or close any probability/assembly obligation. No files outside the assigned 23-point modules and this evidence directory were changed by this worker.

## Continued probability work: actual high-pair branches closed

The coordinator resumed and assigned the r=0 probability callers to this worker. Two genuine `H → PropertyB H` branches are now complete.

`TwentyThreeHighPair.propertyB_of_high_pair` takes an actual `Fin 23` hypergraph with thirty-three edges and two distinct seven-degree vertices of codegree at least four. The degree bounds their codegree above by seven; all four possible pair profiles at positions 5 and 14 pass the exact uncorrected bound in the kernel. The actual four type counts are supplied by the preexisting double-lock realization theorem. This branch does not require pair covering or a large seven-degree set. Explicit build passed (new module 2.5 seconds); `HighPairImportAudit.lean` separately checks the original count form of the Bool coloring conclusion. Its certificate and caller use only the standard three axioms.

`TwentyThreeHighQuad.propertyB_of_pair_at_least_three` covers codegree three as well, assuming actual pair covering and at least nineteen seven-degree vertices. It invokes the previously proved actual common-unit-neighbor selection to produce four distinct seven-degree locks, with pair 01 of codegree three and every other pair unit. Every actual large trace has multiplicity at most one because it contains a unit pair. The six genuine pair inventories then force one of exactly seven labeled high-trace vectors. `data_complete` verifies this full local domain; it does not only check the five isomorphism representatives in the source JSON.

`TwentyThreeHighQuadData.lean` contains the seven exact profiles, positions, and nonnegative two-quota multipliers. `generate_high_quad_data.py` reindexes the five original JSON representatives, reconstructs exact duals with `Fraction`, and saves the source mapping in `HIGH_QUAD_GENERATION.json`. The kernel separately verifies profile validity, each actual-capacity dual inequality and the strict sum of corrected minima; generation and model approval are not trusted proof steps. The data module took 14.853 seconds wall time for its explicit build (13.30 user CPU seconds). The actual caller recovers all type counts, uses the literal total/pure bad-pair quota interface, and returns `PropertyB H`. `HighQuadImportAudit.lean` passes the expanded original coloring caller and five standard-three-axiom checks.

The P3/P3+K2 route is currently being implemented in `TwentyThreeHighPathData`, `TwentyThreeHighPathCatalog`, and `TwentyThreeHighPath`. Its generated local domain has 52+63 labeled inputs, and all exact Python inequalities match the saved numerical witnesses including the corrected final avoided-lock refinement. Kernel data/classification checks and the actual caller are not yet reported as passed in this paragraph; use subsequent logs and updates for their final status.

## r=0 概率形式化继续推进

- `TwentyThreeHighPathData`：全部115个完整标签数据的精确 refined dual 已内核构建通过，544秒模块时间、墙钟9:05；`high-path-data-build.log`。分类与caller仍在接线，不能据此单独宣称诱导路径分支已完成。
- `TwentyThreeHighSixProfiles`：一般实际六锁数值剖面桥接构建通过，导出标准三公理；独立于原25点特殊 `SixLargeProfiles`。
- `TwentyThreeHighSixData`：22个含≥4迹的数值代表全部内核通过，21个bare、1个refined，模块247秒、墙钟4:10；`high-six-data-build.log`。全称完整覆盖与实际caller正在验证。
- 六锁完整覆盖采用实际大迹压缩，见 `SIX_COMPRESSED_COVERAGE.md`。三种匹配自同构规范形只剩10/7/2个可选大迹位，共58个合法输入，覆盖将由Lean证明，不能只把22代表验算称为完整分类。

- `TwentyThreeHighFiveData`随后构建PASS（73个完整标签输入，模块646秒、墙钟10:48.69）；原始JSON的extra=2未用于本分支。
- Catalog核验成本按实际测得的共享55型约537秒调整：P3有两种pair图，完整有限域运行继续，暂设20分钟CPU/30分钟墙钟诊断界；不是整图枚举，没有把在途编译记作通过。

## r=0 局部概率与实际团结构 caller 闭合

`TwentyThreeHighPathCatalog` 已构建PASS（模块1186秒），包含P3/P3+K2的全部52+63标签高迹覆盖、与数值counts对应、全部小迹恢复公式。`TwentyThreeHighPath.lean` 真实输入caller随后独立 `lake env lean` PASS，正式总构建进行中。

`TwentyThreeHighFiveCatalog` PASS（201秒），复用共享55迹域，再以真实共度过滤得到32+41完整标签输入。`TwentyThreeHighFive.propertyB_of_five_case` 正式构建PASS（6.1秒）。

`TwentyThreeHighSixCatalog` PASS（177秒），用真实大迹的三种匹配规范形覆盖58个压缩输入，经明确置换归到22数值代表。`TwentyThreeHighSix.propertyB_of_six_case` 正式构建PASS（4.7秒）。其实际caller证明了每个遗漏大迹重数为0、实际余迹布尔位满足所有点对库存、两次真实标签重排、全部type恢复及原染色结论。

独立 `HighClusterImportAudit.lean` 导入、展开Bool染色结果与7项传递公理审计PASS（`high-cluster-import-audit.log`）；全部仅标准三公理。它是本机构建与独立导入证据，同家族解释审阅保持provisional；不是新增跨家族认可记录。

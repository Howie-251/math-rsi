# 当前 (15,4)=15552：实际源已绑定，648-free 单点覆盖到时未决

旧 source-gap 已解决，同一条记录更新；旧报告/预测原样保存在 [HISTORY_SOURCE_GAP](HISTORY_SOURCE_GAP/)。取到 Zenodo23691325 的实际 literal，一次下载 1311860 字节，实际 15552 点、116316 边，degree14 有 648 点、degree15 有 14904 点。源 D4 继承公开结果，没有重复全源或单根验收 BFS。新图尚未生成。

## 实际度数与被推翻的结构假说

[原文件](source15552.author.adjlist.txt) 是显式 0-based 邻接表，已检查简单、无向；[header 接口](source15552.header.edges) 只规范化同一份 literal。[SOURCE_PROFILE](SOURCE_PROFILE.json) 完整统计 CPU 1.962155108 秒。648 个 free 点各余 1 度；minSatN=12，zero/onefault 原型均为 0，因此不能直接套“满邻点复制”或单饱和 pin 的近星代理。

原事前“192 个独立 81 点纤维、每点五个相邻纤维各 3 邻居”的预测被推翻。连续 81-label bins 并不整体 equitable；block0 的四组外部三邻点与内部 2/3 度只能作为该 bin 的事实，不能外推成真实 192-controller。648 free 集中在 24 个连续 81-bin、每个 27 free，其余 168 bin 无 free。这是标签统计，不是纤维认证；actual controller、affine fibre coordinates 仍未恢复，不改猜为 64×243，也不使用旧 13608/13365 配方。

## 唯一有限构造问题：在实际 free 中选至多 15 个闭 R3 覆盖

[冻结预测](single_vertex_R3_cover/PREDICTION.json) 是：648 个实际 free 中，存在至多 15 个 pin，其旧图闭 R3 并集覆盖全部 15552 点。只用已绑定的实际邻接，不依赖任何纤维标签假说。若命中，保旧边加一点接这些 pin 即可用归纳证明 D4；这次没有命中。

native 一次计算全部 648 个新搜索球，未重复旧图验收。并集覆盖全部 15552 点，每 target 支持 67..185 个候选，稀疏覆盖矩阵共 1496880 非零；准备 CPU 0.028104 秒。只有“全候选并集满”这个必要条件通过，不能将它当成 15-pin 选择存在。

随后只运行一次 648 二元变量、15552 完整覆盖行及 sum(x)≤15 的模型。终态为 HiGHS time-limit、无 incumbent，故是 **UNKNOWN**，不是不可行认证。actual 新图 n/D、普通无序坏对数均空，源 D4 BFS 为 0，没有图导出、IP 重启或更多 pins。

预算必须如实保留：目标 solver≤5 CPU，实际内部 time_limit=4.5/threads=1 的单次调用用了 22.983918811 CPU，整批含编译/准备为 23.953803925 CPU，超出目标。此次只设置内部时间参数，未加进程 CPU 硬限；不能写成预算内完成。调用返回后即停止，没有自动扩时。编译 CPU 0.700006598 秒。

## 准确开放范围与恢复接口

当前实际源有真实余量，保边单点入口未被证明关闭；这个一次有限模型只留下“至多15旧free pins能否覆盖”的明确未决问题。不能因此称一般 15553 点图不存在，也不自动延长 solver。任何后续必须沿保存数据或另有结构理由决定，不能拿错误的 192-fibre 解释继续参数网格。

[完整 R3 缓存](single_vertex_R3_cover/R3_MASKS.bin) 布局：3 个 little-endian uint32 为候选数648、旧点数15552、每球243个uint64；随后每候选一个 uint32 顶点 ID、243 个 uint64 mask。[COVER_CSC.bin](single_vertex_R3_cover/COVER_CSC.bin) 为三个 uint32 行/列/nnz、649 个 int32 column pointers、nnz 个 int32 row IDs。已有球不必重新计算。

证据：[下载记录](DOWNLOAD_RECEIPT.json)、[实际源事实](SOURCE_FACTS.json)、[源 profile](SOURCE_PROFILE.json)、[一次覆盖终态](single_vertex_R3_cover/RESULT.json)、[准备事实](single_vertex_R3_cover/PREPARATION_RESULT.json)、[solver 返回](single_vertex_R3_cover/SOLVER_RESULT.json)、[执行入口](single_vertex_R3_cover/run.py)。独立数学桥接由 [ANALYSIS_PROOF](single_vertex_R3_cover/ANALYSIS_PROOF.md) 给出；它不把 UNKNOWN 变成存在证明。

## Fixed virtual-loop quotient diagnostic

A separate completed diagnostic retains the original graph and the fixed contiguous81-point partition. Adding one virtual self-entry only for each degree14 vertex gives five target controllers with three entries each in every row, and the target-controller signature is constant within every controller. All15552 rows pass. There are192 controllers, 24 of them with27 virtual entries each, 648 total. These entries are relation statistics, not graph edits or ordinary loop degree claims. The earlier ordinary-adjacency failure is retained and does not apply to this different completed relation.

The shared two-source probe costs0.565593974 CPU seconds, recorded once as a shared cost; its per-partition check cost here is0.05999908400000001. It runs no BFS, ball, solver or new graph. It restores an equitable quotient interface; affine line maps and any changed construction still require their own certification. See ../d15_loop_completed_quotient_probe/{PREDICTION.json,RESULT.json,REPORT.md,run.py}.

## Exact affine recipe recovered

The producer then fixed these same local base3 coordinates, fitted Q_v(y)=B*x+c for every directed quotient arc, and compared every actual three-neighbor target set. All960 arcs and77760 rowsets pass. The compact relation table and generator reconstruct the original source exactly, omitting a virtual loop only at equal global source/target labels. This closes the source-recipe interface gap, while leaving the old cover UNKNOWN and all proposed modified graphs undecided. It is not a new graph or diameter verification.

The shared two-source recovery CPU is0.803465985 seconds, not two separate full costs; this source receipt is0.09822721899999999. Zero graph export, BFS, ball or solver runs occurred. See ../d15_loop_completed_quotient_probe/affine_relation_recovery/{RESULT.json,REPORT.md,generator.py,ANALYSIS_AFFINE_CERTIFICATE.md} and source15552_AFFINE_RELATIONS.json.

## Terminal canonical port coverage frame

The fixed zero/selfline probes and the two canonical cover models are now terminal. Zero union misses528; all42504 five-triangle choices fail. The inversion-restricted48-atom model returns raw UNSAT. The independent72-pin model first returns UNKNOWN at3 CPU seconds; one unchanged-CNF budget reassessment returnsUNSAT_RESTRICTED_CANONICAL_INDEPENDENT_MODEL with solver CPU5.952845999999999. No independent UNSAT proof was checked. No candidate, source modification, new ball, BFS or graph occurred. The all648-free-pin historical model remains UNKNOWN and is not renewed.

See ../d15_loop_completed_quotient_probe/PORT_COVER_REPORT.md for all exact domains, counts, shared CPU receipts and links. This is a set of variants of the same source/mechanism record, not new independent methods. No third timer, shifted triangle or additional port family is launched.

## Complete free-space direction domain

Everyself-controller now has an actual3-dimensional27-point free fixedspace, with13 projective directions. All648 free labels exactly match; the full inversion domain has336 disjoint cost1/2 atoms. The target quotient has7872 inversion orbits, with7584 exact distinct support clauses; it represents all15552 targets, not a sample. The one scheduled call returns raw UNSAT/code20 in35.16384300000001 solver CPU seconds. The shared complete batch costs73.957748614 CPU seconds, including the0.063390872 interface receipt, and has no pending source or candidate. No independent UNSAT proof was checked.

The fixed-word prediction at equalcost3 is genuinely supported: 27 old-direction endpoints versus81 new-direction endpoints in one final fiber. That local success is distinct from joint graph coverage. The result excludes no general non-invariant free-pin domain. See ../d15_loop_completed_quotient_probe/full_free_directions/{REPORT.md,ROUTE_COSSET_REPORT.md,ANALYSIS_DIRECTION_COVER.md} and ../d15_loop_completed_quotient_probe/full_inversion_port_cover/RESULT.json.

## Full independent pins and affine-line certificate: final scope

The complete actual-free independent-pin SAT uses648 selectors and all15552 targets, with15552 exact support rows and sum<=15. No target inversion folding is used. Lex chooses between S and -S; a separate final-prefix cut skips the invariant domain only by inheriting the prior uncertified full-inversion UNSAT result. Its one60-second call returns UNKNOWN/code0, solver CPU59.902466999999994. The two-source batch is127.968020737 aggregate CPU under160, with no unattempted source or candidate. The unrestricted append question remains OPEN, and no timer continuation is launched.

The parallel sufficient certificate uses2808 affine3lines, reduced exactly to312 full-target-fiber masks. Its single call returns raw UNSAT in0.5527359999999999 solver CPU seconds. The shared certificate batch is3.85650486 CPU seconds. Failure excludes no combination that fills a target fiber jointly from several partial line unions, and no general free-pin cover. All source edges/caches were retained, with zero new balls/BFS/graphs.

See ../d15_loop_completed_quotient_probe/full_independent_port_cover/{REPORT.md,MODEL_SCOPE.md,RESULT.json,ANALYSIS_LEX_SCOPE.md} and ../d15_loop_completed_quotient_probe/affine_line_block_cover/{REPORT.md,RESULT.json,ANALYSIS_LINE_CERTIFICATE.md}. These are variants of this same source record; no method or row is added.

## Complete joint affine-line family

The old stored full-block columns are equal for all nine parallel cosets, but this does not imply equal point columns. A fixed two-line cache probe finds1062 differing old targets; within one target fiber the two unions have sizes39/39, intersection12 and union66. These are cached coverage-column counts, not graph bad pairs. Their original fixed PREDICTION/RESULT are preserved.

The joint CEG model therefore retains all2808 raw affine lines, including partial-block gains, with at most five selected lines and no prior-negative cut or lex restriction. Its initial1728 necessary point rows already return raw UNSAT/code20 in11.707798 solver CPU seconds. No SAT candidate exists, so zero full-point candidate OR checks and zero new CEX cuts were performed. The complete two-source batch costs25.794664232 aggregate CPU seconds under130. This computational negative covers the full at-most-five-line domain on this source, without an independently checked proof; general fifteen-pin coverage remains UNKNOWN. No graph, new ball or source BFS occurred.

See ../d15_loop_completed_quotient_probe/affine_line_joint_cover/{REPORT.md,MODEL_SCOPE.md,RESULT.json,ANALYSIS_JOINT_CEG.md}, and ../d15_loop_completed_quotient_probe/affine_line_block_cover/{OFFSET_DIAGNOSTIC_REPORT.md,POINT_COLUMN_OFFSET_REPORT.md}. No continuation, new direction or offset is started.

## Signed-frame binary transfer: source prerequisite fails

A separate source-aware proposal would identify the fibers with F3^5/<ones>, carry common-sign permutation arcs to F2^5/<ones>, and give hypothetical192*16=3072 points of maximumdegree10. Its integer-range endpoint argument is valid conditionally. The actual controller0 kernel directions are not a projective5-frame: u2=u1+u4, so subset[0,1,2,4] has rank3. No invertible basis change removes this dependence. The gate inspects five rank3 maps (one-dimensional kernels) and two four-subsets, stopping after0.003352509 CPU seconds. It performs no signed-arc check, binary recipe, graph, BFS or solver.

This is a failed sufficient-source prerequisite, not an actual3072 graph or a negative theorem for general(10,4). The older general singleappend UNKNOWN remains. See ../d15_loop_completed_quotient_probe/signed5_frame_gate/{PREDICTION.json,RESULT.json,REPORT.md,ANALYSIS_TRANSFER_PROOF.md}. No alternate frame, basis or field is tried.

## Intrinsic36-point induced graph: actual D4 failure

The separate original-F3 rule passes all192 rank4/support3 matroid checks and selects36 intrinsic old points per controller,6912 in total. Its unique actual induced graph has6912 vertices,22896 edges and degree1..11, so the intended maximum13 gate passes. This is one actual failed target graph, unlike the earlier source-only gates and cover models, which generated none.

The first new-graph root0 (source label1) has shells[1,6,35,208,1046], R4=1296, missing5616; first missing is new4/source9. One root suffices to refute D4, so no further roots are needed for that negative conclusion. Exact global diameter, connectivity and ordinary unordered bad pairs remain null. A simple explanation from the already computed degrees is R4<=1+6*(1+10+100+1000)=6667<6912 at this root, even before the sharper actual1296 count.

The profile costs0.071742091 CPU; production including compile and generation costs0.585443188, combined0.657185279. Source BFS is zero, new-graph BFS roots one, alternatives/edge changes zero. The actual source's D4 cannot be inherited by this induced graph. The original general singleappend UNKNOWN remains open. See ../d15_loop_completed_quotient_probe/matroid36_induced_subset/{REPORT.md,ANALYSIS_SET_DEGREE.md,production6912/REPORT.md,production6912/RESULT.json}; full failed edges and sorted new-to-old labels are saved. No subset repair or further field experiment is launched.

## Rank-one reflection quotient gate and stronger degree obstruction

The local support3 matroid has exactly two controller-fixed rank-one reflections preserving all five kernel lines. Testing every choice pair on all960 arcs gives3840 tests,3648 forbidden pairs and1812 distinct2SAT clauses; the instance is UNSAT with saved opposite-literal implication paths. Its complete gate CPU is0.445824661, with no orbit map, graph, source BFS or external solver. The conditional10368/max14/D4 quotient proof is valid, but its Aut premise fails.

A stronger paper consequence uses only saved arc5, from nonloop controller1 to4, where all four state pairs are forbidden. In a true quotient without Aut, the neighbors of both source representatives must be unioned. At a nonfixed source class, the minus-input channel contributes2 or3 classes; the other four contribute3,4 or6. Degree<=14 forces precisely the same arc compatibility at every nonloop controller. The nonfixed points span the vector space, so the linear equality holds everywhere. The literal zero-allowed arc therefore excludes maximum14 for every partition from this same two-choice reflection family, even without assuming Aut. No new matrix, graph, degree-CSP or solver was run for this strengthening.

The hypothetical10368 order is not an actual graph; other partition/involution types and general(14,4) remain unaddressed. The old general singleappend UNKNOWN is unchanged. See ../d15_loop_completed_quotient_probe/rank1_reflection_quotient/{RESULT.json,REPORT.md,ANALYSIS_QUOTIENT_PROOF.md,ANALYSIS_DEGREE_NECESSITY.md,NONLOOP_ZERO_ALLOWED_ARC.json}. No further fold class is opened.

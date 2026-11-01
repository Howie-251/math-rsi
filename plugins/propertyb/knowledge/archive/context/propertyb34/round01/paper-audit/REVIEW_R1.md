# T34 paper candidate: fresh review R1

2026-10-13. Reviewer: `/root/t34_paper_proofcheck_r1`.
`review_independence: same-family`; `acceptance_status: provisional`.

本轮完整阅读纸面候选各数学分支后，**未发现会使原命题证明链失效的数学问题**。原始任意有限简单五元超图的约化、21–25 点的实际选点、残型的全局排除、共享实际坏对向量的布局论证、25 点隔离补点调用均能按正文解除前提。发现一项 MINOR：加权 overlap 引理的“已被当前四低表使用”描述与现存最终表不符；该引理本身正确，这项描述不影响主证明。

本轮结论是对所读**纸面数学链及指定精确复算范围**的有限判断。大型局部表没有在本轮全部重新生成、全部逐证书重跑。未执行 Lean，未审计最终 Main 的实际导出类型或传递公理，未做跨家族终审，因此本报告不是完整 T34 Goal 或端到端 Lean 的验收。

## 问题

### R1-01：weighted overlap 的实际依赖描述已过时

- **status:** UNCLEAR
- **impact:** COSMETIC
- **category:** REFERENCE_MISMATCH
- **severity:** MINOR
- **location:** `middle-math/WEIGHTED_OVERLAP_QUOTA.md:3–5`；地图与义务账本中相应的独立 formal obligation 说明。
- **statement:** 该引理已用于选定的 22 点四低纸面证书。
- **why_invalid:** 本轮实际读取的 `FOUR_LOW_22.json` 有 169 项，169 项 `final_bound<1`；其中 167 项直接界、2 项普通 `joint`，没有 `overlap` 字段，全部保留 quota 的 `kind` 均为空。对本目录所有 JSON 检索也未找到 `"kind": "overlap"`。因而该句不能作为当前最终证书依赖的准确定位。这里不否定一般引理，也不否定某段历史计算曾尝试它。
- **counterexample:** 无数学反例；现存最终数据是依赖描述不吻合的直接证据。
- **affects:** 仅依赖导航和下一步 Lean 工作范围；不破坏任何已读严格界或实际 H 调用。
- **minimal_fix:** 将首段改为“可用的独立加强，目前保留的四低最终表仅需普通 quota”，并从必需 formal obligation 中移除它，或给出真实使用它的最终证书路径。一般推导可以保留。

零 FATAL、零 CRITICAL、零 MAJOR。没有为未运行全部算术或未完成 Lean 另外制造数学缺口。

## 原始命题与假设解除

`Target34` 是任意有限顶点型上简单五元边集、边数至多 34 推出原 Bool 二染色；无点对覆盖、固定点数、低度点或证书前提。`Reduction.lean` 的最少点反例可将未覆盖点对合并；若存在未覆盖点对，得到点数更少且仍非 B 的简单五元超图。点对覆盖给 `4d(x)≥v−1`；当 `v≥26` 时每度至少 7，从而总度至少 182，与 `5|E|≤170` 矛盾。17/18 点平衡事件具有一个实际非空交叠，把弱界 1 严格化；其余小点数接旧通用结论。点数足够后将边集扩为恰 34 条，非可染性及点对覆盖保持。不存在把 padding 后的性质错误反推到原输入的问题。

19 点实际选择、单/双/三锁调用已在本轮读到源码；三锁覆盖是 17 个有标签输入，实际全部迹重数由恒等式恢复。20 点读完五/六度、七度的三分流、八度及其较短替代论证。已完成形式化的这些分支只作为现成依赖使用，本轮没有重新编译或把其历史日志冒充新结果。

| 内部输入 | 实际选点和覆盖核对 | 结论接口 |
|---|---|---|
| 21，最小度 5/6/7/8 | 总度 170 排除其他最小度；5 度点的单位 partition、多个 6 度点、唯一 6 度点的七度数量分流，以及七度数量 1/2/≥3 均完整。各种 U 的下界由扣除实际 excess 得到。 | 每个严格局部证书都作用于同一个实际 H；若全部投影非严格，正文的 incidence 或图矛盾有效。 |
| 22，六度点数 0/1/2/≥3 | `2r+t≥6`；每个六度点 excess=3。r=1/2 的额外七度/八度点由精确度总和或剩余 excess 强制；r=0 至少六个七度点。 | 四锁、promotion、全部旧尺寸投影过滤只丢弃已经给出实际染色的输入。 |
| 23，无六度点 | 七度点数 r≥14；最小六点权重集满足 `(r−7)d_S(x)+2W≤30`、W≤6。最大内部度 3 时 W≤4；其余残图仅五类。 | W=6 强制 r=14、两个 K7 和外部九个八度点；W=2/3/4 由同一个实际第七点进入表。 |
| 23，六度点数 1/2 | `t+2r≥14`，common-unit 七度点分别至少 10/6；强七度共度分流不要求全图最小度七。 | r=1 的五点残图使全局非单位图为至多三个、各至多三点的团，矛盾；r=2 的实际五个额外七度点进入严格终表。 |
| 23，六度点数 3 | 外部七/八度点至少 14、七度点至少 8；扣去至多六个 exceptional neighbors 后 U≥8 且七度点至少二。 | 选定含两个七度点的四个实际 U 点，排序不改变角色；含八度点的终分支由严格投影排除。 |
| 23，六度点数 4/5/≥6 | 四低公共单位七/八度点数分别至少 5/3。每个四低子集可选高点，故“所有低低单位”可提升到全部五低。≥6 分支完整 promotion 到六低，七低残域为空，恰六低有七/八度追加点。 | r=4 的每三高恰一七度导致 `3k=4`；r=5 追加实际第五低不强加其低高单位；六低后追加点的总 excess≤1 由 12 对至少十点的预算给出。 |
| 24，六度点数 0/5/6/≥7 | 无低的两种度序、五个单位七度点及第六点的 ≤1 excess 均成立。五低非单位支、全单位支、六低两个高的残型和三高反证逐项可用。 | 五低全单位支调用的是无全局 pair-covering 前提的九锁条件引理，而非直接将 25 点 pair-covering 定理用于补孤立点后的对象。 |
| 24，六度点数 1–4 | 七度加权图三类极小划分给各类内部权重度≤1；每低至少可加入两类，所以某类≥8。选中的非单位 matching 不跨度数角色。 | 保留实际第八低；七锁先降度再检查空迹非负。八锁删除投影重新合并全部迹计数；余 222 型直接或 joint 严格。 |
| 25，全部度序 | r≥5、t≥30−2r；七度非单位图最大度≤4，所以 r=5/6/7 可取四单位七度配五低。r=8、r≥9 分别到 q=8/9。 | q=8 剩型有实际第十七度点单位于旧高；q=9 根据 r=9 或 r≥10 追加七度/六度点；全部原边仍在 conditional probability 空间内。 |

## 新概率接口、计数与依赖

1. **固定对象与概率模式。** P1 的贪心失败确实给单交有序 critical pair；P2–P4 是固定锁位置后对自由点作无放回注入。自由中心没有多余的 `r_T r_U` 因子。不可行 demand 先归零，不形成 0/0。`P(Fail)<1` 在非空有限排列空间上给实际成功排列，随后是原始两色染色。
2. **真实坏对扣除。** 无序槽容量是同型 `choose(n_T,2)` 或异型 `n_T n_U`；损失为两个有序方向的权重和。已经因共享其他锁而权重为零的槽仍按其真实零权重处理。total/pure 是嵌套 quota，先扣 pure 再扣剩余 total；没有重复扣同一坏对。
3. **共享布局弱对偶。** 固定实际 H 和实际 z 后，`γ_l min(a,c−wz)≤(γ_l−β_il)a+β_il(c−wz)` 使用 `0≤β≤γ`。`W≥d−κ`、`z≥0`、quota 下界、容量上界给正确方向的 capacity penalty。有限平均 `<1` 只推出某布局自身的界 `<1`，没有声称不同条件空间的概率相等，没有 max/min 交换或强对偶依赖。
4. **weighted overlap。** `Σ choose(d_a,2)≥4n−M` 不要求 cover 宇宙；不同四元 link 的交至多 3 来自简单性。实际 trace 的交集由已锁部分加至多 `min(f_T,f_U)` 个自由点组成，故正文 h 正确。其加权 quota 进入同一弱对偶时只改变 demand 系数。当前保留表是否实际需要它见 R1-01。
5. **24 点唯一低坏对。** 此结论确实使用 pair covering：六度时 excess=1，所以只一个 λ=2，交叠总量为 1，从而只有一个坏无序边对；避锁 quota 为正时约束的是这一同一实际坏对。检查了无 pair-covering 的条件八锁/九锁引理：它们实际需要的通用 total/pure quota 不要求此唯一性；八锁最后 joint 输入的度数全为七，未把唯一低坏对假设越界使用。
6. **目录和重标号。** 第一未覆盖点对递归有严格下降预算及跟随任意实际剩余迹的路径。promotion 变量满足逐旧迹容量，旧五点迹禁止 promotion；singleton/empty 由新度和旧总边数恢复。投影对同像迹加重数。只按实际全置换或保持度数角色的置换取商，位置随标签运输；incidence invariant 只缩小待检查的 bijection 集合。
7. **依赖无环。** 25 点的 q=5 表先有独立单位锁分类和一般概率证明，再导出无覆盖假设的九锁条件引理，再供 24 点五低分支调用；25 点的选择和 q=8/9 扩张没有反过来使用该 24 点结论。21/22/23 的较小严格投影不依赖尚未证明的整支 theorem。旧 T32/T33 数值没有未经 34 边重算直接移用。
8. **渐近及交换。** 没有 O/o/Θ 或极限、导数、无限积分的主张；F 不适用。仅有限求和重排、精确整数计数、有限最小值存在性和有限平均，因此无隐藏的可积性或一致收敛假设。

## 反例尝试与本轮实际执行

以下结果来自本 reviewer 的本轮只读调用；未调用求解 LP，未写回作者数据。

| 针对问题 | 尝试与结果 |
|---|---|
| 21 点“每四点是 K4/claw/C4/empty”是否遗漏其他全局图 | 独立穷举 5 点全部 1,024 图、6 点全部 32,768 图；满足条件者分别 17/33 个，全为完全图或完全二部图。结合正文一般证明，没有发现反例。 |
| 23 点第七点向量表是否过度筛除 | 从正文交换式、T 的整数界及残图条件独立枚举每类 `3^6` 向量，四行分别得到 4/1/3/7 个，逐项与正文完全相同。未假设六点投影仍为同一个最小化集合。 |
| weighted h 在重叠大、共享锁或自由部分很小时是否失效 | 对 7 点 link 宇宙的全部 35 个四子集之不同对、全部 128 个锁集合，共 76,160 例检查实际交集≤h；全部成立。一般证明仍是上节集合计数，不以此有限测试代替。 |
| 24 点先升为七度是否漏实际 mixed 输入 | 只读重新运行四个六锁 raw 生成，raw=valid 为 352/467/611/787；重新沿 promotion 及降度处理，4,912 次中有 56 次临时负 empty。得到 207 个被救回的实际轨道，全部同时在最终 catalogue 和 bound 表中。没有采用错误的提前非负过滤。 |
| 共享布局精确证书是否掩盖浮点残差/错容量 | 重新执行 middle 的 11 份 joint+2 份 avoided（22 点十三残型）；另重放 23 点最后七锁 joint `904545552/910000091`，24 点最后两 mixed joint 及全七度八锁 joint。17 份总计全部通过保存有理数的注入 ABC、quota、两方向权重、容量及 repaired penalty 重算。 |
| 25 点最紧界或第十锁是否依赖仅近似严格 | 重新核对 q=5/8/9 各最大严格九锁见证，分别 `12869/12870`、`2285/2288`、`1429/1430`；完整重放 q=8/9 的全部 45 个第十锁 orbit 见证，均严格，最大 `2056/2145`。 |
| 21 点单位边唯一性是否偷换 common/exact trace | 在 unique-six 等式支、two-seven 两 matching 支、八度 claw/C4 支逐项反向构造；同一单位 pair 确实强制实际边相等，而仅 λ=2 的 pair 没有被误作唯一。没有得到反例。 |
| 23 点 W=6 是否允许其他极值图 | 尝试带权 2-edge、6-cycle、三 matching 等六点形状：每个外点须有三单位 S 邻居，并由交换迫使它们为三角形；各选点四个 cut 邻居迫使 2K3，再次交换迫使两个 K7。所用九个外部八度点来自 r=14 和总度 170，没有额外正则性假设。 |
| 24/25 无 cover 条件引理是否错误调用低点唯一坏对 | 检查 isolated padding 以及非覆盖低中心可有多个坏对这一反例方向；九锁只用普适 total/pure，八锁混合变体由 direct 表覆盖，故该反例方向没有击中实际调用。 |

主代理随后给出的 `middle-math/NEW23_CERTIFICATES_VERIFIED.json` 也已读取其范围记录：13 个完整来源，1,382 pure 和 153 joint 算术/实际 profile 绑定；这是别的执行者的算术运行记录，不计入上述本 reviewer 重新执行的数量，也不是审阅意见。

## 实际读取范围

完整读取的数学源（以下路径均从项目根解析；不含巨大 JSON 全文）：

- `FORMAL_SPEC_PROPERTYB_34.md`、`context/propertyb34/round01/PAPER_CANDIDATE_MAP.md`、该目录 `paper-audit/PROOF_SKELETON.md`、`proofs/PROBABILITY_LEMMAS.md`。
- `formal/Aris4Math/ThirtyFour/Target.lean`、`Reduction.lean`、`SmallVertices.lean`、`Assembly.lean`、`Nineteen.lean`、`NineteenSelection.lean`、`NineteenSingle.lean`、`NineteenPairs.lean`、`NineteenTriples.lean`。
- `context/propertyb34-hour1-20261013/low-math/` 的 `LOW_DEGREE_SIX.md`、`SEVEN_ONE.md`、`SEVEN_TWO.md`、`SEVEN_MANY.md`、`EIGHT.md`、`TWENTYONE_FIVE_COMPLETE.md`、`TWENTYONE_SIX_REDUCTION.md`；本轮 `twenty-lean/EIGHT_SIMPLIFICATION.md`。
- 本轮 `twentyone-math/` 的 `COMPLETE_TWENTYONE.md`、`SIX_UNIT_SET_LEMMA.md`、`MULTIPLE_SIX.md`、`UNIQUE_SIX_NO_SEVEN.md`、`SIX_WITH_SEVENS.md`、`AT_LEAST_THREE_SEVENS.md`、`TWO_SEVENS.md`、`UNIQUE_SEVEN.md`、`EIGHT.md`。
- 本轮 `middle-math/` 的 `COMPLETE_TWENTYTWO.md`、`CANDIDATE_TWENTYTWO_SEVEN.md`、`WEIGHTED_OVERLAP_QUOTA.md`、`CANDIDATE_LOW_BRANCHES.md`、`CANDIDATE_ONE_TWO_LOW_23.md`、`CANDIDATE_FOUR_FIVE_LOW_23.md`。
- 本轮 `twentythree-seven-math/N23_MIN_SEVEN.md`、`SELECTION.md` 和 `high-math/CANDIDATE_THREE_LOW_23.md`。
- 本轮 `high-math/` 的 `CANDIDATE_TWENTYFOUR_COMPLETE.md`、`EIGHT_MATCHING_SELECTION.md`、`CANDIDATE_EIGHT_SEVEN_MATCHING.md`、`CANDIDATE_FIVE_LOW_FULL.md`、`CANDIDATE_FIVE_LOW_NONUNIT.md`、`CANDIDATE_SIX_LOW.md`、`CANDIDATE_SEVEN_LOW.md`、`CANDIDATE_TWENTYFIVE.md`、`NINE_LOCK_UNIVERSAL_LEMMA.md`、`CANDIDATE_25_MANY_LOW.md`；第一小时 high-math 的 `CANDIDATE_NO_SIX.md`、`CANDIDATE_MANY_LOW.md`，以及 `context/propertyb34-hour1-20261013/MIDDLE_PROGRESS.md` 的完整强共度阈值和 22 点残图覆盖推导。

针对具体疑问读取的代码包括：`joint_layout_lp.py`、`weighted_overlap_lp.py`、`verify_joint_layout.py`、`four_low.py`、`low_coverage_audit.py`、`few_low23.py`、`extend_low.py`、`extend_mixed22.py`、`joint_unit_layout.py`、`joint_mixed_layout.py`、high-math 的 `verify_joint.py`、`seven_matching.py`、`seven_matching_screen.py`、`complete_eight_matching.py`、`eighth_matching.py`、`unit_catalogue.py`、`v25_nine_catalogue.py`、`v25_tenth_catalogue.py`、`subset_position_dp.py`、`audit_seven_temporary_negative.py`、23 七度目录的 `seven_selected.py`、第一小时 `mixed_six.py`，以及通用 `pure_quota.py`、`independent_structure_bounds.py`。具体读取/复算的数据范围在上表列明。

未打开既有 reviewer 文档或 `PROOF_AUDIT`。第一小时 `nineteen/REPORT.md` 用于找已完成 formal 来源，其末尾连带包含一段旧静态审阅范围概述；本轮未将该概述作为数学证据，19/20 点判断依据实际源文件。没有读取或写入 `aris4math_v2`。

## 未实跑范围与有限结论

本轮没有重跑所有 21/22/23 局部表、24 点 16,006 个七锁界/22,837 个八锁轨道，或25 点全部 11,692 个 q=5 界；没有对所有 catalogue 使用第二套独立生成器。已逐支阅读生成的数学覆盖证明，并针对最易漏输入的 promotion、重标号、临时负 empty 和最终狭窄严格界作了代码检查/精确重放。这一范围不等于他机重现或全部独立算术复现。

在该范围内，可读证明的逻辑、假设、概率方向和整体分支覆盖是连贯的，没有发现反例或新增实质缺口。建议按现有数学链推进 actual-H 的端到端 Lean 和最终指定审阅；无需因本轮审阅重新设计已成立的选点与布局机制。R1-01 仅需修正依赖文字。

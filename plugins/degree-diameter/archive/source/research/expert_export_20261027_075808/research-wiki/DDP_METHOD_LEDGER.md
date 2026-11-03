# 已尝试构造与目标差距

更新：2026-10-27 07:58:08 UTC。本Goal已验证新下界仍为0。

本账本覆盖当前 Degree/Diameter Portfolio；旧 D2/DD82 实验保留在原节点，仅作为暂停历史。每条是实验、变体或工具/来源记录，不等于一种独立方法。

先读本页说明和家族目录，再按机制、参数检索对应条目；不必把整页反复装入上下文。完整字段在 [机器账本](DDP_METHOD_LEDGER.json)，每项链接到独立实验节点和原始证据。

## 怎样读“距离”

- n超过基线但直径不达标，仍不是新下界；基线均标保存日期，正式纪录前重新核对公开来源。
- 控制器、条件性大图、完整候选、部分状态和已知源分层记录。控制器阶数不能直接与最终图基线相减。
- 普通无序坏对、NB有序缺项、代表状态缺项、容量不足分列；原文未标单位时保留“待核”，不猜成无序数。
- 无图、UNKNOWN、局部满秩不填作目标图的实际直径；仅两新根BFS会明确写核验范围。
- 默认不追加已停止批次的seed/预算；重启需改变已记录覆盖瓶颈或获得明确新条件，不把局部最小称全族排除。

## 从失败中保留的启发

唯一短路/端点容量不足无法靠同一模板的标量调参补救；应先改变路线重数、内部边或生成结构。局部路由满秩仍需全局控制点覆盖；不同chart的pencil修补不能混用。

方向类等不变量可在大图搜索前排除整族。加边能保留旧近端覆盖，但远端所有类别仍要核对；匹配路径可能用两条新边。R4/R3双点互助是不同于旧单点的覆盖条件。

旧报告中的“8”指8个起始方案，旧单点已用满11/12邻居；不是发现一个尚未用满的度数预算。

## 家族目录

- [A7 three-orbit / cell-design graphs](#family-1)
- [H9 partial fold with later pencil augmentation](#family-2)
- [H9 partial-fold split/copy/twin geometry](#family-3)
- [HS branch affine lifts](#family-4)
- [Heisenberg central-extension Cayley](#family-5)
- [bi-orbit Cayley/voltage constructions](#family-6)
- [branched binary covers](#family-7)
- [cooperative multi-vertex extension](#family-8)
- [degree-plus-one matching shortcuts](#family-9)
- [edge subdivision / cooperative vertex insertion](#family-10)
- [edge-local binary affine line lift](#family-11)
- [fixed-controller affine line relations](#family-12)
- [four-label affine route-chart lifts](#family-13)
- [generalized-quadrangle incidence with internal 2-factors](#family-14)
- [idea:ddp-affine-cayley-d3](#family-15)
- [idea:ddp-bicayley-d3](#family-16)
- [idea:ddp-bicayley220-one-reflection](#family-17)
- [idea:ddp-breadth-20261027](#family-18)
- [idea:ddp-m1-two-orbit-voltage](#family-19)
- [idea:ddp-m2-hierarchical-cover](#family-20)
- [idea:ddp-m3-affine-line-cover](#family-21)
- [idea:ddp-matching-augmentation](#family-22)
- [idea:ddp-open-parameter-construction-20261026](#family-23)
- [idea:ddp-polarity585-complete-replication](#family-24)
- [incidence-design layered linker graphs](#family-25)
- [linear-code syndrome/coset quotient](#family-26)
- [metacyclic base voltage constructions](#family-27)
- [multi-vertex extension with spoke cooperation](#family-28)
- [ordinary cyclic voltage covers](#family-29)
- [plain tensor products](#family-30)
- [pure Cayley low-degree D3](#family-31)
- [record-graph monotone vertex extension](#family-32)
- [shift/toggle Cayley](#family-33)
- [signed/branched double covers](#family-34)
- [source-edge deletion and vertex insertion](#family-35)
- [spanning edge-deletion degree reduction](#family-36)
- [state-shift / de Bruijn graphs](#family-37)
- [uniform graph products](#family-38)
- [vertex splitting and matching](#family-39)

<a id="family-1"></a>
## A7 three-orbit / cell-design graphs

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Rajiv252三轨道原规则来源恢复](experiments/ddp-wave6-record252-mechanism-scout.md) | (5,4)；L=252 | 原生成元附件未取得，未找新参数；后由wave7组合坐标完整恢复。 | 原文A7及42/105/105轨道配额；缺ZIP原置换数组；已由组合规则绕开附件，不重试下载。；[原始证据](../research/ddp/breadth_20261027_wave6/record252_mechanism_scout/REPORT.md) |
| [Rajiv252七胞元完整组合坐标恢复](experiments/ddp-wave7-rajiv252-cell-structure.md) | (5,4)；L=252 | 42+105+105点、630边按组合规则逐边重建完全相等。 | 从旧252边表恢复七K6胞元、35B三角形及pentad/syntheme坐标；不是新record；后续须改变模板的远端覆盖条件，不能只加第八胞元。；[原始证据](../research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/REPORT.md) |

<a id="family-2"></a>
## H9 partial fold with later pencil augmentation

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Dhar后续pencil资料：当前37628/42342原图已得](experiments/ddp-wave4-pencil-source.md) | (12,5)；L=42342 | 原图已得，pencil生成邻接、witness及D证明未恢复。 | Zenodo23653049及主表实际href原始图；不猜作者未公开性；需明确原始规则后才能以pencil做生成，不继续泛搜。；[原始证据](../research/ddp/breadth_20261027_wave4/pencil_source/SOURCE_NOTES.md) |

<a id="family-3"></a>
## H9 partial-fold split/copy/twin geometry

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [H9任意split/copy/twin定理与逐点witness恢复](experiments/ddp-wave3-hexagon-partial-fold-scout.md) | (12,5)；L=42342 | V/E与degree公式恢复；原witness S7959+copies280+twins63=41699，非新record。 | 原H9/duality与部分折叠作者资料；已有41699成品的局部结构恢复；已有逐点Q数据足够解除轨道常值约束，无需换群。；[原始证据](../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/THEOREM_SCOPE_REVIEW.md) |
| [H9逐点解除orbit常值：四序greedy与单调闭包](experiments/ddp-wave3-hexagon-partial-fold-greedy.md) | (12,5)；L=42342；条件性n=42343（未据此计纪录） | 四序新增0；root强迫闭包禁全部25074 merged，故该指定单调cone任何真S超集不可能。 | 原S固定为子集、H3 copies固定280；任意重染也包含在root后续闭包排除内；必须做结构交换，不再加批量split或重染。；[原始证据](../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_greedy/REPORT.md) |
| [H9四预定region联合S/c/copies MILP](experiments/ddp-wave3-hexagon-partial-fold-joint.md) | (12,5)；L=42342；条件性n=42343（未据此计纪录） | 四区均Optimal gap0，gain0；best核心41636且state未变。 | 四预定region、域外固定，freegeneric820/820/899/901；copy变量1/1/28/28；不扩大旧区域；须新的全局结构步骤。；[原始证据](../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_joint/REPORT.md) |
| [H9全局三态三起点固定单点退火](experiments/ddp-wave4-global-partial-fold.md) | (12,5)；L=42342；条件性n=42343（未据此计纪录） | 最好合法核心38383/S4986；另两终态1068/1124实际点度13，不能当Δ12图。 | 全部33033generic自由三态，copies固定0；三starts各50CPU秒；本单点惩罚profile停止，需结构变化非追加时限。；[原始证据](../research/ddp/breadth_20261027_wave4/global_partial_fold/REPORT.md) |
| [H9单锚点equitable全局cell MILP](experiments/ddp-wave4-equitable-global.md) | (12,5)；L=42342；条件性n=42343（未据此计纪录） | 一次MILP无incumbent，UNKNOWN；未生成大图。 | 一个几何绝对点anchor，650genericcells/12H3cells，全部cell常值；无固定域外；须新的结构/单独授权有限profile，不能写全逐fiber排除。；[原始证据](../research/ddp/breadth_20261027_wave4/equitable_global/REPORT.md) |

<a id="family-4"></a>
## HS branch affine lifts

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [HS50×C17固定非均匀分支template](experiments/ddp-wave5-hs850-branch-lift.md) | (12,3)；L=810；条件性n=850（未据此计纪录） | 非邻fiber≤3端点至多12<17，指定整个template不可能D3。 | 固定branch位置和大小(4,2,2,1,1)，六参数及同位置同大小常数替换；必须改变非邻fiber容量；不能继续六参数赋值。；[原始证据](../research/ddp/breadth_20261027_wave5/hs850_branch_lift/REPORT.md) |
| [HS850十轨道26参数结构放宽](experiments/ddp-wave5-hs850-orbit10-relaxation.md) | (12,3)；L=810；candidate_graph_or_family n=850；条件性n=850（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=26180；saved_explicit_graph；最佳850图D4、26180个>3无序对；有限批次失败，家族仍开放。 | 一次固定4starts×25000提案的26参数家族；允许突破旧六参阻断；需覆盖结构新进展；本轮不追加batch。；[原始证据](../research/ddp/breadth_20261027_wave5/hs850_orbit10_relaxation/REPORT.md) |

<a id="family-5"></a>
## Heisenberg central-extension Cayley

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [UT3(F9)五逆对Cayley完整机制容量](experiments/ddp-wave5-heisenberg729-capacity.md) | (10,3)；L=650；条件性n=729（未据此计纪录） | 投影秩不足4则断连；满秩五类关系的central fiber容量为6/6/6/1/1，均<9。 | UT3(F9)任意五个inverse generator pairs；全部projection关系weight；需改变central-fiber路径容量；不搜索域参数或seed。；[原始证据](../research/ddp/breadth_20261027_wave5/heisenberg729_capacity/REPORT.md) |

<a id="family-6"></a>
## bi-orbit Cayley/voltage constructions

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [SL2(F3)×C8双轨道2+2模板](experiments/ddp-wave2-sl23-c8-biorbit384-d5.md) | (4,5)；L=364；条件性n=384（未据此计纪录） | 最大最小fiber容量5<8，全固定模板排除；未开实际图profile。 | 固定group及2+2分配全部13824个SL quotient triples；需改变quotient短路容量。；[原始证据](../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/REPORT.md) |
| [Q64双轨道2+4：phase容量来源筛](experiments/ddp-wave2-two-orbit128-scout.md) | (6,3)；L=120；条件性n=128（未据此计纪录） | 14模式通过，未作参数搜索；交给后续独立有限profile。 | 32个phase模式；只是必要容量筛；只建议一次有界实际profile，已由search执行。；[原始证据](../research/ddp/breadth_20261027_wave2/two_orbit128_scout/RESULT.json) |
| [Q64双轨道128实际14phase有限试验](experiments/ddp-wave2-two-orbit128-search.md) | (6,3)；L=120；candidate_graph_or_family n=128；条件性n=128（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=928；saved_explicit_graph；bestD4/928；所有预定phase完成后停止。 | 14个通过phase，各固定三段邻域/两次kick；非全部Q64参数穷尽；该有限profile停止，不能以余预算加kick。；[原始证据](../research/ddp/breadth_20261027_wave2/two_orbit128_search/REPORT.md) |

<a id="family-7"></a>
## branched binary covers

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [364核binary branching必要matching MILP](experiments/ddp-wave3-binary-branch364.md) | (5,5)；L=650；条件性n=728（未据此计纪录） | 25秒求解无incumbent、无不可行证明，UNKNOWN；未生成728图。 | 固定364核；edge关系bijection或K2,2，必要matching必须击中全部unique5 geodesics；需新结构/明确有限授权，不能把UNKNOWN当UNSAT。；[原始证据](../research/ddp/breadth_20261027_wave3/binary_branch364/source.edges) |

<a id="family-8"></a>
## cooperative multi-vertex extension

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [两相邻新点合作扩张：来源准备未执行](experiments/ddp-wave8-cooperative-extension-scout.md) | (?,5)；L=不适用／见变体；多目标：[{'Delta': 12, 'D': 5, 'savedL': 42342, 'hypothetical_n': 42344, 'pin_cap_each': 11}, {'Delta': 11, 'D': 5, 'savedL': 37628, 'hypothetical_n': 37630, 'pin_cap_each': 10}] | 尚无新profile/MILP/图；全局可行性UNKNOWN，不能登记实际失败。 | 保留旧边、添加a-b、各连至多Delta-1个oldpins；仅恢复完整条件与来源；另行授权有限双新点profile，不能把旧8起点误说8邻居预算。；[原始证据](../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/REPORT.md) |
| [37628→37630：互连双新点的联合半径覆盖](experiments/ddp-wave9-cooperative37630.md) | (11,5)；L=37628；candidate_graph_or_family n=37630；条件性n=37630（未据此计纪录） | 新旧坏对=25，只验新根；two_new_root_eccentricities_only:6,6;source_old_D5_reused;whole_graph_all_pairs_BFS_not_performed；明确生成37630/205317/simple/max11图。两新根独立完整BFS均偏心率6，分别遗漏10、15个旧点，25个新旧坏对逐点MATCH，故候选D5失败；未全图all-pairs，不填全图ordinary坏对数。 | 固定37628源保留全部旧边，添加互连a-b，各≤10旧pins；共享仅原deficit≥2。两个指定确定性初态，每start最多两轮完整20位置坐标扫描；一完整轮无严格改善即停。；复用旧高覆盖A10再贪心补B10在本批优于从空平衡联合贪心；最佳对合法单pin严格替换已停滞。此profile已收束，不追加坐标轮/MILP/node数/source；后续需新的覆盖结构依据。；[原始证据](../research/ddp/breadth_20261027_wave9/cooperative37630/REPORT.md) |

<a id="family-9"></a>
## degree-plus-one matching shortcuts

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [650层结构与加matching降径参数准备](experiments/ddp-wave7-shortcut-matching-scout.md) | (6,4)；L=441；条件性n=650（未据此计纪录）；从属目标：[{'Delta': 5, 'D': 3, 'savedL': 72}, {'Delta': 5, 'D': 4, 'savedL': 252}, {'Delta': 6, 'D': 4, 'savedL': 441}, {'Delta': 7, 'D': 4, 'savedL': 684}, {'Delta': 8, 'D': 4, 'savedL': 1100}] | 恢复500/125/25三层及87800旧D5无序对；full500作用不容许invariant perfectmatching。 | 27格来源和Moore筛后选固定650源；本目录没有matching搜索；已进入独立shortcut650有限profile；不是另一独立方法。；[原始证据](../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/REPORT.md) |
| [固定650源加全局perfectmatching降径](experiments/ddp-wave7-shortcut650.md) | (6,4)；L=441；candidate_graph_or_family n=650；条件性n=650（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=31918；saved_explicit_graph；最佳图D5、31918个>4无序对；不排其他全局matching。 | 两固定starts各5000合法matching switches；允许打破初态对称性/远距限制；该profile停止，需不同覆盖结构，不追加HH修补或seed。；[原始证据](../research/ddp/breadth_20261027_wave7/shortcut650/REPORT.md) |

<a id="family-10"></a>
## edge subdivision / cooperative vertex insertion

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [170→171：删三条matching边并连六端点](experiments/ddp-wave8-insertion171.md) | (7,3)；L=170；candidate_graph_or_family n=171；条件性n=171（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=79；saved_explicit_graph；全部新根三球不满，最少仍漏11；指定整族无D3。保存fallbackD4/79不是全族坏对最优。 | 固定170源所有三条两两不接旧边，共32846935合法matching；须改变插入结构，不能继续同三边族；fallback79不能当全族最小坏对。；[原始证据](../research/ddp/breadth_20261027_wave8/insertion171/REPORT.md) |

<a id="family-11"></a>
## edge-local binary affine line lift

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [72控制点×F2⁴的逐边独立仿射线：1152点两起点失败](experiments/ddp-wave10-binary1152-edge-local.md) | (8,4)；L=1100；candidate_graph_or_family n=1152；条件性n=1152（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=29152；root_independent_all1152_source_ordinary_BFS；完整1152点4608边图simple、connected、8regular；root唯一全1152源BFS确认D5、29152个距离>4无序点对。144条参数反关系逐项合法，参数重建全部4608边与保存best.edges完全匹配。 | 固定72点简单4regular控制图；144条无向边各独立GL4(2)矩阵、非零b和任意affine offset c，GF2反边重新求逆；两预定初态各1000合法单边b/c/transvection proposals，无额外controller/field/move/seed。；独立GF2逐边逆矩阵/offset确实放松旧通用four-label chart限制，但容量和近端合法性不保证全对R4。此固定批已停，不追加move/seed/budget，重启须新的覆盖结构依据。；[原始证据](../research/ddp/breadth_20261027_wave10/binary1152_edge_local/REPORT.md) |

<a id="family-12"></a>
## fixed-controller affine line relations

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [固定Bhakar104×F2⁴二邻点线关系提升](experiments/ddp-wave2-line1664-d4.md) | (8,4)；L=1100；条件性n=1664（未据此计纪录） | 0→32只有唯一三路且无其他≤4walk，至多8<16，指定投影模板统一排除。 | 固定104投影、16fiber、无内部边、每控制边最多两个邻点，含非线性关系放宽；须改变投影路线容量；矩阵/seed不能补足。；[原始证据](../research/ddp/breadth_20261027_wave2/line1664_d4/REPORT.md) |
| [固定104×81三邻点degree预算提升](experiments/ddp-wave2-ternary8424-degree-budget.md) | (12,4)；L=5832；条件性n=8424（未据此计纪录） | 全部208控制边被迫branch3，内部余量0；0→32唯一三路仅27<81。 | 固定104、branch cap3、Δ12；允许内部预算但独占四路迫使全边branch3；须改变degree/路径机制，不能仅换域赋值。；[原始证据](../research/ddp/breadth_20261027_wave2/ternary8424_degree_budget/REPORT.md) |

<a id="family-13"></a>
## four-label affine route-chart lifts

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [31三角重叠扩张2760完整指定族](experiments/ddp-controller31-triangle-overlap2760-20261027.md) | (12,3)；L=810；controller n=31；条件性n=837（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=15；saved_controller_only;hypothetical_lift_not_generated；raw passers0；best controllerD4/15，requiredNB3缺34有序对。 | 345不同triangle/C5点对×8指定插入，2760不同标号quartic图；该族停止，不排一般31控制器。；[原始证据](../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/REPORT.md) |
| [33点三角端口控制系统固定有限合成](experiments/ddp-wave2-triangle-factor33-controller.md) | (12,3)；L=810；controller n=33；条件性n=891（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=12；saved_controller_only;hypothetical_lift_not_generated；best controllerD4/12普通坏对；容量U缺量684、28个有序不足槽。 | 固定三角骨架+external2factor，8starts各100000提案；32是33的共享三角结构跟进；三角端口骨架已收束，不追加31/34/seed；不排整个控制器族。；[原始证据](../research/ddp/breadth_20261027_wave2/triangle_factor33_controller/REPORT.md) |
| [32点三角端口控制系统固定有限合成](experiments/ddp-wave2-triangle-bowtie32-controller.md) | (12,3)；L=810；controller n=32；条件性n=864（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=4；saved_controller_only;hypothetical_lift_not_generated；best controllerD4/4普通坏对；容量U缺量324、14个有序不足槽。 | 固定三角骨架+external2factor，8starts各100000提案；32是33的共享三角结构跟进；三角端口骨架已收束，不追加31/34/seed；不排整个控制器族。；[原始证据](../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/REPORT.md) |
| [通用F3⁵五步chart与180/186控制器固定群筛](experiments/ddp-wave3-source-scout.md) | (12,5)；L=42342；条件性n=42525（未据此计纪录） | 324/324词rank5且逆一致；尚无≥175点quartic exact-NB5控制器。 | 原文通用chart；Cayley控制器子试验为从属有限群范围，不是独立新大类；仅有明确新控制器结构/路由覆盖才继续，不排队换群。；[原始证据](../research/ddp/breadth_20261027_wave3/source_scout/THEOREM_SCOPE_REVIEW.md) |
| [35个C5固定骨架的175控制器](experiments/ddp-wave3-pentagon175-controller.md) | (12,5)；L=42342；controller n=175；条件性n=42525（未据此计纪录） | 实际D=6，目标D=5；普通无序坏对=315；saved_controller_only;hypothetical_lift_not_generated；best controller ordinaryD6/315；exactNB5缺2696有序对。 | 四starts各10000外2factor交换提案；不排整个C5骨架；profile停止，不追加starts/group。；[原始证据](../research/ddp/breadth_20261027_wave3/pentagon175_controller/REPORT.md) |
| [原6点base的C4×C8电压192控制器](experiments/ddp-wave3-controller-lift192.md) | (12,5)；L=42342；controller n=192；条件性n=46656（未据此计纪录） | 实际D=6，目标D=5；普通无序坏对=144；saved_controller_only;hypothetical_lift_not_generated；best controller ordinaryD6/144；exactNB5缺2752有序对。 | 固定base/group，八starts×25000单坐标提案；非全部电压空间；父profile停止，不扩group/sheet/base。；[原始证据](../research/ddp/breadth_20261027_wave3/controller_lift192/REPORT.md) |
| [F2⁴四逆标签通用四步chart完整空间](experiments/ddp-wave3-binary-route-chart4.md) | (8,4)；L=1100；条件性n=1104（未据此计纪录） | 2419200规范候选全部失败；只此规范模型统一排除。 | F2维4、四无不动点逆标签、一步单参数、全部108约化四词均满秩；必须改变通用路由要求或机制，不加seed。；[原始证据](../research/ddp/breadth_20261027_wave3/binary_route_chart4/REPORT.md) |
| [三价exact-NB4/NB5控制器谱与计数界](experiments/ddp-wave3-cubic-nb5-bounds.md) | (?,?)；L=不适用／见变体 | NB4阶≤20；NB5阶≤44，42/44开放，不声称≤40。 | 仅cubic exact-NB4/5控制器，odd-label fiber chart尚未给出；有真实odd-label chart和控制器正向结构才继续。；[原始证据](../research/ddp/breadth_20261027_wave3/cubic_nb5_bounds/REPORT.md) |
| [H3显式对合商192与所有单调补度障碍](experiments/ddp-wave4-controller364-quotient.md) | (12,5)；L=42342；controller n=192；条件性n=46656（未据此计纪录） | 实际D=5，目标D=5；普通无序坏对=0；saved_controller_only;hypothetical_lift_not_generated；商图普通D5但exactNB5缺6288有序对；root10对角短障碍排除所有指定加边补度。 | 固定H3对合商，保留全部旧边、maximumdegree4的所有simple补边；需改变projection或允许删边，不能补度继续搜。；[原始证据](../research/ddp/breadth_20261027_wave4/controller364_quotient/REPORT.md) |
| [Mizuno新版D3边局部矩阵与18个F3模式](experiments/ddp-wave4-mizuno-d3-source.md) | (12,3)；L=810；条件性n=837（未据此计纪录） | 18局部模式/pencil已恢复；原框架good计数给controller n≤31，q3越810只剩31。 | 原30控制器=10K3及6C5，2-(6,3,2)交汇；q4原图1920，q3是另问题；应构造真正global31证书，不恢复旧32/33profile。；[原始证据](../research/ddp/breadth_20261027_wave4/mizuno_d3_source/README.md) |
| [F3⁴通用四步chart：108词满秩](experiments/ddp-wave5-chart4-quotient-probe.md) | (12,4)；L=5832；条件性n=5913（未据此计纪录） | 108/108约化长度四词rank4；正向结果。 | 保存F3⁵ chart公共不变线的四维商；局部线性规则，不是整图；有明确控制器结构与覆盖证书时才值得继续；不要把局部满秩当新下界。；[原始证据](../research/ddp/breadth_20261027_wave5/chart4_quotient_probe/RESULT.json) |
| [Mizuno72宽D4证书恢复及从属容量筛](experiments/ddp-wave5-mizuno-d4-source.md) | (12,4)；L=5832 | 原chart支持局部self与12个R2 pencil；exact-NB4不足不否定宽证书。 | 原72控制器的I∪R2∪100RG4充分证书；多项从属结构容量检查；改变容量瓶颈或有新controller证书；原C10父profile已另行终态。；[原始证据](../research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md) |
| [8base×C10九自由电压宽证书试验](experiments/ddp-wave5-mizuno-d4-c10-wide-search.md) | (12,4)；L=5832；controller n=80；条件性n=6480（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=20；saved_controller_only;hypothetical_lift_not_generated；最佳80控制图D5、20个>4无序对；wide还缺160有序对。 | 8个固定starts×25000电压提案；只此九自由父族有限批次；该父profile停止；只有改变真实结构/覆盖条件才值得重启，不追加seed/sheet/base。；[原始证据](../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/REPORT.md) |
| [AG(2,4) rainbow trade80旗标控制器](experiments/ddp-wave5-affine-flag80-trade.md) | (12,4)；L=5832；controller n=80；条件性n=6480（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=208；saved_controller_only;hypothetical_lift_not_generated；8图宽证书全部失败；最佳图普通D5/208坏对，其他7图未普通BFS。 | 固定parallelclass、lex前8个rainbow exact-cover、固定B次序与方向；需要新的全局几何覆盖步骤，不能靠追加exact-cover解/方向/次序。；[原始证据](../research/ddp/breadth_20261027_wave5/affine_flag80_trade/REPORT.md) |
| [两个6点基图×C13的exact-NB4必要筛](experiments/ddp-wave5-nb4-base-capacity.md) | (12,4)；L=5832；条件性n=6318（未据此计纪录） | 两base各有slot仅8条具名NB4词，8<13；甚至同base任意uniform≥9fiber均不行。 | 原144机制6base及octahedron两固定base，所有电压赋值；不排其他base；必须更换路径容量不足的结构，换电压/群不补足8条词。；[原始证据](../research/ddp/breadth_20261027_wave5/nb4_base_capacity/REPORT.md) |
| [固定F7⋊₃C12 quartic Cayley控制器完整筛](experiments/ddp-wave5-cayley84-nb4.md) | (12,4)；L=5832；条件性n=6804（未据此计纪录） | 722组phase容量不足，98组真群词仅到12或44点，无exact-NB4。 | 该固定84阶群全部820个simple inverse-closed四元生成集；固定群范围关闭，不能仅追加seed/另种S组成。；[原始证据](../research/ddp/breadth_20261027_wave5/cayley84_nb4/REPORT.md) |
| [固定Bhakar104的宽chart必要筛与唯一短路容量](experiments/ddp-wave5-bhakar104-wide-screen.md) | (12,4)；L=5832；条件性n=8424（未据此计纪录） | 0→32全部≤4walk恰唯一三路，至多27<81；固定投影提升统一不行。 | 固定104投影、81fiber、每控制边每点至多3邻点且无额外fiber/非投影边；只有改变固定投影或允许不同边机制才可能突破，改标签不够。；[原始证据](../research/ddp/breadth_20261027_wave5/bhakar104_wide_screen/REPORT.md) |
| [31点两bowtie quartic控制器全局交换](experiments/ddp-wave5-global31-two-bowties.md) | (12,3)；L=810；controller n=31；条件性n=837（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=7；saved_controller_only;hypothetical_lift_not_generated；raw passers=0；最佳controller普通D4/7坏对，required NB3缺18有序对。 | 一个架构，3固定fresh starts各200000合法交换；不排全部31图；须有新的raw可行controller架构，不追加同架构起点。；[原始证据](../research/ddp/breadth_20261027_wave5/global31_two_bowties/REPORT.md) |
| [31点edge-local十八模式稀疏证书求解工具](experiments/ddp-wave5-controller31-pattern-solver.md) | (12,3)；L=810；条件性n=837（未据此计纪录） | 工具已校准，输入0、MILP调用0、新图0。 | 固定31输入的精确pattern模型；本批没有上游raw passer；仅当明确raw31 passer出现再用工具；不自行生成输入。；[原始证据](../research/ddp/breadth_20261027_wave5/controller31_pattern_solver/README.md) |
| [F2³通用三步chart完整枚举与Fano障碍](experiments/ddp-wave5-binary-route-chart3.md) | (8,3)；L=253；条件性n=256（未据此计纪录） | 197568规范输入全部失败，最好28/36；Fano商空间短证明统一排除该模型。 | 四个固定逆矩阵、一步一个binary参数、全部36约化三词单route满秩；要改变通用单route要求，而非换此空间seed。；[原始证据](../research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md) |

<a id="family-14"></a>
## generalized-quadrangle incidence with internal 2-factors

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [W(3,5)关联图加两侧独立2factor：312点八度D3目标失败](experiments/ddp-wave10-gq312-internal-cycles.md) | (8,3)；L=253；candidate_graph_or_family n=312；条件性n=312（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=4090；root_independent_all312_source_ordinary_BFS；完整312点1248边图simple、connected、8regular；root唯一全312源BFS确认D4，4090个>3无序坏对，与production精确R3评分一致。936旧incidence和两侧各156条factor边完全匹配，所有内部度2。 | GF5四维symplectic W(3,5)的156点/156线，保留936关联边；两个156点侧各加入任意简单2factor。只两固定随机Hamilton初态，各1000合法two-edge switch，后续可分裂/合并cycle，不固定Hamilton。；关联几何严格保留大批近端/cross覆盖，独立2factor改变same-side远端路由，但该两起点未闭。停止固定批，不增q/field/source/degree/轮次；未来须明确新的same-side覆盖结构。；[原始证据](../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/REPORT.md) |

<a id="family-15"></a>
## idea:ddp-affine-cayley-d3

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [258阶四反射轨道完整检查失败](experiments/ddp-affine-cayley258-20261026.md) | (8,3)；L=253；candidate_graph_or_family n=258 | 实际D=4，目标D=3；原报告bad（类型见详情）=1935；Existing Wiki Metrics; no experiment rerun；35→18→3 modes;74 reflectionorbits;410478raw,6364illegal,404114legal full rootBFS;noD3. Best258/8/D4,bad1935. | AGL1(43) four-set orbit normalization preserves all4reflections, pairfields enumerateall43². Old10.5m bound never run. All258root unique final done.；AGL1(43) four-set orbit normalization preserves all4reflections, pairfields enumerateall43². Old10.5m bound never run. All258root unique final done.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley258/REPORT.md) |
| [AGL1(17)八元Cayley完整范围失败](experiments/ddp-affine-cayley272-20261026.md) | (8,3)；L=253；candidate_graph_or_family n=272 | 实际D=4，目标D=3；原报告bad（类型见详情）=1224；Existing Wiki Metrics; no experiment rerun；495phasepatterns→158;254852projectiveinputs,17838illegal,237014actualgraphs/fullrootBFS,0D3. Savedall272rootsD4,bad1224,rootspectrum1/8/55/199/9. | Capacity andtranslation/scalar normalization withmarkedduplicates preservefullfixedgroupS8scope; implementationreadindependently. Min9onlyactualscoredrange, notcapacityrejectedpatterns. No arbitrary272graphexclusion.；Capacity andtranslation/scalar normalization withmarkedduplicates preservefullfixedgroupS8scope; implementationreadindependently. Min9onlyactualscoredrange, notcapacityrejectedpatterns. No arbitrary272graphexclusion.；[原始证据](../research/ddp/m2_coset_tower/axis_cayley272/REPORT.md) |
| [312阶仿射直积群完整失败](experiments/ddp-affine-cayley312-20261026.md) | (8,3)；L=253；candidate_graph_or_family n=312 | 实际D=4，目标D=3；原报告bad（类型见详情）=3900；Existing Wiki Metrics; no experiment rerun；4060→370 modes;252258 raw;238440 legal full root BFS;noD3. Best312/8/D4,bad3900. | Full fixedgroup S8 scope; later symbolic filter370→12 is explanatory and not the actual search count.；Full fixedgroup S8 scope; later symbolic filter370→12 is explanatory and not the actual search count.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley312/REPORT.md) |
| [320阶特征2群的统一相位障碍](experiments/ddp-affine-cayley320-char2-20261026.md) | (8,3)；L=253；条件性n=320（未据此计纪录） | 1287→181→0 patterns;phase0≤15forms needs16. Zero fieldassignments/graphs/BFS. | Actual GF16 arithmetic uses XOR and polynomial0x13.332037projectivebound never searched. Only thisfixedgroup excluded.；Actual GF16 arithmetic uses XOR and polynomial0x13.332037projectivebound never searched. Only thisfixedgroup excluded.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley320_char2/REPORT.md) |
| [330阶固定群八元Cayley完整范围失败](experiments/ddp-affine-cayley330-20261026.md) | (8,3)；L=253；candidate_graph_or_family n=330 | 实际D=4，目标D=3；原报告bad（类型见详情）=5280；Existing Wiki Metrics; no experiment rerun；3876phasepatterns→135;17955actualgraphs allfailD3. Bestindependentall330roots D4,bad5280. | CompletefixedgroupS8family via necessarycapacity andprovedtranslation/scalar normalization. Minroot32onlyamongactual17955, notcapacityrejectedpatterns.；CompletefixedgroupS8family via necessarycapacity andprovedtranslation/scalar normalization. Minroot32onlyamongactual17955, notcapacityrejectedpatterns.；[原始证据](../research/ddp/m2_coset_tower/axis_cayley330/PROJECTIVE_SEARCH_REPORT.md) |
| [342阶仿射群唯一剩余模式完整失败](experiments/ddp-affine-cayley342-20261026.md) | (8,3)；L=253；candidate_graph_or_family n=342 | 实际D=4，目标D=3；原报告bad（类型见详情）=7866；Existing Wiki Metrics; no experiment rerun；715→100→1 modes;381 actual graphs;noD3. Best342/8/D4,bad7866. | Full group exclusion combines prior715mode capacity with this381 input completion; minimum46onlyscoredrange.；Full group exclusion combines prior715mode capacity with this381 input completion; minimum46onlyscoredrange.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley342/REPORT.md) |
| [六个固定仿射参数的必要容量比较](experiments/ddp-affine-parameter-capacity-20261026.md) | 多目标：agl7_d4→[4, 3]／L=41；agl7_times_c2_d5→[5, 3]／L=72；agl13_d6→[6, 3]／L=120；agl11_times_c2_d7→[7, 3]／L=170；f11_c20_nonfaithful_d7→[7, 3]／L=170；agl19_d8→[8, 3]／L=253（逐变体，不合成一个距离） | 2381fullpatterns,226plainpass;symbolicsurvivors0/0/0/4/0/1. No actualgraphs. | Four fixedgroups fully excluded; directproduct220notsearched,342actualrunseparate. PureCayley lowdegree literature used only forselection.；Four fixedgroups fully excluded; directproduct220notsearched,342actualrunseparate. PureCayley lowdegree literature used only forselection.；[原始证据](../research/ddp/m2_coset_tower/axis_parameter_capacity/REPORT.md) |
| [812点两六逆对模式完整生产](experiments/ddp-affine812-two-modes-20261026.md) | (12,3)；L=810；candidate_graph_or_family n=812 | 实际D=4，目标D=3；原报告bad（类型见详情）=15022；Existing Wiki Metrics; no experiment rerun；1465082raw,50520illegal,1414562fullrootBFS;bestD4,bad15022;all812roots independentlyverified. | Only2of8613symbolicmodesclosed. Capacity3.185232001CPU separately,notgraphcount.；Only2of8613symbolicmodesclosed. Capacity3.185232001CPU separately,notgraphcount.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley812_capacity/two_sixpair_production/REPORT.md) |
| [816点非忠实仿射作用的完整必要容量](experiments/ddp-affine816-capacity-20261026.md) | (12,3)；L=810；条件性n=816（未据此计纪录） | 593775→131540→67115modes;0field/graph/BFS;theoretical29512699702unexecuted.；后续结果优先：research-wiki/experiments/ddp-affine816-full-closure-20261027.md；Later existing note closes all67115 symbolic survivors in the same fixed group at degree<=12; older remaining-scope text is historical. | Actionorder16onC48,kernelphases0/16/32;anchorrequiresnontrivialscalar. Maximin76modeschosenforseparateproduction.；Actionorder16onC48,kernelphases0/16/32;anchorrequiresnontrivialscalar. Maximin76modeschosenforseparateproduction.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley816_capacity/SURVIVOR_SUMMARY.json) |
| [816点紧纤维与完整四逆对分支](experiments/ddp-affine816-fourpair-tight-20261026.md) | (12,3)；L=810；条件性n=816（未据此计纪录） | 12modes:2excludedbyiteratedtightlinearcapacity;10modes15085980raw10317300legalallfailfirstfiber.0BFS0graphs.；后续结果优先：research-wiki/experiments/ddp-affine816-full-closure-20261027.md；Later existing note closes all67115 symbolic survivors in the same fixed group at degree<=12; older remaining-scope text is historical. | Correct nullspace restoration and onlyz projective normalization. Exact17formsum0 is necessary; no whole816group exclusion.；Correct nullspace restoration and onlyz projective normalization. Exact17formsum0 is necessary; no whole816group exclusion.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley816_capacity/fourpair_tight/REPORT.md) |
| [816固定群十二度完整剩余范围](experiments/ddp-affine816-full-closure-20261027.md) | (12,3)；L=810；条件性n=816（未据此计纪录） | 7124representatives10747252152raw10041562788legal0fiberpass0BFS0graphs. All67115survivormodesclosed. | Explicitcompositionaccounting plus17involutionextension exclude degree≤12 onlyinthisfixedgroup.；Explicitcompositionaccounting plus17involutionextension exclude degree≤12 onlyinthisfixedgroup.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley816_capacity/fivepair_reduction/full_dimension_production/REPORT.md) |
| [816点全部76个maximin模式实际覆盖](experiments/ddp-affine816-maximin-20261026.md) | (12,3)；L=810；条件性n=816（未据此计纪录） | 46500312raw,44015564legal,2484748illegal;allfail exactfibers,0BFS/0graphs.；后续结果优先：research-wiki/experiments/ddp-affine816-full-closure-20261027.md；Later existing note closes all67115 symbolic survivors in the same fixed group at degree<=12; older remaining-scope text is historical. | Only28fivepairmin27+48sixpairmin26modesclosed;other67039open. Budgetaccounted8.644007includes0.5declaredallowance.；Only28fivepairmin27+48sixpairmin26modesclosed;other67039open. Budgetaccounted8.644007includes0.5declaredallowance.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley816_capacity/maximin_production/REPORT.md) |
| [816点完整六逆对剩余分支](experiments/ddp-affine816-sixpair-remaining-20261026.md) | (12,3)；L=810；条件性n=816（未据此计纪录） | 50680 remainingpatterns4497393880raw4407745588legal0BFS0graphs. Combinedall50728modes4501653448raw4412005156legalnoD3.；后续结果优先：research-wiki/experiments/ddp-affine816-full-closure-20261027.md；Later existing note closes all67115 symbolic survivors in the same fixed group at degree<=12; older remaining-scope text is historical. | Exact fibercoverage and actual12elementlegality;χ≠1anchor. Five productionprefix48mask calibrations; completed iterator/no pendinggraph. Otherpaircounts separate.；Exact fibercoverage and actual12elementlegality;χ≠1anchor. Five productionprefix48mask calibrations; completed iterator/no pendinggraph. Otherpaircounts separate.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley816_capacity/sixpair_remaining/REPORT.md) |
| [820点完整生成元相位与组成邻域](experiments/ddp-affine820-phase-moves-20261026.md) | (12,3)；L=810；candidate_graph_or_family n=820 | 17starts43filteredscans26moves148681actualrootBFS;bestmiss34unchanged. | Finite capacity-surviving neighborhoods only. Finaledges exactly equal auditedsource; no repeatfinalBFS.；Finite capacity-surviving neighborhoods only. Finaledges exactly equal auditedsource; no repeatfinalBFS.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley820_phase_moves/REPORT.md) |
| [820点十二度完整相位筛及有界坐标profile](experiments/ddp-affine820-profile-20261026.md) | (12,3)；L=810；candidate_graph_or_family n=820 | 实际D=4，目标D=3；原报告bad（类型见详情）=13940；Existing Wiki Metrics; no experiment rerun；8008→3982→2139modes;34224samples+6258neighbors=40482fullrootBFS;best47→34miss,D4,bad13940. | Allpatterns got16legal samples thenonlytop16fixedphase descent. WholefieldfamilyOPEN;totaltheoretical1321279147846 notsearched.；Allpatterns got16legal samples thenonlytop16fixedphase descent. WholefieldfamilyOPEN;totaltheoretical1321279147846 notsearched.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley820_capacity/PROFILE_REPORT.md) |
| [930阶十一与十二度完整必要容量比较](experiments/ddp-affine930-capacity-20261026.md) | 多目标：degree11 necessary capacity→[11, 3]／L=715；degree12 necessary capacity→[12, 3]／L=810（逐变体，不合成一个距离）；条件性n=930（未据此计纪录） | d11:15504→1509→78;d12:54264→16642→5944. Zero fieldassignments/graphs/BFS.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family. | Necessary phase/form capacities only;d12 theoretical191303804004 inputs notrun.；Necessary phase/form capacities only;d12 theoretical191303804004 inputs notrun.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/REPORT.md) |
| [930点十一度五逆对分支完整失败](experiments/ddp-affine930-d11-fivepair-20261026.md) | (11,3)；L=715；candidate_graph_or_family n=930 | 实际D=4，目标D=3；原报告bad（类型见详情）=55800；Existing Wiki Metrics; no experiment rerun；8260050raw,254536illegal,8005514legal fullrootBFS;noD3. BestD4,bad55800,rootspectrum1/11/110/688/120.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family. | Onlyfivepair+1reflectionfixedgroupbranchclosed;other37fourpairmodesopen. Independentall930rootfinaldoneonce.；Onlyfivepair+1reflectionfixedgroupbranchclosed;other37fourpairmodesopen. Independentall930rootfinaldoneonce.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_PRODUCTION_REPORT.md) |
| [930点四逆对完整范围与全部十一度合并](experiments/ddp-affine930-d11-fourpair-20261026.md) | (11,3)；L=715；条件性n=930（未据此计纪录） | 1094587872raw,990938033legal;firstfiber1488pass,secondfiber0pass;0BFS/0graphs. | Together with oldphase/tight/fivepair checks excludes thisfixedgroup degree≤11 only. Notgeneral930graphs ordegree12.；Together with oldphase/tight/fivepair checks excludes thisfixedgroup degree≤11 only. Notgeneral930graphs ordegree12.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/d11_fourpair_production/REPORT.md) |
| [固定930点图的30种单反射加度扩展](experiments/ddp-affine930-d12-fixed-extension-20261026.md) | (12,3)；L=810；candidate_graph_or_family n=930 | 实际D=4，目标D=3；原报告bad（类型见详情）=31155；Existing Wiki Metrics; no experiment rerun；All30 additions checked;bestadd(20,15),930/12/D4,bad31155,root1/12/130/720/67. | Only fixeddegree11sourceplusoneotherreflection scopeclosed;notalld12. All5580edges and930roots independently checkedonce.；Only fixeddegree11sourceplusoneotherreflection scopeclosed;notalld12. All5580edges and930roots independently checkedonce.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/d12_one_reflection_extension/REPORT.md) |
| [多一形式纤维的必要二次矩诊断](experiments/ddp-affine930-surplus-one-20261026.md) | (11,3)；L=715 | 22modes52fibers allrank6;0newlinearconstraints,37modesremain.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family. | Exactlyq+1forms coveringFq imply sumL²=(sumL)². No highranklinearization oradditionalexclusion.；Exactlyq+1forms coveringFq imply sumL²=(sumL)². No highranklinearization oradditionalexclusion.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_SURPLUS_ONE_SCOPE.md) |
| [紧31形式纤维的排列求和必要约束](experiments/ddp-affine930-tight-linear-20261026.md) | (11,3)；L=715 | d11 modes78→75;fivepair38modes markedscope8260050;fourpair37modes1094587872. No actualgraphs inthisstep.；后续结果优先：research-wiki/experiments/ddp-affine930-d11-fourpair-20261026.md；Later existing note completes degree<=11 in this fixed group. It does not close the full degree12 family. | Exactly31 forms coveringF31 havezero sum. Onlyz normalized innullspace. Later quadratic ranks4/5 give no additional exclusion or linearization.；Exactly31 forms coveringF31 havezero sum. Onlyz normalized innullspace. Later quadratic ranks4/5 give no additional exclusion or linearization.；[原始证据](../research/ddp/m2_coset_tower/affine_cayley930_capacity/D11_TIGHT_LINEAR.md) |

<a id="family-16"></a>
## idea:ddp-bicayley-d3

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [172固定源独立斜率非正则修改](experiments/ddp-affine4-independent-slope-20261027.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；原报告bad（类型见详情）=666；Existing Wiki Metrics; no experiment rerun；574actualall172root candidates;allD4;bestm601min6max7bad666. | Legalmaxdegree modelwithmergededges;onlyonefixedsource onechangedmatching;uniqueall172finaldone.；Legalmaxdegree modelwithmergededges;onlyonefixedsource onechangedmatching;uniqueall172finaldone.；[原始证据](../research/ddp/m2_coset_tower/affine4_172_independent_slope/REPORT.md) |
| [两个四轨道底图共同仿射斜率障碍](experiments/ddp-affine4-shared-slope-20261027.md) | 多目标：shared-slope base→[6, 3]／L=120；shared-slope base→[7, 3]／L=170（逐变体，不合成一个距离） | 27000+74088triples finitecheck;124survivortriples symboliccomposition;0translations0graphs0BFS. | Self-containedHamiltonclassification andmissingline/interpolation proof forceflat;noveltynotclaimed;notindependent-slope irregulargraphs.；Self-containedHamiltonclassification andmissingline/interpolation proof forceflat;noveltynotclaimed;notindependent-slope irregulargraphs.；[原始证据](../research/ddp/m2_coset_tower/affine_four_orbit_matching_cover/AFFINE_MATCHING_COVER.md) |
| [172点七度双轨道九模式有界搜索](experiments/ddp-bicayley172-profile-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；原报告bad（类型见详情）=688；Existing Wiki Metrics; no experiment rerun；110→72→9patterns;144starts;1673581legal two-root evaluations withduplicates;bestmisssum16,D4,bad688. | Completephasefilter butnotcompletefieldsearch. Uniqueall172rootverificationdone;noextra seeds.；Completephasefilter butnotcompletefieldsearch. Uniqueall172rootverificationdone;noextra seeds.；[原始证据](../research/ddp/m2_coset_tower/bicayley172/REPORT.md) |
| [解除820点Cayley层间约束的实际搜索](experiments/ddp-bicayley820-release-20261026.md) | (12,3)；L=810；candidate_graph_or_family n=820 | 实际D=4，目标D=3；原报告bad（类型见详情）=13940；Existing Wiki Metrics; no experiment rerun；33starts297segments,634601legal evaluations/1269202rootBFS. Bestunchangedsource34/34,D4,bad13940. | IndependentA/B/T genuinelyrelaxCayleycoupling;fixedphasefamilynotexhausted. Finalgraphidentityinheritspriorall820rootcheck,nonewfullBFS.；IndependentA/B/T genuinelyrelaxCayleycoupling;fixedphasefamilynotexhausted. Finalgraphidentityinheritspriorall820rootcheck,nonewfullBFS.；[原始证据](../research/ddp/m2_coset_tower/bicayley820/REPORT.md) |
| [124点六度四轨道容量与实际profile](experiments/ddp-cyclic4-124-profile-20261026.md) | (6,3)；L=120；candidate_graph_or_family n=124 | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；47bases25pass;222diag55/off44;64starts545805evaluations;best279D4. | Freshq31inputs,notscaled172seeds;uniqueall124finaldone;wholefamilyopen.；Freshq31inputs,notscaled172seeds;uniqueall124finaldone;wholefamilyopen.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_124_balanced/REPORT.md) |
| [172点平衡322底图有限构造](experiments/ddp-cyclic4-172-balanced-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；原报告bad（类型见详情）=258；Existing Wiki Metrics; no experiment rerun；64starts576segments994264evaluations3977056rootBFS;bestrootmiss2/5/3/2,D4,bad258. | Basecapacityminimum68vs63for421;wholefamilyopen. All602edges and172roots independentlycheckedonce.；Basecapacityminimum68vs63for421;wholefamilyopen. All602edges and172roots independentlycheckedonce.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_balanced/REPORT.md) |
| [平衡172候选完整双坐标邻域](experiments/ddp-cyclic4-172-balanced-pair-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 97020rawslots90663legal6357illegal;plusseed90664fourroot evaluations;noimprovement. | Final602edgesexactlysource,verificationreused;noextra seed/round/triple search.；Final602edgesexactlysource,verificationreused;noextra seed/round/triple search.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_balanced/two_coordinate_moves/REPORT.md) |
| [172点完整普通两边交换邻域](experiments/ddp-cyclic4-172-edge-switch-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 361802raw332906legal28896illegal;332905safe cutoffs,onecomplete score;noimprovement. | All172root bitsetradius3 withoutsymmetry;firstlegalordinaryBFS calibration. Samefinaledges,no repeatedfinalBFS. Strictlocalminimumonly.；All172root bitsetradius3 withoutsymmetry;firstlegalordinaryBFS calibration. Samefinaledges,no repeatedfinalBFS. Strictlocalminimumonly.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_balanced/local_edge_switches/REPORT.md) |
| [172点四循环轨道解除双轨道耦合](experiments/ddp-cyclic4-172-release-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；原报告bad（类型见详情）=387；Existing Wiki Metrics; no experiment rerun；33starts297segments513195states2052780rootBFS;bad688→387,D4;independentall172rootsdone. | 14rawvoltagesminus3treegauge=11;old11minus2=9. Twoactualcouplingconstraintsreleased;wholefamilyopen.；14rawvoltagesminus3treegauge=11;old11minus2=9. Twoactualcouplingconstraintsreleased;wholefamilyopen.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_release/REPORT.md) |
| [172点完整三坐标邻域](experiments/ddp-cyclic4-172-triple-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；原报告bad（类型见详情）=258；Existing Wiki Metrics; no experiment rerun；12224520raw11088102legal1136418illegal;noimprovement,bad258D4. | One fixed source,simultaneous threecoordinate assignments; finaledges same and previousaudit reused. Familyopen.；One fixed source,simultaneous threecoordinate assignments; finaledges same and previousaudit reused. Familyopen.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_balanced/three_coordinate_moves/REPORT.md) |
| [172点已验候选完整双坐标邻域](experiments/ddp-cyclic4-172-two-coordinate-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 97020rawneighbor slots87597legal9423illegal;plusseed87598fourroot evaluations;noimprovement. | Onefixedstart,onecomplete neighborhood. Same602edgesas auditedsource,0newfinalBFS;notwholefamilyexclusion.；Onefixedstart,onecomplete neighborhood. Same602edgesas auditedsource,0newfinalBFS;notwholefamilyexclusion.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_release/two_coordinate_moves/REPORT.md) |
| [172含内部循环边完整底图容量](experiments/ddp-cyclic4-loop-capacity-20261026.md) | (7,3)；L=170；条件性n=172（未据此计纪录） | 91connectedtypes52capacitypass48withloops;bestloopminimum61vsold68.0graphs. | Onlyinverse dartcancelled; treegaugecounts preserved; necessarycapacity only.；Onlyinverse dartcancelled; treegaugecounts preserved; necessarycapacity only.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_loop_capacity/REPORT.md) |
| [172内部循环边固定拓扑profile](experiments/ddp-cyclic4-loop-profile-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；17starts153segments262233evaluations1048932rootBFS;best344D4. | Improves473sourcebutnotold258;wholefieldfamilyopen;uniqueall172finaldone.；Improves473sourcebutnotold258;wholefieldfamilyopen;uniqueall172finaldone.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_loop_search/REPORT.md) |
| [172固定源匹配改循环完整4410项](experiments/ddp-cyclic4-loop-surgery-20261026.md) | (7,3)；L=170；candidate_graph_or_family n=172 | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；4410actualgraphs17640rootBFS;best473D4;uniqueall172finaldone. | Onlyfixedsource;notimprovementover258.；Onlyfixedsource;notimprovementover258.；[原始证据](../research/ddp/m2_coset_tower/cyclic4_172_loop_surgery/REPORT.md) |
| [D64与Q64完整相位容量](experiments/ddp-nonabelian4-capacity-20261027.md) | (8,3)；L=253 | Both8192 maskscomplete;D641953pass/min36,Q647930pass/min52;0graphs0BFS. | Necessarysymboliccounts only;constant16 retained;all tight jointcongruences consistent;no extra exclusion.；Necessarysymboliccounts only;constant16 retained;all tight jointcongruences consistent;no extra exclusion.；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_capacity/CAPACITY_REPORT.md) |
| [Q64四轨道256点实际构造](experiments/ddp-q64-256-profile-20261027.md) | (8,3)；L=253；candidate_graph_or_family n=256 | 实际D=4，目标D=3；原报告bad（类型见详情）=832；Existing Wiki Metrics; no experiment rerun；64starts576segments1895852legalevaluations;best256/8/D4,bad832;uniqueall256rootcheckdone. | Wholefamilyopen;centerquotientstillD4,sofixedmod16centralflipsretainatleast128badpairs;noextraenumeration.；Wholefamilyopen;centerquotientstillD4,sofixedmod16centralflipsretainatleast128badpairs;noextraenumeration.；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_search/REPORT.md) |
| [固定投影的中心匹配替换检查](experiments/ddp-q64-central-matching-20261027.md) | (8,3)；L=253；条件性n=256（未据此计纪录） | All 22 fixed projection modifications fail necessary quotient radius-three coverage; zero center assignments and no graph BFS. | 固定上一轮 L4 投影，删两条跨轨道匹配并加入内部中心匹配的 22 个选择全部检查完毕，均在商图三步覆盖条件处失败。此结论覆盖这 22 个固定改动及其合法中心提升，不排除采用其他投影的一般构造。；固定上一轮 L4 投影，删两条跨轨道匹配并加入内部中心匹配的 22 个选择全部检查完毕，均在商图三步覆盖条件处失败。此结论覆盖这 22 个固定改动及其合法中心提升，不排除采用其他投影的一般构造。；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_central_matching/SCOPE.md) |
| [单商电压改动与全部中心提升](experiments/ddp-q64-central-one-20261027.md) | (8,3)；L=253；candidate_graph_or_family n=256 | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；403projections:395quotientreject,8scored65536legalcenters,noD3;best1152D4uniquelyall256verified. | Exact affinebadsets,properparallellegality;bestonlyinquotientcomplete scoredscope.；Exact affinebadsets,properparallellegality;bestonlyinquotientcomplete scoredscope.；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_central_lift/REPORT.md) |
| [双商电压完整范围与中心形式障碍](experiments/ddp-q64-central-two-20261027.md) | (8,3)；L=253；条件性n=256（未据此计纪录） | 74958projections:74603quotientreject,355singletonreject(min12);0centers0graphs0BFS. | Complete markedtwo-coordinate ball,disjointfromone-coordinate;wholeQ64familyopen.；Complete markedtwo-coordinate ball,disjointfromone-coordinate;wholeQ64familyopen.；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_central_lift/two_quotient_coordinates/REPORT.md) |
| [投影缺口目标的实际构造profile](experiments/ddp-q64-quotient-descent-20261027.md) | (8,3)；L=253；条件性n=256（未据此计纪录） | 16starts144segments232260legalprojections;bestL4,noL0/no centers/no graph. | Bestfour singletonslotsareonlyselfidentityemptywords;centerantipodesforce≥128badforanylift;notattainability.；Bestfour singletonslotsareonlyselfidentityemptywords;centerantipodesforce≥128badforanylift;notattainability.；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_central_lift/quotient_descent/REPORT.md) |
| [指定双三角形的中心提升有限搜索](experiments/ddp-q64-triangle-lift-20261027.md) | (8,3)；L=253；条件性n=256（未据此计纪录） | 16 starts; 144 segments; 204384 legal projection evaluations; best L6; zero center assignments and no saved graph. | 256 点、8 度的指定双三角形试验已完成 16 个起点、144 段和 204384 次合法投影评分。两个三角形保证每个顶点的中心对应点可在三步内到达，修复了上一轮的具体障碍；但最好投影仍为 L=6，每个合法中心提升至少有 192 个距离大于三的无序点对。该下界未必可达到；本批没有枚举中心位，也没有保存新完整图。累计实测 10.386599 CPU 秒。；256 点、8 度的指定双三角形试验已完成 16 个起点、144 段和 204384 次合法投影评分。两个三角形保证每个顶点的中心对应点可在三步内到达，修复了上一轮的具体障碍；但最好投影仍为 L=6，每个合法中心提升至少有 192 个距离大于三的无序点对。该下界未必可达到；本批没有枚举中心位，也没有保存新完整图。累计实测 10.386599 CPU 秒。；[原始证据](../research/ddp/m2_coset_tower/nonabelian4_256_triangle_lift/REPORT.md) |

<a id="family-17"></a>
## idea:ddp-bicayley220-one-reflection

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [220双轨道指定族的九值短矛盾](experiments/ddp-bicayley220-capacity-20261026.md) | (7,3)；L=170 | 2002→48→0 patterns;root0/samelayer/phase0≤9<11. Zero actualS/graphs/BFS. | Gauge/phasecoverage/two-rootwordpaths independently checked without repeatingcapacity. Only1reflection+6crossfamily.；Gauge/phasecoverage/two-rootwordpaths independently checked without repeatingcapacity. Only1reflection+6crossfamily.；[原始证据](../research/ddp/m2_coset_tower/bicayley220/STRUCTURE_SCOPE.md) |

<a id="family-18"></a>
## idea:ddp-breadth-20261027

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [二点仿射线关系与内部匹配有限试验](experiments/ddp-line960-internal-matching-20261027.md) | (12,3)；L=810；candidate_graph_or_family n=960 | 实际D=4，目标D=3；原报告bad（类型见详情）=77784；Existing Wiki Metrics; no experiment rerun；n=960, degree cap=12, target D=3; independently checked D=4, bad pairs=77784. | 4起点；20000次参数更新。随后发现固定源及匹配的统一三步容量障碍；未声称任意图不存在或取得新下界。；4起点；20000次参数更新。随后发现固定源及匹配的统一三步容量障碍；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/line960_internal_matching/REPORT.md) |
| [Möbius置换的Schreier图有限试验](experiments/ddp-mobius108-schreier-20261027.md) | (4,4)；L=104；candidate_graph_or_family n=108 | 实际D=6，目标D=4；原报告bad（类型见详情）=784；Existing Wiki Metrics; no experiment rerun；n=108, degree cap=4, target D=4; independently checked D=6, bad pairs=784. | 30000个矩阵对；断连样本也计入。有限采样完成；整个作用图族仍开放；未声称任意图不存在或取得新下界。；30000个矩阵对；断连样本也计入。有限采样完成；整个作用图族仍开放；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/mobius108_schreier/REPORT.md) |
| [不等长陪集轨道图有限试验](experiments/ddp-pgl2-7-orbits126-20261027.md) | (6,3)；L=120；candidate_graph_or_family n=126 | 实际D=4，目标D=3；原报告bad（类型见详情）=840；Existing Wiki Metrics; no experiment rerun；n=126, degree cap=6, target D=3; independently checked D=4, bad pairs=840. | 固定H8/K4；全部120个六正则组合。关闭固定稳定子、恰六正则的组合范围；未声称任意图不存在或取得新下界。；固定H8/K4；全部120个六正则组合。关闭固定稳定子、恰六正则的组合范围；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/pgl2_7_orbits126/REPORT.md) |
| [PSL(2,13) Cayley图有限试验](experiments/ddp-psl2-13-cayley-20261027.md) | (12,3)；L=810；candidate_graph_or_family n=1092 | 实际D=4，目标D=3；原报告bad（类型见详情）=76440；Existing Wiki Metrics; no experiment rerun；n=1092, degree cap=12, target D=3; independently checked D=4, bad pairs=76440. | 12起点；36段。有限试验完成；整个群族仍开放；未声称任意图不存在或取得新下界。；12起点；36段。有限试验完成；整个群族仍开放；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/psl2_13_cayley/REPORT.md) |
| [PSL(2,23)不等长轨道：D5变体有限试验](experiments/ddp-psl2-23-orbits3542-d5-20261027.md) | (7,5)；L=2810；candidate_graph_or_family n=3542 | 实际D=6，目标D=5；原报告bad（类型见详情）=233772；Existing Wiki Metrics; no experiment rerun；n=3542, degree cap=7, target D=5; independently checked D=6, bad pairs=233772. | 固定C4/C3稳定子；839960组成中预选1000个不重复组合。D5参数的有限试验完成；属于陪集轨道方法变体；未声称任意图不存在或取得新下界。；固定C4/C3稳定子；839960组成中预选1000个不重复组合。D5参数的有限试验完成；属于陪集轨道方法变体；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/psl2_23_orbits3542_d5/REPORT.md) |
| [14点底图的Q8电压提升有限试验](experiments/ddp-q8-lift112-d4-20261027.md) | (4,4)；L=104；candidate_graph_or_family n=112 | 实际D=5，目标D=4；原报告bad（类型见详情）=480；Existing Wiki Metrics; no experiment rerun；n=112, degree cap=4, target D=4; independently checked D=5, bad pairs=480. | 12起点；36段。较大底图与D4路线的电压方法变体，有限试验完成；未声称任意图不存在或取得新下界。；12起点；36段。较大底图与D4路线的电压方法变体，有限试验完成；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/q8_lift112_d4/REPORT.md) |
| [一般图两边交换退火有限试验](experiments/ddp-regular122-anneal-20261027.md) | (6,3)；L=120；candidate_graph_or_family n=122 | 实际D=4，目标D=3；原报告bad（类型见详情）=403；Existing Wiki Metrics; no experiment rerun；n=122, degree cap=6, target D=3; independently checked D=4, bad pairs=403. | 8起点；200万交换提案。有限试验完成；一般图仍开放；未声称任意图不存在或取得新下界。；8起点；200万交换提案。有限试验完成；一般图仍开放；未声称任意图不存在或取得新下界。；[原始证据](../research/ddp/breadth_20261027/regular122_anneal/REPORT.md) |

<a id="family-19"></a>
## idea:ddp-m1-two-orbit-voltage

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [F41半直积C8内部反射分支完整检查](experiments/ddp-f41-reflections-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=656 | 实际D=6，目标D=5；原报告bad（类型见详情）=984；Existing Wiki Metrics; no experiment rerun；40 mixed和4 both骨架全部完成：14059884赋值、13740658合法。mixed最优1804坏对，both984；独立全656根BFS均五正则D6。 | A双反射固定后保留mixed三变量和both四变量，未误用旧projective缩放或mixed侧交换。形式容量筛选有候选保全，实际完整有限范围仅此群/分配，不排一般656图。；A双反射固定后保留mixed三变量和both四变量，未误用旧projective缩放或mixed侧交换。形式容量筛选有候选保全，实际完整有限范围仅此群/分配，不排一般656图。；[原始证据](../research/ddp/m1_f41_reflections/SEARCH_REPORT.md) |
| [702点释放C27后的C13电压修复](experiments/ddp-m1-c13-repair-20261026.md) | (7,4)；L=684；candidate_graph_or_family n=702 | 实际D=5，目标D=4；原报告bad（类型见详情）=1404；Existing Wiki Metrics; no experiment rerun；2268个单电压邻居全部恶化；120s内271274提案/31334接受；best216代表漏点=1404坏无序对，last612=3978。两张完整图均独立BFS验证七正则、直径5。 | 固定54点商图的单电压严格局部最小；定向单/双电压退火未改善。不排除整个C13电压族。此批结束，不追加相同预算。；固定54点商图的单电压严格局部最小；定向单/双电压退火未改善。不排除整个C13电压族。此批结束，不追加相同预算。；[原始证据](../research/ddp/m1_fullgraph_repair/C13_PROFILE.md) |
| [666点图C37商的精确缺陷与单电压邻域](experiments/ddp-m1-c37-diagnosis-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=666 | 18基点45条含环/平行边的商精确还原；每纤维71至105个形式表达式。1620电压修改中1593合法，0改善、9同图中性、1584变差；最小变差把666坏对增为1480。 | 九个37圈各附37片叶构成全部坏对图。失败来自实际表达式碰撞而非形式容量不足；单坐标严格局部最小不等于同时赋值不可行，没有追加退火。；九个37圈各附37片叶构成全部坏对图。失败来自实际表达式碰撞而非形式容量不足；单坐标严格局部最小不等于同时赋值不可行，没有追加退火。；[原始证据](../research/ddp/m1_c37_diagnosis/DIAGNOSIS.md) |
| [(5,5)内部4跨侧1：四个完整有限构造族](experiments/ddp-m1-d5-four-one-20261026.md) | (5,5)；L=650 | 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；823骨架、501645射影代表、399329合法候选完成；四族最佳坏对5616/20274/6724/666，完整图均五正则、直径6。 | 仅排指定四个群及每侧两个非对合逆对的4+1范围；不排对合分支、其他群或一般图。共同共轭/缩放规约已实际进入完整生成。；仅排指定四个群及每侧两个非对合逆对的4+1范围；不排对合分支、其他群或一般图。共同共轭/缩放规约已实际进入完整生成。；[原始证据](../research/ddp/m1_d5_four_one_results.md) |
| [(5,5)共同共轭/射影规约与四个完整构造族](experiments/ddp-m1-d5-projective-20261026.md) | (5,5)；L=650 | 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；原702族1464骨架/267912项目代表/260922合法，最小坏对2106。忠实作用三族654/656/666点，共422骨架/743678代表/631705合法，最小坏对6540/4100/999。全部最佳图独立BFS为五正则、直径6。 | 共轭消一维、缩放取项目点，商同构规约及逐骨架完整记录使指定单逆对2+3族获得完整有限检查；均无D5图。不是一般阶数或整个M1机制排除。新构造必须改变该完整范围内的实际结构，不能增加相同seed。；共轭消一维、缩放取项目点，商同构规约及逐骨架完整记录使指定单逆对2+3族获得完整有限检查；均无D5图。不是一般阶数或整个M1机制排除。新构造必须改变该完整范围内的实际结构，不能增加相同seed。；[原始证据](../research/ddp/m1_d5_projective_reduction.md) |
| [已有电压图删逆对后对(5,5)的直接迁移](experiments/ddp-m1-d5-prunings-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=702 | 实际D=6，目标D=5；原报告bad（类型见详情）=9477；Existing Wiki Metrics; no experiment rerun；702/720两图各4种逆对删边，8张完整五正则图均D6或D7；最佳702图D6，9477坏对。两根与独立全根距离谱相符。 | 更长路线允许同机制检验新参数；直接删边尚未成功。下一步用F13共同共轭及缩放降维，有限覆盖完整2+3赋值，不能只从8张子图否定该族。；更长路线允许同机制检验新参数；直接删边尚未成功。下一步用F13共同共轭及缩放降维，有限覆盖完整2+3赋值，不能只从8张子图否定该族。；[原始证据](../research/ddp/m1_degree5_transfer/REPORT.md) |
| [同一电压机制在(7,4)的702/720点候选](experiments/ddp-m1-d7-first-profile-20261026.md) | (7,4)；L=684；从属目标：[[7, 4]] | 实际D=5，目标D=4；Existing Wiki Metrics; no experiment rerun；702vertices,2457edges,degree7,diameter5,1404badpairs;720vertices,2520edges,degree7,diameter5,2700badpairs. Full-source BFS from edge lists. | Both exceed record684 in order but fail diameter4, so neither is a new bound. Recovered684 baseline all-source regression passed. Analyze actual distance5 failures before local repair or changed quotient.；Both exceed record684 in order but fail diameter4, so neither is a new bound. Recovered684 baseline all-source regression passed. Analyze actual distance5 failures before local repair or changed quotient.；[原始证据](../computations/ddp/m1/d7_profile) |
| [2824点F353半直积C4七度完整图profile](experiments/ddp-m1-d7d5-f353-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=2824 | 实际D=6，目标D=5；原报告bad（类型见详情）=172264；Existing Wiki Metrics; no experiment rerun；1264612提案、27047接受；最佳两根missing244，独立全部2824根BFS：七正则、直径6、172264坏对；末态183560坏对。 | 已知2810边表恢复并通过正例后改变群作用至阶4；一个120CPU秒profile无新下界，不是完整族排除。保留best/last参数和边表，无追加seed。；已知2810边表恢复并通过正例后改变群作用至阶4；一个120CPU秒profile无新下界，不是完整族排除。保留best/last参数和边表，无追加seed。；[原始证据](../research/ddp/m1_d7d5_f353_results.md) |
| [四个1+5电压候选的完整图与直径失败](experiments/ddp-m1-first-profile-20261026.md) | (6,3)；L=120；从属目标：[[6, 3]] | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；UT4(F2):n128,bad1024;D8xD8:n128,bad1536;HeisZ4:n128,bad800;C6xA4:n144,bad792. All simple6-regular connected diameter4; all-source BFS agrees with exact orbit scores. | No new(6,3) lower bound. Best values reached within0.02s and persisted for22–27million evaluated proposals. Change generating degree allocation to2+4/r4 rather than extending unchanged trajectories. This rejects saved candidates only.；No new(6,3) lower bound. Best values reached within0.02s and persisted for22–27million evaluated proposals. Change generating degree allocation to2+4/r4 rather than extending unchanged trajectories. This rejects saved candidates only.；[原始证据](../computations/ddp/m1/profile) |
| [126点两轨道2+4模板：完整有限判定未命中](experiments/ddp-m1-q63-exact-20261026.md) | (6,3)；L=120；candidate_graph_or_family n=126 | 原报告bad（类型见详情）=315；13365 quotient skeletons;10149 necessary-symbolic exclusions;3216 survivor skeletons;54051312 raw and49227360 legal assignments;no radius3 complete graph. Saved skeleton best315badpairs. | Complete for G=F7 semidirectC9 action2,internal inverse pairsA/B,cross4 with identity normalized. Both-root full endpoint coverage required. Does not exclude4+2, other groups, or arbitrary126 graphs. Positive depth4 control and independent direct BFS checks passed; not Lean; later result not covered by earlier Gemini receipt.；Complete for G=F7 semidirectC9 action2,internal inverse pairsA/B,cross4 with identity normalized. Both-root full endpoint coverage required. Does not exclude4+2, other groups, or arbitrary126 graphs. Positive depth4 control and independent direct BFS checks passed; not Lean; later result not covered by earlier Gemini receipt.；[原始证据](../research/ddp/m1_q63_quotient/DERIVATION.md) |
| [非忠实反射剩余三分支完整有限判定](experiments/ddp-nonfaithful-remaining-20261026.md) | (5,5)；L=650；从属目标：[[5, 5]] | 实际D=6，目标D=5；Existing Wiki Metrics; no experiment rerun；3332186 raw slots;3273316 legal inputs all scored. p17 mixed771341; p29 mixed1136191; p29 both1365784. Best graphs816/696/696 are independently simple connected5-regular,D6,bad9792/4350/4524. | Together with saved capacity exclusions and the prior p13 mixed completion, the declared double-reflection A mixed/both families for all three selected groups have no D5. No other A type/group excluded; no further queue.；Together with saved capacity exclusions and the prior p13 mixed completion, the declared double-reflection A mixed/both families for all three selected groups have no D5. No other A type/group excluded; no further queue.；[原始证据](../research/ddp/m1_reflection_nonfaithful/remaining_search/SEARCH_REPORT.md) |
| [F13半直积C28反射mixed族完整有限检查](experiments/ddp-nonfaithful13-mixed-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=728 | 实际D=6，目标D=5；原报告bad（类型见详情）=5278；Existing Wiki Metrics; no experiment rerun；48 skeletons,105456 assignments,all legal and scored; minimum representative misses29. Best full728vertex1820edge graph is simple connected5regular,D6,5278badpairs.；后续结果优先：research-wiki/experiments/ddp-nonfaithful-remaining-20261026.md；Later existing note completes p17/p29 mixed/both branches; the earlier unexecuted statement is historical. | Capacity-preserving normalization and compatible units come from the complete three-group diagnosis. No extra projective normalization or mixed side swap. Only this p13 mixed finite branch was searched; p17/p29 remain unexecuted.；Capacity-preserving normalization and compatible units come from the complete three-group diagnosis. No extra projective normalization or mixed side swap. Only this p13 mixed finite branch was searched; p17/p29 remain unexecuted.；[原始证据](../research/ddp/m1_reflection_nonfaithful/REPORT.md) |

<a id="family-20"></a>
## idea:ddp-m2-hierarchical-cover

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [非正规AGL7两逆对完整范围：仅LL仍失败](experiments/ddp-agl7-two-pairs-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=3200 | 实际D=6，目标D=5；原报告bad（类型见详情）=28224；Existing Wiki Metrics; no experiment rerun；76384728 normalized legalHH inputs;299928 BB passes scored;2 jointhead/blockzero;best roots21/0/0,bad28224allLL,D6,7regular11200edges. | All nonLL pairs can be covered, but every declared two-pair input fails D5. Three-pair HH impossible;zero/onepair remainopen. These conclusions do not exclude the full AGL7 tower or arbitrary3200 graphs.；All nonLL pairs can be covered, but every declared two-pair input fails D5. Three-pair HH impossible;zero/onepair remainopen. These conclusions do not exclude the full AGL7 tower or arbitrary3200 graphs.；[原始证据](../research/ddp/m2_coset_tower/d7_binary_agl7/STRUCTURE_CHECK.md) |
| [非正规AGL8八度塔：2000样本未通过BB](experiments/ddp-agl8-profile-20261026.md) | (8,5)；L=5334；candidate_graph_or_family n=8320；从属目标：[[8, 5]] | 2000 legalHH actualthree-root samples,0BBpass,minBB21;best scored1802752badpairs. Onlypreflight independently fullroot D6,bad6515712;all1024BB targets matchnewtwo-mask formula. | Profile only; huge full family remainsopen and is paused. This does not close other assignments or compositions.；Profile only; huge full family remainsopen and is paused. This does not close other assignments or compositions.；[原始证据](../research/ddp/m2_coset_tower/d8_binary_agl8/STRUCTURE_SCOPE.md) |
| [陪集塔固定425、1066、2257与3200三逆对范围的实际终态](experiments/ddp-coset-towers-20261026.md) | 多目标：F25 fixed tower→[4, 5]／L=364；F41 fixed tower→[5, 5]／L=650；F61 fixed tower→[6, 5]／L=1518；F64 three-pair tower→[7, 5]／L=2810；Z98/C42 fixedtower capacity proof; planned340200 inputs never run→[7, 5]／L=2810（逐变体，不合成一个距离） | d4/F25 all66;d5/F41 valid22932 and HH-scored15190;d6/F61 valid1980573 and HH-scored1671690;d7/F64 three pairs valid1058400,all scored. Independent full edge-list BFS confirms best425 D7/18450bad;1066 D7/42230bad;2257 D6/127185bad;3200 D6/83328bad. F64 best11200edges,7regular,roots48/78/42; independent all3200-root checker0.20992s. Head-zero normalized counts d6=804 and F64=3016; neither family has block-zero among HH passers.；后续结果优先：research-wiki/experiments/ddp-f64-central-quotient-20261026.md；Later existing note closes the cyclic F64 two-pair/two-involution remainder and combines to close that cyclic3200 tower; not faithful semilinear or other towers. | No D5 in any stated finite batch. Necessary HH failures need no full score; best scores have HH-conditioned scope. Fixed425/1066/2257 towers also have separate all-involution exclusions. F64 two-pair/two-involution branch remains open; only three-pair batch exhausted. Separate Z98/4900 tower has a complete paper capacity exclusion including all cost2 block jumps, so planned340200 input search was never executed. Exact six-type group-set route criterion now proved in FULL_ROUTE_CRITERIA.md. No new lower bound, no general-order exclusion.；No D5 in any stated finite batch. Necessary HH failures need no full score; best scores have HH-conditioned scope. Fixed425/1066/2257 towers also have separate all-involution exclusions. F64 two-pair/two-involution branch remains open; only three-pair batch exhausted. Separate Z98/4900 tower has a complete paper capacity exclusion including all cost2 block jumps, so planned340200 input search was never executed. Exact six-type group-set route criterion now proved in FULL_ROUTE_CRITERIA.md. No new lower bound, no general-order exclusion.；[原始证据](../research/ddp/m2_coset_tower/d4_q25) |
| [循环F64剩余分支的中心商完整BB判定](experiments/ddp-f64-central-quotient-20261026.md) | (7,5)；L=2810；条件性n=3200（未据此计纪录） | 13127680 normalized projected inputs;7434370 HH failures;5693310 HH passers;0 BB passers;minimum18 missing blocks. No BH survivors or original C42 lifts evaluated. Saved profile12386-slot prefix continued without repetition. | Center fixes B/H and pairs leaves, so orbit quotient preserves all distances with fixed endpoints; independent saved-graph comparison confirms implementation. All projected multisets have legal original lifts, including duplicated pairs/involutions and identity projection. SCOPE.md proves full coverage. Exact BB obstruction closes all two-pair/two-involution inputs; combining prior other types closes the fixed cyclic3200 tower, not faithful semilinear or arbitrary graphs.；Center fixes B/H and pairs leaves, so orbit quotient preserves all distances with fixed endpoints; independent saved-graph comparison confirms implementation. All projected multisets have legal original lifts, including duplicated pairs/involutions and identity projection. SCOPE.md proves full coverage. Exact BB obstruction closes all two-pair/two-involution inputs; combining prior other types closes the fixed cyclic3200 tower, not faithful semilinear or arbitrary graphs.；[原始证据](../research/ddp/m2_coset_tower/d7_f64_two_pairs/REPORT.md) |
| [忠实半线性F64固定塔：全部生成元组成失败](experiments/ddp-f64-semilinear-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=3200 | 实际D=6，目标D=5；原报告bad（类型见详情）=38976；Existing Wiki Metrics; no experiment rerun；忠实半线性F64固定塔已完整失败：三逆对5058306规范输入、4484088 HH通过、1240 BB通过均评分，最好D6/51072坏对；两逆对两对合41490060合法输入、38982510 HH通过、18524 BB通过均评分，累计89.786032CPU秒。后者最好评分图3200点11200边，独立全部3200根确认简单连通七正则、D6、38976坏对，根缺失24/30/0。至多一逆对由H正规且K/H=C7的280<384容量排除。因此整个指定半线性塔无D5；一般3200点图与其他塔仍开放。零新下界，无新外审或Lean，无当前搜索队列。 | Faithful action removes the cyclic kernel and permits BB and complete head coverage in some graphs, but no tested generator composition completes all routes. Three-pair and two-pair scopes exhaust ≥2 pairs; normal-H/C7 capacity excludes ≤1 pair. Scope is this fixed G,H,K only.；Faithful action removes the cyclic kernel and permits BB and complete head coverage in some graphs, but no tested generator composition completes all routes. Three-pair and two-pair scopes exhaust ≥2 pairs; normal-H/C7 capacity excludes ≤1 pair. Scope is this fixed G,H,K only.；[原始证据](../research/ddp/m2_coset_tower/d7_f64_semilinear/STRUCTURE.md) |
| [3348点忠实循环三角头完整范围失败](experiments/ddp-head-triangle-c31-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=3348 | 实际D=6，目标D=5；原报告bad（类型见详情）=34875；Existing Wiki Metrics; no experiment rerun；18,829,360 inputs;844,697 BB survivors actual3root;D5 hits0. Saved independently all3348roots D6,bad34875 allLL. | SafeC3inversion retainsfixedlayers; complete declared fixedtower scope, notgeneralgraphs. Minbad onlyamongBBsurvivors.；SafeC3inversion retainsfixedlayers; complete declared fixedtower scope, notgeneralgraphs. Minbad onlyamongBBsurvivors.；[原始证据](../research/ddp/m2_coset_tower/d7_head_triangles_c31/REPORT.md) |
| [3348点非忠实循环三角头中心商完整失败](experiments/ddp-head-triangle-c31-nonfaithful-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=3348 | 实际D=6，目标D=5；原报告bad（类型见详情）=111600；Existing Wiki Metrics; no experiment rerun；405000quotientkeys,0BBpass,min12. Eachkey8lifts excluded; no productionliftBFS. SavedindependentD6,bad111600. | Centralz fixesB/H; quotientequalsoriginaldistanceswithB/Hendpoint, notLL. Fixedtoweronly;minBBfallbacknotminbad.；Centralz fixesB/H; quotientequalsoriginaldistanceswithB/Hendpoint, notLL. Fixedtoweronly;minBBfallbacknotminbad.；[原始证据](../research/ddp/m2_coset_tower/d7_head_triangles_c31_nonfaithful/REPORT.md) |
| [6321点循环三角头1200样本无D5](experiments/ddp-head-triangle-c43-profile-20261026.md) | (8,5)；L=5334；candidate_graph_or_family n=6321 | 实际D=6，目标D=5；原报告bad（类型见详情）=384678；Existing Wiki Metrics; no experiment rerun；1200actual3root;BBpass15;headzero19;jointH+B0;bestindependentD6/384678badpairs | All24HHcolor/compositioncells sampled50each;notuniformfullfamilyandnotexhaustive. AlltargetBBmaskschecked. Bestgraphuniqueindependentrebuild/full6321roots.；All24HHcolor/compositioncells sampled50each;notuniformfullfamilyandnotexhaustive. AlltargetBBmaskschecked. Bestgraphuniqueindependentrebuild/full6321roots.；[原始证据](../research/ddp/m2_coset_tower/d8_head_triangles_c43/REPORT.md) |
| [6588点七度三角头必要词筛后完整失败](experiments/ddp-head-triangle-c61-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=6588 | 实际D=7，目标D=5；原报告bad（类型见详情）=4158675；Existing Wiki Metrics; no experiment rerun；1944000originalBBtests,0pass,min36twice. Savedindependentall6588roots D7,bad4158675. | HH/scalar/safeC3inversion and necessaryphasewordbound preservefullfixedtower scope. Savedgraph selectedbyminBB notbadpairminimum.；HH/scalar/safeC3inversion and necessaryphasewordbound preservefullfixedtower scope. Savedgraph selectedbyminBB notbadpairminimum.；[原始证据](../research/ddp/m2_coset_tower/d7_head_triangles_c61/REPORT.md) |
| [43923点十二度Borel三角头192组成样本](experiments/ddp-head-triangle-q11-profile-20261026.md) | (12,5)；L=42342；candidate_graph_or_family n=43923 | 实际D=7，目标D=5；原报告bad（类型见详情）=14133405；Existing Wiki Metrics; no experiment rerun；192actualsamples3fullrootseach,0originalBBpass,1quotientBBpasswith153axisfailures. BestD7,bad14133405. | PROFILE_ONLY: nofullfamilyexclusion. Independentall263538edges andthreeprovedorbitroots, notall43923sources.；PROFILE_ONLY: nofullfamilyexclusion. Independentall263538edges andthreeprovedorbitroots, notall43923sources.；[原始证据](../research/ddp/m2_coset_tower/d12_head_triangles_q11/REPORT.md) |
| [7203点三角头r1完整范围失败](experiments/ddp-head-triangle-r1-20261026.md) | (8,5)；L=5334；candidate_graph_or_family n=7203 | 实际D=6，目标D=5；原报告bad（类型见详情）=3995460；Existing Wiki Metrics; no experiment rerun；HH28894320;quotientpass230496;originalBBpass0;minBB29;diagnosticD6/3995460badpairs | Actualnewaction/trueinversepools rebuilt. ExactBBfails everyquotientsurvivor. Diagnostic selectionminBB,notminbadpair. Scopefixedtoweronly.；Actualnewaction/trueinversepools rebuilt. ExactBBfails everyquotientsurvivor. Diagnostic selectionminBB,notminbadpair. Scopefixedtoweronly.；[原始证据](../research/ddp/m2_coset_tower/d8_head_triangles_r1/REPORT.md) |
| [7203点三角头固定r5塔：必要商过滤与完整BB失败](experiments/ddp-head-triangle-r5-20261026.md) | (8,5)；L=5334；candidate_graph_or_family n=7203 | 实际D=7，目标D=5；原报告bad（类型见详情）=2508408；Existing Wiki Metrics; no experiment rerun；CompleteHHscope28894320; quotientrejected28663824; actualoriginalBB230496; originalBBpass0; one minBB diagnosticD7,2508408badpairs,BB31. | AllHH inputs are covered by the safe normalization and necessary quotient. Quotient pass is not original BB pass. Every remaining original input fails exact BB. All failures after quotientpass lie onfixedaxis v0. Diagnostic is not a global bestbadpair graph.；AllHH inputs are covered by the safe normalization and necessary quotient. Quotient pass is not original BB pass. Every remaining original input fails exact BB. All failures after quotientpass lie onfixedaxis v0. Diagnostic is not a global bestbadpair graph.；[原始证据](../research/ddp/m2_coset_tower/d8_head_triangles/REPORT.md) |
| [K26一因子3/4块连接：对角与循环配对两张完整图](experiments/ddp-hierarchical676-factorization-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=676；从属目标：[[5, 5]] | Both676vertex1690edge graphs simple connected5regular. Diagonal D8/103041badpairs,LL73110 incl73060 cross-index. Cyclic pairing D7/27142badpairs:HH0,HB588,HL1018,BB268,BL8172,LL17096; leafgraph520 and blockquotient130 each connected. | The second candidate changes the actual block-pair matching to break global index preservation while keeping3/4 group multiplicities and16 incidences per block. It is one diagnostic follow-up, not a seed search. Exact head-head coverage survives but other five-step routes fail. Neither candidate improves the public bound or the earlier insertion candidate.；The second candidate changes the actual block-pair matching to break global index preservation while keeping3/4 group multiplicities and16 incidences per block. It is one diagnostic follow-up, not a seed search. Exact head-head coverage survives but other five-step routes fail. Neither candidate improves the public bound or the earlier insertion candidate.；[原始证据](../research/ddp/m2_factorization676/REPORT.md) |
| [676点唯一层次插入候选：完整图D6](experiments/ddp-hierarchical676-insertion-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=676 | 实际D=6，目标D=5；原报告bad（类型见详情）=2172；Existing Wiki Metrics; no experiment rerun；676 vertices1690 edges,simple connected5regular,D6,2172badpairs. HH0,HB6,HL170,BB14,BL776,LL1206; old-old1309,new-old863,new-new0. | The40 removed edges are a matching and all group-head pairs are covered, but other necessary routes fail. One deterministic candidate only; no exclusion of the general mechanism.；The40 removed edges are a matching and all group-head pairs are covered, but other necessary routes fail. One deterministic candidate only; no exclusion of the general mechanism.；[原始证据](../research/ddp/m2_hierarchical676/REPORT.md) |

<a id="family-21"></a>
## idea:ddp-m3-affine-line-cover

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [二元仿射线控制图的必要三角条件与两次反馈](experiments/ddp-m3-binary102-20261026.md) | (6,3)；L=不适用／见变体；controller n=102；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': 816, 'graph_generated': False} | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；自由102点六正则profile缺口2516，76点无三角；固定34三角后无三角点0，容量缺口2800（124对无2/3步路线，102对仅一条2步路线）。各120s，完整控制图和A²/A³独立核对，直径4。 | 每点在三角形是F2³线提升的必要条件，已进入实际生成，但全部短路容量仍失败。两张控制图均不能提升为816点目标；不排除此构造族。；每点在三角形是F2³线提升的必要条件，已进入实际生成，但全部短路容量仍失败。两张控制图均不能提升为816点目标；不排除此构造族。；[原始证据](../research/ddp/m3_binary_capacity_102.md) |
| [仿射线控制器的必要覆盖与实际失败范围](experiments/ddp-m3-control-capacity-20261026.md) | (4,3)；L=不适用／见变体；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': None, 'graph_generated': False} | Recovered810 known edges exactly. Ternary4regular controller needs A³>0 and n≤39. Cyclic3layer m11..17 capacity enumeration0survivors; second implementation agrees. Unrestricted n31/32/33 profiles120s each have4/8/14 zeroentries. Direct binary lifts252×16 and441×16 fail unique3route counterexamples. | Capacity is necessary, never complete fiber coverage. General31–39 controllers remain open. No new lower bound. Latest binary6regularF2³ alternative changes field/degree and must use its own capacity and same-fiber triangle condition.；Capacity is necessary, never complete fiber coverage. General31–39 controllers remain open. No new lower bound. Latest binary6regularF2³ alternative changes field/degree and must use its own capacity and same-fiber triangle condition.；[原始证据](../research/ddp/second_mechanism/DERIVATION_PACKAGE.md) |
| [31点控制图共同端口瓶颈与有界联合SAT](experiments/ddp-m3-control31-joint-boundary-20261026.md) | (4,3)；L=不适用／见变体；controller n=31；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': 837, 'graph_generated': False} | 原图两无序缺孔。2885单交换严格恶化；单侧90/113400端口分配均不改善。88位置16变量边、46固定边、所有961有序对A³>0的联合模型：7326变量23052子句，一次CaDiCaL exit20，result file UNSATISFIABLE。 | 两个端口系统独立调整都被共同唯一路由约束；联合模型仍未找到控制图。SAT为无证明日志的发现级UNSAT，未登记认证排除，不外推一般31点图。继续需改变固定46边中的实际路由，当前不恢复同样随机或端口任务。；两个端口系统独立调整都被共同唯一路由约束；联合模型仍未找到控制图。SAT为无证明日志的发现级UNSAT，未登记认证排除，不外推一般31点图。继续需改变固定46边中的实际路由，当前不恢复同样随机或端口任务。；[原始证据](../research/ddp/m3_control31_diagnosis/REPORT.md) |
| [31点diamond加九三角的固定控制图profile](experiments/ddp-m3-diamond31-20261026.md) | (4,3)；L=不适用／见变体；controller n=31；意图最终提升：{'Delta': 12, 'D': 3, 'savedL': 810, 'n_if_full_lift_valid': 837, 'graph_generated': False} | 实际D=4，目标D=3；Existing Wiki Metrics; no experiment rerun；一个预定profile，145315462次合法交换评分；最好8个A³有序零元，完整31点4正则图直径4。 | diamond使两个共享点各有外部接口，确实改变旧K4/三角链结构；仍不满足必要共同路线条件。仅一次启发式未命中，不排整个拓扑；未运行纤维搜索。；diamond使两个共享点各有外部接口，确实改变旧K4/三角链结构；仍不满足必要共同路线条件。仅一次启发式未命中，不排整个拓扑；未运行纤维搜索。；[原始证据](../research/ddp/m3_diamond31/REPORT.md) |

<a id="family-22"></a>
## idea:ddp-matching-augmentation

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [651点图移动唯一度数缺口的有限邻域](experiments/ddp-degree-deficit651-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=651 | 59坏对图的全部3230合法单步：min61、median109、max138，无改善/中性。两个61最优邻居各自3230步均唯一改善回原59图，其余均>61。 | 只检查源单步及两个指定邻居，不是全部二步或全图排除。精确bitset评分经已知650正例、651源和实际moves全BFS对照；未运行退火。固定源修复暂时停下。；只检查源单步及两个指定邻居，不是全部二步或全图排除。精确bitset评分经已知650正例、651源和实际moves全BFS对照；未运行退火。固定源修复暂时停下。；[原始证据](../research/ddp/degree_deficit651/REPORT.md) |
| [六匹配扩张的共同路径修复profile](experiments/ddp-matching-joint-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=2812 | 实际D=6，目标D=5；原报告bad（类型见详情）=331；Existing Wiki Metrics; no experiment rerun；完整单删边损伤表996145项；旧十例强下界只漏0–2坏对。120CPU profile4542736提案，best强下界330、真实331=295旧旧+36新旧，last339。两图均2812点七正则D6。 | 原G到配对端点的距离给出精确新hub捷径；强下界唯一遗漏是多删边共同损伤。只一次启发式profile，无新下界、无额外seed。；原G到配对端点的距离给出精确新hub捷径；强下界唯一遗漏是多删边共同损伤。只一次启发式profile，无新下界、无额外seed。；[原始证据](../research/ddp/m1_matching_joint/REPORT.md) |
| [2810→2812六匹配扩张十个完整候选](experiments/ddp-matching-ten-20261026.md) | (7,5)；L=2810；candidate_graph_or_family n=2812 | 实际D=6，目标D=5；原报告bad（类型见详情）=364；Existing Wiki Metrics; no experiment rerun；Exactly10 simple connected7regular2812-vertex candidates checked from allroots; allD6. Bestcandidate02 has364badpairs=350old-old+14new-old. DeletedH has514old-oldbadpairs,164repaired. Generation,preprocess,independentcheck total7.344CPU seconds. | Only the predetermined10 candidates were tested, not an exhaustive augmentation search. Across all10 graphs, exact H-distance formulas agree for every old-old and new-old pair. Old-old deletion damage dominates; endpoint selection must combine coverage and path repair. No new bound or further queue.；Only the predetermined10 candidates were tested, not an exhaustive augmentation search. Across all10 graphs, exact H-distance formulas agree for every old-old and new-old pair. Old-old deletion damage dominates; endpoint selection must combine coverage and path repair. No new bound or further queue.；[原始证据](../research/ddp/m1_matching_augmentation/INDEPENDENT_CHECK_REPORT.md) |
| [650源全部两边匹配的非正则651点扩张](experiments/ddp-single-vertex651-20261026.md) | (5,5)；L=650；candidate_graph_or_family n=651 | 实际D=6，目标D=5；原报告bad（类型见详情）=59；Existing Wiki Metrics; no experiment rerun；1319500无序边对中6500共端点非法，1313000合法全部完成；没有新根五步全覆盖者，至少缺19，250匹配达到19。保存图全651根BFS为D6、59坏对，maxdegree5、唯一degree4。 | 该完整固定源构造族均失败；19是全族新根缺失最小值，59不是全族总坏对最小值。最大度目标允许非正则，新点度4合法。独立整数bitset整份覆盖直方图一致。；该完整固定源构造族均失败；19是全族新根缺失最小值，59不是全族总坏对最小值。最大度目标允许非正则，新点度4合法。独立整数bitset整份覆盖直方图一致。；[原始证据](../research/ddp/matching_single_vertex650/REPORT.md) |

<a id="family-23"></a>
## idea:ddp-open-parameter-construction-20261026

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [继承准备期五张已知图的有限检查；零新纪录](experiments/ddp-known-baselines-20261026.md) | 多目标：known baseline→[6, 3]／L=120；known baseline→[8, 3]／L=253；known baseline→[8, 4]／L=1100；known baseline→[10, 4]／L=2485；known baseline→[8, 5]／L=5334（逐变体，不合成一个距离） | Known n=120,253,1100,2485,5334; imported reports say all roots checked by C++ BFS and independent Python bitsets. This session did not rerun them. | 对象：(6,3,120)、(8,3,253)、(8,4,1100)、(10,4,2485)、(8,5,5334)。均为公开已有构造，**零项新纪录**。  120点边表从UPC完整公开数值边表转录；另四张根据公开半直积公式与生成元重新展开。随后两个实现均从展开边表读取：C++全源BFS和Python整数位集的同步可达递推。全部顶点、全部点对检查一致，点数、边数、最大度和直径符合来源参数。  确切输入、源码、逐次结果在项目内`context/DD_PORTFOLIO_START_20261026/baselines/`、`tools/`、`validation/`。未使用抽样、推测对称性或搜索器缓存，没有做新构造搜索或Lean。此处独立指两个代码路径，不是两位独立研究者。  这5图是生成与验证器回归材料，不要求每次会话重跑，不作为“本Goal解决了5道题”。另外7个优先入口尚未在本包独立验算。；对象：(6,3,120)、(8,3,253)、(8,4,1100)、(10,4,2485)、(8,5,5334)。均为公开已有构造，**零项新纪录**。  120点边表从UPC完整公开数值边表转录；另四张根据公开半直积公式与生成元重新展开。随后两个实现均从展开边表读取：C++全源BFS和Python整数位集的同步可达递推。全部顶点、全部点对检查一致，点数、边数、最大度和直径符合来源参数。  确切输入、源码、逐次结果在项目内`context/DD_PORTFOLIO_START_20261026/baselines/`、`tools/`、`validation/`。未使用抽样、推测对称性或搜索器缓存，没有做新构造搜索或Lean。此处独立指两个代码路径，不是两位独立研究者。  这5图是生成与验证器回归材料，不要求每次会话重跑，不作为“本Goal解决了5道题”。另外7个优先入口尚未在本包独立验算。；[原始证据](../context/DD_PORTFOLIO_START_20261026/validation/baseline_verification.json) |

<a id="family-24"></a>
## idea:ddp-polarity585-complete-replication

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [585完全复制扩张的精确阶数上限](experiments/ddp-polarity585-replication-20261026.md) | 多目标：complete-replication bound→[10, 3]／L=650；complete-replication bound→[11, 3]／L=715；complete-replication bound→[12, 3]／L=810（逐变体，不合成一个距离）；条件性n=585（未据此计纪录） | A65/B520;everyvertex has8neighborsB;8N≤520Delta;N≤65Delta sharp. No graphsearch orBFS. | EveryBclassmustremain; originalcompletecrossconnections retained; allowsnonuniformweights,deletedAclassesandextraedges. Nooriginalityclaim.；EveryBclassmustremain; originalcompletecrossconnections retained; allowsnonuniformweights,deletedAclassesandextraedges. Nooriginalityclaim.；[原始证据](../research/ddp/polarity585_replication/DERIVATION_PACKAGE.md) |

<a id="family-25"></a>
## incidence-design layered linker graphs

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [AG(2,3)/K7三层504点全局H交换](experiments/ddp-wave6-affine-linker504.md) | (6,4)；L=441；candidate_graph_or_family n=504；条件性n=504（未据此计纪录） | 实际D=6，目标D=4；普通无序坏对=17073；saved_explicit_graph；最佳504图D6、17073个>4无序对；有限失败不排全部H。 | 固定A/C/CB与任意simple cubic B层H；只2starts×2000合法H交换；需要全局端点覆盖新结构，不能把坏对下降当接近D4或加seed。；[原始证据](../research/ddp/breadth_20261027_wave6/affine_linker504/REPORT.md) |
| [Menon16/6/2×K9：方向类保留模板必要筛](experiments/ddp-wave8-menon1296-screen.md) | (8,4)；L=1100；条件性n=1296（未据此计纪录） | 块外point、不同方向类的B-C必dist≥5；整个指定模板排除D4。 | 固定Menon/K9/B三角形，所有保留四方向类的incidence置换，含每类内任意S9；必须混合方向类；已由一般S36profile跟进，不开a CSP。；[原始证据](../research/ddp/breadth_20261027_wave8/menon1296_screen/REPORT.md) |
| [Menon1296：96独立S36混类置换有限试验](experiments/ddp-wave8-menon1296-unrestricted.md) | (8,4)；L=1100；candidate_graph_or_family n=1296；条件性n=1296（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=69737；saved_explicit_graph；最佳图root唯一全1296源确认D5、69737个>4无序对。 | 全部96incidence独立S36；两固定seed各1000合法transpositions；固定profile停止，不加πmoves/seeds/H自由度或类修补。；[原始证据](../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/REPORT.md) |

<a id="family-26"></a>
## linear-code syndrome/coset quotient

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [线性码Hamming商图：全局covering-radius路由，但27格阶数界均不足](experiments/ddp-wave10-new-structure-scout.md) | 多目标：变体→[4, 3]／L=41；变体→[4, 4]／L=104；变体→[4, 5]／L=364；变体→[5, 3]／L=72；变体→[5, 4]／L=252；变体→[5, 5]／L=650；变体→[6, 3]／L=120；变体→[6, 4]／L=441；变体→[6, 5]／L=1518；变体→[7, 3]／L=170；变体→[7, 4]／L=684；变体→[7, 5]／L=2810；变体→[8, 3]／L=253；变体→[8, 4]／L=1100；变体→[8, 5]／L=5334；变体→[9, 3]／L=585；变体→[9, 4]／L=1768；变体→[9, 5]／L=9020；变体→[10, 3]／L=650；变体→[10, 4]／L=2485；变体→[10, 5]／L=33397；变体→[11, 3]／L=715；变体→[11, 4]／L=3444；变体→[11, 5]／L=37628；变体→[12, 3]／L=810；变体→[12, 4]／L=5832；变体→[12, 5]／L=42342（逐变体，不合成一个距离） | no_new_graph_generated；独立推导diam等于ker(H) covering radius；可交换短词合并为至多D个方向的非零线性组合，n=q^r≤sum binom(s,j)(q-1)^j。有限495项q/s/目标比较覆盖27格，存活0；没有矩阵赋值、码搜索或图。 | 所有标准Fq线性码coset/syndrome图：V=Fq^r，沿H各非比例列方向的全部非零倍数连边；degree=s(q-1)≤12，D∈{3,4,5}。；进一步增加码长度、换H或完美码名称不能绕过统一sphere容量界；新尝试必须改变实际分块/生成边规则并另给路由论证。该入口仍属于广义abelian Cayley相关类，不虚增独立方法数。；[原始证据](../research/ddp/breadth_20261027_wave10/new_structure_scout/REPORT.md) |

<a id="family-27"></a>
## metacyclic base voltage constructions

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Loz–Širáň2008 B/D/T/X原规则门槛筛](experiments/ddp-wave6-voltage2008-scout.md) | (?,?)；L=不适用／见变体 | 无越线；(8,4)=1100仅追平。未试过的完整T(1,1)例D8超范围。 | 原文给定D3/4/5、degree≤12实例与27格保存门槛比较；需有可验证越线参数和覆盖步骤，不能再开群名队列。；[原始证据](../research/ddp/breadth_20261027_wave6/voltage2008_scout/REPORT.md) |

<a id="family-28"></a>
## multi-vertex extension with spoke cooperation

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Tits585批量spoke增阶来源和严格子类界](experiments/ddp-wave3-tits585-batch-extension.md) | (12,3)；L=810 | 所有样本回到旧复制；独立支配组在Δ12总n≤796<810。未排共享spoke/新点互助一般模型。 | 保留585旧核；12个单组贪心仅来源试验，独立二步支配组装填子类另有界；须设计非复制组并用互助覆盖，不仅把组大小8变9/10。；[原始证据](../research/ddp/breadth_20261027_wave3/tits585_batch_extension/REPORT.md) |

<a id="family-29"></a>
## ordinary cyclic voltage covers

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Allwright41(1a)普通C9电压覆盖](experiments/ddp-wave6-cyclic-cover369.md) | (4,5)；L=364；条件性n=369（未据此计纪录） | 根0 self≤5只有{0,±T,±P}五种形式，5<9；整个固定投影不可能。 | 固定Allwright41(1a)全部C9电压赋值；树gauge无损；只有改变base闭路容量才值得继续。；[原始证据](../research/ddp/breadth_20261027_wave6/cyclic_cover369/REPORT.md) |
| [120点D3源的普通C13覆盖](experiments/ddp-wave6-cyclic-cover1560.md) | (6,5)；L=1518；candidate_graph_or_family n=1560；条件性n=1560（未据此计纪录） | 实际D=6，目标D=5；普通无序坏对=31655；saved_explicit_graph；所有槽容量通过；最佳1560图D6、31655个>5无序对，有限profile失败。 | 固定120源、树gauge、两starts各2000单边电压提案；本profile停止，不加底图/层数/seed。；[原始证据](../research/ddp/breadth_20261027_wave6/cyclic_cover1560/REPORT.md) |

<a id="family-30"></a>
## plain tensor products

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [保存因子的普通categorical tensor产品筛](experiments/ddp-wave6-tensor-product-screen.md) | (?,?)；L=不适用／见变体；从属目标：[{'Delta': 4, 'D': 3, 'savedL': 41}, {'Delta': 6, 'D': 3, 'savedL': 120}, {'Delta': 8, 'D': 3, 'savedL': 253}, {'Delta': 12, 'D': 3, 'savedL': 810}] | 7个数值越线组合全部同步walk/奇偶障碍，D4/D5无数值越线组合。 | 保存source orders及oddcycles，2/3因子、目标27格；不含未知因子或修补产品；只有新因子或改变同步路线规则才值得重启。；[原始证据](../research/ddp/breadth_20261027_wave6/tensor_product_screen/REPORT.md) |

<a id="family-31"></a>
## pure Cayley low-degree D3

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [78阶degree5 Cayley入口文献止损](experiments/ddp-wave6-metacyclic78-degree5.md) | (5,3)；L=72；条件性n=78（未据此计纪录） | 拟定16887集合枚举实际0；不是本地新UNSAT。 | 所读文献报告pureCayley(5,3)最优60；本地未独立复核原分类证明；只有可信反例或机制转到非Cayley才值得继续，不重证旧分类。；[原始证据](../research/ddp/breadth_20261027_wave6/metacyclic78_degree5/REPORT.md) |

<a id="family-32"></a>
## record-graph monotone vertex extension

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [37628→37629纪录图单点全R4覆盖有限试验](experiments/ddp-wave4-record37628-single-extension.md) | (11,5)；L=37628；条件性n=37629（未据此计纪录） | best仍漏115个new-old目标，独立multi-source覆盖检查MATCH；未展开新图。 | 全部2504可接旧点R4球；8个起始profile，每个greedy补至11邻居并扫一轮全部坐标；不增加seed/坐标轮数；8是起始profile数，绝非8邻居上限，firstpin也可替换。；[原始证据](../research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md) |
| [42342→42343纪录图单点全R4覆盖有限试验](experiments/ddp-wave4-record42342-single-extension.md) | (12,5)；L=42342；条件性n=42343（未据此计纪录） | best仍漏648个new-old目标，独立multi-source覆盖检查MATCH；未展开新图。 | 全部14396可接旧点R4球；8个起始profile，每个greedy补至12邻居并扫一轮全部坐标；不增加seed/坐标轮数；8是起始profile数，绝非8邻居上限，firstpin也可替换。；[原始证据](../research/ddp/breadth_20261027_wave4/record42342_single_extension/REPORT.md) |
| [37628单点全部2504候选的全局覆盖MILP](experiments/ddp-wave4-record37628-global-cover.md) | (11,5)；L=37628；条件性n=37629（未据此计纪录） | CPU硬限终止，solver未返回，无incumbent/不可行证明，UNKNOWN。 | 全部37628覆盖行、2504二元变量、sum≤11；单solverhandle；该solverhandle已停不重启；如有新结构证据再独立决定。；[原始证据](../research/ddp/breadth_20261027_wave4/record37628_global_cover/REPORT.md) |

<a id="family-33"></a>
## shift/toggle Cayley

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [F2⁶⋊C6 shift/toggle完整参数容量](experiments/ddp-wave6-lamplighter384-capacity.md) | (4,5)；L=364；条件性n=384（未据此计纪录） | phase0全部≤5词仅30形式<64，因此整个指定参数族不行。 | 固定四生成元{t,t^-1,a,b}全部delta,u,v，允许t阶12；须改变phase0路径容量，不搜mask。；[原始证据](../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/REPORT.md) |

<a id="family-34"></a>
## signed/branched double covers

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [170源的signed double加vertical matching](experiments/ddp-wave7-signed-double340.md) | (8,3)；L=253；条件性n=340（未据此计纪录） | 源0→50唯一三路，只给一个sheet；全部signings理论上恰D4。未生成340图。 | 固定170源全部edge signings，全部加fiber内matching；必须使唯一三路能分支，换sign不够。；[原始证据](../research/ddp/breadth_20261027_wave7/signed_double340/REPORT.md) |
| [signed double的matching K2,2分支跟进](experiments/ddp-wave7-branched-double340-capacity.md) | (8,3)；L=253；条件性n=340（未据此计纪录） | 必须击中5130条必需唯一路；任意matching权重≤2810，统一排除。 | 固定170源、branch baseedges构成matching、未覆盖点加vertical、全部signings；只有改变matching分支模板才能重启；不能搜matching或sign。；[原始证据](../research/ddp/breadth_20261027_wave7/branched_double340_capacity/REPORT.md) |

<a id="family-35"></a>
## source-edge deletion and vertex insertion

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [固定104c→105单点四spoke增阶](experiments/ddp-wave2-extension105-d4.md) | (4,4)；L=104；candidate_graph_or_family n=105；条件性n=105（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=8；saved_explicit_graph；20904合法候选全部无D4；bestD5/8。两局部跟进也无改善，best复用同一图验收。 | 固定104c删两条不接边、加一点连其四端点；后续两个局部邻域属于本源跟进；此source已收束，不追加局部自由点或多边交换。；[原始证据](../research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md) |
| [252→254四matching-edge双点增阶](experiments/ddp-wave2-extension254-d4.md) | (5,4)；L=252；candidate_graph_or_family n=254；条件性n=254（未据此计纪录） | 实际D=5，目标D=4；普通无序坏对=133；saved_explicit_graph；bestD5/133，完成有限批次，不是所有四matching扩张穷尽。 | 固定252源四条不接边及方向；8starts×10000提案；固定批次停止，不加seed/删边数/source。；[原始证据](../research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md) |

<a id="family-36"></a>
## spanning edge-deletion degree reduction

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [170/253高次数源的spanning删边降度：全部边已被唯一三路强迫](experiments/ddp-wave10-degree-reduction-scout.md) | 多目标：source170_to_degree6→[6, 3]／L=120；source253_to_degree7→[7, 3]／L=170（逐变体，不合成一个距离） | no_new_graph_generated；170源全部595边与253源全部1012边均属于某条唯一距离3路径，若保持D3则每条都必须保留；根0等所有顶点的必保度分别7/8，超过目标6/7。两项均在必要条件处停止，未生成降度候选。 | 只检查两个固定源的同顶点集任意spanning删边子图；170源降maxdegree6、253源降maxdegree7；不许新增边、删点或重连。；降degree前先查唯一短路强迫边图的最大度；同源只删边不能靠matching优化修复，不能追加该删边profile。；[原始证据](../research/ddp/breadth_20261027_wave10/degree_reduction_scout/REPORT.md) |

<a id="family-37"></a>
## state-shift / de Bruijn graphs

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [无向4字母4位状态移位图256及补边障碍](experiments/ddp-wave3-debruijn256.md) | (8,3)；L=253；candidate_graph_or_family n=256；条件性n=256（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=12354；saved_explicit_graph；实际D4/12354；(27,73)到全部亏度点各至少2步，新增边路线≥5，所有单调补边失败。 | 固定x--(4x+a)mod256去loops/duplicates；全部旧边保留的Δ8补边；必须改变旧边保留约束，不能填度余量继续搜。；[原始证据](../research/ddp/breadth_20261027_wave3/debruijn256/REPORT.md) |

<a id="family-38"></a>
## uniform graph products

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [全部27格均匀lexicographic产品阶数界](experiments/ddp-wave2-lexicographic-products.md) | (?,?)；L=不适用／见变体 | 330个参数对的Moore/degree数值上界筛；无可越线入口。 | G[H]，connected／G／≥2、任意simple／H／≥2；含均匀independent blowup；必须改变均匀产品模板，不能换seed。；[原始证据](../research/ddp/breadth_20261027_wave2/lexicographic_products/REPORT.md) |

<a id="family-39"></a>
## vertex splitting and matching

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [Fano独立集拆点42固定完整族](experiments/ddp-wave5-fano-split42.md) | (4,3)；L=41；candidate_graph_or_family n=42；条件性n=42（未据此计纪录） | 实际D=4，目标D=3；普通无序坏对=45；saved_explicit_graph；全13122候选无D3；最佳显式图D4、45坏对。 | O4中7个Fano点各3种unordered2+2partition及6个固定matching shifts，共13122项；须改变明确模板，不加相同族参数。；[原始证据](../research/ddp/breadth_20261027_wave5/fano_split42/REPORT.md) |

## 计数与来源

本页有152条记录；不以此宣称152种独立方法。原有整轮聚合节点继续保留作历史索引，逐项结果以本账本和对应实验节点为准。

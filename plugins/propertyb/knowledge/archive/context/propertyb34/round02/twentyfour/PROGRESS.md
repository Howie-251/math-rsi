# T34：24点实际分支连接（2026-10-15）

**最新正规结果：r=0完整分支已通过。** `TwentyFourNoLow.propertyB_of_no_six`由真实H24、点对覆盖、恰34边和无六度点推出PropertyB，顶层没有局部表/概率/剖面额外前提。新SparseData2.4秒、SparseBridge14秒；完整CoverageKernel63秒、Actual2.1秒、NoLow1.3秒，最后队列67.82秒成功（1035 jobs）、最大RSS约10.20GB，末端及coverage均标准三公理。日志`TwentyFourNoLow-sparse-build.log`和相应`sparse-build.log`。这一具体疑问已闭合，不再为性能重算或重构已过链。下文早期“r0待验”是历史，六低非单位和其他r分支仍待。独立裸Finset/Bool复述源码`NoLowReviewAudit.lean`已备好，等待主代理实际运行；未冒充独立复现。

执行者为 `resume24_actual`。正式重构建由主代理统一排队；本文所称“轻量通过”是 `lake env lean`，不冒充主工程已构建或完整T34完成。

## 无六度点分支 r=0

结构链已经全部实现并轻量通过：

1. 170总度与最低度7给七度点数22或23。
2. 同一实际共度超额图中消去两部分之间的共同交叉项，内部有向能量分别至多98或102。22个七度点时另两点均八度，若它们共度≥5则由已验双锁直接染色。
3. 一般有限图不等式 `|S|² ≤ k(|S|+energy)`（无k+1独立点时）给五个单位共度七度点。
4. 五点总超额25，外部至少17个七度点，故有第六点与前五点的总超额≤1。
5. 实际重标号为全共度1，或仅01对共度2的六个七度锁。
6. 352/467个完整有标签高迹输入，经实际置换匹配到旧46个严格数值代表；真实低阶上计数与高迹恢复原H全部迹，然后单布局接口返回原染色。

源码：`TwentyFourSparseGraph.lean`、`TwentyFourStrongCodegree.lean`、`TwentyFourNoLowSelection.lean`、`TwentyFourNoLowSix{Data,Numeric}.lean`、`TwentyFourNoLowSix.lean`、`TwentyFourNoLowCoverage{Data,Kernel}.lean`、`TwentyFourNoLowActual.lean`、`TwentyFourNoLow.lean`。

已验：SparseGraph和StrongCodegree正规build通过，标准三公理；NoLowSelection轻量通过，标准三公理。46份旧单布局证书经精确Python重放通过，最坏15907/15912。后续Data/Numeric/Coverage/Actual/最终wrapper尚待正规构建反馈，不能称r=0已验收。

性能选择：`upper`直接存空迹34、单点7与一/二共度，不在819个输入每次重复算64项上计数；它与μ的恢复关系仍由Lean kernel逐项核验。稀疏标签ID用List.lookup；不使用巨大Nat模式匹配。

## 至少六低且有非单位低对

从实际六度集合中保留给定坏对，再取四个点；六度点的唯一非单位伙伴性质保证其余坏对也不交。四点匹配的64个图完整规范化后得到1、2或3条共度2边。

`TwentyFourSixLowPairPatterns.normalize`和`TwentyFourSixLowSelection.exists_labeled`轻量通过，标准三公理；组合调试日志为`six-selection-debug.log`。旧181份单布局证书已精确重放，最坏48617/48620；原始完整高迹域467/611/787，已生成覆盖映射。数据、数值、覆盖和Actual模块已落盘，但尚未构建，后续复用r=0接口修法。

源数据为第一小时的`MIXED_SIX_v24_low6_bad3.json`、`...bad3_12.json`、`...bad3_12_48.json`；不重搜布局。

## 全24点的准确剩余

仍需：r=1–4分支的七/八锁完整提升；r=5分支及其对25点通用九锁q=5引理的调用；r≥6全部单位低点时的实际唯一坏槽、多布局/共同三元结构连接。当前新增代码没有闭合全部24点，也没有证明完整T34。

生成器与精确复放记录都在本目录。原始失败调试文件保留为诊断；只以exit0的具体模块及正式构建日志为形式验收依据。

## 本轮实际性能证据与表示修正

首次正规NoLow队列中，Selection 8.3秒、SixData 39秒、46份SixNumeric 261秒、Six实际caller 1.2秒全部通过。随后CoverageData运行572秒仍未结束，由主代理精确终止（exit143），旧队列失败不计覆盖通过；日志`TwentyFourNoLow-build.log`保留。该队列记录最大RSS约10.5GB。

最初把720个置换存成嵌套向量，再用一个kernel命题逐个证明Injective。Array替换的小探针也出现高内存，已主动停止，不能宣称Array加速成功。最终改为`TwentyFourPermutation.perm`：factoradic索引对应五个`Equiv.swap`的复合，结果天然为Equiv，不需重新核验720个函数的单射性。该模块及前向实际计数定理`count_comp`轻量通过，标准三公理。Python生成器的同向映射仍输出完整352/467域；候选代表与数值证书均未改变。覆盖的最终Lean核验尚待重跑。

新候选数据的进一步算术优化使用已验`CachedRows.rows_eq`，把原A/B/C等价改成六个剩余大小的质量和，避锁配额罚项仍保持原实际槽式。尚未构建的181份六低非单位证书已采用此表示；已经通过的46份不为性能猜测重新核验。

factoradic表示的实测：`ActualInlineProbe.lean`内联新CoverageData，再把覆盖结论显式作为参数调试实际caller，5.74秒exit0，进程组峰值约2.18GB，标准三公理。Data解析和Actual API均已可用；这份探针是有参数的调试命题，不是完整r=0验收。正式源码仍直接导入CoverageKernel，不保留探针参数。记录`actual-inline-probe.log/json`。

这里不需要证明factoradic函数枚举了全部置换：分类完整性由实际迹进入`BoundedAllocations.enumerate`和每个目录输入的`Matched`承担；存储的重标号只是该输入的一个见证。所需义务是每个见证确为置换、实际计数按正确方向运输、每个实际输入都匹配成功。五swap结构性保证第一项，`count_comp`保证第二项，CoverageKernel核验第三项。Python中720个像互异只是生成器自检，不承担Lean证明义务。

## 2026-10-15 续接：六低非单位实际接口与共同高点

`TwentyFourSixLowBadComplete.propertyB_of_nonunit_low_pair`已写成实际分支端点：H24、点对覆盖、34边、至少六个六度点和一个非单位低对，直接推出PropertyB。中间所有选点、matching标签、实际高迹容量、恢复与181证书均由内部调用构造。`unit_of_not_propertyB`供剩余全单位低点分支使用。181证书数值层使用已证`CachedRows.rows_eq`，保持原严格公式与quota扣除；数据/数值/覆盖/实际完整链等待主代理正规构建，不记为已验。详细审阅范围`REVIEW_SIX_LOW_NONUNIT.md`。

新增`TwentyFourCommonSevens.lean`已单文件轻测exit0，末端公理仅标准三项，日志`common-sevens-debug.log`。Q为七度点减去所有六度点的坏伙伴并集，证明`|Q|+3r≥22`，故r=5有至少7个共同单位高点，r=6有至少4个；r=5时任意x∈Q还有另一个y∈Q与x共度一。该结果是真实H上的结构选择，不依赖概率证书，也不表示r=5/6完整分支已完成。

## r0第二次覆盖性能修正：显式见证与稀疏support

五swap结构解决了720函数单射检查，但旧CoverageKernel仍在17分26秒、约4.3GB时被主代理TERM。其每个输入在遍历64种T时反复计算choose的长lookup及高迹decode，不能继续等原实现。新实现为`TwentyFourNoLowSparseData/Bridge`与更新的CoverageKernel：rows直接存实际41位分配编码/case/perm，证明解码rows恰等于完整352/467目录；每行核对二值性、extraPair、必要的01保持和稀疏高块集合相等。`TwentyFourSparseDecode.decode_indicator`一般证明将support相等恢复成全部高迹函数相等，低阶通过置换保空集/单点/指定点对恢复。最终Actual从coverage直接取见证，无lookup，仍返回原H的PropertyB。

非平凡5条固定choice+原逐64检查为7.81秒、2.49GB；5条稀疏support探针3.04秒、2.00GB。显式819×41个Nat列表的inline10条探针18.58秒，遂改固定41位解码；新完整Data+5条编码检查3.82秒、2.03GB。日志均为`nolow-*-pilot.log/json`，不混同完整覆盖已通过。新的Actual条件探针`nolow-sparse-actual-api.log/json`为3.01秒、2.27GB、标准三公理。46型profileHigh对μ的核验、完整rows覆盖及逐行CheapMatch待主代理正规构建；该分支未验收。

规范新生成器为`generate_nolow_sparse_coverage.py`；旧`generate_nolow_coverage.py`仅作为旧Data与数学输入的来源及历史实现保留，不再用其旧Kernel模板覆盖新实现。`generate_nolow_sparse_coverage_explicit_values.py`保留显式大列表实验。不存在编码单射性作为隐藏前提：rows的实际解码值与完整目录相等、并逐行绑定实际置换，即足够。

## 六低非单位稀疏改造：短pilot已过，完整构建待排

新增`TwentyFourSixLowBadSparseData/Bridge`，其完整见证域仍为467/611/787，181原概率证书未变。CheapMatch同时比较非单位点对集合和高迹集合在同一个真实置换下的像；一般support解码引理与低阶上计数公式将其提升为全部实际low/high等式。CoverageKernel改为完整rows一次等于catalogue、逐行SparseMatch，再通过List.mem_map返回明确case/perm。Actual已改为直接接收这个见证，Complete原H结论不变。

选择5条较复杂的真实目录输入做短pilot：case179含6个高块，两条不同标签；case174含5个高块，三条不同标签。原始ID与置换在`SIX_LOW_BAD_SPARSE_PILOT.json`。`sixlow-bad-sparse-pilot-r3.log/json`为exit0，10.21秒、组峰2.26GB，通用桥公理仅标准三项。探针仅内联BadCount等轻数据，以显式profile_high_correct参数调一般桥；正式Bridge另有181型μ/support的内核核验，没有该参数。181数值、完整域和实际末端仍待主代理正规构建，不能把这5条当全支PASS。生成器为`generate_sixlow_bad_sparse_coverage.py`，旧lookup生成器不再生成当前Kernel。

## 181六低非单位支：数据正规通过，恢复与数值独立分块

`TwentyFourSixLowBadData`新表示正规69.82秒PASS。完整181位置单射按case核验、μ稀疏Nat表、R/quota共享同一值；原恢复义务移至六个Recovery块，未删除。Numeric按十case拆成19块，再组合原certificate接口。详细顺序、实测与失败边界见`SIX_LOW_BAD_BUILD_MAP.md`。当前这仅是Data验收，完整恢复、181数值、1870输入覆盖及原H端点仍待正规构建；NoLow链保持冻结。

## 六个单位低点：9型实际分类轻量完成

`TwentyFourSixLowUnitData`单文件轻测PASS9.09秒/3.28GB；与`TwentyFourSixLowUnitActual`完整内联轻测PASS10.20秒/3.39GB，导出`actual_classification`仅标准三公理。它从真实H24、34条边、六个六度点且两两共度一，返回九种完整μ之一及真实重标号；复用已过NoLow的完整352高迹域，不重做分类搜索。正规Data→Actual两模块尚待主代理队列；没有导出该分支的Property B，因为五类严格槽平均及四残类的共同高点论证仍需连接。原候选入口为`context/propertyb34-reader/CHAPTER_24_25.md`的相应两节；槽平均源`context/propertyb34-hour1-20261013/high-math/SIX_LOW_ACTUAL_AVERAGE.json`、`AUTOMORPHISM_AVERAGE.json`，只读定位，未重新搜索。

## 2026-10-15 continued unit-low branch

The six-unit-low actual classification remains the complete nine-type classification; this is not yet the full unit branch.

- Added `TwentyFourSixLowUnitFiveBlock{Data,Numeric,}.lean`: original group 6, bound 47649/48620, full actual-counts-to-PropertyB call. Combined lightweight probe PASS 10.02 s / 3.16 GB, standard three axioms. Regular build requested.
- Added generic `TwentyFourSlotAverageTable` and `TwentyFourSlotAverageCache`, connecting a finite table of fixed actual bad-pair slots to the existing slot-average coloring argument. Combined API light probe PASS; cache API also exercised by numeric probes. Actual slot remains fixed across layouts; exchanging its two edges is accounted for.
- Exported original unit groups 2, 4, 7 to Data/Core/Rows/Slots/actual modules with 48, 25, 12 layouts respectively. The old source relabeling for automorphism averages is absorbed into the explicit positions; original canonical counts are retained. Fraction replay exactly gives 11954/12155, 242899731/243095138, 12107/12155. No layout search performed.
- Group 7 Data/API/Core, including all admissible slot coverage and final average, light PASS 8.40 s / 2.91 GB. First five layouts' full ABC/free equations PASS 15.97 s / 3.35 GB; first layout's 47 slot contributions PASS 5.69 s. Full regular build remains pending.
- Group 4 first-layout ABC/free PASS 10.54 s / 2.95 GB. Its initial monolithic final average reached the 4 GB pilot ceiling, so it is not counted as PASS; data_valid (7.64 s) and complete slot coverage (9.52 s) separately PASS. Final bound arithmetic is being split per slot.
- Group 2 first-layout inline pilot hit 20 s at 2.48 GB, not PASS. Its 48-layout Data elaboration is the main extra prefix cost; all rows and slots are already split into batches of at most five.
- Added `TwentyFourSharedSingletons.at_most_three`, generic in vertex and low-lock counts. If three pairwise-unit high vertices all use singleton-low edges at each designated low label, and each such singleton fiber has size at most two, there are at most three designated low labels. Proof injects labels into the three high pairs. Lightweight PASS 2.16 s / 1.91 GB, standard three axioms. This unifies the triple-high contradictions for residual unit-low types 3 and 5; actual one/two-high classification still must establish its premises.

Remaining mathematical interfaces: unit type 0 average; the complete original 131 first-high promotions and their strict certificates/17 strict mixed certificates; second-high classification and three-high contradiction; the >=7-low seven-lock residues; r=1..5 branches. Existing sources and exact scope are in `CANDIDATE_SIX_LOW.md`, `CANDIDATE_SEVEN_LOW.md`, and `CHAPTER_24_25.md`. Bad181 full-chain regular builds remain with root. No full 24-point theorem is claimed.

Group 4 final-average repair: split the universal slot inequality by `fin_cases`, leaving every original rational formula unchanged. Full Data+API+Core then PASS 15.84 s / 2.64 GB; first layout's all 54 slots PASS 7.69 s / 2.67 GB. Regular group4 chain requested; sources frozen. Group2 Core adopts the same per-slot arithmetic split.

## Stop checkpoint, 2026-10-15

Parent requested no further implementation/probes while the user considers pausing T34 Lean. All subagent processes ended. Authoritative detailed checkpoint: `PAUSE_CHECKPOINT_20261015.md`.

Latest parent regular Bad results: all181 Numeric/Recovery/Bad PASS; CoverageData10.02s, SparseData9.09s, SparseBridge30.32s PASS; CoverageKernel240s timeout, NOT PASS. Actual/Complete not accepted.

Unit0 has exact120-layout compression with original2203/2210 bound, integer dense tables, independent profile-binding chunks and one-reference-profile row compression source. Data+first row lightPASS18.31s; Data+first profile binding lightPASS13.76s. Full Core/Rows/Slots/Profile remains pending. Generic row-congruence lightPASS2.16s. Unit2/4/7 ready modules and exact pilot scope are in checkpoint. Aggregate `TwentyFourSixLowUnitStrict` is source-only pending these dependencies.

Residual type3/5 shared singleton contradiction and binary A/B triple contradiction lightPASS3.94s. `TwentyFourUnitPromotionBase` exact decoded codegree/unit-promotion bound lightPASS2.16s. First-high131 actual catalogue itself not yet generated or implemented. No full24 theorem or new final-review status is claimed.

# 23点低度分支续接（2026-10-15）

目标是完成真实H23、点对覆盖、34条边、至少七个六度点的完整染色分支，随后复用六低残型处理恰六个低点。现有完整23点尚未完成。

## 已有实际核验

- `TwentyThreeSevenLowCounting.exists_deletion_not_two_triple_trace_shape`：对任意五元H和任意七点W，某次删除不满足“所有迹≤3，恰两条实际边产生三元迹”。按原始边计数，不假设迹互异。轻测 `seven-counting-r2.log` exit0，4.63秒、标准三公理；主代理随后正规构建通过。
- `TwentyThreeFourLowCatalog.actual_representative[_perm]`：从真实H23/34边/点对覆盖/任意四个六度锁，推出完整50型。复用旧T33的464输入分类，只证明空迹增加一；未重跑该域。轻测 `four-catalog-r2.log` exit0 2.19秒；主代理正规构建包含perm版本通过。
- 42个严格四低型：38项单布局及4份联合证书，主代理正规构建通过。实际调用者 `TwentyThreeFourLowStrict.propertyB_of_counts` 和 `TwentyThreeFourLowJoint{3,19,20,21}.propertyB_of_counts`。
- `TwentyThreeFourLowClassified.actual_residual`：42个严格型内部排除，保留8个残型，返回同一实际四锁的置换。轻测 `four-classified-r3.log` exit0 11.14秒标准三公理；主代理正规重构建已通过。
- `TwentyThreeLowPromotionBase.actual_mem`：对新增六度点，同时限制度数6、各共度≤3、总共度≤n+2的容量剪枝完整性。`feasible_actual`提供实际所有共度超额≤2。轻测 `low-promotion-base-r3.log` exit0 1.97秒标准三公理；主代理正规构建通过。

## 已写出、待核验的完整连接

依赖链：`FiveLowPromotionData/Numeric/actual → FiveLowClassified → SixLowPromotionData/Numeric/actual → SixLowClassified → TwentyThreeManyLowComplete.propertyB`。

最后的 `propertyB` 原始分支签名只有H23、点对覆盖、34边与至少七个六度点，没有残型/分类/概率证书前提。当前只是源码待核验，不能据签名宣称证明完成。

5/6低严格证书已从原JSON导出并独立复算，无布局搜索：五低9个单布局和1个20布局联合；六低2个联合（9及14布局）。生成器 `export_five_six_low.py`；范围/结果 `FIVE_SIX_LOW_CERTIFICATE_EXPORT.json`。其四锁专用恢复字段已移除，保留一般actual-count调用。

完整promotion生成器 `generate_low_promotions.py`：4→5共3573个容量向量，901满足实际所有中心预算，54个所有四投影均残型，压到原12型；5→6共4863个容量向量，780满足预算，13个所有五投影均残型，压到原3型。与原完整域一致。每个不合法残型只附一个具体拒绝投影，内核验证“该投影仍属旧残型则得到新代表”的蕴含；实际调用用同一H上的旧分类消去该条件。未运行整图枚举。

## 下一动作

主代理唯一正式构建者顺序构建：FourLowClassified、LowPromotionBase、FiveLowPromotionData（先测试表示）、Numeric（主耗时）、actual、FiveLowClassified，再Six对应链与ManyLowComplete。子代理仅调试轻量actual接口，不并发大表。

若覆盖核验成本高，先profile第一张coverage；不直接扩大信任或使用native_decide。数据、数值表和actual模块已拆开；大Nat键用查找表，避免数值模式匹配展开。已有成功证书勿重搜。

## 补充接口与导出修复

- `TwentyThreeTraceShape.shape_of_counts` 将任意 Fin n 锁的真实重数与“正重数仅出现在≤3迹、三元迹总数2”连接到原始边集合的 `TwoTripleTraceShape`。包含重复迹的多条原始边均保留。轻测 `trace-shape-r1.log` exit0，1.93秒，仅标准三公理；主代理正规构建已通过。最终 ManyLowComplete 改为调用该轻量通用接口。
- 5/6/7 锁数值导出器最初的 μ 函数捕获了旧四锁 `fs`，导致高标签截断，Lean 在 `p_eq_computed` 处拒绝；现已与其他函数一起按 K 重绑定，重新导出所有相关数据。修复后 `TwentyThreeFiveLowStrictData` 单文件 exit0，3.14秒，见 `five-strict-data-r2.log`。数值证书自身仍待正规构建。
- `TwentyThreeSixLowExtraSelection.exists_seventh` 已从真实 H/恰六个六度点推出一个七或八度点，其对六低点的共度超额和≤1；不需假定六低之间共度均为1。轻测 exit0、1.96秒，`six-extra-selection-r1.log`。

## 实际 4→5 接口已单独调通

主代理已正式构建 `TwentyThreeFiveLowPromotionData`。`FiveLowActualProbe.lean` 只将容量目录 `coverage` 设为显式参数，对生产 actual 代码的其余部分进行真实检查；`five-actual-probe-r3.log` exit0、2.48秒、标准三公理。它验证原 H 的实际 promotion 入域、全部重数恢复、同 H 上的删除投影、四低分类及置换提升。该探针是接口核验，完整结论仍等待内核证明目录 coverage；生产 actual 没有加入参数或 axiom。

当前顺序冻结：不再增加局部证书，先 profile `FiveLowPromotionNumeric.coverage0`；若表示可行则完整5低覆盖+概率→6低覆盖+概率→最后4b=14。上述链已具备全部纸面/精确数据，尚未宣称端到端分支通过。

终端实际装配的 `ManyLowActualProbe.lean` 也通过：唯一 six classifier 为显式参数，其余 Fin6 标号、原始边迹、任意六子集到 4b=14 及 PropertyB 全用生产代码，`many-low-actual-probe-r1.log` exit0、2.40秒、标准三公理。生产 `ManyLowComplete` 仍无该额外前提，等待实际分类链编译。


## 覆盖核验缓存边界

为避免 pilot 通过后重复整表，覆盖按旧残型分独立模块：`FiveLowPromotionCoverage0…7`、`SixLowPromotionCoverage0…1`；对应 `Numeric` 只导入和汇总。正式构建必须逐 coverage 串行，缓存齐后再 build Numeric，避免 Lake 同时启动八份重表。生成器已同步，既有 Data 源未改。

修复标签后，其余严格数据轻测均通过：`five-joint-data-r1.log` 4.26秒、`six-joint0-data-r1.log` 5.54秒、`six-joint1-data-r1.log` 5.25秒。这只验证数据/计算剖面绑定，数值严格界仍由正式 Numeric 内核核验承担。


## 已采用整体缩减：六锁只用五锁大小谱

主代理同意后已把5→6的删除条件从完整五锁残型改为大小谱必要条件，详见 `CARD_SPECTRUM_REDUCTION.md`。完整780可行输入仍恰剩13个、3轨道；4→5只用谱会多留195例，因此保持原条件。生产 Data 移除120个旧置换和未使用的新置换，仅保存实际13个新置换。通用谱不变引理轻测1.97秒；新6低Data与全部actual接口条件探针3.49秒通过、标准三公理。生产模块仍等待正式旧分类与目录内核核验，不把探针算作完整分支。


## 四低提升进一步改为一二阶矩（当前版本）

单用大小谱4→5会多留195例；加上每种迹大小的重数平方和后，完整901输入恰剩原54个。已实现通用 `cardMoment_map/relabel/of_relabelled_counts`，任意矩阶/锁数成立；生产5低目录与actual改用一二阶矩条件，6低保持一阶谱。存储的新置换分别32与13个。详见更新后的 `CARD_SPECTRUM_REDUCTION.md`。

旧full残型 coverage0 在4分54秒未完成被主代理终止（最终Lake307.47秒/exit143），新版本尚待正式pilot。新FiveLowMomentActualProbe包含完整新Data/实际调用，仅coverage参数化，4.80秒、标准三公理通过。不会把取消、精确Python复算或条件probe当正式coverage通过。当前先更新TraceShape与FiveLowPromotionData缓存再核验Coverage0，之后串行其余分块。


稳定版额外把旧残型期望矩/谱缓存成小常数表并用 `expected_correct` 内核绑定。
5/6 Data+actual 最终probe r2分别7.91/4.96秒通过；实际源码冻结等待新Coverage0 profile。

## 当前：显式行和稀疏投影证书（2026-10-15）

矩版 Coverage0 仍在180秒内未完成，已由主代理精确停止，不能记PASS。重复主要来自：每行反复查901项`choose`、同一`newCounts/extend/decode`在全部共度和投影矩中展开，以及`projected`每个目标迹再次扫描全部源幂集。旧源码生成器快照保留于`generate_low_promotions_before_rows.py`。

现已消除 lookup，`covered`改为**存在显式删除点/代表/置换**，actual从已验证行取出该见证；不再从Nat大键反复查找。每份Coverage有显式 `(promotion values, Reason)` 行及独立 `catalogue = rows.map Prod.fst`，完整容量域没有缩小。`Reason`仅核验该行需要的一种义务：共度为0、中心excess大于2、某删除投影的一二阶矩/大小谱不符、或最终代表等式。

`TwentyThreeSparseTrace`新增任意锁数/投影维数的通用桥：稀疏weighted list允许重复key，投影后重数相加；`projected_counts`与原幂集和严格相同，`moment_eq`把正次矩限制到实际support，`moment_zero_eq_cardMass`连接大小谱。因此稀疏实现仍计算真实重数，未把重复投影当成不同类型。

最新轻量证据：
- 一般稀疏桥`SparseTrace`：2.22秒、标准三公理。
- 新五低Data与一般桥：3.84秒，`sparse-five-data-r1.log`。
- 5条末端非平凡行覆盖四种Reason：5.53秒、1.80GB，`sparse-five-5rows-r1.log`。这是短pilot，不外推整表耗时。
- 新五低actual条件探针：4.95秒、标准三公理，`five-sparse-row-actual-r1.log`。只将正式coverage设为参数，生产模块没有额外假设。

正规构建已新增FiveLowStrict PASS约33秒、SixLowStrictJoint0 PASS约45秒。20布局FiveLowStrictJoint3与14布局SixLowStrictJoint1各180秒仍未完成，已取消，主代理安排一次较长有界构建；不得当作失败数学证书或PASS。后续仍先稀疏Coverage0实际profile，再决定余表串行策略，最终5→6→≥7实际链尚未验收。

新六低Data＋actual条件探针也已通过，`six-sparse-row-actual-r1.log`，4.54秒、1.51GB、标准三公理。新表示的专门跨模型审阅义务在`REVIEW_SPARSE_OBLIGATION.md`；与原矩/大小谱数学缩减的`REVIEW_MOMENT_OBLIGATION.md`分开保存。

### 正规队列后续结果

主代理已报告 `SixLowStrictJoint1` 正规PASS，317.4秒；两份六低联合严格证书现已齐备。五低纯型也PASS，剩五低20布局Joint3的数值实现由24点代理在独立CachedNumeric中优化，原数值文件不改。新SparseTrace/Data随后正规构建，Coverage0按180秒上限进行首次整体实测。不得重启已通过六低证书。

15条Coverage0尾部行短测也PASS，5.33秒/2.12GB（5 zeroPair、5 matched、5 projection；该旧型没有excess行），见`sparse-five-20rows-r1.json/log`；文件名是预期20，实际数量为15，不将命名当数量证据。

另补通用 `TwentyThreeHighPromotion.complete_actual/extend_actual_of_high`：已知所有≥2旧迹promotion与新增点到旧点共度后，singleton promotion由λ减higher和恢复，empty再由新点度数恢复。4.23秒轻测PASS，标准三公理。计划用于恰六低点下一支的真实高迹入域，未改当前5/6覆盖、更未新增完整分支验收。

### 稀疏全表首测已通过

主代理正式构建最新 `TwentyThreeSparseTrace`、`TwentyThreeFiveLowPromotionData` 均PASS；**FiveLowPromotionCoverage0完整731行、catalogue精确绑定与每行验证PASS，41.69秒**，日志`TwentyThreeFiveLowPromotionCoverage0-pilot-build.log`。这不再是少量行pilot，仍只覆盖八个旧残型中的第0个。实现已冻结，不再优化已通过版本。后续顺序为Coverage1…7→FivePromotionNumeric/actual→五低严格Joint3→FiveClassified→SixPromotionData→六低Coverage0/1→SixPromotionNumeric/actual→SixClassified→ManyLowComplete。主代理唯一串行执行；六低表1835/3028行的耗时另以实测为准。

### 完整4→5实际连接已正规构建通过

回读主代理 `*-complete-build.log`：Coverage1…7全部PASS，对应Lean约16/5/24/10/37/23/10秒；此前Coverage0 PASS约40秒。完整3573容量向量的catalogue绑定、逐行证书和4→5真实调用现已闭合。`FiveLowPromotionNumeric` PASS1.2秒、`FiveLowPromotion` PASS1.9秒（Lake墙钟2.30/3.05秒）。主声明 `TwentyThreeFiveLowPromotion.actual` 已从真实H/34边/点对覆盖/任意五个六度锁/¬PropertyB推出十二代表中的实际重标号计数，不再依赖外部coverage参数。

这仍不等于≥7分支：五低20布局Joint3等待Cached实现接线，之后五低残型分类→六低覆盖→六低分类→ManyLowComplete。旧probe和首测状态保留为历史，不覆盖本段正规结果。

### 五低分类闭合；六低全表改成独立64行块

主代理正规确认五低Joint3的CachedNumeric分块全PASS（总约62秒），实际caller已经定点切换，旧Numeric保留。`FiveLowClassified` PASS4.82秒、`SixLowPromotionData` PASS2.76秒。六低Coverage0完整1835行仍在180秒内未结束，主代理精准停止；Coverage1尚未运行，不能记PASS。

沿用21点有效办法：完整1835/3028行分别拆为29/48个64行块，既有Data与每行Reason原样不变；聚合单独核验一次完整enumerator等于所有块输入拼接，并以List.all_append连接已验行。首块正式源单文件轻测4.86秒/2.04GiB PASS，见`six-coverage-block0-r1`。正规串行清单为`SIX_COVERAGE_SERIAL_MANIFEST.txt`，生成器`split_six_low_coverage.py`已经接入原生成器。此处尚不是77块全验结果。

恰六低支并行准备：`TwentyThreeHighPromotion`将singleton由共度恢复、empty由度数恢复，只枚举9个二迹+2个三迹。实际第七点保证共度全1或一处2，完整容量域每度331=6×49+37，复用原36份代表/证书，没有新布局搜索。`actual_extension`仅把coverage设参数的真实输入探针4.41秒PASS，标准三公理；新表尚未核验、完整恰六支尚未验收。

### ≥7六度点完整实际分支正规PASS

主代理报告77块、两个完整容量域聚合、SixPromotionNumeric、SixPromotion、SixClassified、ManyLowComplete全部正规PASS（队列共86 targets）。最终`TwentyThreeManyLowComplete.propertyB`约3.08秒，传递公理仅标准三项。该声明只假设原23点H、点对覆盖、34边及至少7个六度点，不再有局部残型/覆盖/证书前提。主代理正在独立裸Finset/Bool复述并缩小Assembly剩余到≤6六度点。

恰六低完整actual接口已完成条件探针：`six-extra-complete-r6`5.12秒；加入稀疏恢复公式后`six-extra-sparse-complete-r1`6.30秒、标准三项。三个准确待验接口仍是六低实际分类（现已正规闭合）、新增331项覆盖、36型严格概率结论。新通用`SparsePromotion.extendSparse_eq`把高阶求和限制到11个支撑、非空总和限制到17个支撑，2.92秒一般证明PASS；不会丢掉零类型或把无放回计数改成独立模型。

### 恰六低：先做真实自同构规范化，再核验86项域

两行331域pilot原10.91秒，稀疏公式10.13秒，收益有限；8行短探针20秒边界停止，未宣称大加速。随后作实质的无损减域：唯一六低残型的六个实际自同构保持全部oldCounts，并在六点上传递。lift固定第七点，将可能唯一双共度点改为标号0；最终锁置换合成回原H。仅需none的37项和some0的49项，86项完整域；五个其他double位置不进入验收依赖。

`normalizer_preserves`、`normalizer_pairs`及完整归一化actual链轻测`six-extra-normalized-complete-r2` PASS7.31秒/2.29GiB、标准三项。生产`actual_extension`仍接受所有b，内部完成规范化；`TwentyThreeExactlySixLowComplete.propertyB`仍只接受真实H、PairCovering、34边及恰六个六度点。新有限覆盖和严格证书仍待正规队列，不能提前记该支完成。

最短正式清单`EXACT_SIX_SERIAL_MANIFEST.txt`共46 targets，包含86向量的12个8行块及两个完整catalogue绑定，17/18纯型证书、31布局联合证书的8个四布局缓存块与7个精确非零罚项核验。联合actual已转到新CachedNumeric，旧Numeric和旧非规范位置源保留，未重跑其巨式。数学审阅义务集中在`SIX_EXTRA_HIGH_PROMOTION.md`。

### 2026-10-15 用户暂停 T34 Lean

精确暂停边界和恢复顺序见 `PAUSE_CHECKPOINT_20261015.md`。恰六低 Extra7Numeric 正规 180 秒 timeout，未继续诊断；r2 通用角色矩/实际接口仅有轻测，后续源尚未验收。≥7 低分支的正式 PASS 保持。依用户新授权，数学诊断另写 `context/propertyb36-40-diagnosis-20261015/middle/REPORT.md`，不恢复旧 Lean Goal。

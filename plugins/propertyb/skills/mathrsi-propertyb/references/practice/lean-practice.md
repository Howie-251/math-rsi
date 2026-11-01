# Lean 实务：把同一实际 H 接到原染色

本页依据项目实际源码与性能记录，专门处理已遇到的工程失败。不会运行旧35 Lean或恢复36研究。需要新形式化时读取当前 `lean-formalize` 技能并服从当前任务合同；归档代码固定为Lean4.24.0/对应Mathlib，不把全局最新版API强套进去。

## 1. 先做一个非平凡 actual caller

有理表strict并非分支可染。最短连接必须是：实际H及数学分流条件→真实锁embedding→实际迹count→有标号覆盖/显式置换→真实quota→严格排列界→PropertyB H。接口要求用户给profile/概率界/证书，就把最难的一段留在外部了。

T33先接24点混合大迹caller，固定实际恢复、AvoidedLink与RefinedDeletion，再扩其它分支。T34的 `TwentyOneSevenOne.propertyB_of_one_seven` 真正从21点/34边/paircover/恰一七度点返回Property B，925容量证书内部生成；`TwentyOneSevenMany.propertyB_of_many_sevens` 对至少五七度点闭合，九旧残型3618分配，其中1993满足实际其余条件。它们无额外profile前提，是真分支结果。

相反r=4的16个77778 pilot不覆盖1993单布局+7联合见证，r=2的565输入/99代表与两匹配矛盾、r=3的1722代表/67扩展及共同单位选择都未全接。`Target34 ↔ RemainingGoal`很有价值，但不是RemainingGoal证明。完整纸面候选不能改写成“一次总build即可”。[实际剩余接口](../../../../knowledge/archive/context/propertyb34/round01/twentyone-lean/SEVEN_R234_INTERFACE_GAPS.md)、[暂停末次闭合](../../../../knowledge/archive/context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md)。

## 2. 库存、扩锁、投影的已用接口

|源码声明|复用时必须给什么|其输出准确是什么|
|---|---|---|
|`BoundedAllocations.mem_enumerate`|每项界与所有容量|实际有界向量进入递归目录；不等于无重复/双射/每项可实现|
|`ActualAllocations.budget/mem_enumerate`|实际H与包含关系容量|实际大迹计数进入整数目录|
|`LockExtension.count_split/promotion_le_old/sum_promotion_degree`|同一H、扩展embedding与新点|每旧迹分含/不含新点；全部promotion和等于新点度|
|`PromotionCatalog.actual_mem_of_old/decode_nonempty`|旧count绑定、支持/无重复条件、真实新度与共度容量|非空promotion进入目录并可读回|
|`PromotionReconstruction.fillEmpty_actual/extend_actual`|非空promotion真实等式、实际新点度d、旧全部count|恢复含空迹/新singleton的全部新库存|
|`LockProjection.count_comp`|保留锁的embedding复合|同一H全部边的trace纤维求和；不是诱导子超图|
|`LockRelabel.count_comp_perm`|明确置换方向|置换后的实际count等于对应旧count|
|`LockLiftRelabel.restrict_lift_trans`|旧锁标准化且固定新末锁|标准化与真实扩展embedding相容|

具体源码都在归档[ThirtyFour](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/PromotionReconstruction.lean)同目录。`MultiLockRecovery.actual_recovered` 的宿主仍是 `Simple5Hypergraph`，锁数与点数是参数，并非一般k的导出定理；`realizes_recovered` 另外把边数固定为33。调用前读实际声明，按真实caller需求泛化，别复制600行概率引擎或按文件夹名字判断不可复用。

## 3. 自然数减法必须由实际计数等式支持

`PromotionReconstruction`中

    fillEmpty p d ∅ = d − Σ_(S≠∅)p S；
    extend μ p d U = if new∈U then fillEmpty p d oldTrace(U)
                    else μ(oldTrace(U)) − fillEmpty p d oldTrace(U)。

Lean Nat减法是截断减法。给任意虚拟p,d，上式可能静默变0，绝不能据定义本身说“恢复正确”。`fillEmpty_actual`用真实非空promotion等式、degree及`count_new_singleton`证明第一式；`extend_actual`在含新点/不含新点两支用`with_last/without_last/count_without_new/old`恢复真实count。这里正确性来自同一H的计数恒等式。

新增caller先证明promotion≤旧重数、全部promotion和=实际新度，再用接口恢复empty。不要靠`omega`在丢失真实容量时碰巧证明一个截断后较弱结论。一般增长源码也在改写k−1时显式给`1≤k`，用`Nat.sub_add_cancel`或`omega`建立k=(k−1)+1，再做幂运算。自然数、整数和实数强制转换的位置也要跟实际声明核对。

## 4. 稀疏大 numeral：先找归约表示，再加heartbeat

21点七度四锁，数学域固定674实际键/70代表。首个整块覆盖exit137；改64个声明仍>15分钟、RSS约8GB，由owner停止。随后15552编码数组在数据elaboration约84秒栈溢出exit134，尚未进入数学覆盖。不能把“大数组”记成成功修法。

最后只存673非默认键，用`List.lookup`/显式数值相等查询：data r23总4.22秒，完整kernel r24总87.75秒，user83.93秒、峰值8,123,957,248字节；真实残型接口r26通过，数学域未缩。没有完整旧运行耗时，也未隔离所有变量，因此不能给精确speedup或说pattern match是唯一已证根因。

**实际操作。** 对慢声明先读首个有效错误与系统成本，分清elaboration/数据展开/kernel归约/重依赖构建。选非平凡输入试替代表示。小稠密域可数组，稀疏大Nat域试关联表；保留同一覆盖命题。仅把一巨句切成64段，底层稀疏numeral归约不变时也可能仍慢。原始日志与改法：[PERFORMANCE_NOTES](../../../../knowledge/archive/context/propertyb34/round01/middle-lean/PERFORMANCE_NOTES.md)。

## 5. 数据、重核验与caller隔离，要真正切断昂贵依赖

有重数据时分Data→Certificates/Numeric→coverage/dispatcher→actual caller。925唯一七度证书152秒/约10.74GB；3618多七度357秒（完整调用360.32）/约8.99GB。其后修dispatcher与wrapper只1–2秒，未再核同一公式。改变数学依赖时照常Lake重建；短证明无重复成本就不机械拆四文件。

唯一七度caller曾反复展开符号化`Matched values`。修法是显式标注中间证明类型、`attribute [local irreducible] Matched`，需要时显式展开；分派helper先接受抽象`values : List Nat`，再代入实际count，避免kernel对符号目录深递归。实际caller1.7秒/wrapper1.5秒通过，公理基础不变。提高heartbeat本身不减少证明工作。

分块必须有全域索引覆盖：T33六锁改64行块，最终用商/余恢复全部索引；不是只接受pilot块。T34容量剪枝依赖`mem_enumerate`实际完备性，不能只引用Python输出。460/167容量分配、246/66正pair输入、73/48轨道是不同对象，表头须说明。

25点33几何/至多1376公共A/B/C系数的缓存只完成系数等式与带剩余假设caller probe，未有公共整表、一般分组、11,692输入批量核验；另358修正见证还缺导出器删掉的配额乘子恢复。它是有价值待做降本，不是已测提速。源：[成本分析](../../../../knowledge/archive/context/propertyb34/round01/high-math/TWENTYFIVE_FORMALIZATION_COST.md)。

## 6. 构建指定模块，并在构建后审实际导出

归档有固定`formal/lean-toolchain`、`lake-manifest.json`；工具链/缓存不随档案自动就绪。使用独立工作副本，按副本环境配置elan，不把作者绝对路径作为通用命令。依赖准备后，在该副本`formal/`运行所需命令：

```sh
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

上面是已完成T33的验收入口；本整理没有新运行Lean。默认`lake build`目标仍旧`Aris4Math.Main`，不能代替新Main。一般k完整入口是：

```sh
lake build Aris4Math.General.Growth.Twelve
lake env lean ReviewAuditGeneralGrowth12.lean
```

`ReviewAudit33`从裸`[Finite V]`、五元Finset边集、≤33恢复Bool两色与34下界；general审计从原积分/全部正整数最大性/floor公式与裸Finite边集恢复结论。要看真实定义、定理类型、所有隐含参数及`#print axioms`。标准三公理不保证命题对齐，`P→P`也可只有它们；搜不到sorry不保证传递依赖无sorryAx。

本项目已验顶层仅`propext`、`Classical.choice`、`Quot.sound`，无新增未证公理、sorryAx、native_decide。按当前合同审信任基础，不推广成所有数学项目只能恰好三公理。模型静态读源码、内核接受、本机增量导入、干净重建、第二台机器复现分别记录。

历史T33主装配1138 jobs约12.5秒，是大量依赖先验后的增量；general Twelve 2576 jobs15.64秒同样大量缓存，原题审计7.70秒。不能用它估计一个新题从零只需十几秒。一个正式执行者排重型构建，别让多人重复核同一8–11GB依赖；其它独立数学/检索/caller可同时推进。

## 7. 暂停瓶颈的准确交接

m(5)≥35：全纸面候选与全Lean是不同成果。已闭≤20，以及21δ5/6/8、21δ7且r=1或r≥5；RemainingGoal留下21δ7的r=2/3/4和22…25完整染色。23点3→4分类已通过部分strict/残型接口，22+19残型仍在，不能写成完整23染色。以[最后收卷](../../../../knowledge/archive/context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md)为准。

m(5)≥36：本阶段不要求Lean，八类仍开是实质数学缺口，停Lean不会自动消除。21高e、22两类、23δ7尚无整域候选；不要派人“补最后caller”掩盖根本没有足够数学门。保留[条件工具](../../../../knowledge/archive/research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md)已证部分和[真正剩余](../../../../knowledge/archive/context/propertyb35-paper/REMAINING_AUDIT.md)，用户未恢复时只读整理。

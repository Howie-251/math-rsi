# 23点一/二低四锁严格项：导出与实际调用

来源为 `middle-math/FEW_LOW23_1_3.json` 与 `FEW_LOW23_2_2.json`，对象分别为标签度数 `[6,7,7,7]`、`[6,6,7,7]` 的四个真实锁点；H 有23点、34条五元边。

第一表有47个纯严格项、4个混合严格项、22个残型；第二表有28个纯严格项、1个混合严格项、19个残型。本导出只处理严格项，不宣称残型已排除或局部分类已覆盖每个实际 H。原始代表标号和原布局均保留，没有对低/高度混合标签做任意置换。

导出器 `generate_few_low_four.py` 的 `--pilot` 只生成首个纯项与首个混合项；`--all` 用于试点核验后导出整批。纯项先用 `pure_quota.certificate` 恢复原表未存的 quota 证书，再重建两个嵌套配额的精确非负对偶。其 A/B/C 用独立标号注入公式重放，全部比较使用有理数。混合项直接调用 `twentyone-math/verify_joint.py`，核对原表的布局概率、共用真实坏对容量、配额、双向权重和严格界。

每个导出分为 Data、Numeric、实际 caller 三层。Data 定义全部16个迹标签、真实计数目标 μ、布局与精确系数；Numeric 用 `decide +kernel` 核验严格算术；`propertyB_of_counts` 假设所选实际四锁的 `MultiLockRecovery.count H vertices T` 确实等于 μ，内部构造 `RealizesProfile`，调用通用实际计数/坏对扣除引理，得原始 `PropertyB H`。纯项还提供 `propertyB_of_data`，从真实34边、四个度数、六个共度及五个大迹重数恢复全部实际 μ。

## 试点

- `TwentyThreeOneLowFour`：试点时为 `Case := Fin 1`，源 group 1，纯界 `459161/461890`；同时具有 counts caller 和 degree/codegree/high-trace caller。
- `TwentyThreeOneLowFourJoint17`：源 group 17，两个原布局，混合界 `453670144353/461890000000`，具有 counts caller。

试点的 Python 精确重放及两个实际 caller 的 Lean 构建均已通过。正规 r20 日志为 `../twentyone-lean/build-queue-TwentyThreeOneLowFour-r20.log` 和 `build-queue-TwentyThreeOneLowFourJoint17-r20.log`（同目录），导出两种 actual caller 的传递公理均仅标准三项。绑定记录 `FEW_LOW_FOUR_PILOT_EXPORT.json` 保留试点源 group；纯项详细重放文件随全批导出扩充。

## 整批导出

试点通过后已运行 `python3 context/propertyb34/round01/middle-lean/generate_few_low_four.py --all`。全部75个纯项和5个混合项完成独立精确重放，生成7组Data/Numeric/actual模块：一低纯项47例，二低纯项28例，一低混合groups17/22/53/57，二低混合group39。两个纯项模块中 `sourceGroup` 将 Lean Case 对应到原表group；完整索引与41个残型列表保存于 `FEW_LOW_FOUR_ALL_EXPORT.json`。

整批80个严格项的数值核验与实际 counts caller 已由唯一正规构建者串行构建通过。r21分别验证两个纯项模块和其余四个混合项模块；Joint17源未改变，沿用r20。全部导出 caller 的传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`。日志为 `../twentyone-lean/build-queue-<target>-r21.log`，其中 `<target>` 为 `TwentyThreeOneLowFour`、`TwentyThreeTwoLowFour`、`TwentyThreeOneLowFourJoint22`、`TwentyThreeOneLowFourJoint53`、`TwentyThreeOneLowFourJoint57`、`TwentyThreeTwoLowFourJoint39`；本执行者逐一读取成功记录。两个纯项Numeric分别用100秒、51秒，四个混合项Numeric分别用5.7秒、5.8秒、5.3秒、11秒。

这些定理闭合的是原表80个严格代表的实际计数调用。41个残型完整保留，实际四锁必落入表中以及残型后续提升/排除由上层分类模块负责；本批通过不表示23点分支或T34已经完成。

后续3→4实际覆盖与严格／残型分流现已接通：`TwentyThreeFewLowFourClassified.OneLow/TwoLow.actual_residual` 从同一实际H的旧三锁计数、新增七度点及其共度上界，在不可染假设下导出角色保持重标号后的22／19残型。Numeric r37、Coverage/Classified r39均通过，最终六个实际导出仅标准三公理。详情和日志见 `FOUR_PROMOTION_COVERAGE.md`。这补齐了局部分类输入与80个严格代表的连接，后续41个残型及完整23点分支仍开放。

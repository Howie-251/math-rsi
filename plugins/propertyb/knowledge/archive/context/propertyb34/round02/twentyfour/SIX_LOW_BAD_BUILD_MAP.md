# 24点六低非单位完整支：表示与构建地图

保持原181个单布局严格证书、467/611/787完整输入域、真实选点/置换/迹恢复、原Property B端点。NoLow已过链冻结，本次不修改。正规构建仅主代理执行；下列短probe不冒充完整分支验收。

## 数据层已经正规通过

`TwentyFourSixLowBadData`正规69.82秒PASS，见`TwentyFourSixLowBadData-sparse-build.log`。原90秒timeout没有通过；最终数据改为：

- 原181行μ的Finset逐项比较向量改为同值稀疏Nat(typeCode,count)表。类型码为有限子集的二进制和；后续完整p_eq_computed、high support与recovery照常绑定，未引入编码单射作为隐藏前提。
- 181个positionFn单射分编号kernel核验，不做一个巨大的∀i命题求值。
- R和quota的181行完全相同，经原记录核实后共享一行；未改变候选配额。
- 无调用的co向量退出当前数据闭包；其原值仍在源JSON及本目录REPLAY中。
- 实际调用需要的μ_eq_recovered保留在Recovery0…5与Recovery组合模块，Bad caller显式导入。没有删除真实恢复义务。

定位短测（秒/组峰GB）：labels之前3.82/2.27；原μ前缀20.15/2.44；仅外层Array失败于isDefEq默认heartbeat上限；稀疏μ4.87/2.39；原整体验单射触4GB停止；拆开的完整181单射11.87/2.43；完整computed加5个实际profile绑定12.43/2.65。原失败日志保留。

## 后续确定顺序

1. `TwentyFourSixLowBadRecovery0`至`Recovery5`：每块30（末块31）个原恢复等式独立kernel证明。随后`Recovery`只选用已证条目，导出原名/原类型。
2. `TwentyFourSixLowBadNumericCases0`至`NumericCases18`：18块各10项，末块1项。每项仍完整核验profile有效、避锁配额、loss支配和缓存ABC严格界。随后`Numeric`组装181项并用通用rows_eq恢复原Numeric.boundA/B/C接口。
3. `TwentyFourSixLowBad`：由全部实际count到原染色，low/high由恢复引理相接。
4. `TwentyFourSixLowBadCoverageData`、`SparseData`、`SparseBridge`、`CoverageKernel`：完整1870标签输入、同一真实置换、非单位对集和高迹support。
5. `TwentyFourSixLowBadActual`、`Complete`：完整原H24分支；再独立裸Finset/Bool复述、传递公理检查。

结构选择模块`TwentyFourSixLowSelection`须在最后Complete之前正式构建。源已轻测，不把此前轻测改写成正规通过。

## 数值与恢复的实测成本

五个代表0、37、90、174、179的原恢复等式13.06秒/2.89GB通过；按30条/模块给90秒初始预算，具体以正规结果为准。另试过直接低阶balance的一般桥，数学引理轻测4.10秒且标准三公理；但五代表balance核验17.77秒更慢，因此它不进入当前依赖链，不能宣称加速。

复杂case179完整数值证书6.47秒/3.16GB通过。五case数值试验20秒预算停止、峰3.42GB，不计通过。因此不再尝试整181的单模块kernel任务；十项一块，可分别编译、定位和复用。预计总数值CPU约十余分钟，不能把单代表成本当完整确定耗时。三case短测结果另附实际日志。

规范生成器`generate_sixlow_bad.py`先从原三个JSON生成同一数学数据和证书，再调用`optimize_sixlow_bad_data.py`及`split_sixlow_bad_numeric.py`保持本表示。旧Data/单体Numeric分别保留为`SixLowBadDataBeforeSparse.lean`和`SixLowBadNumericBeforeChunks.lean`。正规已过数据源码冻结，不为后续可能的性能改善重建。

三个实际代表0、37、179的完整数值短测已PASS，17.56秒/3.42GB，见`bad-numeric-three.log/json`。全部19块与最终接口源码冻结，交主代理正规构建。`SixLowBadReviewAudit.lean`备有纯Finset输入、显式Bool染色结论，待实际完整分支构建后运行；当前不计audit已过。

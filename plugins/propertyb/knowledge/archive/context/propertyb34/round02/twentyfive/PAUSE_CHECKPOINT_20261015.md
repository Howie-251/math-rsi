# 25点与21点三七度支：暂停检查点

根代理通知用户正在决定暂停35的Lean，转入36–40纸面研究。本代理收到通知后停止新增实现与探测，只收回已结束进程并保存状态。下列只是局部交接，不改变 Goal 工具状态，也不宣称 T34 完成。

## 最近最重要的数学压缩

连续九锁、固定无色块族、恰五个六度点其余七度点、固定每位置 A/B/C 选择时，选择上界之和关于低点指示变量严格仿射。真实单点计数 s_i=7−a_i−x_i，空迹 n0=Σa_i−|B|−24 保持固定。自由中心一侧只有空迹；锁中心只有自身 singleton 可变；Boolean 平方 x_i²=x_i 消去所有剩余二次项。一般参数可将7与五低替换为固定高低相差1的度数，并保持低点总数固定；仍须核对真实库存与非负性。若锁不连续，此证明不能直接沿用；若加入 quota 罚项，也不能据此声称整体仿射。逐位置 min 本身不必仿射。

详见 Q5_AFFINE_METHOD.md。初始三族127/200/365各126颜色均由一个既有连续布局覆盖；全374族实测结果不能从三个试点外推。

完整诊断 Q5_AFFINE_FAMILY_ALL.json：

- 65族整族度数拒绝；2族（56、86）整族总边数预算拒绝；10族不足5个可低位置。
- 297个有实际可行颜色的族中285族已被既有连续布局的仿射上界覆盖。12族仅余34个颜色，沿用已保存的非连续证书即可，无需重新搜索。
- 已选1923个共享布局；完整285族中67族单布局，其余2–37布局。
- 每个 chosen 布局都对该族全部合法5低子集调用原 BareLayout 精确 Fraction 公式复算，等于其仿射表达式；保存 constant、coefficients、assigned_lows、assigned_max、top_five_bound。
- 全扫描60.31秒，脚本 q5_affine_family_pilot.py --all。未重搜任何新布局，未改动旧正式通过的 q5 group89。

## 新增Lean通用桥的准确状态

下面模块均仅做轻量 lake env lean；正式 Lake 由根代理统一调度。

1. CachedAffine.lean：PASS，2.79秒/约1.29 GiB。有限仿射乘积、二次多项式求和、Boolean对角线性化，以及六残余桶 A/C 展开。日志 cached-affine-r2.log。
2. CachedAffineBinding.lean：连同前模块的联合探针PASS，4.93秒/约1.30 GiB。真实 cached mass、几何系数和 diagonal 一旦分别绑定，即推出 selected bound 等于二次表达式，并由off-diagonal为零和严格仿射界推出原 min 总界严格。日志 cached-affine-binding-r1.log。
3. CachedAffineTable.lean：三模块联合探针PASS，2.20秒/约1.31 GiB。固定几何和trace形状列表，允许零count；若各真实count已写成仿射式，则通用证明 mass、真实 diagonal 与整条selected bound的绑定，不需每个颜色重新展开类型对。日志 cached-affine-table-r3.log。
4. CachedActualValidity.lean：未通过，独立试验无import它的验收模块。最后失败只是 table_count_sum 里 simp 同时使用 Finset.sum_const 与 Finset.card_eq_sum_ones 导致重写循环；应删除后者再检查后续 cast 步骤。暂停后未修复、未重试。日志 cached-actual-validity-r1.log。这个模块旨在从真实 TableRealization 导出总计数有效性，避免逐颜色复算。

目前尚未完成：实际族127的全caller；零singleton的pruneZero到未剪枝mass恒等桥；每个共享布局的内核系数证书；全部374族的安全覆盖装配。故这次新增通用桥与Python结果都不是25完整分支或T34验收。

## 恢复时的最小顺序

用户授权恢复后：

1. 由根代理正规构建 CachedAffine → CachedAffineBinding → CachedAffineTable（此前如已有正规日志则复用）。不要重新运行11692布局搜索或1844模块全量队列。
2. 修复 CachedActualValidity 的明确simp循环，补必要的真实计数/零行剪枝桥。优先用族127做首个完整 actual H caller：该族空迹恒0，九个singleton在所有低色下均正，可先避免零行分支。
3. 族127沿用目标4424的连续布局，固定选择只有一个锁中心C，仿射式的统一界6241/6435<1。真实输入需证明 n0=0、s_i=7−a_i−x_i、Σx_i=5、x_i²=x_i；再接到CachedAffineTable，而非把仿射count等式作为原题额外前提。
4. 核验一个有零singleton的真实族，通用处理剪枝；随后才扩全部1923个共享布局。为每族保存一个完整无色库存；每个布局只核稀疏仿射数据和小覆盖。先1–5条pilot，仍20秒/4 GiB护栏，超过就诊断，不直接扩大阈值。
5. 12残族34颜色保留旧显式证书。不得因新的连续布局覆盖未命中而把这些原成功证书丢弃。

## q9与旧q5正规结果

根代理已正式通过 Unit8完整Checked与Actual、Unit9Data与全部114 Rows批。原Unit9Checked单体150秒timeout，已拆65个CheckedParent并保留原名aggregate；Parent64正规11.54秒PASS，Parent0仍150秒timeout。

根代理最新发现是 UnitExtension.choices 的隐式 Fintype 枚举，而非 rows 数据。它正在独立新增 UnitChoicesFast 的显式bounded Decidable与choices_eq桥，轻探针11.56秒PASS、尚未正规、未改parents。本代理没有并行修改q9parents、已通过UnitExtension或Rows。相应选择与恢复由根代理接手。

q5唯一已正式验证的数据组89保持不变：Data18.11秒、Inventory24.06秒、Numeric40.53秒、Family60 3.34秒。未启动其余1844全量队列。不要把该单组通过当作完整q5。

## 21点三七度结构

四个新模块 TwentyOneSevenThreeSelectionWeights / Selection / Common / Five 已稳定；联合 ThreeSelectionFiveProbe PASS11.06秒/约1.33 GiB，关键导出标准三公理。具体范围见 ../twentyone-three-selection/REPORT.md。

select_five 从实际 H21、34边、cover、min7、sevens.card=3、noB 构造 [7,7,7,8,8] 五锁。两八度点具有同一个非空unit模式，且相互codegree=2；所有锁对codegree≤2。Common.four_common 仍明确假设残型结构，不能宣称整个r=3关闭。根代理已据λuv=2把旧1722型数值域缩至1048型（1033单布局+12joint+3残），新覆盖/实际装配由根代理负责。

## 进程

所有本代理新增的轻量探针与Python全族诊断均已结束。没有遗留运行进程；没有更改既有Goal状态、全局AGENTS、正式Assembly、原T32/T33成果或aris4math_v2。

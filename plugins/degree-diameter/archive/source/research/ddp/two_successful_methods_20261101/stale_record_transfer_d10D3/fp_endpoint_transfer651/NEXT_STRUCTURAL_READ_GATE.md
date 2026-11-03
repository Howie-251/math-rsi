# actual650 FP-transfer：下一结构门（只读准备）

状态：**旧一次模型 UNKNOWN 原样保留；本次没有新数值授权或运行。** 只读了 FP_NOTE/PRED/RESULT、模型元数据/labels、生成器必要段和已有 STRUCTURE_ROOT 的字段，不读 source 邻接、A2 数组或稀疏系数内容，不运行 source/BFS/solver/候选。

## 旧模型先卡在哪里

源是 [已有读取接口](SOURCE650_FP_TRANSFER_READ_GATE.md) 指定的 actual10D3/650/3250，全10度；F520、P130，65对 P 具有相同的8个 F 邻点，P 子图为 C79+C21+C30。不是其它同名650源。

[FP_once.py](FP_once.py) 的1170 binary/1302行/90480非零项模型只问：八条 FP cut 的 F/P 端各异，两个 star-P 必须是 donor，十个新根 pins 的原源 closed-R2 是否覆盖520个 F。这个门先于 PP repair，因为已继承的 twin 替路接口使它恰为新根到 F 的三步覆盖条件；它不是全部新根或旧旧 D3 条件。

唯一20秒 HiGHS 窗口无 incumbent，原 [RESULT](FP_RESULT.json) 为 `UNKNOWN_F_COVER_MODEL_NO_INCUMBENT`。不能从中判断覆盖本身不可能、哪行冲突、solver 卡于哪个组合，或 PP 修补损伤了旧路。冻结原型、15配对、新根/旧根 BFS 均为0。

## 已有 PP 边的分支没有被模型漏掉

生成器263–273行已允许：余六个 donor-P 的某个 repair pair 若原本就是 PP edge，则保留原边，不加重边，这两个点最终保持 degree9。若 k 条 repair 是原非边，最终 m=3252+k，最大度仍10；仅 k=3 时才全10度、m3255。故这个合法 underdegree9 分支**已准备但尚未执行**，不能说它失败或缺失。

它不改变前置 F-cover：repair 的两个端点都在“没有直接接 z 的六个 P”中。含新 PP repair 的 z→F 路至少长4；三步 z→F 不能使用它。因此允许保留旧 PP edge 不会放松现有 F-cover 模型，也不能借此绕过无 incumbent 的门。它可能影响后续 P 覆盖与旧旧路径，只有实际冻结后才有相应问题。

## Twin 结构给出的精确投影

记65个 twin class 为 c，每类有两个 P 点及它们共同的八点集合 F_c；这些 F_c 分割520个 F。每个 F 点只可选其两个 twin-P 中的一个作为 cut endpoint。

把旧1040 cut变量投影为520个 `y_f=该F是否被选中`，保留130个 `z_p=该P是否为star-P`。对每类只需

`Σ_(f∈F_c)y_f ≤ 2`，

`Σ_(p∈P_c)z_p ≤ Σ_(f∈F_c)y_f`。

再加全局 `Σy=8, Σz=2` 和原520行 F-R2 coverage。这是 **650 binary/652行** 的等价 F-cover 投影，不是改规则：每类选0/1/2个 F，可恰给0/1/2个不同 P 分配 donor，且包含指定的 star-P；反之旧 cut 选择必满足这两式。FP cut列的覆盖系数只依赖其 F 端，正是生成器81–87行的写法。

不能据此把130个 star-P 直接并成65个变量：twins 仅保证 F-neighborhood 相同，二者 PP 邻点可能不同，故它们的 source-R2-to-F packets 尚不保证相同。此精确投影也不说明旧 solver 的实际困难原因，更不是下一次 solver 授权。

## 唯一建议的下一小数据问题：分 class 的八 packet 容量门

下一问题只问：**是否有两个 star-P 的选择，在 twin-class donor quota 下仍能通过八个 F-packet 的覆盖容量上界？** 不续原 MIP，不先试15种 repairs。

可在授权后仅从保存的模型 coefficient 提取 `C_f=R2_G(f)∩F`（520个）及 `D_p=R2_G(p)∩F`（130个），不用重算源 R2。对一个 star-P pair {p,q}，令 `U=F\(D_p∪D_q)`，`h_c=|{p,q}∩P_c|`。在每类定义

`m_c(0)=0`，`m_c(1)=max_(f∈F_c)|C_f∩U|`，

`m_c(2)=max_(f≠g∈F_c)|(C_f∪C_g)∩U|`。

只用 cost0/1/2、下界 cost≥h_c、总 cost=8 的小 knapsack DP，求 `T(p,q)=max Σ_c m_c(cost_c)`。不同 classes 的重叠仍被有利地忽略，所以 `T<|U|` 是排除此 star pair 的严格必要失败证据；`T≥|U|` 只说明这一个容量界尚未排它，绝不代表真覆盖或651图。若全部 pairs 失败，可关闭 F-cover 子问题；否则只给 surviving pair/缺口 witnesses，不能扩大成全族结果。

一个可推翻的下一预测是“至少有一个 pair 能通过该 grouped 容量界”，但本只读门不预先支持其真假。即便该预测支持，也只表示简单容量无法解释原 UNKNOWN，不能自动续 solver。

最小输入只有 [FP_MODEL.json](FP_MODEL.json) 的 row/column labels、[FP_MODEL_MATRIX.npz](FP_MODEL_MATRIX.npz) 的520 coverage rows，以及 `research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json` 的 F/P/twin labels。class→8F 可由旧 cut-column labels 关联，无需 source 邻接、A2/A3、PP球或 source 验收。本文没有读取这些系数或计算任何 DP、packet union、pairing。

旧≤5纯 hub/all-endpoint/no-old-old completeNO 不排此八 FP cuts+PP repairs 规则。新机制目前仍 UNKNOWN，后续只围绕同源/同规则这一结构门，所有数值等待 root 授权；不换参数或列模板。

两次标准库只读进程 measured CPU 合计0.002869774秒；连同路径定位和文档准备保守 charge0.25/1秒。没有新增图、参数、Lean 或数学数值批。

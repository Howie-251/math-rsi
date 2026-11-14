# E16 的完整 μ=4 层

直接 caller `/root`。作者稿，合并证明待独立审计。

**定理。** 设 $M$ 是 $Q_7$ 的任意 56 边短匹配，$H$ 为原孔集。记第 $i$ 位取一的半面内偶孔数减奇孔数为 $\delta_i$，令 $\mu=\min_i|\delta_i|$。若 $\mu=4$，则存在包含全部 $M$ 的全短 Hamilton 圈。

## 证明

若 $H$ 中有一对相邻点，则将这条短边加入 $M$。它的两端均为原孔，所得仍是短匹配，且有 57 条边。完整 E14 定理给包含增广匹配的全短 Hamilton 圈，因而保留全部 $M$。此处 E14 的入口只需要增广后的短匹配边数。 [E14 总定理](R7_MU1_FULL_CLOSURE.md) · [联合审计](R7_MU1_CENTRAL_T1_AND_E14_REVIEW.md)

以下原孔独立。由已审初始归约 §4，同时规范孔集和原匹配后，可把原孔写为 $L\cup\overline V$，其中 $L,V$ 各八点，且两组同奇偶，$\overline V=127\oplus V$。每列合计载荷为 $c_i=8-|\delta_i|\le4$。规范变换是立方体自同构。 [E16 初始归约 §4](R7_E16_INITIAL_REDUCTION.md) · [归约审计](R7_E16_INITIAL_REDUCTION_REVIEW.md)

若两组均为偶点，初始归约进一步给出 $L=\{0\}\cup E(G)$、$V=\{0\}\cup E(K)$，其中 $G,K$ 各为七边简单图且逐点度数和为四。规范原偶孔为 $L$，原奇孔为 $\overline V$。完整偶组定理覆盖这个模型的每个短匹配实现，故规范化后的 $M$ 有全短延拓。 [偶组整族](R7_E16_EVEN_MU4_CONTROLLED_COVERAGE.md) · [审计](R7_E16_EVEN_MU4_CONTROLLED_COVERAGE_REVIEW.md)

若两组均为奇点，已审奇组归约排除重量五、七，故只含单位点与三元支撑。记两组各自的三元支撑数为 $t_L,t_V$。全补是七维立方体自同构，将规范原奇孔 $L$ 与规范原偶孔 $\overline V$ 分别送到 $\overline L$ 与 $V$，因而交换规范组的角色，并同步运输原匹配。由此可取 $t_L\le t_V$。重量归约给出下表四个且仅有的候选数型。各型定理均覆盖对应孔集的每个短匹配实现。 [奇组重量归约](R7_E16_ODD_MU4_WEIGHT_REDUCTION.md) · [归约审计](R7_E16_ODD_MU4_WEIGHT_REDUCTION_REVIEW.md)

| $(t_L,t_V)$ | 有正计划的规范代表数 | 分支证明及审计 |
|---|---:|---|
| $(2,2)$ | 329 | [整型闭合](R7_E16_ODD_22_COMPLETE_COVERAGE.md) · [审计](R7_E16_ODD_22_COMPLETE_COVERAGE_REVIEW.md) |
| $(2,3)$ | 732 | [整型闭合](R7_E16_ODD_23_COMPLETE_COVERAGE.md) · [审计](R7_E16_ODD_23_COMPLETE_COVERAGE_REVIEW.md) |
| $(2,4)$ | 191 | [整型闭合](R7_E16_ODD_24_COMPLETE_COVERAGE.md) · [联合审计](R7_E16_ODD_24_33_COMPLETE_COVERAGE_REVIEW.md) |
| $(3,3)$ | 375 | [整型闭合](R7_E16_ODD_33_COMPLETE_COVERAGE.md) · [联合审计](R7_E16_ODD_24_33_COMPLETE_COVERAGE_REVIEW.md) |

四型合计 1,627 项，计数采用各分支的单位缺位规范与共同坐标群有限基。这个计数不涉及原匹配数量或完整立方体自同构商。偶组或奇组定理得到的圈经全部规范变换的逆变换运输，仍为全短 Hamilton 圈，且包含原输入的每条边。$\square$

## 构造记录与范围

先前窄门诊断界定了当时所用模板的适用范围。最终奇组回代使用精确核心 117 及整面供体接口，并按实际接收孔型调用整面、正跨分面或受控单根。各分支已经给出全实现正计划，本稿仅合并已有证明和有限证书。相对全部旧工具的净新增量未知。本次合并的孔集扫描、原匹配枚举、求解器调用和秩重算均为零。

本结论闭合 E16 的完整 $\mu=4$ 层。E16 整层和 $R_7$ 仍待证明，最高完整孔层仍为 E14。

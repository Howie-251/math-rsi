# E16 的完整 μ=3 保边 Hamilton 延拓

2026-11-15。

本证明为计算辅助证明。数学归约使用下列已审导入。偶支撑及较高总重奇支撑的有限不可满足性，均由绑定到冻结 CNF 的实际 RUP 证书完成。

**定理。** 设 $M$ 是 $Q_7$ 的任意 56 边短匹配，$H$ 为未覆盖顶点集。令 $\delta_i$ 为位一半面上的偶孔数减奇孔数，并设 $\mu=\min_i|\delta_i|=3$。则 $Q_7$ 有包含 $M$ 的全短 Hamilton 圈。

## 1. 规范化和已接受的剥离

每条原短边覆盖一偶一奇，故 $H$ 有八偶八奇。若两枚原孔相邻，将其短边加入 $M$，对所得 57 边匹配调用 E14。以下 $H$ 独立。存在绝对孔差七或八的轴时，调用对应的已审整族。余下每轴满足 $3\le|\delta_i|\le6$，且有一轴等于三。 [E14 总定理](../R7_MU1_FULL_CLOSURE.md) · [E14 散列及接受回执](../R7_MU1_CENTRAL_T1_AND_E14_REVIEW.json) · [差七总定理及偶支撑导入](../R7_E16_MU3_GAP7_ODD_CLOSURE.md) · [差七回执](../R7_E16_MU3_GAP7_ODD_REVIEW.json) · [差八回执](../R7_MU3_THREE_BRIDGE_FULL_REVIEW.json)

初选颜色组 $G$。若某轴的位一面中 $G$ 孔数大于另一颜色组孔数，就翻转该轴。翻位后，$G$ 的像 $P$ 在每轴的位零面中孔数均大于另一颜色组。把另一物理孔组写成 $\overline Q$，横线为七位取补。两支撑组 $P,Q$ 各八点，同属权重奇偶 $\sigma\in\{0,1\}$。记 $p_i,q_i$ 为各组在轴 $i$ 的位一载荷，$\lambda_i=p_i+q_i$。按 $P,\overline Q$ 色序，位零和位一孔型分别为
\[
(8-p_i,q_i),\qquad(p_i,8-q_i).
\]
因而 $\lambda_i=8-|\delta_i|$，$2\le\lambda_i\le5$，$\max_i\lambda_i=5$。物理异色孔距离为 $d(p,\overline q)=7-d(p,q)$，故独立性恰排除跨支撑组距离六。翻位与共同坐标置换始终运输整个 $M$。物理全补交换 $P,Q$，保持 $\sigma$。 [规范孔归约](../R7_E16_INITIAL_REDUCTION.md) · [原输入到模型的独审](EVEN_GLOBAL_REVIEW.md)

若 $\lambda_i=5$ 且 $\min(p_i,q_i)$ 为零或一，选择相应少数孔较少的一面为接收，得到单色三孔 $(5,8)/(3,0)$ 或 R41 $(4,7)/(4,1)$。这两情形由已审整族覆盖。此后每个载荷五轴的两组载荷为 $(3,2)$ 或 $(2,3)$。可共同置换坐标使 $\lambda_i$ 降序，并在必要时物理全补，使轴零为 $(3,2)$。较高总重奇支撑还可在并列 $\lambda$ 的块内按 $p_i$ 降序，轴零条件仍可同时实现。 [单色三孔及绑定](../R7_E16_THREE_MONOCHROMATIC_CLOSURE_REVIEW.json) · [R41 及绑定](../R41_FULL_REVIEW.json) · [奇支撑排序及必要条件](ODD_HIGH_WEIGHT_REDUCTION_REVIEW.md)

## 2. 奇支撑最小总重分支

令 $D=\sum_i\lambda_i$。当 $\sigma=1$，每组至多六个单位点。否则物理中心 $0$ 或 $127$ 的七个短邻都是孔，独立性使中心自身为非孔，因而不可能由 $M$ 覆盖。每组总重至少 12。等号 $D=24$ 时，两组各恰为六个单位点及两个不同三元支撑。

首组的无序三元对按交数 $t=0,1,2$ 分型，缺失单位轴按所在 Venn 格再分。交换两三元使两个独占格等价，所得 2、3、3 个首组轨道穷尽。把首组搬到代表时，共同运输次组及整个 $M$。每个代表配次组的全部七个缺位及 $\binom{35}{2}$ 个三元对。物理独立性与载荷过滤后，固定基有 9,072 个入域条目。独审核准 7,538 项的三种早筛构造和其余 1,534 项的全部固定计划。每项均适用于该孔型的每份实际原匹配，实际端口配对由 $M$ 读取。这里的计数单位是几何参数条目。 [八源归约审计](ODD_D24_REDUCTION_REVIEW.md) · [整域独审](ODD_D24_CLOSURE_REVIEW.md) · [审计回执与 hashes 字段](ODD_D24_CLOSURE_AUDIT.json) · [固定计划及依赖绑定](ODD_D24_FIXED_PLANS.json)

其余奇支撑有 $26\le D\le34$ 且 $D$ 为偶数。若某组有重七支撑，跨距离六禁尽对组单位，对组重至少 24，而含重七组重至少 16，矛盾。因此只剩重量一、三、五。记 $U,F$ 为两组合计的单位数及重五数，则 $D=48-2U+2F$。重五的补二元禁止对组对应单位。若一组有至少三个重五，或两组分别有至少两个和一个重五，该限制给 $U\le9$，并有 $F\ge3$，故 $D\ge36$。因此 $F\le2$，较高总重模型可施加 $7\le U-F\le11$ 和重七变量为零。 [独立重量界](ODD_HIGH_WEIGHT_REDUCTION_REVIEW.md)

## 3. 未获构造的实际原输入给出 CP 赋值

设规范后的实际 $M$ 避开对应模型所列的所有保边构造。给物理孔变量赋 $P,\overline Q$ 的真指示值，给区域计数赋实际和，给供接旗标赋实际计数比较结果。硬域及规范条件均满足。每个禁止的同组选源合取若成立，就给出下列一项保边构造。

- **两支共用。** 中央三稀列或两稀列带强列的已审宏，中央差三双向旧五门与整面接收，正向 $(3,6)/(5,2)$ 的同侧五门与完整六维 A6，以及差 $k=3,4,5$ 且接收少数孔至多二的分居供体。旧中央门的两返回配额与同一个前送、同一个供体标记面相容。完整 A6 接收正向修改后的 $(4,2)$ 并恰避指定标记。分居门以实际 $M$ 的可控正跨供体接上完整小孔接收。双轴标量许可表也只剥离可按两轴计数回代的已有入口，保留 106 个许可列，包含每份未获所列构造的输入之实际列。 [共用模型及数学回代审计](EVEN_GLOBAL_REVIEW.md) · [三稀列散列](../R7_E16_MU3_CENTRAL_S3_REVIEW.json) · [强列散列](../R7_E16_MU3_CENTRAL_S2_STRONG_REVIEW.json) · [正向 A6 审计及散列](FREE_A6_TRANSFER_REVIEW.md) · [分居供体](SPLIT_DONOR_SMALL_RECEIVER.md) · [独立许可表复核及散列](EVEN_GLOBAL_AUDIT.json)
- **较高总重奇支撑加项。** 差四至六的同侧四门配正跨分面接收，以及差四双侧整面各用四门。在正跨项里，两行前送格的整数区间之和给出供体标记面内前送数的全部可选值，返回两格容量可独立兑现。双整面项里，固定标记半面后两组选源来自相异原面，各自可选即能组成同一组前送、返回。侧存在旗标取实际存在值满足单向定义。 [高差正跨、双整面审计及源码散列](ODD_HIGH_GAP_WHOLE_PAIR_REVIEW.md)

所以未获上述构造的实际 $M$ 产生该支冻结 CP 模型的满足赋值。后者可能容纳不能由原短匹配实现的几何，所需蕴含只从实际反例指向满足赋值。

## 4. CP 赋值延拓与 CNF 证书

每个源 CP 满足赋值都可拓展为所对应 CNF 的满足赋值。赋各整数真实阈值，再以实际相等值、合法表行和前缀计数补足辅助变量。守卫使编码条件仅在源约束活动时生效。奇版另用永久单位子句表示常零域，并把宽 $\pm1$ 布尔和写成正负字面量的有界前缀计数。两支编码审核均逐字节重建源 PB，并逐行核对生成的 DIMACS。 [偶 CNF 保满足性](EVEN_GLOBAL_CNF_REVIEW.md) · [奇 CNF 保满足性](ODD_HIGH_WEIGHT_CNF_REVIEW.md)

冻结构建回执记录源模型、变量映射、编码器和 DIMACS 的版本绑定。以下实际验真使用上游 DRAT-trim 固定提交 2e3b2dc0ecf938addbd779d42877b6ed69d9a985，启用仅单位传播检验的 -U 模式。两次均记录 s VERIFIED、退出码零并且证明核心含零个 RAT 引理。JSON 绑定 CNF、证书、检查器源与可执行文件、驱动和日志的散列。 [固定检查器源码](PROOF_TOOLS/drat_trim_official_2e3b2dc/drat-trim.c) · [运行驱动](PROOF_TOOLS/drat_trim_official_2e3b2dc/verify_fixed_proofs.py)

| 支撑域 | 冻结模型、CNF 及其 SHA-256 | 证明及其 SHA-256 | 实际验真 |
| --- | --- | --- | --- |
| $\sigma=0$ | [even.pb](PROOF_TOOLS/even.pb)、[even.cnf](PROOF_TOOLS/even.cnf)，1701716ee858ddfacb356dee41f8cdfb7b53046bf101b22698da2065d84341df。 [构建回执](PROOF_TOOLS/build.json) | [even.drup](PROOF_TOOLS/even.drup)，74e891aee25f80a80b0dffeb102833779a35bbf071d9eb150b55e9cdc271a2d3。 [生成回执](PROOF_TOOLS/prove_900.json) | VERIFIED_RUP_UNSAT，373.523 秒。 [验真 JSON](PROOF_TOOLS/drat_trim_official_2e3b2dc/even_official_drat_trim.json) · [日志](PROOF_TOOLS/drat_trim_official_2e3b2dc/even_official_drat_trim.log) |
| $\sigma=1,D\ge26$ | [结构化奇 PB](ODD_DGE26_STRUCTURED_FULL.pb)、[odd.cnf](PROOF_TOOLS/odd.cnf)，b731f9c347471ec3c5a8e5e7613beac9678d72714961d342b44bd6ffdcb8f6f1。 [构建回执](PROOF_TOOLS/build_odd.json) | [odd.drup](PROOF_TOOLS/odd.drup)，d79dbce279e5c4d9b5f14cfc785eac9e69c309e52e6c57a6a682aebf12398060。 [生成回执](PROOF_TOOLS/prove_odd.json) | VERIFIED_RUP_UNSAT，270.897 秒。 [验真 JSON](PROOF_TOOLS/drat_trim_official_2e3b2dc/odd_official_drat_trim.json) · [日志](PROOF_TOOLS/drat_trim_official_2e3b2dc/odd_official_drat_trim.log) |

RUP 增补由反向单位传播取得，保留的每条增补子句都是当时公式的逻辑后果。由已核证书推出空子句，两份冻结 CNF 均不可满足。

## 5. 完整回代

由上述两个证书，任一尚未覆盖的实际 $M$ 经 §1 落在偶支撑、奇支撑 $D=24$、奇支撑 $D\ge26$ 三支之一。中支由 §2 覆盖。对其余两支，若未命中模型中的任何合法计划，则 §3、§4 依次给出冻结 CP 和 CNF 的满足赋值，与经验证的不可满足性矛盾。因此至少一个已审构造适用于同一实际 $M$。

在三桥和双返回构造中，独立原孔使每个选源的外镜像原来均有面内伙伴。局部定理接受基于实际端口的合法辅助配对。需正跨或控制根的构造按实际 $M$ 先选择其配对。删辅助边并接回原跨边、真实短桥和标记的原伙伴，得到带标签的不交路径。接收圈沿标签展开，恢复原规定边和全部先前未上圈的顶点，仍是一个圈且只新增短边。其余剥离入口直接调用各自的全实现定理。逆规范同构后所得全短 Hamilton 圈含初始 $M$。 [三桥保边展开](../R7_THREE_BRIDGE_TWO_RETURN_WHOLE_RECEIVER.md) · [两返回保边展开](../R7_CONTROLLED_TWO_RETURN_BRIDGE.md) · [全实现计划的依赖范围](ODD_D24_CLOSURE_REVIEW.md)


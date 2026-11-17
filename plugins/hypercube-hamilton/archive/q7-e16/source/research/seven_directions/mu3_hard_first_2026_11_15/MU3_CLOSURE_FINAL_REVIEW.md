# E16 μ=3 完整层独立审计

2026-11-15。**PASS · same-family · provisional · sound-modulo-imports。** 原输入为 $Q_7$ 的任意 56 边短匹配 $M$，其七轴最小绝对孔差为三。接受完整 $\mu=3$ 原域有含全部 $M$ 的一个 128 点全短 Hamilton 圈。审查并绑定最终正文，SHA-256 为 cb46b6cb0d31866903a72c2768fb25996f6be9aed7c1d16f8d063a08dd8b0f34。 [最终证明](MU3_FULL_CLOSURE.md) · [机器回执](MU3_CLOSURE_FINAL_REVIEW.json)

## 原输入穷尽及逆回代

1. 逐条短规定边覆盖偶奇各一点，故剩余八偶八奇。若存在相邻孔，向同一原 $M$ 加其自由短边，所得 57 边匹配满足已审 E14，最终圈自然含原 $M$。余下为独立原孔。若任一绝对孔差为七或八，调用该差值对应的已审全实现整族。因此余下每轴差在三至六之间，且至少一轴差三。 [E14](../R7_MU1_FULL_CLOSURE.md) · [差七独审](../R7_E16_MU3_GAP7_ODD_REVIEW.json) · [差八独审](../R7_MU3_THREE_BRIDGE_FULL_REVIEW.json)
2. 选一个原颜色组，若某轴位一面中该组的孔数大于另一颜色组孔数，就翻转该轴。翻位后，该组在每轴位零面中的孔数均大于另一组。记该组为 $P$，另一组为 $\overline Q$。七位补变色使 $P,Q$ 同为奇权或同为偶权，且各八点。$\lambda_i$ 为两组位一载荷之和，按物理两色孔差得 $\lambda_i=8-|\delta_i|$。同一变换运输全部原边，跨组物理短邻恰对应跨支撑距离六。若差三列的一组载荷为零或一，调用方向重选后的单色三孔或 R41。其余每个差三列为 $(3,2)$ 或 $(2,3)$。物理全补可交换 $P,Q$ 且保支撑奇偶；共同坐标置换可选轴零为 $(3,2)$ 并排 $\lambda$ 降序。高总重奇支撑另按并列轴 $p_i$ 降序时，先使某个最大列的 $p_i=3$，排序后轴零仍符合指定。 [规范化及基础门](EVEN_GLOBAL_REVIEW.md) · [单色三孔](../R7_E16_THREE_MONOCHROMATIC_CLOSURE_REVIEW.json) · [R41](../R41_FULL_REVIEW.json)
3. 奇支撑每组至少重 12 且各至多六个单位点，超过六时物理中心在独立孔假设下是没有可匹配短邻的非孔。故总重偶数 $D$ 满足 $24\le D\le34$。$D=24$ 的八类首组轨道与第二组全部参数已独立核定，33,320 个粗基条目经过两项必要过滤后余 9,072 项，其中 7,538 项由显式早筛门覆盖，其余 1,534 项各有逐条独验的全实现计划。$D\ge26$ 阶段重七不可能，重五至多两枚，$D=48-2U+2F$，所以新增取值域 $7\le U-F\le11$ 与重七为零均为必要条件。 [D24 整域](ODD_D24_CLOSURE_REVIEW.md) · [高总重必要性](ODD_HIGH_WEIGHT_REDUCTION_REVIEW.md)
4. 余下实际输入因而必落在偶支撑或奇支撑 $D\ge26$。若其规范后的几何命中模型排除的任一构造，则对应工具对这一个实际 $M$ 保边。低孔层及其它直接门按已审声明调用。三桥与双返回首先用独立性取得真实短镜像及各自的面内原伙伴。适用时按有效端口双射预选配对，删选配、接回原跨及伙伴并把真实不交路径压缩；所得接收匹配满足选定的已审完整孔型。沿标签逆展开恰恢复互不相交的外供体与标记内部点、原规定边及一个全短圈。然后逆同构，得到初始输入的圈。 [三桥展开](../R7_THREE_BRIDGE_TWO_RETURN_WHOLE_RECEIVER.md) · [双返回及全称回代](../R7_E16_DISTANCE2_TWO_RETURN_PLAN_REVIEW.md)
5. 若该实际输入没有命中模型所列的合法构造，给孔和计数变量其物理真值，给存在旗标对应实际值，即能满足同支 CP 各条件。基本中央宏、旧五门、完整 A6、新分居及标量表的排除全部依赖已审充分计划。高总重额外高差正跨的区间容量及整面两侧的各自源选择都对应能够同时实现的同一组桥源，守卫和单向旗标容许每份真实余域赋值。偶、奇两份冻结 CP 可满足赋值均可延拓至冻结 CNF，其中阈值、表选择、守卫、常零及宽布尔区间编码已独验，并分别逐行重建了实际 DIMACS。因此两个有限不可满足性结论足以推出任意实际真余域为空。 [基础模型审核](EVEN_GLOBAL_REVIEW.md) · [额外两门审核](ODD_HIGH_GAP_WHOLE_PAIR_REVIEW.md) · [偶 CNF](EVEN_GLOBAL_CNF_REVIEW.md) · [奇 CNF](ODD_HIGH_WEIGHT_CNF_REVIEW.md)

## 终端证据

原输入的穷尽、保边回代和两份 CNF 的归约通过审核。官方 DRAT-trim 固定提交 2e3b2dc0ecf938addbd779d42877b6ed69d9a985，以 MinGW GCC 15.2.0 构建。原源码无改动。编译旗标提供 Windows 所需的等价字节读取，将 getc_unlocked 映射为 getc。实际检查用默认反向模式、文本输入且只允许 RUP。源文件、执行文件、驱动、两输入及日志的散列随回执绑定。相同可执行件和参数先后接受有效 RUP 小证书，拒绝 SAT 伪空子句，也拒绝没有根层单位传播矛盾的 UNSAT 小公式直接加空子句。 [官方固定提交](https://github.com/marijnheule/drat-trim/commit/2e3b2dc0ecf938addbd779d42877b6ed69d9a985) · [三项实际控制](PROOF_TOOLS/drat_trim_official_2e3b2dc/controls/controls.json)

在冻结偶 CNF 上，官方反向检查读到空子句并在 373.523 秒后输出 s VERIFIED，退出零。日志明确记录零 RAT 引理。核对 CNF 散列 1701716ee858ddfacb356dee41f8cdfb7b53046bf101b22698da2065d84341df 及证明散列 74e891aee25f80a80b0dffeb102833779a35bbf071d9eb150b55e9cdc271a2d3。该原生回执完成偶支撑的终端义务。 [偶回执](PROOF_TOOLS/drat_trim_official_2e3b2dc/even_official_drat_trim.json) · [偶日志](PROOF_TOOLS/drat_trim_official_2e3b2dc/even_official_drat_trim.log)

在冻结较高总重奇 CNF 上，同一检查器读到空子句并在 270.897 秒后输出 s VERIFIED，退出零，且零 RAT 引理。核对 CNF 散列 b731f9c347471ec3c5a8e5e7613beac9678d72714961d342b44bd6ffdcb8f6f1 及证明散列 d79dbce279e5c4d9b5f14cfc785eac9e69c309e52e6c57a6a682aebf12398060。该回执完成奇支撑 $D\ge26$ 的终端义务。 [奇回执](PROOF_TOOLS/drat_trim_official_2e3b2dc/odd_official_drat_trim.json) · [奇日志](PROOF_TOOLS/drat_trim_official_2e3b2dc/odd_official_drat_trim.log)

两支均实际验证了空子句。复查了两个模型导出回执、两个求解源回执和原生检查回执对同一 CNF 与证明散列的绑定，以及实际源码、二进制、驱动和两份日志。原生偶回执 SHA-256 为 1cb0d762cad0cdf4172ff8f00f88fb6964de66c30788bdda8de56de0c6d8f24d，原生奇回执为 5d103bc7c90139dae50d2fcc3726576773391ce8af2ecc9e4961ee7c50b3cb6a。

任一原输入均已由直接剥离、最小总重奇支撑的构造或两份无解证书和其保边归约覆盖。最终正文的归约及两份实际证明合在一起完成完整 $\mu=3$。其它 $\mu$ 值、完整 E16 和完整 R7 超出本回执。

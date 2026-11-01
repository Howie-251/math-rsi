# 一般增长下界 Lean 最终语义审计

2026-10-21。审阅者为 fresh GPT-6.1 Sol 子代理；`review_independence: same-family`，`acceptance_status: provisional`。本审计按 `lean-formalize` 的原题反译、实际调用和传递公理核查原则进行，限定为本次全参数增长定理；没有改动 Lean 源码，没有运行 Lean，也没有读取或写入 aris4math_v2。

**结论：在下列实际源码和复用范围内，未发现原题语义不一致、未闭合调用条件或遗留内部前提。** `propertyB_of_general_growth` 已表达并证明指定 k≥17 的全部原始有限简单超图染色命题；`non_propertyB_edges_ge_general_growth` 给出每个原始不可染超图的相应边数下界。本审计是 same-family 语义复核，不代替指定 Grok/Gemini 最终审阅。

## 1. 独立反译与规格对齐

比较依据为 `FORMAL_SPEC_PROPERTYB_GENERAL.md` §§1–3 和 `proofs/propertyb-general/CLIQUE_REFINEMENT.md` 定理 C。定义体和主定理独立反译如下。

设自然数 k≥17，令 d=2^(k−1)，a(p)=1−(1−p)^k，J(p)=∫₀ᵖ(1−y²)^(k−1)dy。接受条件是存在实数 0≤p≤1，使 M(M−1)J(p)/d²<a(p)^(M/d)，其中整数 M≥1。`rsBudget k` 是所有这种整数的最大值 B，且 B 本身具有严格接受见证。令 s=floor(sqrt(B)/(8(1+log k)))。对任意宇宙中的有限类型 V 和由互异有限子集组成的有限边族 E，只要每条边恰有 k 个顶点且 |E|≤B+s，就存在 V→Bool 的函数，使每条边均有 true 顶点和 false 顶点。

`Finset (Finset V)` 保证顶点在每边内不重复、边族不重复；`[Finite V]` 包括任意有限顶点域，允许孤立点、空顶点域和空边族。统一性只有 `∀ e∈E, e.card=k`。最终声明没有点对覆盖、顶点数上限、度数、共度、线性、平衡染色、参数、概率界或证书前提。自然数 k≥17 与规格中的整数 k≥17 一一对应。

独立原始词汇文件 `formal/ReviewAuditGeneralGrowth.lean:10` 不以 `AcceptedAt`、`PropertyB` 等封装词作为最终命题，而是展开积分、最大值、Nat.floor 和 Bool 两色结论，并同时证明该最大值服务于所有 V/E。其 `original_noncolorable_lower_bound`（第36行）给出 B+1+s≤|E|。Lean 没有另行定义图类上的最小值 m(k)；对每个不可染原始 E 的这个点态结论，正是规格中 m(k)≥B+1+s 的下界内容，不需要外加结构性质。

## 2. 关键语义及实际调用

| 核查义务 | 源码与实际证据 | 结论 |
|---|---|---|
| 精确接受式 | `Growth/Definitions.lean:12`，`RS/Integral.lean:17,20`；`AcceptedAt` 使用实数 M(M−1)、精确积分和实指数 | 与规格相同，无浮点替代 |
| 截断不遗漏接受整数 | `Growth/Budget.lean:9` 先证明任意接受 M<k·2^k：M<2^k 时直接成立，M≥2^k 时调用同一接受见证的参数控制 | 截断是已证明覆盖结论，不是额外范围假设 |
| 最大值实际存在并接受 | `Budget.lean:32,37,45,49,65`：对 range(k·2^k) 中接受项取 sup；显式种子 2^k,p=1/k 保证非空；从有限集成员取回最大值本身 | B 为全部接受整数的最大值，非只对某个采样集合最大 |
| 正参数与严格性 | `Seed.lean:81` 排除 p=0；`ParameterControl.lean:54` 从同一接受式得 p>1/k²、J≥1/(2k²)、M/d<2k 和 (M/d)log a>−2log k | 没有假设连续最优参数可达或更换接受参数 |
| floor 的正域 | `Elementary.lean:11,24,36,42,49,56`：整数归纳证明 k⁴≤2^k，推出 sqrt(M)≥k²；分母为正且≤sqrt(M)，故商≥1，Nat.floor≥1 | Nat.floor 没有对负数截断改变正文 floor 的含义 |
| 原始对象至实际点对覆盖反例 | `Structure/Reduction.lean:70` 用所有≤N边反例的最小顶点数；合并未共边两点在每条实际边上单射，统一性保持、边数只减、染色可拉回 | 点对覆盖由原始反例内部构造；重复像边的去重不破坏≤N预算 |
| 实际顶点预算 | `Reduction.lean:107,143` 由真实有序点对覆盖计数得到 n(n−1)≤k(k−1)N，同时推出 k≤n | 没有对抽象库存的可实现性假设 |
| 团界适用于真实边 | `Structure/Clique.lean:19,49,91,125,141`：公共点余集互不交；无公共点时每个星≤k；图团映为实际原边族且保持基数 | 得 r₀=max(k²−k+1, floor((n−1)/(k−1)))，不需要 Gram 加强 |
| 有向计数无因子二错误 | `Structure/Turan.lean:18,42,65,89` 将 `singlePairs` 与实际单交图 darts 双射，gamma=2·图边数，再调用标准 Turán | 同一实际边族的 gamma≤(1−1/r₀)|E|² |
| 实际概率预算单调代入 | `Structure/ProbabilityBudget.lean:9` 用 0<a≤1、|E|≤N、J≥0 将实际边数和 gamma 上界代入旧 RS 核 | 指数单调方向正确，返回原始 `PropertyB` |
| 同一 p、a、J 的增量比较 | `Growth/Main.lean:13` 一次取 hA 的 p，由其参数控制取 hlog；`LogStep.lean:42` 的 a、J 均是 ak k p、jk k p，末项接受式直接用 hA.2.2 | 不同参数的估计没有拼接 |
| 全部 n 的数值前提闭合 | `Elementary.lean:94` 用 n(n−1)预算和 N≤2M 推得 r₀≤2sqrt(M)；`Slack.lean:16` 证明所需严格 log slack | 主定理没有留下顶点数或数值充分条件 |
| 原主定理装配 | `Growth/Main.lean:46` 从 `rsBudget_accepts hk` 取实际见证，`seed_le_rsBudget hk` 解除 M≥2^k，再实际调用 `propertyB_of_accepted_gain` | 只剩 k≥17、统一性与 stated edge budget |

这里只形式化支撑定理 C 所需的公共点二分团界 r₀。未实现正文推论 C.2 中可选的 Gram/min 加强，也未实现参考比较 D/E；这些都没有作为本次最终主定理的未证前提。

## 3. 已读范围和执行范围

逐体读取了 `formal/Aris4Math/General/Structure/` 的6个文件（Definitions、Reduction、Clique、Turan、ProbabilityBudget、Main）以及 `General/Growth/` 的8个文件（Definitions、Seed、ParameterControl、Elementary、Slack、LogStep、Budget、Main），并完整读取 `formal/ReviewAuditGeneralGrowth.lean`。

同时读取 `RS/Definitions.lean`，`RS/Integral.lean` 的定义和基本符号/单调界（前65行），`RS/ProbabilityBound.lean` 的最终实际对象充分判据，检索 `RS/Lift.lean` 的相关接口。其余已完成 RS 概率核视为原有已审实现复用，没有冒称本轮重新审计其全部算法、概率空间或积分组合证明。未做文献搜索或付费模型调用。

本子代理仅执行源码读取、局部检索和本报告写入。源码检索在上述14模块及独立审计文件内未发现 `sorry`、`admit`、新 `axiom`、`native_decide` 或 unsafe/extern 实现；检索到的唯一文字命中是独立审计文件注释中的 “external assumption”。

已读取 root 执行产生的 `build-main01.log`、`final-audit01.log` 及持久执行记录 `VERIFICATION.json`。前者显示指定 `Aris4Math.General.Growth.Main` 构建完成（2574 jobs）；后者展开实际定义、主定理及原始词汇重述，并输出七项传递公理审计，均仅为 `propext`、`Classical.choice`、`Quot.sound`。`VERIFICATION.json` 记录正式构建 session59833 与独立审计 session59058 均已实际取回 `exit_code=0`。这是 root 的实际本机构建和独立导入证据，不是本审阅者执行，不是第二台机器复现。

固定环境读取结果：`formal/lean-toolchain` 为 Lean 4.24.0；`formal/lake-manifest.json` 的 Mathlib rev 为 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。

## 4. 问题与处置

未发现需要修改源码的实质问题。没有未闭合的语义义务或实际 caller 条件需要用户补给。本报告不评价尚未实施的参考比较形式化，也不将 same-family 审核计为指定跨家族最终审阅。

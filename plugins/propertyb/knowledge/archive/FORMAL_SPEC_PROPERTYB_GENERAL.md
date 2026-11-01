# 一般 Property B 下界：正式数学规格

2026-10-21 更新。本规格固定扩展至全部 k≥12 的当前对象、函数和比较范围。原一般 Goal 已完成，本次延伸未新建 Goal；调度状态以工具为准。

## 1. 原始对象

对整数 $k\ge2$，$V$ 为任意有限集合，$E\subseteq\binom Vk$ 为互异边组成的简单超图。允许孤立点和空边族。Property B 是存在 $c:V\to\{0,1\}$，使每条 $e\in E$ 满足 $\{c(x):x\in e\}=\{0,1\}$。

$m(k)$ 是不具有 Property B 的此类超图的最少边数。该最小值存在：$2k-1$ 点上的全部 $k$ 元子集族不可二染。主定理不假设顶点数、点对覆盖、度数、共度、线性或均衡染色。

## 2. 精确定义的旧判据预算

令 $d=2^{k-1}$，$\log$ 为自然对数，
\[
a_k(p)=1-(1-p)^k,\qquad J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.
\]
对 $k\ge12$ 定义
\[
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
\]
这个集合非空且有限，并已证明 $2^k\le B_{\rm RS}(k)<k2^k$。最大整数本身有实际严格见证 $p$；没有假设连续最优参数一定可达。

此预算由本文定义：其正关联端项来自 [RS2000，Appendix A，Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)，单交对精确积分来自 [Claim 2.4的证明，第7页的未编号式](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)。本文引理1将两项用于同一实际算法，再取有向对数上界 $M(M-1)$ 得到接受判据；最大化记号沿用本文定义B.1；k≥12 的非空与有限性由 ANALYTIC_EXTENSION.md 引理2重新证明，原论文没有直接定义这个最大预算函数。积分是显式有理系数多项式；判据等价于非负两侧取$d$次幂后的严格多项式不等式，定义不依赖浮点求根。

## 3. 主定理与整数下界

定义
\[
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor,
\qquad B(k)=B_{\rm RS}(k)+\Delta(k).
\]
**主定理：**
\[
\forall k\in\mathbb Z,\ k\ge12,\quad
\forall V\text{ 有限},\quad \forall E\subseteq\binom Vk,\quad
|E|\le B(k)\ \Longrightarrow\
\exists c:V\to\{0,1\}\ \forall e\in E,\ \{c(x):x\in e\}=\{0,1\}.
\]
因而
\[
\boxed{m(k)\ge B_{\rm RS}(k)+\Delta(k)+1\qquad(k\ge12).}
\]
$\Delta(k)\ge2$在整个范围内由统一不等式证明；展示用的若干数值例子不承担范围外推。无需逐超图枚举或无限生成样例。

## 4. 严格比较与本Goal采用的范围

本Goal的完整比较尾范围固定为 **$K=\{k\in\mathbb Z:k\ge256\}$**。主定理本身保持更强的$k\ge12$范围。比较分两层：

1. 对所有 $k\ge12$，令 $L_{\rm ref}(k)$ 为 BASELINE_COMPARISON.md 式(B2)明确列出的五项包络：RS精确、RS／CK线性、Grill连续、Pluhár纯坏对概率，以及GR–Schönheim覆盖／平衡min–max。已统一证明
   \[
   L_{\rm ref}(k)=B_{\rm RS}(k)+1,
   \quad m(k)\ge L_{\rm ref}(k)+\Delta(k)>L_{\rm ref}(k).
   \]
   每个预算与下界相差一的取整关系均保留；未知渐近起点不冒作有限参数结论。
2. 对所有 $k\ge256$，BASELINE_COMPARISON.md 第5节明确的零锁必要数据测试方案，使用真正离散式(B9)和原文两条度／最大共度上界，不能接受任何整数 $M>B_{\rm RS}(k)$。证明覆盖每个更大 $M$，不是只验一次失败后假设下闭性。所构造的是通过列出测试的数据，并不宣称来自实际边族或完整对称共度矩阵；结论不扩张为全部潜在Grill／多锁方法的能力上限。

因此在指定$K$上获得覆盖全部原始超图的严格新整数下界，并超过已核明确参考界和上述指定测试方案。公开来源的实际核查范围在 round02/final-literature/REPORT.md；没有将未命中搜索解释成穷尽世界最优。该改进不提高领先渐近常数。

## 5. 完整证明与验收证据

规范证明位于 proofs/propertyb-general/：

- CORE_THEOREM.md：同一重染算法的FKG／Jensen项和精确有向单交积分；最小顶点商、实际单交图与原染色结论。
- UNIFORM_INTEGER_GAIN.md：统一参数控制、严格加一、非空有限最大预算。
- CLIQUE_REFINEMENT.md：经典公共点／无公共点团二分及增长整数增益。
- BASELINE_COMPARISON.md：五项参考包络及明确有限数据测试方案的完整解析比较。

本次扩展已并入上述四份规范正文，完整证明 k≥12 的预算良定义、增益至少2、真实原超图调用和五项包络比较。初始扩展推导保存在 [ANALYTIC_EXTENSION.md](context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)，修改前四份正文保存在同目录 `before-paper/`。旧B.2/B.3的17起充分路线保留原范围，新主定理不依赖它们。当前阅读页为 PROPERTY_B_GENERAL_BOUND.html；本次渲染证据位于 `.aris/traces/render-html/2026-10-21_general-bound-k12/`，实际完成状态以该目录报告为准。交接入口 HANDOFF_PROPERTYB_GENERAL.md。

本次 fresh proof-checker 覆盖扩展全部7个源单位、37项义务，`PROOF_AUDIT.json` 为 `PASS_WITH_DECLARED_IMPORTS`，如实标为 same-family/provisional。声明进口及适用域完整列出，没有新增未解数学义务。证据见 [本次审计](context/propertyb-general/bridge-12-16-20261021/PROOF_AUDIT.md)。原核心18源单位／78义务及比较合并审计仍保存在 `context/propertyb-general/round02/formal-audit/`，作为历史依赖证据。

全部 k≥12 的完整增长主定理C已完成端到端 Lean。`rsBudget_characterization_twelve` 给出同一 `rsBudget` 对全部正整数预算的最大性，`rsBudget_parameter_twelve` 给出严格正参数见证，`integerGain_two_twelve` 证明 Δ≥2；`propertyB_of_general_growth_twelve` 从任意裸 `[Finite V]`、`E : Finset (Finset V)` 的均匀性和边数上界推出每条原边两色的 Bool 染色。指定 `Aris4Math.General.Growth.Twelve` 正规构建 exit0（2576 Lake jobs，15.64秒；含缓存依赖），构建后 `ReviewAuditGeneralGrowth12.lean` 以原积分／全域最大预算／floor／Bool 结论独立复述并编译 exit0（7.70秒）。六项核心导出及两个原题声明的传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`，无 `sorryAx`、新增公理或 `native_decide`。证据见 [Lean报告](context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md)、[核验记录](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)、[主源码](formal/Aris4Math/General/Growth/Twelve.lean)及[原题复述](formal/ReviewAuditGeneralGrowth12.lean)。这是本机增量构建与独立导入，不是第二台机器复现。比较定理D（k≥12）／E（k≥256）仍为纸面结论，均未在本次形式化。

新扩展的首轮及最终 Grok 均已有效完成（grok-4.7-build/xhigh/end_turn）。最终审阅全文静态读取 Twelve.lean、独立原题复述及构建／审计日志，确认原始量词、全正整数最大性、严格参数、Δ≥2及两区间衔接，结论认可且无实质问题；未执行 Lean，未重审旧核心模块的全部证明体。准确范围及原回应见 [本次处置](context/propertyb-general/bridge-12-16-20261021/REVIEW_DISPOSITION.md)。本次不调用 Gemini；旧 k≥17 的 Grok/Gemini 有效终审保持为历史证据，见 [旧增长终审](context/propertyb-general-lean-growth/reviews/final/DISPOSITION.md)，不记为新 k≥12 的审阅。模型意见不替代数学证明及实际 Lean 核验。

## 6. 项目隔离

旧$m(5)\ge36$自然语言研究与$m(5)\ge35$ Lean保持暂停，原规格、未解义务和全部成果保留。新一般定理不自动解决这些小参数。所有本次工作只在aris4math；不读取、写入或干扰aris4math_v2。

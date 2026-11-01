# 一般 Property B 下界：正式数学规格

2026-10-21。完整自然语言证明与核心／比较审计已完成；本规格固定最终对象、函数和比较范围。完整目标仍为 GOAL_PROPERTYB_GENERAL_BOUND.md，最终调度状态以Goal工具为准。

## 1. 原始对象

对整数 $k\ge2$，$V$ 为任意有限集合，$E\subseteq\binom Vk$ 为互异边组成的简单超图。允许孤立点和空边族。Property B 是存在 $c:V\to\{0,1\}$，使每条 $e\in E$ 满足 $\{c(x):x\in e\}=\{0,1\}$。

$m(k)$ 是不具有 Property B 的此类超图的最少边数。该最小值存在：$2k-1$ 点上的全部 $k$ 元子集族不可二染。主定理不假设顶点数、点对覆盖、度数、共度、线性或均衡染色。

## 2. 精确定义的旧判据预算

令 $d=2^{k-1}$，$\log$ 为自然对数，
\[
a_k(p)=1-(1-p)^k,\qquad J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.
\]
对 $k\ge17$ 定义
\[
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
\]
这个集合非空且有限，并已证明 $2^k\le B_{\rm RS}(k)<k2^k$。最大整数本身有实际严格见证 $p$；没有假设连续最优参数一定可达。

这是本文准确组合RS重染估计后定义的精确预算函数，不冒称原论文逐字使用同一记号。积分是显式有理系数多项式；判据等价于非负两侧取$d$次幂后的严格多项式不等式，定义不依赖浮点求根。

## 3. 主定理与整数下界

定义
\[
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor,
\qquad B(k)=B_{\rm RS}(k)+\Delta(k).
\]
**主定理：**
\[
\forall k\in\mathbb Z,\ k\ge17,\quad
\forall V\text{ 有限},\quad \forall E\subseteq\binom Vk,\quad
|E|\le B(k)\ \Longrightarrow\
\exists c:V\to\{0,1\}\ \forall e\in E,\ \{c(x):x\in e\}=\{0,1\}.
\]
因而
\[
\boxed{m(k)\ge B_{\rm RS}(k)+\Delta(k)+1\qquad(k\ge17).}
\]
$\Delta(k)\ge1$在整个范围内由统一不等式证明；展示用的若干数值例子不承担范围外推。无需逐超图枚举或无限生成样例。

## 4. 严格比较与本Goal采用的范围

本Goal的完整比较尾范围固定为 **$K=\{k\in\mathbb Z:k\ge256\}$**。主定理本身保持更强的$k\ge17$范围。比较分两层：

1. 对所有 $k\ge32$，令 $L_{\rm ref}(k)$ 为 BASELINE_COMPARISON.md 式(B2)明确列出的五项包络：RS精确、RS／CK线性、Grill连续、Pluhár纯坏对概率，以及GR–Schönheim覆盖／平衡min–max。已统一证明
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

四份正文全部内联于 PROPERTY_B_GENERAL_BOUND.html，公式离线可读；MD、脚本与原始资料作补充。交接入口 HANDOFF_PROPERTYB_GENERAL.md。

正式审计：context/propertyb-general/round02/formal-audit/PROOF_AUDIT.json、BASELINE_ADDENDUM.json、COMBINED_AUDIT.json；核心18个源单位、78项义务及新增比较全覆盖。fresh审计如实标same-family/provisional。

Grok4.7/xhigh和Gemini4 Argon/high均有效审阅核心及完整比较，问题处置分别在 round02/reviews/CORE_DISPOSITION.md 和 BASELINE_DISPOSITION.md。模型意见辅助查错，不替代数学证明。原始回应、实际身份记录、完成状态及阅读范围保留。本课题没有新增Lean形式化或外部合作者独立复现。

## 6. 项目隔离

旧$m(5)\ge36$自然语言研究与$m(5)\ge35$ Lean保持暂停，原规格、未解义务和全部成果保留。新一般定理不自动解决这些小参数。所有本次工作只在aris4math；不读取、写入或干扰aris4math_v2。

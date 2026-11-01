# 一般 Property B 下界：查验与交接

2026-10-21。执行目录为本项目 `aris4math`；旧 m(5)≥36 研究和 m(5)≥35 Lean 保持暂停。

**当前范围：全部 k≥12。** 同一 RS 最大预算和同一增长公式现已覆盖12…16及原有全部k≥17，且 Δ(k)≥2。五项明确参考包络在全部k≥12等于B_RS+1，因而当前下界严格超过该包络至少2；这五项仅指本文准确列出的参考函数。定理E的范围仍为k≥256。原始超图不附加点数、点对覆盖、度数、共度或线性条件。

## 主结果与当前验收状态

本次扩展已完整并入下列四份规范证明源；初始推导保存在 [ANALYTIC_EXTENSION.md](context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)。fresh proof-checker 全覆盖7源单位／37义务，结论 `PASS_WITH_DECLARED_IMPORTS`（same-family/provisional），见[审计](context/propertyb-general/bridge-12-16-20261021/PROOF_AUDIT.md)。同一预算的良定义、严格参数见证和实际原超图连接均已证明；可选数值表不承担统一定理的证明。

全部k≥12的主定理C已完成端到端Lean：[Twelve.lean](formal/Aris4Math/General/Growth/Twelve.lean)导出 `Aris4Math.General.RS.propertyB_of_general_growth_twelve`，仅接受裸有限顶点类型、k元边集及边数≤B_RS+Δ，直接输出每条原边同时含 true/false 的Bool染色。`rsBudget_characterization_twelve`覆盖全部正整数预算的最大性，`rsBudget_parameter_twelve`给出严格正参数，`integerGain_two_twelve`证明Δ≥2。指定构建exit0（2576 Lake jobs，15.64秒，含缓存依赖）；构建后[独立原题复述](formal/ReviewAuditGeneralGrowth12.lean)exit0（7.70秒）。六项核心导出及两个原题声明传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`，无 `sorryAx`、新增公理或 `native_decide`。这是本机实际增量构建与独立导入，不是第二台机器复现。

查验：[本次总报告](context/propertyb-general/bridge-12-16-20261021/REPORT.md)、[Lean报告](context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md)、[核验记录](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)、[构建日志](context/propertyb-general/bridge-12-16-20261021/lean/BUILD.log)、[原题审计日志](context/propertyb-general/bridge-12-16-20261021/lean/REVIEW_AUDIT.log)。比较D（k≥12）和E（k≥256）仍为纸面证明，本次均未形式化。

新扩展首轮及最终Grok均已有效完成（grok-4.7-build/xhigh/end_turn）。最终全文静态读取Twelve、独立原题复述与构建／审计日志，确认原始量词、预算最大性、参数严格性、Δ≥2与12–16／17起两支衔接，认可且无实质问题；未执行Lean，未重审旧核心模块全部证明体。准确范围和原回应见[本次REVIEW_DISPOSITION](context/propertyb-general/bridge-12-16-20261021/REVIEW_DISPOSITION.md)。本次不调用Gemini，旧k≥17的双模型有效终审保留为[历史证据](context/propertyb-general-lean-growth/reviews/final/DISPOSITION.md)，不扩记为本次k≥12审阅。本次未新建Goal，旧pilot Goal保持complete。

当前阅读版已按定义、编号定理／引理、证明重新组织。准确文献定位见 [来源地图](context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md)，改写的命题与依赖对照见 [语义核对](context/propertyb-general/formal-exposition-20261021/SEMANTIC_AUDIT.md)。本次文字修订与此前跨模型数学审阅分别记录。

对每个整数 $k\ge12$，令 $d=2^{k-1}$，并定义

$$
a_k(p)=1-(1-p)^k,\qquad J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

$$
B_{\mathrm{RS}}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
$$

此判据组合 [Radhakrishnan–Srinivasan，Appendix A，Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26) 与 [§2.1，Claim 2.4的证明，第7页未编号的精确积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)，并使用有向单交对数至多 $M(M-1)$。最大整数预算 $B_{\mathrm{RS}}$ 是本文定义；原文没有直接定义这一记号或最大化量。证明包含这个整数最大值的存在性及 $2^k\le B_{\mathrm{RS}}(k)<k2^k$。记

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\mathrm{RS}}(k)}}{8(1+\log k)}\right\rfloor.
$$

主声明是：任意有限顶点集上的简单 $k$ 元超图，若边数至多 $B_{\mathrm{RS}}(k)+\Delta(k)$，则可二染色，使每条边同时含两色。因此

$$m(k)\ge B_{\mathrm{RS}}(k)+\Delta(k)+1.$$

顶点数、点对覆盖、度数、共度和线性不是主定理的附加前提。$\log$ 为自然对数。$B_{\mathrm{RS}}$ 是本文准确组合并定义的 RS 精确判据预算，不冒称原论文以同一名称逐字陈述过这个函数。

## 阅读顺序

首先打开 [完整离线阅读页](PROPERTY_B_GENERAL_BOUND.html)。数学规格为 [FORMAL_SPEC_PROPERTYB_GENERAL.md](FORMAL_SPEC_PROPERTYB_GENERAL.md)。可核对的规范证明源为：

下列规范源已经同步k≥12的主结论；[初始扩展稿](context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)另存本次改动的推导与依赖范围：

1. [一般充分判据与实际超图连接](proofs/propertyb-general/CORE_THEOREM.md)：随机重染、条件正关联、精确有向单交积分、最小顶点商约化、关联矩阵和图论计数。
2. [整数预算与参数控制](proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)：最大预算存在性、严格端点及统一加一。
3. [团结构与增长整数增益](proofs/propertyb-general/CLIQUE_REFINEMENT.md)：公共点／无公共点二分，将结构削减接成 $\Delta(k)$。
4. [新旧界的完整比较](proofs/propertyb-general/BASELINE_COMPARISON.md)：准确的一般旧界及有限位置比较。该文件全部十节已内联同一 HTML；[原始来源核对](context/propertyb-general/round02/baseline-comparison/SOURCES_FINAL.md)保留原文公式、适用条件与阅读范围。

证明不依赖整图枚举、抽样或数值拟合。已有确定性检查用于攻击公式和实现；数学覆盖由正文的全参数推导承担。

## 比较声明的范围

核心定理和五项参考包络比较均覆盖全部 $k\ge12$。覆盖／平衡的 GR–Schönheim min–max 公式在此范围不超过 $2^k$；新证明使用12／13两个精确起点及步长2归纳。RS／CK 线性概率式及使用一般边对数的连续式由上述精确判据控制。

另有 $k\ge256$ 的补充比较：对每个整数 $M>B_{\mathrm{RS}}(k)$，Grill 零锁离散式及指定的两条度／最大共度上界，在**明确列出的必要数据松弛验收方案**中不能通过全部输入。证明直接覆盖全部更大 $M$，不假设可接受预算下闭。所给数据未被宣称由真实超图或完整对称共度矩阵实现；这个补充定理不排除使用额外结构或多锁的未来加强。

增长增益提高整数下界，但没有提高已知领先渐近常数。经典重染、正关联和单交团二分均注明来源；研究贡献应按这个组合及其严格整数比较来评估。

## 审计与复算

核心正式审计入口：[PROOF_AUDIT.md](context/propertyb-general/round02/formal-audit/PROOF_AUDIT.md)，并有 `PROOF_AUDIT.json`、`COVERAGE.json`、`PROOF_SKELETON.md` 和 `PROOF_CHECK_STATE.json`。审计为 same-family/provisional，覆盖 18 个源单位和 78 项义务。[合并审计](context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md)另纳入比较源全部十节及完整拼接。

比较的独立核查：[REPORT.md](context/propertyb-general/round02/baseline-independent/REPORT.md)。两家跨家族审阅的原始请求与回应保存于 [round02/reviews](context/propertyb-general/round02/reviews/)；[核心处置](context/propertyb-general/round02/reviews/CORE_DISPOSITION.md)和[比较与最终拼接处置](context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md)记录实际完成证据、阅读范围及主代理核算。模型意见是辅助审阅，数学依据是正文的完整推导。

当前阅读页为 [一般下界全文](PROPERTY_B_GENERAL_BOUND.html) 与[完整Lean阅读页](PROPERTY_B_GENERAL_LEAN.html)。本次渲染与保真记录统一放在 [.aris/traces/render-html/2026-10-21_general-bound-k12/](.aris/traces/render-html/2026-10-21_general-bound-k12/)，完成状态以实际报告为准；不沿用旧版本的公式数量或展示检查充作本次证据。原来源地图、文献比较表及旧渲染记录继续保留。

从项目根目录复现本次实际主结论：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.General.Growth.Twelve
lake env lean ReviewAuditGeneralGrowth12.lean
```

原k≥17阶段的[正式报告](context/propertyb-general-lean-growth/REPORT.md)、[主模块](formal/Aris4Math/General/Growth/Main.lean)、[独立复述](formal/ReviewAuditGeneralGrowth.lean)及[17元试点](PROPERTY_B_GENERAL_LEAN_PILOT.html)保持历史记录，不能用旧入口代替本次Twelve主模块验收。

以下可选命令从项目根目录执行，只复核辅助程序，不取代正文证明：

```sh
python3 context/propertyb-general/round02/formal-audit/counterexample_checks.py
python3 context/propertyb-general/round02/baseline-independent/check.py
python3 context/propertyb-general/round02/examples/check_examples.py
```

第一项所需解释与输出见同目录报告；它枚举的是有限小例的攻击测试。第二项独立核对离散归一化和整数取整。第三项验证展示用的保守增益数值，不声称算出 $B_{\mathrm{RS}}(k)$ 本身。核心证明没有依赖浮点求根结果。完整增长主定理C的Lean核验见上方正式报告；本段三个命令仅核对纸面证明的辅助程序。

## 保存与后续查验

本轮完整成果从 [PROGRESS](context/propertyb-general/PROGRESS.md) 和 [一般方法综合](research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md) 定位；正式任务范围保存在 [GOAL_PROPERTYB_GENERAL_BOUND.md](GOAL_PROPERTYB_GENERAL_BOUND.md)。原有 `research-wiki/`、全部证明源、审阅和复算证据继续保留。旧 35 Lean 与 36 研究保持暂停，本一般定理没有解决它们。合作者可先通读 HTML，再按上述顺序核规范源与证据；若发现具体错误，按原式和实际对象核查修正。

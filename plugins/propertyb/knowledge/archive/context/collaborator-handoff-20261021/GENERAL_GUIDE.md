# 一般 Property B 定理：合作者阅读与复算指南

本指南对应2026-10-21的最终文件。入口是项目根的 [PROPERTY_B_GENERAL_BOUND.html](../../PROPERTY_B_GENERAL_BOUND.html)，它将完整数学证明、文献比较和结果图内联到一份离线阅读页。形式证明阅读页为 [PROPERTY_B_GENERAL_LEAN.html](../../PROPERTY_B_GENERAL_LEAN.html)，规范源与证据仍按原相对目录保存。下面的程序命令是已有脚本的复现入口；本次交接整理没有重跑数学计算或Lean。

## 先确认主命题与证据范围

对每个整数 $k\ge12$，令 $d=2^{k-1}$、$a_k(p)=1-(1-p)^k$、$J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy$，并定义

$$B_{\rm RS}(k)=\max\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\ M(M-1)J_k(p)/d^2<a_k(p)^{M/d}\},$$

$$\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\ln k)}\right\rfloor.$$

主定理C证明：$2^k\le B_{\rm RS}(k)<k2^k$、$\Delta(k)\ge2$，且**任意有限简单 $k$ 元超图**在边数至多 $B_{\rm RS}(k)+\Delta(k)$ 时可二染，即 $m(k)\ge B_{\rm RS}(k)+\Delta(k)+1$。没有顶点数、点对覆盖、度数、共度或线性条件作为外部假设。这些结构只在证明内部通过最小反例约化使用。

|结果|当前范围与性质|首先核对的文件|
|---|---|---|
|统一增长主定理C|全部 $k\ge12$，端到端Lean已完成|[Twelve.lean](../../formal/Aris4Math/General/Growth/Twelve.lean)、[独立原题复述](../../formal/ReviewAuditGeneralGrowth12.lean)|
|五项明确参考包络比较D|全部 $k\ge12$，纸面证明；包络等于 $B_{\rm RS}+1$|[BASELINE_COMPARISON.md](../../proofs/propertyb-general/BASELINE_COMPARISON.md)，定义D.1、定理D|
|指定零锁必要数据测试方案比较E|全部 $k\ge256$，纸面证明；拒绝全部 $M>B_{\rm RS}$|同文件，定义D.2及定理E；数据松弛并非真实超图构造，也不覆盖所有未来多锁方法|
|加强充分判据C.2的数值应用|$k=12,\ldots,16$ 的精确判据最大预算；数值证书与不同实现复算|[NUMERIC_REPORT.md](../propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md)、[独立复算报告](../propertyb-general/bridge-12-16-20261021/INDEPENDENT_NUMERIC_CHECK.md)|

这里 $B_{\rm RS}$ 是**本文组合RS两项估计后定义的最大整数预算**，不是RS原论文的一条同名定理。统一结果提高该明确整数基线；没有声称提高领先渐近常数或穷尽全部文献方法。

## 建议的阅读顺序

1. 读离线HTML首屏和 [FORMAL_SPEC_PROPERTYB_GENERAL.md](../../FORMAL_SPEC_PROPERTYB_GENERAL.md)，固定原始超图量词、预算与下界的“加1”关系。图中蓝线、紫点、红点有不同证明状态，须按图注阅读。
2. 依次读四份规范证明：[CORE_THEOREM.md](../../proofs/propertyb-general/CORE_THEOREM.md)（共同重染过程、实际有向单交对、最小顶点商与概率界）→[UNIFORM_INTEGER_GAIN.md](../../proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)（预算良定义与接受参数控制）→[CLIQUE_REFINEMENT.md](../../proofs/propertyb-general/CLIQUE_REFINEMENT.md)（公共点二分、C.2及增长定理C）→[BASELINE_COMPARISON.md](../../proofs/propertyb-general/BASELINE_COMPARISON.md)（D/E的准确比较对象）。源中仍保留17起的部分旧充分引理；当前C/D的12起证明已在同一规范源中接齐。
3. 针对12–16的向下延伸，读 [ANALYTIC_EXTENSION.md](../propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md) 和 [PROOF_AUDIT.md](../propertyb-general/bridge-12-16-20261021/PROOF_AUDIT.md)。核心调整是12起的严格种子、$r\le3\sqrt M$ 与严格余量，以及D的12/13双起点步长2归纳；数值表不是统一定理的前提。
4. 对照 [完整Lean报告](../propertyb-general/bridge-12-16-20261021/lean/REPORT.md)、`formal/Aris4Math/General/` 下的RS→Structure→Growth依赖链和 `Twelve.lean`。`rsBudget_characterization_twelve`覆盖所有正整数的最大性，`rsBudget_parameter_twelve`给实际严格正参数，`integerGain_two_twelve`给增益至少2，`propertyB_of_general_growth_twelve`直接给原Bool染色。
5. 最后检查数值及比较证据，避免把有限图点验算当作全参数定理的证明。已有总交接 [HANDOFF_PROPERTYB_GENERAL.md](../../HANDOFF_PROPERTYB_GENERAL.md) 保留原始报告与日志导航。

## Lean复现与审阅证据

依赖由 `formal/lean-toolchain`、`formal/lakefile.toml` 和 `formal/lake-manifest.json`固定：Lean 4.24.0，Mathlib提交 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。一般模块另导入 `formal/Aris4Math/Counting.lean`；仅复制General目录不足以构建。

在项目根执行，或将首行改为收到的包根目录：

```sh
cd /path/to/aris4math
cd formal
lake build Aris4Math.General.Growth.Twelve
lake env lean ReviewAuditGeneralGrowth12.lean
```

接收方需要已安装的Elan/Lake及锁定依赖；本机使用项目 `.tools/elan`，该机器路径不作为可移植依赖。默认 `lake build` 的目标仍是旧 `Aris4Math.Main`，不能代替上述指定模块。

[VERIFICATION.json](../propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)、`BUILD.log`、`REVIEW_AUDIT.log`记录本机指定构建与构建后独立原题编译：均exit0；六项核心导出和两项独立声明的传递公理仅 `propext`、`Classical.choice`、`Quot.sound`，无 `sorryAx`、新增公理或 `native_decide`。这是已有本机增量核验，不是第二台机器复现。

新12起的 [REVIEW_DISPOSITION.md](../propertyb-general/bridge-12-16-20261021/REVIEW_DISPOSITION.md) 及同目录Grok原始JSON记录有效 `grok-4.7-build/xhigh/end_turn`。Grok静态读新源码、原题复述及日志，没有执行Lean；本轮没有Gemini。旧17起的 [双模型最终处置](../propertyb-general-lean-growth/reviews/final/DISPOSITION.md) 和更早 [概率核心C处置](../propertyb-general-lean-pilot/reviews/C/DISPOSITION.md)保留各自实际范围，不升级为新12起的双模型审阅。fresh proof-checker为same-family/provisional；确定性Lean结果单列。

## 数值证书、主图与复算

蓝线有53个展示点 $k=12,\ldots,64$。17–64的 `general_data.json` 只证明保存的 $M_*\le B_{\rm RS}$ 及保守 $g_*\le\Delta$，没有求出真正最大预算；12–16的数值证书另给旧RS/C.2两种判据的精确整数最大预算。主图紫色菱形目前只画C.2的12、13：

|$k$|参考下界 $B_{\rm RS}+1$|蓝线统一保守下界|C.2接受预算|C.2下界（相对参考增益）|
|---:|---:|---:|---:|---:|
|12|4633|4635|4646|4647（14）|
|13|9539|9542|9563|9564（25）|
|14|19602|19606|19646|19647（45）|
|15|40215|40221|40293|40294（79）|
|16|82377|82386|82492|82493（116）|

C.2本身是覆盖全部原超图的纸面充分判据。其数值求值使用精确有理积分、定向对数区间和下一整数全参数排除；全部15份主要接受见证及10份全参数排除、8030个叶区间经不同积分递推、顶点预算二分和 `mpmath.iv` 对数独立复算通过。它们不是逐项Lean优化认证，也不是 $m(k)$ 的精确值。新两点的再次接受见证重算保存在 [C2_12_13_READBACK.json](../propertyb-general/c2-figure-20261021/C2_12_13_READBACK.json)。

以下命令均从包根运行。前两项只需Python标准库，读取保存证书重放；不会重新进行参数优化：

```sh
python3 context/propertyb-general/bound-figure-20261021/general_data.py --verify
python3 context/propertyb-general/bridge-12-16-20261021/numeric_bridge.py --verify
```

独立实现需要 `mpmath`（原记录版本1.4.1），其命令会重写同目录 `INDEPENDENT_NUMERIC_CHECK.json`为本次结果。建议先保存收到的证据副本，再重放：

```sh
python3 context/propertyb-general/bridge-12-16-20261021/INDEPENDENT_NUMERIC_CHECK.py
```

如需重新生成候选证书，去掉相应 `--verify`；这两项生成额外依赖 `mpmath`，并会重写证书JSON。原项目记录的解释器为 `.tools/math-python/bin/python`，接收方可用自己已配置的Python环境。

图源是 [RESULTS_FIGURE.md](../../proofs/propertyb-general/RESULTS_FIGURE.md)，绘图程序为 [plot_bounds.py](../../figures/propertyb_bounds/plot_bounds.py)，成品含SVG/PNG/单图PDF及 [三页矢量PDF](../../figures/propertyb_bounds/propertyb_bounds.pdf)。先复核证书，再派生五点蓝线与绘图：

```sh
python3 context/propertyb-general/bridge-12-16-20261021/build_bridge_plot_data.py
python3 figures/propertyb_bounds/plot_bounds.py
```

绘图需Matplotlib（原记录3.11.2），还读取 `bound-figure-20261021/small_k_sources.json`、`locks-vs-uniform-20261021/baselines/MATCHED_BASELINES.json`及 `k12-lock-pilot-20261021/pilot/SUMMARY.json`。这些图依赖已在清单中保留。红色k12的4661是完整691429局部型的锁点候选，尚未完成两／三锁的第二次完整复算和Lean；13没有新的完整红锁点下界。红色小参数的更详证据由对应小参数交接说明承担。

辅助比较复核的已有入口为：

```sh
python3 context/propertyb-general/round02/formal-audit/counterexample_checks.py
python3 context/propertyb-general/round02/baseline-independent/check.py
python3 context/propertyb-general/round02/examples/check_examples.py
```

分别是有限小例攻击、离散归一化／整数取整、保守展示增益核对；都不替代正文全域证明。

## 文献及准确定位

[SOURCE_MAP.md](../propertyb-general/formal-exposition-20261021/SOURCE_MAP.md)给出处与读过的范围，[LITERATURE_COMPARISON_TABLE.md](../../proofs/propertyb-general/LITERATURE_COMPARISON_TABLE.md)给当前比较表。可直接在随包PDF核对：

|文献|本地PDF／原稿|本证明的准确使用处|
|---|---|---|
|Radhakrishnan–Srinivasan，2000|`ref/radhakrishnan_srinivasan_2000_two_coloring.pdf`（27页作者稿）|p.4算法；§2.1 Claim 2.4 proof p.7的未编号精确积分；Appendix A Claim A.1 pp.26–27。这里页码不是期刊页码。|
|Cherkashin–Kozik，2015|`ref/general-propertyb/cherkashin_kozik_2015_published.pdf`及txt|刊p.408 Theorem 1；刊pp.409–410，特别Eq.(2.3)。不要混用2013 arXiv编号。|
|Pluhár，2009|`ref/pluhar_2009_greedy_colorings.pdf`（6页作者稿）|pp.2–3 Claim 1 proof中的准确排列概率；p.3 Corollary 1。|
|Grill–Linzmayer，2024 v3|`ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf`；`ref/source_packages/grill_linzmayer_2403_05674/PropB.tex`|§2 Eqs.(5)–(8) pp.3–4；Theorem 1 p.7只给k5–9；Theorem 2 p.8是固定v特例。|
|Goldberg–Russell，1995|`ref/goldberg_russell_1995_toward_m4.pdf`，比较目录另有全文txt|覆盖／平衡包络及GL重述的定位按 `SOURCES_FINAL.md`；不把固定参数结论放大。|

公共点／无公共点的单交族二分和所需正关联特例在正文自含证明；Deza和FKG的历史归属不被包装成读过其原证明的外部进口。

## 可移植依赖与历史材料

数学阅读页已经内嵌SVG公式及三幅图，阅读无需本机ARIS或网络。若要重新生成HTML，`context/rendering/render_propertyb_general.py` 经 `render_propertyb33.py`、`render_proof_package.py`导入ARIS `render-html/scripts/render_html.py`、模板及 `compose_proof_package.py`，并需Playwright/Chromium、构建时MathJax加载；现有脚本还写有本机代理 `127.0.0.1:7890`。这是重渲染的外部依赖，不能把随包源码说成开箱可离线重渲染；不会影响已有HTML离线阅读或Lean／数值复算。

`NUMERIC_REPORT.md`、旧来源核对与审阅中出现的“只到17/32”“尚未形式化”是原阶段记录；当前范围以本指南、规范四源、`Twelve.lean`与12起报告为准。旧35 Lean／36研究继续暂停，本包的一般定理没有解决那些题，也不涉及独立编码理论项目。

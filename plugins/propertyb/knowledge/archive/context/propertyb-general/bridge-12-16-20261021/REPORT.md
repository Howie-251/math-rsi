# 从 k=12 起的统一 Property B 下界

2026-10-21。原来的12–16参数空档已由同一个一般定理闭合，且完整主定理已经通过Lean。小参数5–11的逐项成果与12起的一般定理在参数范围上连续；两类成果的证明方式仍分别标明。

## 统一定理

沿用正文的RS精确组合判据最大可染预算 $B_{\rm RS}(k)$，对每个整数 $k\ge12$ 定义

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则

$$
2^k\le B_{\rm RS}(k)<k2^k,\qquad \Delta(k)\ge2,
\qquad m(k)\ge B_{\rm RS}(k)+1+\Delta(k).
$$

这里的结论量化任意有限简单 $k$ 元超图，不附加点数、点对覆盖、度数或线性条件。五项明确参考下界的最大值 $L_{\rm ref}(k)$ 也在整个 $k\ge12$ 范围等于 $B_{\rm RS}(k)+1$，因此该定理相对这个参考包络统一增加 $\Delta(k)$。

完整正文与图为 [PROPERTY_B_GENERAL_BOUND.html](../../../PROPERTY_B_GENERAL_BOUND.html)，形式证明阅读页为 [PROPERTY_B_GENERAL_LEAN.html](../../../PROPERTY_B_GENERAL_LEAN.html)。规范证明源仍是项目原有 `proofs/propertyb-general/` 四份文件；本目录 `before-paper/` 保留修改前版本。

## 为什么能向下延伸

证明只需三处有针对性的调整。首先，在预算 $2^k$、参数 $p=1/k$ 处，用二项式前三项得到 $a_k(p)>3/5$，于是从12起已有严格接受种子。其次，允许单交团预算满足 $r\le3\sqrt M$，仍有

$$
(2+2\log k)s+2\le\frac{\sqrt M}{4}+2
<\frac{\sqrt M}{3}\le\frac Mr,
\qquad \sqrt M\ge64.
$$

同一个接受参数足以承担原公式的增益，无需逐个参数的超图搜索。最后，覆盖／平衡参考式在12、13两处验证起点，再按步长2归纳；这给出全部 $k\ge12$ 的参考包络比较。

初始完整推导为 [ANALYTIC_EXTENSION.md](ANALYTIC_EXTENSION.md)，规范主证明为 [定理C](../../../proofs/propertyb-general/CLIQUE_REFINEMENT.md)，参考比较为 [定理D](../../../proofs/propertyb-general/BASELINE_COMPARISON.md)。旧B.2/B.3的17起充分路线保留其范围；新主定理不依赖它们。定理E仍从256起。

## Lean与审阅

主入口为 [Twelve.lean](../../../formal/Aris4Math/General/Growth/Twelve.lean)，导出 `Aris4Math.General.RS.propertyB_of_general_growth_twelve`。独立原命题为 [ReviewAuditGeneralGrowth12.lean](../../../formal/ReviewAuditGeneralGrowth12.lean)，同时展开全正整数最大性、原积分、取整公式和原Bool染色。

指定主模块构建通过（2576 Lake任务，含既有依赖重放）；构建后独立原题审计也通过。传递公理只有 `propext`、`Classical.choice`、`Quot.sound`，无未完成证明或新增公理。实际日志、时间和准确命令见 [Lean报告](lean/REPORT.md)与[核验记录](lean/VERIFICATION.json)。比较D/E没有在本轮形式化。

fresh数学审计覆盖7个单位、37项义务；Grok完成解析讨论和新Lean最终接口审阅，在所读范围内未发现实质问题。完整身份、阅读范围和两处文字纠正保存在 [REVIEW_DISPOSITION.md](REVIEW_DISPOSITION.md)。按用户指令，本轮不调用额度耗尽的Gemini。

## 可选的数值加强

一般定理不需要下表才能成立。若直接优化同一个结构加强判据C.2，新增五个参数还有更强的逐项结果：

|$k$|指定旧参考下界 $B_{\rm RS}+1$|统一定理保守增益 $\Delta_{\rm cert}$|统一定理的可展示下界|C.2直接数值下界|
|---:|---:|---:|---:|---:|
|12|4633|2|4635|4647|
|13|9539|3|9542|9564|
|14|19602|4|19606|19647|
|15|40215|6|40221|40294|
|16|82377|9|82386|82493|

图中蓝线统一使用原 $\Delta$ 公式的保守保证值，不把最后一列的逐项优化混成一般定理的增益。C.2数字有严格接受证书和下一预算的全参数排除；独立实现完整复算通过。细节为 [NUMERIC_REPORT.md](NUMERIC_REPORT.md)和[独立复算](INDEPENDENT_NUMERIC_CHECK.md)。这些数字不是 $m(k)$ 的精确值，也不声称已比较所有可能文献方法。

## 当前文件与恢复

图表数据、生成器和检查见 [CHART_SYNC.md](CHART_SYNC.md)；主图仍为英文，同一 $k$ 横轴，红色小参数读左轴、蓝色统一定理读右轴，各自差值基线明确。正文、形式化阅读页、正式规格、交接与research wiki同步本次范围。旧35 Lean和36研究及独立编码理论项目保持原状态；本轮未创建或恢复Goal。

## 展示交付核验

主阅读页1027处公式、Lean阅读页118处公式均已内嵌SVG；离线桌面／手机检查通过。fresh保真审阅对Lean全文及主页面本次范围／图注检查PASS、零问题（same-family/provisional），见[审阅记录](../../../.aris/traces/render-html/2026-10-21_general-growth-lean-k12/review.json)。数学、形式核验与展示保真分别记录。

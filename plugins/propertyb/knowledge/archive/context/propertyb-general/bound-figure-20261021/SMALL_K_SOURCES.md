# 小 k 图值及文献来源核对

2026-10-21。图的纵轴是最少不可二染边数 m(k) 的下界；它比相应“至多 M 边可二染”预算大1。本表比较选定的此前文献结果与文献公式，不声称列出当前世界纪录或全部文献中的最强值。没有新建研究 Goal、启动跨模型审阅或运行 Lean。

| k | 选定此前文献／公式基线 | 本次指定展示 | 基线性质及定位 |
|---:|---:|---:|---|
|4|23|不作新改进|Östergård (2014) 已发表精确值 m(4)=23；见下列书目与读取范围。|
|5|32|35|Grill–Linzmayer v3，§3末 Theorem 1，p.7。|
|6|64|65|同上。|
|7|128|130|同上。|
|8|263|266|同上。|
|9|538|542|同上。|
|10|1070|1112|GL v3 §2 p.4 Eq.(7) 本次精确代入；**公式基线，非原文报告值**。|
|11|2213|2275|同上。|

Grill–Linzmayer 的 Theorem 1 明确列出的普遍数值界只到 k=9；其中途单锁／双锁数及 §4 固定 v=2k+1 的结论均不替代该定理。原始版本为 Karl Grill and Daniel Linzmayer, *Improved Lower Bounds for Property B*, [arXiv:2403.05674v3](https://arxiv.org/abs/2403.05674v3)，2024-06-20 修订；[Theorem 1 原PDF p.7](https://arxiv.org/pdf/2403.05674v3#page=7)。本次直接以 pdftotext 读取本地 v3 PDF 的 pp.3–4、7，并对照本地 TeX；文件为 `ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf` 和 `ref/source_packages/grill_linzmayer_2403_05674/PropB.tex`。

## k=10、11 的严格公式代入

GL v3 §2 的 [Eq.(6)，p.3；Eq.(7)，p.4](https://arxiv.org/pdf/2403.05674v3#page=3) 给出连续贪心失败判据。取其同页明确的有序单交边对界 γ≤M(M−1)，并取 0≤x≤1/2：

\[
F(k,M,x)=2Mx^k+M(M-1)\int_x^{1-x}u^{k-1}(1-u)^{k-1}\,du<1
\quad\Longrightarrow\quad m(k)\ge M+1.
\]

本次选用简单有理见证，直接以 Python Fraction 整数有理运算验证：

| k | M | x | F 的严格精确值 | 十进制仅供阅读 |
|---:|---:|---:|---|---:|
|10|1069|81/200|15916312165999946484170523963892172207690827767 / 15931801600000000000000000000000000000000000000|0.9990277663261854|
|11|2212|103/250|59651917368901694395512374936811377728807950466119447 / 59671378949133213609457015991210937500000000000000000|0.9996738540222422|

每行分子严格小于分母，所以分别支持下界1070与2213。这是既有文献公式的本次可行代入，不声称原作者报告了这两个整数，也不声称该判据的全局最优值。复算只需：

```python
from fractions import Fraction as F
from math import comb
for k, M, x in [(10, 1069, F(81, 200)), (11, 2212, F(103, 250))]:
    def A(z):
        return sum((F((-1)**j * comb(k-1, j), k+j) * z**(k+j)
                    for j in range(k)), F(0))
    upper = 2*M*x**k + M*(M-1)*(A(1-x) - A(x))
    assert upper < 1
    print(k, M+1, upper)
```

## k=4 文献锚点

Patric R. J. Östergård, *On the minimum size of 4-uniform hypergraphs without property B*, **Discrete Applied Mathematics 163(2)** (2014), 199–204, [DOI:10.1016/j.dam.2011.11.035](https://doi.org/10.1016/j.dam.2011.11.035)。本次核对了[作者所在机构的正式书目](https://research.aalto.fi/en/publications/on-the-minimum-size-of-4-uniform-hypergraphs-without-property-b/)及[出版社作者页中的文章摘要](https://www.sciencedirect.com/author/7005657523/patric-r-j-ostergard)；后者确认该文通过穷尽计算闭合精确值。全文在本次工具访问中未取得，因此不编造定理编号或具体定理页码。k=4可作为图的独立精确值锚点23，不应标成本项目的新改进；JSON 的 ours 为 null。

## 本项目／合作者值的展示状态

m(5)≥35是本次用户指定的展示值；对应35阶段的完整 Lean 尚未完成，不能借已有 m(5)≥34 的 Lean 验收扩大其证明状态。

k=6,…,11 来自合作者材料。六组原算术证书共103,190个局部参数型已在本机退出0；它们不是整图枚举。这些材料目前是纸面证明候选加实际算术重放，尚无本项目全链跨家族终验或 Lean 终验。准确范围及原文件链接见 [PROPERTY_B_SMALL_K_TRANSFER.md](../../../research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)。图例宜使用“本文／合作者小 k 结果（证明状态见说明）”，并在图下注明这一状态；不能将它们统一标为本项目已完成 Lean 的结论。

k=12,…,16本次没有核定图值；保留空白，勿连线插值成数学下界。一般 k≥17 图另用已完成的增长定理及其准确比较基线。

# 最终文献核查：实际来源与检索记录

2026-10-21；有界一次性检索。主判断见[REPORT.md](REPORT.md)。搜索引擎结果只作发现；数学适用性依据下列原始论文/出版方页面的实际可读部分。

## 原始来源

|canonical ID|原始URL|实际读到的部分|状态|
|---|---|---|---|
|10.1007/978-3-032-18810-6_9|https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9|元数据、摘要、25条完整公开参考表|正文订阅，未读|
|2504.12430v2|https://arxiv.org/html/2504.12430v2|引言、定义、Theorem1–3与Proposition1全部结果陈述|已读相关范围；v2日期2026-06-07|
|2504.12430v1|https://arxiv.org/html/2504.12430v1|引言与结果，后由v2替代|不使用旧版本条件作为最终公式|
|1903.11708v1|https://arxiv.org/html/1903.11708v1|引言、Theorem1、B_s定义|未重审后续证明；期刊2022排版未读|
|2610.07379v1|https://arxiv.org/html/2610.07379v1|§1–2模型与量词、主结果摘要、引用链|已确认a.a.s.随机范围|
|10.3390/axioms15040252|https://www.mdpi.com/2075-1680/15/4/252|原始页面搜索提取的摘要、引言、§2部分、§10、Theorem6收敛率说明|直接open/PDF与urllib403，未读完整§9|
|10.1070/RM9905|https://doi.org/10.1070/RM9905|期刊原始元数据；MathNet原PDF搜索索引的相关段落|PDF直接链接跳转/超时，未读全文|
|MathNet原PDF链接（瞬时URL）|https://www.mathnet.ru/links/044364f63d508367639a3ebbff93649a/rm9905_eng.pdf|检索返回§2.1、§4等原PDF段落；直接open转首页|不是有效下载|
|MathNet原PDF备用瞬时URL|https://www.mathnet.ru/links/8800749648dfae10406420e8138fc20d/rm9905_eng.pdf|检索返回相关算法段落；直接open错误|不是已读完整PDF|
|panchromatic原始论文（误读排除）|https://www.mathnet.ru/links/db2141094d8339dc98f5549b9602d179/sm7480_eng.pdf|原PDF搜索提取的m(n)公式与RS归属|仅核sqrt3−1带2^(n−1)，未读全文|

## 本轮执行的网页查询

以下均为实际执行字符串；部分极宽查询返回大量同名Property B或无关two-color命中，未将它们列为数学证据。

近期普遍界：

- `"property B" "lower bound" 2025 2026 hypergraphs`
- `"property B" "lower bound" 2024 Grill`
- `"non 2-colorable" hypergraphs "lower bound" 2025 2026`
- `"property B" "lower bound" 2025 2026 -site:researchgate.net -site:en.wikipedia.org`
- `"property B" "leading constant"`
- `"property B" Radhakrishnan Srinivasan 2026`
- `"Property B" "2025" hypergraphs lower bounds uniform`
- `"Property B" "2026" Grill Linzmayer Overview`
- `"uniform hypergraphs" "lower bound" "sqrt" "2025" colorable`
- `"Improved Lower Bounds for Property B" citations 2025 2026`
- `"Property B" "1/√2"`
- `"Property B" "constant" "lower bounds" 2024 2025 2026`
- `"property B" "lower bound" "Shabanov" constant`
- `"Property B" "lower bounds" "2026" -site:researchgate.net -site:en.wikipedia.org -site:erdosproblemaday.com -site:arxiv-troller.com`
- `"hypergraph" "2-coloring" "lower bounds" "2026" property`
- `"hypergraph" "two-colouring" "lower bound" "2025" property B`
- `"m(n)" "property B" "constant" "sqrt"`
- `"hypergraph" "2-colorability" "lower bound" "2024" "Radhakrishnan"`
- `"property B" "lower bound" "1/sqrt" -site:scribd.com`
- `"non-2-colorable" "2025" "lower" "uniform"`

定点原始引用链：

- `"An Overview of Property B" Grill Linzmayer pdf`
- `"An Overview of Property B" site:tuwien.at`
- `"property B" "m(n)" "2019" lower bounds Demidovich`
- `"Extremal problems in hypergraph colourings" 2020 pdf`
- `"Extremal problems in hypergraph colourings" "best" "0.7"`
- `"Extremal problems in hypergraph colourings" "2.1.3"`
- `site:mathnet.ru "rm9905" "2.2" "Srinivasan"`
- `"Extremal problems in hypergraph colourings" "2.1.4"`
- `"Extremal problems in hypergraph colourings" "Radhakrishnan" "constant"`
- `"Extremal problems in hypergraph colourings" "√3"`
- `"Extremal problems in hypergraph colourings" "sqrt{3}"`
- `"Extremal problems in hypergraph colourings" "constant" "2.3"`
- `"hypergraph" "sqrt{3}-1"`

近期旁支论文：

- `"Sharp Choice Number Thresholds for Complete Bipartite Graphs"`
- `site:mdpi.com/2075-1680/15/4/252 "Property B" "Theorem"`
- `site:mdpi.com/2075-1680/15/4/252 "9." "Erdős"`
- `"Sharp Choice Number Thresholds" pdf axioms-15-00252`
- `"Sharp Choice Number Thresholds for Complete Bipartite Graphs" "2" "k-uniform"`
- `"Sharp Choice Number Thresholds for Complete Bipartite Graphs" "union"`
- `"Sharp Choice Number Thresholds for Complete Bipartite Graphs" "balanced" "2"`
- `"Sharp Choice Number Thresholds for Complete Bipartite Graphs" "Property B" "log"`
- `"Fractional hypergraph coloring" arxiv`

## arXiv API

通过规范helper执行，均设置`ARIS_REPO=/Users/rfy_naiveai/Desktop/aris_main`：

1. `python3 "$ARIS_REPO/tools/arxiv_fetch.py" search 'all:"property B"' --max 20`，exit0；复核既有canonical IDs与2610.07379；未将终端输出冒充保存文件。
2. `python3 "$ARIS_REPO/tools/arxiv_fetch.py" search '(all:"property B" OR all:"2-colorability" OR all:"two-colorability") AND submittedDate:[202401010000 TO 202610212359]' --max 30`，exit0；原始JSON为[ARXIV_RECENT_SEARCH.json](ARXIV_RECENT_SEARCH.json)。

第二次30项为相关性限制返回，不能称arXiv全部近期相关论文。新增2504.12430由额外网页检索命中，实际以当前v2补核。2609.12214/2609.31574/2511.03036依据API原始摘要排除，余同名或无关命中不逐篇读全文。

## 访问失败

MDPI直接网页、/htm、/pdf：工具错误或HTTP403。Python最初requests不可用，改用标准urllib后同样403；没有为此安装依赖或绕过访问要求。MathNet瞬时PDF链接直接open跳转首页/报错，urllib短超时未得到有效PDF。Springer综述为订阅正文，未尝试购买。以上均不记为全文阅读。

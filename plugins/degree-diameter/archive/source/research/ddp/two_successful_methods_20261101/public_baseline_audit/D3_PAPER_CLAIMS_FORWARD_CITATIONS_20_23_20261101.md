# 20–23度D3：论文怎样声明“最大”，后续是否引用／更新

**结论：确有明确的“largest known／best published”声明，也有可逐条核验的后续引用和数值更新。但这些声明带日期和范围，不是数学最优性证明；2791及21–23度的三个数不能写成原文逐格宣布的世界纪录。** 本记录为root更新HTML提供依据，不再重做七格数值检索。

## 原文声明：说了什么，没说什么

| primary | 原文与位置 | 声明的准确范围 |
|---|---|---|
| [Rajiv July，2026-07-03](https://doi.org/10.5281/zenodo.21180071) | abstract：**“We present new largest known graphs”**；Theorem1／Table1明确20/D3=2202 | 对四个一般N(d,3)格子的当时largest-known声明；实际用Cayley构造，并非只声称Cayley子表。比较Wiki快照2026-07-02，不是最优性证明。 |
| [Rajiv August，2026-08-24](https://doi.org/10.5281/zenodo.22073603) | abstract：**“improve the best published lower bounds”**；Theorem1／Table1明确20/D3=2750 | Table1限定为作者当时已知的公开最好值；Comellas访问8月23日，Wiki8月24日。并未声称2026-11-01仍是最大。 |
| [Rajiv September，2026-09-30](https://doi.org/10.5281/zenodo.23052995) | Table1：19/D3和20/D3均2783；caption：**“the largest published order”** | caption这句话修饰的是previous bound列，日期为September2026。新2783是改进下界；它是同一最大度19图用于cap20，不是另一张20正则图；两表访问日期均9月29日。 |
| [PolarStar，SPAA2024](https://spcl.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf) | abstract：**“largest known diameter-3 network topologies for almost all radixes”**；§1.2及contributions | 确实有较广泛的largest-known声明，限定almost all radixes及其当时比较对象，不能缩写为“所有参数最大”。另一项near-optimal说法只针对当前已知factor性质可造出的star products。不是所有一般图的最优性定理。 |
| [Delorme EJC1985](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf) | §7／p297一般复制；intro／Table2注明表值截至end1983 | 给通用构造和旧日期的best-known表；没有声称把任何未来源代入都得到全球最大，更不可能原文明确列2026年推得的2791。 |

每份primary在此英文短引均少于25词；完整位置、日期和缓存文件见机器记录。后续引用不按搜索引擎被引计数推断。

## 已核验的“后续文献→所引论文”

| 后续文献 | 实际bibliography条目 | 数值更新与本四格的关系 |
|---|---|---|
| Rajiv August | **[11]** → [July DOI21180071](https://doi.org/10.5281/zenodo.21180071)；Remark2也点名此前四图 | 20/D3：2202→2750来自Remark2；August Table1本身的previous仍写1958，二者分开记录。未达本地3840。 |
| Rajiv September | **[19]** → July；**[20]** → [August DOI22073603](https://doi.org/10.5281/zenodo.22073603) | Table1明确把cap20此前2750改为2783；未达3840。 |
| Rajiv September | **[13]** → [Isham等2026](https://arxiv.org/abs/2608.27253v1)（原条目未写版本；按September日期为当时v1） | 19/D3此前2470→2783；该图同时适用于cap20。 |
| [Isham等v2，2026-10-22](https://arxiv.org/html/2608.27253v2#bib.bib32) | **[31]** → PolarStar SPAA2024，345–357页；§7.8.1实际使用该引用 | 18/D3此前1830→2340；其Table3还列19／2470、20／2600。后者低于Rajiv2783，也未达到本地四值；“发表日期较晚”不等于每格数值更强。 |
| [同一Isham v2](https://arxiv.org/html/2608.27253v2#bib.bib37) | **[19]** → Delorme EJC1985；§7.7明确讨论复制 | 这是对本任务一般复制来源的真实引用；该特殊极性乘积族20／2600不是2791，也不是所有一般图的全局表。另[20]是Delorme的JGT1985另一篇论文，不能混为同一来源。 |
| Rajiv September | **[5]** → Delorme EJC1985 | bibliography关系真实；不因此把我们后算的2791说成该论文的原始数值。 |

还有一个不同证据类别：[V3R1T4S作者包README](https://raw.githubusercontent.com/elder-plinius/V3R1T4S/main/known-knowns/biggest-graphs/README.md)在References及credits中实际指向Rajiv DOI23052995，并用该源改进其它D4／D6参数。它是后续作者资料，不当作已审稿论文；其七项范围没有20–23／D3更新。

Isham v2的完整已读bibliography未出现Rajiv三DOI／作者，故这里不编造“Isham引用了Rajiv”的关系。没有找到的其它later cite只记为本次未定位，不称无人引用。

## 回到HTML中四个数应怎样写

| cap／D≤3 | 当前所用公开来源保证 | 应标明 |
|---|---:|---|
| 20 | 2791 | 原文显式图为Rajiv2783，且实际度≤19；结合Delorme§7得2783+ceil(2783/(19²+1))。**2791是推论，不是原文record行。** |
| 21 | 2928 | PolarStar q13、IQ7的合法公式代入；未定位原文逐格“2928是全球最大”的声明。 |
| 22 | 3294 | PolarStar q13、IQ8的合法公式代入；同上。 |
| 23 | 3549 | PolarStar q16、Paley13的合法公式代入；同上。 |

与本地3840／3984／4192／4336比较仍应写“超过本次已查公开来源保证；未找到达到本地数值的后续公开结果”，而不是“引用多所以不可能被更新”或“没人引用所以无人研究”。用户3250线索仍未绑定source／参数，保持待核、不否认；实时高degree表及未索引资料缺口继承[上一轮记录](D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.md)。

本次唯一一批forward查询：

- `"PolarStar" "2026" "Kronecker"`
- `"23052995" "Rajiv" references`
- `"New lower bounds for the degree-diameter problem from generalized quadrangles and hexagons" -site:zenodo.org`
- `"Grands graphes de degré et diamètre donnés" "2026" replication`

所有正向引用关系均回到primary正文／bibliography核验；没有仅凭标题或二手被引次数给结论。0图下载、0BFS／Lean／solver／真人消息／新付费；没有改HTML、rootstate、Wiki或冻结包。

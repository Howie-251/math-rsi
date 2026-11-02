# 度 8–12、直径 3 的纯 Cayley 来源边界

本轮有界读取日期：2026-10-26 会话。**没有读到能据以关闭当前 820 或 812 点纯 Cayley 入口的高阶最优性定理。** 这不是断言相关定理不存在，而是以下两条来源链没有取得这类结论。未生成图、运行 BFS、搜索生成集或修改共享状态。

## 1. Comellas 原文：度 8–12 的条目实际都是 D2

实际读取 [F. Comellas, Non-Isomorphic Optimal Cayley Graphs, arXiv:2606.10954v2](https://arxiv.org/html/2606.10954v2) 的目录、引言、§6–§10 标题与表格范围，以及参考文献 [5]、[6]。这五节覆盖 `(8,2),(9,2),(10,2),(11,2),(12,2)`，没有相应的 D3 条目，故不能把其中的 optimal 标记移到本轮 D3 参数。

引言描述了既有最优阶上的非同构实例搜集，方法包含随机搜索；实例集合非穷尽不等于已证明最大阶的反例，也不能当成对更大阶的完整分类。参考文献 [6] 当时把 Conder 的相关论文列为准备中；本次没有从该引用取得原证明。

此前已读的 253 构造仍是本轮可明确引用的高阶纯 Cayley 下界：`F23⋊9 C11` 上八生成元，来自 Comellas–Mitjana；完整参数和实际读取范围已保存在 [D3_BASELINE_STRUCTURE_NOTES.md](D3_BASELINE_STRUCTURE_NOTES.md)。本次不重新下载该图或复查其直径。[UPC 原说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html#83) 提供的是具体构造，未在此读到“所有 8 度 D3 Cayley 图至多 253 点”的证明。

## 2. Conder 原作者链：发现投稿状态，未取得高阶范围

沿 [作者主页](https://www.math.auckland.ac.nz/~conder/) 实际读取其 [出版物列表](https://www.math.auckland.ac.nz/~conder/publist) 的有关条目与末尾状态。第 201 项现列题名 *Largest order Cayley graphs with prescribed degree and diameter*，标为投稿中。它与 Comellas 的引用题名高度相符，但目录没有给出论文正文、定理范围、度 8–12 的 D3 数值、完整分类对象或证明文件。

该网页自标最后更新 **27 October 2026**；这里按实时返回内容原样记录，不将它改写成已在会话日期前发表，也不推断接受/发表状态。标题和投稿状态只能证实作者列有这项工作，不能承担本轮停止参数搜索的上界依据。

另读 [作者预印本目录](https://www.math.auckland.ac.nz/~conder/preprints/index.html) 的说明及目录：其页首明确说明自 2010 年后未更新，因此该目录中缺少这篇稿件不能证明当前没有公开版本。

Comellas 引用的 [CombinatoricsWiki 最优 Cayley 描述页](https://combinatoricswiki.org/wiki/Description_of_optimal_Cayley_graphs_found_by_Marston_Conder) 本次一次读取超时；[Degree/Diameter 页面](https://combinatoricswiki.org/wiki/The_Degree/Diameter_Problem) 一次读取返回 502。没有重试、换代理或追逐工具故障，未把失败页面当成已读原文。

## 3. 对当前选择实际可用的信息

下表的一般图基线是任务已给且此前确认的值；本次没有重新检索整表。

| 度 | 当前一般图 D3 基线 | 本次可据原材料采用的纯 Cayley 信息 |
|---:|---:|---|
| 8 | 253 | 已有 253 点纯 Cayley 构造；未取得其纯 Cayley 最优性上界 |
| 9 | 585 | 本次未恢复可信的纯 Cayley 最佳值表或最优性证明 |
| 10 | 650 | 同上；不能把一般图记录自动标成纯 Cayley 记录 |
| 11 | 715 | 同上；低度最优表不能外推到本格 |
| 12 | 810 | 未取得纯 Cayley 全局上界；810 的构造可表性边界见此前结构笔记 |

因此，当前 `F41⋊36 C20` 的 820 点、`F29⋊ C28` 的 812 点度 12 入口，**没有因本次读到的外部定理而被排除**。其成立与否仍需本地具体容量、真实生成集和完整距离检查决定。这句话不是存在性判断，也不保证该一般图基线在未来保持不变。

解释结果时应维持以下范围：一个明确 D3 Cayley 图只给下界；有界随机/邻域搜索未命中只说明该实际轨迹失败；完整枚举某个固定群的所有保全生成规则也只关闭该群/该声明族。要据纯 Cayley 最优性关闭整个参数入口，必须有覆盖相关群与生成集范围的上界定理或完整分类，而不是仅有“optimal”标题、某阶非同构实例表或未命中的搜索统计。本次未取得后者所需证据。

## 4. 查询额度与未读材料

只沿两条链：Comellas 原文/其既有 UPC 数据，以及其引用指向的 Conder 作者数据/CombinatoricsWiki。共五条定向查询，已到本任务上限：

1. `site:combinatoricswiki.org Cayley "Diameter 3" "Degree 8"`
2. `"Marston Conder" "Largest Cayley graphs with prescribed degree and diameter"`
3. `site:math.auckland.ac.nz/~conder/ Cayley diameter degree 12`
4. `site:combinatoricswiki.org "Cayley" "253"`
5. `site:combinatoricswiki.org "Cayley" "diameter" "12"`

没有查询命中提供可读的高阶 D3 最优性正文。检索出现的 Comellas 镜像只用于定位，结论引用原 arXiv 页面；不依赖非原始转载。没有展开到其他综述、Loz 博士论文、Sampels 原论文、图数据库普查或 Conder 稿件的猜测地址。

实际结论止于资料边界：本次未补出度 9–12 的纯 Cayley 最佳已知阶，更没有把未取得的上界作为停止理由。后续若取得 Conder 第 201 项正文，需再按其真实参数范围判断；本任务不追加检索。

# 5832点公开D4源：13—16度 frozen-full-N 扩张全部停止

2026-11-01。**四个参数范围均STOP，不返回生产候选。** 已保存公开保证全部超过该源的普通度预算上包络，无需寻找controller code或仿射平面。本次是计算选择门，不是新图、源复现或新容量定理。

## 实际源与继承证据

`research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json`的实际字段是：field_order=3、fiber_dimension=4、base_order=8、cyclic_modulus=9、controller_order=72、graph_order=5832、graph_degree=12。其顶点为72×F3⁴，**不是**F4上的18432点/16度图。

同目录`proof_ja.md`标明2026-09-24，定理3给simple12regular、5832点、D=4；`README.md`给34992边。已执行的`small_certificate.json`报告100个满秩四词、12个pencil、同层18平面覆盖及72²控制点对；两个旧独立实现BFS receipts均报告5832根/34012224个有序点对、34992边、degree12、D4。这些仅作为已有证据继承，未运行任何checker、field/rank、BFS或生成器。

公开源包：[Mizuno degree12/diameter4 certificate](https://github.com/rmizuno42/ddp/tree/main/results/degree12-diameter4/certificate)。本地`results_degree12-diameter4_certificate.json`保存README、construction和proof的实际作者URL。本门不声称5832仍是12度当前最佳；缓存主表已有更大的12度条目，这也不影响以下阻断。

## 同一源、同一扩张规则的包络与公开阻断

固定保留全部旧边。每个新点只连接一个旧中心在**原始源**中的完整N12，允许重复中心/任意次序，但不加new-new边。若新增M点，旧点总余度只有5832(Delta−12)，而新增边恰12M。因此

    12 M <= 5832 (Delta−12),  n_final <= 486 Delta.

这只是已继承的度预算，未宣称包络可达到。

| cap Delta | 该规则最终点数上包络 | 缓存实际公开D4保证 | 保证减包络 | 决策 |
|---:|---:|---:|---:|---|
|13|6318|6804|486|STOP|
|14|6804|9720|2916|STOP|
|15|7290|15552|8262|STOP|
|16|7776|16384|8608|STOP|

四个公开数值来自已缓存的[Comellas实际主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)，本地`research/ddp/more_graphs_20261027/PUBLIC_BASELINES_2055.json`记录checked_UTC=`2026-10-27 20:54:11 UTC`，原始`public_table_2055.html`保留四个D4 cells及“Last changed: October27,2026”。每个条目的实际degree为对应cap、D4，未把D3/D5、较高度数图或假设性upper envelope当成公开保证。直接条目是[13/4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#134)、[14/4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#144)、[15/4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#154)、[16/4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#164)。本次未联网更新它们；停止决定只需要已有公开构造存在，更晚更大的条目不会撤销这个阻断。

此外，停止决定并不依赖只读主表数值：

* 实际[13度6804作者包](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg13/dia4)的README/完整recipe/source metadata已缓存于`research/ddp/more_graphs_20261027/d13_D4_current6804/`。`SOURCE_RECEIPTS.json`保存2026-10-27T18:28:34—37Z的作者文件与主表读取时间；`SOURCE_FACTS.json`给degree13/D4/6804。此前`RESULT.json`实际输入绑定simple6804/44226、全部13度，D4继承作者公开recipe而非本次复验。它在cap13超过6318，在cap14也以degree13≤14达到6804包络，因此即使只用此一个已发表对象，13和14都无法严格改善。
* 已有[15度15552公开对象](https://zenodo.org/records/23691325)实际边文件与下载receipt/source profile保存在`research/ddp/more_graphs_20261027/d15_D4_current15552/`。`SOURCE_FACTS.json`实际点数15552、degree14有648点/degree15有14904点、D4继承公开结果。故degree≤15，同时适用于cap15和16，已经远超7290/7776。该公开数值也出现在上述2026-10-27主表快照中；本地缓存没有据此确定Zenodo原始首发日期，本门不编造该日期。

所以四个STOP均有参数正确的公开保证支持，无UNKNOWN格，也无需穷尽全球文献或读取更多大图。这里不把这些竞争源返回为新的研究source或模板。

## 旧范围检查与决策边界

现有Wiki `ddp-wave5-mizuno-d4-source`的原scope是72controller的宽D4充分路线证书及从属controller容量筛；它没有把这四个raised-cap full-N范围登记成普遍无解。`ddp-more-graphs-20261027-source-slack-monotone`的D4满度筛是**原cap不升**时保留旧边不能附加新点，不把它误用于这里的Delta13—16。另一个`ddp-d13-d4-current6804-source-20261027`上的matching/hub/split严格小域和完整模型UNKNOWN属于6804宿主改边，既不是本5832宿主，也不是这里的复制预算范围；其UNKNOWN保持不变。

本门的准确结论是：**在这个固定5832源、保全部旧边、每个新增点完整原N12、无new-new边的范围内，cap13、14、15、16都不能超过已保存公开保证。** 这不是一般N(Delta,4)上界，不排删改旧边、不同新增邻接/辅助点、new-new边或其他构造。当前不开展这些替代范围，也不改q、controller或另选source。root应停止本次四cap候选，不排队packing、生成、BFS、rank、solver或Lean。

本次仅本目录PRED/NOTE/RESULT/TERMINAL落盘；0图/参数/Lean/method增量，未改Wiki、root-owned文件、专家稿或冻结包。已有源证明和普通度预算均不计为本轮新成果。

# 2026-11-01 supplement：6144→6160 的 spread 补点既有性核查

这是对[原23/24度公开比较](DEGREE23_24_EXTENSION.md)的有限补充，保留此前6144比较的历史范围。本次仅查来源；未读边表、验图、BFS或求解。任务下达时6160仍是拟议候选，其合法性由另一代理检验。

**本次未定位明确公开的6160实例、≥6160保证，或恰好使用这项固定度数spread补点的公式；这不证明新颖性，也不把6144称作全球最优。**

核查结果：

- [arXiv2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)给opposite-GQ基图的N=(s+1)(t+1)(1+st)²、Δ=(s+1)(t+1)，并列出GQ(q−1,q+1)存在。该节未见另加st+1点的增强式。已存全文中的6160、6,160、spread均无命中。
- [同文§7.7](https://arxiv.org/html/2608.27253v2#S7.SS7)复述的Delorme复制为N+k|S|、Δ+k。现有[Delorme《Grands Graphes》EJC1985 §7/8](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)亦读到一般复制和绝对点例子。这些已读陈述不能直接等同于本次保持Δ24、使用incident flags余度的16个新hub规则。
- **检索缺口**：[Delorme《Large bipartite graphs》JGT9(1985),325–334](https://doi.org/10.1002/jgt.3190090304)是opposite-product原始来源。本次出版社PDF与DownloadPDF入口都回到摘要，未取得其全文；不能声称原文没有这种增强。两批精准web检索亦未命中6160或对应规则，随后停止。

贡献口径应保留：GQ/Payne几何、spread及opposite-product基图属于经典来源；父级本次提出的spread-indexed helper补点属于正在检验的具体推导，**首创归属与最新全球纪录仍未认证**。若合法性验收通过，可先称“本地合法6160点实例，超过已定位的6144公开公式构造”，不称世界首次。

机器摘要及精确检索词见[补充JSON](DEGREE23_24_EXTENSION_SPREAD_SUPPLEMENT_20261101.json)。本次无新增数学构图成果，也未更改专家包。

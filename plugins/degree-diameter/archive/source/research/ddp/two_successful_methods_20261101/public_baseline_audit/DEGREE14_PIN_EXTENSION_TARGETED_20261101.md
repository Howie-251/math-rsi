# (14,3) pin扩张入口：1088不是当前公开基线

核查日2026-11-01 UTC。仅一批三条窄搜索、官方主表与详情页、已存primary，以及一个指定GitHub目录API检查；未下载源图、运行生成器、BFS、solver、Lean或校验函数，未修改Wiki／root状态／冻结专家包。

**当前官方主表已列(14,3)=1201，更新归于Rajiv 2026-10-30。因此1088→1089不构成新下界；要超过本次定位到的最新主表值，至少需要1202。** 本报告没有验证1201图或认证全世界不存在更高公开图。

## 一手证据与页面不同步

[Comellas官方Degree–Diameter主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)的Δ14、D3单元为1201；页面updates作者列表中，Rishabh Rajiv的Oct.30,2026更新明确包含(14,3)。主表同时提示数值先更新、详细页面可能滞后。

[官方D3详情页的14度段](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html#143)仍列1141，作者Comellas、2026-10-23；其下依次保存Mizopl1118（10月19日）、Yugeswardeenoo1116（10月7日）、de Messieres1094（10月3日）及Rajiv1088（9月30日）。这解释了为什么仅重读September论文会落后。详情中1141的“新增六点”文字与1118到1141的数值差不一致，本报告不复算或采用其改边数字；阻断1089所需的已发表阶数信息已经充分。

重要的是1094一项已经保留全部1088源边、另增六点，并加入旧旧边和新新边；因此一般“用余度保边增点”的方向本身已有该源上的公开先例。它不直接证明或否定当前一Wline8点＋其他pins的具体覆盖规则。

## Mizuno／Mizopl区分

本次只读查询rmizuno42/ddp的指定路径results/degree14-diameter3返回404，不能据此推断其全部仓库没有相关结果。官方详情里的1118来自另一位作者mizopl，链接到[其原始公开PR457](https://github.com/elder-plinius/V3R1T4S/pull/457)，不应把这位作者误归给rmizuno42。无需为判断1089已被超过而另下载1118边表或核验旧图。

## 已有源与当前决策边界

Rajiv September2026论文Table1的1088仍是有效源下界；旧本地q8原witness／K64也仍可用于机制分析。当前研究若只构造1089，最多增加一个已知基线以下的机制例，应与新纪录分账。要继续以本格改善为目标，需解释如何跨过1201，而不是把1088当成全球前值。

本任务没有重跑q8旧13度K5／循环／删边范围，没有读取新的adj／边表，没有启动新source或构造模板。搜索范围：degree14／diameter3／1201、1089，以及rmizuno42的指定目录；未做全球穷尽。故global_record_confirmed=false，当前决策应为BASELINE_BLOCKS_1089。

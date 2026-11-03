# (19,3)：3840候选的有界公开比较与2783源入口

核查日期：2026-11-01 UTC。只做两批窄搜索、已存primary阅读和小整数公式代入；未构图、运行BFS/solver/Lean、安装软件或更改冻结专家包。

**本次找到的最强公开来源下界为2783。若3840点图真能降到最大度19并保D3，将比该值多1057点；本报告没有取得这样的图，也没有认证全球最高。**

## 数值和准确度数

[Rishabh Rajiv，2026-09-30 Zenodo论文与数据](https://doi.org/10.5281/zenodo.23052995)的Table1明确同时列(19,3)2783（此前2470）与(20,3)2783。新读的作者README也明确：20度一格由同一19度图保证，并非两张不同图。这不是将最小度19误作最大度19。

论文§2 Definition1／Theorem1给源图的一般规则：
- 从W(q)删除指定点、与其共线的点及过它的线，留下点集P（q³点）和线集L（q²(q+1)线）。
- transvection z_λ在点坐标(a,1,b,c)上把a改为a+λ。
- 每个点按X加transvection邻边；每个线类经β_i复制同一个q²点class graph K。K含X'给出的pencil边，另加gadget。
- incidence边、point-transvection边、class-K边三类同时保留；点度q+1+|X|，线度q+deg_K。
- q=11，X={±2,±4,±5}，X'={±1,±3}，gadget为4正则。故1331个点的度恰18，1452个线点度不超过19，原文给整图最大度19、D3。作者实际check_fibre源码另断言全部line为19度；本任务未执行该断言、未读取adj或独立确认line度数直方图，不能冒称已实测全19。

点集的1331个单余度是可供保边pin-cover研究的具体接口；要保D3仍须覆盖所有点和线，并非仅按容量相加。K的实际有限gadget不可由q和X两集合自行猜定。

## 可读取的准确源文件

[Zenodo API记录](https://zenodo.org/api/records/23052995)本次实读publication_date=2026-09-30，仅列三个文件：README、论文PDF、data-and-verification.zip（59224157 bytes）。[作者README](https://zenodo.org/api/records/23052995/files/README.md/content)仅3462 bytes，本次已读取。

[数据及生成/验证源码ZIP](https://zenodo.org/api/records/23052995/files/data-and-verification.zip/content)的central directory通过HTTP Range只读取末尾65557 bytes，没有下载图或59MB全包，准确确认：
- `witnesses/fq_d19_k3_n2783.json`，2598 bytes：具体q／field／X／X'／K的构造数据。
- `verify_witness.py`，31323 bytes：含按witness重建fibre图的实际程序入口；作者将其作为standalone verifier。
- `graph_d19_k3_n2783.adj`，237750 bytes：具体源图，0起编号的每行邻居表。

作者README描述的默认verifier会重建并全源BFS；本任务未执行它。后续只读小witness／生成函数即可继承字面构造，不必重跑所有13图或其最大图。

## 其他primary公式对照

[PolarStar，SPAA2024](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)的Brown底图q有q²+q+1点、最大度q+1，supernode度d'使总最大度不超过q+1+d'。在cap19的小整数合法代入中，IQ最大2128（q11,d'7）；Paley最大1729（q11,d'6，总cap18）；BDF最大1862（q11,d'7）。IQ要求d'≡0或3 mod4，Paley要求2d'+1是≡1 mod4的primepower，未对非法supernode套公式。

[Isham等，arXiv2608.27253v2 §7.8 Table3](https://arxiv.org/html/2608.27253v2#S7.SS8)的19度2470，是18度2340源的130绝对点复制，低于September2783。其一般族不等于完整全球表。新定位的[该族显式实现论文](https://ideosphere.ai/papers/polar-degdiam)也只给这组2470／2600数值，不能取代更晚2783。这里仅读其原作者页面，不采用其Lean/最大性声明为本地已验证结果。

本轮两批精确degree19／diameter3／2783／2026查询没有定位≥3840的公开图。结果召回有限、维护主表止于16度；未完成全球穷尽检索。因此`global_record_confirmed=false`。本报告不支持把纯删边失败推广为一般19度构造无望，实际3840删边的路线结论由另一研究任务另记。


## 同一源的后续小文件取读（05:52 UTC）

按root对具体保边覆盖问题的跟进，只通过原ZIP的5个精确HTTP206请求读取76900 bytes，取得两份作者原文件：
- [完整小witness](degree19_source_primary/fq_d19_k3_n2783.json)：2598 bytes，含实际有限gadget。
- [实际生成/验证源码](degree19_source_primary/verify_witness.py)：31323 bytes，仅读取，未执行。
- [Range取读回执](degree19_source_primary/RANGE_RETRIEVAL.json)及[准确β与入口说明](degree19_source_primary/RETRIEVAL.md)。

q11的实际来源是fibre_build:88..158：对PG点归一化、lex排序，按line-sets排序；每个class的pencils由交点排序，β_i(a,l)=z_l(base_a)，base_a取该pencil的最小line-set。check_fibre:175调用此函数绑定原adj。另一个fibre_coordinate_edges:208..242给快速仿射坐标公式，但原程序仅在matching构造验证中调用；如将它移用于q11，必须另核β约定，不能直接声称标签等于原adj。未下载原adj或大ZIP，未生成源图、运行BFS或作者验证器。

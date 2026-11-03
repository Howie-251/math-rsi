# Dhar pencil 来源侦察：找到当前作者原图，未取得生成规则

2026-10-27。本轮找到此前未读的作者原始 deposit [Zenodo23653049](https://zenodo.org/records/23653049)，题为 *Large graphs of given maximum degree and diameter (Degree-Diameter Problem): 34 constructions*，creator 为 Dharunish Yugeswardeenoo，当前 metadata 发布日期2026-10-26。其文件表提供37628与42342两个当前原图；本轮没有得到可直接实施的 pencil 几何生成公式或证明，已按有限来源侦察范围停止。

## 实际来源和阅读范围

- 重新读取 [Comellas 直径五页面](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html) 的 H(9) 条目和实际 href，保存为 `desc_g5_current.html`。当前两图各只给 rawadj；旧 Rajiv partial-fold 条目的链接文字仍是22907863，而实际 href 为已读过的23056128。本轮未重复旧论文或旧构造试验。
- 用官方 [Zenodo API record23653049](https://zenodo.org/api/records/23653049) 取得 creator、完整文件表及 H9 描述。`zenodo_23653049.json` 保留该 metadata 的标题、作者、文件表和三段 H9 相关构造文字，省略其他构造描述。文件表只有图邻接数据、metacyclic 参数、README、CURRENT_GRAPHS 与两个通用 C verifier，没有 H9 split/color/copy/pencil witness、pencil 生成器或独立几何论文。
- 完整阅读作者 `README.md`（8238字节）和本次下载的 `CURRENT_GRAPHS.txt`。README 将三个 H9 图的底层来源指回23056128，未给 pencil 定义、邻接公式或新增点之间的距离证明。metadata 的相关三段文字与主表概述相同，没有补充这些细节。
- 定向查询作者名及 pencil/closed-split 关键词，没有找到另一份相关原始技术文档。公开 API 对 creator 名 Dharunish 的这次检索返回上述 deposit。候选 GitHub 用户 `dharunish` 的18个公开仓库名未显出 degree-diameter 项目；其主页仅为225字节的占位页。该 profile 未写姓名，故不把这个同名候选账户当成已经完全核实的作者身份，更不据此断言作者所有公开代码都已查尽。没有联系作者或外发消息。

作者原始文件：

- [37628邻接表](https://zenodo.org/api/records/23653049/files/deg11_diam5_n37628.txt/content)，本地 `deg11_diam5_n37628.txt`。
- [42342邻接表](https://zenodo.org/api/records/23653049/files/deg12_diam5_n42342.txt/content)，本地 `deg12_diam5_n42342.txt`。
- 对应主表文件为本地 `graph_37628.adjlist.txt`、`graph_42342.adjlist.txt`，URL保存在 `raw_sources.json`。

去掉注释并规范空白后，作者与主表两个版本的邻接数据均逐行完全相同。这里直接比较邻接行，未计算哈希。没有运行随附 BFS verifier，也没有安装依赖。

## 当前42342图的便宜度数核验

只读邻接并检查对称性，得到 n=42342、m=245217：

|度数|顶点数|空余度 slots|
|---|---:|---:|
|12|27946|0|
|11|11190|11190|
|10|3149|6298|
|9|48|144|
|8|7|28|
|7|2|10|
|合计|42342|17670|

14396个点至少有一个空余度 slot。最后165点中有88个此类点，共173 slots；此前42177点有14308个此类点，共17497 slots。最后165点之间有一条边，因此不能默认作者这些新增点相互独立。

这些是 degree 计数，不是覆盖证书。没有对14396个候选运行半径四球覆盖搜索，也没有做全根 BFS。该数据已交 root 决定是否另开一次有界“加一顶点”初试。机器可读结果为 `degree_capacity_42342.json`。

## 37628图的有限类型侦察

作者说明为部分折叠核心、29个 H3 额外 copies、122个 pencil，再加6点。算术给出 split fibers 数4074；若按自然追加顺序编号，则部分折叠段为0..37470、H3-copy 段37471..37499、pencil 段37500..37621、最后6点为37622..37627。后述标签分块是有数据支持的推定，尚不是作者提供的几何 witness。

- 最后6点度数之和恰为50，彼此无边，符合作者记载的最终6点/50边。
- 删除后续122+6点后，29点段的每个点都与一个前缀点有完全相同的邻集，支持其 copy 解释；亲本候选逐项保存在 `degree11_append_order_check.json`。
- 候选122点段内部有7条边，另有4条边连最终6点。最终度分布为117点度十一、5点度十。该段向部分折叠前缀接1314边，向29-copy 段接5边。
- 对每个候选 pencil，保留其0..37499范围内的旧邻集，检查是否包含于某个旧点的完整邻集。仅4/122有这样一个旧点，另外118个没有。故这些邻集不能直接套用“复制一个旧点全部邻居”的普通 twin 规则，甚至多数不是其旧邻集的子集。具体邻集、重叠计数及候选亲本在 `pencil122_neighborhood_test.json`。

上述工作只做邻接交集和度计数，总计约一秒CPU；没有从原图重新求直径，也没有把规律猜测提升为几何定理。

## 尚缺的可实施规则

当前材料仍没有给出：

1. pencil 的几何对象、中心/参数和由它确定新点邻居的公式。
2. pencil 与原部分折叠点、其他 pencil 之间距离至多五的论证，以及7条内部边这类额外 anchor 的选择规则。
3. 当前42342图的 S、颜色、H3-copy 数与 pencil 的逐点分解或生成器；完整显式图本身已经取得。
4. Dhar 所称 closed split set 的明确定义。旧 Rajiv 公式当然给出 merged 度预算对应的必要闭包条件，但这里不能把那一条件自动冒充后续作者未写出的完整定义。

因此本轮没有生成新的 pencil 构造，也没有启动当前图扩张搜索。状态为 `CURRENT_AUTHOR_GRAPHS_FOUND_PENCIL_RULE_NOT_RECOVERED`，详见 `SCOUT.json`。后续可从已取得的显式42342图执行另行授权的有限实验；若要复用 pencil 作为新几何机制，以上邻接与距离缺项仍需解决。

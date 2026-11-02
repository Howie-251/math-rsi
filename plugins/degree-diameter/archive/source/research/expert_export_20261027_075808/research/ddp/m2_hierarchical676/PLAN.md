# 单个确定性 650 → 676 层次扩张

本次只生成和完整检查一个候选，单核成本上限 30 CPU 秒；不启动随机种子、修复、参数或候选队列。原 650 图、压缩对象和其他代理的 `DISTANCE_RULES.md` 均只读。

输入是 `m1_degree5_transfer/rithwik650_source.edges` 及 `source650_hierarchy/compressed_graph.json`。旧图由 25 个 group heads、125 个 block heads、500 个 leaves 组成。每个 group 有五个 blocks，每个 block 有四个 leaves。叶子诱导图为 4 正则。

新增顶点标签为：group head 650；block heads 651–655；leaves 656–675，按连续四个分给一个 block。新增树边 25 条。

在旧叶图选择 40 条两两不共端点的边。每一步仅考虑尚未使用两个端点、且删除后对应旧 group pair 至少保留一条叶边的边。确定性字典序优先级为：覆盖更多尚未覆盖的旧 groups；使 group 端点负载均衡；较小的已知单删边损伤；较小的旧 block 负载；原边序。达到 40 条后，必须核实 80 个端点互异且覆盖全部 25 个旧 groups。若贪心没有落实这些条件，保存失败状态并返回，不编造候选或自动追加搜索。

把这 40 条边两两配成 20 份，各含四个旧叶端点。依次轮转五个新 blocks，为当前 block 选择尚未使用的边对，优先增加该 block 的直接旧 group 覆盖，再增加旧叶一步邻居所触及的 groups，最后用原边序打破并列。每个 block 得到四份。这里的一步邻居只用于确定性布置，不作为直径证明。每份四端点连接到一个新 leaf。

删除所选 40 条旧边，加入 80 条新旧叶连接和 25 条新树边。旧叶失一条边并加一条，所有新 leaves 的度数为 4+1，新 block heads 为 4+1，新 group head 为 5，因此预期 676 个顶点全部 5 正则，边数 1625−40+80+25=1690。

保存完整边表、所选边及全部标签/分配参数。通过独立通用 `computations/ddp/verify_graph candidate.edges 5 5` 检查全图；另从完整边表重新建立邻接并全源 BFS，统计实际直径及所有距离超过五的无序对，按 head/block/leaf 和 old/new 类型分解。完整覆盖 25 个旧 groups 只保证新旧 group heads 的显式五步路线，不能据此断言其他点对均合格。

复用现有实验结构检查器，保留真实终态和 CPU 成本。一个失败候选仅诊断这次确定性实例，不排除整个层次机制。

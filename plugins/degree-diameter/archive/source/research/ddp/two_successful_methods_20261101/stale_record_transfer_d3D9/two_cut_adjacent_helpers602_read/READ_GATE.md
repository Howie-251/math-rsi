# Actual Exoo600：双cut＋相邻双helper的历史读取门

限定历史读取未定位该固定Exoo600源、两条顶点不交cut、四端点任意2+2接相邻helpers的既有严格NO或UNKNOWN终态。此处“未定位”不是断言从未被研究，也不是一次已运行而超时的UNKNOWN。旧目录 `two_helper_repair602` 名称相似，但实际规则是三cut＋一条old–old repair；其 `four_cut_spread_pins` 子目录是四cut＋两条repair。两者各10000样本，双方helper全覆盖均0，整族仍UNKNOWN，不是本次双cut范围。

唯一源输入与格式：

- `research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.author.adj`：从primary保存的原始600行邻接，每行隐含标签0..599，行内三邻居也是0-based，不含每行自身label前缀。
- 同目录 `source600.edges`：已规范化的等价字面，首行 `600 900`，然后900条排序0-based无向边。
- `SOURCE_PROFILE.json`：已验simple/reciprocal/cubic/connected；degree3有600点，D9继承primary。该图非二分，旧parity冲突(215,465)；不能继承odd-bipartite自动细分覆盖。source VT/ET都未绑定，不能借Conder另两个C600或任意anchor缩域。
- `SOURCE_REPORT.md` 与 `CONDITIONAL_SUBDIVISION_LEMMA.md` 只因二分前提为假而停止旧论证，明确没有测试graft，不构成全部单/双cut NO。

规则参数账：删除两条顶点不交旧边，将四端点分为无序两组A/B、每组两个点；新增x=600、y=601，分别接A/B并加xy。旧端点失一补一，所有点degree3；条件n602、m=900−2+4+1=903。未生成图。

**完整域不能直接按每edgepair乘2。** 对e={a,b}, f={c,d}，unordered2+2有三种：ab|cd、ac|bd、ad|bc；交换helper不另计。只有另加“每helper各取两条cut的一端”的约束才剩两种，排除了wholecut-pairing。按已有simple cubic degree谱，unordered disjoint edgepairs的静态组合数为C(900,2)−600·C(3,2)=402750；因此任意2+2完整域为1208250配置；cross-only子域为805500。更粗上界分别为C(900,2)×3或×2。这里仅算规则的组合式，没有sourceparse、edgepair循环或配置枚举。后续owner仍须按字面实际绑定domain，不用本门代替枚举结果。

实际helper路线必须按修改后的旧host K=G−e−f及其pin组判断。精确式为

    d_J(x,t)=min(1+d_K(A,t), 2+d_K(B,t)),
    d_J(y,t)=min(1+d_K(B,t), 2+d_K(A,t)).

双方新根R9完整等价于 `R7_K(A) ∪ R7_K(B) ∪ (R8_K(A) ∩ R8_K(B))` 覆盖全部600旧点。不能要求每个own R8单独覆盖；也不能由旧source D9直接推出新根通过。source距离与删除后K距离不同，若要用source球替代，须另有本规则的exact route lemma，而非偷换缓存语义。双方helper通过后，还须实际验证600个旧标签在最终602图里的D9，不能把newroot覆盖当完整图。

**距离/球缓存定位结果：** 限定源目录与现有d3D9实验目录中未定位通用source distance matrix或source R7/R8/R9球文件。旧SOURCE_PROFILE明确source_BFS=0；旧数值driver只对修改后的候选做ordinary BFS，没有保存可移作source球的全根缓存。现存可复用材料是：

- 上述source字面和profile；无需重新下载或source D9验收。
- `stale_record_transfer_d3D9/two_helper_repair602/{RESULT.json,RAW_RESULT.json,ATTEMPTS.csv}` 与 `four_cut_spread_pins/` 的对应文件：保存那些旧样本的first actual helper failure路径与配置，仅作诊断，不能当source全距离表或新双cut结果。
- `two_helper_repair602/PAPER_NOTE.md` 保存相邻helper精确K-route公式；旧 `run.cpp` 可供实现实际候选BFS，但其三cut/repair生成域必须更改，不能原封不动当双cut程序。

本门实读actual460行ledger相关记录、canonical三/四cut样本节点、源报告/profile/条件lemma、旧sample PRED/NOTE/PAPER及两个driver的输入/距离接口。未导入Wiki、未读源边正文。此次保守read/prep0.5 CPU秒；sourceparse=0、source/候选BFS=0、cut枚举=0、solver=0、图=0、Lean=0。停止本门，不自动跑任何双cut子域、seed、其它source或参数。

root后续纸面接口（未执行）：H=K2时新根到四个pins的起步权重只有1/2，任意两个cut端点权差≤1。原source路线若经过被删cut，可在最后一次cut的下游pin重启，增加的起步权重不超过省掉的那一步。因此拟用原G的exact式 `min(1+d_G(A,t),2+d_G(B,t))` 替代K式，另一helper对称。该项记录为下一待paper绑定的接口，不是本门新增数值、候选通过或source球已有的声明。若另获授权且纸面接口接受，可一次从600个原根产生depth8的R7/R8两层作为新覆盖问题输入；这是未来新数据，不是sourceD9重验，也没有在本门启动。

实际确认与继承分开：本门实际确认的是现存文件/文档中的格式和范围，degree3/simple/600/900全部继承已验SOURCE_PROFILE，未做新的字面degree验。402750与1208250是基于该继承simple cubic事实的静态组合式；actual枚举计数仍未产生。

# 缓存 unique3 witness 子集的三额外边容量门：事前预测

root最新修订优先本门，而非读门PRED中的完整middle-critical假设。本次从既存1012个edge/oneunique3path记录取**有效证据子集**，不重新枚举9108个unique3pairs，也不声称完整critical matrix。累计cap10CPU：继承source-read0.8、新准备0.2、独立read攻击0.25；唯一标准库进程hard8，不编译/solver/BFS/field。

实际RIGHT CM253 law/action9、label23x+y。用四个完整positive generators（不能只比phase）给每cachededge确定方向h→h*s；若保存路径反着经过该cut，先反转整条路径，再将四个点全部left乘h^-1归一化。绑定path三条旧edge和canonicalcut位置，不重证unique3。

对归一化路径(p0,p1,p2,p3)：cut位置1时hitset为{p0,p3}，位置0时为closedB1(p3)，位置2时为closedB1(p0)。这些是其它六pins必须命中的集合，不能把首/末段当成中段。相同normalizedpath合并保全部原记录provenance；不同oldpair即使有相同hitset仍保存，并在mask分子同样计入每个义务。

可推翻预测：每个firstcanonicalclass的全部cached义务，都不能由三条其它源edge的六pins覆盖，即 `3*max_other_edge_hits < required_obligations` 对四类同时成立。每类完整扫1012sourcepositiveedges，先剔触0/s的15条边，实际admissible应997；保zero和每一条实际edge mask，不枚四cut。这个upperbound甚至允许其它三edge互相共享端点，故负结论对合法disjointcuts也成立。

同时只在cached middle子图上求实际bipartite matching，并保存真实端点证书；7matching若存在可给六pins不足证据，若小于7不代表真实fullcritical图也小。容量预测不支持时不能将该规则记为NO；首中末计数/完整edge masks供root决定下一fullword或cutjoin，不自动扩算。

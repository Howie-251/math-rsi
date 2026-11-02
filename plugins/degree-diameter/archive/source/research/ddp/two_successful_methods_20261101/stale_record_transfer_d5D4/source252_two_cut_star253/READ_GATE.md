# (5,4) Rajiv252→253：两不交cut／单四星读取门

结论：当前official描述页仍列Rajiv252为(5,4)252点源。项目已有同源完整literal和组合recipe；本次有限same-source读取没有定位完全相同“删两条不交旧边、四端点接一个新点”的strictNO或UNKNOWN。不把未定位写成历史或全球不存在。当前只准备源和exact接口，未做任何cut/覆盖测试。

## source与真实格式

fresh official入口：[Comellas diameter4 #54](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#54)，该节标Rajiv252、2026-09-24、A7三orbit42/105/105。作者包为[Zenodo22928337](https://doi.org/10.5281/zenodo.22928337)。只从该节实际link29得到[精确raw edge URL](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/graph_d5_k4_n252.edges)，没有猜文件名或改源。

本门保存SOURCE252_RAW.edges，origin=fresh_primary；one HTTP尝试状态FETCHED_EXACT_PRIMARY_LINK，与旧缓存byte equality=True。数据是**无NM header的undirected edge pairs**，labels0..251，第一行0 148是边。不能套用wave7 regenerated252.edges的252 630 header格式。当前n252/m630、degree profile{5: 252}，全部252点degree5，原sourceD4继承，不BFS复验；依据：inherited already-verified cachedsource; freshprimary bytes equal cache。新文件之外没有改旧literal。

已有源完整组合坐标/生成规则在wave7 rajiv252_cell_structure/REPORT.md和coordinate_tables.json，literal reconstruction曾逐全部630边相等；其A7原始generator witness与此组合recipe不同，不需要为本扩张重新下载作者大包。

## 已排旧范围与本次差异

full-neighborhood clone253在保prototype全旧star时已严格NO：旧630边都critical，clone fold不能修复删边造成的oldold损坏。此处newz只有四个cut端点邻居，非旧5点fullN，fold前提不成立；不能照搬该NO。旧252→254 fourmatching/twohub批次、七胞元triangle模板边界也都是不同规则。它们保留、不重跑。

本门有限查了same-source机制scout/cell/clone的已有报告和相关canonical节点，以及旧extension254报告；没有全Wiki重导、全history读取或任何数值重做。

## 交给唯一数值owner的exact接口

源全5regular，没有可直接填的旧spare。取两条vertex-disjoint原边，P是四个端点；删两边后加z252并连P。仅条件度数账：n253/m630−2+4=632，原252点仍degree5，新z degree4，max5合法，未生成该图。

所有cut端点都在P，故d_(G−cuts)(P,t)=d_G(P,t)：最短P路线若用了cut，可从其下游P端点重新出发而更短。因此新root的D4覆盖**恰等价**source closedR3四pins并覆盖all252。oldold D4仍需actualcandidate检查，源边critical并不直接排这个新四星，因为新star可能提供repair路线。

本轮source/candidate BFS、R3、枚cut、graph生成、solver均0；只保存来源/格式/inputbinding，未测任何新构造预测。localprep cap1.5，保守先前读取/准备.8＋本writer实际CPU约0.013258，不涉及webservice CPU计量；不改STATE/Wiki/pages。STOP，root另给一次finite数值预算才开始；不换源/参数或重试已闭clone范围。

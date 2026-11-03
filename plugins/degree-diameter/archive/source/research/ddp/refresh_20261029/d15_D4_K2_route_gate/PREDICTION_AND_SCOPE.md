# (15,4) 固定15552源的相邻双 helper 路线门

唯一源为 `research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.header.edges`，
15552点、116316边。继承其D4，不重验源直径。原648个freeport均应度14、spare1。
复用 `single_vertex_R3_cover/R3_MASKS.bin` 的完整closedR3，不重算R3。

本次只读literal源一次，按旧R3文件的字面648标签顺序计算closedR2并转置R2/R3。
源header、freeport完整列表、每个spare与旧缓存标签绑定必须一致，否则停止。

新增相邻两点的两侧pin集合A、B各至多14，且因spare1必须不交。对全部旧目标，
精确新根D≤4条件为 `R3(A) ∪ R2(B)=V` 及反向式。令T0为全部648port的R2都
不覆盖的旧目标，则A、B须分别以R3覆盖T0。T0中R3-support0立即排除；support1
迫同一个spare1端口同时分给两侧，也立即排除。support2迫两端口分居两侧，
本批只记录这类必要关系，不进行整数求解。

事前预测仅为：比D14的互助R3，本次互助R2更稀，T0可能给出实际限制。
没有保证T0非空或存在singleton。若无上述反例，仅记必要门通过，不声明K2可行。

编译/native/driver合计≤10 CPU秒，单worker；0solver、0新图、0源D4全根BFS，
不进入102060源或其它15度参数，不续旧single-helper优化。

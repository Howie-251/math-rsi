# actual104c →105 two-cut star：同一旧完整 NO，继承停止

状态：**发现完全相同的 fixed-source/rule 已经穷尽，停止，不重新枚举。** 这不是把旧98源结果迁移到104，也不是将另一种 vertex split 的 NO 当作本规则。

## 准确 primary 与可直接复用的 literal

缓存官方 `research/ddp/m1_sources/desc_g4.html` 的 `#44`（72–82行）明确：Nishant Bhakar于 **2026-08-27** 给出三张非同构104点/208边图。描述为13点带 loops/semi-edges 基 multigraph 的 Z8-voltage lift，随后经过 symmetry-breaking repair；因此不能只用未经 repair 的电压模板代替实际104c。

本地绑定的是 **104c**，primary raw 为

[官方104c edge list](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/104c_d4D4.txt)。

已有原始与规范化文件：

- `research/ddp/breadth_20261027_wave2/sources/bhakar104_source.txt`；
- `research/ddp/breadth_20261027_wave2/sources/bhakar104.edges`；
- 旧同规则 case 的 `research/ddp/breadth_20261027_wave2/extension105_d4/source.edges`。

`sources/bhakar104_check.json` 保存同一 raw URL、2026-10-27读取日期、n104/m208、simple、min=max degree4、D4。它是历史source验收，本次没有重跑或重新parse图。旧 `d4_vertex_split/source104.edges` 亦标注同一104c，但本次不用它取代同规则的原始 source。

## 新根接口成立，但本域早已执行

若在104/208全4源中删除两条顶点不交的旧边 F，四端点为 P，再添新点 z邻接全部P，则n105/m210全4正则、simple。令T=G−F，所有删除边的两端都在P，故

`d_T(P,t)=d_G(P,t)`。

理由是从整个P集合到t的最短路不必经过一条P内部删除边：若经过，从下游P端重新起步即可更短。因此新根R4恰当且仅当原源四个closedR3球并覆盖全部104。此条件本身不保证旧旧D4；旧路可能被删除边破坏，完整候选仍须检查旧旧。

## 同一实际 strict NO 的直接原始证据

原 case 是

`research/ddp/breadth_20261027_wave2/extension105_d4/`。

其 `inputs.json` 的字面scope就是：

> Fixed public104c source; replace each unordered pair of vertex-disjoint source edges by four spokes to one new vertex104. No other edge changes.

已读原 `REPORT.md`、`production.json`、`run.json`、`terminal.json`：

- 全21528对源边已访问，其中624对共端点不合法；
- **20904/20904合法两不交边对全部评分，found_D4=false**；
- 最好保存候选仍有8个普通无序distance>4点对；独立 `best.independent_check.json` 对其105根确认D5、4正则、210边；
- 原生产CPU0.298779秒，原整批0.766514469秒，restarts0、pending空。

这些是旧实际数值，不是本次重验。不能把“best D5/8坏对”写成对每个候选逐一测得的全直径，但“全合法参数无D4”已由原完整范围支持。

canonical `research-wiki/experiments/ddp-wave2-extension105-d4.md` 的 reasoning 也准确指向本操作。后续固定best的40740个2-switch和230个九点补全没有改善，均属历史，不启动重做。另有旧 `d4_vertex_split` 和更宽 split/absorb NO，但本门不需要借它们证明此处结论。

`run.json` 中 `entire_extension_family_exhausted=false` 是“不排本源任意扩张”的边界，不否定上面这个明确 two-disjoint-cut/four-spoke 参数域已经穷尽。

## 停止边界

结论仅为 **fixed Bhakar104c / 删两条不交原边 / 一新4-star / 无其它修改** NO。它不排Bhakar另外两张104图、其它源或一般105/max4/D4；也不把旧98源当依据。按本轮只选这一源的授权，不改换104b/其它source，不新cut/R3/BFS/图/solver。

本次复用现有官方缓存，无新HTTP/download。一次只读metadata reader遇到旧distance cache为list而非dict，异常发生在访问字段时；未提取或处理其中距离，也没有启动图计算。随后只读原报告/终态完成scope绑定，此异常纳本门准备成本，不重跑任何验证。

三个成功标准库只读进程measured CPU合计0.001654802秒；含文本检索、初始reader失败与文档准备，保守charge0.50/1.5秒。新source验收、距离球、BFS、候选枚举、图、参数、solver、Lean、外审均0。完成即停。

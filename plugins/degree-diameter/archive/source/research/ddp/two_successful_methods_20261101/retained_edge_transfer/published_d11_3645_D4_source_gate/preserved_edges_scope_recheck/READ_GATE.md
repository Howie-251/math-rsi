# Actual3645：保全部旧边的扩张没有剩余pin接口

结论：直接继承既有严格NO，当前保边范围不应再跑球、solver或补点搜索。本门没有换源/参数；旧645条插入层边猜测需要删除旧edge，因此不属于本次问题，也不在此获得授权。

## 实际源与元数据

已读 `STAGE_STATE.json.source3645_existing_scope_recovery`、上层原READ_GATE、原source目录的SOURCE_PROFILE/COVER_RESULT/FREE_R3_CACHE及作者README说明。实际源为Bhakar在Yugeswardeenoo W(9) double/spread-twin 3444基图上做201次absorbed-deletion insertion的3645点图，不是45×81 affine模型。degree profile直接继承：m20044；3638点degree11，7点degree10，各只有一个free slot。

唯一free labels：3456、3489、3564、3571、3583、3603、3643。没有其它可接入旧点。源 literal 为 `research/ddp/more_graphs_20261027/d11_D4_current3645/source3645.edges`（作者类型注释，无整数NM header）；`source3645.header.edges`是仅补3645/20044 header的格式副本。原recipe/README/insertions/verification均已缓存。当前主表3645继承root已核值；历史desc_g4仍3444的滞后不作为新门槛。本门0新web、0literal解析、0degree重新统计、0D4验证。

## 严格全保边NO，不只是七pin星形失败

原COVER_RESULT已给出七free source闭R3并集只覆盖2902点，遗漏743点；首漏点6距每个free点都是4。其状态明确为 `ALL_EDGE_PRESERVING_EXTENSIONS_OF_FIXED_SOURCE_EXCLUDED_BY_FREEPORT_R3`，范围允许任意正数new vertices/helpers，甚至额外old-old边，只要求保留全部旧source边、maxdegree11和D≤4。

所有饱和旧点不能接新增边，所以任何新增边的旧端都只能是这七个原free点。若某new vertex在4步内到达旧target6，取其路径上最后一条非source边：其后旧端为free，且至多剩3条旧source边；但每个free到6均距4，矛盾。新增old-old边与多helper都不能绕过这个last-nonsource-edge障碍。该既有证明关闭的是整个保边增广接口，不是某固定新点邻域或小样本。

因此当前没有一个仍开放的保边pin问题可供数值；不得把“有7余度”误读为可补一个点。原负结论不排删改旧边、别的源或一般N(11,4)，但这些已是不同问题。

## 旧删改范围只作边界，不恢复运行

同源另有已完成的2673原twin/line-host paired cuts（47新根pass后oldold全fail）、679 firstbad-derived switch项（138 oldoldfail）和intact-square buddy入口0例。它们既不变更本全保边NO，也不等于所有删边构造No。

历史645条插入层边u–v的“删uv并将新点连u/v及free7”建议明确是NOT_SELECTED、未枚举；因为删除uv，不是本次保全部旧边范围的剩余空间。这里不把它升级为当前下一问题，不补缺失端点球，不续旧UNKNOWN/seed，也不换一批源。

本门只读与落盘，保守计本次整理0.5CPU，旧原source-gate读门1.0CPU历史不改。0source/BFS/球/solver/field/graph/Lean/ARIS/HTTP/索引；不改STATE/Wiki/pages或唯一Goal。当前STOP，向root报告“保边无剩余接口”。

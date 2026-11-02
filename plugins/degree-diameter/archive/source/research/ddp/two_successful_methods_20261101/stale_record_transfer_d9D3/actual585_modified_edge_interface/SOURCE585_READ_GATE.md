# (9,3) actual585：改旧边接口只读门

实际源是官方 Q′8 极性商图，**585点/2600边，65个8度绝对点A＋520个9度core B**；不是9正则，也不是Cayley源。来源为 [官方说明#93](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html#93) 及 [字面隐式邻接表](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt)，说明引Delorme1985。原literal `research/ddp/polarity585_replication/source585.implicit_adj.txt` 与 `SOURCE_PARTITION_CHECK.json` 已存；本轮未读解析源邻接或验证D3。

继承actual数据：A独立，每A有8个B邻点，每B恰有1个A与8个B邻点。A为闭一球perfect1code，各A互距3。缓存 `d9_D3_polarity_cover_prediction/PORT_R2.json` 给65个端口R2，大小73；`BLOCKS.json` 给520个core的九端口R2集合，已绑定Steiner3-(65,9,1)。旧任务的完整源D3由primary继承，不把结构R2检查说成全源D3验收。

## 已关闭范围必须继承

* `d9_D3_polarity_cover_prediction/THEOREM.md` 严格排除固定源保全部585点/2600旧边的任意有限cap9/D3增点，即使允许任意追加旧旧、新旧、新新边。bulk portmatching本身不能绕过此定理；必须改变旧边。
* `polarity585_replication/DERIVATION_PACKAGE.md` 对保每个core类及规定完整cross连接的任意复制给n<=65Delta。
* `gadget_preparation/REPORT.md` 的八anchor parallel-class规则：删八anchor邻边、转接到各自唯一port、新点连八anchor+固定port、任意匹配剩56ports，统一漏八个port。该纸面NO独立于sigma，不可用换involution重启。
* `sigma_edge_spread/REPORT.md` 只对actual固定p0/sigma的32条旧core边，四个16-port union的exactcover完整失败（17节点），最大兼容数2。`paired_edge_spread_gadget/RESULT.json` 明确五cut+9star+一core-port修复+32portmatching producer从未启动。此特定前提NO不排所有非sigma core删边与portmatching。

## 仍可能改变路线的具体接口

65个度8 ports可匹配其中64个，留一个p；不能给奇数65个ports作完美匹配。旧条件graft已有精确度数账：五条不交core cuts释放10个槽，9端点接新9星，另一core端点w补到p，余64ports作32条旧旧matching。若w-p原非边，则候选586/2637全9度，保2595/2600旧边。这里只继承接口，不声称存在所需路线或合法图。

## root最终选定的下一唯一问题（仍未运行）

选四条顶点不交旧core边并删除，新点z连接八个core端点及一个绝对点p；其余64个绝对点作32条旧旧matching。条件图586/2637全9度，保2596/2600旧边。所查相关旧scope里未定位此exact四cut+8core/1portstar规则的strictNO：它不同于已排八anchor转边规则（删8边并向各自port重接），也不同于sigma前提已败的五cut+9corestar+w-p规则。不能互套。

**当前唯一可推翻预测：** 存在p与四条不交corecuts，使旧源 `R2({p}∪八个cut端点)` 覆盖全部520core。这是新根必要条件，不是完整图成功预测。

该条件有精确路线解释：星pin集包含全部删边端点，因此删这些pin内部边不改变到pin集的距离。新加A-A matching不可能出现在z到core的至多3步路中：若z第一步到p，p未匹配；若第一步到corepin，再到A并用matching，第三步仍在A。因此新根core覆盖只能由原源pin集合的R2给出。新根到其他A、全部旧旧对仍需另验，不能由这一条件代替。

所需下一数据是实际core-target R2 bitset支持。旧wave3曾计算R2，但目前所存RESULT只有大小分布、12个贪心组与相应未覆盖点；PORT_R2/BLOCKS则保存绝对点及port/core关联，没有完整core-core R2表。本读门不重建它，不作cut/matching枚举。先前“去sigma选四个portspread”的想法保留在JSON为未选历史，不构成并行计划或已做实验。

只读与准备保守0.8CPU秒＋小文件写入实际成本，cap2；详细累计见SOURCE585_READ_GATE.json。本轮0新BFS、0路线/边集枚举、0候选、0solver、0field、0图。读取门完成即停，任何数值门另待root授权，不动root/Wiki/其他成果。

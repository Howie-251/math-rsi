# DD Portfolio research brief

## Problem Statement

恢复入口先读[方法账本的说明与家族目录](research-wiki/DDP_METHOD_LEDGER.md#家族目录)，再按家族、目标(Δ,D)、source及已排范围检索相关条目和实验节点。完整字段在[机器账本](research-wiki/DDP_METHOD_LEDGER.json)；不要每次把整页或整个JSON重载进上下文。

当前Goal为4≤Δ≤12、D∈{3,4,5}，找超过对应最新公开下界的完整简单无向图。27格是选题池，不要求全部求解或证明精确最优。执行计划为[RESEARCH_GOAL](context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)，后续导航见[NEXT_SESSION](context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md)。已验证新下界仍为0。

## Constraints

默认最多两条主机制，代理合计≤8 CPU workers；每个批次先明确结构、范围、预算和停止条件。按用户广度指导比较有实质区别的覆盖机制，同一模板停滞后及时跳出，不因局部坏对下降自动追加seed或邻域。

保存生成参数和完整边表，按实际对象核验简单性、degree、连通和全对距离；必要条件、symbolic容量通过与局部满秩都不是图存在证明。实际完整图、控制器、条件性lift和仅局部根诊断分列。真实发现之后再安排Lean；无哈希、无新依赖或无关防护流程。持续工作约每小时及重要变化更新原research/progress.html，报告不代表暂停。

## What I'm Looking For

选择或重启前，先查对应家族的已试构造与目标差距，给出完整V/E规则、degree/n公式、已保证的覆盖、尚未闭合的目标，以及相对旧失败改变的实际数学条件。未被排除不等于有成功直觉。

每次有限实验收束即通过现有Research Wiki helper记录目标/保存门槛及日期、真实距离与计数类型、验证范围、已排子族、可复用启发和重启条件。整轮汇总是索引，不能代替逐方法记录；原scope已关闭时不换seed重跑，UNKNOWN不作不存在性。

## Background

启动材料在context/DD_PORTFOLIO_START_20261026/；唯一知识库为research-wiki/。方法账本与canonical experiment节点保存早期M1/M2/M3、仿射群、陪集塔、匹配、四轨道及后续wave的结果。人工意见仍在research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md；该文件名不表示恢复D2。

本次替换前的Brief原文已归档至research/ddp/wiki_backfill_20261027/archive/。不另建第二套Wiki，也不因压缩摘要丢失已验失败。

## Non-Goals

旧N(8,2)、n61谱、h5/h6、旧SAT及D=2均已暂停，不自动恢复。保留57≤N(8,2)≤61、历史已闭范围、RAW证据和Lean缺口。已知基线复现、同阶新实例、局部坏对改善、容量通过、UNKNOWN或模型赞同都不计新下界，不为已知文献排除重跑穷举。

## Domain Knowledge

- 度数和阶数合格仍须共同覆盖所有点对；控制器的实际D不能当作最终lift的D。普通无序坏对、NB有序缺项、代表根漏点及容量下界必须分列。
- 唯一短路或统一端点容量不足通常要求改变路线结构，同一模板的标量调参不能补出缺失路径。有限profile失败仅关闭所述批次；只有完整必要证据才能排除对应族。
- 旧single-extension的“8”是8个起始profile，实际已用满12/11邻居，不是8个old pins上限。相连双新点a-b各有Δ−1个old pins预算，精确合作条件为R4(A)∪R3(B)=V及R4(B)∪R3(A)=V，并逐旧点满足现有degree deficit。
- 最新外部review仍仅覆盖固定192点商保留旧边、只向亏度点加边的exact-NB5局部障碍；[回执](reviews/ddp/controller_quotient_obstruction_20261027_raw.json)不覆盖其他192控制图、wave8或wave9。wave8/9没有新review receipt；本地独立检查与外部review分别报告。

## Existing Results (if any)

最新wave10已终态：72×F2⁴逐边仿射1152图独立D5/29152个>4无序对（目标8,4）；W(3,5)+双侧2factor312图独立D4/4090个>3无序对（目标8,3）。两个源删边降度被唯一三路挡住，syndrome码商全27格被球界挡住。账本现152条；都不是新下界，不追加已停预算。


已验证新下界：0。逐项完整状态和证据以[方法账本](research-wiki/DDP_METHOD_LEDGER.md)检索结果为准。

- wave8 insertion171：目标(7,3)，完整171源独立BFS确认maxdegree7、实际D4，79个普通无序点对距离>3（old-old68、new-old11），不是新下界。[检查](research/ddp/breadth_20261027_wave8/insertion171/fallback.independent_check.json)
- wave8 Menon1296：目标(8,4)，完整1296源独立BFS确认8正则、实际D5，69737个普通无序点对距离>4。[检查](research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.independent_check.json)
- wave9 cooperative37630：目标(11,5)，保留37628源全部旧边，已独立检查degree及新增规则；仅从两个新点完成BFS，两根ecc均6，new-old坏无序对25，已足以否定此候选D5。未执行37630全源BFS；25不能写成all-source坏对总数，全图实际直径不得冒填。[局部检查](research/ddp/breadth_20261027_wave9/cooperative37630/best.independent_check.json)

这些失败及其范围已停止，不构成自动继续队列。下一个构造须依据账本中的覆盖瓶颈和重启条件另定有限范围。

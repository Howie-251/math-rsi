# DD Portfolio research brief

## Problem Statement

恢复入口先读[方法账本的说明与家族目录](research-wiki/DDP_METHOD_LEDGER.md#家族目录)，再按家族、目标(Δ,D)、source及已排范围检索相关条目和实验节点。完整字段在[机器账本](research-wiki/DDP_METHOD_LEDGER.json)；不要每次把整页或整个JSON重载进上下文。

当前Goal为4≤Δ≤12、D∈{3,4,5}，找超过对应最新公开下界的完整简单无向图。27格是选题池，不要求全部求解或证明精确最优。执行计划为[RESEARCH_GOAL](context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md)，后续导航见[NEXT_SESSION](context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md)。数学验收改进参数2项，完整Lean仍0项。

## Constraints

最新人工优先级：①已有结构依据、较可能产出完整新图；②尚未深入入口；③难点攻关。先预测并检验覆盖直觉，再投入有界算法。未尝试本身不是最高优先级，局部坏对下降也不自动授权续算。

最新trade-off按用户“不要过度验证之前的，尽可能多产出，验证适量”执行：已验基图、未变代码和既有证据直接复用。同一扩张族由生产程序一次检查新增度数与当时全旧图的完整覆盖即可，不逐图重复root全源BFS、互审或Lean审计。新的机制或参数首次命中再安排一次必要独立核验；观察到具体矛盾才扩大检查。当前主力是更多完整图，Wiki/HTML按批次简要同步。完整数学覆盖标准保留，形式化真实未完状态保留，不以减少重复验证替代完整图。

当前人工指导是“先做针对性的构造直觉研究，再集中攻关”；暂缓独立模板大筛。代理合计≤8 CPU workers，当前围绕同一个承重覆盖问题做机制分析、反例、实验和核验。每批有具体预测、范围、预算与复评点；有问题与反馈时可深入，不以未成功或总坏对下降自动无限续算。

保存生成参数和完整边表，按实际对象核验简单性、degree、连通和全对距离；必要条件、symbolic容量通过与局部满秩都不是图存在证明。实际完整图、控制器、条件性lift和仅局部根诊断分列。真实发现之后再安排Lean；无哈希、无新依赖或无关防护流程。持续工作约每小时及重要变化更新原research/progress.html，报告不代表暂停。

## What I'm Looking For

当前唯一分析入口是原清单(6,4)441点PSU三轨道源：恢复实际连接与四步覆盖规则，先检验具体几何解释再决定新参数/算法，尚未启动新数值搜索。上一批原(10,4)C25/r25的1040604规范参数已完整失败；Exoo72最小73插入4992120项必要覆盖全失败、固定循环放大已关闭；Rajiv5334固定2667基图的两条短路阻止任何>2-sheet普通cover。这些精确范围与反例在195条方法/实验账本中，不原样重跑，不把它们扩成原题无望。自由C14等困难协调问题保留但不机械启动solver。

当前数学最强：N(11,5)≥37631、N(12,5)≥42398，共59个不同阶数完整例子，覆盖2个参数。37631/42377代表图此前全源通过；其后按一次新增degree与完整current-baseR4归纳接受，不重复全源/互审。完整参数及生成器在research/ddp/more_graphs_20261027/delivery/。完整Lean实例0，Goal ACTIVE，旧D2暂停。

### 上一轮72控制图对照（已完成且已收束，不再派发）

最新纠偏：不深陷几百坏点对的微调。当前1152单/双边/port-preserving局部线已收束；2520筛选实际未启动且已取消。以下对照结论保留为选择整体覆盖规则的依据，不再据此追加局部边、候选或轮次。后续继续依据必须是能同时保证整类点对覆盖，不以总坏对小幅下降代替完整新图。


2026-10-27最新人工修订：先做针对性的可检验构造直觉，再集中攻关。上一轮研究同一72控制图：原F3⁴成功5832与cached F2⁴/global offset0失败1152。先冻结预测、用推导/现有数据/小实验检验，解释覆盖缺口怎样产生，结果要实际改变下一连接规则。暂缓横向模板大筛；不把成功复现或文件更新算新成果。严格排除不重跑；有具体问题或有效反馈可增加有预算的研究，不要求每次先有新定理。

本轮P1已验中：best68的base0→10只有AACA和DCC，两张不同法向的8点超平面任意平移并恒12；固定T/b的offset再自由也不能修该槽。原F3同槽AACA已rank4/81，区别是方向损失而不是没有控制路线。

后续受控检验：只改0→18的b修目标，却坏37↔63紧路，预测与1152全源验图一致；联动T'=S T,b'=S b保持反向方向8，目标与468紧槽全保住，仍有12800全图坏对。已定位非目标点对(0,5)：闭路ABCD的rank仍2，像从{0,5,8,13}变{0,4,8,12}，self0总并16→15；所有16源值均漏x XOR5，consistent offset也不能救。所得保护468紧路与72self闭路并集的认识保留，但不继续局部修补；不因总坏对少于另一改动而盲目续算。证据：research/ddp/breadth_20261027_wave12/route_complementarity/。

## Background

启动材料在context/DD_PORTFOLIO_START_20261026/；唯一知识库为research-wiki/。方法账本与canonical experiment节点保存早期M1/M2/M3、仿射群、陪集塔、匹配、四轨道及后续wave的结果。人工意见仍在research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md；该文件名不表示恢复D2。

本次替换前的Brief原文已归档至research/ddp/wiki_backfill_20261027/archive/。不另建第二套Wiki，也不因压缩摘要丢失已验失败。

## Non-Goals

旧N(8,2)、n61谱、h5/h6、旧SAT及D=2均已暂停，不自动恢复。保留57≤N(8,2)≤61、历史已闭范围、RAW证据和Lean缺口。已知基线复现、同阶新实例、局部坏对改善、容量通过、UNKNOWN或模型赞同都不计新下界，不为已知文献排除重跑穷举。

## Domain Knowledge

- 度数和阶数合格仍须共同覆盖所有点对；控制器的实际D不能当作最终lift的D。普通无序坏对、NB有序缺项、代表根漏点及容量下界必须分列。
- 唯一短路或统一端点容量不足通常要求改变路线结构，同一模板的标量调参不能补出缺失路径。有限profile失败仅关闭所述批次；只有完整必要证据才能排除对应族。
- 旧single-extension的“8”是8个起始profile，实际已用满12/11邻居，不是8个old pins上限。相连双新点a-b各有Δ−1个old pins预算，精确合作条件为R4(A)∪R3(B)=V及R4(B)∪R3(A)=V，并逐旧点满足现有degree deficit。
- 最新实际外部review为wave11 Gemini3.8Flash/high SUCCESS，仅接受固定72/global/offset0闭合、GQ平均容量和80点41变量精确覆盖公式；群阶、免独立验图和未经测量的求解器原因外推未采用。回执与处置见reviews/ddp/wave11_scoped_review_20261027*。新的commuting强化是本地纸面证明，不冒充已获外审。

## Existing Results (if any)

当前阶段：一个明确对照研究，新增两个受控1152图而非大量模板。P1方向上界12/16得到支持；只改b的图D5/13424，矩阵与b协调后D5/12800，原图D5/12384仅复用。目标与468紧路的预测均验中，新增同fiber反例解释了一个具体损坏机制；没有新下界。方法账本159条记录不等于独立方法数。本阶段证据：research/ddp/breadth_20261027_wave12/route_complementarity/REPORT.md。


历史wave11已终态：fixed72/global线性/offset0的2419200规范输入，仅1024通过26必要四路词，完整R4全失败；最好1152图独立D5/12384无序>4。GQ80精确MILP UNKNOWN、无incumbent；norm5/PSL11固定660图单位根漏132，root独立漏点证实。GQ交换障碍给出新选边原则：四个过线入口两侧内部邻接都必须不与几何矩阵交换。q8/max3非正则1170入口仍开放，不因奇偶误排。新下界0，账本158条（非独立方法数），本轮不续已停seed或窗口。


已验证新下界：0。逐项完整状态和证据以[方法账本](research-wiki/DDP_METHOD_LEDGER.md)检索结果为准。

- wave8 insertion171：目标(7,3)，完整171源独立BFS确认maxdegree7、实际D4，79个普通无序点对距离>3（old-old68、new-old11），不是新下界。[检查](research/ddp/breadth_20261027_wave8/insertion171/fallback.independent_check.json)
- wave8 Menon1296：目标(8,4)，完整1296源独立BFS确认8正则、实际D5，69737个普通无序点对距离>4。[检查](research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.independent_check.json)
- wave9 cooperative37630：目标(11,5)，保留37628源全部旧边，已独立检查degree及新增规则；仅从两个新点完成BFS，两根ecc均6，new-old坏无序对25，已足以否定此候选D5。未执行37630全源BFS；25不能写成all-source坏对总数，全图实际直径不得冒填。[局部检查](research/ddp/breadth_20261027_wave9/cooperative37630/best.independent_check.json)

这些失败及其范围已停止，不构成自动继续队列。下一个构造须依据账本中的覆盖瓶颈和重启条件另定有限范围。

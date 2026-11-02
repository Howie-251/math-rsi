# 四blocker转接＋五helper合作：342域完整NO

**最新分类：**一次只读旧helper-ball的K5放宽检查得到342个case即使忽略degree、五helper全互连也仍缺base目标；“K5通过而全部合法H失败”为0。所以下列指定oldP的障碍不是H度容量不足，而是被删附件的一步预算没有由其它oldP追回。最新同Ccase累计 **37.985870069 / 120 CPU秒**；没有重算球或搜索新H。原有限门的37.767076346成本保留为历史。

实际有限门已完成：**342个未选center、全部5886个inclusion-maximal合法helper图H均失败**。其中324个先失败于helper两两≤4，5562个helper pairs过门后仍有helper不能四步覆盖base。没有生成16417图，所有进程终态。

这只关闭当前accepted16416上、恰四blocker的342个center、确定性blocked donor-edge转接、新Z完整原sourceN及五helper任意H的规则；不排S5、任意repair、多helper或一般(16,4)。不续timer或新中心族。

## 预测与真正执行的改变

此前直接在当前余度pins上找≤16个closedR3 cover的批次保持UNKNOWN。本次 [PRED](PRED.md) 改变了生成规则：每个v从同一accepted16416重新开始，blocked source点先删其唯一donor-clone边，再接新Z；四donor因此得到helper内部余度，Z仍接完整原N(v)。只删除这些指定边，原15552的116316条source边始终保留。

正预测“至少一个v/H可协作恢复D4”被完整有限域推翻。不是只试了一个helper拓扑，也不是先后在同一图上累积删边，更不是只挑342中的162个四blockedslots对象。342来自**四个不同blocking owners**；每个owner可负责多个blockedslots。

[COOPERATIVE_BLOCKER_REPAIR_PAPER.md](COOPERATIVE_BLOCKER_REPAIR_PAPER.md) 已先给出精确iff。旧source degree14的容量2共享点没有删掉，P_i与P_Z重叠对应cost2。H按“任何缺边都不能合法再加”筛inclusion-maximal，不以最大边数取代maximal。

实际出现三种effective cap向量：

| effective helper cap | 全合法H | 全inclusion-maximal H |
|---|---:|---:|
| 4,4,4,4,2 | 704 | 6 |
| 4,4,4,4,1 | 320 | 4 |
| 2,2,2,2,1 | 145 | 31 |

完整五点10边有限枚举与各H字面mask存于 [ALL_CAPACITY_MAXIMAL_H_DOMAINS.json](ALL_CAPACITY_MAXIMAL_H_DOMAINS.json)。固定端口集时添加合法H边只缩短距离；因此这些maximal H的失败覆盖相应全部合法H，未漏较稀疏成功者。

## 新缓存完整，没有把旧4050行缺项当空

当前16416 literal为新距离问题一次parse，未重新验D4或field。以bitset递推生成全部16416行R1/R2；所需15552个oldsource-root R3中，3186行从旧available缓存复用，**其余12366行实际新计算**。旧4050缓存里的864个clone-root没有被误当成所需oldsource根。

移去四donor顶点后，base为原15552＋860个完整clones，共16412点。donor→其oldsource center的retraction固定base，故current闭球屏蔽四donor目标后恰为base闭球。它不是把被删donor边原样当base路径。每v的五组P、B0…B3均真实存在，闭R0端口本身保留。

- [IMMUTABLE_BASE_DISTANCE_SCHEMA.json](IMMUTABLE_BASE_DISTANCE_SCHEMA.json)：actual labels、row bytes、递推与retraction范围。
- `CURRENT_ALL16416_R1.bits`、`CURRENT_ALL16416_R2.bits`、`CURRENT_OLDSOURCE15552_R3.bits`：实际新缓存，2052 bytes/row，little-endian。
- [ALL_VISITED_CENTER_HELPER_INTERFACES.json](ALL_VISITED_CENTER_HELPER_INTERFACES.json)：全部342个Nv、donor roles/labels、删边、P集、容量及初始basecost。
- `ALL_VISITED_CASE_HELPER_B0_B3.bits` 与 [HELPER_BALL_SCHEMA.json](HELPER_BALL_SCHEMA.json)：case/helper/radius顺序与base目标掩码。

## 为什么端口合法仍没修回旧四步路线

对每个H做Floyd5：真H边cost1，base集合间距离0/1/2对应cost2/3/4。允许多次helper/base交替；没有把base路径限制成只能用一次。先查全部helper pairs，再对每helper按最后helper g的准确界

`union_(q(h,g)<=3) B_(3-q(h,g))(P_g) = all16412base`

检验完整覆盖。[ALL_MAXIMAL_H_STAGES.tsv](ALL_MAXIMAL_H_STAGES.tsv) 返回全部5886个首失败，[ALL_FAILURE_ROUTE_DECOMPOSITIONS.jsonl](ALL_FAILURE_ROUTE_DECOMPOSITIONS.jsonl) 给真实首helper／target类别、初始与Floyd矩阵、每条last-helper的old-leg预算及原donor附件损失；没有继续优化坏对总数。

第一个实际反例是v=15、Hmask255、helper15560到旧source target1。此前经删去附件15560–6421、–6434或–6462，可以用“1条附件边＋3步base腿”四步到target。合作后helper15560虽直接邻接其余四helper，相关新末段仍至少需要“1条helper边＋1条到base的边＋3步base腿”，即5步；另一个last-helper连3步旧腿也不够。该例说明自由helper内部连接能修连接性，却不能自动追回被donation消耗的一步预算。它只是一个已保存的具体反例，整体NO来自全部5886项的精确门。

若截断Floyd返回INF或>4，只解释为无≤4路线，不冒称实际图不连通或距离无限。没有命中，所以正向五helper ordinaryBFS／完整新图构建阶段均未进入。

## 成本与停止

唯一driver1114998／child1115001、session32282已exit0。新增child CPU **1.259067秒**、driver **0.016844857秒**、准备预留1.0；连同prior available-case35.491164489，累计 **37.767076346 / 120 CPU秒**。无编译、MIP、solver、sourceD4/allrootBFS、field、Lean或ARIS重跑。

[RESULT](RESULT.json)、[TERMINAL](TERMINAL.json)、[HANDLE](HANDLE.json)、[finite_child.py](finite_child.py)、[run_once.py](run_once.py) 保存全部实际终态。图／参数／Lean计数均0。完成即STOP，不S5、seed、更多helper或另一轮timer；旧16416及专家包未修改。

## 随后旧球K5放宽：区分路由损失与H容量兼容

先保存 [K5_RELAXATION_PRED.md](K5_RELAXATION_PRED.md)，再只读已有342×5×4个helper球，以degree完全忽略的K5作为同oldP最强helper连接。对每helper h精确检查

`B3(P_h) OR union_(g!=h) B2(P_g) = all16412base`。

K5中所有helper pairs直接距离1；此处只问base覆盖。K5不被称为合法cap16新图；它是所有合法H的距离放宽。两类实际结果为：

| 路由分类 | case数 |
|---|---:|
| 即使K5也缺base目标 | 342 |
| K5全base覆盖，但所有degree合法H失败 | 0 |

[K5_RELAXATION_POSTPROCESS.json](K5_RELAXATION_POSTPROCESS.json) 保存每case的cliquePASS布尔值、全部五helper cover大小、首helper、首target实际类别与五种last-helper旧腿预算。第二类确实为空，未编造示例。

具体预测“v15/helper15560到target1即使K5仍失败”得到支持。H255此前已使15560直接连接其余四helper，因此K5不再缩短这一行的helper代价：自己仍只可用3步旧腿，其他helper只可用2步旧腿。自己的保留P与helper15563连3步旧腿也到不了；15564、15568、Z的旧腿最短3，组成1＋1＋3＝5，仍超4。这个预算分解解释了为何增加helper边无济于事，而不只是报一个剩余漏点数。

因此在这342个确定donation/P集上，任意H乃至忽略degree的K5都不能恢复D4；不能归因为某个helper少一条合法H边。要绕过本障碍需要保持被损伤的关键旧附件或实质改变oldP／其它规则，**本批没有自动启动这些变化**，不排其它中心族或一般16/D4。

后处理由 [k5_relaxation_once.py](k5_relaxation_once.py) 执行，实际CPU **0.068793723秒**，准备0.10。首脚本在读取任何数据前发生条件表达式语法错误，已在 [K5_INITIAL_SYNTAX_FAILURE.json](K5_INITIAL_SYNTAX_FAILURE.json) 保留，未测CPU保守计0.05；没有重置预算。沿原37.767076346后最新累计 **37.985870069 / 120秒**，此次收费小于授权1CPU。新sourceparse／ball／Hsearch／BFS／field／solver／Lean／ARIS／图全部0。旧原始球、有限门RESULT/TERMINAL未修改，完成STOP。

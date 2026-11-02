# 非整层完整旧邻域克隆：append／one-out-two-in完整NO

**最新纸面补充：**一次只读旧profile后处理得到342个blocker4中心的责任四元组全部不同，group最大值1。原数值门的append／one-out-two-in终态不改；min4阻塞直接排k≤3 out／k+1 in，再由group max1<5排4 out／5 in。最新同case累计 **2.956499532 / 20 CPU秒**；没有测试任何新packing或候选。下方先保留首次门的范围与成本，末节给后处理和扩展证明。它仍不是最大864证明。

## 首次数值门：原范围与成本

结论只针对**当前已接受864个center的二元选择**：不能直接追加一个未选旧center，也不能删去一个既有clone再加入两个互异center的clone。每个原center至多复制一次，允许删去后重新加入该center。它不是“864最优”，也不是全source非整层packing无解。

## 实际问题与预测

本轮先读 [只读接口](../FULL_VERTEX_CLONE_PACKING_READ_GATE.md)，继承原15552源及864中心；[PRED](PRED.md) 预测每个未选center的满端口邻点至少由两个不同既有clone负责。真实源简单开邻域始终冻结在原15552源，不从扩大的16416图复制，也不要求整个W27-plane、center独立或邻域两两不交。

预测获支持，实际更强：**所有14688个未选center都有4至15个不同blocking clone owners**，没有0或1个。原864个center各只有自身clone作为blocking owner。因此失败不是pair搜索只试少量样本，而是任何单移除都无法释放一个新center。

## 为何这个筛选精确

令R(w)=16−d_source(w)−L864(w)。实际旧load仅0/1，所以每个R=0的slot恰有唯一责任clone。未选center v的clone若要直接加入，其N(v)中不能有R=0邻点。

若删除角色u，其N(center_u)上的余度各增加1。v可单独放入，当且仅当v所有R=0邻点的责任clone都等于u。若blocking owners有两个以上，删除一个clone不能同时释放它们；实际每个未选v至少有四个。

因此对864个删除角色，完整可行center列表均仅为被删center本身。二元域禁止同一center加入两次，故没有任何互异pair进入下一比较：**864/864删除域完成，pair domain=0、pair checks=0**。这包括“先删后re-add”的选择，没有把它机械排除。

代码仍给出了若pair存在时的精确条件：两个新N的共享slot须满足R(w)+1_N(u)(w)≥2。degree14旧点允许容量2及邻域重叠，未被错误收紧为N(v)∩N(t)=∅。此次这道pair层没有实际候选可进入，不声称观测过某个成功重叠pair。

## 输入与返回对象

一次解析现成作者邻接表 `research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt`，每行首列为旧label，后续列为冻结simpleN；center顺序来自 `degree16_plane864/PARAMETERS.json:source_center_labels`。未读取旧16416完整边表，未重建field或controller，未重新检验源D4。

实际残余分布为R0:12366、R1:3096、R2:90。R2端口保留在精确模型中；阻碍来自各未选center触及的满槽责任分散，而不是把degree14余度丢掉。

- [全部15552 center的blocking/slot/责任role记录](ALL15552_CENTER_BLOCKING_PROFILES.tsv)。
- [完整blocking数量分布](BLOCKING_SUMMARY.json)，包含未选center的owner数4..15直方图。
- [全部864移除角色与其可行center列表](ALL864_REMOVAL_FEASIBLE_CENTER_LISTS.json)。
- [864个移除域的实际终态](ALL864_REMOVAL_STAGES.tsv)；[pair阶段](ALL_PAIR_STAGES.tsv) 仅表头。
- [单次源码](run_once.py)、[RESULT](RESULT.json)、[TERMINAL](TERMINAL.json)、[HANDLE](HANDLE.json)。

源degree/load的计算仅为此新incidence余度输入；不是源直径或旧图全对有效性复验。原864中心和旧16416接受材料未修改。

## 成本、验收边界与停止

单进程actual CPU **0.283706889秒**；同case总计 **2.783706889 / 20 CPU秒**，包含继承read准备2.0与新准备预留0.5。输入解析、完整profiles与全部输出均在actual进程计时中；无编译、solver、子数值任务或预算中断。全部进程已终态。

新完整图0；source-D4／old16416 BFS、field、Lean、ARIS均0。未得到865-center候选，当然不声称新16417图或直径验收通过。既有generic FullNeighborhoodClones距离接口只继承，未新实例化。

停止append／one-out-two-in范围，不自动转2→3、seed或I33。任意更大改组、不同incumbent、多重复制及全source非整层最优性均未由本轮排除；没有增加graph、参数、Lean或独立方法成果计数。

## 随后唯一旧profile后处理：342个blocker4组全为单点

按另行授权，先写 [BLOCKER4_GROUP_PRED.md](BLOCKER4_GROUP_PRED.md)，再执行一次 [blocker4_group_once.py](blocker4_group_once.py)。只读原15552行profile一次，实际分隔符是tab；没有重写原文件、读source、重算degree/load或枚packing。

正预测“存在至少五个新center共享相同四个责任clone”被实际推翻。342个恰四blocker的未选center按完整排序role四元组分成 **342组**，group-size直方图 **{1:342}**，最大组 **1**。每组完整旧roles、对应旧center labels与真实新center都在 [BLOCKER4_GROUP_POSTPROCESS.json](BLOCKER4_GROUP_POSTPROCESS.json)，没有只保抽象代表或截取少量样本。

这给两个直接必要性结论，均限同一864 incumbent／一center至多一clone／冻结原simpleN：

1. 任何原未选center至少有四个R=0 slot责任clone。若要加入它，必须真正删除全部这些责任clone；添加别的新clone只会增加load，不能释放这些slot。因此删除k≤3个旧clone后不可能引入任何原未选center，k out／k+1 in全被阻断。
2. 删除四个旧clone再加入五个互异center时，若包含重新加入的旧center，则最终真正删除的旧clone少于四，已由上一项排除。所以五个新增center必须全部来自原未选集合。每个都须至多四blockers，而全体未选center至少四，故五个center必须拥有**同一个被删四元组**。最大组1不足五，4 out／5 in也NO。

第二项仅是完整有限profile加必要性推导，不是执行4out5in候选、pair或坐标余度检查；没有把单独可放入当作同时可行。它允许旧degree14的容量2，论证只使用真正满槽R=0的必要阻挡。

postprocess actual CPU **0.072792643秒**，准备另预留0.10，沿旧2.783706889后同case累计 **2.956499532 / 20秒**；本次授权自身≤1CPU。新sourceparse／degree-load重算／packing或pair测试／BFS／field／solver／Lean／ARIS／图均0。原RESULT/TERMINAL及其2.783706889成本保持为首次门历史，最新累计与terminal字段见后处理JSON。

完成停止。纸面扩展只关闭同一incumbent的≤4 out／k+1 in改进，不排五个以上旧clone的整体改组、不同incumbent、多重复制或完整非整层模型，不自动运行局部阶梯或global模型；后续由root基于这些数据另行决定。

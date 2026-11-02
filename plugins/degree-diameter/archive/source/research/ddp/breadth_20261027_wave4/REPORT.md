# 第四轮：全局几何生成、当前纪录扩张与一个明确商图

已验证新下界仍为 **0**。本轮没有越过当前(11,5)=37628、(12,5)=42342，也没有生成满足条件的46656点路由提升。参数变化如实作为同一机制的变体；UNKNOWN与明确失败分开记录。

|入口|实际产物与结果|终态范围|
|---|---|---|
|[H9全局三态](global_partial_fold/REPORT.md)|3个全局起点各50CPU秒；最好合法S4986、核心38383点。两段大S末态分别有1068/1124个实际点度13，不能当合法图。|这一个150CPU秒全局单点惩罚退火profile失败；没有排除一般逐fiber模型。|
|[全局单锚点分区](equitable_global/REPORT.md)|只用几何类型与一个绝对点，稳定为650个generic cells、12个H3 cells；全部33397点检查equitable。一次全局越线MILP无incumbent。|UNKNOWN；没有固定外部状态，也没有只优化旧S，但仍是cell-constant子类。|
|[新作者原始来源](pencil_source/SOURCE_NOTES.md)|取得37628/42342当前原图，直接邻接比较与主表一致；未取得pencil邻接公式、构造witness或距离证明。|有限来源侦察已结束，不能把没有找到说成作者从未公开。|
|[42342→42343](record42342_single_extension/REPORT.md)|全部14396个可接点R4球；8个有限profile最好仍漏648点，独立BFS一致。|只关闭此profile，没有一般不可行结论；未展开42343点图。|
|[37628→37629](record37628_single_extension/REPORT.md)|全部2504个可接点R4球；8个有限profile最好漏115点，独立BFS一致。|是上一行的degree参数变体，不虚算新大类；未展开37629点图。|
|[37628全局覆盖](record37628_global_cover/REPORT.md)|全部37628点覆盖约束、2504个二元变量、20260765个非零项。一次solver未返回；触及CPU硬限，无incumbent。|UNKNOWN。内部45秒时限未能及时返回，实际worker到56CPU秒结束；总59.07CPU秒。没有不可行证明或重启。|
|[H3明确对合商](controller364_quotient/REPORT.md)|两个绝对点作锚点，1-WL得到20单点与172二点cell；同时交换二点cell后逐边验证为involution。商图192点362边，最大度4、普通D5，exact-NB5缺6288有序对。|所有保留旧边的最大度4简单补边均被一个短障碍排除；补度搜索未启动。不排其他商、删边或控制器。|

## 为什么明确商图现在停止

20CPU秒的通用VF2入口没有返回生成元；root换用两个绝对点2、11的全局颜色细化，0.044CPU秒取得可直接逐边核查的置换。它固定20点，其余172对合并为192点。这里不用“cell必是群轨道”的猜测：构造置换之后直接验证它的平方和每条边。

商图度谱为4度152点、3度36点、2度4点，40个亏度点共有44个槽。root对保存边表作唯一一次全192根普通BFS及显式非回退walk枚举，独立确认D5与6288个exact-NB5缺项；非正则图未套用四正则计数多项式。见[quotient.independent_check.json](controller364_quotient/quotient.independent_check.json)。

关键见证点u=10已经满度，其邻居为16、126、157、183。令P为亏度集合，P∩B2(u)仅含184，且dist(u,P)=2；旧图没有u处NB5闭walk。任何新增边两端必须都在P。一个含至少两条新边的u闭walk，旧前缀/后缀各至少两步，总长至少六；若只用一条新边，恰五步要求两端均在P∩B2(u)，只能成为禁止的自环。因此不可能补出所需NB5对角。这覆盖有重复顶点的非回退walk，并非只检查简单五圈。

root的短见证核对见[root_obstruction_check.json](controller364_quotient/root_obstruction_check.json)。Gemini随后接受这段数学论证及其固定加边范围；该意见没有审全部代码、未确认新颖性，也不是Lean证据。原始回执和意见处置在`reviews/ddp/controller_quotient_obstruction_20261027_*`。

这是停止该固定商的充分依据，不等价于一般192点控制器不存在，也不说明所有可能46656点提升不存在。没有自动追加对合、锚点、删边邻域或补度起点。

## 剩余问题

几何部分折叠的直径充分保证保留，但此次全局生成没有取得足够大的合法状态；后续pencil规则仍缺具体邻接与证明。当前纪录加点的有限profile及一次完整覆盖模型均已收束。原专家材料仍保持03:15:51截点；后续状态以本报告和`research/progress.html`为准。旧D2/n61/Lean工作未恢复。

## 新三步规则与最后的31点有限构造

已完整恢复[Mizuno较新的degree16/diameter3原始实例](mizuno_d3_source/REPORT.md)：30点控制器由10个互不相交K3与6个C5组成，交汇为2-(6,3,2)设计。纤维为三维空间，逐边矩阵而非通用chart；原实例在F4上给1920点、十六度，没有内部translation。换F3的数值仅为810，未声明全局q3证书已经复现。

局部GL3(F3)完整枚举给每边18种bad-two-matching及实现矩阵；每种相邻纤维平面pencil均覆盖27点。该充分证书要求非相邻控制点对含对角有good NB3路。good路总数至多28n，闭三步反向成对要求至少n(n−3)条，故n≤31。想胜810只剩31→837；31时good计数矩阵必为J−A+I。此界不外推一般(12,3)图，三角的循环起点未假设保持rank。

保持原互不交三角factor会要求3整除n，无法越线，因此最后一项实际构造改为三角重叠：[controller31_triangle_extension](controller31_triangle_extension/REPORT.md)。从不同三角和C5的两个源点作短接、添加共享三角并把新点插回指定两个C4，完整枚举345×8=2760个不同标号四正则图。2280个实际含11三角，480个含12三角，均未漏检。

全部候选都缺少raw NB3必要覆盖，passers=0，故没有浪费资源解后续18模式CSP。最好图的[root唯一独立核查](controller31_triangle_extension/best.independent_check.json)为31点62边、四正则、普通D4/15个>3无序对，必需NB3有序缺项34。有限枚举耗0.886CPU秒；没有837点提升，没有追加family或恢复旧32/33 profiles。

一般31点控制器及其全局边模式证书仍开放；它是一个明确的剩余构造问题。当前各批均已终态，Goal保持ACTIVE，新下界仍0。

# P3实际检验：固定W、retained4完整池没有811整数packing的MIP解

**唯一一次MIP返回INFEASIBLE，不是超时。** SciPy status2／HiGHS status8明确报告model infeasible，没有incumbent。只关闭retained=[31,59,60,72]、固定W={(a,b,4a)}、全部19可用controller层的这个有限模型，证据尺度为数值MIP；没有独立UNSAT树或Lean证明，不能外推其他W、phase、retained或整个F9族。

原pilot含import、全部真实pin生成、建模、solver及汇总共3.733016668 CPU秒；solver3.333370611秒。Root随后要求的一次模型代入sanity另用0.056869364秒，两个测量批次合计3.789886032秒／60秒。无第二次solver、续timer、改seed或新大图。

## 1. 实际模型没有缩成容量正support

固定四层各81个center，共324。其真实完整N54合17496个不同pins，恰覆盖24个controller targetfibers。其余完整admissible层为

    16,17,30,32,35,42,43,44,45,58,61,64,71,73,74。

64、71虽不在旧837正support，仍各有81个变量。总候选1539点，其中1215个selection变量。所有坐标使用同一个W，无eta、phase或retained变化。

每center实际54pins由已接受PARAMETERS中的controller、八个literal matrices、真实inverse dart indices及GF9乘法表生成：每个port取M*x+t*ell_inverseport，t遍历9域元素。没有读56862边表，没有重验field laws／旧全部rank，也没有假设fiber translation自动同构。全部候选坐标与54pin列表已保存。

每个实际oldpin一条load≤1约束，共37908条；cardinality要求剩余变量至少487，即总数至少811。固定pins的占用并入同一load规则。于是约束是逐pin兼容，而非只按729fiber总容量。完整W平面与每个port像均真实生成，没有把部分counts当作center构造。

目标48的17／35／74三入射噪声方向实际小det为6。已有独立三方向证明给min(w17,w35,w74)≤20。本次只加入这个已证逻辑cut：w_u≤20+61z_u、Σz≤2，三个z为binary。它适用于任意一个family为零的情况，未错误地强加“三非空总数≤73”到零family情形。

总1218变量（1215point＋3switch）、37913行、67074个nonzero。objective为0的feasibility，只调用一次scipy.milp，threads1、time_limit44wall秒，并保留solver45CPU与total60CPU余量。零objective的dual不是最大center数上界。

## 2. 必要负对照通过，模型确实包含原810

在当前生成的candidate pin数据中代入原U10：

    31,32,44,45,59,60,61,72,73,74，各81点。

共810center／43740distinct pins，maxload1；变量部分486，固定部分324。逻辑counts(w17,w35,w74)=(0,0,81)，取z=(0,0,1)，三cut左端为(0,0,20)，Σz=1，全部合法。

它只违反新cardinality一条：486<487。没有误删原810、错误的逻辑cut、pool漏层或pinload冲突。这个检查只代入当前小输入，没有读旧source边表或跑旧BFS。

因此结合已有810与“≥811不可行”，可在**该有限模型的solver证据尺度**记optimum810。不是把raw solver的dual当810；raw node_count／dual／gap都是null，未提供rootLP或search trace，不能宣称已取得某种presolve证明或可核验整数不可行证书。

## 3. 837在哪里丢失可实现性：分数点仍可行，完整线必须是整数

同一次sanity还直接代入既有837容量向量，不调用LP：每个81点层均匀赋值w_u/81，即point variables取1／3或2／3；64、71为0，固定四层为1。把所有数乘3，用整数累加检查实际pin行。

这个向量总数837、变量部分513，所有逐pin load仍≤1。把三个辅助switch也放松为1／3，三logic行依然满足，cardinality也满足。因此**当前模型原始连续松弛确有837可行点**，不是单纯把实际pin约束加上便令连续问题不可行。

在target48，729个pin各得到17／35／74三个family的1／3贡献，恰load1。线性counts或fractional点看不出问题；选择整数center时，每个center必须贡献一条完整9点线，三个独立方向的27／27／27条完整线无法互不相交。已有几何证明的product≤8000和min≤20排除了这个特定837整数权重。

本次全池MIP进一步允许所有其他权重（以及64、71），仍报告没有≥811整数选择。这是全部共享target约束下的有限整数兼容性失败。Raw return没有冲突子集或branch证书，不能把全811结论偷换成“单target48一条cut已解析证明810最优”；它只明确解释了旧837为何不能直接构造，并区分分数容量与整数完整线互补。

## 4. 结果及下一步边界

P3未获支持：本retained4／固定W池的≥811模型被一次数值MIP判不可行。没有返回实际packing incumbent，故没有SELECTED_CENTERS或新完整图；不会把容量837、旧整数counts811或原810包装为新结果。

MODEL.json保存完整scope，ALL_CANDIDATE_CENTERS.tsv与ALL_CANDIDATE_PIN_ROWS.tsv给出1539候选的真实坐标／邻域。SOLVER_RETURN.json保留原返回对象，MODEL_SANITY.json保留原810负对照及精确837分数代入，RESULT／TERMINAL记录实际终态。

继续同一池加时间或只改counts没有依据：此轮不是UNKNOWN timer，而是已返回infeasible。也不能据此关闭不固定W的center集合、其他retained选择或任意F9构造。下一项若开展，必须先指出如何改变这些完整线在共享target的交错结构，而不是盲扩到729点全池。本任务不选择新eta／phase／seed，不派新solver或graph／Lean批次。

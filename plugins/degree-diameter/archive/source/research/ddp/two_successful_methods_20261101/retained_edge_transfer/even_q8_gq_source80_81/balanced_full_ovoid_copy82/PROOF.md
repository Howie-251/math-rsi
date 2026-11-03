# 唯一degree82生产规则、实际接口及fresh验收边界

生产实际终态PASS，完整物理图为graph_d82_D3_n346515.edges，首行346515 14204970，之后每条a<b且按(a,b)严格字典序输出一次。全部生产CPU含准备/编译2.146262777秒，小于30CPU；单worker。producer没有接受图，没有运行BFS、Lean、field/geometry/projection重验；root计数不变。

## 固定物理标签及实际fullN81

原source是已独验balanced填补图../balanced/graph_d81_D3_n342290.edges（342290/13862745、全81regular）。OVOID65.tsv按原i行顺序取o_i，SPREAD65.tsv按原spread行顺序取原isotropic line ID S_j；不重新sort这两个对象。parent TABLES_INPUT.txt的linePoints和pointLines物理ID原样继承。centers c_ij=o_i*585+S_j，index65*i+j，新label342290+index。

预期N81为linePoints[S_j]×pointLines[o_i]的原label Cartesian product，删c_ij自身；若j=owner(o_i)，加入原source fill342225+j。这里fill已经是旧source的一部分。全部实际spreader owners保存在PARAMETERS.json；不是将diag简单理解为i=j。

程序仅parse原source一次。每条源边被保留并流式与预先排序的342225条new-old边合并；同一pass从每条源边的两个端点抽取所有4225个中心的actualN。逐中心排序后，actualN与事前生成expectedN81完整相等。ORDERED_EXPECTED_N81.tsv和ORDERED_ACTUAL_N81.tsv各342225个有序pin行，CENTERS.tsv给4225个原中心/新label/diag绑定。

完整接口实际得到：所有N81两两不交，union有342225个点，恰为source\D65；65个D是对应owner的diagonal旧中心。旧负载0有65点，负载1有342225点。不是只按729或总容量推测不交。实际centers诱导2080条matching边和65个孤点，CENTER_MATCHING.tsv保存全部matching；中心并非独立集。

## 全部边、度数和prefix

源13862745条边全保留；仅增加4225×81=342225条old-new边，没有clone-clone边。终图点数346515、边数14204970。旧source各81度，342225个负载1旧点变82度，其余65个旧D保持81；新4225个clone也均81。因此degree81共4290、degree82共342225。

PREFIX_DEGREES.csv有k=0..4225共4226行，每行：n342290+k，m13862745+81k，oldload1=81k，oldload0=342290−81k，degree82数81k，degree81数342290−80k。这个prefix保证来自实际不交的immutable source N，不使用currentN，也不从最大图删点倒推直径。

## 完整D3与prefix为何由旧内部路线保持

令source为H，新clone x_c只接旧N_H(c)。所有旧点对继续使用已接受H的真实Walk，不受新增点影响。

对x_c与旧点v：若v=c，任取旧邻点给x_c–a–c；否则取H中c到v的长度≤3简单路径，将第一个c替换为x_c，得到同长路径。所有内部点均是旧source，包括原65填补点。

对两个不同clones x_c、x_d：H中c到d若距离1，使用x_c–d–c–x_d；若距离2，使用共同旧邻点；若距离3，将旧路径两端替换为两个clone。中间点始终为旧source。实际N不交使距离2中心分支为空，但无须假定中心独立；matching分支显式保留。由此每个实际prefix都独立有D≤3，不是根据最大终图的BFS删点推断。n远大于degree82的radius2上界6725，故在所述绑定和旧D3前提下恰D3。

以上是规则的数学覆盖解释，生产端并未用它代替fresh字面验收；仍交独立代理检查完整新边绑定及所有4225新根BFS。

## root事前预测与实际未做的检验

PREDICTED_NEWROOT_HISTOGRAMS.tsv逐4225根保存root在生产前给出的两类预测：

- 65个diagonal新根：(1,81,5249,341184)。
- 4160个off-diagonal新根：(1,81,5329,341104)。

源R2公式分别73²−81=5248、73²−1=5328；newroot R2再含旧中心自身1。其他clone没有二步路线，因为完整N81两两不交。这里没有实际sourceR2或newroot BFS；TSV全部明确PREDICTION_ONLY_NOT_BFS，必须由fresh普通BFS比较，而不是再代入一次式子。

## 竞争性及停止范围

本次degree82公开门best-located346450，候选只多65。exactfilledsource优先权UNKNOWN/JGT缺口继承；若同filledsource及接口已公开，优势归0，不称世界纪录。没有使用Payne源、没有生成经典source复现、没有83+端点或samecap饱和后helper batch。

RESULT.json和TERMINAL.json包含真实compile/producer/wrapper CPU及exit状态。生产现已停止，后续数学独立接受/具体Lean/外审/加计由root另行负责。parent source81文件及正在运行的q8源Lean队列未修改或重编。

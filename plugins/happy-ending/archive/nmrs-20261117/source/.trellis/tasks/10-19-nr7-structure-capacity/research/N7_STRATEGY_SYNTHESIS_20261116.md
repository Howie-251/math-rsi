# N(7,r,s) 的上界由哪些结构决定

截至2026年11月16日，757／766／767／777的工作上界是 **39／49／75／76**。决定后续下降的关键，是同一实际母体中长路的共同覆盖、取等结构及删后见证的存活，单独增加局部必要条件未必改变数值。[现用原件对照](N7_STRATEGY_PRIMARY_INDEX_20261116.md)

## 1. 对象、基线与真正产生过的下降

记 \(N(m,r,s)\) 为完整有序rank-3 signotope中，禁蓝 \(r\) 点路径、红 \(s\) 点路径和weak \(m\) 的最大避免点数。每个递增三元组完整染色；任意四点 \(a<b<c<d\) 的包 \((abc,abd,acd,bcd)\) 至多变色一次。路径长度计实际顶点；weak \(m\) 指同一对实际首末点的异色路径长度和达到 \(m+2\)。诱导删点继承禁形，路径及角色则须按实际残域重算。经典区 \(2\le r,s\le m\)、\(r+s\le m+3\) 中weak条件自动，容量为 \(\binom{r+s-4}{r-2}\)。[历史模型与R1—27](../../../../RESEARCH_REVIEW_R1_R27_20261026.md)

以下令 \(a,b,A,C,Q,F\) 依次表示747、756、757、766、767、777容量。

| 参数 | 747：a | 756：b | 757：A | 766：C | 767：Q | 777：F |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 构造下界 | 16 | 25 | 26 | 30 | 31 | 32 |
| 现用上界 | 16 | 25 | 39 | 49 | 75 | 76 |

\(a=16\)沿Baek的Theorem 2.7；\(b=25\)沿C1—10限定域人工接受，保留same-family／provisional说明。25点存在性另由E21完整染色和物理核验支持，不由接受记录自动提供。后四项仍是未获整链独审及正式接受的工作证明；\(F\le76\)经几何包含与强迫阈值加一，给工作推论 \(\mathrm{ES}(7)\le77\)。Schroeder作者预印本报告的几何81是另一来源、另一保证层级。[Baek v2 Theorem 2.7](https://arxiv.org/html/2206.04260v2)、[C8接受](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)、[E21核验](../../../../reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)、[构造与数值原件入口](N7_STRUCTURAL_SYNTHESIS_AND_PRIORITIES_20261115.md)、[Schroeder配套页](https://michaelschroeder.ai/research/ErdosSzekeres/companion)

历史链由45／58／103／206，经40／50／80／81走到现在。Q从80降到75，依靠同一中间匹配补偿和临界替锁；C降到49，依靠一般参数的实际路径交替环。新757的39来自owner区间、五行缺额和第一端冲突，不是旧蓝壳条件界。[Q75／F76证明](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)、[C49证明](../../../../reports/n766-strict-capacity-20261105/PROOF.md)、[A39证明§7.7](../../../../reports/n7-owner-intervals-20261116/PROOF.md)

这些上界分别回答所有允许输入最多有多少点，表中下界则只回答至少有一个多大的允许对象。两者未相等时不能说容量已经求出。抽象染色的完整见证也不自动提供平面坐标；几何调用必须另外保留合法根、投影解释和强迫阈值的连接。后续策略以实际对象和适用条件为准，不以文件标题中的数字决定结论。[原件保证与见证边界](N7_STRATEGY_PRIMARY_INDEX_20261116.md)

## 2. 五种可复用的方法

**状态与真切片。** 真实末对路长生成下理想并注入；756有35态，其中25普通、10异常，\(|X|=25+e-\mathrm{miss}\)。其用途是把人口转为共同缺额，不能把目录占态当成实际染色。普适坐标删除令 \(u=r-2,v=s-2,M=u+v\)、\(U_m(u,v)=N(m,u+2,v+2)\)，给

\[
U_m(u,v)\le\min\left\{
\left\lfloor\frac{M}{v}U_m(u,v-1)\right\rfloor,
\left\lfloor\frac{M}{u}U_m(u-1,v)\right\rfloor\right\}.
\]

每个切片都是真实点集。757四十点使 \(5\cdot40=8\cdot25\) 全取等，迫 \(D=E\)，再由owner代表红团得 \(L+R+c\le6\)，五行缺额和第一端终于矛盾。39点有余量，不能照搬。第一活跃族 \(m=u+v\) 的平移行还以真实同端异色路迫洞，再作支撑不交的洞打包；它必须保存同一pair标签。[坐标删除](../../../../reports/n78-row-compression-20261115/PROOF.md)、[共同切片](../../../../reports/n7-joint-slices-threshold-20261115/PROOF.md)、[平移同端支撑](../../../../reports/n79-overlap-20261116/TRANSLATED-PATHS.md)

这类方法最强的场景是总人口逼迫大量切片同时取等。此时缺席、角的承载和前后路径都受同一个输入约束，可以把纯计数转成真实结构；离取等较远时，各切片仍可分别消耗余量。任意挑选每片的一份最优见证，不会自动得到共同母体，换坐标后也必须保存原点与新标签的对应。[同步取等接口](../../../../reports/n7-joint-slices-threshold-20261115/PROOF.md)

**严格覆盖与安全增广。** 当 \(4\le r\le m\)，实际覆盖使递推节省一单位：
\[
N(m,r,m)\le N(m,r-1,m)+N(m,r,m-1)-1.
\]
balanced一般 \(p\ge4\) 则由真实替末、安全增广及完整端图交替环得 \(c_p\le2b_p-1\)。触发点是独立两域不能共同取满；局部能加一个点，仍须验证所有新暴露长路。[R5](RESET_R5_COVER_AUGMENTATION_CAPACITY.md)、[一般balanced严格容量](../../../../reports/n766-strict-capacity-20261105/PROOF.md)

一个成批删点实例是：在禁 \(B_{r+1},R_{r+2},\mathrm{weak}(r+2)\)、\(r\ge5\) 的母体，固定实际纯红 \((r+1)\) 末q与纯源p，q＜p；取 \(C_0\subseteq(q,p)\) 中既非该红路源也非末的点，且 \(C_0\cup\{q\}\)、\(C_0\cup\{p\}\) 均无 \(R_r\)。同一对端口图最长链按顶点数计为 \(\ell_-,\ell_+\)，则 \(|C_0|+\ell_-+\ell_+\le\beta\)、\(4\le\ell_-+\ell_+\le r\)，β是禁 \(R_r,B_{r+1},\mathrm{weak}(r+2)\) 的人口界。r＝5时可一次计4，有连续两边则计5，仍须在同一对上支付删点费。[端口共同增广§2](../../../../reports/n7-structural-roadmap-20261107/synthesis.md)

**共同M0、匹配与锁。** 两侧M0和中间图必须来自同一输入，同一个中匹配的费用只能计一次。实际owner与锁迫同端蓝四／红五，在临界取等处替锁封口，给 \(Q\le3b\)。分别找到三份有利匹配、或把倒二owner的末点直接认作其终锁，都不够。[共同匹配及替锁原件](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)、[owner勘误](N7_ROOT_DOMAINS_AT_29_20261113.md)

**合法chart运输。** 同一抽象母体的合法径向chart删根、换色及反向添根给 \(F=Q+1\)；R20 §0.2的全参数形式为 \(N_{\rm sig}(m,m,m)=N_{\rm sig}(m,m-1,m)+1\)，\(m\ge4\)。它适合把777与767精确联通，不能任意换序、独立重标内部态，或把不同chart的费用相加。[R20 §0.2](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

**物理横截与见证打包。** 任一 \(n\) 点767域满足 \(\tau_{R_6}\ge n-C\)；支付端二部图可经Kőnig化成物理横截。支付端互异不代表整路顶点不交。证书只能在输入提取和有限域覆盖完整后承担排除，固定CNF的checked UNSAT不能自行扩成全母体定理。[整数横截](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[H17有限投影](../../../../reports/n7-blue-through-seventeen-20261113/execution-20261116-restored-route/REPORT.md)

横截是同一批物理点命中全部目标路，打包则是整份支撑彼此不交。前者给删后容量，后者给必须同时存在的障碍；二者可互相约束，不能替换量词。特别是某条认证路径经过一个已付点后，它在残域可能已经消失；保留这条旧图边会虚增匹配，删去未实际命中的替代路又会虚减费用。[完整路径与删后重建](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)

## 3. 当前瓶颈为何不在单独压低一个小参数

现有接口合起来是
\[
Q\le\min\left\{3b,C+b+5,A+C-1,
\left\lfloor\frac{9A}{4}\right\rfloor,
\left\lfloor\frac{9C}{5}\right\rfloor\right\}
\le\min\{75,79,87,87,88\}=75.
\]
因此A38或C48单独不动Q；A33／32经坐标界给Q74／72，C44／43经旧残余界给Q74／73。75点767的九个含侧对A39总余量为 \(9\cdot39-4\cdot75=51\)，九个避侧对C49为 \(9\cdot49-5\cdot75=66\)，远离757四十点的零余量。总余量只是记账，不是新禁形。[现用综合接口](N7_STRUCTURAL_SYNTHESIS_AND_PRIORITIES_20261115.md)、[坐标删除原证](../../../../reports/n78-row-compression-20261115/PROOF.md)

小模型说明必须审方法的损失：16点收费6可降真实3；18点所有准许cut与三阈值最低仍6，真实横截却为4。r2十二点的完整非中性迹不可二染，删点1后只剩端边6—12；H17冻结投影SAT又只有4／17标点具实际局部双向B5，不能推全域贯穿结论。另一方面，一般 \(|S\cup E|\le2b=50\) 一次把75点窗收为 \(25\le d\le28\)。满20原cut帽的特定分配 \(h=0\)及镜像已由真实十核的 \(3\times2\) 截断逐点固定，迫早图至多三列，\(12+9+3=24\) 给条件人口≤73，无d28前提。这里h是饱和分配参数，不是蓝五贯穿人数。[匹配净收益](../../../../reports/n7-owner-intervals-20261116/MATCHING_GAIN.md)、[r2全部路径](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[D23一般人口](../../../../reports/n7-owner-intervals-20261116/D23.md)、[EARLY_HALL](../../../../reports/n7-owner-intervals-20261116/EARLY_HALL.md)、[H17实证](../../../../reports/n7-blue-through-seventeen-20261113/execution-20261116-restored-route/REPORT.md)

## 4. 首选：删后真实端图的净收益

以下是**本次从既有原件推得的条件判据，未外审**，不是新全局界。固定任意767域X，人口n，全红六首末点并U的大小为 \(m_0\)，\(d=n-m_0\)。选实际点集J，在 \(X\setminus J\) 用全部幸存红六重建端点并 \(U_J\) 和端图 \(G_J\)，同一物理点只有一个节点。若 \(G_J\) 二部，令其最大匹配为ν，定义
\[
i=|J\cap U|,\quad o=|J\setminus U|,\quad
e=m_0-i-|U_J|,\quad u_J=|U_J|-2\nu,
\qquad g=e+u_J-i-2o.
\]
e数未删而失去端点身份的点，\(u_J\)数最大匹配未覆盖点。Kőnig给一份真实横截，构造费用为
\[
|J|+\nu=\frac{m_0-g}{2},\qquad
n\le C+\frac{m_0-g}{2}.
\]
这是该构造的费用等式，不是 \(\tau_{R_6}\) 的等式。结合 \(m_0\le2b\)，若目标层每个输入都有构造性J使 \(g\ge g_0\)，则
\[
n\le C+b-\left\lceil\frac{g_0}{2}\right\rceil.
\]
\(g_0=0,1,3\)依次给74、73、72。也可保留实际欠饱和量：\(2b-m_0+g\ge2t-1\)即保证上述整数构造费≤b−t，因此欠饱和量可以补偿收益；单要求g为正只应用于候选临界层。更弱的逐层排除门槛为 \(g\ge2C+2-n-d\)；g与 \(m_0\) 同奇偶。74点由一般人口界仅知d≥24，d24／25／26分别需g≥2／1／0，不能照搬75点窗。[一般人口与鲁棒奇环](../../../../reports/n7-owner-intervals-20261116/D23.md)、[实际cut整数覆盖](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)

这个收益把三件事放在一张账上：删除旧端点有费用，支付中性点有费用，而未删除却不再承载任何幸存长路的旧端点贡献释放量。二部图匹配的未覆盖点再提供一份可加的收益。先用J截住被删除的路，再用端图顶点覆盖截住全部幸存路，才得到所写全域横截；任何中间路都不能跳过。若删后图仍有奇环，这份二部图判据暂不能调用，需要改选J或补足物理支付。[同域覆盖原件](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)

还有一项同会话可证的跨层预算推论：任一使 \(G_J\) 二部的J，均须满足
\[
i+2o\ge n+d-2C+e+u_J.
\]
75点、d＝28假设母体的右端至少5；任意删两个物理点，即使两点都是中性内点，也有 \(i+2o\le4\)，故全部幸存红六端图仍含奇环。直接核算是原U共47点，若删后图二部，较小色类至多23点，连两预删点总费至多25，违 \(\tau_{R_6}\ge26\)。这是允许支付中性点的鲁棒必要条件，不是d28已排除。[一般人口及旧端点鲁棒性](../../../../reports/n7-owner-intervals-20261116/D23.md)、[实际删后图](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)

r2取 \(m_0=6,J=\{1\},U_J=\{6,12\}\)，有 \(i=1,o=0,e=3,u_J=0,g=2\)，得到全截费用2。\(u_J\)可按不交二部连通分量相加，每分量左右人数差绝对值给下界。J应从可行cut原帽、同组路径退款或共同区间构造；若允许直接取未知最小横截，优化就退化为原问题。首项攻击是满20帽剩余h≥3与非饱和帽的二择一，允许释放旧点和支付中性点，但必须截齐全部复活单侧路和所有替代跨路。现有h＝0只是充分子类，普适低费cut仍待证。[r2核验](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[整族退款](../../../../reports/n7-owner-intervals-20261116/PAIR_REFUND.md)、[已闭h＝0](../../../../reports/n7-owner-intervals-20261116/EARLY_HALL.md)

可优先尝试一条统一定量估计。令Z为同一原cut至多20点帽，\(R\subseteq Z\)是放回旧点，\(P\subseteq X\setminus Z\)是新付点，取 \(J=(Z\setminus R)\cup P\)。先验证全部单侧路仍被J命中，再对全部删后跨路证明
\[
\nu(G_J)+|P|\le4+(20-|Z|)+|R|.
\]
则总费 \(|J|+\nu(G_J)\le24\)，一次覆盖74点反设；常数5对应25费。可尝试把超过四个基准名额的匹配／新增费用单射到该帽缺失的经典态或真实释放点。这是尚待证的定量目标：重排费用式不产生注入，放回点也不能同时算已付点。[同cut原帽](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[退款与复活路](../../../../reports/n7-owner-intervals-20261116/PAIR_REFUND.md)

这项目标的验收对象应是一整个剩余输入类：给出合法cut和真实帽的选择规则，说明每次退款后哪些路复活，并对这些路与原跨路统一建图。若某个强制配置需要额外付点，也须在同一费用式内支付。只对一份固定匹配选中点，仍可能漏掉具有相同外端的另一条绕行；小模型中的方法最优正是这种风险的诊断。[全部绕行与共同选点](../../../../reports/n7-owner-intervals-20261116/MATCHING_GAIN.md)

## 5. 其余三条路线的价值与代价

**长期的一般混合分划。** 在禁 \(B_{p+1},R_{p+2},\mathrm{weak}(p+2)\) 的任意输入中，找一份真实K截全部 \(R_{p+1}\)，且K无 \(B_p,R_{p+1}\)，补集balanced。记短帽、balanced、混合容量为 \(b_p,c_p,q_p\)；若两域联合未用容量可计为γ，则 \(q_p\le c_p+b_p-\gamma\)。p＝5时γ＝0、1、2给74、73、72。饱和截面 \(r(L)+r(R)=p+1\)、两侧均小于p＋1及递归常色二块已有条件覆盖，待覆盖的输入包括不可如此分解且有多个贯穿点的母体。这独立于前述物理横截：前项不要求横截本身成为短帽。[混合分划原稿](../../../../reports/n7-mixed-partition-bridge-20261106/PROOF.md)

**同步切片的近极值稳定性。** 39点757每套八坐标中，度14、15、16的坐标数恰为 \((3,5,0),(4,3,1),(5,1,2)\)，至少三满25避片、\(\tau_{R_6}=14\)、面积缺缝≤27；49点766缺缝≤16，至少33点D＝E，并有交替Hamilton端链。目标是把总缺格、owner缺口和多条实际链的代价写成参数不等式，不能继续排已闭40点。A38／C48仍有独立价值，但不立即向Q传播。[39点真实接口](../../../../reports/n79-overlap-20261116/SEVEN-39-SOURCE.md)、[49点共同切片](../../../../reports/n7-joint-slices-threshold-20261115/PROOF.md)

**按机制探索split打包。** 当 \(\max(r,s)\le m\le r+s-2\)，Baek–Balko的split-free最大避免人口为L，强迫阈值是L＋1，其中
\[
L=\sum_{j=m-r+2}^{s}\binom{m-2}{j-2}.
\]
最大不交完整共右端split支持的并截住全部split，每份至多m＋1点，故 \(|X|\le L+(m+1)\nu_{\rm split}\)。767中L＝31，72或74点都至少六份；若六份不可能，则Q≤71、F≤72、几何工作阈值≤73，尚未证明。六支撑区间中有三分离或三跨同缝，可尝试同步混合三元组迫同端weak；也可同域保留四条硬胞不交红六加三份split。两种选法不能相加，六份存在不等于已有矛盾。[Baek–Balko全文Theorem 6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13.html)、[split归约与共同选法§5](N7_STRUCTURAL_SYNTHESIS_AND_PRIORITIES_20261115.md)

74点已有工作仍应接回上述共同结构：小d要在同一balanced域保存14条完整双臂；H17要核全母体扩张。四路单首单末中无完整锚支已闭，单侧有锚与至少五路仍开，不宜把重复拆小病例另列主线。[E1整支闭合](N7_74_E1_COMMON_FIVE_FACE_20261116.md)、[单侧锚后继](N7_74_ONE_SIDED_ANCHOR_AND_POPULATION_20261116.md)、[四路范围](N7_74_FOUR_MAXIMUM_RED_PATHS_20261115.md)

因此几条路线应按不同的失效机制分工：物理横截争取直接控制整数费用，混合分划要求更强的短帽身份，稳定性利用临界人口的同步取等，split则寻找另一种完整支撑障碍。某个必要投影的SAT只否定该简化排除，某个局部构型的矛盾也只关闭其覆盖域。值得继续的增量，应能统一支付一批旧缺口，或提供明确反例阻止同域反复加强。[同日范围对照](N7_STRATEGY_PRIMARY_INDEX_20261116.md)

本次工作限策略审核、上述归约、公开来源核读及本地证据整理。25层沿限定域人工接受进口，后四项工作界仍未外审、未获整链正式接受。外部Claude深审的启动因自动审批拒绝向该服务发送这批私有原件，未取得独立意见；无新solver、证书重放或正式接受。完整对象、勘误、有限反例及同日来源边界见[原件索引](N7_STRATEGY_PRIMARY_INDEX_20261116.md)。

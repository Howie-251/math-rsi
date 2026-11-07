# N7：空锁定分支的全残余普适性与实际分块的费用边界

日期：2026-10-28。结论：**本轮没有找到新的全局容量损失机制，没有新的全局上界。** 实质交付是一个覆盖全部 D_n 的严格方法障碍：两方向空锁定、全部红长链终点缺少蓝长链覆盖、以及最新延伸定理对每个混合源全部终点均适用，这些条件可以在同一个实际母配置中同时成立，且不排除任何合法残余。另给出非真空的完整参数家族。它们说明下一次收费必须真正使用较大核心的共同实现性，不能继续仅细化残余端点标签。

全蓝根嵌入本身是R7旧结果，不重新认领；本轮提取的是它在最新锁定/可达性语言下的全类障碍。新增推导全部 **unreviewed / unaccepted**。同族数学生成协作、Sol实现核查和文档检查都不替代独立审阅。当前长期任务保持in_progress、completedAt=null；旧证明、CNF、反例、失败回执与接受记录不改。

## 1. 原始材料、两条主线比较及本轮选择

已读取AGENTS.md、Trellis workflow、ARIS README及执行分工，继续用户指定任务。先读最新端点延伸报告、R26 §§2–4、R27 §§2–4、全缺额Joint报告、D12完整反例报告，再回读R7 §§3.3、5.2，D7全局临界端点报告§§2–4，R22 §5.1和D12原始颜色/语义回执。现有research目录的最新相关稿仍为2026-10-27端点延伸报告；未发现可据以登记C≤49或C≤47的新完整证据链。

主要依赖：

- [N7_ENDPOINT_PRESERVING_EXTENSION_AND_R26_JOINT_BUDGET_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PRESERVING_EXTENSION_AND_R26_JOINT_BUDGET_20261027.md>)：定理E的完整路径域与全终点覆盖判据。
- [RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>)：同一实际K的内禀锁定收费与canonical共同预算。
- [RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md>)：完整修复后的交换精确返回旧核。
- [N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)：Joint17全类迁移、全缺额角色关系及Closure边界。
- [N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>)：完整D12及全部18条红六。
- [RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)：旧全类canonical嵌入与端点闭包。
- [D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>)：完整D7内全部红六末点及其后缀性质。
- [RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>)：§5.1早已否定普遍实际端点图二分。

| 比较 | A：空/少锁定的障碍必现或实际分解 | B：766共同近极值实现性 |
|---|---|---|
| 完整入口 | R26从任意767的全部红六源进入实际K、D；canonical预算覆盖所有缺额 | 任意766的全部五链源末角色、Joint和内部重算核心 |
| 可用中间机制 | 已有锁定收费、全终点延伸；未知的是障碍必现或覆盖失败后的有效操作 | 一步扇规则已有完整审计；未知的是不同中点供应被迫在同一packet冲突 |
| 真正损失出口 | 实际A1给C+b+z；锁定按同一K计费 | 完整C≤2b−Δ后沿旧链传播 |
| 已知停止依据 | R27纯人口交换精确抵消；R22端点图二分失败；D12否定红六两两相交 | 现有人口标量共同可行，不能仅改写through数量 |

本轮选择A，先检验“覆盖缺口本身是否缩小全类入口”，随后检查端点投影是否可承担实际分块费用。结果是第4节的全类障碍；没有把它修补为某个特殊满核模板。B保留为竞争方向，未把新的一步或跨中点必要条件登记为容量进展。

## 2. 模型、最强旧工具和八项前置审计

N_sig是最大避免规模。四点packet按abc、abd、acd、bcd排列，至多一次变色；路径长度按点数。单色路径的所有子序列仍同色，故两色同端最大长度之和在no weak n配置中至多n+1。全部路径、源、末点与邻点集合均在注明的同一实际配置中计算，诱导子配置内部身份重新计算。

令Q_n类无B_(n−1)、无R_n、无weak n；D_n类无B_(n−2)、无weak n，且内部End_R(n−2)∩Src_B(n−3)=∅。D_n自动无R_n，因为R_n与同端两点蓝路径构成weak n。一般参数论证使用n≥6；第5节显式家族使用n≥7。

对n=7继续保留a、b、C、Q。R26在同一canonical H⊔R中已证明

\[
|A|+|U|+|W|+|E_A|\le d_H=2b-|H|,
\]

其中A⊆F_+∩R，U、W按原文，E_A=o(A)∩(S_R\setminus W)。取A空得到|U|+|W|≤d_H。它来自同一次实际K和不同出口的最早neutral代表，绝非R20两条独立估计相加；不与反向预算或内禀锁定费用重复相加。

深入前的八项审计：

1. 本轮命题覆盖每一个D_n，并通过已证明的全蓝右根操作进入真实Q_n；没有固定一个横截、尾或模板代替全类。
2. 红长链、蓝长链及canonical分解都来自同一实际X；新增点只有明确规定颜色的一个右根。
3. 本轮没有新增严格容量损失。要检验的机制是假设“所有缺口共同存在会自动缩小残余类”；第4节严格证明它不成立。
4. 全部路径超图被原样保留，全部蓝长路径统一定位到新根，因此共享、替代与多路径不会逃出证明；也没有按它们的次数收费。
5. 正收益仍须经第3节组合式或第7节A1/A2公式兑现；本轮未满足新正收益前提。
6. 第4节是显式全类嵌入的附加结论，与目标数值无关，不是缺额式改名。第3节则明确只是旧构造的代数组合，不算突破。
7. 已知R22、D12反例已否定端点二分/两两相交等关键假设，本轮不重新立这些猜想。小H例不能否定近满H的联合命题。
8. 失败后停止的是“仅靠空锁定及缺口标签缩小残余类”这一整类机制；并未停止所有可能的全路径分块或真正的大核心联合机制。

## 3. 核对R26与C改善的正确组合

对任意实际X∈Q_7，R26使用全部锁定源F及出口O=o(F)。记f=|F|、o=|O|；其实际集合满足

\[
K\in766,\quad D\in D_7,\quad K\cap D=F,\quad K\cup D=X\setminus O,
\]
\[
|K|+o\le2b,\qquad |D|\le b+5.
\]

所有共享出口只在O内计一次，全部owner保留在真实交集F内。因此精确地

\[
|X|=|K|+|D|+o-f.
\]

分别应用|K|≤2b−o和|K|≤C，得到

\[
\boxed{|X|\le\min\{3b+5-f,\ C+b+5-(f-o)\}.}\tag{1}
\]

这是对每个完整X、所有缺额及所有共享出口都成立的旧构造组合。若另有独立完整证明C≤2b−Δ，则

\[
\boxed{|X|\le3b+5-\max\{f,\ \Delta+f-o\}.}\tag{2}
\]

映射F→O满射，所以f≥o。只有实际交集盈余f−o能与C改善按第二项结合；不能把全部f与Δ直接相加。f=o时第二项只给Δ；F空时o=0，公式退回旧C+b+5。正反两份公式各自成立，但只能取所得上界的较小值，不能相加费用。

一般n≥6，设b_n为相应不对称类有效界，c_n为平衡类有效界，d_n为D_n有效界，同一证明给

\[
|X|\le d_n+\min\{2b_n-f,\ c_n+o-f\}.
\]

五点横截只在n=7使用；未向其他n代入b_n+5。组合式没有证明f、f−o或Δ必为正。

## 4. 全类障碍：空锁定和所有覆盖缺口仍容纳全部残余

**命题U。** 对每个n≥6及每个非空实际R∈D_n，存在完整X∈Q_n，其canonical残余恰为R，核心H只有一个点h，且同时满足：

(a) F_+(X)=F_-(X)=∅；

(b) X中的全部B_(n−2)都终于h，全部R_(n−1)都在R内；

(c) 全部R_(n−1)终点与全部B_(n−2)第二点两集合不交；

(d) 每个红长链终点都没有任何B_(n−2)入链，特别没有来自任一混合源之前的这种蓝覆盖；

(e) 对每个混合源s，T_s∩Q_s=∅，故T_s^≠=T_s，最新定理E适用于它的全部红终点。

这里T_s、Q_s是全部实际路径定义的集合，不是选定见证。命题的旧部分是R7全类嵌入；本轮提取并证明的是(a)–(e)对该整个嵌入类同时成立。

**证明，完整模型和canonical身份。** 在R右侧添加h，所有含h的三元组染蓝，旧三元组不改。新packet为(χ(a,b,c),B,B,B)，旧packet不变。若B_(n−1)含h，删除h后成为R内被禁的B_(n−2)；不含h时也不可能。含h的红链至多二点，不含h的R_n由R中no weak n排除。旧实际端点的路径不会使用较大的h；新端点对(x,h)上的红长至多二、蓝长至多n−2，长度和至多n，故无新weak n。

对a<b<h，蓝三元组强制bh≺ah≺ab。因而每个旧r的最小关联对是rh，p(r)=h；p(h)=maxR。于是P_+=R、P_-={h}。在完整诱导R内部重新计算的junction集合G为空，所以canonical H={h}、残余R原样。单点R时直接核对唯一关联对。这里没有选择或优化λ；每项最小性已被三元组强制。

**证明，终点闭包。** 任取R内实际R_(n−1)终于t，末前驱u。若t启动B_(n−4)=(t,q,...)，则χ(u,t,q)为红会把入红链延长为R_n；为蓝则u启动B_(n−3)，同时u已是R_(n−2)末点，违反D_n条件。故任何这样的t都不能启动B_(n−4)。n=6时该蓝链是二点，q仍存在，两种joining分支仍成立。n=7的“红六终点无蓝三后供”是R7旧闭包，不重计原创。

**证明，全部路径集合同时分离。** 因R内无B_(n−2)，X中每条该长度蓝链都含h并终于h。红(n−1)链不可能含h。若q是任一B_(n−2)的第二点，删掉这条链的首点与h，剩下R中从q出发的B_(n−4)。由上一段，q不是任何R_(n−1)终点。这是全局两集合不交，而非只对同一源的一次选择不等。

从而每个混合源的两个非空集合T_s、Q_s不交，不能锁定，且每个t∈T_s均有q∈Q_s不同于t，所以T_s^≠=T_s。所有蓝(n−2)终点只可能为h，而红(n−1)终点不含h，故没有混合终点，F_-也为空。每个红终点没有任何该长度蓝入链，(a)–(e)全得证。

证明允许任意共享尾、任意替代路径及所有前驱。没有假定不同混合源的尾独立，也没有用父配置的内部秩代替子配置秩。

**严格的方法结论。** 把满足(a)–(e)的这种母配置投影到canonical残余，所得类恰为全部D_n。特别地，n=7时红六超图逐边不变；τ_X=τ_R，α_X=α_R+1，新根只是这个超图的孤立点。

因此，仅使用“canonical、两方向空锁定、全部红终点不可蓝覆盖、E对全部终点有效”作为筛选条件，不会排除任何D_n残余。若要从这些条件单独证明某个残余性质Φ(R)，仍须对每个D_n证明Φ；不能把这些标签称为已经进入一个更小的残余类。

这不证明D7无法改善，不反驳A1/A2，也不反驳大H和近满安全核心的联合定理。这里H只有一点；真正的大核心假设必须提供新共同颜色约束，不能从本命题中删掉这一限制后反向声称近极值配置存在。

## 5. 非真空完整家族：混合源存在且所有替代都留下缺口

为避免第4节只被理解为“没有混合源所以真空成立”，给出一个不依赖SAT的显式家族。它仅作机制校准，不是近极值构造，也不认领新的下界纪录。

设n≥7。按序取A={a1<...<a_(n−1)}，随后取B={b1<...<b_(n−5)}。完整颜色为：AAA红，BBB蓝，AAB蓝；ABB的颜色r_i在A点为a_i时取蓝，唯一例外r_(n−1)=红。

**全部packet。** 4A全红，4B全蓝；3A1B为RBBB；2A2B为(B,B,r_i,r_j)，i<j迫r_i=B，故为BBB r_j；1A3B为(r_i,r_i,r_i,B)。均至多一次变色，不存在未处理的交织型，因为A、B连续排列。某块不足相应点数时该类型为空。

**全部单色路径。** 蓝链至多两个A；若还使用至少两个B，则第二个A不能是a_(n−1)，否则边界AAB蓝、ABB红。故蓝最大长n−3，全部达到者恰为：从{a1,...,a_(n−2)}选两个点，然后接全部B。若只用一个B，蓝长至多三，小于n−3；零或一个A的情形也更短。

跨块红链不能用两个A。若唯一A不是末A，红链至多二；若是末A，红链至多三，因为BBB蓝。于是全部红(n−2)、红(n−1)都在A内，后者唯一为A本身。

逐实际端点验证weak：A/A两色和至多(n−1)+2=n+1；B/B至多(n−5)+2；非末A到B的红长至多二、蓝长至多n−3；末A到B的红长至多三、蓝长至多二。因此全部同端长度和均≤n+1。

准确角色为

\[
\operatorname{End}_{R_{n-2}}(D)=\{a_{n-2},a_{n-1}\},\qquad
\operatorname{Src}_{B_{n-3}}(D)=\{a_1,\ldots,a_{n-3}\}.
\]

二者不交，故这是完整D_n。再按第4节加全蓝h，得到Q_n。其唯一混合源是a1，而且

\[
\mathcal T_{a_1}=\{a_{n-1}\},\qquad
\mathcal Q_{a_1}=\{a_2,\ldots,a_{n-2}\}.
\]

所有这些蓝第二点均有真实长蓝路径实现；所有红终点均无所需蓝覆盖；两方向锁定均空。这里混合源是最早点，E的前驱不等式在该源处真空，不将此例冒充已有丰富前供或近满H的反例。它严格反驳的是“只要有混合源，所有端点缺口便不能共同存在”的无条件假设。

## 6. 实际分块与端点投影：完整判据及旧障碍的准确校准

本节不把定义展开认作结构创新；它明确哪些操作才真正构造了A1。对任意实际767 X，令S=Src_R6(X)、H0=X\S。取任意删集Z和A⊆S\Z，定义

\[
K=(H_0\setminus Z)\cup A,\qquad Y=S\setminus(A\cup Z).
\]

S内部无蓝五：若有，末点启动ambient红六，joining红迫红七、蓝迫蓝六。故Y自动无蓝五；其余蓝帽和weak均遗传。

对每条避开Z的实际红六P，令T_P=V(P)∩S，非空，因为首点属于S。于是K属于766、Y属于756，**当且仅当**同时满足：

- 若P经过H0，则T_P至少有一个点进入Y；
- 若P完全在S，则P同时含一个A点与一个Y点。

证明：第一支的P本就不可能全部在Y，而全部在K恰等价于T_P⊆A；第二支要同时排除P⊆K和P⊆Y，恰须两块都有点。遍历全部实际P即为必要且充分；经过多个新增A点、共享内点或被内部Z点击中的路径均包含在判据中。不要求每条ambient红六的两个端点异块。此判据自身没有构造低成本A、Z，故不是新上界。

**历史纠正与停止范围。** R22 §5.1已用完整九点R5端点三角反例停止普遍实际端点图二分；不能将本轮再次发现三角形当新通用障碍。D12只提供与当前R6及空锁定问题直接对齐的费用校准。

旧D12全部18条红六的端点边恰为0→6、0→11、2→11、6→11；源集S={0,2,6}。完整颜色及全路径验证见D12原始报告§4与原回执。底层三角形0–6–11–0说明任何“所有存活红六两端异块”的二分操作在Z空时不可能；删除6，取Y={0,2}、其余为K则达到一删点。因此这种端点约束的最优删除费为一。

但真正A1取Z=A=空，Y=S、K=D12\S即可：Y只有三点，无相应禁形；K已删除全部ambient红六源，故无内部红六，其他禁形遗传。其实际最优删除费为零。两方向锁定也空，因为D12无蓝五。

这给精确校准z_endpoint=1>z_actual=0。端点奇圈成本不是实际分块必付成本；同块端点不意味着路径全部内点同块。它不否定完整路径交换，不否定带近满核心条件的命题，也不重计旧D12构造或旧R22的通用失败结论。

## 7. 一般参数的传播出口与本轮未闭合处

若所有目标X都实际进入A1：X=K⊔Y⊔Z，K∈766、Y∈756、|Z|≤z，则

\[
Q\le C+b+z,\qquad N_{\rm sig}(7,7,7)\le C+b+z+1.
\]

若C≤2b−Δ独立成立，则Q≤3b+z−Δ。若实际进入A2的三块分解，则只能直接得Q≤3b+z，不能再叠加C的改善。

若完整全类二分成立：每个X或者有至少k个实际锁定源，或者进入A1的z删点分解，则

\[
Q\le\max\{3b+5-k,\ C+b+z\}.
\]

这仍是条件性传播，不是本轮已经证明的二分。第4节不能担当“缺口分支已经低容量”的证明；第6节不能以端点图修复代替构造A、Z。

本轮仍缺的关键步骤只有容量层面的这一项：证明近极值母配置中的实际大核心供应，不能和全部缺口共同实现；或从其共同实现中构造满足第6节全部路径判据的A、Z并给统一较小成本。R27修复回旧核、单纯through人口及根本没有缩小残余类的标签都不提供这一步。

## 8. 有限核查、证据等级与最后数值

主会话完成上述一般证明后，才安排固定家族n=7、8的单次确定性核查：全部颜色、全部四包、全部顶点子集路径、逐实际端点两色最大长度、junction、全部T/Q及canonical身份。预算和输入在执行前固定；这不是目标数值SAT，也不是一般证明的替代。

实际执行为**无SAT/UNSAT求解、无证书重放；一次完整小例语义核查**。执行模型请求为native gpt-6.1-sol/high；未独立报告的backend模型和实际effort仍不可验证。首次本地SSH预检在建立连接前被沙箱网络权限阻断（WinError10013），[失败回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/preflight_blocked.json>)保留；主会话随后明确授权同一路径提权预检，它在首次远端科学派发前确认Linux主机ubun与新目录不存在，见[预检回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/server_preflight.json>)。科学运行只有一次，没有科学重试、续跑或预算追加。

规则及输入在实现和运行前保存为[MATHEMATICAL_SPEC.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/MATHEMATICAL_SPEC.md>)和[INPUT_MANIFEST.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/INPUT_MANIFEST.json>)，源码与输入绑定见[prelaunch_binding.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/prelaunch_binding.json>)。权威Linux目录为/data/ktqiu_hdd/math_agent/tmp/n7_global_operation_20261028；实际命令、stdout、stderr、退出码完整保存在[scientific_execution.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/scientific_execution.json>)。命令使用timeout的120秒外部墙钟限制、TERM后2秒KILL，进程内CPU115秒和地址空间1GiB限制。远端退出码0、stderr为空；内部核查用时0.047354789974633604秒，峰值RSS16384KiB。

| 固定参数 | D/X点数 | D/X颜色数 | D/X四包数 | D/X已核对顶点子集数 | 最大同端两色长度和 | X红(n−1)/蓝(n−2)路径数 |
|---|---|---|---|---|---|---|
| n=7 | 8/9 | 56/84 | 70/126 | 247/502 | 8/8 | 1/10 |
| n=8 | 10/11 | 120/165 | 210/330 | 1013/2036 | 9/9 | 1/15 |

每个至少二点的顶点子集均独立比较“连续三元组同色”与“全部三元组同色”，结果一致；每对实际端点的两色最大长度逐一保存。D的唯一红(n−1)、全部红(n−2)末点、全部蓝(n−3)源与空junction均符合第5节预测；X的唯一混合源、完整T/Q、F_+=F_-=∅及全部长链末点也符合。canonical依据全部实际三元组构造统一点对偏序和确定性线性扩张，再用可达性核对最小关联对先于每个替代关联对；两参数均得p(r)=h、p(h)=最后B点、G空、H={h}、残余为原D，没有λ优化。负对照中，指定两条AAA翻蓝产生BRBR并被packet规则拒绝；全红X通过packet规则而被红n长链上限拒绝。

全部颜色、四包、完整单色路径及逐端点最大值见[n7_D_paths.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/n7_D_paths.json>)、[n7_X_paths.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/n7_X_paths.json>)、[n8_D_paths.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/n8_D_paths.json>)、[n8_X_paths.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/n8_X_paths.json>)及同目录相应colors、packets、canonical、negative_controls文件。完整总回执[result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/result.json>)状态为FINITE_CONSISTENCY_PASS_UNREVIEWED_UNACCEPTED，SHA256为c05d9fd3f63ca4a5278183a417ac5a78911e2d7640ca45b0be5ce9c3e4179394。源码verify_family.py的SHA256为7732db9cacee4b0d52fbf101b90bf4eff74e1ef9fe2dc2e60891a173fa95628b。文件一致性回执[scientific_file_check.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/scientific_file_check.json>)记录149个保护路径零变化，27个Linux/本地文件哈希全部一致；这是文件与传输核对，不是独立数学审阅。

旧b25状态已回读C8人工接受记录：限定完整signotope/noB5/noR6/no weak7模型内接受，原same-family/provisional和未知backend/effort保持。Joint17完整strict重放及全类语义稿保持原范围；Closure实际完整来源/CNF/proof仍未闭合，原ABORTED_BUDGET_FEASIBILITY回执保留，没有重启。

独立审阅状态须准确区分：.aris/README.md仍写prepared disabled；当前review-runtime.json却有activated=true、partial-functional记录，同时backend/effort仍标unverified。不能把二者摘要成“已核实可用”或简单断言runtime仍disabled。本轮未激活、改配置、调用或重试Claude，新增数学继续unreviewed/unaccepted。

现在最后代入a=16、b=25：

\[
N_{\rm sig}(7,5,7)\le a+b-1=40,
\]
\[
C\le2b=50,\qquad Q\le C+b+5\le80,
\]
\[
N_{\rm sig}(7,7,7)=Q+1\le81.
\]

本轮全局上界改善为零。第5节n=7例仅有D8及加根后的Q9；n=8例为D10/Q11，均非近极值或新纪录。条件性的Δ=3，或独立Δ=2与残余改善ε=1，或全类A1且z=2，仍可传播至Q≤77、777≤78；它们均未在本轮证明，不能登记为数值结果。

## 9. 状态分栏、局部最优审计及保留的下一步

| 类别 | 本轮准确状态 |
|---|---|
| 已完成手写证明，未独立审阅/接受 | 命题U的全部D_n集合分离和空锁定性质；显式n≥7非真空家族；式(1)–(2)的正确组合 |
| 操作定义的完整核对，非新容量定理 | 第6节全部路径必要充分判据；它没有提供低成本解 |
| 旧完整反例的新语境校准 | D12端点法费1而实际A1费0；通用端点二分失败归R22旧结果 |
| 条件性 | C的Δ改善、全类A1/A2、锁定/分解二分及77/78传播 |
| 尚未证明 | 近满核心为何迫足够锁定/共享出口，或为何迫低成本全路径分块 |
| 旧计算未决 | Closure完整实际CNF/proof链仍未闭合；没有借本轮小例核查升级它 |
| 接受状态 | 新数学unreviewed/unaccepted；b25既有人工接受单列 |

停止：仅靠空锁定、canonical和终点缺口标签宣称已缩小残余类；普遍端点图二分及奇圈费用收费；R27已抵消的纯人口交换；红六两两相交、无传播机制的ν阈值、λ优化及超时续预算。

降级：proper rootfan cut模板、无新传递的757、仅固定最小横截/私人路径的残余曲线。它们尚无所需完整进入机制。

下一步只保留两项：

1. **带实际大核心的全路径分块。** 使用R26最强共同预算，把“剩余配置满足什么全路径条件”落实到第6节实际P的判据，必须同时利用H的内部供应与R；先找一种对所有相关P同时有效的构造，再估计删点成本。命题U要求这一步显式使用H，不能再把缺口当成残余内部的新增禁形。若操作修复再次退回旧核，就停止该操作，不细化人口参数。
2. **766跨中点的共同实现冲突。** 从全类Joint和完整核心出发，寻找必须落在同一四点packet上的相反长链供应；必须证明这种支持交错在整个近极值类中必现。仅给出“若某几条供应如此交错则矛盾”的必要局部引理不计进展。完整成立的Δ可一次传播到Q和777，避免单独追逐757。

目前没有依据把其中任何一项预先指定为Δ=3或z=2。衡量下一轮的是同一实际容量预算中的新严格损失，或能真正构造低成本分解的全类进入定理。

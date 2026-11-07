# 饱和四核的异色供应匹配与临界路径障碍支持

日期：2026年10月28日。**本轮没有新全局上界；全部新增数学unreviewed/unaccepted。** 主定理和竞争引理由主会话及生成协作提供、主会话自核，文档执行者仅忠实转写与机械检查；这些过程均不是独立审阅。本轮scientific_invocations=0，未执行研究代码、有限科学枚举、SAT、证明重放或Closure重试，外部新文献0。

**1. 当前基线、来源时间与证据分层**

本稿开始时只读查看研究目录，最新原稿仍是[满25核内部插入与路径交换障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md>)；其后没有更新基线的研究文件。该稿已明确：单满25核的内部插入反例不排δ0双满核，同端点任意两路径的小步替换障碍也不排真正极小不可满足支持的消交叉。本轮不重新弱化这两个目标。

完整有序rank-3 signotope中，N_sig(n,r,s)表示避免蓝r路径、红s路径及weak n的最大规模。路径长度计顶点；四点a<b<c<d的packet按abc、abd、acd、bcd排列，至多一次变色。weak n要求同一对实际首末端点的两色路径长度和为n+2，不加内部不交条件；更长时可保端点缩短。诱导核的路径、秩和状态内部重算。

令a、b分别为747、756的有效工作上界，C=N_sig(7,6,6)、Q=N_sig(7,6,7)、F=N_sig(7,7,7)。a16沿既有有效输入；[C8正式人工接受](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)确认C1–C10均已接受，限定模型内N_sig(7,5,6)≤25，same-family/provisional与精确backend/实际effort不可核实的保证限制保持。后续结构草稿并未随之被独立接受，25点存在性也由构造另证。

证据必须区分四层：

- [Through14绑定结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/through14_binding/result.json>)为PASS，5077/5077规则行检查完成，all_Valid=true、ordered_literal_equality_all_rows=true、historical_UNSAT_receipt_linked=true；该次绑定的solver_calls、checker_calls、proof_replay_calls均0。[历史Through14 strict-RUP回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/through14_replay_result.json>)为PASS，5077源子句、3009添加步骤、81736严格提示。结合[完整全类语义原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>)，得到两色through各≤13；全类语义推导仍未独立审阅、未接受。
- [旧Joint17公式绑定](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json>)保留其原范围；[后续Joint17完整strict-RUP](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)为PASS，59479源子句、102563添加步骤、5166479严格提示，最终空子句。其[全类语义迁移](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)给端点联合界；公式重放和全类语义是不同证据边，不升级接受状态。
- [Closure规则结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)为PASS，但actual_cnf_equality_checked=false、UNSAT_checked=false。[来源获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)为ABORTED_BUDGET_FEASIBILITY，source_acquisition_complete=false、CNF_binding=false，solver/proof-checker调用均0。C≤49仍未闭合。
- [.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>)原文“Both project MCP routes disabled; review-runtime activated=false.”。本轮未调用、激活或重试独立Claude路线，未作模型或服务回退；机械文档检查不是科学核查或独审。

先写原结构关系：

\[
N_{757}\le a+b-1,\qquad C\le2b,\qquad Q\le C+b+5,\qquad F=Q+1.
\]

代a=16、b=25，仍是40/50/80/81。完整背景见[综合报告](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261028/synthesis.md>)及[R5覆盖增广](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>)、[R7残余结构](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)、[R20根归约](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)；本稿不改变其原有证明、作用域和接受层级。

**2. 方法审计：保持实际取等母体，不借错误弱化入口**

本轮主线始终保留同一完整取等母体的四个饱和核和全部实际路径；竞争线则进入真正包含极小不可满足族，不再使用任意两路径例子代替其支持结构。

| 审计项 | 饱和接口主线 | 极小不可满足族竞争线 |
|---|---|---|
| packet | 两份实际同色供应共享pair时逐包拼接出实际红四/蓝四 | 两条族内红六阻挡共享区间支持时逐包补齐同端红路径 |
| weak | 与同实际端点的异色p路径相撞；不得拼接不同端点的极值 | 与同一蓝五子链相撞，首末点逐一相同 |
| 取等或临界入口 | 母体规模2b，四核饱和，全部长路径横截数恰b | 删除临界蓝五后的实际满足赋值，极小性产生五个族内阻挡 |
| 新排除 | 完整异色pair阻断导致Hall缺陷或两色匹配冲突的临界接口子类 | 同一临界赋值的五个红阻挡具有过大区间内共同支持 |
| 反例与量词前提 | 单满核δ24反例不能替代双满核；不以抽象图冒充真实取等构造 | 任意两路径障碍不替代MUS；不合并不同Q的临界赋值 |

本轮不把“若交换合法就有收益”重复写成存在定理，不把匹配端点互异解释为路径支持互不交，也不从匹配数直接收取独占资源费用。实际匹配还将在各自本色through删除后的诱导核内实现，路径按内部实际三元颜色重新定义，不继承ambient图的路径。

**3. 旧R23的全类饱和入口与七点取等范围**

先保留一般参数。设整数p≥4、n=p+2，b是完整signotope模型N_sig(n,p,p+1)的有效上界；X完整、无两色(p+1)、无weak n，且|X|=2b。全部ambient集合S_R、E_R、S_B、E_B分别是实际红p、蓝p路径的首点、末点集合，诱导核路径在内部重算。

以下入口沿[R23 §5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)推广，不认新：同owner v若有蓝p末链与红p首链，取前者末前驱u和后者首后继w，检查χ(u,v,w)。任一颜色都会延成对应(p+1)路径，因此

\[
S_R\cap E_B=S_B\cap E_R=\varnothing.
\]

E_B内部无红p，否则其首点有蓝p前供，由同一连接禁配矛盾；X∖E_B无蓝p。两者分别落在容量b的颜色对偶域与原域，大小和为2b，故各恰b。又S_R⊂X∖E_B，且X∖S_R无红p、容量≤b，所以S_R=X∖E_B。换色同理：

\[
S_R\sqcup E_B=X,\qquad S_B\sqcup E_R=X,\qquad
|S_R|=|E_B|=|S_B|=|E_R|=b.
\]

每个v∈E_B，S_R∪{v}有b+1点，故由容量b必有蓝p；其末点不能在S_R，因为S_R没有ambient蓝p末点，故所有这类违规路径均为B_p(S_R^{p-1},v)。每个u∈S_R同理有R_p(u,E_B^{p-1})。另两族换色，得到到E_R的红入供和从S_B的蓝出供。这里保存全部实际供应，不固定便利的一条。

定义四原子

\[
L=S_R\cap S_B,\qquad D=E_R\cap E_B,\qquad
T_R=S_R\cap E_R,\qquad T_B=S_B\cap E_B.
\]

它们互斥覆盖X，且

\[
|T_R|=|T_B|=m,\qquad |L|=|D|=k=b-m.
\]

从l∈L出发的纯红出供进入E_B，末点又必在E_R，故末点在D；到d∈D的纯红入供来自S_B，首点又必在S_R，故首点在L。蓝色对偶。这是实际共同母体的全类入口，不能与任意覆盖的端点化混淆。

现在才代p=5、n=7、b=25。E_R和E_B各25点，既非两色末点的集合为L，双末点集合为D，均有25−m点。Joint17全类端点联合界给

\[
\min\{|X\setminus(E_R\cup E_B)|,\ |E_R\cap E_B|\}\le16,
\]

左边就是25−m，故m≥9。Through14全类语义分别给红、蓝through≤13，而t_R=t_B=m，所以

\[
9\le m\le13,\qquad 12\le k=25-m\le16.
\]

此范围使用上述未独审的语义迁移及各自固定公式证据，不升级接受，也未排任何完整m分支。

**4. 一般主定理：全部异色供应pair-shadow与两色边不交完美匹配**

**主定理。** 在第3段一般p≥4、n=p+2、|X|=2b的全部假设下，由完整纯供应定义的两色候选兼容图Γ_R、Γ_B，必须容纳两份边不交的完美匹配，分别覆盖L、D。红色匹配由诱导Y_R=X∖T_R内的实际红p路径实现，蓝色匹配由诱导Y_B=X∖T_B内的实际蓝p路径实现；各自避开本色through原子。

本轮匹配与接口定理本身不依赖Joint17、Through14；这两条既有研究结论只把七点剩余参数限制到9≤m≤13，其原始证据和未独审状态分别保留。

先证明实际拼接步骤。设红路径P从l开始、红路径Q在d结束，两个实际点l<x<y<d同时属于P、Q。路径遗传给χ(l,x,y)=χ(x,y,d)=R，packet(l,x,y,d)首尾同红迫全包红，所以(l,x,y,d)是实际红四。不要求P终于d或Q始于l，也没有预设两条原路径共同端点。若还有蓝p(l,d)，两色长度和4+p=n+2，得到weak n。此处packet/weak局部工具本身不认容量突破。

对l∈L定义A_R(l)：取全部纯红出供R_p(l,E_B^{p-1})，把其中包含于T_B的全部实际无序点对取并。对d∈D定义B_R(d)：取全部纯红入供R_p(S_B^{p-1},d)，把其中包含于T_B的全部点对取并。两者都是完整供应族的pair-shadow；全部替代路径、多外点参与的实际供应都保留。

颜色对偶地，A_B(l)取全部纯蓝出供B_p(l,E_R^{p-1})在T_R内的点对；B_B(d)取全部纯蓝入供B_p(S_R^{p-1},d)在T_R内的点对。定义

\[
\begin{aligned}
\Gamma_B&=\{(l,d)\in L\times D:l<d,\ A_R(l)\cap B_R(d)=\varnothing\},\\
\Gamma_R&=\{(l,d)\in L\times D:l<d,\ A_B(l)\cap B_B(d)=\varnothing\}.
\end{aligned}
\]

若红两族有共同pair{x,y}，纯供应的位置自动给l<x<y<d，不是另加次序假设。刚才的packet拼接排除该端对的任何实际蓝p，颜色对偶亦然。

现在以诱导核内部实际路径定义H_B：它是Y_B=X∖T_B中全部实际蓝p的L×D端点图；H_R是Y_R=X∖T_R中全部实际红p的L×D端点图。不是从ambient端点图删点后继承路径。纯蓝出供l+E_R^{p-1}及纯蓝入供S_R^{p-1}+d均避T_B，所以Y_B内每个L、D仍有相应供应；红色对偶。**H_c中的路径仍可使用L、D及相反颜色through的多个内部点，绝不要求是纯供应。**

Γ仍由全部ambient纯供应定义，按供应颜色对应，红纯供应在Y_R，蓝纯供应在Y_B。Γ_B由Y_R中的红纯供应在T_B上的共同pair决定；Γ_R由Y_B中的蓝纯供应在T_R上的共同pair决定。不能把Γ_B的红供应写成在Y_B中，因为它们正可使用被Y_B删除的T_B。上述排斥针对任意同端点异色p路径，因此仍有

\[
H_B\subseteq\Gamma_B,\qquad H_R\subseteq\Gamma_R.
\]

下面容量信息实质超出包含极小性。X中全部蓝p路径的最小顶点横截数τ_B恰为b：任一横截Z删后进入N_sig(n,p,p+1)域，故|X∖Z|≤b、|Z|≥b；E_B大小b给相反上界。红色对偶，所以

\[
\tau_B(X)=\tau_R(X)=b.
\]

更精确地，Y_B的蓝p横截数恰为k。删去任一内部横截Z后，实际配置进入容量b的原域，因此

\[
|Y_B|-|Z|\le b,\qquad |Z|\ge(2b-m)-b=k.
\]

Y_B内全部蓝p的首点在L，删L给相反上界。红色对偶得到Y_R的红p横截数也恰为k。两个层次是同一容量的不同实际删点陈述，不叠加收费。

证明H_B满足Hall。任取U⊆L，令N=N_{H_B}(U)，构造

\[
Z=T_B\cup(L\setminus U)\cup N.
\]

任意实际蓝p若在任何位置遇T_B，已遇Z；否则整条路径在Y_B内，其首点在L、末点在D。若首在L∖U亦遇Z；否则首在U，因整条路径属于新定义的H_B，末点必属于N。故Z横截X内全部实际蓝p，不管路径内部是否使用L、D或相反颜色through的多个点。三个集合互不交，因此

\[
|Z|=m+k-|U|+|N|=b-|U|+|N|.
\]

由τ_B(X)=b得|N|≥|U|。等价地，在Y_B中，(L∖U)∪N横截全部蓝p，大小k−|U|+|N|；内部横截数恰k也直接给同一Hall不等式。红侧在Y_R中同证。

为自足，Hall的匹配证明如下：若最大匹配不能饱和L，从未匹配左点出发沿交替路到达左集U及其全部邻集N(U)。不能到达未匹配右点，否则可增广；所有到达的右点各有匹配左点，而起始左点未匹配，所以|N(U)|<|U|，矛盾。故H_B、H_R各有饱和L的匹配；两侧均k点，都是覆盖L、D的完美匹配。

最后，两色实际端点图不可能有共同边(l,d)。否则同端点有红p和蓝p，2p≥p+4=n+2（p≥4），保端点缩短即得weak n。因而任取两色实际完美匹配，其边都不交，分别落在Γ_R、Γ_B，主定理得证。

两份匹配的实际路径分别避开自身颜色through原子。其抽象并图是交替偶圈覆盖，圈长至少4；这是无向二部接口的交替圈，**不是有向实际路径圈**，不能再以“点序有圈”制造矛盾。匹配只保证端点互异，不保证原始路径内部支持互不交，不按2k收独占费用。

旧归属必须分清：[R3 §6.3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md>)已有同端支持矩形和同一中间边的可靠拼接；[R22 §5.1](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>)已有单色实际端点匹配，内部也允许共享；R23给四核取等和纯互补供应。本轮组合新增的是相反through原子中的全部纯供应pair-shadow、两色边不交匹配及其临界接口禁止类，不认Hall、packet或旧单色匹配本身新颖。

**5. 已排除的具体接口子类、一般禁止类与首次断点**

先给不靠图名称的具体结论。假设存在两个不同实际双源l1、l2∈L和一个d*∈D，使每个i=1,2、每个d∈D∖{d*}且l_i<d，都能从完整纯红出供(l_i,E_B^{p-1})和完整纯红入供(S_B^{p-1},d)中找到共享两个T_B点的两条供应，则这一取等母体不存在。

证明：packet+weak使这两个源的任何蓝p路径若终于D，只能终于d*。在l_i之前的d本就不能当终点，无需供应阻断。于是

\[
Z=T_B\cup(L\setminus\{l_1,l_2\})\cup\{d^*\}
\]

横截全部蓝p，且|Z|=m+(k−2)+1=b−1。留下b+1个真实点进入原容量域，矛盾。p5、b25时就是删24留26。结论覆盖任意实际点序、全部9≤m≤13、全部25核目录和替代见证，不是固定构造模板。它只排上述明确的临界接口模式，未证明每个取等母体都必有此模式。相比只知每源有终点，这里两个源不能被完整异色pair阻断压到同一个终点；容量用于真实抗删除，普通最小性不能代替。

一般地，主定理排除两个接口子类：

- **I：Hall缺陷。** 某一颜色存在U⊆L使|N_{Γ_c}(U)|<|U|，也就是另一色完整纯供应的共同pair阻断，把U的全部可行终点压到少于|U|。H_c⊂Γ_c，上段Hall横截构造给至多b−1点的全部长路径横截，留下至少b+1点的实际核心矛盾。
- **II：两色匹配冲突。** 两色兼容图各自通过Hall，却不存在边不交的两份完美匹配；特别是某条实际边在两色各自的所有完美匹配中都被强制使用。实际H_R、H_B的两份边不交匹配不可能落入这种接口，故同样排除。

这些模式在任何取等母体中都不可能，已经是临界接口子类排除，不只是“若操作合法则有收益”的判据。但没有证明所有取等母体落入I或II，也没有声称I或II曾有真实50点构造。

代p5、n7、b25后，每个剩余取等母体都必须在Y_R内有12至16对实际红五匹配，在Y_B内有同规模实际蓝五匹配；两色边不交，各自避开本色through，并同时受到全部异色纯供应pair-shadow排斥。仍未排任何完整m值。首次断点是：容量虽把两个本色through删除核的实际横截数分别钉为k，仍未给出pair-shadow必须具有的密度或排列，因而尚未证明Γ_R、Γ_B必不能容纳这两份诱导核内匹配。不提供抽象图或小例来冒充完整临界反例，也不把这个断点改名为新全局定理。

**6. 独立竞争引理：真正MUS内部的五条红六阻挡**

设X是实际767母体，F是按完整路径计的包含极小不可满足族：每条红六捆绑要求同时遇K、Y，每条蓝五要求遇K。这里的极小性在路径要求层面，而不是把红六的两个条件拆成普通CNF出现次数。

设蓝五Q=(q1<q2<q3<q4<q5)属于F。对任意满足F∖{Q}的角色赋值σ，Q必全为Y，否则σ已满足F，矛盾。把qi单独改为K会修好Q，不能破坏任意蓝五，也不能新造红六全Y；F不可满足，所以必有某条红六Ri∈F∖{Q}变成全K。原赋值因此满足

\[
R_i\cap Y=\{q_i\},\qquad R_i\cap Q=\{q_i\}.
\]

五条Ri各不相同：同一条阻挡不可能在同一原赋值下有两个不同的唯一Y点。此结论对每个临界赋值和所有阻挡选择成立，不挑便利的五条。

任取i<j，令

\[
H_{ij}=(R_i\cap R_j)\cap(q_i,q_j),\qquad k=|H_{ij}|.
\]

若k≥2，Ri给qi加H中全部三元红，Rj给H加qj中全部三元红。每个h∈H另选h'∈H，packet(qi,min(h,h'),max(h,h'),qj)首尾红迫全红，补齐同时含qi、qj的三元。因此qi、H、qj按实际次序形成红(k+2)路径。Q的子链qi,…,qj则是同实际端点的蓝(j−i+1)路径。no weak7给

\[
k+j-i+3\le8,\qquad\text{即}\qquad
|(R_i\cap R_j)\cap(q_i,q_j)|\le5-(j-i).
\]

若k≤1，上界自动成立，故该式对所有i<j都成立。

真正被排除的是MUS内临界蓝五的阻挡共享模式：首尾阻挡不能有两个区间内共同点；相隔三个位置的阻挡不能共享三个区间内点，相隔两个位置不能共享四个区间内点。不是任意两条路径，也不是普通CNF出现次数：包含极小性和不可满足性先产生族内五个阻挡，packet再从同色阻挡制造新的共同实际端点路径，最后使用weak。

范围和断点保持：没有控制区间外共享，没有证明所有MUS都被迫产生足够的区间内交叠，没有得到z≤4。不同Q的critical assignments不能合并。没有证明每个MUS必含蓝五；纯红六MUS分支没有这一入口。该引理不依赖主线匹配或未证交换，是实质独立的竞争结构，不重复上一轮任意两长路径反例。

**7. 来源核查、机械检查与零科学调用**

本轮只读上述主承重来源、最新原稿与原始结果；[来源保护清单](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_saturated_interfaces_20261028/SOURCE_MANIFEST.json>)固定34个明确读取的旧文件当前字节及SHA256，之后逐项复核。这个范围是被读取的保护源，不是全工作区前后审计；不按历史hash恢复文件。

新增证明无需新的小规模枚举，本轮未启动研究代码、Windows或Linux科学运行、SAT、长算、证明重放、Closure下载或重试。scientific_invocations=0、solver_invocations=0、proof_checker_invocations=0、external_review_calls=0、external_new_literature=0。旧Through14、Joint17的PASS只按既有绑定读取，绝不填作本轮执行。

新增稿只由指定执行者忠实转写主会话已定数学，机械检查只核对本地链接存在性、公式分隔、文本边界和读取源hash；不是数学独立review。请求的native gpt-6.1-sol/high角色不等于backend或实际effort已由独立证据核实。没有调用禁用独审，没有更换模型、服务或审阅路线，unreviewed/unaccepted保持。旧稿、综合、接受、证书、封存运行、traces、任务状态和指针均不由本轮改动。

**8. 收益结算与唯一承重问题**

仍先沿原结构式

\[
N_{757}\le a+b-1,\qquad C\le2b,\qquad
Q\le C+b+5,\qquad F=Q+1,
\]

最后代a16、b25得到40/50/80/81。本轮新增全局数值下降0；排除的是有明确完整供应特征的临界接口子类，以及真正MUS内部不允许的区间共享模式，尚未排任何完整m分支。

停止任意覆盖的普遍端点化、任意两路径的普遍小步交换，并停止从匹配数直接按独占资源收费。不以更多标签或小模板替代全类进入。

下一步只保留一个承重问题：在9≤m≤13的同一真实饱和四核中，完整纯供应是否必迫某一Hall缺陷或两色匹配冲突？若该机制不足，需要实际接口层面的障碍；本轮尚未决定。此问题不削弱成单满核或任意小路径对问题，也不新增其它路线。

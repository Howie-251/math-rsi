# N7：R26共同预算下的全终点延伸定理与空锁定分支障碍

日期：2026-10-27。本轮继续现有长期任务，保持 in_progress、completedAt=null。结论先说明：没有新的全局数值上界。本轮实质交付是从旧三链证明提取并完整证明的“保留每个实际终点、统一服务全部前供”的延伸定理，独立引理扩至 n≥5；以及由旧完整七点模型严格排除“空锁定自动产生 proper rootfan cut”的全类入口。旧三链核心思路、R26共同预算与旧构造不作为本轮原创重计。

主会话 Astra 负责数学，Astra生成协作提供来源定位和推导协作；native gpt-6.1-sol/high只忠实转写和机械文档核查，请求的模型/effort与未独立报告的backend/actual effort分开。本轮不需要新的科学代码、SAT、枚举或checker，全部证明在正文逐分支给出。若未来执行科学工作，仍须指定执行模型在权威Linux运行。独立Claude服务仍按 [.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>) 保持disabled，未激活、未改模型、未重试；生成协作和文档检查不替代独立审阅。新增结论均为 unreviewed / unaccepted，b25的既有接受范围和assurance单独保留。

## 1. 原始材料、历史纠正与两条主线比较

本轮读取 [AGENTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/AGENTS.md>)、[Trellis workflow](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/workflow.md>)及执行分工，继续用户指定研究目录。首先核对 [N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>)、[RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>)（R26）§§2–4、6–7、11、[N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)、[N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md>)、[RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)（R7）、[RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)（R20）、[BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>)。直接依赖又回读R7三链、R26逐支证明及完整小例、[RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md>)（R27）§§3–4，以及 [BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md>) §§6–7。

**纠正上一轮的当前口径。** R20单凭两份独立估计不能相加，是正确的历史限制；但R26已经用同一次实际K证明更强的共同预算。上一轮报告§6.1停留在R20，遗漏了这项已完成强化，不能继续据此说当前没有 |U|+|W|≤d_H。本稿使用R26最强版本，旧稿保留不改。R26当时的b25尚为用户工作输入；随后C8验收已更新b的状态，不能反过来修改R26原历史记录，也不能把R26本身升级为已接受。

| 比较项 | A：障碍必现／强制分解 | B：766共同近极值稳定性 |
|---|---|---|
| 全类入口 | 任意767的ambient红六源分解；canonical端封闭；R26同一K预算 | 任意766的四类五链源末点、Joint全类端点界、全缺额角色恒等式 |
| 已接近完成的机制 | 锁定出现后的完整收费已完成；空锁定可从旧三链导出更强的实际端点约束 | 一步五链扇的直接色冲突已能完整分类，但不同中点间的packet耦合尚未形成强迫引理 |
| 严格净损失来源 | R26共享出口只删/补一次，实际交集中的不同owner各留一单位；仍缺这些owner必现 | 必须由同一颜色函数中的禁形或合法操作产生；through人口增加本身没有容量收益 |
| 已知障碍 | D12否定红六两两相交；旧七点族否定空锁定必有proper cut；R27全修复会回到旧核 | 标量约束有共同松弛赋值；实际点对匹配不是缺失状态匹配；共享尾不能按次数收费 |
| 明确出口 | A1给C+b+z；A2给3b+z；锁定族按R26收费 | 若证C≤2b−Δ，才给Q≤3b+5−Δ |

本轮选择A，具体工作限定为：保留空锁定源的全部红终点及所有前供，把R26的最大出链余量升级为同一实际端点上的路径不等式。B保留竞争地位，不另开状态或人口分支。没有预设z=2，也不把顶点重新分块误称为改变三元组颜色。

## 2. 模型与实际使用的最强既有预算

N_sig(n,r,s)是最大避免规模。完整有序rank-3 signotope满足四包abc,abd,acd,bcd至多一次变色；路径按点数，weak n由同一对实际左右端点的异色路径、长度和n+2定义。单色路径的所有子序列仍同色；因此异色同端路径不能共享内点。长度和超过n+2时可以保端缩短，故无weak n意味着两色同端最大长度之和≤n+1。

用 \(\mathscr Q_n\) 表示无蓝(n−1)、无红n、无weak n的完整配置类，避免与其最大规模混淆。对实际x<y，\(P_c(x,y)\) 是X中首末点恰为x,y的最长c色路径点数，至少为2。下文所有路径均在注明的同一配置内计算，子配置身份必须重算。

先固定n=7、X∈\(\mathscr Q_7\)，b为756及换色类的有效容量上界。canonical分解X=H⊔R来自R7；R20已证任意ambient红六的两个外端点不能同时落在H，内点允许经过R。令
\[
d_H=2b-|H|,\quad S_R=R\cap\operatorname{Src}_{R6}(X),
\]
\[
W=\{r\in R:\text{存在从H出发、终于r的ambient红六}\},\quad
U=R\setminus(W\cup S_R).
\]

对混合源s∈Src_R6(X)∩Src_B5(X)，令\(\mathcal T_s\)为全部红六实际终点，\(\mathcal Q_s\)为全部蓝五实际第二点。R26的锁定族为
\[
F_+=\{s:\mathcal T_s=\mathcal Q_s=\{o(s)\}\}.
\]
所有替代供应都在定义中。R26内禀定理为
\[
|X|+|F_+|\le3b+5,
\]
反序给F_-的同式，但不能相加两方向费用。

### 2.1 R26共同预算：完整机制及其域

任取A⊆F_+∩R，定义
\[
B=o(A)\cap(H\cup U),\quad E=o(A)\cap(S_R\setminus W),
\]
\[
K=((H\cup U)\setminus B)\cup A.
\]
则R26§4已证明
\[
\boxed{|A|+|U|+|W|+|E|\le d_H.}\tag{R26}
\]
为明确全部路径域，重述证明机制，不作为新结果。

任何红六末点都不能启动蓝五：在入链末前驱、共同点、出链第二点组成的joining三元组上，红使红链增为七，蓝使蓝链增为六。因此锁定owner与出口不交，A∩W=∅。

K中若有红六，按外端点分类：H→H违端封闭；H→U违W定义；U不能启动任何ambient红六；H→A违反A是蓝五源；从A启动只能终于o(A)，而这些出口已删或在K外。其余禁形由X遗传，故K为实际766。这个分类允许内点使用多个新增A点。

对每个w∈W∪o(A)，在全部H-origin红六到w的源，以及A中出口为w的源之间，选最早c_w。canonical H的红六源均有ambient红五入、蓝五出，由旧三链，其全部蓝五第二点都等于w；A候选同样由锁定定义满足此事实。c_w是蓝五源，不能是红六末点，因此未被B删除，实际属于K；w在K外，所以c_w不是K内部蓝五源。

若K内部有红五终于c_w，取其末前驱u及任一ambient蓝五(c_w,w,…)。χ(u,c_w,w)若蓝给蓝六，故红；红五后接w便得到同终点、更早起点x的红六。若x∈H或A，则是同一候选集的更早成员，矛盾；若x∈U，则违反无ambient红六源。故c_w也不是K内部红五末点。不同w不能给同一c_w，因为该点的非空蓝五第二点集已被迫同时等于两个不同单点。

因此每个不同出口贡献一个不同的实际neutral。出口的精确不交分类给
\[
|\operatorname{neutral}(K)|\ge|W\cup o(A)|=|W|+|B|+|E|.
\]
在任意766中，内部蓝五源与内部红五末点不交；分别删这两类后为756及换色类。因此
\[
|K|+|\operatorname{neutral}(K)|\le2b.
\]
又\(|K|=|H|+|U|-|B|+|A|\)，相加抵消B得(R26)。共享出口只计一次，新增前供和多外点路径由共同最早代表完整处理。

取A=∅已得
\[
\boxed{|U|+|W|\le d_H},\qquad
|R\setminus\operatorname{Src}_{R6}(X)|\le d_H.
\]
非空A还保留E及W∩S_R的扣减。它覆盖所有缺额，不能与反向预算、内禀F费用再次作为独立节省相加。R20给较弱独立估计；R26提供真正升级的操作证明，两者历史范围不混淆。

### 2.2 为什么收费定理尚未给统一下降

R26还构造内禀S=Src_R6(X)、H0=X\S及带出口修正的K,D，证明
\[
\delta:=3b+5-|X|=|F_+|+\varepsilon_K+\varepsilon_D,
\quad\varepsilon_K,\varepsilon_D\ge0.
\]
这里\(\varepsilon_K=2b-|K|-|o(F_+)|\)、\(\varepsilon_D=b+5-|D|\)来自实际操作，不是额外收费。若F_+=∅，则原S已经属于D7、H0属于766，X=H0⊔S。这是全类入口，但仍只给旧C+D7。空族不自动使某项余量严格，尚未得到更低容量分解。

## 3. 深入新命题前的八项审计

1. **完整模型和进入。** 独立引理针对每个X∈\(\mathscr Q_n\)、n≥5及每个实际混合源；集合从全部路径定义。混合源若锁定已有R26收费；否则下述可用终点集非空。没有假定近满、某个尾或固定分解。
2. **同一母配置。** 红长链、蓝长链、任意红前供与用于weak的蓝前供始终来自同一X、同一实际点对偏序；不拼接独立接口。
3. **严格机制。** 新机制是固定实际终点t后，存在同一实际两点延伸服务全部红前供，从而排除同端蓝路径。它比最大出链数的余量保留更多信息，但本轮尚未证明这种排斥必造成容量净亏。
4. **共享和补偿。** 同一源的所有前供共用所构造的两点；不同源/终点可以共享这些点。不作单射假设，不按路径或尾数收费。新增容量收费仍只能走R26。
5. **传播。** 新的全终点蓝覆盖充分条件可触发R26锁定收费；其他分支若能进入A1/A2，再按第8节各自公式传播。本轮没有证明全类强制覆盖或分解。
6. **是否改写目标。** 命题直接规定实际三元组颜色及指定首末点路径长度，与a、b、目标规模无关；不是缺额或障碍数量的重命名。
7. **旧反例。** D12只否定红六两两相交，不否定本引理；单根嵌入不改变证明域。共享尾例要求保留共享，本证明不对其收费。空锁定必cut被第6节完整例否定，不作为引理假设。
8. **失败时的停止。** 若全类端点延伸失败，将直接否定所需同端桥接机制；本轮已逐分支证明。下一步若必须限定某个尾、某个满核或某个cut才能迫覆盖，应停止该入口，不扩展模板。

## 4. 新的全类结构定理：保留全部实际终点的统一延伸

### 4.1 准确陈述

设n≥5、X∈\(\mathscr Q_n\)。对
\[
s\in\operatorname{Src}_{R_{n-1}}(X)\cap\operatorname{Src}_{B_{n-2}}(X)
\]
定义非空集合
\[
\mathcal T_s=\{t:\exists R_{n-1}\text{从s到t}\},\quad
\mathcal Q_s=\{q:\exists B_{n-2}\text{以}(s,q)\text{开始}\},
\]
以及
\[
\mathcal T_s^{\ne}=\{t\in\mathcal T_s:\mathcal Q_s\setminus\{t\}\ne\varnothing\}.
\]
这里集合只保存实际路径的终点或第二点，不是自由flags。

**定理E。** 任取t∈\(\mathcal T_s^{\ne}\)、q∈\(\mathcal Q_s\setminus\{t\}\)，以及任意实际红(n−1)路径P从s到t，均存在实际a满足s<a<t，且
\[
\boxed{\chi(f,s,a)=R\quad\text{对全部}f<s,\qquad\chi(s,a,t)=R.}\tag{E1}
\]
若q<t，可取a=q；若q>t，可取a为P的末前驱。同一个a与t服务该s的全部红前供，不依赖前供的起点或所选路径。

因而对所有实际x<s及所有t∈\(\mathcal T_s^{\ne}\)，同时有
\[
\boxed{P_R(x,t)\ge P_R(x,s)+2,}\tag{E2}
\]
\[
\boxed{P_R(x,s)+P_B(x,t)\le n-1.}\tag{E3}
\]
不同的t,q,P不必共用同一个a；不同源也不必具有不同的a或t。这些共用/不共用都不影响结论。

**与旧结果的关系。** R7§3.1和R26§3.1已经给出下述核心分支。R26的陈述保留的是\(\rho_R(x)\ge k+2\)或锁定；它忘掉新链的实际终点。本定理保留每个可用t、给出一个同时服务全部前供的实际两点尾，并与同一个(x,t)上的蓝链比较，得到(E3)。本轮认领这个量词和端点层面的强化及独立n=5边界，不认领旧三链分支为新思路，也不把它计为容量下降。

### 4.2 完整证明：q<t分支

取任意实际蓝(n−2)路径J=(s,q,j,…)，j存在因为n≥5。对任何f<s，若χ(f,s,q)=B，则把f前接J形成蓝(n−1)，违反X的蓝帽。因此
\[
\chi(f,s,q)=R\quad(\forall f<s).\tag{1}
\]
若q<t而χ(s,q,t)=B，则蓝三(s,q,t)与红(n−1)路径P共享实际端点s,t，长度和n+2，形成weak n。因此χ(s,q,t)=R，取a=q即得(E1)。q可以是P的内点，所构造的新路径的前供全部≤s，而q,t>s，不会重复。

### 4.3 完整证明：q>t分支

记P末三点为(v,u,t)。n≥5保证P至少四点，所以s<v<u<t<q<j；n=5时P恰为(s,v,u,t)。令J'=J删去s。

首先χ(u,t,q)=B，否则P后接q为红n。

若χ(s,t,q)=R，则统一点对偏序给
\[
\lambda(tq)>\lambda(sq)>\lambda(qj).
\]
后一个比较来自蓝链J。于是χ(t,q,j)=B，否则红三t<q<j会给相反的点对比较。结合χ(u,t,q)=B，(u,t,J')为蓝(n−1)，矛盾。故
\[
\chi(s,t,q)=B.\tag{2}
\]

再反设χ(s,u,q)=R。若χ(v,u,q)=R，则P删去t后追加q仍为红(n−1)，它与蓝三(s,t,q)同端点s,q，构成weak n。若χ(v,u,q)=B，则
\[
\lambda(uq)>\lambda(sq)>\lambda(qj)
\]
迫χ(u,q,j)=B，所以(v,u,J')为蓝(n−1)。两种颜色都矛盾，故
\[
\chi(s,u,q)=B.\tag{3}
\]

由(1)和(3)，对每个f<s都有
\[
\lambda(fs)<\lambda(sq)<\lambda(su).
\]
若χ(f,s,u)=B，蓝三会给λ(su)<λ(fs)，矛盾。因此对全部f<s同时有χ(f,s,u)=R。P的子链给χ(s,u,t)=R，取a=u，得到(E1)。

q>t时J'全部在P之后，所以上述拼接无次序或重复点问题。证明没有假定前供的内部点属于某个核心；全部域均是X。

### 4.4 全部前供、同端weak及边界

任取从x到s的红路径，长度k≥2，记其末前驱f。由(E1)，在其后追加同一a,t得到长度k+2的红路径，实际首末点为x,t。任取最长前供即得(E2)。这也处理只有两点的前供：此时f=x，新增的两个三元组正是(E1)。

再取X中从x到t的最长蓝路径。它与上述延长的红路径具有同一对实际端点；无weak n给两长度和≤n+1。因此
\[
P_R(x,s)+2+P_B(x,t)\le n+1,
\]
即(E3)。若两路径共享内点，packet子链闭包早已直接矛盾；若总长过大，保端缩短得到weak n。无需添加内部不交假设，也不能改用不同实际起点。

s为最早点时，全前驱断言真空，但a的构造仍成立。n=5时两条禁止蓝拼接分别是(u,t,q,j)、(v,u,q,j)，均为四点；删t补q为红四，配蓝三正是weak5。故n=5全部分支有效。n=4缺J的第三点，本稿不声称适用。

这次扩域只属于独立定理E。canonical、D_n分解和R26完整预算仍保持原n≥6范围。定理证毕。

## 5. 空锁定分支现在得到的实际结构及尚缺之处

### 5.1 精确二分和蓝端点覆盖判据

因为\(\mathcal T_s,\mathcal Q_s\)都非空，
\[
s\in F_+\iff\mathcal T_s^{\ne}=\varnothing.
\]
证明：若右侧为空，任取t∈\(\mathcal T_s\)，便有\(\mathcal Q_s=\{t\}\)；遍历全部t迫\(\mathcal T_s\)也是同一单点。反向直接成立。

所以任意实际混合源都进入“锁定”或“具有非空全终点延伸族”之一，覆盖完整路径族。空锁定时，所有混合源同时具有(E1)–(E3)，并非只获得一个最长链人口限制。

若t∈\(\mathcal T_s\)，且有某个实际x<s的蓝(n−2)路径终于t，则t不能属于\(\mathcal T_s^{\ne}\)：否则(E3)左侧至少2+(n−2)=n>n−1。故
\[
\boxed{\text{若存在 }B_{n-2}:x\to t,\ x<s,\ t\in\mathcal T_s,
\quad\mathcal Q_s=\{t\}.}\tag{E4}
\]
仅一个终点被这样覆盖时，只能得到蓝第二点集单点，不能提前声称全部红终点单点。

若**每个**t∈\(\mathcal T_s\)都有这种来自s之前的蓝(n−2)路径（不同t允许不同起点与完全共享供应），(E4)及非空\(\mathcal Q_s\)迫所有t相同，于是s∈F_+。这是一个真实的全终点覆盖充分条件。

等价地，若s未锁定，则至少一个实际红终点不能被s之前启动的蓝(n−2)链达到；更强地，所有t∈\(\mathcal T_s^{\ne}\)都满足(E3)。对n=7，红前供长k时，同一个(x,t)的蓝路径至多6−k；k=4、3、2分别给蓝至多2、3、4。这是实际同端排斥，不是缺失状态计数。

### 5.2 反向版本及不重复收费

反序同色得到终点版本。对混合终点s，令可用红首点t<s对应的全部蓝(n−2)倒数第二点不全等于t，则对所有y>s有
\[
P_R(t,y)\ge P_R(s,y)+2,\qquad
P_R(s,y)+P_B(t,y)\le n-1.
\]
正反两组约束可以在同一个X中同时成立，但R26的两份容量预算仍不能相加。这里没有给同一个neutral、缺失状态或路径尾重复收费。

### 5.3 已扩大什么，尚未完成什么

定理E把原来仅知道“某处存在长红后续”的\(\rho_R\)余量，改为对全部可用实际终点的同端长度约束；同一个所选后继对服务全部前供，因此可以与另一核心供应的具体蓝路径发生可核对的颜色/weak冲突。这是可直接用于共同实现的结构强化。

但尚未证明近极值配置会强迫第5.1节的全终点蓝覆盖发生，更未证明发生于足够多个不同源。若某些红终点缺少这种早蓝供应，也尚未证明这些缺口构成A1或A2的低容量分解。不能把缺口数量另命名为“交换缺额”就宣称下降。故本轮完整二分的第二支已得到更强实际路径结构，却尚没有更低容量；这一未闭合边界明确保留。

## 6. 严格障碍：空锁定不强迫proper rootfan cut

以下构造来自R26§7.3，原模型不是本轮新造。本轮提取其对**所有**proper cuts的排除，终止一个无条件全类入口，而非只排某个指定cut。

取a1<…<a6<v，令t1=R，t2=t3=R，t4=t5=B，并规定全部三元组
\[
\chi(a_i,a_j,a_k)=\overline{t_j},\qquad
\chi(a_i,a_j,v)=t_i.
\]
只需t1,…,t5，因为三元中点和根三元第一点不会是a6。

**全部packet。** 不含v时为\((\overline t_j,\overline t_j,\overline t_k,\overline t_k)\)。含v时为\((\overline t_j,t_i,t_i,t_j)\)：若t_i=t_j，只有第一项可能不同；若二者不同，前三项相同。每种至多一次变色，已覆盖全部四点型。

**全部路径与weak。** 内部单色路径的每个内点必须有同一个指定标签，a2,…,a5中红蓝各二，故两色链均至多四点。任意终于v的同色路径若至少四点，其末四点ai,aj,ak,v的两连续三元色分别为\(\overline t_j\)、\(t_j\)，矛盾，所以至多三点。固定内部首末点ai,ak，红/蓝最大长度分别等于2加中间相应标签数，两者之和为该区间点数加二，至多八；终于v时和至多六。因此整个七点X是完整766，亦属767，无任何红六。

于是F_+=F_-=∅，内禀S=∅、H0=X。

**排除全部proper cuts。** 反设实际连续分割L<R，两侧各至少两点，满足R26§6.3的rootfan条件：AAB色不依右点选择，ABB色不依左点选择。由于v最大，取ai<aj∈L和z<v、z∈R。固定右对(z,v)，左点独立性迫
\[
t_i=\chi(a_i,z,v)=\chi(a_j,z,v)=t_j.
\]
固定左对(ai,aj)，右点独立性迫
\[
\overline t_j=\chi(a_i,a_j,z)=\chi(a_i,a_j,v)=t_i,
\]
矛盾。因此没有任何proper rootfan cut。

它严格否定“F_+=F_-=∅便强迫X或H0有proper cut”的无条件命题。它不否定还要求大H0、大S、近饱和等真正共同容量条件的命题，也不否定其他A1/A2分解。R26短前供条件在此例S为空而真空成立，所以该条件本身不可能提供通用cut入口。不能借该小例声称近极值配置存在，也不能继续用空族标签直接调用cut容量界。

## 7. 竞争主线B的精确停止点

对任意完整766核心K，在K内重新计算全部五链第二点集Q_c(v)和末前驱集P_c(v)。禁止单色六链直接给
\[
w\in Q_c(v)\ \text{或}\ u\in P_c(v)
\quad\Longrightarrow\quad\chi(u,v,w)=\overline c
\quad(u<v<w).
\]
这是完整的一步延伸扇规则，包含所有替代路径。

对同一个实际三元组提出相反颜色，当且仅当：w同属Q_R(v)、Q_B(v)；或u同属P_R(v)、P_B(v)；或w∈Q_R(v)、u∈P_B(v)；或w∈Q_B(v)、u∈P_R(v)。这是两种颜色的两个析取逐项展开，四种组合穷尽。

后两类已被Src_R5∩End_B5=Src_B5∩End_R5=∅排除；前两类只限制同一中点的同方向邻点集合。红through点的入红五和出红五都强迫蓝色，彼此不冲突；不同中点不能强迫同一个有序三元组，因为中点唯一。

所以Joint给更多through人口，本身不会在这一完整的一步规则层制造颜色矛盾。下一步必须加入跨不同中点的packet约束，或给出保留实际邻点的新路径达到定理。这个障碍仅针对上述一步规则，不否定完整packet、异常专用charging或长路径共同实现方法。

R26的有效收费恰通过另一项真实结构：同一个出口的最早代表、内部红五若存在就产生更早同出口红六。不能用ambient前供代替K内部前供，因为它可能穿过已删除出口。B暂留竞争方向，未构造异常组到实际缺失普通状态的全子族关联，不预设κ，也不继续逐异常增加局部条件。

## 8. 一般参数传播：各出口分开

令a为747有效界，b为756有效界，C=N_sig(7,6,6)，Q=N_sig(7,6,7)。已有研究骨架为
\[
N_{\rm sig}(7,5,7)\le a+b-1,\quad C\le2b,\quad D_7\le b+5,
\]
\[
Q\le C+D_7,\qquad N_{\rm sig}(7,7,7)=Q+1.
\]

定理E本身没有推出新的C、D7或Q容量常数。它给出如下准确条件性接口：

- 对某个完整配置族，如果每个X都存在至少k个不同的混合源，且每个这样的源的全部红六终点都能被该源之前启动的实际蓝五链覆盖，则这些源属于F_+，R26给\(|X|\le3b+5-k\)。不同源才各计一次；覆盖路径数量不收费。要升级全体Q，必须另证完整进入定理，不能由命名条件替代。
- 若全体X都有实际分割X=K⊔Y⊔Z，K∈766、Y∈756、|Z|≤z（A1），则\(Q\le C+b+z\)。若另独立证明C≤2b−Δ、z≤5−ε，则\(Q\le3b+5-\Delta-\varepsilon\)，777再加一。
- 若全体X删Z后能分为两个756块和一个换色756块（A2），|Z|≤z，则\(Q\le3b+z\)。它不能自动再减去C的Δ。
- 若未来证明一个真正全类二分：每个X或者有上述k个被覆盖的不同源，或者进入A1的z分解，则

  \[
  Q\le\max\{3b+5-k,\ C+b+z\}.
  \]

  两支由实际路径覆盖或实际分块定义，不把“已满足上界”本身当第二支。这个进入定理尚未证明。

- 竞争主线若完整证明C≤2b−Δ，则\(Q\le3b+5-\Delta\)、\(N_{\rm sig}(7,7,7)\le3b+6-\Delta\)。整体状态方法仍需先证明同一X的异常—实际缺失普通状态全子族覆盖；仅有\(|X|=30+e-m\)不给Δ。

proper rootfan cut仍只有子类界\(U_{\rm cut}\le\max(2a,a+b+5)\)。第6节没有为它提供近极值进入定理，故不开展模板搜索。残余曲线若真能全类证明\(\tau=t\Rightarrow\alpha\le b-f(t)\)，才有\(D_7\le b+\max_{0\le t\le5}(t-f(t))\)；本轮没有新的f。

## 9. 证据等级、核查与路线裁剪

| 类别 | 本轮准确状态 |
|---|---|
| 新完整推导，未独立审阅/未接受 | 定理E的全终点、全前供、同端蓝排斥及独立n≥5范围；全终点蓝覆盖迫锁定的充分条件 |
| 新提取的严格方法障碍，未独立审阅/未接受 | R26旧七点族排除全部proper cuts，否定空锁定自动cut；一步五链扇的全部直接颜色冲突按中点分类 |
| 旧结果沿用 | R7三链和单根嵌入、R20端封闭、R26同一K共同预算和内禀收费、Joint及全缺额角色定理、原七点构造 |
| 条件性公式 | k个覆盖源、A1、A2、C下降以及残余曲线的传播；均不登记新数值 |
| 尚未证明 | 近极值强迫足够多全终点蓝覆盖；覆盖失败强迫低容量分解；跨中点packet冲突；异常到缺失状态全子族覆盖 |
| 已知反例保留 | D12的ν=τ=2、α=10；仅补canonical不能恢复两两相交；共享尾和前驱重复各保持原否定范围 |
| 计算/证明未决 | Joint17已有严格重放及全类语义迁移，状态不升级；Closure实际完整CNF/proof仍未闭合，不能用C≤49或C≤47；旧超时不重启 |

本轮不启动新科学计算：新定理的q<t、q>t、全部拼接、n=5边界、共享与退化情形均已逐支证明；七点障碍按全部packet型及全部cut直接证明。没有需要用大型SAT替代的步骤，也不为了增加证据数量重跑已完成检查。文档执行者只进行来源身份、链接、给定公式转写、状态标签和旧工件保护核查，不构成独立数学验证。

本轮隔离记录在 [D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_extension_r26_20261027/](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_extension_r26_20261027/>)。[source_manifest.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_extension_r26_20261027/source_manifest.json>)、[protection_before.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_extension_r26_20261027/protection_before.json>)、[metadata_and_pointers_before.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_extension_r26_20261027/metadata_and_pointers_before.json>)保存写入前身份；文档检查回执保存写入后的保护比较。旧报告、CNF、证明、反例、失败回执、接受、task及会话指针均保留。

路线决定：主投A的实际全终点蓝覆盖/覆盖失败结构；B只保留跨中点packet共同实现这一明确缺口。停止无条件空锁定⇒proper cut、红六packing阈值续搜、canonical标签修补、λ优化和R27已证明精确回到旧核的纯人口交换。A2仍是候选出口，不预设唯一主线。单独757没有新传递定理时不投入。

下一步只保留两项：

1. 在同一个近满H与残余中，证明某些混合源的全部红六终点确实有来自源之前的蓝五供应；若该覆盖失败，必须利用定理E明确给出的同端蓝缺口构造A1，或给出完整模型反证。不能把H内部供应的起点擅自移到s之前，也不能只覆盖一个方便终点。
2. 竞争性研究766中不同实际中点的五链扇如何被同一packet耦合。先给固定实际点的强迫引理，再谈人口或charging；不只重排已有标量。

## 10. 最后代入当前参数

代入a=16、b=25，已有研究链仍为
\[
N_{\rm sig}(7,5,7)\le40,\qquad C\le50,\qquad Q\le80,\qquad N_{\rm sig}(7,7,7)\le81.
\]
本轮新全局数值改善为零。b25的既有接受状态单列，其余含未独立接受结构依赖的链不能统一标成已接受。

proper cut子类界仍为\(\max(32,16+25+5)=46\)，第6节没有把46推广到一般766或767。定理E在n=7给的是\(P_R(x,s)+P_B(x,t)\le6\)，不能将常数6解释为人口节省。

若将来完整证明Δ=3，或独立证明Δ=2且A1残余修复ε=1，才得到Q≤77、777≤78；这些仅为条件性收益。若A2独立给z=2也得到77/78，但不能再叠加C的下降。本轮没有证明这些前提。

尚缺的核心数学步骤已精确收缩为：在同一完整近极值配置中，为什么定理E保留下来的实际蓝可达性缺口不能全部同时存在，或者这些缺口为何必产生一个容量更低的实际分解。仅有共同预算、端点约束或空族标签都不能替代这一进入定理。

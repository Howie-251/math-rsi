# N(7,r,s)：全缺额联合定理与一次下降多单位的结构入口

日期：2026-10-27。状态：**新增研究结论，未独立审阅／未正式接受**。主会话负责数学推导与针对性自核；Astra子代理参与生成与源码逐构造子核查，不充当独立审阅。native Sol/high只实施固定证据检查及忠实转写。以下新定理未独立审阅、未正式接受；旧稿、失败回执、接受状态和长期任务状态保持。本轮无Claude重试。

本轮实际完成两项结构进展：把Joint17迁移为任意规模完整signotope的端点联合定理；由它与反序版本推导覆盖全部缺额的总through不等式。另完整证明同一前缀与同一尾共用neutral预算的入口。它们没有排除48点，不能报C≤47；Closure完整来源和proof仍缺，C≤49也尚未闭合。新的数学目标直接设为排除48点，从C≤50争取C≤47；不把只排除一个取等角当作最终目标。

## 1. 定义、依赖及本轮证据

N_sig(n,r,s)是完整有序rank-3 signotope中同时禁B_r、R_s、weak n的最大规模；不是forcing threshold。蓝B、红R，路径长度为点数；weak n为同一对外端点的异色路径长度和n+2。四点packet至多一次变色。单色路径任意子序列仍同色。

固定无B6/R6/weak7的完整X。S_R,S_B,E_R,E_B均为X中的实际五链源/末点集合；t_R=|S_R∩E_R|，t_B=|S_B∩E_B|。所有ambient秩都在X中计算，任何诱导核心的内部路径另行重算。b表示有效N_sig(7,5,6)容量上界；数值代入前不固定b。

本轮Joint17固定公式已完成完整strict-RUP：59479源行、102563添加步骤、5166479严格提示，最终空子句，PASS。CNF SHA为9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467，与旧逐行Valid/literal集合/字典绑定一致。新proof回执补的是旧proof_verified=false之后的证据边，不修改旧文件。Closure固定schema检查也完成，但不等于Closure实际CNF或UNSAT验证。文末另列工程状态。

## 2. 任意规模的Joint17端点定理

**定理J（新完成的完整signotope迁移，计算机辅助）。** 任意上述X，令N0=X∖(E_R∪E_B)，U=E_R∩E_B，则

\[
\min\{|N0|,|U|\}\le16.
\]

反序同时给

\[
\min\{|X\setminus(S_R\cup S_B)|,|S_R\cap S_B|\}\le16.
\]

不要求50点、满源核、零缺额或几何可实现性；本轮不认领公开几何Joint17的原创。

**证明：选点与状态。** 反设两集合各至少17点。对u<v，记ell(u,v)=(r(u,v)−1,b(u,v)−1)，r/b为终于实际末对(u,v)的最长同色路径长度。D(v)为全部入对标签的下闭集。无两色六链给D(v)⊆[1,4]^2；v∈E_R当且仅当(4,1)∈D(v)，v∈E_B当且仅当(1,4)∈D(v)。因此N0状态落在20个3×3 low ideals中，U状态落在同时含两角的20个high ideals中，正是公开目录的两半。

u<v时ell(u,v)∈D(v)\D(u)：若属于D(u)，某个w<u的入对标签同时支配它；χ(w,u,v)所在颜色的实际链追加v使该坐标严格增加，矛盾。因此实际状态单射，状态包含与真实点序相容。全配置最早两点都属于N0，状态为空和{(1,1)}。选N0的17点时保留这两点，另选U的17点；按状态唯一命名34个active names。

给全部40名字选一次共同严格次序，同时保留状态严格包含和active owner的真实次序。所加关系无环：纯严格包含边不能成环；包含路径连接两个active名时也迫实际次序一致，故混合环同样不可能。取线性扩张。inactive owner任意，涉及其真实路径的使用均有active guards。变量解释为同一X中的实际颜色、pair标签、路径和计数。路径内部点允许不在34个选点内，绝不改用34点诱导秩。

**NamedRules的13种构造子。** 以下在全部guard为真时证明结论；有假guard时蕴含子句自动成立。

1. order：共同严格次序传递。
2. pairActive：真实Pair的定义包含两端active。
3. pairOrder：真实Pair包含两端严格依序。
4. pairChoice：真实ell(u,v)属于状态差；Valid要求候选列表覆盖这个完整差集，所以有一个pair literal为真。
5. pairUnique：同一实际末对的两个最长长度唯一。
6. firstPair：空状态只能属于全配置第一点，终于以它为末前点的路径长度为2，标签(1,1)；单格状态只能属于第二点，相应长度至多3，两坐标≤2。这里是ambient最早两点，不是选集的前两点。
7. forward：在真实末对(i,j)、(j,k)与正确转向颜色下，将达到第一标签相应坐标的链接上k，第二标签对应坐标严格增大；Valid所指非增长情形矛盾。
8. endpoint：忘掉真实路径的末前点限制，保留同一首末点。
9. pathActive：NamedPath定义要求首点、末前点、末点均active，全部slot成立。
10. pathOrder：真实路径给首点<末前点<末点。
11. base：三个有序active实际点及其正确颜色给真实三点路径。
12. growth：真实k链止于(h,i)，i<j且χ(h,i,j)同色，追加j得到k+1链；若达到6即违反禁形，故相应真guard不可能出现。
13. polygon：同首末点异色链长度a,b≥2且a+b=9正是weak7，矛盾。

base/growth调用的PathAllowed剪枝不会删去真实路径：真实点序与状态差保证各必要次序；无六链给长度3…5；删去末点给终于末前点i的k−1链，故k≤该色maxLength(i)+1；原链给k≤该色maxLength(j)。maxLength由同一ambient downset相应最大坐标加1给出。这些证明不使用所选低点为双源，也不使用外部五链延伸。

**JointRules其余构造子。** named由上述13项覆盖。packet：在active和真实次序guard下，完整四点packet首尾两项同色迫其中间项同色；目录编号不替代实际owner次序。counter：列表已有active计数c，新增项d∈{0,1}，新计数c+d；四个子句正是c+d≥k蕴含(c≥k或c≥k−1)、蕴含(c≥k或d=1)，以及两条反向充分条件c≥k、或c≥k−1且d=1。Valid保证k≥1；重复项按列表重数计数，递推仍真。population：两侧各恰选17，故至少17且不至少18。mandatory：只要求名字0、1，已保留其真实前两点。

因此同一真实赋值满足所有Valid schema。旧固定行绑定把59479条实际CNF行逐条识别为这些子句；本轮同一CNF的strict-RUP最终空子句证明它们不能同时满足，矛盾。反序保持packet和weak禁形并交换源末角色，得到第二式。这里使用literal集合相等保留子句语义，不声称源行字面顺序相等。证毕。

来源：[ES7JointRules.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7JointRules.lean)、[ES7NamedRules.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7NamedRules.lean)、[ES7NamedGeometry.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7NamedGeometry.lean)、[ES7NamedVariables.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7NamedVariables.lean)、[ES7NamedPacket.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7NamedPacket.lean)、[ES7JointCatalog.lean](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/inputs/ES7JointCatalog.lean)，以及[旧joint17_binding/result.json](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json)与[本轮joint17/result.json](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json)。

## 3. 全缺额联合through不等式：先公式再数字

写M=|X|=2b−δ，定义a_R=b−|S_R|、a_B=b−|S_B|、e_R=b−|E_R|、e_B=b−|E_B|。

先证明0≤a_R,a_B,e_R,e_B≤δ。S_R内部不能有蓝五：将其末点与从该点开始的真实红五连接，桥接三元组任一颜色均迫某条六链；故|S_R|≤b。X\S_R无内部红五，换色应用b得到|X\S_R|≤b，故|S_R|≥M−b=b−δ。其余角色换色或反序同理，也得到δ≥0。相同桥接证明S_R∩E_B=S_B∩E_R=∅。

令

\[
Z_1=X\setminus(S_R\cup E_B),\quad Z_2=X\setminus(S_B\cup E_R),\quad z_i=|Z_i|.
\]

由实际不交并，正确恒等式为

\[
\boxed{z_1=a_R+e_B-\delta,\qquad z_2=a_B+e_R-\delta.}
\]

所以0≤z_i≤δ。特别注意：这里是减δ；不能写成a_R+e_B+z_1=δ。例如49点两角色各24时a=e=z=1。

记A=a_R+a_B，E=e_R+e_B，L=S_R∩S_B，U=E_R∩E_B，q=|Z_1∩Z_2|，x_+=max(x,0)。定理J与反序版本给

\[
\boxed{|U|\le16+(\delta-E)_+,\qquad |L|\le16+(\delta-A)_+.}
\]

证明：|X∖(E_R∪E_B)|−|U|=E−δ，故min(|U|,|U|+E−δ)≤16，等价第一式；源版本相同。

四个互斥原子L、S_R∩E_R、S_B∩E_B、U的补集恰为Z_1∪Z_2。因此

\[
t_R+t_B=2b-\delta-|L|-|U|-z_1-z_2+q.
\]

代入上式及z_1+z_2=A+E−2δ，得到

\[
\boxed{t_R+t_B\ge2b-32-\delta-(A-\delta)_+-(E-\delta)_++q.}
\tag{T}
\]

由于A,E≤2δ，进一步有

\[
\boxed{t_R+t_B\ge2b-32-3\delta.}
\tag{T'}
\]

这是同一X的联合约束；两份反证选点不需同时被选中，因为两个普遍定理已经分别对该X成立。

还可保留真实异常点。令ell=|S_R∩Z_2|，eta=|E_R∩Z_1|，则

\[
|L|=b-a_R-t_R-\ell,\quad |U|=b-e_R-t_R-\eta,
\]

\[
\ell\le a_B+e_R-\delta,\quad\eta\le a_R+e_B-\delta.
\]

故

\[
t_R\ge\max\{0,\ b-a_R-16-(\delta-A)_+-\ell,\ b-e_R-16-(\delta-E)_+-\eta\}.
\]

消去异常人口可写为

\[
t_R\ge\max\{0,\ b-16-\min[e_R+(A-\delta)_+,\ a_R+(E-\delta)_+]\}.
\]

换色给t_B版本。以上均由真实不交分割推出，没有为共享点重复收费。

**最后代入b=25。** δ=0、1、2对应50、49、48点，(T')给总through至少18、15、12；此前把两份最坏单色下界相加仅得18、14、10。新收益是在49、48点中分别增加1、2个必需through人口，**不是容量直接下降1、2单位**。已有全类U13给各色through≤13，但这与新下界尚不矛盾。

例如形式人口L=U=16、t_R=t_B=6，另四种单角色各1点，合计48；四源末角色均23，z_1=z_2=2、q=0。它同时满足新Joint界、(T)、U13和所有这些人口等式。这只是形式人口松弛，不是实际signotope构造；它严格说明继续只调这些标量仍不能排48，下一证明必须加入同一颜色对象的packet、核心、前缀和尾的共同实现。

## 4. 统一核心入口与同一前缀、尾的联合预算

以下证明保留一般p≥3和weak n。设X无两色p+1及weak n，b为有效N_sig(n,p,p+1)容量；源末角色改为p链，M=2b−δ。上一节角色界、不交性、z_1/z_2恒等式同样成立。

**定理F。** 令S=S_R。若最早k≥3点为红链，m=p+k−3，且|S|≥m，则取实际最早m点P、h=maxS及其任意一条真实红p出链(h,t_1,…,t_(p−1))，尾集T={t_1,…,t_(p−1)}满足

\[
P\cap E_B=\varnothing,\qquad T\cap S=\varnothing,\qquad P\cap T=\varnothing,
\]

并有

\[
\boxed{|P\setminus S|+|T\setminus E_B|\le z_1=a_R+e_B-\delta\le\delta.}
\tag{F}
\]

证明：任何结束于P的蓝p链完全位于P内，与最早红k点至少交p+k−m=3点；单色路径的三点子序列同色，矛盾。所以P没有蓝p末点。T严格晚于h=maxS，故不在S；|S|≥m又迫h不早于第m点，故P和T不交。于是P\S=P∩Z_1，T\E_B=T∩Z_1，是同一个Z_1的两个不交子集，得到(F)。更精确地，z_1=|P\S|+|T\E_B|+|Z_1∖(P∪T)|。证毕。

条件|S|≥m用于不交，不可省略。结论对h的任意一条完整尾成立，但不同尾之间不能累加费用。

源核中low点S\E_R若不属于S_B，恰好落在S∩Z_2，故其准确坏点数ell≤z_2。不能把Z_1和Z_2说成同一份δ预算；也不能把eta、前缀坏点、尾坏点直接相加，因为eta可能与后两者重合。

**饱和推论。** 若|S_R|=b，则S_R⊔E_B=X：X\E_B无内部蓝p，容量≤b，却包含大小b的S_R，故相等。这不要求M=2b。它解释了原Closure前缀/尾覆盖其实只需饱和源核；但low覆盖还另需S_R∩Z_2为空，不能顺手删除。

**数值后置。** 现在取p=5,b=25，直接考察M=48即δ=2。统一入口为：完整红源核大小23、24或25；low坏点≤2；前缀缺席和尾部非蓝五末点合计≤2；精确联合through下界(T)成立，尤其总through≥12；两色through各≤13。开始仅整体换色一次使实际首三点红，随后重算所有角色。|S|≥23保证k=3、4、5时m=5、6、7的全部不交条件，不需预先选定满25颜色。

这些是所有假想48点模型的强制入口，不是固定见证模板。源核状态仍用ambient X；源核内部路径另在完整S重算。缺额尾若不是E_B，它的ambient状态可能落在核心盒中，与inactive核心名字同状态；不能照搬满50时按状态唯一code给各名字赋key。数学上可在全部名称副本上同时保留严格状态包含和active owner次序，相同状态副本不加包含边；同样的无环论证给不同key。未来编码须保留这个区别。

## 5. 多单位传播公式与下一条主攻目标

沿用已有完整signotope研究稿中的canonical分解Q=N_sig(7,6,7)≤C+D_7、C=N_sig(7,6,6)、D_7≤b+5，以及N_sig(7,7,7)=Q+1。这些依赖仍保持原审阅/接受状态。

**传播命题。** 对整数k≥0，若完整证明不存在2b−k点的balanced配置，则

\[
C\le2b-k-1,\qquad Q\le3b+4-k,\qquad N_{\rm sig}(7,7,7)\le3b+5-k.
\]

证明：三种禁形及完整packet公理都向诱导子集遗传；任何更大balanced配置会含2b−k点反例，故第一式。对任意Q配置，canonical X=H⊔R使H为balanced、R为D_7，故|X|≤(2b−k−1)+(b+5)，得到第二式；第三式使用已证的根归约等式。证毕。传播命题完整，但其“排除2b−k点”前提尚待研究，不能把条件当成果。

现在才代b=25,k=2：主目标直接排除48点，而不是先只排50、再逐点降低。若成功，得到

\[
N_{\rm sig}(7,6,6)\le47,\quad
N_{\rm sig}(7,6,7)\le47+25+5=77,\quad
N_{\rm sig}(7,7,7)\le78.
\]

这是相对于50/80/81研究链的一次三单位改善目标，**本轮尚未证明这些新数值**。无需先逐个排除50和49；遗传性说明完整排48已一并排除更大规模。

最优先的下一数学方向是证明第4节整个δ=2入口不可共同实现：完整23/24/25源核、两种真实neutral集合、同一全尾、初始前缀、全packet和第3节联合through同时约束。先找能在这整个参数族成立的严格共同不等式或结构分类，随后才做数值/有限证书验证。不得固定单尾、删除坏点后沿用父状态、把两个neutral预算相加作同一费用，或只把满25旧Closure重复跑一遍。

第二方向是canonical H–R的总缺额，而不是只盯R30。若未来C≤49闭合，想进一步做到Q≤77，由遗传性只需排完整78点Q配置。其canonical人口只有

\[
(|H|,|R|)=(48,30)\quad\text{或}\quad(49,29).
\]

证明：|H|≤49、|R|≤30且和78，直接枚举两个整数可能。R30的(最大安全子集alpha,最小R6横截tau)必为(25,5)；R29则为(25,4)或(24,5)，因为alpha+tau=|R|、alpha≤25、tau≤5。因此只证明H49/R30角不能完成这个更强目标；新的联合定理必须同时覆盖上述人口及tau/alpha组合。第3—4节全缺额入口可用于H48和H49，不擅自假设B0为空或全尾资源不共享。本轮没有排除这些组合。

Closure证据闭合列为独立收尾工作，目的仅是稳固C49台阶；不得把下载、绑定或计数控制次数记作新的多单位数学收益。N757支线若无向C或D传递的定理，继续降低其数值不进入本轮主目标。

## 6. 一条彻底停止的伪自由度

**命题。** 固定点序和完整颜色后，R7最小关联对p(x)以及P_±、G、H、R与所选兼容点对线性扩张lambda无关。

证明：固定x，其任意两关联对xy,xz已经由三元组{x,y,z}的红/蓝三链直接比较，所以所有关联对在原偏序中已是一条全链，有唯一最小元素。任何线性扩张都保留此最小元素，p(x)固定。P_±由p和点序决定，G在固定诱导P_+内部按真实路径定义，故H/R及其全部内部路径也固定。等价地，不可比的两点对必顶点不交，合法相邻交换不会改变任一顶点关联对的内部次序。证毕。

因此不再尝试“换lambda挑一个更好的canonical分解”；这项优化没有实际搜索空间。若要换分解，须证明新的合法构造；径向chart又不自动保持短色帽，不能沿用lambda名义绕过此问题。

## 7. 本轮固定证据检查与范围

| 切片 | 原始结果及精确范围 | 回执 |
|---|---|---|
| Joint17完整来源与strict-RUP | 完整Literal为38,734,663 bytes，SHA 22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a；完整CNF SHA 9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467与旧literal集合/字典绑定相同。原7控制符合预期；一次全proof检查exit0、PASS，59479源行、102563添加步骤、5166479严格提示，最终空子句。不是新SAT求解、Lean编译或独立审查。 | [result.json](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json)、[checker.stdout](../../../../tmp/n7_global_proof_completion_20261027/joint17/checker.stdout)、[transport_receipt.json](../../../../tmp/n7_global_proof_completion_20261027/joint17/transport_receipt.json) |
| Closure固定schema | 190932行schema/Valid/字典检查PASS，12负控制均拒绝、1个明确合成正fixture通过；11个负控制来自实际固定行，1个是缺席sourceAttain的合成schema负控制。sourceForward/sourceAttain/internalBound均明确0行。旧FAIL保持，不倒改其状态。尚不等于实际CNF或UNSAT验证。 | [新result.json](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json)、[旧FAIL](../../../../tmp/balanced49_remaining_hr_20261027/closure_rules/result.json)、[新REPORT.md](../../../../tmp/n7_global_proof_completion_20261027/closure/REPORT.md) |
| Closure指定成员取得 | 按实测速率无法在900秒预算内完成，已受控停止本轮新进程；状态ABORTED_BUDGET_FEASIBILITY。最后checkpoint收到3,145,820 bytes（含头部，约3MiB），partial plain为15,799,377 bytes。完整源身份、实际CNF绑定及proof checker均未完成；后两者dispatch=0。没有重试、续时或其他传输。 | [abort_receipt.json](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json)、[停止前进度](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/acquisition_progress_before_abort.json)、[停止后进度](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/acquisition_progress_after_abort.json)、[transport_receipt.json](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/transport_receipt.json) |
| 保存与旧文件边界 | 新目录保存全部实现、规格与回执；7个保护本地源/旧回执hash均未变。本轮本地接入胶水错误和网络沙箱阻止均发生在远端目录/传输/科学dispatch之前，另有原始记录；主会话授权修复后首次实际接入，各科学切片没有重试。 | [FINAL_ENGINEERING_REPORT.md](../../../../tmp/n7_global_proof_completion_20261027/FINAL_ENGINEERING_REPORT.md)、[outcome.json](../../../../tmp/n7_global_proof_completion_20261027/outcome.json)、[保护源baseline](../../../../tmp/n7_global_proof_completion_20261027/protected_source_baseline.json) |

Joint17的proof为37,141,401 bytes，SHA 967f022d44e230bddff7b1234e93d7bde718230841d03100f0d6fed1b2506e0b；checker报告0.420317秒。Closure规则检查wall为8.693406秒。取得原始进度仍保留STARTED，外层TRANSPORT_COMPLETE只表示返回进程状态和取回部分回执；停止控制另明确记为ABORTED_BUDGET_FEASIBILITY，不能解释为下载完成。完整Literal、closure.cnf、closure.rup均不存在。

数学状态：全类Joint定理及(T)/(F)是本轮新研究结论；C≤49仍缺Closure实际CNF与完整proof，C≤47/Q≤77/N777≤78仅为明确标注的下一目标。没有更新任何接受记录，没有把同族生成协作写成独立审核。本轮未重试上一轮失败的Claude review。

## 8. 来源导航

- [原始综合稿：N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md](N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md)。
- [R7：残余分解与五点横截](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)；[R20：根归约与共同实现](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)。
- [最新BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md](BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md)。
- [旧Joint17实际公式/schema绑定](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json)；[Through14绑定结果](../../../../tmp/balanced49_remaining_hr_20261027/through14_binding/result.json)。
- [本轮Joint17完整proof回执](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json)；[本轮Closure规则回执](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json)；[取得受控停止回执](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json)；[本轮全部工程范围](../../../../tmp/n7_global_proof_completion_20261027/FINAL_ENGINEERING_REPORT.md)。
- [b25的C8正式人工验收](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)。

旧稿中的“Joint17尚未重放”保留历史意义，由本稿的新日期证据补足，不覆盖历史。

# 满25核的内部插入反例与同端点长路径替换障碍

日期：2026年10月28日。**没有新全局上界；全部新增数学仍unreviewed/unaccepted。** 数学定义、证明与作用域由主会话提供并自核；指定native gpt-6.1-sol/high执行者忠实转写并在权威Linux完成一次冻结的有限一致性核查。生成协作、主会话读源码自核、工程检查及有限枚举均不是独立数学审阅，不改变既有接受状态。

**0. 核心结论与准确增量**

本轮给出两个完整构造。第一，在实际七点模型和b25下，即使一个756核真正满25，所选覆盖又同时global最优、lex最优，该覆盖的外角色点仍可只有内部私人蓝五见证，不能被免费端点化。第二，对任意整数p≥5、n≥p+2，可有两条具有相同实际端点的最长红(p+1)路径，必须一次换完p−1个内部点，无法经过任意更小步长的同端点长红路径链互换。

两个结论分别停止“只靠单满核/global/lex即可普遍端点化”与“只靠同端点即可普遍小步替换长路径”这两个前置机制。第一例不是δ0双满核；第二例不在极小不可满足支持层面。因此它们既没有排除双满核取等类，也没有排除真正的support消交叉，更没有证明C≤49。

第一例底层25点构造已经出现在[R22 §3.4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>)，经典join及25点多目录在[R23](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)继续使用。本轮新增是加第五个T点进入766，并把完整插入族、实际满核和global/lex最优覆盖放在同一母体中认证；不把旧25构造全部重新计为新成果。

**1. 模型、来源与当前证据层级**

N_sig(n,r,s)是完整有序rank-3 signotope中，避免蓝r路径、红s路径及weak n的最大规模。路径长度计顶点；四点a<b<c<d的packet顺序为abc、abd、acd、bcd，至多一次变色。weak n由同一对实际首末端点的异色路径组成，长度和为n+2；不加内部点不交条件。较长路径可保端点缩短。所有诱导核的路径、秩和状态都在内部重算，不能运输ambient状态。

令a、b分别为747、756的有效工作上界，C=N_sig(7,6,6)、Q=N_sig(7,6,7)、F=N_sig(7,7,7)。先保留结构关系

\[
N_{757}\le a+b-1,\qquad C\le2b,\qquad Q\le C+b+5,\qquad F=Q+1.
\]

再代入a=16、b=25，得到沿用的40/50/80/81草稿链。覆盖增广、canonical残余和根归约分别沿[R5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>)、[R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)、[R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)的原有证明与范围；不把数学草稿等同已接受证明。

[C8正式接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)明确C1–C10均已由用户人工接受，限定模型内N_sig(7,5,6)≤25，保证标记仍same-family/provisional；精确reviewer backend与实际effort不可核实。此上界证书不承担25点存在性，后者由完整构造另证。后续结构草稿没有随之被独立接受。

[Joint17结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)只给指定固定公式的strict-RUP重放PASS。[Closure规则结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)虽然为PASS，却仍有actual_cnf_equality_checked=false、UNSAT_checked=false；[获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)为ABORTED_BUDGET_FEASIBILITY，source_acquisition_complete=false、CNF_binding=false、solver_invocations=0、proof_checker_invocations=0。故不能使用C49。本轮读取原始证据没有发现改变这一状态的材料，也没有重启来源获取或证明重放。

本轮参考[综合报告](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261028/synthesis.md>)及原稿入口：[近容量与双向搬移](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>)、[lex覆盖与联合成本](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>)、[最优交叠与完整交换](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)、[源核尾区间](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md>)、[空锁普适性](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_EMPTY_LOCK_UNIVERSALITY_AND_OPERATION_LIMITS_20261028.md>)以及[R12共同实现与区间容量](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md>)。这些来源按各自的原范围使用，不能只引用综合来替代承重构造。

**2. δ0主线的证明尝试、首次断点与方法审计**

在766母体X内，取不交实际角色U、V分别横截全部R5、B5，并在所有合法角色对中最大化unused大小ρ。令A=X∖V、B=X∖U、W=X∖(U∪V)，d_A=b−|A|、d_B=b−|B|、δ=2b−|X|，则

\[
d_A+d_B+\rho=\delta.
\]

δ0只推出ρ=d_A=d_B=0，此时A=U、B=V，各有25点。每个a∈A的私人红五恰由a和B中四点组成，每个b∈B的私人蓝五恰由b和A中四点组成。这是包含极小性已经保证的完整私人路径事实，不登记为新引理，也不能把普通最小性改名为近容量信息。

首次断点在于：这些实际供应尚未被证明共享端点，完整覆盖增广也尚未被证明存在。同端R5与B4的长度和为9，确实禁止weak7，但只有两条路径的实际端点真正相同时才能使用，不能把各自的极值或不同供应者拼成同一pair。

本轮曾尝试把“满核”转为“每个插入点均可端点化”，以接入R5点对机制。第4段反例排除了只靠单满核、global最优和lex最优的版本。它没有证明δ0版本为假，不能删去其双满条件。两路线不共用尚未证明的交换引理，不双收费，不把source-tail定理迁移到任意最优核，也不预设ordinary目录。

| 审计项 | 满25核内部插入反例 | 同端点路径替换反例 |
|---|---|---|
| packet | 完整全三元定义，逐四点包类型证明 | 完整全三元定义，逐四点包类型证明 |
| weak | 全部实际端点类别的两色长度和≤8 | 一般参数全部实际端点类别的和≤n+1 |
| 容量信息 | 真实25点核且使用b25；δ=24，不是near50 | 无近容量前提 |
| 新排除的命题 | 七点单满核/global/lex蕴含普遍端点化 | 同端点长路径可任意小步互换 |
| 没有排除的对象 | δ0双满核；存在一个好最优选择 | 极小不可满足支持族的真正消交叉 |

据此停止继续扩展这两个已经被否定的普遍机制。

**3. 路径遗传、经典join与容量工具**

在packet条件下，单色路径的连续三元定义等价于全三元同色。全三元同色显然推出连续三元同色。反向对长度m归纳，前m−1与后m−1的全部三元均同色c。唯一未覆盖的三元含原首末点x1、xm；对任一内部xi，再选另一个内部xj（m≥4），四点包x1、min(xi,xj)、max(xi,xj)、xm的首项和末项已为c，至多一次变色迫中间两项也为c。m≤3直接成立。因此所有三元同色，任意子序列保持，不因“不相邻”而逃逸。此工具沿[R23 §2.1](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)使用。

记经典构造F(a,b)的蓝最大为a、红最大为b。F(2,b)为全红b点，F(a,2)为全蓝a点；a,b≥3时

\[
F(a,b)=F(a-1,b)\oplus F(a,b-1),\qquad
|F(a,b)|=\binom{a+b-2}{a-1}.
\]

正join左块在前，UUV取蓝、UVV取红。递归四包与路径分类给出上述两色最大值及大小；F(3,5)有15点，F(3,3)有6点，F(3,4)达到10点。该经典工具已在[R22 §3.4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>)、[R23 §2.2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)使用。

下面只需经典杯帽容量：无蓝4、红5的完整signotope至多10点。为自足，令f(r,s)为无蓝r、红s的最大规模，取蓝(r−1)路径末点集合E。补集无蓝(r−1)；E无红(s−1)，否则把其首点接入结束于该点的蓝(r−1)路径，检查两条实际路径相邻的桥三元色：蓝则延蓝，红则延红，违反原帽。因此

\[
f(r,s)\le f(r-1,s)+f(r,s-1),\qquad
f(3,s)=s-1,\qquad f(r,3)=r-1,
\]

递推得f(4,5)≤10，而F(3,4)达到10。此经典上界不使用weak条件；不能把F的最大长度参数和f的禁止长度参数混写。

**4. 主反例：实际七点模型、满25核与内部私人蓝五**

正文使用1-based编号：U={1,…,15}、T={16,…,20}、V={21,…,26}，U<T<V，记T=(t1,…,t5)。机器CSV/JSON使用0-based编号，正文每个点逐点减1即为机器编号；特别正文t3=18对应机器17，不能混引。

取U=F(3,5)、V=F(3,3)，先形成base=U⊕V。纯base继承其颜色，纯T全蓝；混合base/T三元按中点属于base取蓝、属于T取红。等价的完整三块表为：

| 类型 | UUT | UTT | TTV | TVV | UTV | UUV | UVV |
|---|---|---|---|---|---|---|---|
| 颜色 | B | R | R | B | R | B | R |

配合U、V内部F递归与纯T全蓝，完整决定全部2600个三元组，没有未指定颜色。

逐类核对packet，无需借一般合并定理。以下c为相应U或V内部三元色，任取R/B都合法：

| 四点类型 | packet |
|---|---|
| 全在U或全在V | 继承合法F |
| 3U、1V | cBBB |
| 2U、2V | BBRR |
| 1U、3V | RRRc |
| 4T | BBBB |
| 3T、1U | RRRB |
| 3T、1V | BRRR |
| 2T、2U | BBRR |
| 2T、1U、1V | RRRR |
| 2T、2V | RRBB |
| 1T、3U | cBBB |
| 1T、2U、1V | BBRR |
| 1T、1U、2V | RRRB |
| 1T、3V | BBBc |

所有包至多一次变色。base的蓝最大为4，且蓝四全部跨U|V；红最大为5，全部红五在U。因为跨块蓝路径至多一V加U的蓝链，长度至多3+1；跨块红路径至多一U加V的红链，长度至多1+3。

对混合蓝路径，全三元判据迫使T点只能作至多两个端点，其余为base蓝链。但T连续，若两T包围base点则不可能，故至多一个T，而且base点全在U或全在V。因此混合蓝路径长度至多4。纯base蓝≤4，纯T为五点蓝，于是**X唯一的蓝五恰为T，无蓝六**。混合红路径中的base点只能作至多两个端点；纯T红链至多2，所以混合红≤4。全部X红五仍在U，无红六。这一推导来自完整全三元判据，没有预先假设插入点是端点。

weak7须核对同一实际端点，而非相加全局红蓝最大值。全部端点类别满足：

| 实际端点类型 | (L_R,L_B)上界 | 长度和上界 |
|---|---|---|
| UU | (5,3) | 8 |
| VV | (3,3) | 6 |
| UV | (4,4) | 8 |
| TT | (2,5) | 7 |
| UT或TV | (3,4) | 7 |

故无weak7，X属于766。全局红max5与蓝max5的和10不构成weak：它们不在同一端点pair上。

取x=t3=18、A=X∖{x}。T删后剩全蓝四，混合蓝仍≤4、红≤5，weak禁止遗传，所以A是25点756。结合已接受的工作上界b25，它真正达到容量。X唯一蓝五为T，而x严格在内部，因此向A插x产生的全部蓝五见证恰有一条，且端点见证为0。t2、t4同样；t1、t5则是端点阳性对照。不能误说不存在任何有利的最优选择。

令P为U最左的F(2,5)五点。U∖P=F(3,4)的红最大为4，故P命中全部红五。任何红五横截至少5点：全部红五在U，从U删至多4点仍剩至少11点且无蓝四；若同时无红五，会违反第3段经典容量10。因此红五最小横截恰为5。

取角色U_role=P、V_role={x}，合法且不交。每个合法角色对的红横截至少5、蓝横截至少1，故used≥6；显示角色对达到6，因此

\[
\rho=26-6=20.
\]

P全在x之前，所以I=#{(u,v):u∈U_role,v∈V_role,u>v}=0，已经是global最优族中的lex最优。A有25点；B=X∖P有21点，其内部无红五、蓝≤5，属于756颜色对偶域。两者都内部重算，不运输states。于是

\[
d_A=0,\qquad d_B=4,\qquad \delta=50-26=24,\qquad
d_A+d_B+\rho=0+4+20=24.
\]

这里没有双满核，也没有δ0/1/2。

被精确反驳的全称命题是：**对每个766母体、每个global+lex最优覆盖，若对应756核满25，则该侧每个外角色点的私人蓝五均可选为以它为端点。** 上例否定这一命题。它不否定存在一个好最优覆盖的存在命题，不否定两个核都满且ρ0的特化，更不否定C≤49目标。相对NEAR的旧p3/n5例，本例真正使用七点模型、满25核和同时global/lex最优；底层25构造的既有归属保持。

**5. 参数化竞争构造：同端点长红路径必须整批替换**

取任意整数p≥5、n≥p+2。令X={a}<A<B<{b}，|A|=|B|=p−1。含a或b的三元组一律红；内部三元组若全在A或全在B则红，否则蓝。

内部四点包按4A、3A1B、2A2B、1A3B、4B分别为RRRR、RBBB、BBBB、BBBR、RRRR。只含a的包为RRRc，只含b的包为cRRR，同时含a,b的包全红；内部c任取两色都合法。因此完整packet合法。

一条红路径若内部点至少3，必须全部同块；跨两内部块的红路径至多2个内部点，加a,b后至多4。于是红最大为p+1，全部红(p+1)恰为

\[
P=(a,A,b),\qquad Q=(a,B,b).
\]

蓝路径长度至少3时不能含a或b，每个内部块至多2点，所以蓝最大为4。同一实际端点的两色长度和完整分类为：

| 实际端点类别 | 长度和上界 |
|---|---|
| a,b | p+3 |
| 恰有一个外端 | p+2 |
| 同一内部块 | p+1 |
| 不同内部块 | 6 |

因p≥5、n≥p+2，上表均≤n+1，故无weak n，X属于(n,p+1,p+2)。

固定a,b，把A中k点换成B中k点。若1≤k≤p−2，所得p−1个内部点至少4点且混块，必有蓝三元，不是红(p+1)路径。只有k=p−1整批替换才合法。全X只有P、Q两条长红路径，因此也不存在通过第三条长红路径作更小步骤的绕行。这是一般参数的精确替换批量下界，不只是一份10点模板。

代p=5、n=7，得到10点767，红最大6、蓝最大4；两条R6有共同实际端点。换1、2、3个内部点的全部候选数为

\[
\binom41^2+\binom42^2+\binom43^2=16+36+16=68,
\]

均失败；唯一4-for4完整替换成功。

作用域随证明保留：K={a}、Y=X∖{a}、Z为空是合法分块，Y蓝最大4、红最大p，weak禁止遗传。因此该构造不是极小不可满足路径约束族，不能反驳真正support消交叉，也不能给z下界。它否定的只是仅凭packet、weak和相同端点，先对任意红六路径作普遍小步替换的前置引理。首次断点仍是：尚无能保留全部红六双色命中及蓝五进K约束的支持替换定理；本轮没有把这一断点重新命名为新定理。

**6. 一次Linux有限核查：范围、原始输出与限制**

实现前保存[冻结数学规格](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/MATHEMATICAL_SPEC.md>)和[冻结输入预算](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/INPUT_MANIFEST.json>)，再保存[科学脚本](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/verify_fixed_constructions.py>)及[启动前绑定](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/prelaunch_binding.json>)。规格冻结时传输尚未解决的状态保留在原清单中；随后使用主会话明确指定的原生SSH/PowerShell askpass，同一既有凭据源、主机、账号和认证，无Windows Python、安装或科学执行。

首次预检在建立连接前被沙箱网络权限阻断，保留[初次预检回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/server_preflight.json>)；同一授权传输经权限升级后[预检成功](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/server_preflight_escalated.json>)，主机返回ubun、新目录不存在并创建成功。此前没有科学派发，不把预检权限问题计为科学重试。

唯一科学进程在/data/ktqiu_hdd/math_agent/tmp/n7_full_core_internal_and_path_exchange_20261028运行，解释器为/opt/anaconda3/envs/forktqiu3/bin/python3.12。外部wall180秒、TERM后2秒KILL，内部deadline150秒、CPU175秒、地址空间512MiB，超时规则为UNDECIDED且不重试。Linux进程内py_compile通过；没有SAT、参数搜索、证明重放或独立审阅。

每个对象均重新生成其内部颜色和packet。端点DP按固定起点及末两点状态计算全部可达长度和见证，独立于顶点子集枚举；逐端点、逐颜色、逐长度与完整子集路径族比较。26/25/21/15点对象枚举全部2至6点子集，并由覆盖全部长度的DP排除遗漏长路径；10点及9点枚举全部子集。单点核无2点以上子集，端点表为空。

| 对象 | 三元组 | 四点包 | 子集数 | 红max | 蓝max | 同端两色和max |
|---|---:|---:|---:|---:|---:|---:|
| X26 | 2600 | 14950 | 313885 | 5 | 5 | 8 |
| U15 | 455 | 1365 | 9933 | 5 | 3 | 8 |
| A25_t3 | 2300 | 12650 | 245480 | 5 | 4 | 8 |
| A25_t1 | 2300 | 12650 | 245480 | 5 | 4 | 8 |
| A25_t5 | 2300 | 12650 | 245480 | 5 | 4 | 8 |
| B21 | 1330 | 5985 | 82138 | 4 | 5 | 8 |
| X10 | 120 | 210 | 1013 | 6 | 4 | 8 |
| K1 | 0 | 0 | 0 | 1 | 1 | 0 |
| Y9 | 84 | 126 | 502 | 5 | 4 | 7 |

全部packet通过；X26的红五共206条，全部在U，蓝五恰一条T。U15的全部32768个横截掩码核验得最小5；[主反例结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/full_core_result.json>)保存全部最优掩码及插入证据，t3位置为零基2且端点族空，t1/t5分别位置0/4并有端点见证。有限核查只对t1、t3、t5重算25点核，不把纸面t2/t4结论说成另行执行。

[路径替换结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/path_exchange_result.json>)记录两条R6及合法K1/Y9分块；[全部69个候选](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/all_path_exchange_candidates.json>)逐一保存68个失败候选及其首个非红三元，以及唯一完整替换成功。没有抽样或隐藏未通过分支。

完整颜色、所有四点包和路径证据分别见：X26的[颜色CSV](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X26_colors.csv>)、[packet CSV](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X26_packets.csv>)、[全部路径族](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X26_paths.json>)、[实际端点全部长度与见证](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X26_endpoint_paths.json>)；X10的[颜色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X10_colors.csv>)、[packet](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X10_packets.csv>)、[路径族](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X10_paths.json>)、[端点证据](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/X10_endpoint_paths.json>)。其余诱导核同目录以A25_t1、A25_t3、A25_t5、B21、U15、partition_K1、partition_Y9为前缀保存全部同类输出；[U15所有掩码CSV](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/U15_all_transversal_masks.csv>)完整保留。

[原始result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/result.json>)为FINITE_CONSISTENCY_PASS_UNREVIEWED_UNACCEPTED；内部elapsed为4.07140272698598秒，峰值RSS19456KiB。[科学命令回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/scientific_execution.json>)exit0，SSH派发至回收用时7.1385773秒；[stdout](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/scientific.stdout>)与result字节一致，[stderr](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/scientific.stderr>)为空。[工程报告](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_core_internal_and_path_exchange_20261028/ENGINEERING_REPORT.md>)不构成独立数学审阅。

脚本SHA256为a8ac54fa6eef4b0b1220910aa4e042d32268312816453b7e0816cf63e4e548e0；result SHA256为bb430cd6815058aaa5cf9191ade260d71487791069b93b9e90c546294da61309。数学的一般参数证明不依赖从p5/n7有限核查向外推广。

**7. 停止条件与唯一未解决的承重问题**

[.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>)仍明确“Both project MCP routes disabled; review-runtime activated=false.”；本轮未调用、未激活或重试独立Claude路线，也没有模型或服务回退。生成子代理不是独审，Sol工程和有限检查不是独审，主会话读取源码作本会话自核也不是独审。新增证明仍unreviewed/unaccepted。旧稿、综合、接受状态、运行、证明、traces和任务指针均未由本轮修改。

停止两项机制：无需双满条件的普遍端点化；仅凭同端点的普遍≤3点路径交换。本轮对δ0主线只排除了一个错误的弱化入口，**没有取得双满核取等类本身的新排除**。继续扩大小例家族会重返局部优化，应在这两个已否定命题处停下。

只保留一个下一步承重问题：在同一个假想766的50点母体中，两个实际25点核、ρ0及完整多外点路径族能否共同实现？必须证明直接同实际端点冲突，或经全部路径认证的unused增广；不能再削弱成单满核或任意小路径对问题。本轮没有解决该问题，不另提出标签、路线或条件扣减数字。全局界40/50/80/81保持。

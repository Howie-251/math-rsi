# N7：全类残余路线审计与不交红六的完整反例

日期：2026-10-27。当前任务继续保持 in_progress。本轮完成的是一个完整模型反例，以及据此作出的路线裁剪；没有得到新的全局上界。数学推导和路线选择由主会话 Astra 提供，Astra 生成协作不充当独立审阅；显式 native gpt-6.1-sol/high 子代理在权威 Linux 环境实现并执行预先规定的有限检查，随后忠实记录正文。请求的模型/effort 与未独立报告的实际 backend/effort 分开记录。

全部新增数学和计算反例均为 unreviewed / unaccepted；完整语义核验通过不等于独立审阅或正式接受。已有 b 的接受范围和 assurance 保持原样。独立审阅未运行：仓库 [.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>) 明确写有“Both project MCP routes disabled; review-runtime activated=false”，并禁止未获新授权时重新激活或改动 fixed-wire。没有改用同族代理作 reviewer，也没有重试失败的审阅服务。

## 1. 模型、原始材料与本轮路线选择

N_sig(n,r,s) 是完整有序 rank-3 signotope 中，同时避免蓝 r 点链、红 s 点链及 weak n 的最大规模。四点 packet 按 abc,abd,acd,bcd 顺序至多一次变色。路径按点数；weak n 的异色路径共享实际左右端点、长度和 n+2。全文实际路径均包括所有替代、混合及多外点路径，不继承被删母配置的内部秩。

记 a、b 分别为 N_sig(7,4,7)、N_sig(7,5,6) 的有效上界，C=N_sig(7,6,6)，Q=N_sig(7,6,7)。D_7 是完整配置类的最大规模，该类无蓝五、无 weak7，且内部 End_R5∩Src_B4=∅。同一符号 R∈D_7 表示属于此类，D_7 在数值式中表示其最大规模。

本轮首先沿 [N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)、[N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md>)、[RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)（下称 R7）、[RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)（R20）、[BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>) 读取，再回到 R7 §§1–5.2、R20 §§5–6，以及 [D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>) §§4–6、[D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md>) §§3–6 的原始证明和反例。状态方向使用 [RESTART_SETTING_ANALYSIS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md>) §§1–2、[state/cardinality-layer-theorem.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md>)、[state/methods-and-results-20260913.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/methods-and-results-20260913.md>) §§4.1–4.5 的原始定义与审计记录。旧文稿中的历史数值不作为当前新上界。

先比较两个具体机制，而非只比较目标不等式：

| 路线 | 可审计的中间机制 | 当前证据与决定 |
|---|---|---|
| 同一配置联合损失 | 残余全部红六的交叠/横截结构能否提供全局交换入口 | 已有完整 D11、D15 负对照，且“存在两条不交红六”具有精确十二点入口；本轮选择这一可迅速证伪的入口命题深入 |
| 766 整体 charging | 用实际 attained corners 构造关联，再把关联资源无重复地转为缺失普通状态 | 实际点对层的匹配容易成立，但还没有到缺失状态层的非平凡关联；直接压成前驱点会重复收费。本轮降级，不展开四十个异常的局部条件 |

本轮考察的候选 P 是：“每个完整 D7 中任意两条实际红六均相交”，即 ν_6(R)≤1。它不是所需缺额式的改写，也不直接蕴含容量改善；它只是潜在的全路径交换机制入口。已有 D11 的 ν=1、τ=2 已排除把相交错误地升级为单点横截或 ν=τ。本轮在进入容量推理之前先检验 P。结果为假，之后停止该分支，不追加例外条件，也不顺势启动 ν≤2 等新阈值搜索。

## 2. 深入前的七项局部最优审计

1. **完整覆盖。** P 的量词是全部完整 D7。任意反例中的两条不交红六恰有十二点，诱导并集仍属于 D7，故有限入口不漏其他规模或交织。证明见第3节。
2. **同一母配置。** 两条指定路径、所有混合路径、packet、weak 和 junction 均由同一个完整颜色函数决定。selector 只表示真实颜色的合取，不将独立可满足的接口拼接。
3. **严格损失来源。** P 本身尚不提供严格损失。若 P 成立，还需独立证明全路径横截/交换如何压低实际容量；本轮没有把潜在入口包装成这一缺失步骤。
4. **共享与补偿。** 模型检查枚举全部替代路径，不把路径数、尾数或端点数当作资源；τ 由完整红六超图计算。由于 P 被完整反例否定，不进入可能重复收费的下一步。
5. **传播。** 只有进一步得到全类 τ=t⇒α≤b−f(t)，或同一 X 的合法三块分割，才能按第8节传播到 Q。P 没有独立的数值出口。
6. **是否重命名。** P 是具体的、独立于 a,b 的路径交叠性质，确实可被完整模型证伪；并非 d_H+d_Y 目标的等价改写。
7. **旧反例。** 已有 D11 的 τ2/ν1 和解析 D15 的 τ1/ν1 都未否定 P；它们却已否定若干更强横截推断。新的 D12 现在直接否定 P，并可嵌入 canonical 母配置。只添加“canonical”不能修复它。

## 3. 精确有限入口与全部路径域

### 3.1 子链闭包及 weak 的完整枚举

四点 packet 的首尾项同色时，四项全同色。因此从任意单色路径删去一个内点后，新出现的连续三元组仍同色：它们分别处于删除点左右的原连续四点 packet 中。边界删除同理，三点缩为两点时条件为空。反复删除得到：单色路径的任意子序列仍单色，等价地其全部三元组同色。这是已有基础事实，不计作本轮新容量定理。

若两条异色路径共享左右端点 s<t，还共享一个内点 z，则子链闭包使 (s,z,t) 同时为红和蓝，矛盾。因此实际异色同端点路径自动没有共同内点，无须额外假设。

于是 weak7 的两路径总长为9时，其并集恰有7点。对每个七点集，固定极小/极大为共同端点，将五个内点以全部 2^5 种方式分给红路径和蓝路径，便精确枚举所有 weak7，包括一条路径仅有两点的情形。枚举不遗漏共享内点情形，因为该情形已被 packet 证明不可能。

### 3.2 十二点进入定理

存在完整 D7 违反 P，当且仅当存在十二点完整 D7，其点集可分为两条红六。

正向：取违反 P 的两条不交红六 A、B，限制到 A∪B。packet、no蓝五、no weak7 都遗传；若诱导子集内出现 End_R5∩Src_B4，同样的两条实际路径在原 R 中也存在，矛盾。两条红六保留，点数恰十二。

反向显然。对十二点有序集，把含最小点的一条命名为 A，另一条为 B，全部分法共 C(12,6)/2=462 种；这只是两条同色路径的命名，未固定它们的交织位置。故入口覆盖全部位置和全部大小的原始反例。

此外，指定两条红六已使并集自动无蓝五：任何五点中至少三点同属 A 或 B，这三元组红；蓝五的全部三元组应蓝，矛盾。每条蓝四也必恰取 A、B 各两点。实际实现仍保留 noB5 约束作冗余核查，未用该简化删去任何混合红路径。

### 3.3 固定公式的精确投影

公式有全部 C(12,3)=220 个颜色变量（true=红），及462个分法 selector。逐项如下：

- 每个四点集禁止八种超过一次变色的 packet，共3960条。
- 每个五点集禁止连续三元组全蓝，共792条。
- 每个七点集禁止全红路径，共792条；这项也由 weak7 的红七/蓝二情形保证。
- 每个七点集及其32个内点分配禁止两条同端异色路径同时成立，共25344条。
- 每个八点集禁止其前五点形成红五、后四点形成蓝四（共享第五点），共495条。任何 junction 的红五点在共享点之前、蓝四点在其后，故它恰是这样的八点集，不遗漏其他次序或共享。
- 每个 selector 蕴含指定两条六点链的八个连续三元组全红，共3696条；另加至少一个 selector 为真。

总计682变量、35080条。任意满足赋值的颜色投影属于完整 D7 且有不交红六；反之任意这样的颜色模型可选择其分法 selector，扩展为满足赋值。没有依赖状态松弛、固定尾、预选最小横截或额外模板。这是公式语义证明；实际结果为 SAT，反例的有效性最终还由独立于公式构造器的直接颜色枚举确认。

## 4. 新结果：最小十二点完整反例

**命题。** 存在完整 D7 配置 R_*，|R_*|=12，ν_6(R_*)=2、τ_6(R_*)=2、α_6(R_*)=10。因此 P 为假；含两条不交红六的 D7 的最小点数恰为12。这里“最小”只指该交叠性质的反例规模，不是 D7 的极值规模。

### 4.1 完整颜色定义

点序为0<1<…<11。蓝三元组恰为下列九个不交族，其余全部红：

| 蓝三元组 | 参数范围 | 条数 |
|---|---|---:|
| (i,j,k) | i∈{1,3,4,5}, 7≤j<k≤9 | 12 |
| (1,j,k) | j∈{5,6}, k∈{7,8,9} | 6 |
| (3,j,k) | j∈{4,5,6}, k∈{7,8,9} | 9 |
| (4,j,k) | j∈{5,6}, k∈{7,8,9,10} | 8 |
| (5,6,k) | k∈{7,8,9,10,11} | 5 |
| (1,2,k) | k∈{3,4,5,6,7,8,9} | 7 |
| (0,2,k) | k∈{3,4,5,7} | 4 |
| (0,6,7) | 单个三元组 | 1 |
| (2,6,k) | k∈{7,8} | 2 |

这精确指定54蓝、166红，共220色。完整55行点对分组颜色表及54个蓝三元组清单见 [science/COLOUR_TABLE.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/COLOUR_TABLE.md>)，原始赋值见 [science/sat_colors.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_colors.json>)。表格回读和九族展开分别与原始220色逐项相等，见 [science/colour_table_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/colour_table_result.json>) 与 [science/compression_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/compression_result.json>)。

### 4.2 完整模型的穷尽核验

直接验证器 [science/validate.py](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/validate.py>) 不导入公式构造器。其 mono(P,c) 检查 P 的所有连续三元组，另对每个单色候选交叉核对全部三元组同色。完整有限证明的枚举域为：

| 义务 | 完整枚举次数 | 违规数 |
|---|---:|---:|
| 四点 packet | 495 | 0 |
| 蓝五 | 792 | 0 |
| 红七 | 792 | 0 |
| 同端 weak7 | 25344 | 0 |
| 内部红五末点/蓝四起点 junction | 495 | 0 |

枚举的完备性由第3节证明。它包括全部交织、混合和替代路径；没有只验证 SAT 选出的两条红六。完整返回值见 [science/sat_semantics.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_semantics.json>)。实际最大红/蓝链长分别为6、4，End_R5={5,6,10,11}，Src_B4={1,3,4}，两集合不交。因此该完整颜色确属 D7。这里采用公开的精确有限核验，不声称已经给出495个 packet 的逐型手写证明，更不把 SAT 本身当作域有效性的充分证据。

### 4.3 全部红六、横截和独立集

对全部 C(12,6)=924 个候选枚举，全部18条红六恰为下表（每项按原点序排列）：

| 六点集合族 | 条数 |
|---|---:|
| {0,1,3,4}∪P，P∈{{5,6},{5,11},{6,11},{10,11}} | 4 |
| {0,1,3,x,10,11}，x∈{5,6,7,8,9} | 5 |
| {0,1,4,x,10,11}，x∈{7,8,9} | 3 |
| {0,2,x,9,10,11}，x∈{6,8} | 2 |
| {0,6,8,9,10,11} | 1 |
| {x,7,8,9,10,11}，x∈{0,2,6} | 3 |

六族展开与原始完整列表相等，见 [science/compression_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/compression_result.json>)。特别地，
A={0,1,3,4,5,6}，B={2,7,8,9,10,11}
是两条不交红六，所以 ν≥2、τ≥2。十二点不容纳三条不交六点链，故 ν=2。集合{6,11}命中表中全部18条路径，故 τ≤2，于是 τ=2。

对任意有限路径超图，点集 Y 无红六当且仅当其补集命中全部红六。因此 α=|R|−τ=10。该互补恒等式不用 matroid，也不只针对指定私人路径。直接检查枚举全部最小横截，得到14个，完整列表在语义回执中。

还可由红六列表独立推出 noR7：唯一不含11的红六是 A。若有红七，子链闭包迫使其为 A∪{11}；删去0得到的六点集不在表内，矛盾。两条不交红六至少需要十二点，配合构造得最小反例规模恰十二。命题证毕（其中完整颜色域的验证为计算辅助的有限证明）。

## 5. 旧全类嵌入引理的适用：canonical 不能单独挽救候选

以下是 R7 §5.2 已有引理的重述和本例应用，绝不登记为本轮新定理。

对 n≥6，令 D_n 为无蓝(n−2)、无 weak n，且内部 End_R(n−2)∩Src_B(n−3)=∅ 的完整类。任取非空 R∈D_n，在最右增加 h，所有含 h 的三元组染蓝，则新 X 为 Q_n=N_sig(n,n−1,n) 类，canonical 分解恰为 H={h}、残余 R 原样。

证明：新 packet 为(χ(a,b,c),B,B,B)，旧 packet 不变。含 h 的蓝链删去 h 后在 R 中，所以原链长≤n−2；不含 h 的链继承原约束。R 中的红 n 会与同端蓝二构成 weak n，故不存在；含 h 的红链最多两点。新 weak n 若用 h，则两条链都终于 h，蓝长≤n−2、红长≤2，和≤n<n+2；不用 h 时继承排除。

红三元组 a<b<c 给 ab≺ac≺bc，蓝反向。对 a<b<h 有 bh≺ah≺ab。于是对每个旧 r，rh 小于 r 的全部其他关联点对，p(r)=h；所有 rh 按 r 反序排列，p(h)=max R。单点 R 时直接成立。故 P_+=R、P_-={h}。G 必须在实际诱导 P_+ 中重新计算，恰为 D_n 所禁止的 junction 集，所以 G=∅，H={h}。这些最小关联边已在原偏序中被强制，任何兼容线性扩张都相同。证毕。

将本轮 R_* 扩展为十三点 X_* 后，独立确定性核验得到全部286色合法，715个 packet、1716个蓝六、1716个红七、54912项 weak7 全部无违规。由全部实际三元组计算点对偏序与可达性，确认 p(0),…,p(11)=12、p(12)=11 在每个线性扩张中均被强制，G=∅，H={12}，残余恰 R_*。见 [science/extension_colors.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/extension_colors.json>)、[science/extension_result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/extension_result.json>)、[science/extension_canonical_comparisons.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/extension_canonical_comparisons.json>)。

因此本反例也是一个真实 canonical 残余。它排除“只需来自 canonical 分解便会两两相交”的修补，但 H 仅一点、α仅十点，绝不反驳需要大 H/近满安全核心的联合缺额候选。单根嵌入本身早已说明所有 D_n 都能成为 canonical 残余；新例只把这一旧全类结论应用于新失败机制。

## 6. 两条主线的严格障碍与裁剪

### 6.1 残余末间隙不能代替完整路径横截

R20 §§5.2–5.5 的全类结果继续保留。令 d=2b−|H|，W={v∈R：存在从H到v的ambient红六}，S=R∩Src_R6(X)，U=R\(W∪S)。已有：任何ambient红六的两个外端点不能同时在H；W注入同一H的neutral集合，故|W|≤d；H∪U无红六，故|U|≤d以及|R\S|≤2d。这些结论处理混合内点和非零缺额，但没有证明W或U必须非空，不能把它们加成|W|+|U|≤d。d=0才由H加单点超容量得到每个R点都有完整H红五尾；d>0时，现有通用结论只保证任意d+1点集合B⊂R\W触发从B出发的红六，路径可能用多个B点。因此本轮不把零缺额的逐点干净尾供应无条件推广到全部缺额层。

将每条实际红六最后两点 u<v 之间的全部次序间隙视作一个离散区间。设其最小 cut 刺穿数为 κ_I；区间族自身有 packing/piercing 等价，但它不是红六点超图。

已有完整 D11（[D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>) §5）点序 P5<L5<v，全部红六为 P+v、P+l5、{p}+L。τ=2、ν=1，而全部末间隙共享 l4 与 l5 之间的 cut，κ_I=1。因此 τ≤κ_I 为假。

已有解析 D15（[D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md>) §4.2）点序 P5<a<Q4<F5，七条红六 P+a、a+Q+f_i、a+F 全共享 a，所以 τ=1；末间隙(p5,a)、(q4,f1)、(f4,f5)两两分离，故 κ_I≥3。因此 κ_I≤τ 也为假。此处是解析七路径例；本轮工程控制使用的 minor15 SAT 十路径例是另一个配置，不混用。

R20 的全部尾位置与 neutral 单射仍有效，但若 κ_I 个不交间隙各容纳五个 H 点，所得仅是 5κ_I≤|H| 的人口需求，并非 H 的容量亏损。共享间隙、不同尾的共享点以及非零缺额下没有干净 H 尾的情形仍须保留。故停止从区间数量直接推出横截/缺额的路线，不继续细化没有全类入口的共同 cut 模板。

### 6.2 766 的实际关联对象与收费缺口

本节统一坐标顺序为(蓝,红)，使用 [RESTART_SETTING_ANALYSIS.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md>) 的实际终端对标签 σ(u,v)。D(v) 是所有 σ(u,v),u<v 的下闭包。实际递推保证 σ(u,v)∈D(v)\D(u)，从而 D(v) 两两不同。

在4×4矩形内有70个 down-set。普通状态为空集或包围盒 w+h≤6，共30个；异常盒(3,4)、(4,3)、(4,4)分别有10、10、20种。故 |X|=30+e−m，是精确记账而非新的严格不等式。

一个规范的实际关联是：左侧为 (v,c)，其中 c 是 D(v) 的 maximal corner；右侧为实际点对(u,v)；当且仅当 σ(u,v)=c 时连边。每个最大元必须被某个真实生成元达到，不同角不能由同一实际点对达到，不同 v 的点对也不同。因此这个关联自动有覆盖全部左侧的匹配。

但右侧不是缺失普通状态；该匹配不产生 e 对 m 的任何新收费。更不能把右侧压缩成前驱点 u 并设容量一。一个完整四点反例为 packet BBRR，即 χ123=χ124=B，χ134=χ234=R。实际标签为 σ12=σ13=σ14=(1,1)，σ23=σ24=(2,1)，σ34=(1,2)。D(3)、D(4) 都有角(2,1)，且唯一达到前驱均为2。两个角需求在点对层可分别用23、24，在前驱点层却只有一个邻点，违反容量一的 Hall 条件。四点自动满足本节长链/weak 禁形，packet 合法，故这是完整模型中的资源重复。全部四个状态都是普通状态，所以该例只否定“通用角需求→前驱容量一”的投影，不反驳尚未构造的异常专用关联。

旧756审计还已否定 E431/path5_before_path6→missing G331；只提供 G410 这一个普适缺失无法自动支付多个异常。Qeq 的逐目标可行性是对每个 G 分别存在模型，不能误读为同一个模型占满全部 G；位置标记的假原子数50+m也不能冒充 m。上述都是 [state/methods-and-results-20260913.md](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/methods-and-results-20260913.md>) §§4.1–4.5 的原始障碍，不是本轮重跑。

因此主线二保留研究价值，但降级。重新升级前，必须给出同一实际 X 中“异常需求—缺失普通状态”的明确关联，并对每个异常子族证明带可控 deficiency 的 Hall/覆盖条件。仅完成实际点对层匹配、或逐异常找一个可能缺失状态，不足以启动新的容量结论。本轮未得到任何新的 κ。

### 6.3 路线结论

| 处理 | 方向 | 理由 |
|---|---|---|
| 保留为首选 | 同一母配置的全路径跨块重着色/交换 | 直接作用于实际容量资源，允许全部块同时变化，具有多单位传播出口 |
| 保留但低优先级 | 766 全部异常组对缺失普通状态的覆盖 | 需要补上实际关联和全子族条件，当前没有严格净收费 |
| 停止 | D7 红六两两相交；仅补 canonical 条件 | 本轮完整12点反例及真实 canonical 扩展已否定 |
| 停止作为损失机制 | 最后间隙数直接代替 τ；按路径或尾数收费 | 旧 D11/D15 双向反例及共享资源问题 |
| 降级 | 独立残余函数 f(t) | 仍可有收益，但必须来自整个超图与安全核心的共同机制，不能固定一个最小横截或私人路径族 |
| 低配额，当前不扩张 | proper rootfan cut / 不可分块模板 | 仍缺任意目标配置必然进入的定理 |
| 不单独推进 | 757 单列改进、λ 优化、单点状态补丁 | 尚无向目标传递的新增机制；λ 不改变 canonical 分解；局部条件易丢全类入口 |

## 7. 下一步唯一主候选：完整路径超图的三块重着色

本节是下一轮候选及其已知入口，不把它记为已证改进。

对 n≥6，记 b_n 为 N_sig(n,n−2,n−1) 的有效上界。若一个 Q_n 配置存在删集 Z，使剩余点不交分为 A1、A2、B，其中两个 Ai 都无蓝(n−2)/红(n−1)，B 无蓝(n−1)/红(n−2)，则各块继承 no weak n；颜色交换保证 B 的容量同样至多 b_n。因此 |X|≤3b_n+|Z|。

**已有全类入口（非新容量结果）。** 任取 canonical H⊔R，在完整 R 的红(n−1)路径超图中取横截 T。令 A1=Src_R(n−2)(H)，B=H\A1，A2=R\T，Z=T。A2 属第一类。B 内若有红(n−2)，其首点按定义属于 A1，矛盾；其余约束遗传。若 A1 中有蓝(n−2)路径，末点 v 启动一条 H 内红(n−2)。设蓝链倒数第二点 u、红链第二点 w，则 u<v<w；χ(u,v,w) 若蓝就把蓝链延长为蓝(n−1)，若红就把红链前接 u 变成红(n−1)，均与 H 的平衡禁形矛盾。故 A1 属第一类。证明没有固定替代尾，任取实际供应即可，连接点严格有序且无重复。

对 n=7，已有五点横截保证这类分割能以 |Z|≤5 从任意 Q 配置进入。这只是旧分解的结构化重述，不另算成果。

**待证强命题。** 对每个完整 Q7 配置，存在这种实际三块分割且 |Z|≤2。

它要求证明的是实际诱导块同时避开全部规定路径，比一个总规模不等式更具体。可从上述五点入口研究全路径超图的最小不可重着色障碍：A1、A2 的禁止边为全部蓝五和红六；B 的禁止边为全部红五和蓝六。重分配必须检验整条边，允许改变三个块及全部原横截点；不要求原 R 有两点横截，不假定 matroid 交换，也不只检查单外点路径。

真正缺少的是：当保留三个或更多未分配点时，完整 packet、weak7 和 canonical 共同实现性为何强迫存在一次或一组合法全局交换，或者为何最小失败障碍必产生禁形。不能把“存在使 Z 降到2的交换”当作已证明机制；必须给出实际构造及终止性/阻碍矛盾。若只能固定一种尾、满核类型或特殊顺序才成立，入口便丢失，应停止而不是扩张模板。

七项审计对这个下一候选的答案为：全类入口目前只有 |Z|≤5；所有路径来自同一个 X；严格节省来自实际吸收至少三个原删点；共享和多外点边须由重着色的完整边条件处理，尚未证明；传播是3b+2；三块可分性是比规模界更强的结构要求；现有 D12 小 H 例、单根例和共享尾例未直接否定它，但也没有提供它成立的证据。因此它是有明确全局出口的待证机制方向，不是本轮新上界。

## 8. 一般参数传播及其逻辑等级

已有骨架保持为
N_sig(7,5,7)≤a+b−1，C≤2b，D7≤b+5，Q≤C+D7，N_sig(7,7,7)=Q+1。

对同一 canonical 配置令 α为最大无红六诱导子集大小，τ为全部红六的最小横截数。恒等式 α+τ=|R|，配合 d_H=2b−|H|、d_Y=b−α，给
3b+5−|X|=d_H+d_Y+5−τ。
这仅是记账；本轮没有证明 d_H+d_Y≥(τ−2)_+。

三种独立的条件性出口须分开：

1. **实际三块定理。** 若所有 Q 配置都有第7节分割且 |Z|≤z，则 Q≤3b+z、N_sig(7,7,7)≤3b+z+1。已有入口仅给 z=5；z=2仍待证。
2. **完整残余容量函数。** 若对全部 R∈D7 和 t=τ(R)∈{0,…,5} 证明 α(R)≤b−f(t)，则 D7≤b+max_t(t−f(t))，Q≤C+b+max_t(t−f(t))，N_sig(7,7,7)≤C+b+max_t(t−f(t))+1。函数必须来自实际结构，不得只按所需出口倒写。例 R_* 仅显示 t=2 可以发生，并未控制近满核心，也未给出 f。
3. **766 整体状态覆盖。** 若在同一完整配置中构造异常集 E 到实际缺失普通状态集 M 的关联，且对每个 S⊆E 有 |N(S)|≥|S|−κ，则 deficiency 形式的 Hall 定理给出覆盖至少 e−κ 个异常的匹配，于是 e≤m+κ，C≤30+κ，Q≤30+κ+b+5，N_sig(7,7,7)≤30+κ+b+6。此处只有传播已证明；关联和全子族条件尚缺，不能预设 κ。

新反例不改变上述任一容量常数。旧单根嵌入还能给 D_n+1≤Q_n，但这是旧下界关系，不是本轮上界收益。

## 9. 有限执行、证据绑定及未解决事项

本轮科学目录在 Linux 为 /data/ktqiu_hdd/math_agent/tmp/d7_disjoint_path_mechanism_20261027/，本地完整副本为 D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/。[science/MATHEMATICAL_SPEC.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/MATHEMATICAL_SPEC.md>) 与 [science/INPUT_MANIFEST.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/INPUT_MANIFEST.json>) 在实现前保存，输入身份和预算先于求解。

只启动一次外部 AE_kissat2025_MAB，CPU/wall60秒、AS4GiB、证明输出256MiB，外层90秒、超时TERM后2秒KILL。实际5.470秒返回SAT、exit10；没有续时、回退或旧任务重启。公式682变量、35080条，完整赋值逐条满足；直接颜色验证另在30秒/2GiB预算下通过。之后两次预先规定的确定性重构只校验颜色表、十三点扩展和六/九族压缩，各30秒/2GiB，无新增求解或 proof checker。全部科学代码和计算在权威 Linux 执行。

核心身份：

| 工件 | SHA256 |
|---|---|
| [science/query.cnf](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/query.cnf>) | c60b055e7b6ccd0d03797421ae6fd732dac4a88d819b4fec5b48836e9e82b80d |
| [science/sat_colors.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_colors.json>) | 4e12b069550256aa4e1b936466d652b9ed92badba9619d333a0204d2e6b72e81 |
| [science/sat_semantics.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_semantics.json>) | 28530bd88f4913e4e70e2155ff16a11c28f8d6d75d7b521605f11c452d0c906e |
| [science/extension_colors.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/extension_colors.json>) | 81e7b7ca64b559f675d8afff20f55b94b8d3acde49037b0ffd56f107a5b7ad94 |

[science/binding.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/binding.json>)、[science/variable_ledger.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/variable_ledger.json>)、[science/solver_receipt.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/solver_receipt.json>) 保存公式与命令绑定；[science/EXECUTION_REPORT.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/EXECUTION_REPORT.md>)、[science/RECONSTRUCTION_REPORT.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/RECONSTRUCTION_REPORT.md>) 汇总原始回执。保留的 [query.drat](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/query.drat>) 是 SAT 搜索轨迹，不是 UNSAT 证书，本轮 proof checker 调用数为零。有效反例依靠完整颜色及直接穷尽验证，不靠该轨迹。

控制包括全部16种 packet、全红/全蓝负例、既有 D11 七路径例及 minor15 十路径例。初次准备因本地/服务器 AGENTS 字节不同而在构造公式和求解前停止，失败回执保留。之后完整读取服务器规则，确认 Linux执行、AE路径、运行保护等相关要求一致；分别记录文档身份而不错误要求远端文档副本字节相等。四个科学控制源哈希完全一致。此修正不是科学重试，也未改求解预算。[science/server_instructions.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/server_instructions.json>) 与 [science/ENGINEERING_NOTE.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/ENGINEERING_NOTE.md>) 保存说明。

十三项旧输入/保护对象在本地及服务器分别比较，保持不变；原 CNF、证明、运行、任务元数据、接受和会话指针未修改。本报告本身不执行或批准后续搜索。

| 等级 | 本轮及依赖状态 |
|---|---|
| 已给出完整推导/有限证明，未独立审阅未接受 | 十二点入口、完整 D12 反例、其 τ/ν/α、确定性 canonical 扩展；普通前驱容量一的四点障碍 |
| 旧结果复述，非本轮新成果 | 子链闭包、R7 单根全类嵌入、既有容量骨架、三块五删点入口 |
| 既有接受状态单独保留 | b 的 C1…C10/C8 接受链及原 same-family/provisional assurance；本报告不提升其外延 |
| 条件性结论 | z删点三块、f(t)、κ三条传播公式 |
| 猜想/待证机制 | z=2 的全类重着色；联合缺额；异常到缺失普通状态的全子族覆盖 |
| 已否定 | 全 D7 红六两两相交；其仅添加 canonical 条件的版本 |
| 计算/证明链未决 | Closure 实际完整 CNF 与 proof 尚未闭合，不能使用 C≤49；更不能使用 C≤47。旧大型求解超时保持未决，本轮没有重启 |

Joint17 的严格重放和其全类语义报告沿用各自原状态；Closure 的固定规则检查通过不替代实际完整 CNF/proof。两者都不能被本次文档检查或反例核查升级为新的数学容量界。

## 10. 最后才代入数值

现在代入有效 a=16、b=25，沿已有研究骨架仍得到
\[
N_{\rm sig}(7,5,7)\le16+25-1=40,\qquad C\le2\cdot25=50,
\]
\[
D_7\le25+5=30,\qquad Q\le50+30=80,\qquad N_{\rm sig}(7,7,7)\le81.
\]
这些是以既有结构稿为依赖的研究上界链，不能统一标记为正式接受；b25 的既有接受状态单独保持。本轮真实新增的全局上界改善为零。

仅当下一轮完成全类 z=2 三块定理时，才可得到 Q≤3·25+2=77、N_sig(7,7,7)≤78；这两个数值目前不是结果。状态方向代入 b 后也仍只是 C≤30+κ、Q≤60+κ、N_sig(7,7,7)≤61+κ，κ尚未确定。

本轮的进展标准是一个已完整验证的失败机制反例：它及时关闭“残余全部红六相交”的支线，并确认 canonical 标签本身不能补救。仍缺的核心数学步骤是同一配置中能够兑现严格净收益的全路径交换/不可重着色障碍定理。下一轮只优先这一机制；整体状态覆盖保留为竞争方向，须先找到真正的缺失状态关联再投入计算。

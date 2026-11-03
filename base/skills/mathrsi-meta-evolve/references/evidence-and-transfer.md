# 从研究证据到可执行修改

本参考供 `mathrsi-meta-evolve` 的维护 owner 使用。输入是一项已授权的技能维护任务，以及能定位原件的研究记录；输出是对现有流程或领域知识的具体修改及采用理由。它不启动源项目研究，不把历史 Goal、预算和运行句柄当成本轮授权，也不要求先把整份历史资料逐文件读完。

先明确这次要改变的行为。例如“路线必要门通过后，调用方误把它当实际构造”“修改源图后继续使用旧邻域”“文献比较只查表格，没有代入已知构造族”。沿这一行为找到够用的原始链，开始修改成熟部分；只有未决问题会改变修改时才补读。仓库归档可以完整保留，执行时按义务读取。

DD 在这里是**历史经验来源**。该研究不是使用 MathRSI v1 完成的对照实验，不能把它的成功、耗时或失败归因为 v1，也不能据此报告 v2 已提高解题率。

开发案例的取证入口：

- [数学提炼及首批七条机制](../../../../development/evolution/dd-v2-20261102/intake/DD_MATHEMATICAL_EXTRACTION.md)：完整条件、真实 caller、反例和可执行片段。
- [后续原件审计](../../../../development/evolution/dd-v2-20261102/intake/late/SOURCE_AUDIT_LATE.md)：更晚的修正、D2／仿射／克隆／Lean 链和缺件登记。
- [逐文件阅读账本](../../../../development/evolution/dd-v2-20261102/intake/late/READ_LEDGER.tsv)与[按机制阅读地图](../../../../development/evolution/dd-v2-20261102/intake/late/READING_MAP_BY_FAMILY.tsv)：区分全文、部分阅读、结构解析、精确重复和未读。计数表示阅读覆盖，不是数学质量分数。
- [461 条轨迹索引](../../../../development/evolution/dd-v2-20261102/intake/late/TRAJECTORY_MAP_ALL461.tsv)：定位成功、失败和后继修法；索引本身不替代原证明或代码。
- [ARIS 外层适配底稿](../../../../development/evolution/dd-v2-20261102/intake/ARIS_META_ADAPTATION.md)：原版能力与本次数学适配边界。

以下 `A/...` 表示维护输入中明确给出的 DD 原始交接根下的相对路径。迁移成插件时，把所需原件放入仓内归档并改成相应相对链接；不要把作者机器上的绝对目录写成通用执行入口。本文当前的开发证据链接可直接用于核对这次修改。

## 1. 怎样取到足够的证据并开始写 diff

### 读一条决定链，而不是收集同意意见

从本轮已选问题开始，找出四个连接：当时真正想判断什么；使用什么对象和允许操作；实际得到什么结果；哪一项后继动作因此改变。通常先读一份预测或接口、一份证明／实际代码和结果，再读后继修正。若后继改变了失败的范围，必须回到旧失败的假设检查；一段最新总结不能抹掉旧结论成立的理由。

例如“全局 chart 失败，改逐边 chart 成功”需要知道它释放了什么共同参数，而不是只有两个图阶数。程序声称检查了全域，就读它的枚举／规范化与退出条件；只要一个显式反例已否定待用引理，完整核对那个反例即可，不要求把所有失败搜索重跑。

将证据写进现有维护记录即可，不强制新增固定数量的表。至少使下列问题能被下一位执行者回答：

| 要回答的问题 | 实际应找到的材料 |
| --- | --- |
| 原命题和本次局部命题是否相同？ | 精确量词、参数、允许假设、原输入到局部表示的连接 |
| 程序的成功／失败意味着什么？ | 实际输入、代码谓词、算术／遍历范围、退出状态及其数学方向 |
| 为什么应改变操作？ | 一个具体失败输入、共同约束、遗漏 caller 或后继结果 |
| 什么仍可继承？ | 没变的对象、已证引理及其适用条件；变动处的依赖 |
| 这次修改由谁消费？ | 现有技能中的具体步骤、返回产物、调用方收到后做什么 |

作者报告、模型审阅、独立程序和 Lean 是不同来源。审阅者没执行程序就写静态审阅；只读部分文件就写相应范围。保存原始意见和处置，不能将最后的正面意见倒填为所有早期调用均通过。

### 先分层，再写到已有位置

同一条证据通常同时产生几种内容：

- **Base 行为**：换领域后仍成立的执行动作，例如共同参数必须由同一对象供给、改变输入后检查失效依赖、必要门通过后仍要消费后继义务。落到现有五个 workflow 的具体步骤。
- **领域知识**：有限域、图距离、子空间覆盖、克隆路径、负载公式、具体检查器。进入 DD 插件的技能／参考，写完整条件及实际用法。
- **单题状态**：当前已找到哪些中心、某求解器 UNKNOWN、某图还缺终审、当日公开表值。留在该研究工作区的 wiki 和恢复入口；归档可保存历史版本。
- **不采用或等待证据**：一次网络错误、未验证的泛化、重复已有通用规则、会增加执行负担但没有解决具体缺口的检查。记录拒绝理由即可，不硬写成技能限制。

先阅读准备修改的现有段落。如果 v1 已正确要求这个行为，优先补一个能触发正确操作的例子、领域输入或缺失的返回消费；不要再复制一条“加强验证”。必要的修改可以跨多个文件，但应围绕同一真实缺口，保留原有五流程及其有效接口。

下面五条链可直接用于练习这一判断。

## 2. 链一：覆盖的是共同路线并；满秩只是其中一种工具

### 原始数学与反例

仿射图的顶点为 `(a,x)`，其中 `a` 是控制器顶点，`x∈F_q³`。一条实际 dart 的关系为

```text
(a,x) → (C[a,p], T[a,p] x + t L_reverse(p)),  t∈F_q.
```

无向性要求反向关系是真正的逆；它不是“项目方向看起来相同”。三步路线的目标坐标是固定源坐标的一个中心，加上三个独立噪声参数的线性像。一条路线噪声满秩即可覆盖整个目标 fiber，但图的直径条件只要求**所有允许短路线的并**覆盖目标。不能未经证明把“每一条路线都满秩”设为必要条件。

四端口 frame 的中央商空间中，两组三个方向交于 `k` 个项目点时，前／后回退给 `6−k` 个共线平面，覆盖大小为

```text
q + (6−k)(q²−q).
```

因此原 F5 成功实例不能只换一个更大的域就继续成立。在 F25 的实际反例中，真逆与相关满秩条件仍成立，但相邻层平面并只有 `3625/15625` 个点，漏 `12000` 个目标。这是一项局部代数反例，不是对巨大候选图运行 BFS 后的猜测。

更晚的 D4 源15552还说明相反方向：单条满秩 word 不足以覆盖所有控制器层对，不能因单 word 失败就排除构造。修法对**同一实际源坐标**的路线统一写成

```text
M_w x + c_w + H_w,
```

其中 `H_w` 是该 word 的噪声像。选一个参考中心 `M_r x+c_r` 后，先证明 `im(M_w−M_r)⊆H_w`，再检查相对 coset 的并是否为整个目标空间。这样 `x` 的变化可被吸收进同一 `H_w`，不能为每条路线另选源点或假定它们中心相同。91组 coset 证书补齐了单 rank 路线留下的缺口；六个参考选择失败被保留，没有改写成“任取参考均可”。

另一个真实逆陷阱应随领域案例保存：F11 中项目归一化后的二维逆可满足 `Q_wrong Q=6I₂`。若提升成 `diag(1,Q)`，乘积是 `diag(1,6,6)` 而非 `I₃`。相应原点测试返回错误向量，且不存在噪声补偿。项目方向／秩／平面方向全对，也可能没有正确的无向图。

### 取证与实际修改

原件入口：

```text
A/research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md
A/.../affine_field_conditions/general_ports/DERIVATION_PACKAGE.md
A/.../affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.py
A/.../retained_edge_transfer/published_d15_15552_D4_source_gate/GLOBAL_COSET4_NOTE.md
A/.../retained_edge_transfer/published_d15_15552_D4_source_gate/global_coset4.py
```

维护者读共同覆盖公式、F25失败输入、D4参考中心推导及实际 coset 程序，确认“满秩不足／过强”分别发生在哪一类点对。代码结果不替代 `im(M_w−M_r)⊆H_w` 的证明。完整细节与已读范围见上述数学提炼和后续审计。

可进入 base 的动作是：在 [route-loop](../../mathrsi-route-loop/SKILL.md)／[prove](../../mathrsi-prove/SKILL.md) 中，先写原义务所需的并／交／共同量词，再问现有局部工具是充分条件还是必要条件。局部工具失败后，检查能否由同一对象的多个贡献共同闭合。产物应含共同对象和实际组合式，消费方据此选择“继续组合证明”或“以确证反例否定所需条件”。

DD 插件应保存上述平面计数、路线中心与噪声空间、真逆绑定和失败向量，并给对应程序输入。单题状态则是具体91组、当前采用的参考和未完成形式化。**不采用**“每条路线须满秩”“凡有 rank 证书就不用核相邻层”“所有领域都要做 coset 枚举”等通则。

一个可审阅的修改理由可以写成：

> 当前插件只返回各路线 rank，调用方无法判断共同覆盖；增加同一源坐标下的路线像和并覆盖接口。base 已要求实际输入连接，因此只在 prove 的组合处补充消费例子，不新增全流程阶段。

## 3. 链二：对象变了，哪些旧证明保留，哪些旧失败已越界

### 冻结邻域的正向继承

设有限简单源图 `G` 无孤立点、直径至多 `D≥3`。对任意中心函数 `c:I→V(G)` 增加 clones，每个 clone `i` 只连源图的完整开邻域 `N_G(c(i))`，保留旧边、不加 clone–clone 边。中心函数允许重复，也允许两个中心相邻。

原点对由旧路径继承。clone 到旧点可替换源路径的首边；到自身中心用任一旧邻点走两步。两个不同中心距离至少2时可替换路径两端；相邻中心有 `clone_i–c(j)–c(i)–clone_j` 三步；同中心的 clones 共享旧邻点，两步。这正是 `D≥3` 所需的 pair 分类，不能将定理直接降为 D2。

度数独立记账：旧点 `v` 的增加量是 `{i:v∈N_G(c(i))}` 的重数，clone 的度数为源中心的度数。构造代码必须先冻结源邻域，再修改图。若后继 clone 使用 `current(center)`，前面新加的 clone 会进入该集合，图已不是定理定义的对象。

q4 的 ovoid×spread 中心有匹配边，仍能做到完整开邻域互不交。这是“中心独立”过强的反例；检查负载应看实际邻域交，不是只看中心间有无边。

### 失败证明也有依赖

在 Exoo72 控制器删除相邻两点后，只许 A–B perfect matching 时，一项唯一旧 cross 路线若未直接匹配就无法在三步修好。于是同一边界点需要两条不同新 matching 边，产生矛盾。

若放宽为任意边界 matching，旧“必须直接匹配”论证就不适用：真实路径 `51–59–36–18` 用 A–A 新边修好了旧 cross 点对。后继证明没有否认这个修复，而是重新分类全部边界路线，得到

```text
d_H(s,t)≤3
或 d_H(mate(s),t)≤2
或 d_H(s,mate(t))≤2.
```

由边界独立和 matching 度1，三步内其他新边布局不可能提供更多路线。全部105 perfect matchings 覆盖每个 partial matching 的单调补全；完整排除的是这个固定源、删相邻两点、保留其余边、最大度5的操作，不是一般70点控制器。

对 diagonal-fill 修法也要明确改了什么。它保留 filled 源 `H` 的旧边，但 clone 使用 unfilled `U` 邻域，省去 diagonal clone→filler 连接，再用 hub 接全部 fillers。不能把 hub 错误塌缩到 `H` 继续套旧 clone 证明。较高重数的正确源是实际第一张 `G1`，复制其 first-clones **和 first-hub** 的完整冻结邻域；不是继续复制旧 GQ center。

### 取证与实际修改

原件入口：

```text
A/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean
A/.../retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/PROOF.md
A/.../retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md
A/.../f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md
A/.../f4_c72_nucleus_C4/controller70_general_matching/PROOF.md
```

可进入 base 的动作是：对象／生成规则修改后，沿实际依赖检查已有正结论和负结论。保留满足假设的进口；只重做受影响的连接。要求新方案指出它具体释放了哪一条旧限制，以及旧失败为何不能直接排除它。这个动作可以补到 route-loop 的修法与 prove 的输入接入，不要求整项研究重新准备。

实际落点是 [prove](../../mathrsi-prove/SKILL.md) 写明冻结源与演化对象、返回受影响假设；[route-loop](../../mathrsi-route-loop/SKILL.md) 消费这些变化，决定旧失败是否仍阻断当前候选；[verify](../../mathrsi-verify/SKILL.md) 复用未变源证明，核受影响连接与新顶层声明。每个结果回原义务，不另开一次整题准备。

DD 插件保存 frozen fullN 定理、pair 分类、负载公式、matching 路线反例和 diagonal/G1 对象关系。中心集合、重数、原始图路径和此次旧边编辑留在单题记录。**不采用**“任意改图都要重跑全部根”“旧失败永不失效”“只要改了参数就算新路线”或“中心必须独立”。

实际 diff 应能回答：构造技能在哪里冻结源；验证技能如何确认新点的实际邻域等于该源邻域；改变规则后哪一个定理仍被调用、哪一项假设由新证明供给。只加“注意缓存过期”而不改变这三个调用位置，不能解决本例。

## 4. 链三：基线改变的是研究价值，不是图的合法性

### 被更强公开对象超过的完整成果

F7/C60 构造给20580点、35正则、直径3，生成与独立字面检查均支持其合法性。若只与某个 PolarStar 家族的13272点实例比较，会误判纪录价值。后来读到 Delorme 的适用 q=32 极性图与复制规则，得到已知35度35875点保证，足以否定20580的纪录资格。这没有推翻新图的数学证明。

另一次更具操作性的变化是 q7 partial ovoid。O22 产生的65／70度图已经完整生成、核验和形式化；后来原论文扫描表显示 W(3,7) 已有33点 partial ovoid，表中的43是上界，不能误读为已找到43点。公开 P33×spread50 配合既有复制，给65／70／77度更强保证。旧 O22 两图因此被公开机制超过；尚未生成的 F11/m33 目标175692也被181450保证挡住，停止该竞争目标。之后使用真实 P33 坐标，针对 filled 源得到新的克隆接口；“更强基线”在这里改变了实际源与中心规则。

### 取证与实际修改

原件入口：

```text
A/.../f7_c60_d35/PROOF.md
A/.../f7_c60_d35/PUBLIC_COMPARISON.md
A/.../public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md
A/.../retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/
```

维护者要区分实际发表边表、已知一般定理的合法数值后果、某个家族的实例和“当前最好”的维护表。已知族的代入足以阻断竞争目标，即使没有单独发表该数值边表；它不因此成为全球最优上界。比较条件包括最大度／正则、直径、字段存在性、中心诱导结构和所读版本。

实际入口是 [prepare](../../mathrsi-prepare/SKILL.md) 调用 [survey](../../mathrsi-survey/SKILL.md)：survey 在 LITERATURE.md 中记录明确表值及已知族的合法代入、可复用公开对象和条件；[route-loop](../../mathrsi-route-loop/SKILL.md) 与 [prove](../../mathrsi-prove/SKILL.md) 消费后调整竞争型队列，保留固定目标，或把公开对象接成新源及其待证条件。保留数学合法、独立核验、形式化和优先权各自状态。未定位全文就保存缺口；若它正影响选题，再定点找原文／引用链，而不是把一次查找未获结果写成不存在。

DD 插件保存这些公开构造公式、归属、条件和 source-selection 用法。某日表值、尚未拿到的论文、具体候选 margin 和当前停止点是单题状态。**不采用**“每次推导都完整重做文献调查”“表外参数无人研究”“已被超过的合法图应删除”或“所有查询只能一次且不得修复后重试”。搜索和外部服务依当次任务、工具状况和已授权预算判断；本次历史的单次调用边界不是通用禁令。

对应 diff 的检查重点是下一动作：若基线被提高，技能是否仍机械派发原弱候选？如果当前 v1 已要求增量回文献，新增领域比较实例和返回字段就足够，不另建一个比较 workflow。

## 5. 链四：必要门、UNKNOWN、精确证书与实际构造分别消费

### 三种不同的输出

F4 unique-route matching 门全部通过，只说明局部必要排列有空间；它没有产生共同 chart。后续57600组全局 projective 选择全部失败，释放为150条边各选 chart 后才有实际 SAT 构造。必要门通过应交出后继共同约束，不返回“图已找到”。

106点 D2 源的 internal-S 修法选择10／11个 pins，只允许修改旧图 `G[S]`，新点连 `S`，cross／outside 边冻结。对 mixed 旧点对必须保存原直接边、outside common middle 或选定 internal middle 的确切路线。实际6253 binary 模型唯一限时求解无 incumbent，状态为 UNKNOWN；后继某些对称 pin 子族被严格排除，也不能把这个更大模型改成 NO。

Mizuno13 的块选择则展示另一种后继证据。原数值 MIP 的 infeasible 输出没有独立证明；后来读取共同容量行，给出非负有理 dual 的纯整数核验：364列系数至少10001，共同分母10000，右端2061908，所以整数块数≤206。这关闭的是全部364 source-dependent **affine full27 transverse block** 域，不排 nonlinear／partial blocks 或任意14度图。数值状态保持原样，严格结论来自新的、可检查的证书及模型行的几何必要性。

### 何时已经足够

对存在性目标，一个实际候选满足完整规格就足够，无需把产生它的搜索证明穷尽。对必要域的排除，一个严格矛盾已经关闭该必要域，就无需继续生成图或运行更强检查。Brown91 的 helper 容量探索曾在 B=101 遇到 scalar 上界可行；逐组 excess 不等式进一步迫所有 helper 饱和，helper 度数和75为奇数，解析矛盾已足够。不能因“还有更强 DP 没跑”拒绝这个已闭结论。

原件入口：

```text
A/.../f4_c60_forced_turn_gate/REPORT.md
A/.../f4_c60_global_projective/REPORT.md
A/.../f4_c60_edge_projective/MODEL_CODE.md
A/.../d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md
A/.../d2_record106_edge_repair/internal_pin_rewiring/{run_once.py,RESULT.json}
A/.../mizuno13_clone_interface/source_dependent_geometry/controller213_capacity_gate/lp_exact_bound/
A/.../d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md
```

可进入 base 的行为是：发出探针前说明返回值将改变什么决定；收回后先读实际谓词、范围、退出码／证书，再接当前义务。必要 PASS、sample 未命中、raw solver infeasible、UNKNOWN、实际见证和严格全域 NO 不是同一种布尔结果。已有 exact 证书足够时消费它；只是必要门通过时，明确把剩余条件交给 prove。

落点是 [route-loop](../../mathrsi-route-loop/SKILL.md) 的探针派发／回收与 [prove](../../mathrsi-prove/SKILL.md) 的停止判断。必要门 PASS 返回存活输入和剩余共同约束；UNKNOWN 保留未解状态；已完整验证的见证或覆盖当前必要域的严格矛盾，则关闭对应义务并停止为同一结论继续扩算。

领域插件提供建模等价、饱和目标容量、dual 的数学含义和具体重放入口。某次求解器时长／节点、已使用预算、未完成参数是单题状态。**不采用**“UNKNOWN 后一律停止整个研究”“求解器 infeasible 永不能使用”或“必须所有方法都全域穷尽”。应根据所需证据强度选择数值发现、可检查证书、完整枚举或解析证明，并准确报告它实际承担的用途。

本案例还有真实 portable 限制：Mizuno `verify_exact.py` 依赖的 `LP_INPUT.json` 不在原包内，且会写回源目录。现有 `MODEL.json` 足够在内存重建365行后核 dual；仓内[提炼§13](../../../../development/evolution/dd-v2-20261102/intake/DD_MATHEMATICAL_EXTRACTION.md)给出已核过算术的只读命令。模型行的必要性仍由人读几何证明供给，算术 PASS 不能承担它。

## 6. 链五：Lean 的实际 caller 与表示改变

### 从局部 decoder 到原点对

F4 固定公式图的形式化没有只导出“给定 certificate 则 D3”。其路线如下：

1. `F.ofCode` 解释保存的有限域编码，防止 ring numeral `2=0` 与编码 `2=w` 混淆；实际源、矩阵、方向和逆 port 绑定到图定义。
2. 真逆与方向关系证明 `adj_iff_forward`，所以 symmetrization 没有悄悄增加未计邻点。邻域是 `Fin5×F4` 的像，给最大度≤20。
3. `bounded_walk_of_route` 用三个真实 forward edges 构造 `SimpleGraph.Walk`，前提只是 controller 与 fiber 两个终点等式。
4. 非邻／同层3300对的 decoder 在三个 basis 上检查，再用加法和 F4 scalar 线性提升到所有 displacement；相邻300 darts各64 residual 检查，利用真实 inverse 证明前／后回退具有同一个 direct center。
5. 实际任意 `u,v` caller 减去各自 route center，供给 decoder，闭合两个终点等式。`Diameter` 调用已闭的 `Certificates`，最终定理不留下证书前提。
6. 非D2由具体0→6无一步／两步 forward word，经真实 Walk 分解得出；不是拿一个未连接的 Moore 统计替代原命题。

原图矩阵大表造成核内检查成本时，后继表示将重复矩阵／decoder intern 成小表，但保留原 `graph` 定义，先证明全部300原 dart matrix 等于 compact lookup。60行有限 caller 分模块核验，已通过模块被复用。表示更小不等于命题自动相同；这条 equality bridge 才使复用有效。

原件入口：

```text
A/formal/DegreeDiameter/Portfolio/F4Graph3840{Field,Routes,Linear}.lean
A/formal/DegreeDiameter/Portfolio/F4Graph3840{DecoderInterface,DiameterInterface}.lean
A/formal/DegreeDiameter/Portfolio/F4Graph3840{Certificates,Diameter,Exact,Lower}.lean
A/.../f4_c60_edge_projective/formalization/{CHECKPOINT_C.md,FINAL_COMPILE_RESULT.json}
```

### 能转移的行为和不能转移的结论

可进入 [verify](../../mathrsi-verify/SKILL.md) 的行为是沿实际导出声明回查：载体／编码是什么、开发接口的前提由哪个 caller 供给、如何构造真实目标关系、表示压缩依据什么等式保持原对象。已有局部 kernel PASS 后回原 caller 补输入，不把它当主定理完成，也不重新编译未变的全部 imports。只有对象／证明修改影响相应依赖时才补核。

按 [ARIS 调用约定](../../../../docs/ARIS_REUSE.md) 使用当前宿主 lean-formalize；正式构建前对一个非平凡的真实模块测成本，再安排批量模块。需要压缩时在内核证明新表示等于原定义，保留有效已编译模块；纯 Lean 目标的直接入口见 [lean-target-entry](../../mathrsi-verify/references/lean-target-entry.md)。

DD 插件保留具体 route／decoder／Walk 引理、有限输入表绑定和源码地图。这个 Lean 结果是固定公式图的阶数、最大度、真实 Walk D3及非D2；它没有同时证明 ASCII edge parser 等同、精确20正则和38400边数。外部字面检查可分别承担后者，不能把两种验证合成未实际证明的更强 Lean 声明。旧 source kernel 完成也不自动完成新 clone 图的 load／label／caller。

**不采用**“每个新数学结果必须 Lean”“压缩表无需语义 bridge”“编译成功就完成原题”或“主文件包含相同数字就算输入绑定”。已编译的正确局部引理应保留其价值；它暂时缺 caller 时，准确交回缺口即可。

## 7. 将这些证据变成真实补丁

对准备采用的一条行为变化，按以下顺序工作。直接使用现有维护报告，不为这几步另建调度系统。

**先写原执行方式和观察到的失败。** 引用现有 skill 的具体段落与真实产物。如果还没读到实现，不写“旧版本缺少”；可以写“需要核查当前流程是否已覆盖”。DD 的问题发生在源研究中，不等于已复现 MathRSI v1 的故障。

**接着写目标行为及消费方。** 例如“插件返回同一对象的路线像并与未覆盖 witness；prove 消费它，判断组合证明还是反例”，比“加强共同覆盖意识”具体。若现有输出已有这些材料而父流程未消费，修调用处；若父流程正确但领域知识缺完整定理，补插件。不要因材料来自 DD 就把所有变化都塞进插件。

**实际编辑成熟部分。** 保留五 workflow。把新增条件放在使用处，必要例子和程序输入进领域参考；长证明／原 wiki 进只读归档。通用步骤不要写死某个 field、图阶、作者目录、solver秒数或 reviewer供应商。开发案例可以保留具体数值，因为它们使反例能被检查。

**只核此次改变涉及的命令与接口。** 例如核 `rebuild` 的实际参数和输入依赖，或用保存的 dual 跑纯整数证书。大历史图已具证据且本次未改，不为维护重复 BFS／Lean；命令只是文档示例就如实写未执行。用户要求的实际使用可以由维护 owner 按新技能完成并记录具体行为，不额外制造“无历史 agent”“全材料重读”或固定跨家族层数作为新门。

**回收并决定。** 维护 owner读实际 diff及相关结果，接纳、缩小、拒绝或留下具体待测项。交付时说明“修改了哪个步骤、证据为何支持、核查做了什么、还没测什么”。若一次修法只改善投影指标而未改善实际目标，保存这一结果，不宣称整个研究效率已提高。

最小可消费记录示例：

```text
旧执行位置：mathrsi-prove 已要求实际输入连接；DD 接口只返回独立 rank。
来源：F25相邻pencil反例；D4共同coset补齐；真实逆反例。
决定：base补共同并的消费例子；DD补完整route-image接口及具体反例。
实际文件：此次修改路径与 diff。
核查：检查任意源坐标量词、true inverse、输入路径及输出消费者；未重跑历史大图。
未采用：不强制每条路线满秩，不把旧秒数变成默认预算。
```

这不是固定 schema。复杂修改可以更长；一个已经明确的小缺口可以更短。关键是下一位执行者无需猜测“这些记录怎样改变代码或技能”。

## 8. 反模式捕捉：保留数学失败，修复操作噪声

复用 ARIS 的 [capture anti-patterns](../../skills-codex/shared-references/capture-antipatterns.md) 所区分的四类：环境特定错误、暂时故障、负面工具能力断言、只有单次叙事而没有可迁移含义的记录。它帮助检查拟写进长期技能的理由；不是数学真值判定器，也不是自动删除失败材料的工具。

如需要运行机械筛查，从仓根按实际文件调用：

```bash
python3 base/tools/capture_filter.py path/to/proposed-rationale.md
```

flag 后读具体文本并判断：若是一次服务故障，保存真实错误与已知修法到执行记录，把“某模型不能读长证明”改成这次输入、完成状态和实际 workaround；不要固化为未来禁用。若筛到的是合法数学反例或必要条件，保留它的对象、假设、失败输入、结论和重启条件。筛查未 flag 也不能证明这条规则正确。ARIS 原参考自身的审阅路由按主技能的数学适配执行，不由本参考增设一层固定评审。

特别保留下列知识：F25 plane并反例、归一项目逆的6倍标量反例、相邻中心 clone 路径、放宽 matching 后旧必需边论证失效、数值 UNKNOWN 与独立整数证书的区别。它们给出可复查的机制边界，属于正当 anti-repeat 知识。不能把它们概括成“有限域提升无用”“helper都会失败”“求解器不能证明数学”。

同样，不把旧项目的一次限额、单次查询、固定模型或“不得续旧timer”复制成通用永久规则。后续若有新证据、修复后的服务或真正改变的数学条件，接手者可以在当前授权内重新决定。应保留的是原尝试及其准确范围，避免把同一失败当新成果；不是禁止有理由的进一步工作。

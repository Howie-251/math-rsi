# balanced49 共同赋值与剩余 H49 分支：架构更正及实际绑定

日期：2026-10-27。主会话数学推导与针对性自核；有限实现／检查明确请求 native gpt-6.1-sol/high，在权威 Linux 执行。实际 backend/effort 未由独立证据核实。继续跳过 Claude；新数学、程序检查、构造均未独立审查、未正式接受。旧任务、稿件、CNF、证书、封存运行和接受状态不变，无提交／归档。

隔离目录：[balanced49_remaining_hr_20261027](../../../../tmp/balanced49_remaining_hr_20261027/README.md)。本轮接通 Through14 的全类语义、实际公式与已有证明回执，排除 no R6/B6/weak7 中红五 through 人口 t≥14 的完整分支（新结论，未独立审查／未接受）。本文不把该人口界称为 C 或 D 容量下降。当前 C≤49 尚不能使用，H49/R30/B0=∅ 的 W=0/1、残余 E5/E6 均未排除。

## 1. 主会话首先核实的两项架构更正

### 1.1 双外点公共点并不是一个独立局部入口

**命题 A。** 设 Y 是安全满25，a,b 为不同外点，Y+a+b 继承 no B5、no weak7。则对每个 y∈Y，存在实际 R6⊆(Y−y)+a+b。因此 Y+a+b 的全部实际 R6 在 Y 中的公共交集为空。

**证明。** (Y−y)+a+b 有26点，完整 signotope 及两个禁形由诱导遗传保留。若无 R6，它就在 accepted scoped b25 域中，矛盾。对每个 y 分别应用，不需要挑选或拼接路径。证毕。

这一命题甚至不需要全部 D7 条件。它纠正前轮记录 §8 把“删一加二”列为较容易下一候选的研究优先级；旧稿保持原样。由假想 R30 迫公共点仍可成为反证的最后一步，但证明必须实质使用另外三个外点等全局事实。它本身没有得到更容易的局部支持。

一般 A⊆T、D⊆Y、|D|<|A| 同样被容量迫保留某条 R6。因此所有严格交换都是在完整临界结构下导出与容量相冲突的全路径命中，不预先限定 |A|=2。删二加三、删四加五全部保留；同一 Y 和含多个外点的路径不可省略。

### 1.2 balanced49 自动消去的分支及准确数值

**命题 B。** 在同一 canonical X=H⊔R 中，若 C≤49，则 H50 不存在；若 |H|=49，则 B0=∅。

**证明。** H 是 no R6/B6/weak7 的 C 模型，所以 |H|≤49。若 r∈B0，H+r 有50点、无 R6；它继承 no B6/weak7，亦属 C，矛盾。证毕。

因此若另证明完整分支 H49、R30、B0=∅ 不存在，则在 C≤49 下：|R|≤29 时 |X|≤49+29=78；|R|=30 时 H 不可能为49，故 |H|≤48，也有 |X|≤78。这个顺序不要求先在 C≤50 下证明全部 R30⇒H≤48。

反之，单独排除 H49/R30/B0=∅ 尚无新全局数值：H50/R30 及 H49/R30/B0非空没有被这个命题排除。命题 B 是条件消去规则，不提前使用尚未完成的 C≤49。

## 2. 原始状态与本轮实际读取

实读 [前轮全局记录](D7_GLOBAL_EXCHANGE_AND_BALANCED49_SEMANTIC_BRIDGE_20261027.md)、[共同核心记录](D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md)、R20 §5—6、R7 的 fan／人口分割，以及 [cardinality-layer-theorem](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md) 的精确模型／状态／接受部分。读取 E5/E6 的 EXECUTION_REPORT 和各 result.json：均 TIMEOUT_UNDECIDED，−9，各180秒，未续跑。读取前轮 SOURCE_MAP、PRIMARY_EVIDENCE_AUDIT 和 prefix_source/ACQUISITION_STAGE。

b25 的接受只给完整 ordered rank-3、no B5/R6/weak7 上界及 m≥ε，不给构造存在、取等分类或稳定性。前轮26点完整反例 τ=1、满 Y 的 ε=m=2 仍否定单外根路线；本轮没有重跑或增加端点。

Joint17 完整源早已在本地取得并验 SHA；本轮不是重新发现下载失败。Through14、Terminal20 原 strict-RUP PASS 保留其各自绑定范围。ClosureData 原已取得，ClosureLiteral 尚无取得／证明检查完成证据。Lean 包下载、上传、部署、编译分开，未进行新部署／编译。前轮 DOCUMENT_CHECK 仅检查文档，本轮所有检查也不称为独立审查。

## 3. 一个 master 对象及可同时使用的命名次序

固定假想 balanced50 Z：完整 ordered rank-3、no R6/B6/weak7。所有实际点零基编号0,…,49。必要时只在开始整体换色，使 χ(0,1,2)=R，然后所有组件固定此颜色。

从 b25 与对偶得到两个人口分割：

\[
S_R\sqcup E_B=Z,\quad S_B\sqcup E_R=Z,\qquad
|S_R|=|S_B|=|E_R|=|E_B|=25.
\]

理由：同色五源集合无异色五链（在末点用一条五源链的第二点续出异色六链），其补集无该色五链；对两者分别用 b25／对偶。源与异色五末点不交，因为连接三元组的任一颜色迫某条六链。于是人口各25且覆盖。这里全在同一个 Z 中计算。

记 S=S_R，固定 h=max S 的一条实际红五 (h,t1,t2,t3,t4)。尾点都晚于整个 S，且在 E_B。公开 label 的坐标固定为 (红入链长−1，蓝入链长−1)。对 u<v 记 ℓ(u,v)，D(v)=其所有入对标签的正坐标 down-closure。全部状态在4×4盒；S 的状态在4×3盒，因为 S 不含蓝五末点。

**引理 K（一个全局命名次序，可供不同目录共同拉回）。** 令 Ω 为4×4盒的全部70个 down-set，给每个状态固定不同 code∈{0,…,69}，另给一个 inactive 空状态副本 code=70。对状态 A 定义

\[
c(A)=\max(\{v+1:D(v)\subseteq A\}\cup\{0\}),\quad
k(A)=1207c(A)+71|A|+\operatorname{code}(A).
\]

inactive 副本使用 A=∅ 的 c、面积，单独 code。若 A=D(v)，则 c(A)=v+1；实际 owner 次序、状态严格包含次序均被 k 保留，各目录内名称的 k 不同。

**证明。** u<v 时 ℓ(u,v)∈D(v)\D(u)：若被某个 w<u 的 ℓ(w,u) 支配，χ(w,u,v) 所在颜色的入链增长与支配矛盾。因此状态单射，D(u)⊆D(v) 迫 u≤v；取 u=v 达到 c(D(v))=v+1。包含使 c 不减，严格包含使面积至少增加1，71的面积增量大于 code 最大差70。对实际不同 owner，c 至少差1，而面积／code 余项在0,…,1206，因此系数1207保留次序。模71的余数区分所有不同 code，给注入。证毕。

Closure 的35核心名按 **BalancedNamed 实际 cell 集合相等**映到 Ω；它的目录不能与 StateUniverse 同号相认。35,…,38映到 D(t1),…,D(t4)，39映到 inactive 副本。Joint17 的40名按 JointCatalog cell 集合映到同一 Ω，重合的实际状态使用同一 owner 和同一 k。available 状态的 owner 取唯一真实点，不存在的状态 owner 任取0。Closure 中29个 active 及 Joint17 条件分支选出的 active 集合各有明确的角色谓词；这两种 active 不是未经标注的同一变量。

引理 K 无需任何几何坐标，不构造公开的几何 Configuration 类型。它使“不同目录可选择相互不一致的次序”的自由消失。代码中的数字名称仍由 dictionary 映射，不拿名称大小当核心点的实际顺序。

**全部变量的单一语义来源。** 定义 ν(组件角色,变量) 为上述 Z 中的真实事实：active 是该组件声明的实际选点角色；order 是共同 k；color 是 owner 三点按实际顺序排列后的 χ；pair label 是规定域中的实际最长入链；路径／见证是完整实际存在性；计数是实际列表的真项个数。未选中的点不从 Z 的 ambient 路径域中删除。

秩域固定如下：Closure 和 Joint17 的 ambient 标签使用 Z；Through14 的 ambient 经 f 映回仍使用 Z，core 只用所选14点；Terminal20 在所选24点 U 上诱导并重算；prefix 只因是实际最早前缀，其入链／状态与 Z 完全相等。最后一项不能推广到任意子集。不同变量编号和角色是 ν 的明确参数，不是分别寻找几个无关赋值。

## 4. prefix 全类语义迁移：本轮完成的数学／固定表环节

新取得的 ES7PrefixData 是129个具体模式，包含4个四点 base、7个五点 sector、118个六点 sector。其 pairs/triples 均采用源码的递增词典序；五、六点的“最早四点 packet”不是整张 bits 表的前四项。

**定理 P。** 对任意上述同一 normalized balanced50 frame，给全部 prefix 变量赋以“这个具体模式恰为该对象的实际最早前缀”的真值，则公开全部3198个 prefix rule 的符号子句在 ν 下同时为真。

**全类入口。** 最早四点无法结束蓝五，故在 S。最早三点红时，最早五点中的蓝五将含该红三，矛盾，所以最早五点都在 S。最早四点全红时，最早六点内的任何蓝五与这四点至少交三点，也矛盾，所以最早六点都在 S。单色路径所有三点同色由 packet 首末同色迫全包同色及跨度归纳得到。

每条末于最早 n 点的路径都在该前缀内，故其中完整重算的 label/state 就是 Z 的实际值。首 packet 为 RBBB、RRBB、RRRB、RRRR 之一；cut=1 调用五点覆盖，cut=4 调用六点覆盖。每个实际完成色满足完整 packet；六点时还因 no R6 排除四个连续三元组全红。

**固定表覆盖的完整有限证据。** 一次 Linux 检查枚举64个五点、65536个六点完成色，分别恰有7、118个 Good 色；与相应模式表颜色集合完全相等，missing/extra/duplicate 均0。129行全部 owner/state、bits、pair labels 都与直接路径递推及另一路径子集枚举一致。因此每个实际前缀有表中匹配行，其 owner 由状态单射唯一确定，且全部颜色、标签是这个同一实际前缀的值。

**逐构造子证明。** 对每条规则，若某 guard 为假，其否定已满足子句；以下只看 guards 全真。

1. activation、order：Prefix 定义给每个位置的 actual active owner 恰为该位置，其 key 次序因此正确。
2. exhaustion：某 active 核名不在前缀 owner 表；若实际 owner 仍早于前缀末点，完整前缀位置表和 owner 单射会把它认成表内同一个名字，矛盾。故它晚于前缀。
3. sign：记录 bits 就是固定 χ 的值；名称排序由 source color helper 拉回实际 owner 排序，不改变真实颜色。
4. attainment：若从 pos 到 owner(j) 的 b 入对标签坐标≥2，取达到最大值的实际前驱 t<pos，有 b 色三元组且前驱标签坐标加1恰为当前值。t 必在同一最早前缀；PairComplete 给其记录，Valid 的覆盖条件保证 t∈terms。它不同于 j，故该列出的实际颜色项为真。没有另换一个前缀或不相容的前驱。
5. unique：Disagree 给同一实际三元组的相反记录，两个 Prefix guard 不可能同时真。
6. implies：Extends 逐项包含 owner／bits／labels，故较长模式为真时被包含模式在同一对象上真。
7. baseCover、sectorCover：由上面的全类入口和固定表完整覆盖，各自列出的某个实际模式为真；Valid 确保没有漏掉相应完整列表。

这覆盖全部九种构造子，证明没有假设这些规则能各自选不同 assignment。证毕。

一次检查还验证了3198条的精确 Valid：activation360、order106、exhaustion1185、sign602、attainment746、unique167、implies29、baseCover1、sectorCover2。五个受控错误均被拒绝，包括删掉实际 attainment 前驱和删掉一个 Good sector 行。符号子句均映入151801项 dictionary。

数学与固定表层已完成；**实际 Closure CNF 行相等未检查**，因为 ClosureLiteral 未取得。故定理 P 不等于 C≤49。证据：[SUMMARY](../../../../tmp/balanced49_remaining_hr_20261027/prefix_check/SUMMARY.md)、[result](../../../../tmp/balanced49_remaining_hr_20261027/prefix_check/result.json)。新检查不作独立审查或自动验收。

## 5. Joint17：同一真实对象的坏人口分支及实际公式绑定

设 t=|S_R∩E_R|。由两个25+25分割，记 L=S_R∩S_B、U=E_R∩E_B，有 |L|=|U|=25−t；另一个 through 原子也有 t 点。若 t≤8，则 L、U 各至少17。最早两点0、1不能结束任何五链，所以都在 L。

**引理 J。** 对这个同一 Z 的 t≤8 分支，可选实际 L 中17点（包含0、1）和 U 中17点，使源目录 Joint17 CNF 的全部实际59479条子句在 ν 下同时满足。

**命名与人口证明。** L 点不结束红／蓝五，D(v) 不含 (4,1)、(1,4)，恰落在3×3盒的20种 low ideal；U 点结束两色五，D(v) 同时含两角，除去首行首列后为3×3 ideal，恰有20种 high ideal。JointCatalog 经固定检查与全部70个4×4 ideal 中这两类完全一致。state 注入使所选34点映到不同的40名；0、1的状态为空和单格，恰为目录0、1。active 分别17，key／owner 使用 §3 的同一 master 定义。

**全部 schema 的组合证明。** named/order 用共同严格次序；pair activation/order 是定义；pairChoice 使用实际标签属于 D(v)\D(u)；pairUnique 使用唯一的实际标签；firstPair 使用 actual owner0、1 的最长入链分别≤2、≤3；forward 用正确颜色的入链增长。path activation/order、endpoint 由实际路径定义；base／growth 是实际三点／后接，PathAllowed 的上界来自 no 单色六链及末点／末前驱实际状态，故不删掉一个真的路径。polygon 的同端点异色链长度和9给 weak7：它们不能共享内点，否则该内点与两端组成兼具两色的三元组。packet 由 active 的共同实际次序及完整 packet 公理；counter 为真实列表阈值递推；population 和 mandatory 使用刚才实际选出的17+17及0、1。以上覆盖五组、named的13构造子，不调用几何凸性。

给每个 dictionary 编号 ν 所定义的真值。固定绑定检查对每个实际 CNF 行，先验证精确 Valid，再验证 decoded literal 集合等于对应 guards.neg++conclusion 经常量化简的集合。因此每条语义为真的子句都是同一赋值下的真实 CNF 子句。这不是把“几份各自存在的 assignment”合并。证毕。

**本轮完整固定行检查。** 59479条全部匹配、92886名字全部解码，40目录覆盖通过，七个变异控制被拒绝。Linux一次检查 wall1.871秒，CPU1.928秒，maxRSS89288KiB。原始证据：[RESULTS](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/RESULTS.md)、[result](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json)。

**公式身份的精确链。** 本地完整 Literal SHA为 `22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a`。独立的上传阶段120秒中断，只留下远端部分文件。绑定任务没有重试上传，而是核对远端30932992字节恰等于这份完整已验源的相同前缀，SHA为 `7760d1d01c73536ea64ed3c2f587caff67e37ff3531dfbd5b012bfb32fc823a2`。完整 CNF 字符串从零基字节126开始，结束引号在1490293，完整包含在已认证前缀中；解码 payload SHA为 `9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467`。source signed literal 的编号明确经 abs(literal)−1 变为零基 dictionary 索引。

这证明具体公式／schema 绑定，**不证明远端完整源／完整 proof 身份或 UNSAT**。上传中断导致验证 driver 未 dispatch，checker 调用次数0。故引理 J 尚不能反证 t≤8；只要该同一公式的完整证书检查通过，它才会排除这个全 balanced50 坏人口分支。其成功重放仍缺，不能沿用源码内 `native_decide` 字样作本轮运行回执。

## 6. Closure 全组共同语义：条件人口输入必须写在前面

本节明确条件 P1：9≤t≤13；P2：S 内实际红五源至少6个。它们不是由 frame 存在自动得到。本节证明**若同一 Z 还满足 P1/P2**，则其公开全部 Valid Closure schema 可由 §3 同一 ν 同时满足。

使用的三项纯组合事实如下。

- 实际 b 五链起于 v，固定其第二点 q，则所有 u<v 满足 χ(u,v,q)=非b，否则前接为六链；末点版本对偶。因此核心异色链可用其末点的一个真实邻点延伸，不要求该邻点是已选名字。
- 若两点都是红五 through，不能在它们之间有蓝四：用前者红五入链的倒数第二点和后者红五出链的第二点，给实际蓝六。
- 实际路径都有达到的前驱／后继；保留指定端点的缩短由 packet 子链性质合法。入、出同端对长度和8给六链；入、出共享一顶点并有正确桥接颜色、长度和7亦给六链。所有桥接点均是同一条真实路径的点。

**域与辅助常量。** 核心名0…34，尾名35…38，39 inactive。source active helper 在≥35时为真，但它与真实 active 的等价只在 Valid 的 <39 范围调用；绝不把39当真点。tail 比较数字大小有效，因为实际尾全晚于核心且已固定排序；核心比较仍是共同 k。j为核心时真实pair标签落在 coreStates(j)\coreStates(i)，而 j为尾时只用4×4盒上界。PathAllowed 的所有剪枝均由真实状态差和长度上界推出。ambient/core 的 k=2 helper 是常真，只有已从其他 guards 得到 active、不同点、次序时才能还原二点路径；low2则是真实变量。

逐组论证如下，所有 rules 的 false guard 情形仍由其否定满足。

| 组 | 所有构造子的真 guard 情形 |
|---|---|
| base | order传递；pairActive/Order/Unique定义；pairChoice状态差或尾盒；firstPair实际首两点入链界；forward入链增长；endpoint/pathActive/pathOrder定义；base/growth实际路径与合法PathAllowed；polygon为实际weak7矛盾 |
| ambient | activation/order定义；nesting真实截断；base/growth真实前接；selectedRank实际入对最长性；pairBudget上述同对拼接；vertexBudget见下一段；throughCap上述蓝四禁形 |
| core | activation/order定义；witnessNeg七项定义，witnessPos在len=3用active/order建真实二点后缀，len>3用真实core后缀；forward拼接；attainment取真实第三点，其名字在完整successors列表；extension红链留在ambient、蓝链用同一末点邻点延长；capPair蓝二点同理；sourceForward定义，sourceAttain取内部五链实际第二点，覆盖列表含该名 |
| low | activation/order定义；extension对真实low末点（蓝五源）用固定邻点延长红链；impossible的low2末点同时含(4,1)矛盾；base由两个有序核心点且末点low；growth前接真实点，末点low保持，若长度5则延伸成红六矛盾 |
| counting | recurrence真项阈值；coreBound=25；mandatory为空、单格实际首两点；throughBound使用P1；internalBound使用P2，无额外人口断言 |
| packet | 取同一实际key次序的四点，packet同色区间性使中项同色；不按目录数字预排核心 |
| terminal | last是固定h；最大性来自h=maxS；全部尾链三元组由同一实际五链及packet子链性质；cover列全35名 |
| prefixRule | 定理P的同一实际前缀，不更换颜色、owner、标签或frame |

vertexBudget 尤其不能省略 Valid 的 y≤3。它使蓝 helper 的长度6−y至少3，其真值提供真实 active 和顺序；随后才能把红 helper 可能为2的常真项还原成同一对上的真实二点路径。由 (x,y)∈D(i) 选**一个**同时支配两坐标的真实入对前驱 u。桥接 χ(u,i,j) 若红，用长 x+1 的实际红入链和长6−x的红出链拼成红六；若蓝对偶。没有给两色另选不相容前驱。

因此 P1/P2 成立时，不依赖平面可实现性也能给每条 Valid schema 同时赋真；这是条件的完整 schema 层迁移，不是 C≤49 结论。P1 下界来自 Joint17 的坏人口反证，上界需 Through14；P2 用删除 S 中所有内部红五源后选20点，再以 max 的四点尾得到 Terminal20 实际24点对象。这些选点始终来自同一 Z，但 Terminal20 的秩必须在所选子集中重算。

本轮完整 Closure 固定行检查的整体结果是 **FAIL**：所有190932行完成 Valid／符号重建／字典映射后，控制程序因预设存在 sourceAttain 行而抛出 KeyError。实际固定表无此类行，三个错误控制已拒绝，另九个未运行。保持失败回执，不修复重跑。该状态既不是某个数学规则的反例，也不是完整检查通过；actual ClosureLiteral CNF 相等及证书检查均未完成。本轮未声称公开 Lean Model 已构造或编译。

### 6.1 固定表使 Terminal20 从最短依赖链中退出

**命题 D（只删除未被公式使用的前提）。** 对同一 balanced50 Z，仅假设 P1：9≤t≤13，不假设 P2。则 §3 的同一 ν 满足所有 Valid Closure schema，唯一可能的例外是 `counting.internalBound`。因此，任何由这些规则组成、没有 internalBound 的固定公式，其语义迁移不需要 Terminal20 的内部源人口下界。

**证明。** 给 `.internal i` 仍赋实际“i为S内部红五源”的真值；`.internalCount xs k` 仍是真实列表阈值。计数递推对任意真项人口恒成立，不需要其总数至少6。sourceForward、sourceAttain 分别是实际五链推出实际源、实际源取达到的第二点，也完全不需要源的总数。§6其余每条证明只用 frame、P1、路径、packet、no weak7。逐构造子检查，唯一调用 P2 的是结论为“内部源计数≥6”的 internalBound。删除这类规则后，所有保留的规则同时由同一个 ν 满足。没有改动赋值、目录、实际配置或路径域。证毕。

本次完整固定行库存显示：core 的 sourceForward/sourceAttain 各0行，low.impossible 为0行，**counting.internalBound 为0行**；throughBound 有2行，分别保留上下界。因此这份公开固定表落在命题D的范围。这里使用的是失败控制阶段之前已经完成的全表统计，未将整体 FAIL 改为 PASS；统计及检查程序仍属未经独立审查的新证据。未来若 actual CNF 绑定发现额外行或另一版本存在 internalBound，就不能套用这个依赖削减。

该结论不是容量下降，但确实改变本轮A的最短链：对这份固定 Closure 表，应优先 Joint17、Through14、Closure 的完整证据边；**不再把 Terminal20 绑定作为这条路线的必要前置工程**。原完整 schema/公开 Lean Model 的 P2 义务保留；若选择构造那个完整 Model，不能用本命题跳过其字段。本命题走的是实际固定 CNF 的直接共同赋值路线。

### 6.2 Through14 的全类实际选点与全部规则迁移

**命题 U（语义部分）。** 设 Z 为任意有限完整 ordered rank-3 signotope，no R6/B6/weak7。若有14个实际红五 through 点，则存在一个严格递增的实际选点映射 f:{0,…,21}→Z，使 Through14 的全部 Valid schema 在同一 ν 下同时成立。这里无需 balanced50 或 b25。

**实际选点。** 取14个 through 点 q1<…<q14。取一条结束于 q1 的实际红五 `(l1,l2,l3,l4,q1)`，以及一条开始于 q14 的实际红五 `(q14,u1,u2,u3,u4)`。固定 f 依次为 l1,…,l4,q1,…,q14,u1,…,u4。前四点严格早于全部 q，后四点严格晚于全部 q，故22点互异、顺序正确。第4…17号正好是 K={q1,…,q14}。端部五点内的全部三元组为红，由 packet 的单色子链性质成立；这覆盖源码 actualCup 的全部条件 k≤4 或 i≥17。

**秩与布尔语义。** ambient 的 C/P/E/L/R 变量经 variableMap(f) 在整个原 Z 中解释：完整颜色、固定起点末对的实际路径、同端点实际路径、以指定对结束／开始的实际路径。它们不是22点诱导秩。core 的左右秩只在实际 K 内解释，witness 是相应 K 路径的真实前驱／后继及真实转向颜色的合取。所有变量只是 §3 的同一 ν 在新组件角色和 f 下的取值。

**通过点的共同延伸。** 对 q∈K，固定红五入链的倒数第二点 p<q；对每个 v>q，χ(p,q,v)=B，否则原红五延长为红六。对 q 的红五出链，固定其第二点 w>q；对每个 v<q，χ(v,q,w)=B。它们是对所有相应 v 成立的同一实际邻点，不分别挑选相互不相容的见证。

故任意 K 内蓝对可以在左、右各伸出蓝三；任意 K 内蓝三可在左或右伸出蓝四。若 K 有蓝四 `(a,b,c,d)`，在 a 左侧用其上述 p，在 d 右侧用其上述 w，得到实际蓝六 `(p,a,b,c,d,w)`，矛盾。所以 K 无蓝四；它也由 Z 遗传无红六。

**全部基础规则。** Through 的 `.base` 只允许 OrderedContract 中除 core、terminal 以外的规则。它们在 Z 中逐项成立：pathExtend/base/extend 是实际前接或后接；pathMax/maximum 否则给单色六；endpoint/pathRank 是忘掉部分指定点的存在性；suffix 缩短真实链而保留指定对；pair 的两链共享一对、长度和8，拼成6点；triple 的两链共享中点、有指定桥接颜色、长度和7，拼成6点。若参数长度小于2，对应实际路径变量本来为假。weak 的两色同端点链长度和9，不可能共享内部点（否则同一端点三元组有两色），其并集就是被禁的 weak7。packet 恰排除源码列出的八个多次变色字。f 的严格次序和范围把每条 `Valid 22 0` 的实际点条件搬回 Z；没有把未选中的 ambient 路径内部点删除。

**全部核心规则。** witnessNeg/Pos 是同一 witness 合取的两个方向；forward 把实际前驱／后继接上，k=3时由实际颜色和真实二点路径构造。attain 从实际 K 路径取邻点，该点属于 K，且由 f 的严格次序恰在源码 predecessors 的完整列表中。nesting 对实际路径截短，保留起／末对。extension 对红链直接遗传到 Z；蓝链在 Valid 中只能为3，用上面的共同延伸给 ambient 蓝四。pair 用共同邻点给 ambient 蓝三。maximum 红侧若再接一点给红六，蓝侧给 K 内蓝四，均不可能。actualCup 已由两端的同一实际红五证明。它们覆盖全部十种 Schema 构造子。所有 false 前件自动满足相应子句，所有真前件均由同一对象给出结论。证毕。

这个证明不调用几何坐标或公开 Configuration 的可实现性。

**实际公式绑定已完成。** 新的一次 Linux 检查对全部5077条实际 CNF 行验证精确 Valid 和 **有序 literal equality**（并非只比去重后的集合）；12158个 dictionary 名称完整解码，14个负变异控制均拒绝。字典长度12158与历史 checker 的最大使用变量编号12156是不同量，不能混同。表中没有 top tag5的 nesting，也无 ambient suffix 行；它们的普遍语义证明不因零行而省略，但不冒称它们被固定行测试覆盖。实际 wall0.156155秒，maxRSS21504KiB，没有调用solver／checker／新proof重放，没有重试。

当前旧 Linux CNF 的 SHA为 `8a59bfc9ee2a64987b41fb9fc7251fb25c20a70388508afcd5478b1d51a4812b`，并逐字节等于完整已验 Literal 内嵌公式。Literal SHA为 `640acebb5128073f1731f88893fe4178fb73d9259577fc562f4579c66650e250`。它们与历史 strict-RUP PASS 回执中的来源／公式 SHA一致；该回执SHA为 `c4a0e1ed8bc9d42102651915c80caaaa6a8cb400dea84c17d1af5070906468de`，记录5077个源子句、3009个添加子句、81736个严格提示以及最终空子句检查成功。新 result SHA为 `ac35cea650ff3d33b0676fd2b09fdc8186d0467c4622a66d19533c1f4b449cb5`。证据：[SUMMARY](../../../../tmp/balanced49_remaining_hr_20261027/through14_binding/SUMMARY.md)、[result](../../../../tmp/balanced49_remaining_hr_20261027/through14_binding/result.json)、[历史strict-RUP回执](../../../../tmp/balanced49_abstract_port_20261026/through14_replay_result.json)。历史 proof 检查和本次公式绑定各自记账，没有伪称本轮又重放了proof。

**推论 U13（新研究结论）。** 任意上述完整 Z 均有 `|Src_R5(Z)∩End_R5(Z)|≤13`；换色给蓝色同一结论。

**证明。** 若至少14，命题U给一个同一实际语义赋值。对任意实际 CNF 行，固定检查给出的 ordered literal equality 将该行精确解码为命题U中已证为真的子句。因此所有5077行被同一个布尔赋值满足。它与已绑定到同一实际公式的 strict-RUP 空子句证明矛盾。每个目标 Z 都能作该实际选点，故排除的是完整 through≥14 分支，不是某个模板或必要接口。没有费用计数、例外状态或见证共享可补偿这个“同一公式既满足又不可满足”的矛盾。证毕。

此推论依赖所列确定性检查及历史回执，仍未经独立审查／未正式接受，不更新项目接受记录。它直接补上 balanced50 的 P1 上半边 t≤13，但不单独给 C≤49。

**完整分流必须显式写明。** 对同一个假想 balanced50，t≤8 用Joint17的实际选点；t≥14 用命题U的实际选点；9≤t≤13 用命题D的Closure赋值。这三个条件穷尽所有实际t。不同反证分支不必同时选出彼此人口不相容的17+17与14 through，但每个分支中的全部约束必须共用那个 Z 的完整真实语义。当前只有 t≥14 已接通矛盾；t≤8尚缺proof检查，中段尚缺Closure实际CNF和proof绑定。

## 7. H49、R30、B0=∅：合法全路径入口与未获的不可共享性

始终在同一 canonical X=H⊔R。H49 的内部四个人口各在24…25之间，而不是已知恰24或25；两预算分别是

\[
a_R+e_B+z_R=1,\qquad a_B+e_R+z_B=1.
\]

不相加。B0空时没有权利导入 B0非空时的共同 S24/F25。第一 H 尾点已经在 Src_R5(H)，不属于新源提升。

R20 的 H 两端封闭和 |W|≤1 完整适用。B0=∅ 时每个 H+r 含 R6；对 r∉W，起点不能在 H，因此该路径为 (r,h1,…,h5)，全部 hi∈H。对 r 的每条这样的尾均保留。

任取 R 内实际 R6 的末对 (u,v)。若 u∉W 且其某条 H-only 尾末点 h>v，为免在原 R6 后接 h 得 R7，须 χ(u,v,h)=B；而 (u,v,h) 与从 u 到 h 的红六同端点，给 weak7。h∈H不能等于v，故每条尾全在(u,v)。这是既有全路径位置约束，不登记为突破。

把 R30 的真实临界性接入时，固定 E5/E6 对应 Y25、T5，全部私人路径和多外点路径不变。W=∅ 时每条路径的末前驱都有上述尾供应。W={w} 时：若 w∈T，则 R−w=Y+(T−w)，由满Y的部分扩张恒等式确有α=25、τ=4；若 w∈Y，则不能这么说，只由任何删点横截并回w得τ(R−w)≥4，结合D7遗传五横截仅知τ为4或5。私人路径不擅自改用别的补集。

**本轮推导的停止位置。** 尾的第一H点至多落在25个实际 Src_R5(H) 点中；30个残余需求出现共享并不产生矛盾。没有证明某个共享会产生禁形，也没有一个给每个需求分配不同 H 资源的映射。末间隙可以重叠／嵌套，且同一实际尾可能服务多条路径；因此不作第二费用或严格交换记账。没有从30个需求、25个源的数字差直接推出五个 neutral 点。

### 7.1 为什么只靠 canonical／全尾供应不能证明资源单射

下面仅是数学反例，**不是 H49/R30 反例，也不计作本轮目标成功**。它明确否定删去大规模／临界假设后的通用“尾源不可共享”说法，故不再细化这种说法。

取完整7点0<1<2<3<4<5<6，只有 χ(0,1,2)=B，其余34个三元组全红。含012的packet为BRRR，其余RRRR，故完整合法。唯一蓝三是012，无蓝四；全7点的首连续三元组蓝，所以无R7。含蓝三的weak7只能与同端点0、2的红六配对，但该区间仅3点且012蓝，最长红链为2；其他蓝侧只能2点，须有R7才能weak7。因此X无B6/R7/weak7。

canonical 最小关联对满足 p(0)=2、p(1)=2：蓝012给12≺02≺01，所有后续相关三元组红，故02、12分别为0、1的最小关联对。对 i≥2，任一后续对(i,j)都有更小的入对(0,i)，故 p(i)<i。于是 P+={0,1}，G空，R={0,1}，H={2,3,4,5,6}。W空，B0空。两个实际残余点的**全部 H-only 尾均是同一条**红五(2,3,4,5,6)，其第一H点2是同一个实际内部红五源。

故不能仅凭 canonical fan、无混合禁形、B0空和全尾供应推出源或尾点的单射。真正的待证机制必须用 H49 的预算和 R30 的同一满 Y／τ5；本例不否定含这些条件的命题，也不建议围绕它加点搜索。

## 8. 原始有限工作及阶段界限

全部预算在[FINITE_BINDING_SPEC](../../../../tmp/balanced49_remaining_hr_20261027/FINITE_BINDING_SPEC.md)或取得前 request 中写明。这些是完成用户要求的来源／语义／公式链所需的固定数据检查，不是新SAT短跑。无求解器调用、无旧运行重启、无自动重试或续时。

1. 来源库存118份副本与manifest匹配。唯一一次60秒 Linux 取得任务完成 PrefixData 来源hash/CRC；ClosureLiteral 阶段未完成，outer124，最后回执停在range_request。没有把STARTED进度当成功。
2. Prefix一次60秒／2GiB上限验证，实际1.568秒，通过；模型和用途见定理P。
3. Joint17计划一次180秒／4GiB checker，但唯一120秒源上传中断，check_dispatches=0、checker_invocations=0。完整源仍在本地已验；未取得成功重放。
4. Joint17另一项固定公式绑定一次120秒／3GiB，使用已认证完整CNF所在的既有远端前缀，实际1.871秒，通过；未重新上传Literal、未执行proof。
5. Closure 一次120秒／3GiB上限验证实际8.648秒，整体FAIL；190932行全部完成后在控制阶段停止，3个控制完成／9个未运行。分组行数为base77368、ambient21238、core30987、low1922、counting1561、packet54009、terminal649、prefix3198；151801个名字全部解码。无actualCNF或UNSAT信用。[SUMMARY](../../../../tmp/balanced49_remaining_hr_20261027/closure_rules/SUMMARY.md) 与 [result](../../../../tmp/balanced49_remaining_hr_20261027/closure_rules/result.json) 保留原始失败。
6. 在命题D明确削去未使用依赖后，新增一次 Through14 固定数据绑定，规范先写入 FINITE_BINDING_SPEC；5077行精确有序绑定PASS，接通同一CNF的历史strict-RUP回执。它不是Closure检查重试，也没有新求解或proof重放。结合主会话命题U才得到U13；单看程序PASS不等于语义迁移。

源码取得、来源hash、固定表验证、schema Valid、字典行绑定、证书检查、抽象迁移、Lean编译分别记账。这里没有任何“下载成功所以数学已完成”或“文档检查即独立审查”的合并。

## 9. 研究价值、完整开放分支与下一步

| 新结论 | 删除R30/τ5/满Y后是否成立／全类入口 | 实际破坏的取等与补偿边界 | 分支作用 |
|---|---|---|---|
| 命题A | 是；任何安全满Y25的双外点合法扩张 | 不破坏取等；反而证明局部公共点不可能 | 停止先锁定删一加二 |
| 命题B | 是；同一canonical对象且条件C49 | C49下50点容量矛盾是真实净人口差 | 自动消去H50和H49/B0非空，当前未提前使用 |
| K、P | 是；全部normalized balanced50同一frame | 无ε或H缺额损失；关闭命名／前缀语义层 | 支持A，不冒充B/C改进 |
| J | 是；全部balanced50的t≤8坏人口分支 | 目前只有共同满足实际CNF；无UNSAT重放不能消去分支 | 剩余最短义务是已绑定公式的完整证书检查 |
| Closure条件迁移／命题D | 是；全schema用P1/P2，固定表的保留规则只需P1 | 不破坏容量取等；逐项证明未使用内部人口下界 | 从实际固定公式最短链移去Terminal20，仍缺CNF＋proof |
| 命题U／U13 | 是；任意no R6/B6/weak7中的14个真实through点 | 同一实际赋值满足精确公式，与绑定的空子句证明冲突，无资源补偿 | 本轮已接通，排除完整t≥14分支；C49仍未闭合 |
| 全尾位置／共享反例 | 是；通用入口，反例只有H5/R2 | 无不可共享性，不能按路径数收费 | B的W0/1仍完整开放 |

E5、E6及ε=m=k的全部k=0,…,10仍开放。没有新的完整R30或H49/R30反例，没有主线严格净损失。符号7点反例只否定不使用临界性的通用资源单射，不替代完整目标判别。

下一步不应再提“某个双外点有公共点”。A的最短链按命题D修正为：完成已绑定Joint17的真实proof检查；在同一ν与P1下绑定Closure真实CNF并检查其完整proof。Through14的实际codec边本轮已经接通。Terminal20不再是这份固定表路线的必要前置项。相关源缺失／上传中断不是新的数学定理，也没有无限重试授权。

B的最小数学缺口是一个**真正使用H49预算和同一满Y/T全路径族的不可共享定理**，或直接的混合禁形／严格交换。它必须说明两个实际需求若落在同一 H 资源上，哪个具体packet或路径会矛盾；目前没有这个推导。C保留一般 |D|<|A| 的完整命中或 m≥ε+1，未找到排除exceptional补偿的步骤。

本轮达到的严格排除仅为A中的完整人口分支t≥14；它不是E5/E6或H49/R30的排除，也不是C49的全部证明。B/C仍停在准备工具和明确缺口；没有新的完整目标反例、容量净损失或数值改进。不得用U13重复收费为H缺额，也不得把它登记成已接受定理。

## 10. 数值结算

- 当前C≤50、D≤30：Q≤80，对称避免规模≤81。
- 仅C≤49或仅D≤29：Q≤79，对称避免规模≤80。
- 完整联合目标R30⇒H≤48、尚无C≤49：Q≤79。
- 仅排除H49/R30/B0空、尚无C≤49：不自动获得新全局数值。
- C≤49且D≤29，或C≤49且H49/R30/B0空的W0/1两支都排除：Q≤78，对称避免规模≤79，既有几何衔接给强迫阈值≤80。

根归约的一点不重复计入；同一损失不重复记为容量下降与拼接缺额。本文不更新任何正式接受状态。

<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 八参数总亏损313：普通866至多57与完整整数格

2026-11-19，本轮只处理m≤10，实际推进对象为八参数。独占本文和
`evidence/n8-total-deficit-313-20261119/`，不改上轮原件、封存CNF/proof或作业。
没有外审。上游普通866≤57现已完成独立完整语义重建和两次实际DRAT，
据此兑现**C8≤189、真实D8≤123、Q8≤312、F8≤313，以及ES8≤314**。
前四项是最大避免人口上界，ES8是平面强迫阈值，不作sharp性主张。
本稿另给70条普通行的完整整数像定理与互补割图表达式；这些本身并不排除
189人口取等。科研运行全部在权威Linux。稳定证据入口见第8节。

## 1. 原输入及62洞的两种临界谱

balanced母体的252态写成五元子集W⊂[10]。去掉端坐标后把八内坐标重标为
Ω=[8]。蓝内部洞由I∈binom(Ω,3)标记，指标bI；红内部洞以其五元码的补
三集标记，指标dI。两类私洞的指标为aJ、eJ，J∈binom(Ω,4)。这些指标
全部是同一实际母体中物理状态的0/1洞，不独立选择各子面。

置pJ=aJ+eJ，普通十态行的超3余量zJ≥0。每条行的准确方程是

$$\boxed{\sum_{I\subset J}b_I+\sum_{I\subset J^c}d_I+p_J=3+z_J.}\tag{1}$$

共有70行。令B=ΣbI、D=ΣdI、T=B+D、P=ΣpJ、H=T+P，则

$$\sum_Jz_J=5T+P-210=5H-4P-210.\tag{2}$$

普通866≤58时，两不交私面各至少12洞。H≤61已由普通行计数排除；H=62
只剩P=25、T=37、Σz=0，或P=24、T=38、Σz=4。前者私面洞数为12／13，
后者两面都12。完整旧接口及未结SAT回执见
[上轮balanced原件](N8_BALANCED_SLICE_GAIN_20261119.md)。这些仍不是两种
实际signotope的存在性结论。

## 2. 新的完整整数像定理

令A为70×112整数矩阵，行按四集J、两类列按三集I，定义

$$A_{J,(B,I)}=\mathbf1_{I\subset J},\qquad
A_{J,(D,I)}=\mathbf1_{I\subset J^c}.$$

对任意整数四集数组w，记坐标度wi=Σ_(J∋i)wJ。任取Ω的四对完美匹配
π=((x1,y1),…,(x4,y4))，定义四阶差分

$$\Delta_\pi(w)=\sum_{\epsilon\in\{0,1\}^4}
(-1)^{|\epsilon|}w_{\{v_{1,\epsilon_1},\ldots,v_{4,\epsilon_4}\}},
\quad v_{i,0}=x_i,\ v_{i,1}=y_i.$$

**整数像定理。** w是A的整数列组合，当且仅当

$$\boxed{\Delta_\pi(w)=0\text{ 对全部105个匹配π成立，且 }
w_1\equiv\cdots\equiv w_8\pmod4.}\tag{3}$$

105个差分中只需固定14个基。A的有理秩为56，完整整数格的饱和指数为64，
Smith不变量为1×50、2×6、0×14。没有额外的3、5或其它素数扭结。
“模4”与六个二同余并不冲突：在有理列空间的整数点上，坐标度之差已自动
为偶，剩下是其半差的六个独立奇偶条件。

必要的有理关系可直接看出：每一三元星在匹配的16个横截四集上至少有一对
未被固定，沿这对的交替和相消。对坐标i计(1)的内部关联，得到

$$\sum_{J\ni i}(A(b,d))_J=B+4b_i+4(D-d_i),$$

所以其八个坐标度全同余mod4。充分性及“恰好这些条件”由下述独立精确
整数证书核准，未引用未核的Wilson/Smith现成表。

### 2.1 实际证书及可独立重放的充分性

发现阶段SymPy1.14求得上述Smith对角。完整Smith U/V导出在45秒外部硬限
后退出124，没有结果，不赋信用，也没有重试延时。改用标准库1634个整列
初等操作，每步行列式±1，得到56个零列和70×56基H。选定56行的H方阵
C为三角形，det(C)=64。

独立标准库检查器从三集／四集重新构造A，逐步重放全部操作，重算C的精确
有理逆和P=H C^{-1}，核得P为整数矩阵且所选56行构成单位阵，A=P A_selected。
因此P·Z^56正好是有理列空间的全部整数点，H·Z^56正好是A的整数像。

C^{-1}的分母均至多2，2C^{-1}模2秩为6。再把七个坐标度差作用于P，
核得全部系数为偶；其半差模2行空间与2C^{-1}的模2行空间完全相同，秩均
为6。故(3)的充分性逐项落在精确整数运算上。14个匹配差分基模1009独立，
A模1009秩56，核定全部有理余核；A模2秩50复核六个二扭结。

[独立重放原件](../SOURCE_MAP.md#excluded-sources)
返回`PASS_EXACT_INTEGER_IMAGE_AND_CLOSED_MOD4_CRITERION`；
[纯标准库checker](../SOURCE_MAP.md#excluded-sources)
无需SymPy或求解器。它证明的是允许任意整数内部系数的精确像，**不是**
内部bI、dI∈{0,1}的共同可行性，更不是实际pair／颜色实现。

### 2.2 本轮m≤10内可复用的一般必要结构

令m=k+4、2≤k≤6。balanced矩形为(k+1)×(k+1)，内坐标宇宙有2k个元素，
普通行以k集J标记，需求q=k−1。两类内部洞用(k−1)集标记。相同取消证明
给任意k对完美匹配的k阶交替差分`Δ(p−z)=0`。

每坐标恰属于binom(2k−1,k−1)条行。一个B星包含该坐标时服务k+1条，
否则一条；一个D星避开该坐标时服务k条，否则零条。因此同一实际输入有

$$w_i=q\binom{2k-1}{k-1}-kT+(k-1)B-k(b_i-d_i),$$
$$\boxed{w_1\equiv\cdots\equiv w_{2k}\pmod k,\qquad
\sum z=(k+1)H-kP-(k-1)\binom{2k}k.}\tag{G}$$

若两私面各至少t洞，同一式还给

$$\boxed{H\ge\left\lceil
\frac{(k-1)\binom{2k}k+2kt}{k+1}\right\rceil.}$$

这些是m=6,…,10的通用必要式。完整整数像的充分性只对第2节k=4进行了
精确证明；不把六个二扭结或模4充分条件未经核验搬到其它宽度。

## 3. 接回同一母体：互补割图与闭合同余

常数一数组在A的整数像中：把Ω标为F2³，蓝／红两类都取xor0的七个三集，
每条普通行恰获1。因此(1)的整数内部解存在，当且仅当

$$w=p-z\quad\text{满足(3)。}\tag{4}$$

令bi、di为两三元族的坐标度。由每个坐标35条行的总需求105，得

$$w_i=105-4T+3B-4(b_i-d_i).\tag{5}$$

于是P25临界层的wi全同余3B−43(mod4)，P24层全同余3B−47(mod4)。这
把私面真实洞的坐标度与内部蓝红差度接在一起；各面只知12洞不能替代它。

还可把所有互补行和变成一份共同加权图。令c_ij为两类内部三集在边ij上的
总共度，G为这份非负整数加权图。它满足Σcij=3T，顶点度为两三元族总度
的两倍。对平衡割J|Jᶜ，每个内部三集若跨割恰贡献两条割边，故

$$\boxed{c_G(J,J^c)=2T-12+2(w_J+w_{J^c}).}\tag{6}$$

P25层T=37、z=0时，35份平衡割的费用都介于62与70，且由同一112指标的
共度图提供；不能逐割各挑图。P24层T=38时，(6)的基值为64，只有总量4的
z可以共同补偿。互补关系、(3)、(5)、(6)均可在其它相同70行调用方复用。

## 4. 与两份真实58候选面的相容仍未闭

本轮把112个内部洞完全投影掉，建立新的140个私洞变量模型：两面各导入
冻结metadata解码后的641个纯局部核和15个Hall，私洞数分别在12至13、
合计25；加入14个四阶差分等式及八坐标度同余mod4。不导入原P首二占态
单位。该模型有23813变量、93093子句，CNF SHA256为
`9e5af7bbb333b79ce7a3d8a0be225163e17b140d46ec627830eca4f211b91fed`。

一次新的受控外部AE查询30秒后return0、UNKNOWN；没有SAT私面见证，也
没有UNSAT或checker信用，未延长。它区别于上轮252洞母体查询，但并未关闭
P25；P24更没有由此关闭。原件为
[private-p25/result.json](../SOURCE_MAP.md#excluded-sources)。

纯普通行的整数格本身不可能排除P25：上轮Fano删五线给了明确的0/1内部
37洞、私洞25、两面12／13，70行全恰3的覆盖；它满足(3)，却被其他实际
必要行拒绝。其全标号单类删线模板已被独立有限证书排掉，不能把该负结果
当所有整数设计的排除。真正未闭的是：两份候选58面必须有实际完整点序、
共同pair差格、全部三元色和路径，并与同一内部112态同时相容。

## 5. 普通866≤57已兑现313

以下公式曾以条件响应准备；现已由第8节的实际双DRAT及独立重建绑定上游
普通866≤57。一般设普通866≤70−t。
70条普通行的总需求210及两私面各至少t洞给

$$H_C\ge\left\lceil\frac{210+8t}{5}\right\rceil,
\qquad C_8\le252-\left\lceil\frac{210+8t}{5}\right\rceil.$$

真实残余按双缺9、10的70态A层与其余84态B∪C层物理不交分开：前者是
普通866，后者是普通858≤66，故

$$D_8\le(70-t)+66=136-t.$$

二者作用于R7的同一母体真实分拆，再接R20的合法chart加一，得到

$$\boxed{F_8\le389-t-\left\lceil\frac{210+8t}{5}\right\rceil.}\tag{7}$$

| 上游t | 普通866 | H_C | C8 | D8 | Q8／F8 |
|---:|---:|---:|---:|---:|---:|
|12（上一轮）|58|62|190|124|314／315|
|13（现已兑现）|57|63|189|123|312／313|

因此(7)现已直接兑现F8≤313，比上一轮315净降2；几何包含另给ES8≤314。
九份普通867的避坐标866切片中每点计五次，故同时有
**普通867≤floor(9·57/5)=102**，较上一轮104净降2。
这里没有把普通868≤164替代真实残余D8，
没有把C8和D8分别挑出的极值实现拼成一个实际输入。

若在t=13进一步企图达到C8人口189，H=63时只有P=26、两私面各13洞、
Σz=1。这是(2)的新临界接口；当前未排。若要不依赖上游57而单靠balanced
达到F8≤313，则需C8≤188配现有D8≤124；只降C8至189仅给F8≤314。

## 6. 当前结果与恢复

新闭合的整数像定理(3)及其同母体影子式独立保留；实际数值下降来自上游
普通57与第5节同母体计数的装配。所有本分支文件
独占于[evidence目录](../SOURCE_MAP.md#excluded-sources)，对应Linux根为
`<private-artifact-root>`。
本格／私投影批的有界进程已退出。第8节两个成功checker、完整语义重建、
两固定hash及本地原日志现已齐备；第5节的t13行已经兑现。

完整紧凑证据已取回
[lattice-and-private-evidence.tgz](../SOURCE_MAP.md#excluded-sources)，
包含70×112矩阵、105个差分及14个基、1634步操作、独立PASS、私投影CNF
及UNKNOWN原日志。矩阵原件SHA256为
`72ad6b3fce172fd6175d8beaa706f4cffee0e3b49f1797ba361c39a4851d8b2d`，
整列操作证书SHA256为
`9f624e9aa07d271451343596ca3d8e057d16aff325cbfc66a47ff9ddf08daf83`。

## 7. 新互补全域H12：共享极大角及真rank前驱已启动

后续主调度另行授权了一个真实全域58点推进，独占
[ordinary866-exact-rank-20261119](../SOURCE_MAP.md#excluded-sources)。
原输入证明先写在其[PROOF.md](evidence/n8-total-deficit-313-20261119/ordinary866-exact-rank-20261119/PROOF.md)。
任一实占P态的每个极大角都必须由某实际前点的**精确**rank达到；同一前点
只能给该目标一个rank，所以不同角的来源不能独立复用同一物理pair。
新公式在全部70态的140个角请求上统一这些来源，可比pair复用冻结标签，
721个不可比pair使用同一方向与两向one-hot允许rank。全占三元共享方向传递。

另对低17池源点的全部可比后pair，若色c秩k≥2，必须有同一实际前点证实
前pair的色c秩恰k−1且同一三元色为c。不可比前点保留为候选，使用共享
rank／方向／色变量；这些不可比低转角的全部标签组合也有逐色严格增长。
并非给各个角或递推另设互不相干的标签。未加58点专属的z=0条件，保留
36点真例可作全部非预算子句的正校准。

新完整公式110662变量、2427843子句，比只读复制的window H12源式新增
220443子句。CNF SHA256为
`6d88da2254b4b04e85adbc865590ce2540cc4c87982b56cf5a79bd4c2e47517c`。
[真实正例校准](../SOURCE_MAP.md#excluded-sources)
重算ambient36的全部真实末秩并赋值全部新旧变量，逐完整2427842条非预算
子句PASS，仅排除唯一H12预算unit。另写
[完整来源审计](../SOURCE_MAP.md#excluded-sources)
从原70理想重建全部新增子句并核对完整CNF字节hash，也已PASS。

无外部solve/check deadline的受控外部AE单次运行已经自然返回20，求解
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
完整DRAT checker PID/PGID3763225；最近采样核准其活cmdline与本式／proof
绑定一致，仍`RUNNING_DRAT_CHECK`、尚无VERIFIED，故未据此登记57。
原window公式、proof及PID全部保持。真实阶段应读该目录`status.py`，
不可据历史PID重新启动查询。

[完整新源与小回执包](../SOURCE_MAP.md#excluded-sources)
已经取回；运行中的完整CNF/proof/log保留Linux，不截断、不替换。恢复说明在
[README](evidence/n8-total-deficit-313-20261119/ordinary866-exact-rank-20261119/README.md)。

## 8. 上游H12的独立完整语义重建与第二实际DRAT

另对window的原H12另写完整标准库编译器，未把原body复制为重建结果，
也未把原作者audit输出当独立证据。从70态、可比关系、所有变量及93条原
支撑重建2165442条base；641冻结核按hash进口，四矩形Hall重新生成；再
穷尽全部2^20六点色表、重算906份真实最初六点模板及全部41958条尾句。
[独立重建回执](../SOURCE_MAP.md#excluded-sources)
实际PASS，完整70172变量、2207400子句的CNF字节hash与原式相同。
[原输入桥](evidence/n8-total-deficit-313-20261119/ordinary866-h12-second-replay-20261119/SEMANTIC_BRIDGE.md)
另列真实P、来源秩、同一三元及最初六点的全域量词。

绑定CNF SHA256为
`5d51a77cceb8296381c1ab8cd61c5b52460c5e64a80537d316b067b7803e561d`；
原proof为1160694777字节，自己另读全文件所得SHA256为
`fabcd1750c8c093ca8c5d84d4caa0d890536ab7d6901aae590a4fdff0654acee`。
第二checker PID3762654使用自己重建的CNF、只读原proof及同一权威drat-trim
实现，是另一进程而非另一checker实现。服务器旧版`-t0`会立即超时，故
显式`-t2147483647`且无外部deadline；未改第一checker。

第一实际DRAT现已成功：本地读回
[primary-result.json](../SOURCE_MAP.md#excluded-sources)
为`CHECKED_UNSAT_H12_FULL_QUERY`，checker退出0、唯一VERIFIED，
[原日志](../SOURCE_MAP.md#excluded-sources)
给核验2034.175秒。第二实际DRAT也已成功，
[second-result.json](../SOURCE_MAP.md#excluded-sources)
为`PASS_SECOND_FULL_DRAT_WITH_INDEPENDENT_RECONSTRUCTION`，退出0、唯一VERIFIED，
[第二原日志](../SOURCE_MAP.md#excluded-sources)
给核验2074.270秒。结束后独立重算CNF与proof两个hash均未变，两个最终
结果及原日志都已本地实取回；因此第5节现在兑现，而非仅等待求解器的条件表。
两次是同一checker实现的独立进程，没有冒称第二种实现或外部评审。
确切大原件路径、恢复方式及回执在
[独立重放README](evidence/n8-total-deficit-313-20261119/ordinary866-h12-second-replay-20261119/README.md)。

最终[双回放集合回执](../SOURCE_MAP.md#excluded-sources)
为`PASS_TWO_ACTUAL_DRAT_AND_INDEPENDENT_COMPLETE_SEMANTIC_RECONSTRUCTION`。
[独立重建及两原日志小包](../SOURCE_MAP.md#excluded-sources)
共150953字节，SHA256为
`c6b60a91793b77374bfb87141fef246e1e68085dc1925d446fb93e8af77a1b57`；
已本地实取回、解包并逐文件核对全部导出hash，
[传输回执](../SOURCE_MAP.md#excluded-sources)
只承担本地字节核对。完整大CNF/DRAT仍在Linux所列原路径，不以小包冒充。

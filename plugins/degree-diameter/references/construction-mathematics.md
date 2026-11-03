# 可调用的构造定理与共同覆盖

本页的定理按实际假设调用。历史具体值是实例，不证明任意field／几何对象存在。原文与源码均在[archive/source](../archive/source/)，由[来源地图](source-map.md)定位；本页已经写出的数学可用于推导，承重进口仍应读原证明与实际数据。

## 1. 有限简单图、最大度与精确直径

图G无自环、无重边，Adj对称。`B_r^G(v)`为闭距离球，包含v。`diam(G)≤D`表示任意u,v有长度≤D的真实walk；它隐含非空图相应的连通性。构造`n`点、最大度≤d、直径≤D给`N(d,D)≥n`。如需直径恰D，另证非≤D−1。

最大度d的简单图，根周围距离≤r至多 `1+dΣ_{i=0}^{r−1}(d−1)^i`，因为第一层≤d、后继每点至多d−1个新方向。超过这个Moore数可排直径≤r。它是上界而非可实现承诺，不能按缺口百分比估成功率。

## 2. 单点保边扩张：充分且可逐步复用

**条件。** G有限简单、最大度≤d、直径≤D。S⊆V(G)，`|S|≤d`，每个s∈S满足deg(s)<d，且 `⋃_{s∈S}B_{D−1}^G(s)=V(G)`。

**结论。** 新点z只连S且保全部旧边，得到最大度≤d、直径≤D的简单图。

**证明。** old-old沿旧walk。任意oldv有s与它距≤D−1，新z经s至v≤D；z度为|S|，每个旧pin只加1。证毕。

**实际caller。** D5三族103步的每一步使用**当前完整图** `G_i`，不是只覆盖最初base。几何Q-line／Baer／Rédei经实际折叠成为pins，anchor／guard补齐残余，并检查当时的逐点余度。原源D5进口不由current-cover重放重证。确定性入口为[verify_covers.py](../archive/source/constructors/early_d5/verify_covers.py)。

动态cache可使用已证明的更新式；只要添加改变了被查询球，旧negative cover未必仍为negative。不能将18个旧时刻的一anchor失败当最终图的全域不可能。顺序本身是配方输入。

## 3. 冻结完整邻域克隆，允许相邻与重复中心

**条件。** G有限简单无孤立点、直径≤D且D≥3；I为任意有限索引，c:I→V(G)不要求单射。新增`i`只邻接原始开邻域`N_G(c(i))`；保留G全部旧边、无new-new边。

**结论。** 新图直径≤D；oldv度为`deg_G(v)+#{i:v∈N_G(c(i))}`，newi度为`deg_G(c(i))`。若原G非D2，则新图也非D2；所有旧点间距离实际保持。

**证明。** newi到oldv≠c(i)替换源路径首边；到c(i)用任一原邻点走2步。两个new点同center共享邻点2步；center相邻时走 `i–c(j)–c(i)–j` 三步；center源距≥2时替换源路径两端。old-old有旧walk，任意新walk把每个clone塌缩为center可得同长oldwalk，故旧距离不变。度数由实际spokes计数。证毕。

**调用。** 固定frozen source和有重数的center列表。输出新N与该源邻域 N逐项绑定；不能读变异后的current(center)。q4的289中心诱导136K2+17isolates仍合法，说明独立中心不是必要条件。通用源码[FullNeighborhoodClones.lean](../archive/source/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean)及[ovoid原证明](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/PROOF.md)给真实caller。

**容量。** regular源度δ、oldcap增加k时，`δ|I|=Σold load≤k|V|`，故`|I|≤floor(k|V|/δ)`，只是这项fullN/no-new-new规则的界。非正则源必须按每个center真实degree记账；不排一般图。

## 4. 横截plane把点级负载降到controller负载

源fiber为`F_q³`，每dart从center x到目标fiber的neighbors为`T x+F_q L_r`。选择plane W满足对每实际 dart `T(W)∩F_q L_r={0}`。因dim2+1=3，q²个center的q点邻线互不交且分割整个目标fiber。

若每controller a选择r_a份同样的q²center块，则目标fiber b每点load为`Σ_{a∈N_C(b)}r_a`，在满足端口／chart条件时可用小整数负载模型找可行向量。必须同时满足所有dart；为不同target单独挑plane不构成同一center集。

实例：F5旧3750取`x0+x1+x2=0`；F4边依赖3840取横截五方向的plane；F9/56862取`W={(a,b,ηa)}`且η=1+w为nonsquare。F9 U10实际10controller/810centers/五K2，k复制给55..59五个端点，是一项规则的多个实例。局部packing达到81不证明全source最优。

## 5. 仿射三步路线与pencil联合

**邻接条件。** C简单rregular，端点port各异；每dart e=(a,b)给可逆T_e、非零noise L_reverse，实际reverse为T_e^{-1}且运输source noise line到target noise line。允许noise自由重参数，但不能丢掉影响整个三维作用的scalar。

实际三步word w的像是`M_w x+c_w+H_w`；H_w为三列noise的span。满rank3时一条word覆盖整个fiber。一般D3只需所有长度≤3word像的并覆盖，不能先改成每一条满秩。

**共同rport证书。** directions任意三条独立。中央边两组各r−1个projective quotient方向，交k点，则降rankturn数k；回退pencil并为 `q+[2(r−1)−k](q²−q)`。全turn满秩且pencil全覆盖迫 `q=2r−3`。这是joint证书条件，不是所有affinelift的必要q公式。

对原C30四port的外边，没有额外triangle／C4短路线，故q>5甚至允许edge-local矩阵／逆相容offset仍不能D3；至少漏`q(q−1)(q−5)`。F25具体失败3625/15625在全rank门仍过时发生，必须保留相邻层义务。

**六／七port条件。** PGL2(F9)720置换作用的252五半集有180/72两orbit且各补集相容；选定sixconic set配42张真正的逆 chart，可处理任意distinctlocalport labels。F11的924六半集为110/220/264/330四orbit，792七子集里只有132具(0,0,2,5)punctureprofile；选定两special＋五ordinaryport，实际十chart只支持指定inverse配对。不能照搬F9任意sortedneighbor结论。

**一般仿射coset准则。** 对同一源坐标x，选比较用的仿射中心 `M_r x+c_r`；这个reference不必可逆，也不必本身是一条实际路线。若每个参与的像满足 `im(M_w−M_r)⊆H_w`，则

```text
M_w x+c_w+H_w = M_r x+c_r+((c_w−c_r)+H_w).
```

右侧相对coset `(c_w−c_r)+H_w` 不依赖x；它们的并若为全目标空间，就对所有x覆盖。不要求每个H_w满秩、所有M_w相同或c差属于H_w。这是一般代数准则，实际图应用还须把所用路线及状态序列接到原邻接关系。

**源15552的实际应用。** 对有序控制器对(a,b)，该实现只从a到同一b、长度≤2的实际word中选reference；这项选择限制属于该实现，不是上面一般引理的额外假设。所有实际常数c为0，但准则与证明仍保留offset。相同reference／endpoint-word集合的尝试压成97组，其中6次首reference尝试失败并原样保留；91组成功证书覆盖原先缺失的3648对。其余33216对沿用各自的rank-4 word及保存的逆证书，合起来覆盖全部36864个有序控制器对。

每份命中给长度≤4的实际状态序列。只删除连续相同**完整global label**的virtual stay；同控制器但不同fiber状态、或同fiber状态但不同控制器都不能删除，其余步骤已绑定为真实源图边。因此得到原简单图中长度≤4的walk。这一桥不单独给出阶、度数或非D3，也不是仅凭fiber覆盖就宣称后继Lean定理已闭。

原证明：[general ports](../archive/source/research/ddp/two_successful_methods_20261101/affine_field_conditions/general_ports/DERIVATION_PACKAGE.md)、[D4共同coset](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/GLOBAL_COSET4_NOTE.md)。

## 6. Opposite-GQ spread填补与ovoid乘积

设实际GQ(s,t)，s,t≥2。每line有s+1点，每point有t+1条line；非incident点p与line l有唯一共线投影q∈l及过p/q的line m。设真实spread把points分为互不交lines。未填图U的顶点为全部(point,line)，交叉incidence `q∈l` 且 `p∈m` 给邻接，排self。

置`R=st+1, δ=(s+1)(t+1)`。point数(s+1)R、line数(t+1)R，U阶δR²。incidentflag的self项去掉使度δ−1，其余度δ。projection给old-old≤3。为每spreadline添加一个helper，连接该line所有point的所有incidentflags，共δpins；spread共有R条，partition全部flags，filled H阶`δR²+R`全δregular、D3。实际labels和projection前提需绑定，名字GQ不替代它们。

若P为p点partialovoid（每line≤1P点），中心`P×spread`共有pR。一个oldvertex若邻接两中心，line上的P唯一性与point的spread唯一性迫两中心相同，故完整N_H两两不交；可相邻，不要求independent。k份clone负载≤k，阶`δR²+R+kpR`、最大度数δ+k。

实例q4：s=t=4,R17,δ25,H7242，P17给289centers，新7531。q7：s=t=7,R50,δ64,H160050，P33给1650centers，k1..15。q8实际balanced(8,8)与Payne(7,9)来自不同几何，不把field／projection表互换。

## 7. Diagonal省边加hub：是新定理，再成为G1克隆

使用上项实际P/spread，保filledH所有边。每(Ppoint,spreadline)的clone仅复制U中的邻域，省去p条diagonal clone→filler边；另加hub，邻接全部R fillers。每block有pR clones＋1hub；取整数 `k≥1`，k个block都按此规则。

阶与边数：

```text
n = δR²+R+k(pR+1)
m = δ(δR²+R)/2 + k(δpR+R−p)
maxdegree = δ+k
```

令`Q=δpR−p`，度分布为：δ+k有Q+R点；δ有`δR²−Q+k(pR−p)`点；δ−1有kp个diagonalclone；R有k个hub（数值度重合时合并）。

证明按旧U、filler、diagonal／off-diagonal clone、hub分类，原U/H内的路线承担旧部分。`p>0`且`k≥1`时，任取一个hub和一个clone：它们不相邻，hub邻域全在F、clone邻域全在U，故无共同邻点，距离不可能≤2。全覆盖证明又给出长度≤3路线，因此这对点距离恰3，是非D2见证。不能把hub映到某个旧H点假用collapse。

每个prefix的直径上界依据该点插入时已经存在的覆盖路线，不从终图删除顶点倒推。k>1严格等同在实际G1上克隆首block全部新增角色（pR个clones和首个hub）的完整G1邻域；这些邻域互不交，再用fullN定理。q8的G1=346516，pR+1=4226，不是4225。

完整证明：[general note](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md)。实际小例与命令见[冻结与diagonal案例](../examples/frozen-clones-and-diagonal.md)。

## 8. D2保边helper：单点闭支配与合作预算

源G直径≤2，spare b(v)=d−degG(v)，T为b>0。单新点只接S、保边，合法iff `S⊆T, |S|≤d, N_G[S]=V`。

任意helper图K，helper i接旧pins S_i，旧诱导图不变，则helper-old准确条件是 `V=N_G[S_i] ∪ ⋃_{j∈N_K(i)}S_j`，度为`|S_i|+degK(i)≤d`，oldload≤b。还需helper-helper距离；K为clique时自动，K无边时需各自支配且pins两两相交。

饱和旧目标 v只能借旧spare邻点给每个helper提供两步路，必要 `h≤Σ_{u∈N(v)∩T}b(u)`。若N[T]漏一饱和target，同cap保边任意非空helper增广均失败，即使允许额外old-old边；这不是一般D2无解。完整Brown57/91容量及奇偶证书见下页。

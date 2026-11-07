# 从临界取等到实际端点相容

这是当前插件对 2026-11-03/04 新原稿的执行说明，数学保证保持 **same-session / unreviewed / unaccepted**。它给作者可复用的证明动作和检查接口，不替代独立数学验收。原件完整保存于 [新包](../../../archive/n7-20261103/README.md)；旧 archive/source 不改写。

下文 `R` 指 [新包研究目录](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/)。主要原件为：

- [全供给](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md) §1–4：同一实际母体的取等、角色单射、共同核和锁根次序。
- [替锁](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) §1–4：排除整个 n=3b+1 层。
- [依赖及 through](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)：AUD-01…16 与 w=1 的单独排除。
- [t=0](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)：下一人口层重新核算和失败边界。
- [regular 共根](../../../archive/n7-20261103/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_COMMON_ROOT_EXCESS_EXCLUSION_20261104.md)：条件加权定理、三个余支和真实 canonical 双插点反例。

## 1. 接到哪个问题才执行

route-loop 的触发是：已有整数上界 n≤3b+1，目标仅差一单位，且原推导含非负缺额、角色数/实际点数或匹配损失。先追等号，不开更大样本搜索。prove 收到的是同一 X 的临界假设及下列接口；verify 收到证明正文和每条接口的来源或实际证明。若请求只是下一层 n=3b，直接进入 §5，不能沿用 n=3b+1 自动结论。

caller 提供原对象、路径颜色/点序定义、有效共同整数容量 b、当前 n/w/t、可用进口、任务写域和返回点。没有显式色表时，这是符号推导；不能伪造一份已经存在的临界实例。

对任意 767 母体 X（禁 B6/R7/weak7），按同一 X 定义 ambient R6 首末点 S,T，I=S∩T，P=S\T，Q=T\S，D=X\(S∪T)。只在 D 内重算 R5 首末点 U,V，w=|U∩V|，|D|=b+q。M0 给含 D 的实际 766 核 H_L,H_R，缺额 α,β，owner A_H⊆P、B_H⊆Q，锁 Ω、Ψ；每个 owner 有唯一对应锁，但最初允许同锁多个 owner。设 a=|A_H|、d=|B_H|、o=|Ω|、p=|Ψ|，u=a−o≥0、v=d−p≥0。

n=3b+1 先经已用加权界 n+w≤3b+1 得 w=0；增强根分类再给共同根 z∈I\Γ，Γ=(Ω∪Ψ)∩I，以及 I 内锁序。这里需要参数无关 M0、加权根分类和实际帽/扇；不能单凭 z∈I 声称增强根条件。原依赖见替锁 §1 和 AUD-02/03。

## 2. 把整条取等链回收到同一对象

从实际 H_L,H_R 重算 C=End_R5(H_L)、C'=Src_R5(H_R)，Z_+=C∩D、Z_−=C'∩D，c_±=|Z_±|。令 P_H=P∩H_R、Q_H=Q∩H_L，基础核

K_−=Z_− ⊔ P_H ⊔ B_H，K_+=Z_+ ⊔ Q_H ⊔ A_H，
κ_−=q+β−c_−，κ_+=q+α−c_+。

它们须先证是实际 756；整数式不承担这一步。取 B=(I∩(−∞,z))\Ψ、A=(I∩(z,∞))\Ω。在 K_−⊔B 的**全部实际** R6 末对中收前驱 L，在 K_+⊔A 的全部实际 R6 首对中收后继 R。保留每个端口的一条实际路径见证。有效增强根排除其它角色，得 L⊆Z_−、R⊆Z_+、L<z<R。容量加 König 给

ell0=|B|−κ_−≤|L|，r0=|A|−κ_+≤|R|。

初步 ell0/r0 可负，不提前判参数非法。任意 R5(l→k) 若 l∈L,k∈R，兑现两侧外对 (l,r),(s,k)，满足 l<r<z<s<k；R6 两帽迫两个蓝三元组，给同端 B4，违反 weak7。这排除的是全部实际 L→R 路径，不只是选中匹配的边。

在 D_all=H_L∩H_R=D⊔A_H⊔B_H 定义**角色**容器

U_c=Z_− ⊔ A_H ⊔ (C'∩B_H)，V_c=Z_+ ⊔ B_H ⊔ (C∩A_H)。

它们分别包含全部实际 R5 首、末点。源/末是两个角色副本，即使对应同一个实际点也先分别保留。令 U0=c_−+a+v、V0=c_++d+u、m=q+a+d≥0。纤维极端代表论证给 |U_c|≤U0、|V_c|≤V0；人口账给 ell0+r0=U0+V0−m。

角色覆盖 C_roles=(U_c\L)⊔(V_c\R)，实际点像 C_phys 击中全部 R5 的端点。删去它后是换色 756，容量给下界；于是

m ≤ |C_phys| ≤ |C_roles| = |U_c|+|V_c|−|L|−|R| ≤ U0+V0−ell0−r0 = m。

执行时将 |C_roles|−|C_phys|、U0−|U_c|、V0−|V_c|、|L|−ell0、|R|−r0 分别解释为非负量。整链取等同时消灭所有这些量，得到实际像单射、两容器取满及外端口供给取满。不能把不同母体或不同选择上的等号合并。

全部左 owner 已在源覆盖，若又在 C∩A_H 就重复为末覆盖；右侧反序。因此 C∩A_H=C'∩B_H=∅，配合容器取等得 u=v=0，每锁单例、a=o、d=p。再收 D 内实际端点覆盖

C_D=(U\L)⊔(V\R)，|C_D|=q，K=D\C_D，|K|=b，
Z_−\L=U\L，Z_+\R=V\R。

q≥0 是结论；不是先对任意 D 假设。K 无 R5。K 加任何外点 x 会迫一条使用 x 的 R5，但这一句仍不指定 x 的位置或兼容端点。

## 3. 先兑现交换所需的锁序和旧根排除

用 K⊔A_H 的全部 R5 首末图：R5 不可终于 A_H，也不能两端都在 K（否则 L→R），故每条从 A_H 到 K∩R。若匹配不足 a，删少于 a 个角色实际点将留下超过 b 点的换色 756，矛盾。取得饱和 A_H 的实际 R5 匹配；右侧同理。与饱和外供给匹配合成锁→根注入，逐锁得 z<s_ω<ω 和 ψ<r_ψ<z。因此**整个** Ψ<z<Ω，包括 I 外锁。

旧末根 Ehat 的定义是实际 R6 末对两点都在 W=S\Ω；旧首根 Fhat 反序在 W'=T\Ψ。必须独立取得 z∉Ehat∪Fhat，不能用最终替锁矛盾反证其自身进口。实际满核

J_−=P_H⊔B_H⊔B⊔(U\L)，|J_−|=b

来自删除全部 L 后击中所有左域 R6。旧根排除在旧根稿 §1–3：假定首对 (z,t0)，owner 首对限制排 t0∈B_H；J_−加普通 t0 无 B5，容量迫 R6 终于 t0，帽迫首点>z，第二点落 S∪U，增强扇前接 z 产生不可能的旧末点。反序排旧末根。返回时给原件或这段实际证明，不能仅写“对称可得”却遗漏新增异常角色。

## 4. 替锁、容量迫证和同一端点

现在才在同一母体定义 F=(J_−\B_H)⊔Ψ⊔{z}。逐组证明不交：Ψ在 H_R 外，B 避开 Ψ，z避开 J_−和锁，U\L在 D。d=p 使 |F|=b+1。F⊆S∪U；任何这些点若是 ambient B5 末点，与其出 R6（S）或 D 内出 R5（U）连接，蓝桥给 B6，红桥给 R7 或终于 D 的 R6。因此 F 无 B5，weak7 继承。

756 容量**迫存在一条实际 R6**，不要求它经过新点 z。由 F∩T=B⊔(Ψ∩I)⊔{z} 定位末点 r≤z，设实际末前驱为 j。

- j∈S：j<r≤z，整个 Ω 在右，j,r∈W，故 r∈Ehat；增强极值与旧共根排除均已否定 r≤z。
- j=u0∈U\L：K⊔{u0} 恰 b+1 点，继承 B6/weak7 禁形，换色容量迫实际 R5 P0。P0 避开 C_D\{u0}，所以精确**端点**覆盖迫其一个端点为 u0；w=0 排其末点身份。因此 P0 真从 u0 到某 k∈V\C_D⊆R。取兑现**同一个 k**的外首对 (s,k)，得到 u0<r≤z<s<k。两帽给 B4(u0,r,s,k)，与 P0 同端且长度和 4+5=9，矛盾。

两类穷尽 F。q=0 时 u0∈C_D 已不可能；R为空时被迫 k∈R 直接矛盾；d=p=0 时 F仍是 J_−加 z，原证明照用。以这些实际域排整个 n=3b+1 层，整数性得 n≤3b。独立合法 chart 归约再给 N777=N767+1；几何包含与阈值定义再加一。b25时分别为75、76、ES≤77，均沿用原工作稿状态。

verify 的返回应明确闭了哪一箭头：接口的符号推导、固定实例的路径检查、历史容量进口或完整原命题。成功算出 b+1 不证明 F 无 B5；迫一条路径不证明所需端点；同端 B3+R5只有8，不是 weak7。

## 5. 新一层先重新算松弛：不能无条件继承

原 through 稿证明 n+1[w>0]≤3b，故 n=3b 时 w=0,t=n+w−3b=0。t≥1 的共根分类没有覆盖全部 t=0：要重新分严格交错、分离、共根、根族空。

在 **regular 共根**子类，额外要求增强根族 E+,F+非空，min E+=max F+=z∈I\Γ，Ω∩I>z、Ψ∩I<z。按实际域重新收全部 L,R。定义

e_L=|L|−ell0，e_R=|R|−r0，
Ctilde=(Z_−\L)∪(Z_+\R)，H=(Z_−\L)∩(Z_+\R)，
h_U=|H∩U|，h_V=|H∩V|，h0=|H\(U∪V)|，d_D=|Ctilde|−q。

这些数非负，w=0使三种重合点互斥，精确人口式为

n+(u+h_U)+(v+h_V)+e_L+e_R+h0+d_D=3b+1。

C_D端点覆盖仍给 h0≤d_D。原 regular 稿 §3 在反设 n+max(u+h_U,v+h_V)>3b 下，先由整数性迫 e_L=e_R=d_D=h0=0 和一个单侧权重为零，重建实际满域，再沿 §4 的替锁逻辑排除；它处理全部异常重合点，而非只处理一个。结合 h0≤d_D 得

n+Λ≤3b，Λ=h0+max(u+h_U,v+h_V)。

返回给 route-loop 的是这个**有条件**工具；不能将 Λ换成w。n=3b时仅剩 e_L=1、e_R=1、d_D=1 三支：前两支有一侧 J只有b−1，加入旧邻点仅到b，下一次加入z允许被迫R6从z开始；第三支 Ctilde删出的核只有b−1，不代表所有R5自由核都这么小。这些是真实缺口，不能计为反例实现或全局≤74。

## 6. 失败见证怎样决定停止或重拆

**逐点供应不够（全供给 §7）。** 取严格块 L5<z<R5，三元组全在 L5∪{z} 或 {z}∪R5则红，其余蓝。全部packet合法，最长R6/B4，同端长度和≤8。S={min L5,z}、T={z,max R5}、I={z}；D=K去掉两个外端和z后有8点且无R5。每个外点x使K+x有R5，但没有严格跨左右的R5，增强根E*=F*=∅。它反驳“中性核逐点饱和+z∈I⇒端点相容”。它没有临界人口、有效增强共根或b25饱和，不能反驳带这些条件的新引理。

**单点可加不够（regular稿附录C）。** 在[10]取 C1={1,2,3,4}、C2={4,5,6,7}、C3={7,8,9,10}，三元组同属某Ci则蓝，其余红。实际757，canonical A为没有B4末点的{1,2,3,5,6,8,9}。A+7和A+10各无B4，A+{7,10}含C3；且7,10都在canonical B\A（B去掉R6首点{1,2}）。这是原canonical单点兼容命题的真实反例。下一动作必须检查同时用两个新点的全部B4，或换成真正联合交换。

**取等层换了（t=0稿§4）。** regular共根的零锁补偿时，覆盖上界允许 m+1；不能复用m夹等号迫单射。严格交错的K可保留最早owner，不能再当纯中性域。分离根碰在一点时只得B3+R5=8，必须另外兑现一个实际顶点。三个失败分别指向预算、身份、路径长度，适用的新假设必须针对相应缺步。

仓库 [check_strategy_examples.py](../../../tools/check_strategy_examples.py) 有界枚举前两个固定反例的全部递增路径和packet，检查这些准确失败，不检查全称75/76证明。使用方法见 [certificate](../../happy-ending-certificate/SKILL.md)。新失败交任务wiki，保留原输入、被否定句及额外条件；archive保持历史。

## 7. 交回原 caller

返回一段可直接接回当前义务的内容：原X和各诱导域、实际/角色区分、容量进口、非负松弛与零值结论、合法换入换出、被迫路径及精确端点、成功关闭的子类或失败见证、保证状态及剩余箭头。route-loop 据此选择取等排除/联合交换/重算新层；prove 消费具体引理；certificate 核具体接口后交base verify装配；不自行改canonical claim或启动整卷验收。

# h=6双C端口：完整父点缺陷行与两特殊父类的容量

2026-10-19。**Local only：独立纯纸面推导，无计算、Lean或直接外审。** 只处理 [传播稿§8](NONADJACENT_DOUBLE_DEFECT_PROPAGATION.md) 的分支：两根无三角、所选非邻双缺陷在两端孤立，h=6，$X=\{a,P\}$、$Y=\{b,Q\}$，两个不同R端口a、b均在C，且 $\tau(W)=2$。P、Q分别是V、U中唯一UV度为2的点。继承真实缺陷行和4、条目至多2及原边共同邻点至多1。

记 $L=N_U(a)$、$N_U(b)=\{z\}$、$N_V(a)=\{w\}$、$M=N_V(b)$。已有 $|L|=|M|=2$、$z\notin L$、$w\notin M$；令 $U_0=U\setminus(L\cup\{z\})$、$V_0=V\setminus(M\cup\{w\})$。两点p、q为W中的额外重复点，均邻a、b。三组Wi不交、独立；各 $\delta_i$ 总量2，故 $\tau(C)=4$。

## 1. U、V完整缺陷行

对 $x\in U$，写 $C_x=N_C(x)$。由于W无U/V邻边，

$$|C_x|=7-d_V(x),\qquad
\Delta(x,V)=|C_x|+d_V(x)-5+\mathbf1_{\{x=z\}}
=2+\mathbf1_{\{x=z\}}.$$

额外一项来自b：它有两个V父点，只有当x=z时，在跨V共同邻点总量中比一次C关联多计1。两个U点共有的C邻点只能是a，而共有V邻点的额外贡献只能来自P。因此

$$\Delta(x,U)=\mathbf1_{\{x\in N_U(P)\}}+\mathbf1_{\{x\in L\}}.$$

加上 $\Delta_{xv}=\mathbf1_{\{x=Q\}}$，对u及S的缺陷均为0，完整行和给

$$\boxed{\Delta(x,R)=
2-\mathbf1_{\{x=z\}}-\mathbf1_{\{x=Q\}}
-\mathbf1_{\{x\in N_U(P)\}}-\mathbf1_{\{x\in L\}}.} \tag{1}$$

对 $y\in V$ 的对称式为

$$\boxed{\Delta(y,R)=
2-\mathbf1_{\{y=w\}}-\mathbf1_{\{y=P\}}
-\mathbf1_{\{y\in N_V(Q)\}}-\mathbf1_{\{y\in M\}}.} \tag{2}$$

这里R侧缺陷没有被预先删除，两个端口的多父点贡献也均保留。

## 2. 统一短排除：PQ不能是原边

若PQ是边，(1)、(2)的非负性迫

$$Q\in U_0,\qquad P\in V_0,\qquad
\Delta(Q,R)=\Delta(P,R)=0.$$

于是 $C_Q\cap C_P$ 必为空：若其中有c，原边Q–c已有共同邻点P，给 $\Delta_{Qc}\ge1$，矛盾。

另一方面，每个W点与Q不相邻，其全部共同邻点恰在C_Q。它与Q的缺陷为0，故 $e(W,C_Q)=18$。对C中每点三份闭邻覆盖相加给 $d_W(c)=3+\tau(c)$，而 $|C_Q|=5$，从而

$$18=3|C_Q|+\tau(C_Q)=15+\tau(C_Q).$$

即 $\tau(C_Q)=3$，同理 $\tau(C_P)=3$。两类不交却都包含于C，与 $\tau(C)=4$ 矛盾。因此

$$\boxed{PQ\notin E(G).} \tag{3}$$

这个排除覆盖本稿全部允许父色，没有选择p、q的两个额外C邻点如何配对。

## 3. 特殊父类交集只余两点或三点

先核逐点上界。端口a处 $d_X(a)\le1$，b处 $d_Y(b)\le1$，故两点τ均至多1。若普通C点c有 $\tau(c)\ge2$，逐点传播迫c同时邻a、b、P、Q；而它的H度为6，$d_W(c)=3+\tau(c)\ge5$，给 $d_C(c)\le1$，与a、b两个不同C邻点矛盾。因此C中τ处处至多1，四个C缺陷单位的端点全部不同。

现在不假定Q、P的R缺陷为零。完全相同的父类边计数仍给

$$\tau(C_Q)=3+\Delta(Q,W)\ge3,\qquad
\tau(C_P)=3+\Delta(P,W)\ge3.$$

记 $K=C_Q\cap C_P$。由 $\tau(C)=4$，

$$\tau(K)\ge2+\Delta(Q,W)+\Delta(P,W)\ge2.$$

结合τ逐点至多1、(3)，以及 $\mu(Q,P)=|K|\le3$，得到

$$\boxed{|K|\in\{2,3\}.} \tag{4}$$

若 $|K|=3$，则 $\Delta_{QP}=2$。Q行另有非邻点v处的1，P行另有非邻点u处的1；各自只剩一个单位，故该双缺陷两端孤立，且任何三角形所需的两个邻点单位都会超出行和4。因而Q、P可作为合法的新无三角双缺陷根。旧u、v分别在新U、V侧，所以新h只能为6或7；这里**没有保证h严格下降**，也没有将合法换根写成排除。

若 $|K|=2$，上面的全部不等式迫两点τ均为1、$\Delta(Q,W)=\Delta(P,W)=0$。四个C缺陷点准确分布为：K内两点、$C_Q\setminus C_P$中一点、$C_P\setminus C_Q$中一点。此时 $\Delta_{QP}=1$，不能据此把Q、P当作新的双缺陷根。

## 4. 交集仅有两份重复时，Q、P属于两套剩余父色

本节仍为本地纸面追加。反设 $\tau(K)=2$；这包括 $|K|=2$，也包括三点K中仅两点重复。由 $\tau(C_Q),\tau(C_P)\ge3$ 和 $\tau(C)=4$，两父类各恰有三份重复，故 $\Delta(Q,W)=\Delta(P,W)=0$；四个重复点恰为K内两点以及两个父类差集中各一点。点名额外W点为 $p\in W_2,q\in W_3$，对应 $\delta_2(q)=\delta_3(p)=1$。每份δ总量2且C上τ至多1，故它们各剩一个不同C支撑点，暂记为r2、r3。交换 $(s_2,Q)$、$(s_2,P)$ 分别给

$$1+\Delta(W_2,Q)=A_{r_2Q},\qquad
1+\Delta(W_2,P)=A_{r_2P},$$

所以r2属于K；对第三组同理，r3也属于K。可因此将K中的两个重复点记为 $\{c,d\}=\{r_2,r_3\}$，使

$$\delta_2=\mathbf1_{\{q,c\}},\qquad
\delta_3=\mathbf1_{\{p,d\}},\qquad
\delta_1=\mathbf1_{\{e,f\}},$$

其中 $e\in C_Q\setminus C_P$、$f\in C_P\setminus C_Q$，四个C点不同。这些点目前尚未被假定不是端口。

先由(1)、(2)和PQ非边得 $\Delta(Q,R),\Delta(P,R)\le1$。因此C_Q、C_P内部均独立：若同一父类内有边，其两个端点与父点构成三角，会在父点的R行贡献至少两个单位。

对e，逐点传播准确给

$$\Delta(U,e)=d_X(e)-\tau(e)=A_{ae}-1.$$

故 $a\sim e$ 且 $\Delta(U,e)=0$。由于 $e\sim Q$，若 $Q\in L$，三角a–e–Q将给 $\Delta_{eQ}\ge1$，矛盾。因此 $Q\notin L$。对称地 $b\sim f$、$\Delta(V,f)=0$、$P\notin M$。利用已有ab非边，再在端口处传播，

$$\tau(a)\le d_Y(a)=A_{ab}+A_{aQ}=0,\qquad
\tau(b)\le d_X(b)=A_{ab}+A_{bP}=0.$$

所以四个C缺陷点确实都不是端口，e、f现在各有唯一的两侧父点。

令y为e的V父点，故 $y\ne P$；f的唯一V父点则是P。s1的完整缺陷行仅在另两个S点及e、f处各取1。由于普通V点y没有来自u、v的缺陷，交换 $(s_1,y)$ 精确给

$$\Delta(W_1,y)=A_{ey}+A_{fy}=1. \tag{5}$$

若Qy为边，三角e–Q–y还给 $\Delta_{ye}\ge1$。另一方面y普通且邻Q，(2)给 $\Delta(y,R)\le1$；(5)的W1单位与C位置e的单位不同，矛盾。因此Qy非边。UV图在PQ非边时由两个三点路径加两条孤立边组成；y必为其中一条孤立边的V端。记它的唯一U配偶为x。对称地，f的U父点也是一条孤立边的U端。

最后反设 $P=w$。a此时邻P，而 $Q\notin L$、ab非边，逐点式给 $\Delta(V,a)=0$。若 $L\cap N_U(P)$ 非空，对应点与a、P构成三角，违反 $\Delta_{Pa}=0$。故L同时避开Q与P的两个U邻点；由于 $|L|=2$，L恰为两条孤立UV边的两个U端，特别地 $x\in L$。

现在e的唯一U父点是Q而不是x；非邻对e、x却同时经a和y有两条共同邻点路线，给 $\Delta_{ex}\ge1$，违反 $\Delta(U,e)=0$。因此 $P\ne w$；对称地 $Q\ne z$。结合前面的排除，得到

$$\boxed{\tau(K)=2\Longrightarrow
Q\in U_0,\quad P\in V_0,\quad \tau(a)=\tau(b)=0.} \tag{6}$$

## 5. 交集仅有两份重复的短矛盾

本节为新完成的本地纸面排除，不借用外部回执。继续反设 $\tau(K)=2$。由(6)、ab非边及两个根的逐点传播，

$$\boxed{\Delta(a,U\cup V)=\Delta(b,U\cup V)=0.} \tag{7}$$

保留y为e的唯一V父点，另记 $x_f$ 为f的唯一U父点；不要将它与§4中y的UV配偶混同。已知y、x_f分别是某条孤立UV边的V、U端，且 $a\sim e$、$b\sim f$、$\Delta(e,U)=\Delta(f,V)=0$。

首先 $w\ne y$：否则a、e、w构成三角，违反 $\Delta_{aw}=0$。同理 $z\ne x_f$。非邻对a、Q已有共同邻点e；若w邻Q，又有不同共同邻点w，违反 $\Delta_{aQ}=0$。故w不是Q的V邻点，且由(6)有 $w\ne P$，所以w也是一条孤立UV边的V端。对称地z不是P的U邻点，且 $z\ne Q$，也是孤立UV边的U端。因此

$$\{w,y\}\text{ 恰为两条孤立UV边的两个V端，}\qquad
\{z,x_f\}\text{ 恰为它们的两个U端。} \tag{8}$$

反设 $x_f\in L=N_U(a)$。按(8)，x_f的唯一V配偶只可能为w或y，且两种情况都矛盾：

- 若配偶为w，则a、x_f、w构成三角，违反 $\Delta_{aw}=0$。
- 若配偶为y，则e的唯一U父点为Q而不是x_f；非邻对e、x_f同时有共同邻点a、y，违反 $\Delta(e,U)=0$。

因此 $x_f\notin L$。结合既有 $z\notin L$、$Q\notin L$，而U恰由Q、两个孤立边端点z、x_f及P的两个普通U邻点组成，$|L|=2$ 迫

$$L=N_U(P).$$

但a不邻P，因为a的唯一V父点为w且 $w\ne P$。a与P遂经L中的两个不同点有两个共同邻点，给 $\Delta_{aP}\ge1$，与(7)矛盾。故

$$\boxed{\text{本稿完整双C端口、}\tau(W)=2\text{ 分支中，}\tau(K)=2\text{ 不可能；必有 }|K|=\tau(K)=3.} \tag{9}$$

该短排除没有选择两条孤立UV边的配对，也没有固定其余父色或C配边。加强到三点K中仅两点重复时，额外的非重复K点没有进入任何承重步骤；根与数学代理已逐行核对。结合§3，剩下的三点交集必给出合法无三角、两端孤立的新双缺陷根Q、P；尚不能保证换根后h严格下降或落入已关闭情形。本稿本身只到这一止点；后续完整排除见 [不同端口匹配定理](H6_DISTINCT_PORTS_MATCHING_THEOREM.md)，不再研究其覆盖的换根循环。没有新增求解、Lean或外审。

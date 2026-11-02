# h=6不同双C端口、W上无重复的纸面排除

2026-10-19。**Local paper：根提出闭合链，独立逐项核对成立；无新求解、Lean或直接外审。** 在 [不同端口匹配定理](H6_DISTINCT_PORTS_MATCHING_THEOREM.md) 的同一准确分支中，选择无三角形、两端孤立的非邻双缺陷根u、v，h=6，$X=\{a,P\}$、$Y=\{b,Q\}$，a、b是不同R端口。这里只反设

$$a,b\in C,\qquad \tau(W)=0.$$

不要求其他双缺陷孤立，不预设全图无三角形。继承实际缺陷非负、行和4、条目至多2，以及原图每条边至多有一个共同邻点。

Wi各六点、独立、不交，三对组间是完美匹配。每个W点H度7，无U/V邻边；普通C点H度6，端口a、b的H度5。令

$$L=N_U(a),\quad |L|=2,\quad N_V(a)=\{w\},\qquad
N_U(b)=\{z\},\quad M=N_V(b),\quad |M|=2.$$

本稿**允许 $z\in L$、$w\in M$**。这些交叠在当前分支尚未排除，以下不使用上一重复分支的父集不交结论。P、Q仍分别为V、U中唯一UV度为2的点。

## 1. 完整父点行与六个不同C重复点

对 $x\in U$，跨V共同邻点总量仅在x=z时因b的双V父点多1；同U共同邻点只从特殊V点P及双U端口a获得额外贡献。因此，无论父集是否交叠，

$$\Delta(x,V)=2+\mathbf1_{\{x=z\}},\qquad
\Delta(x,U)=\mathbf1_{\{x\in N_U(P)\}}+\mathbf1_{\{x\in L\}},$$

$$\boxed{\Delta(x,R)=2-\mathbf1_{\{x=z\}}-\mathbf1_{\{x=Q\}}
-\mathbf1_{\{x\in N_U(P)\}}-\mathbf1_{\{x\in L\}}.} \tag{1}$$

同理

$$\boxed{\Delta(y,R)=2-\mathbf1_{\{y=w\}}-\mathbf1_{\{y=P\}}
-\mathbf1_{\{y\in N_V(Q)\}}-\mathbf1_{\{y\in M\}},\quad y\in V.} \tag{2}$$

各 $\delta_i$ 总量2，且W上τ为0，故 $\tau(C)=6$。端口处 $\tau(a)\le d_X(a)\le1$、$\tau(b)\le d_Y(b)\le1$。若普通C点r有 $\tau(r)\ge2$，逐点传播迫r同时邻a、b，而 $d_W(r)=3+\tau(r)\ge5$、$d_H(r)=6$，使 $d_C(r)\le1$，矛盾。因此六个C重复单位全部位于不同点，并有

$$d_C(a)=2-\tau(a),\qquad d_C(b)=2-\tau(b). \tag{3}$$

## 2. 先恢复ab非边，不借用旧额外W点

记 $K=C_Q\cap C_P$。任意Q、P对的全部共同邻点恰在C，所以 $|K|=\mu(Q,P)\le3$。

反设ab为原边，写 $\varepsilon_a=\tau(a)$、$\varepsilon_b=\tau(b)$。普通C重复点共有 $6-\varepsilon_a-\varepsilon_b$ 个，其中至多三个属于K。每个不在K中的普通重复点，由

$$1\le A_{ra}+A_{rP},\qquad 1\le A_{rb}+A_{rQ}$$

至少须邻接a或b。故至少 $3-\varepsilon_a-\varepsilon_b$ 个不同普通点须占用端口的C边。但(3)扣掉边ab后，两端合计仅余

$$2-\varepsilon_a-\varepsilon_b$$

条到其余C点的边，少一条，矛盾。因此

$$\boxed{ab\notin E(G).} \tag{4}$$

## 3. PQ也不能为原边

若PQ为边，(1)、(2)非负迫Q不属于 $L\cup\{z\}$、P不属于 $M\cup\{w\}$，并给 $\Delta(Q,R)=\Delta(P,R)=0$。因此K为空：若r同时邻Q、P，原边Q–r已有共同邻点P，与 $\Delta_{Qr}=0$ 矛盾。

每个W点与Q的共同邻点恰在C_Q，故

$$18=e(W,C_Q)=3|C_Q|+\tau(C_Q)=15+\tau(C_Q),$$

即C_Q含三个不同重复点。它们均不邻P，逐点传播迫三点都邻a，与 $d_C(a)\le2$ 矛盾。因此PQ非边。由度序，UV图恰由两个三点路径及两条孤立边组成。

## 4. 任何重复点都不能只属于一个特殊父类

反设重复点 $g\in C_Q\setminus C_P$。逐点式给

$$\Delta(U,g)=A_{ag}-1,$$

故 $a\sim g$、$\Delta(U,g)=0$。g不是a；由(4)，也不是b，因此g有唯一的V父点y，且 $y\ne P$。若 $Q\in L$，三角a–g–Q违反 $\Delta(U,g)=0$，故 $Q\notin L$。在a处传播，得到

$$\tau(a)=0,\qquad \Delta(V,a)=0.$$

设g属于 $\delta_i$，其另一支撑点为f。W上没有重复，故f也在C；这里不要求f属于K或任何指定父类。s_i的完整缺陷行恰为另两个S点各1及g、f各1，所以对普通V点y交换给

$$\Delta(W_i,y)=1+A_{fy}\ge1. \tag{5}$$

若Qy为边，三角Qyg还在另一个R位置g给 $\Delta_{yg}\ge1$，而(2)对普通且邻Q的y给 $\Delta(y,R)\le1$，矛盾。因此y是两条孤立UV边之一的V端。

若 $P=w$，由 $\Delta(V,a)=0$ 知L不能与 $N_U(P)$ 相交，否则形成经过a、P的三角。L还避开Q，故L恰为两个孤立UV边的U端。取y的U配偶x，则 $x\in L$，非邻对g、x同时共有a、y，违反 $\Delta(U,g)=0$。故 $P\ne w$；a处另一逐点式随即给 $\Delta(U,a)=0$。

若w=y，三角a–g–w违反 $\Delta(V,a)=0$。若w邻Q，则非邻对a、Q同时共有g、w，违反 $\Delta(U,a)=0$。故w是另一条孤立UV边的V端；两条孤立边的V端恰为w、y。

L不能包含这两条边的任一U端x：若x的配偶为w，三角a–x–w违反 $\Delta(V,a)=0$；若配偶为y，非邻对g、x共有a、y，违反 $\Delta(U,g)=0$。L还避开Q，所以只能为 $N_U(P)$。但a不邻P，却经L两点共有两个邻点，违反 $\Delta(V,a)=0$。

因此不存在 $C_Q\setminus C_P$ 中的重复点；对称地也不存在 $C_P\setminus C_Q$ 中的重复点。上述链没有使用 $z\notin L$ 或 $w\notin M$。

## 5. 三个剩余重复点超出端口C度

对一般父点Q、P，边计数始终给

$$\tau(C_Q)=3+\Delta(Q,W)\ge3,\qquad
\tau(C_P)=3+\Delta(P,W)\ge3.$$

由§4，这些重复点全部在K。结合 $|K|\le3$ 和逐点τ至多1，K恰有三个点且全部重复。其余三个C重复点均不邻Q、P；逐点传播迫它们各自同时邻a、b，也自动排除它们是端口本身。因此a至少有三个不同C邻点，与(3)矛盾。

故本稿完整 $a\ne b$、$a,b\in C$、$\tau(W)=0$ 情形不存在。结合 [不同端口匹配定理](H6_DISTINCT_PORTS_MATCHING_THEOREM.md) 对 $\tau(W)=2$ 的排除，得到

$$\boxed{h=6\text{ 的两个不同R端口不能同时属于C。}}$$

这是明确条件分支的纸面排除；尚未排除至少一个端口在W的不同端口情形，也未排除整个h=6或61点目标。没有固定父色、UV配对或C图模板，未修改主传播稿、源码或求解输入。

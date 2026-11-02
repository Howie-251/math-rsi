# ε=1共享星：共同配边与η=0的局部矛盾

2026-10-18。**纸面证明：根独立核对及本稿直接复核已接受。** 实际回执：reviews/dd82/20261018_epsilon1_shared_star_review.json（cell660终态，gemini-3.8-flash-high/high）。此处η1未纸面关闭是本稿方法止点；后续完整CNF已经独立LRAT检查，见EPSILON1_CHECKED_EXCLUSION.md。 不计算、枚举、修改输入或求解。使用 [交叠packing结构](EPSILON1_OVERLAPPING_PACKINGS.md)、[精确端口式](ADJACENT_DOUBLE_PORT_PROPAGATION.md) 和 [AP两单位预算](SIX_STAR_AP_DEFECT_BUDGET.md)。下述收紧需要真实端口，不声称仅靠两份总量为2便能推出。

沿用A、B两六packing，独立补集P、Q，$C=A\cap B$、$|C|=t$、$|P\cap Q|=\eta$，以及 $R=Z\setminus(A\cup B\cup P\cup Q)$。对 $c\in C$，同一组四片叶为 $L_c=N_H(c)\subset R$；令 $R_C=\dot\bigcup_cL_c$、$R_0=R\setminus R_C$。

## 1. 每个R点恰接一个P、一个Q，故t=1+η

记r的实际S/T父点为x(r)、y(r)。r不在A、Q，所以x(r)不是K列p的两个邻点；r不在B、P，所以y(r)不是K行q的两个邻点。r也不在两种端口支持P、Q。精确邻居式因此给出

$$\boxed{d_P(r)=1+\gamma_{pr}-\mathbf1_{r\in P}-K_{x(r),p}=1,\qquad
d_Q(r)=1+\beta_{qr}-\mathbf1_{r\in Q}-K_{q,y(r)}=1.} \tag{1}$$

两个邻点可能是同一个实际点，仅当 $\eta=1$ 且它是 $w=P\cap Q$。不能把这种情况计成两条边。

P的20条H边中，到 $B\setminus A$ 恰有 $5-\eta$ 条，到 $Q\setminus P$ 恰有 $1-\eta$ 条，其余都到R。式(1)及 $|R|=13+t+\eta$ 给出

$$20=(5-\eta)+(1-\eta)+(13+t+\eta),\qquad
\boxed{t=1+\eta.} \tag{2}$$

所以 $(t,\eta)=(2,0),(1,1)$ 不可能；此结论没有固定任何双色或叶序。

## 2. 共享星的两份缺陷都恰为1

为避免与packing B混淆，记完整61图的真实缺陷矩阵为
$\Delta=A_{\rm full}^2+A_{\rm full}-7I-J$。它非负，每行总量4。

每片共享叶恰有一条P边、一条Q边，故
$e(L_c,P)=e(L_c,Q)=4$。c与P中任何点不共S/T父类，也没有H直接边，因此

$$\Delta_{cp}=(H^2)_{cp}+\mathbf1_{f(c)=f(p)}
+\mathbf1_{g(c)=g(p)}-1.$$

P是双色横截面，对其求和得到 $4+1+1-5=1$；B–Q完全对称。于是

$$\boxed{\sum_{p\in P}\Delta_{cp}=\sum_{q\in Q}\Delta_{cq}=1
\quad(c\in C).} \tag{3}$$

每个共享中心因此各占去AP、BQ两单位总预算中的一个单位。若 $\eta=1$，两份单位可能重合在w；令 $b_c=\Delta_{cw}\in\{0,1\}$，准确并集预算为

$$\sum_{z\in P\cup Q}\Delta_{cz}=2-b_c. \tag{4}$$

令 $h_c=|L_c\cap N_H(w)|$，$\delta_c=\mathbf1_{f(c)=f(w)}+
\mathbf1_{g(c)=g(w)}$。同一真实两步路线和双色局部双射还给

$$\boxed{h_c+\delta_c=1+b_c,\qquad h_c\delta_c=0.} \tag{5}$$

故c、w不同两色时 $h_c=1$或2；同一种色时 $h_c=0,b_c=0$；同两色时 $h_c=0,b_c=1$。这是同一四叶组的准确配边限制，不是各自独立的颜色匹配。

## 3. η=0产生六单位大于四单位的矛盾

此时式(2)给t=1，只有一个共享中心c及四片共享叶。P、Q不交。每个 $r\in R_0$ 已有两个不同中心邻点，再由(1)接一个P点、一个Q点，四度已满，故 $d_{H[R]}(r)=0$。每个 $r\in L_c$ 已有中心c及P、Q两邻点，恰剩一条R边。因此

$$H[R]\text{恰是 }L_c\text{上的两条匹配边，加其余孤立点。}$$

每片叶r与其匹配伙伴均邻接c，所以真实边cr属于一个三角形，$\Delta_{cr}\ge1$。四片叶给c至少四个缺陷单位；式(3)又在互不相交的P、Q中各给一个单位。这三个顶点集合不交，故

$$4=\sum_z\Delta_{cz}\ge4+1+1=6,$$

矛盾。**本地纸面结论：真实 $\varepsilon=1,\eta=0$ 分支不可能。**

剩余 $\eta=1,t=2$ 时，w有四个R邻点，记 $W=N_H(w)$。同样逐点计度仅给

$$d_{H[R]}(r)=
\begin{cases}
1+\mathbf1_{r\in W},&r\in R_C,\\
\mathbf1_{r\in W},&r\in R_0.
\end{cases}$$

这里 $|R_C|=|R_0|=8$、$|W|=4$，所以 $H[R]$ 有六条边。两颗共享星已用完AP、BQ各自的两个缺陷单位，其余中心相应行均为零；式(4)–(5)仍须作用于同一叶配边。本稿未从这些条件得到 $\eta=1$ 矛盾或实际构造，到此停止。所有条件已隐含于完整ε=1编码，不修改该输入，也不据此启动子族求解或更高阶分类。

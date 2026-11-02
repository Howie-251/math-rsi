<div class="result-strip"><div><span>六元超图下界</span><strong>64 → 67</strong><small>相对 64 增加 3</small></div><div><span>原始染色结论</span><strong>66 条边必可染</strong><small>任意有限简单六元超图</small></div><div><span>验证范围</span><strong>独立数值复算</strong><small>完整计算机辅助证明 · 尚未 Lean</small></div></div>

<p class="proof-status">完整计算机辅助证明 · 独立数值复算 · 尚未 Lean</p>

<a id="main-proof"></a>


# 六元超图的 Property B 下界：$m(6)\ge67$

## 1. 原命题与证明结构

**定义1.1。** 有限简单六元超图是二元组 $H=(V,E)$，其中 $V$ 有限，$E$ 是互不相同的六元顶点子集组成的集合。它具有 Property B，是指存在 $\chi:V\to\{\mathrm{红},\mathrm{蓝}\}$，使每条原边同时含两种颜色。$m(6)$ 是不具有 Property B 的有限简单六元超图的最少边数。

**目标命题T67。** 每个有限简单六元超图若满足 $|E|\le66$，便具有 Property B；等价地，$m(6)\ge67$。

**证明性质。** 本文给出覆盖任意有限简单六元超图的计算机辅助证明。选点、度数分流与概率充分条件均有数学证明；有限计算仅用于完整局部迹类型的精确有理不等式，全部实际使用域另有独立重建与概率复算。本文尚无 Lean 形式化。数学与数值证据分别列于第9节，最终审阅另见审计记录。

**定义1.2。** 记 $P_v$ 为下述内部命题：任意恰有 $v$ 个顶点、恰有66条边、覆盖每个不同顶点对的有限简单六元超图都具有 Property B。

**主定理1.3。** 任意有限简单六元超图，若边数至多66，则具有 Property B。因此 $m(6)\ge67$。

证明先将假定反例归约为27–44点、恰66边的点对覆盖超图，再用第6、7节逐支建立全部 $P_v$，最后回到原染色。主定理不要求原输入预先满足点对覆盖、度数、顶点数或证书假设。

全文记

$$d(x)=|\{A\in E:x\in A\}|,\qquad\lambda_{xy}=|\{A\in E:\{x,y\}\subseteq A\}|.$$

下文的点对覆盖、度数及锁点条件都在同一个实际反例内部推出，不作为原目标的附加条件。

## 2. 从任意原始反例到27–44点

**引理2.1。** 若T67为假，则存在一个不具有 Property B 的简单六元超图，满足

$$27\le v\le44,\quad |E|=66,\quad\sum_xd(x)=396,\quad
 d(x)\ge\left\lceil\frac{v-1}{5}\right\rceil,\quad\lambda_{xy}\ge1\ (x\ne y).\tag{2.1}$$

**证明。** 在边数至多66的所有反例中选顶点数最少者。若不同点 $x,y$ 从不同时属于一条边，则将其识别。每条边仍有六个不同像点，重复像边仅保留一次。所得简单六元超图的边数不增加，任何合法染色拉回都会染好原超图，所以所得仍是反例，违背顶点数最小性。故原反例覆盖每个点对。

对每个点求共度和，得到

$$5d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,$$

进而 $v\lceil(v-1)/5\rceil\le6|E|\le396$。该整数函数非减，而 $45\lceil44/5\rceil=405>396$，故 $v\le44$；端点44不能遗漏，因为 $44\lceil43/5\rceil=396$。

当 $v\le10$，把顶点分成两个大小均至多五的颜色类即可。当 $11\le v\le26$，均匀选大小为 $\lfloor v/2\rfloor$ 的红色类。固定六元边单色的概率为

$$p(v)=\frac{\binom{\lfloor v/2\rfloor}{6}+\binom{\lceil v/2\rceil}{6}}{\binom v6}.$$

完整十六个整数的精确值如下；每行同时适用于所列两个点数。

|$v$|$66p(v)$|
|---|---:|
|11,12|$1/7$|
|13,14|$4/13$|
|15,16|$6/13$|
|17,18|$132/221$|
|19,20|$231/323$|
|21,22|$264/323$|
|23,24|$396/437$|
|25,26|$792/805$|

各值小于一，故并集界给出没有单色边的染色，排除这些点数。上述直接有理计算由 [base_domain_check.py](context/propertyb-m6-67-progress-20261029/root/base_domain_check.py) 独立执行并保存在 [BASE_DOMAIN_CHECK.json](context/propertyb-m6-67-progress-20261029/root/BASE_DOMAIN_CHECK.json)。

此时 $27\le v\le44$，且 $\binom v6\ge66$。若原边数不足66，补入不同的新六元边直至恰66条。补边不改变顶点集，保持点对覆盖及不可二染。以后全部度数、共度及边迹均指这个补边后的同一实际超图，于是得到(2.1)。∎

## 3. 原染色算法及可计算的严格充分条件

本节复用并重述 [六元66下界证明](context/propertyb-m6-66-20261029/PROOF_M6_GE66.md) 第3节的机制；该机制本身不依赖总边数65。此处所有边重数之和一律为66。

**定义3.1。** 固定不同实际锁点 $S=(x_0,\ldots,x_{s-1})$ 及不同位置 $p_0,\ldots,p_{s-1}\in\{1,\ldots,v\}$，将其余 $N=v-s$ 个实际顶点均匀排列在其余位置。对指标子集 $T\subseteq\{0,\ldots,s-1\}$，令 $\ell_T$ 为恰含这些锁点的实际边数，$r_T=6-|T|$。因此 $\ell_T\ge0$、$\sum_T\ell_T=66$。

**引理3.2（失败见证）。** 按给定排列初始全部染红，依次处理顶点；当前点若是一条当前全红边的最后点，便改蓝。最终没有红色单色边。若存在蓝色单色边，则有不同原边 $A,B$ 及点 $z$，使

$$A\cap B=\{z\},\qquad z\text{ 是 }A\text{ 的最后点和 }B\text{ 的最早点}.\tag{3.1}$$

**证明。** 最终全红边的最后点在处理时必会改蓝，矛盾。若 $B$ 最终全蓝，取其最早点 $z$；$z$ 改蓝时有一条仍全红且在此结束的边 $A$。$A\setminus\{z\}$ 全在 $z$ 前，$B\setminus\{z\}$ 全在 $z$ 后，故交点唯一。∎

**定义3.3。** 在位置 $h$，记 $a_h,b_h$ 为前、后自由位置数，$I_h^-,I_h^+$ 为前、后锁指标集。$e_h(T),f_h(T)$ 是一条实际 $T$ 型边在 $h$ 结束、开始的条件概率；$w_h(T,U)$ 是固定有序单交原边对、类型为 $T,U$ 时形成(3.1)且共同点在 $h$ 的概率。

自由位置上的精确公式为

$$e_h(T)=\frac{r_T\binom{a_h}{r_T-1}}{N\binom{N-1}{r_T-1}},\qquad
f_h(T)=\frac{r_T\binom{b_h}{r_T-1}}{N\binom{N-1}{r_T-1}},$$

分别要求 $T\subseteq I_h^-$、$T\subseteq I_h^+$ 及 $r_T\ge1$，其余为零；并有

$$w_h(T,U)=\frac{\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}}
 {N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}},\tag{3.2}$$

要求 $T\subseteq I_h^-$、$U\subseteq I_h^+$、$r_T,r_U\ge1$、$r_T+r_U-1\le N$，否则为零。

若 $h=p_j$，则

$$e_h(T)=\frac{\binom{a_h}{r_T}}{\binom N{r_T}},\qquad
f_h(T)=\frac{\binom{b_h}{r_T}}{\binom N{r_T}},$$

要求 $j\in T$ 且其余锁点分别全在前、后；并有

$$w_h(T,U)=\frac{\binom{a_h}{r_T}\binom{b_h}{r_U}}
 {\binom N{r_T}\binom{N-r_T}{r_U}},\tag{3.3}$$

要求 $T\cap U=\{j\}$、$T\setminus\{j\}\subseteq I_h^-$、$U\setminus\{j\}\subseteq I_h^+$、$r_T+r_U\le N$，否则为零。超出二项式容量的取值为零。

这些公式按“固定共同点占位，再放前方及后方互不相同顶点”的条件抽样直接得到，完整推导见所引第3节引理3.2。定义

$$A_h=\sum_T\ell_Te_h(T),\quad B_h=\sum_T\ell_Tf_h(T),\quad
 C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})w_h(T,U).$$

$C_h$ 给全部不同有序边对赋非负记账权；实际非单交对不会成为失败见证，其虚记权可以依法扣除。

**引理3.4。** 若锁点位置有合法非负扣除量 $D_h$，不大于该位置实际非单交边对的总记账权；自由位置取 $D_h=0$，则

$$\Pr(\text{失败})\le U:=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}.\tag{3.4}$$

特别地，$U<1$ 给出原超图的一份合法染色。

**证明。** 位置 $h$ 的见证事件分别蕴含某边结束、某边开始，以及某个实际有序单交边对的见证。三次并集界分别给出括号中的三个上界。再按位置求并集界并用引理3.2。条件排列空间是实际有限顶点的非空均匀空间；失败概率小于一意味着至少一份排列成功，其贪心输出逐条染好当前实际全部66条边，也就染好补边前的每条原边。∎

## 4. 同一实际坏对的三种扣除

**引理4.1（链接配额及共同向量）。** 固定锁 $j$，取经过它而避开锁指标集 $R$ 的实际边，数目为 $f_{j,R}$。删去该锁后，得到至多 $v-1-|R|$ 点上的不同五元集合。若其中有 $Q$ 个相交无序集合对，则

$$5f_{j,R}\le v-1-|R|+4Q,$$

因为每点重数 $a$ 满足 $a\le1+\binom a2$，不同五元集合的交至多四点。因此可取

$$q_{j,R}=\max\left(0,\left\lceil\frac{5f_{j,R}-(v-1-|R|)}4\right\rceil\right).\tag{4.1}$$

令 $z_{TU}$ 为含锁 $j$ 的无序迹型格内实际非单交原边对数，容量为 $c_{TT}=\binom{\ell_T}{2}$、$c_{TU}=\ell_T\ell_U$。同一个实际向量满足每项约束

$$0\le z_{TU}\le c_{TU},\qquad
 \sum_{(T\cup U)\cap R=\varnothing}z_{TU}\ge q_{j,R}.$$

其目标权为 $\sum_{\{T,U\}}[w_{p_j}(T,U)+w_{p_j}(U,T)]z_{TU}$。在这些约束下取整数最小值，即得合法的共同配额扣除 $D_j^{\rm joint}$。也可对每项 $R$ 单独按权重填足 $q_{j,R}$，得 $D_{j,R}$，再用

$$D_j^{\max}=\max_R D_{j,R}\le D_j^{\rm joint}.$$

**证明。** 实际向量同时满足全部容量与下界，所以其目标不小于共同最小值，也不小于每个单项最小值及其最大值。不同 $R$ 的扣除不相加；固定位置上每个实际坏对只记一次。∎

**引理4.2（组件加强）。** 对 $f$ 个不同五元集合、支撑至多 $N$，建立集合相交图。其一个连通分量有 $t$ 个集合、$e$ 条相交边，则独立数至少

$$a(t,e)=\max\left(\left\lceil\frac{t^2}{t+2e}\right\rceil,
 \left\lceil\frac{2t-e-1}{2}\right\rceil\right).$$

分量支撑至少 $5a(t,e)$；$t\ge2$ 时还至少六。若 $e<\binom t2-\lfloor t/2\rfloor$，分量支撑还至少十一。

**证明。** 第一独立数界由随机排列独立集期望及Cauchy–Schwarz得到。第二界固定一棵生成树，删除至多 $e-t+1$ 个点以击中各非树边，余图为森林；较大二分部给该界。独立顶点对应互不相交的五元集合。两个不同五元集合的并至少六。若支撑至多十，每个五元集合至多有一个不交伙伴（恰十点时只有其补集），故相交图的补图为匹配，非边数至多 $\lfloor t/2\rfloor$，给最后断言。∎

不同相交分量的支撑互不相交。设 $u(t,e)$ 为上述全部适用支撑界的最大值，另取 $u(1,0)=5$。递推

$$S(0,q)=0,\quad S(f,q)=\min_{1\le t\le f,\ t-1\le e\le\min(q,\binom t2)}
 \{u(t,e)+S(f-t,q-e)\}$$

给出至多 $q$ 个相交对时的必要支撑下界。因此

$$q_*(f,N)=\min\{q\ge0:S(f,q)\le N\}$$

是合法相交对下界，可用于引理4.1中的每个实际避锁池。递推按一个实际分量归纳即证明；允许没有实现图的参数只会使下界更弱。完整证明与输入表分别见 [small31_33/REPORT.md](#appendix-a1) 和 [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/small31_33/CERTIFICATE.json)，独立组件及配额核查见 [independent31_33/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent31_33/REVIEW.md)。

## 5. 实际选锁与迹覆盖工具

**引理5.1（整数低度单位锁）。** 令 $\delta=\lceil(v-1)/5\rceil$，$L=\{x:d(x)\le D\}$，

$$Z=(D+1)v-396>0,\quad Q=\max_{\delta\le d\le D}(5d-v+2)(D+1-d).$$

若 $Z>(s-1)Q$，存在 $s$ 名度至多 $D$、两两共度一的实际锁点。

**证明。** 在 $L$ 上以共度至少二连冲突边。点 $x$ 的冲突度至多 $5d(x)-(v-1)$。随机排列独立集期望至少

$$\sum_{x\in L}\frac1{5d(x)-v+2}
 \ge\frac{\sum_{x\in L}(D+1-d(x))}{Q}\ge Z/Q>s-1.$$

分母为正，独立数为整数，故至少 $s$；点对覆盖把独立性变为共度恰一。∎

本稿尾部调用为 $(v,D,s;Z,Q)=(39,10,3;33,16),(40,10,4;44,14),(41,10,5;55,12)$。42–44点使用下文更直接的九度计数。

**引理5.2（实际最小邻点）。** 取实际最小度点 $x$，$d=d(x)$，令 $n=2(v-1)-5d>0$。在其实际单位共度邻点中选最低度点 $y$，度数 $e$，则

$$d\le e\le d+\left\lfloor\frac{396-vd}{n}\right\rfloor.$$

令 $t=n-1-(5e-v+1)$。若 $t>0$，在两者实际共同单位邻点中可选最低度点 $z$，度数 $f$，满足

$$e\le f\le e+\left\lfloor\frac{396-vd-n(e-d)}t\right\rfloor.$$

**证明。** 第一实际单位池大小 $r\ge n$，其中全体度至少 $e$，故 $396\ge vd+r(e-d)$。共同单位池大小至少 $r-1-(5e-v+1)\ge t$，且它在第一池内。选其最低度点后，$396\ge vd+n(e-d)+t(f-e)$。∎

**引理5.3（指定单位边的弱楔）。** 若实际 $R\subseteq V$，$|R|=r$，$a,b\in R$，$\lambda_{ab}=1$ 且

$$5(d(a)+d(b))<2v+2r-6,$$

则有 $z\in R\setminus\{a,b\}$，使三个点对共度全一，或恰一个为二、另两个为一。

**证明。** 若不存在，记 $u_a,u_b$ 为两点在 $R$ 中的单位邻点数。$b$ 的每个除 $a$ 外单位邻点都与 $a$ 共度至少三，且不是 $a$ 的单位邻点。因此

$$5d(a)\ge v-r+2(r-1)-u_a+u_b-1.$$

交换 $a,b$ 后相加，得到 $5(d(a)+d(b))\ge2v+2r-6$，矛盾。∎

**引理5.4（三锁扩第四锁）。** 对三个实际锁 $S$，令度和 $T$、内部共度超额 $L=\sum_{\{x,y\}\subset S}(\lambda_{xy}-1)$，并令

$$E=5T-3(v-1)-2L,\quad p=v-3-\lfloor E/2\rfloor.$$

若 $p>0$，可选实际第四锁，其到原三点的共度全一或恰一个二，且度数在

$$\delta\le d_4\le\delta+\left\lfloor\frac{396-T-(v-3)\delta}{p}\right\rfloor,$$

其中 $\delta$ 是实际最小度。

**证明。** 向外共度超额总和正是 $E$，故至少 $p$ 名外点的总超额至多一。外点总度超额为 $396-T-(v-3)\delta$，对这至少 $p$ 名点取平均。∎

**引理5.5（实际迹分类）。** 固定实际锁集及其全部点对的共度。每条至少含两锁的原边诱导一个锁子集块 $B$，其重数 $m_B$ 满足

$$\sum_{B\supseteq\{i,j\}}m_B=\lambda_{ij}.$$

全部非负整数解覆盖全部实际多锁迹；单锁迹由实际度数减去多锁贡献，空迹由66减去非空总数。扩锁时必须把新多重块限制到旧锁集后，恢复旧的完整多重块集。

**证明。** 每个实际点对恰被其共度条原边包含，故给上述等式；后两项由度数及边数定义给出。按剩余点对容量递归枚举允许团块，终点为零容量，按总剩余容量归纳覆盖每个非负解。共度全一时这是 $K_s$ 的团划分，$s=3,4,5$ 的完整带标签型数分别为2、6、32。本文只枚举有限锁迹，不枚举原超图。∎

## 6. 二十七至三十三点及三十六至四十四点

### 6.1 二十七至三十点：零锁

**引理6.1。** $P_{27},P_{28},P_{29},P_{30}$ 成立。

**证明。** 记 $Q$ 为不同无序原边对中交至少二者的数目。点对覆盖给

$$10Q\ge\sum_{\{A,B\}}\binom{|A\cap B|}{2}
 =\sum_{\{x,y\}}\binom{\lambda_{xy}}2
 \ge990-\binom v2.$$

第一步用不同六元边交至多五；最后一步用 $\binom a2\ge a-1$ 和全部共度和 $66\binom62=990$。故取 $q(v)=\lceil(990-\binom v2)/10\rceil$，实际有序单交边对至多 $\gamma(v)=66\cdot65-2q(v)$。零锁时每个固定有序单交对在 $h$ 的权相同，得到

$$U_0(v)=\sum_h\min\left\{
 \frac{396\binom{h-1}{5}}{v\binom{v-1}{5}},
 \frac{396\binom{v-h}{5}}{v\binom{v-1}{5}},
 \frac{\gamma(v)\binom{h-1}{5}\binom{v-h}{5}}
 {v\binom{v-1}{5}\binom{v-6}{5}}\right\}.$$

四项完整精确结果为

|$v$|$q(v)$|$\gamma(v)$|$U_0(v)$|
|---:|---:|---:|---:|
|27|64|4162|$1491391/1560090$|
|28|62|4166|$794453/825930$|
|29|59|4172|$2365165/2395197$|
|30|56|4178|$179971/180090$|

均严格小于一。新独立短程序及全部结果见 [BASE_DOMAIN_CHECK.json](context/propertyb-m6-67-progress-20261029/root/BASE_DOMAIN_CHECK.json)。引理3.4产生原染色。∎

### 6.2 三十一至三十三点

**引理6.2。** $P_{31},P_{32},P_{33}$ 成立。

**证明。** 全文实际选点证明、每个完整度数区间及迹式见 [small31_33/REPORT.md](#appendix-a1)，本文说明覆盖接口。

31点实际最小度为6–12。6–11用一锁；最小度12时至少七名十二度点，固定其中一人，其余六人若共度均至少七就消耗至少36共度超额，超过实际30，故选十二度二锁且共度1–6。全部十二型严格。

32点最小度7–11按引理5.2选实际单位伙伴，全35型严格。最小度12时有至少20名十二度点；若有其中单位对直接用通过型，若有十二度点到十四至二十四度的单位伙伴，也用通过型。否则这些低点的全部单位邻点都是十三度，至多12人。若没有十三度中心、十二度端点且端点共度至多二的单位楔，单位二部图每条边 $rb$ 都满足 $t_b<u_r$。对边求和 $1/t_b>1/u_r$ 就得十三度邻点数大于十二度点数，矛盾。该四种真实弱楔迹均严格。此支合计51型。

33点最小度7–12按引理5.2选最低度单位伙伴；除 $(d,e)=(9,14),(10,14),(11,14)$ 外，全25型严格。第一例全部单位伙伴至少十四度：度预算迫使恰十九名单位伙伴，并在外部留下至少另一名九度点；其实际共度必为二。该单型以 $101147/103385$ 严格。后两例度预算分别保证至少四、三名十四度单位伙伴，取其中两名，互相共度为1–14、三重交为0或1，共各27种非负实际迹，全部严格。

完整143型保存在 [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/small31_33/CERTIFICATE.json)，最大 $163866331/163881900<1$。独立重建参数域、125项组件配额表及独立注入概率复算全部143行通过，见 [independent31_33/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent31_33/REVIEW.md) 和 [CHECK.json](context/propertyb-m6-67-progress-20261029/independent31_33/CHECK.json)。所以每个实际输入都到达引理3.4。∎

### 6.3 三十六至三十八点

**引理6.3。** $P_{36},P_{37},P_{38}$ 成立。

**证明。** 完整证明见 [PROOF36_38.md](#appendix-a8)。36点最小度7–9用引理5.2，全部到严格二锁或三锁。最小度10时实际度至多12的点集至少24人；最低度点可选此集中一名单位伙伴，其度和至多22，满足引理5.3的 $110<114$。因而实际弱楔落在全部48种 $(10,e,f)$、$10\le e\le f\le12$ 型中；29型直接严格，余19型由引理5.4完全延展为3048型，全部严格。最小度11时恰十一正则，取 $R=V$ 用引理5.3；单位三锁迹直接严格，余两种弱楔迹经第四锁完整延展为31型，全部严格。

37、38点实际最小度均为8–10。引理5.2完整覆盖分别九、六个最低度／伙伴分支，所有所需共同池均正。已严格类型直接结束；余15及12个实际三锁迹用引理5.4扩成1452及855个四锁型，保留每个父迹，全部严格。

[独立审阅及重放](context/propertyb-m6-67-progress-20261029/independent36_38/REPORT.md)核对真实选点和完整域，并以独立注入概率、独立单项最大扣除／共同覆盖动态规划实际验证全部5604条保留与冗余通过行。36、37、38点整支最大界分别为 $480239/480240$、$1334992/1335015$、$9343777/9345105$。因此这些完整分支均由引理3.4闭合。∎

### 6.4 三十九至四十一点

**引理6.4。** $P_{39},P_{40},P_{41}$ 成立。

**证明。** 39点由引理5.1取三名度在8–10的单位锁。对其度和 $T=24,\ldots,30$，引理5.4给

$$p=36-\lfloor(5T-114)/2\rfloor,\qquad D=8+\lfloor(108-T)/p\rfloor.$$

$T=24,25,26$ 时 $D=10$，$T=27,28,29$ 时 $D=11$，$T=30$ 时 $D=12$。第四锁共度全一或恰一加倍，完整多重团型为 $6+3\cdot7=27$ 种，合计999必要型全严格，最大 $113467943/113476275$。实际选择及完整证明见 [PROOF39.md](#appendix-a9)，完整独立域与注入复算见 [independent39/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent39/REVIEW.md)。

40、41点由引理5.1分别取四、五名度在8–10的单位锁，原完整型数90、672。40点只需排除 $(8,8,8,10)$ 且四锁同边：低度池至少15点，该边外至少九名低度点，而三名八度锁总共至多三名冲突邻点。可用边外低度点替换第四锁，保持单位且不再全同边。

41点只需排除度和 $T\le49$ 的五锁同边。若边外有八度点，它与全图均共度一，可直接替换；否则边外低度点度为9或10。低度权 $11-d$ 的总量至少55，边外低度点至少 $\lceil(T-3)/2\rceil$；五锁到边外的总冲突关联至多 $5T-200$。对 $40\le T\le49$ 有 $2\lceil(T-3)/2\rceil>5T-200$，故某边外低度点至多冲突一人，选四名非邻锁加它即可避开全同边。原锁中点对的唯一共边保证新五锁不能同在另一边。

余下89、652型全部严格；独立复算最大值分别 $18678881/18690210$、$74754181/74760840$。完整结构与型表在 [PROOF40_41.md](#appendix-a10)，独立全部域和保留行在 [INDEPENDENT40_41.json](context/propertyb-m6-67-progress-20261029/root/INDEPENDENT40_41.json)。于是三支均到引理3.4。∎

### 6.5 四十二至四十四点

**引理6.5。** $P_{42},P_{43},P_{44}$ 成立。

**证明。** 最低度均为九。九度点至少有 $10v-396$ 人，九度点冲突度至多 $46-v$。因此42点至少24名九度点、冲突最大度4，可选五名九度单位锁；43、44点分别至少34、44名九度点，冲突最大度3、2，可先选至少九名九度单位锁。

42点若初选五锁全在边 $A$ 内，边外至少18名九度点，而五锁总共至多20次外部冲突关联。故有边外点至多冲突一名旧锁，取四名非邻旧锁加它。旧锁任一对的唯一共边为 $A$，所以新五锁不能全在任一边内。

43、44点在九名单位锁中，若无边含其中至少四点，任取五点即可；否则取一条含四至六名锁的边 $A$，选其中三点及 $A$ 外两点。另一原边至多含这三点之一，否则同一锁点对有两条共边。因此新五锁的全部迹大小至多三。

完整32种五锁团划分中，42点保留31型；43、44点分别保留26型。全部83型严格，其最大值分别为

$$1382147533/1383075540,\quad48389416/48663769,\quad132269531/133185052.$$

完整结构证明与原证书在 [原诊断证明包](context/propertyb-m6-67-diagnosis-20261029/DERIVATION_PACKAGE.md) 的新引理二；实际输入和独立注入复算保存在 [TAIL_ARITHMETIC.json](context/propertyb-m6-67-diagnosis-20261029/integer-lock/TAIL_ARITHMETIC.json)。因此三支全部到引理3.4。∎

## 7. 三十四、三十五点的完整结构分流

### 7.1 三十四点

**引理7.1。** $P_{34}$ 成立。

**证明。** 实际最小度只能为7–11。最小度7、8时引理5.2给伙伴范围分别为7–12、8–12，全部11个二锁输入由旧组件配额加共同整数扣除严格通过；独立重放保留原来的两项组件界及实际标签，没有换用未说明的概率公式。

**最小度九。** 固定九度点 $x$，其单位共度邻点集 $A$ 的大小 $u\ge21$，最低邻点度 $e\le13$。$e\le11$ 时直接用严格二锁型。若 $e=12$，固定十二度邻点 $y$，其唯一 $x$ 共边至多容纳五名 $A$ 成员。此边之外至少 $u-5\ge16$ 名 $A$ 点；若它们度数都至少14，则相对九度基线的超额至少

$$3u+2(u-5)=5u-10\ge95>396-34\cdot9=90,$$

矛盾。故有该边外的单位邻点 $z$，度为12或13。三重交为零，两条 $x$ 臂共度一，剩余共度 $\lambda_{yz}=1,\ldots,11$；上端由 $y$ 的度12及三重交零得到。全部22个实际型严格。

若 $e=13$，$A$ 消耗至少 $4u$ 度数超额，故 $u=21$ 或22。$A$ 外九度点至少

$$34-u-(90-4u)=3u-56\ge7.$$

至少六名与 $x$ 不同，且都与 $x$ 非单位共度。$x$ 的总共度超额为12；若这六人全与 $x$ 共度至少4，就需至少18，矛盾。故有另一九度点与 $x$ 共度2或3，两型均严格。这三组共27型，详证与独核见 [34_min9/REPORT.md](#appendix-a2)。

**最小度十。** 若有两名十度点，其共度为1–10；全部十种双锁型严格。故只需唯一十度点 $x$。若它有十一度单位伙伴，用一个严格二锁型。否则全部单位伙伴度至少12。记其单位伙伴数为 $u$；$x$ 的行超额为17，故 $u\ge16$。其余33点至少十一度，总预算给 $373+u\le396$，所以 $u\le23$。在 $33-u$ 名非单位伙伴中，相对十一度的剩余超额至多 $23-u$，因而至少十名度数恰十一。这些非单位伙伴中共度至少三者至多 $17-(33-u)=u-16\le7$。因此至少三名十一度点与 $x$ 共度二。

选其中两名。三个点度数为 $(10,11,11)$，两条臂共度二，底边共度1–11，三重交0–2；非负迹限制留下29个完整实际型。26型用完整池扣除，另三个底边共度二型用逐避点配额最大值，全部严格。连同上述十一双锁型共40型，见 [34_min10/PROOF.md](#appendix-a3)。

**最小度十一。** 总超额 $396-34\cdot11=22$。令 $R$ 为十一度点集，$r\ge12$；$A$ 为十二／十三度点集，大小 $a$；$C$ 为至少十四度点集，大小 $c\le7$；$b=a+c=34-r\le22$。若 $R$ 有单位点对，一个二锁型严格。否则每个 $x\in R$ 的至少十一名单位伙伴都在外部。记实际单位伙伴数为 $u_x\in[11,b]$。

若某 $z\in A$ 是两名 $R$ 点的共同单位中心，且两端共度二，则四种 $(d(z),\tau)\in\{12,13\}\times\{0,1\}$ 全部严格。假设此结构不存在。在 $R$–$A$ 单位二部图中记 $t_z$ 为 $z$ 的度。对每条实际单位边 $xz$，其他 $t_z-1$ 名 $R$ 邻点与 $x$ 共度至少三，故

$$55\ge66-u_x+t_z-1,\qquad t_z\le u_x-10.$$

只对正度边求倒数和，得到

$$a\ge\sum_{xz}\frac1{t_z}
 \ge\sum_{x\in R}\frac{u_x-c}{u_x-10}
 \ge\frac{ra}{b-10}.$$

最后一步用 $c<10$、$u_x\le b$；且 $a>0$，因为每名 $R$ 点至少十一名单位伙伴而 $c\le7$。因此 $b\ge22$，迫使 $r=12$、外部22点全十二度。首尾取等又迫使 $u_x=22$，所以所有内外点对共度一，而 $R$ 内全部共度三。

固定一名十二度外点，其十二条边将12名 $R$ 点按唯一共边分组，每组至多五人。取三个不同组的 $R$ 点，得到四锁：三名十一度点两两共度三，十二度中心到它们共度一，且无边同时含中心与两名端点。仅余三个端点的三重交 $\tau=0,1,2,3$ 四型，全严格。连同前面五型总计九型。完整等号分析、实际迹及九个精确值见 [34_min11/REPORT.md](#appendix-a4)。

三十四点全部最小度合计87个必要型，独立覆盖与精确重放见 [independent34_min10/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent34_min10/REVIEW.md)、[34_min9/CHECK.json](context/propertyb-m6-67-progress-20261029/34_min9/CHECK.json) 及 [independent_new_branches/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent_new_branches/REVIEW.md)。每个实际输入均到引理3.4，故 $P_{34}$ 成立。∎

### 7.2 三十五点

**引理7.2。** $P_{35}$ 成立。

**证明。** 最小度同样为7–11。最小度7、8按引理5.2的完整二／三锁域处理，全部严格。下面覆盖其余三支。

**最小度九。** 固定九度点 $x$。若最低单位伙伴度数至多11，已有完整自适应证书；其中需要三锁的输入保留完整度数区间和两种迹，不能仅将非严格二锁行当作结论。其余情况令 $A$ 为 $x$ 的单位邻点集、$u=|A|$，则所有成员度数至少12，且 $23\le u\le27$，因为相对九度的总超额为81。

令 $l$ 为与 $x$ 共度恰二的伙伴数。其余 $34-u-l$ 名非单位伙伴至少共度三，故

$$11\ge l+2(34-u-l),\qquad l\ge57-2u.$$

若这些 $l$ 名伙伴度数都至少十一，则其与 $A$ 的合计超额至少 $3u+2l\ge114-u\ge87>81$，矛盾。所以存在共度二伙伴 $y$，度数 $e=9$ 或10。

$y$ 至多有 $5e-34$ 名非单位伙伴，其中一名是 $x\notin A$。所以 $x,y$ 的共同单位邻点集 $C\subseteq A$ 至少有 $u+35-5e$ 人。这些点都至少十二度；在 $A$ 的基线超额 $3u$ 及 $y$ 的超额 $e-9$ 之外，总余量至多 $81-3u-(e-9)$。因此可取共同单位邻点 $z$，满足

$$12\le d(z)\le12+\left\lfloor\frac{81-3u-(e-9)}{u+35-5e}\right\rfloor.$$

当 $e=9$ 时上端为12；当 $e=10$ 时至多13。因此只有 $(d(z),d(x),d(y))=(12,9,9),(12,9,10),(13,9,10)$，两条单位臂、底边共度二及三重交0／1，共六型，全部严格。详证见 [PROOF35_MIN9.md](#appendix-a5)。

**最小度十。** 以下三个完整数值域全部严格，见 [PROOF35_MIN10.md](#appendix-a6) 与 [CERT35_MIN10.json](context/propertyb-m6-67-progress-20261029/mid34_38/CERT35_MIN10.json)：

1. 两名十度点共度一时，存在实际第三共同单位点，其度数10–56；非负迹将两种三锁域分别限制为10–49、10–48，共79型。
2. 十度点有两名十一度单位邻点时，剩余共度1–11、三重交0／1，非负迹留下21型。
3. 十二度中心连接两名十度点，中心两臂单位、端点共度二，三重交0／1两型。

反设当前实际超图不可二染。前两个数值域意味着：每名十度点都没有十度单位邻点，且至多一名十一度单位邻点。固定十度点 $x$，其单位邻点数 $u\ge18$，这些点的总超额至少 $2u-1$，故 $u\le23$。共度二伙伴数 $l$ 满足

$$16\ge l+2(34-u-l),\qquad l\ge52-2u.$$

若它们都至少十一度，总超额将至少 $(2u-1)+l\ge51>46$，矛盾。故有另一名十度点 $y$ 与 $x$ 共度二。

令 $P$ 是全体度数至少十二的点，$c=|P|$。每名十度点有至少17名 $P$ 内单位邻点，所以 $c\ge17$；总超额46又给 $c\le23$。$x,y$ 在 $P$ 内至少有 $34-c$ 名共同单位邻点。若它们全至少十三度，超额至少

$$2c+(34-c)=c+34\ge51>46,$$

矛盾。因此有实际十二度共同单位中心，落在第三数值域，其两界为 $185588/186093$ 与 $1644827/1654160$，都严格。此支闭合。前述反设只用于利用已证充分条件排除局部配置，没有将待证结论循环用作引理。

**最小度十一。** 至少24名十一度点，因为其余点至少十二度而总度396。取其中一名 $a$；其非单位伙伴至多21，所以在该集合内至少两名单位伙伴，选一名 $b$。引理5.3适用，因为

$$5(11+11)=110<2\cdot35+2\cdot24-6=112.$$

所得三名十一度点的点对共度全一或恰一个二，三重交0／1，带标签共八型，全部严格，最大 $13429/13485$；见 [STATUS35.md](#appendix-a7) 的最小度十一证明及 [MIN11_35.json](context/propertyb-m6-67-progress-20261029/mid34_38/MIN11_35.json)。

全部实际最小度现已覆盖，每支均通过引理3.4得到原超图染色，所以 $P_{35}$ 成立。∎

## 8. 主定理与原染色

**主定理1.3的证明。** 若原命题为假，引理2.1给同一个实际简单、点对覆盖、恰66边反例，点数在27–44。引理6.1–6.5及7.1–7.2覆盖这一完整区间，并各自给出合法染色，矛盾。各概率分支的成功排列对当前全部66条边都合法，因此也染好补边前的原边；点对识别只用于最小反例归约。故任意有限简单六元、至多66边超图具有 Property B，亦即 $m(6)\ge67$。∎

## 9. 证据及范围

|原始归约分支|完整证明／域|实际独立复算|
|---|---|---|
|$v\le26$、$27\le v\le30$|本稿第2、6.1节|[BASE_DOMAIN_CHECK.json](context/propertyb-m6-67-progress-20261029/root/BASE_DOMAIN_CHECK.json)，完整16+4项新精确算术|
|31–33|[small31_33/REPORT.md](#appendix-a1)|[independent31_33/CHECK.json](context/propertyb-m6-67-progress-20261029/independent31_33/CHECK.json)，143型及125项配额|
|36–38|[mid34_38/PROOF36_38.md](#appendix-a8)|[independent36_38/RESULTS.json](context/propertyb-m6-67-progress-20261029/independent36_38/RESULTS.json)，完整必要域及5604行|
|39|[tail39_41/PROOF39.md](#appendix-a9)|[independent39/CHECK.json](context/propertyb-m6-67-progress-20261029/independent39/CHECK.json)，全部999型|
|40–41|[tail39_41/PROOF40_41.md](#appendix-a10)|[root/INDEPENDENT40_41.json](context/propertyb-m6-67-progress-20261029/root/INDEPENDENT40_41.json)，完整762型、结构排除21型、余741行|
|42–44|[原诊断证明包](context/propertyb-m6-67-diagnosis-20261029/DERIVATION_PACKAGE.md)|[TAIL_ARITHMETIC.json](context/propertyb-m6-67-diagnosis-20261029/integer-lock/TAIL_ARITHMETIC.json)，全部83型|
|34|第7.1节及三个完整最小度证明|87型完整覆盖与独立复算，见上述逐支报告|
|35|第7.2节及三个完整最小度证明|完整原参数域与最终配置，见 [独立审阅](context/propertyb-m6-67-progress-20261029/independent_new_branches/REVIEW.md)|

“独立”指本地不同实现及覆盖重建，不表示第二台机器或Lean内核认证。跨家族静态审阅的实际范围单列于 [审阅处置](context/propertyb-m6-67-progress-20261029/reviews/DISPOSITION.md)。组件配额的作者与独核角色分别记录于具体报告，不把作者自审当独审。本总稿不替代各证书的精确行，也不把旧参数、试算菜单失败或历史说明写入最终数学假设。

## 分支证明全文

下列附录在本页内收入各实际分支的完整证明，不需跳转 Markdown 才能阅读。附录保留各稿形成时的状态说明；当前完整原题与验收范围以本卷首部及正文第9节为准。


<details class="proof-appendix" id="appendix-a1">
<summary>A1 · 31–33点：完整分流与组件配额</summary>

### A1 · M66: complete 31/32/33-point branches

The original target remains all finite simple six-uniform hypergraphs with at most 66 edges. The imported minimal-counterexample reduction gives pair-cover, exactly 66 edges, total degree 396 and minimum degree at least ceil((v−1)/5). This report establishes the complete v31, v32 and v33 branches. It does not claim the global target.

The probability engine is imported from [propertyB_small_k/propertyB_m6_certificate.py](propertyB_small_k/propertyB_m6_certificate.py), with its module constant explicitly reset to M=66. This is exact local finite verification, not an independent probability implementation. [certificate.py](context/propertyb-m6-67-progress-20261029/small31_33/certificate.py) generates every actual local type used below, together with its successful layout and exact upper bound. [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/small31_33/CERTIFICATE.json) records the result. Root must independently verify this candidate and integrate it with the complete object domain.

#### A1 · Lemma 1: a stronger link bad-pair quota

Let F be a family of f distinct five-element sets on at most N points. Let G have these sets as vertices, adjacency meaning nonempty intersection, and q edges. Different connected components of G have disjoint supports.

For one component with t vertices and e edges, where t−1≤e≤C(t,2), define

$$a(t,e)=\max\left(\left\lceil\frac{t^2}{t+2e}\right\rceil,\left\lceil\frac{2t-e-1}{2}\right\rceil\right).$$

Its independence number is at least a(t,e). The first term follows from the random-order independent-set expectation and Cauchy–Schwarz. For the second, fix a spanning tree. There are r=e−t+1 edges outside it. Delete at most one endpoint for each such edge, a total of at most r vertices. The remaining induced graph is a forest on at least t−r vertices, whose larger bipartition class is an independent set of size at least ceil((t−r)/2)=ceil((2t−e−1)/2). If this expression is nonpositive it is harmless.

Disjoint five-sets from an independent set imply component support at least 5a(t,e). A component with t≥2 also has support at least six, because its five-sets are distinct. A further valid strengthening is support at least eleven if

$$e<\binom t2-\left\lfloor\frac t2\right\rfloor.$$

Indeed, if the component support had at most ten points, any five-set would have at most one distinct disjoint partner: on fewer than ten points there is none, and on exactly ten points the only possible partner is its complement. Thus the nonedge graph would have maximum degree at most one and at most floor(t/2) edges, contradicting the displayed condition.

Write u(1,0)=5. For t≥2 let u(t,e) be the maximum of 6, 5a(t,e), and eleven when the last condition holds. Define recursively

$$S(0,q)=0,\qquad S(f,q)=\min_{\substack{1\le t\le f\\t-1\le e\le\min\{q,\binom t2\}}}\{u(t,e)+S(f-t,q-e)\}.$$

Then the union of F has at least S(f,q) points. To prove this, select an actual component (t,e), apply its valid support bound, and apply induction to the remaining actual components, whose supports are disjoint. The recurrence permits component parameters without a realizing graph; this only lowers S, hence preserves its necessary-bound direction. It also permits unused budget q, as needed for an at-most-q assertion.

Consequently define

$$q_*(f,N)=\min\{q\ge0:S(f,q)\le N\}.$$

Then F has at least q_*(f,N) intersecting pairs. The implementation starts from the older valid ceiling bound ceil((5f−N)/4), truncated at zero; since that lower bound is valid, this does not skip a possible actual q. Its finite search terminates whenever a family F exists, and all parameter inputs used here admit an accepted relaxed component partition.

Applied to the actual link at a lock vertex, F consists of the original edges containing that vertex with the vertex removed. These five-sets are distinct because the original hypergraph is simple. Their support is at most v−1. Therefore q_*(d,v−1) can replace the old quota in the existing nonnegative capacity/weight deletion argument. For an avoided-lock subfamily the same conclusion uses f equal to its actual number of edges and N=v−1−|R|. The script [diagnose.py](context/propertyb-m6-67-progress-20261029/small31_33/diagnose.py) exports `support_min(f,q)` and `quota(N+1,f)` for this purpose.

All three strengthening components above are used by the current candidate. In particular, the final two-point delta11 cases use the feedback-vertex bound and the unique-complement bound. The full table for f=0,…,24 and support N=28,…,32 is in [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/small31_33/CERTIFICATE.json). No claim of novelty is made for these elementary graph bounds.

#### A1 · Lemma 2: complete v31 selection

The minimum degree d lies in 6,…,12. For d≤11 choose a vertex of degree d and one lock; the six exact bounds are strict.

If d=12, at least seven vertices have degree exactly twelve: otherwise at least 25 vertices would have degree at least thirteen, forcing total degree at least 31·12+25=397>396. Fix a twelve-degree vertex x among them. Pair-cover gives

$$\sum_{y\ne x}(\lambda_{xy}-1)=5\cdot12-30=30.$$

If its six other twelve-degree partners all had codegree at least seven, the sum would be at least 36. Thus some second twelve-degree vertex y has 1≤λxy≤6. The complete trace multiplicities are

$$\ell_{xy}=\lambda,\quad\ell_x=\ell_y=12-\lambda,\quad\ell_0=42+\lambda.$$

All six actual types have strict recorded bounds. Wider layouts are essential for λ=3 and λ=4; checking only central adjacent locks had missed these cases. This closes all v31 inputs.

#### A1 · Lemma 3: complete v32, minimum degree at most eleven

For a minimum-degree vertex x of degree d, there are at least

$$n=2(v-1)-5d$$

unit-codegree neighbors. This follows because the sum of λxy−1 is 5d−(v−1), and each nonunit neighbor contributes at least one. Here n>0 for d=7,…,11. If all unit neighbors had degree greater than

$$t=d+\left\lfloor\frac{396-vd}{n}\right\rfloor,$$

the total degree would exceed vd+n(t+1−d)>396. Choose a unit neighbor y with degree e in d,…,t. [certificate.py](context/propertyb-m6-67-progress-20261029/small31_33/certificate.py) enumerates this entire necessary interval separately for each d, uses the unique two-lock trace, and obtains strict bounds for every such type. This closes v32,d≤11.

#### A1 · Lemma 4: complete v32, minimum degree twelve

Let R be the twelve-degree vertices. The total excess above twelve is twelve, so |R|≥20. All vertices outside R have degree at most 24. Each r∈R has at least two unit neighbors because its pair-excess is 29 among 31 partners.

If there is a unit pair inside R, its two-lock type (12,12,1) is strict. If there is a unit pair from R to a vertex of degree e∈{14,…,24}, the complete eleven-type two-lock certificate is strict. Hence assume every unit neighbor of every r∈R has degree thirteen. Let B be the set of these neighbors. Since each costs at least one of the twelve excess units, |B|≤12. The unit pairs between R and B form a bipartite graph with every r nonisolated.

Write u_r for r's degree in this bipartite graph and t_b for b's degree. Suppose there is no b-centered wedge r–b–r′ whose endpoint codegree is at most two. Then every such r′ has λrr′≥3. For every edge rb, all t_b−1 other R-neighbors of b are among these partners. Relative to baseline codegree two on all 31 partners of r, exactly u_r unit partners decrease its row sum by one each; the t_b−1 identified partners increase it by at least one each. Thus

$$60=\sum_{z\ne r}\lambda_{rz}\ge62-u_r+t_b-1,$$

so t_b≤u_r−1 and therefore 1/t_b>1/u_r. Summing over all bipartite edges gives

$$|B|=\sum_{rb}\frac1{t_b}>\sum_{rb}\frac1{u_r}=|R|,$$

contradicting |B|≤12<20≤|R|. Hence there is an actual wedge with center degree13, endpoints degree12, both center–endpoint codegrees one and endpoint codegree l∈{1,2}.

The triple intersection τ is zero or one. These four complete actual trace types are

$$\ell_{123}=\tau,\quad\ell_{12}=\ell_{13}=1-\tau,\quad\ell_{23}=l-\tau,$$

$$\ell_1=11+\tau,\quad\ell_2=\ell_3=11-l+\tau,\quad\ell_0=66-\sum_{T\ne\varnothing}\ell_T,$$

where vertex1 is the degree13 center. All four certificate bounds are strict. This closes v32,d12.

#### A1 · Lemma 5: complete v33 selection

The same actual minimum/unit-partner selection covers d=7,…,12. With the stronger link quota every two-lock type is strict except e14 at d9,d10,d11. In particular d12 is handled directly, and the earlier max-unit-degree wedge idea is unnecessary.

Here take y to be a minimum-degree unit neighbor of the minimum-degree x. If e=d(y)≠14, the corresponding passing type applies. In the exceptional three cases e=14, all unit neighbors of x have degree at least fourteen.

If d=9, x has at least 19 unit neighbors. The total excess above nine is 99. Nineteen vertices of degree at least fourteen cost at least 95 of those excess units; twenty would cost 100, so x has exactly nineteen unit neighbors. Its other thirteen partners are nonunit. Since

$$\sum_{z\ne x}(\lambda_{xz}-1)=45-32=13,$$

every one of those thirteen partners has codegree exactly two with x. The nineteen unit neighbors leave only four excess degree units among the other fourteen vertices (including x), so at least ten vertices have degree nine. Thus another degree9 vertex y exists, is a nonunit partner, and has λxy=2. Its two-lock type has exact upper bound

$$101147/103385<1$$

at positions (16,18). This closes d9 entirely, including the previous failed three-lock λ=3 profiles.

If d=10 or d=11, let n=64−5d, respectively 14 or 9. The total excess above d is 396−33d, and n unit neighbors cost at least n(14−d). The respective remaining slacks are ten or six. Among at least n unit neighbors, therefore at least n−slack have degree exactly fourteen: respectively four or three. This count is still valid if there are more than n unit neighbors: each additional one costs at least 14−d≥3 extra units and cannot reduce the lower bound. More directly, if u≥n actual unit neighbors and h of them have degree above fourteen, then

$$u(14-d)+h\le396-33d,$$

so the number u−h of degree14 unit neighbors is at least (15−d)u−(396−33d)≥(15−d)n−(396−33d)=n−slack.

Choose two degree14 unit neighbors. Their mutual codegree l ranges from one to fourteen. Their triple intersection τ with x is zero or one; nonnegative single traces require 13−l+τ≥0. The actual trace multiplicities are

$$\ell_{123}=\tau,\quad\ell_{12}=\ell_{13}=1-\tau,\quad\ell_{23}=l-\tau,$$

$$\ell_1=d-2+\tau,\quad\ell_2=\ell_3=13-l+\tau,\quad\ell_0=66-\sum_{T\ne\varnothing}\ell_T.$$

For each d=10,11 the complete 27 actual (l,τ) types have strict bounds in the certificate. This closes v33.

#### A1 · Exact verification and status

[certificate.py](context/propertyb-m6-67-progress-20261029/small31_33/certificate.py) enumerates every necessary type in these selection branches, without enumeration of original hypergraphs. It records all multiplicities, positions and exact rational upper bounds in [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/small31_33/CERTIFICATE.json). Every final certificate row is strict. [DIAGNOSTIC.json](context/propertyb-m6-67-progress-20261029/small31_33/DIAGNOSTIC.json), [FOUR.json](context/propertyb-m6-67-progress-20261029/small31_33/FOUR.json) and the exploratory files preserve failed older menus; those failed menus are not assumptions or components of the final proof.

The arithmetic imports the existing conditional random-greedy probability formulas and replaces only the justified link quota. It is not an independent reimplementation. No Lean, external model review or global m(6)≥67 conclusion is claimed by this local delivery.

</details>

<details class="proof-appendix" id="appendix-a2">
<summary>A2 · 34点：最小度九</summary>

### A2 · 34点、最小度九的完整分支证明候选

**定理34.9。** 设 $H=(V,E)$ 是有限简单六元超图，$|V|=34$、$|E|=66$，每个点对均被某条边覆盖，且最小度为九。在既有条件排列／随机贪心失败上界定理和 component 支撑配额引理下，$H$ 可二染。

以下给出覆盖全部实际输入的选点证明，以及全部27个必要局部型的精确证书。主代理提出的选点推导已经独立核查；所有最终布局也已用既有独立下降阶乘注入计数和独立 component DP 完整复算。状态为 same-family / provisional；本文只处理34点最小度九，不单独宣称完整 $m(6)\ge67$，也没有 Lean 或外部模型审阅。

#### A2 · 1. 实际单位伙伴的完整分流

**引理34.9.1。** 可以选定实际九度点 $x$，使其单位共度伙伴集
$$A=\{y\in V\setminus\{x\}:\lambda_{xy}=1\}$$
有大小 $u\ge21$，且其中最小度数 $e$ 满足 $9\le e\le13$。

**证明。** 最小度九保证实际点 $x$ 存在。其共度总和为 $5d(x)=45$，相对33个伙伴的单位基线，超额为
$$\sum_{y\ne x}(\lambda_{xy}-1)=45-33=12. \tag{1}$$
点对覆盖使每个超额非负，因此非单位伙伴至多12名，单位伙伴至少 $33-12=21$ 名。总度相对每点九的超额为 $396-34\cdot9=90$。若 $A$ 中所有点的度数至少十四，则至少贡献 $21\cdot5=105>90$，矛盾。因此其最小度 $e\le13$，而最小度假设给 $e\ge9$。$\square$

当 $e\in\{9,10,11\}$，取达到此最小度的单位伙伴 $y$，得到三种实际双锁型 $(9,e,\lambda=1)$，精确上界分别为
$$\frac{14695667}{14887440},\qquad
\frac{7364641}{7443720},\qquad
\frac{1643881}{1654160},$$
均严格小于一。以下只需分别处理 $e=12$ 和 $e=13$，不对二者混加假设。

#### A2 · 2. 最小单位伙伴为十二时的实际双臂选点

**引理34.9.2。** 若 $e=12$，则存在三个不同的实际点 $x,y,z$，度数为 $(9,12,f)$、$f\in\{12,13\}$，使
$$\lambda_{xy}=\lambda_{xz}=1,\qquad
1\le\lambda_{yz}\le11,$$
且没有原边同时包含三点。

**证明。** 取 $y\in A$，$d(y)=12$。设 $F$ 是 $x,y$ 唯一的共同边。六元性使 $F$ 最多包含五名 $A$ 点，故
$$C=A\setminus F,\qquad |C|\ge u-5\ge16.$$
因为 $e=12$，全部 $A$ 点的度数至少十二，相对九的基线至少贡献 $3u$ 度数超额。若 $C$ 全部度数至少十四，便另贡献至少 $2(u-5)$ 超额，从而
$$90\ge3u+2(u-5)=5u-10\ge95,$$
矛盾。因此可以选 $z\in C$，其度数为十二或十三。$z\in A$ 保证 $\lambda_{xz}=1$，且 $z\notin F$ 保证 $z\ne x,y$，以及三点不在同一条原边中：任何含 $x,y$ 的原边都只能是 $F$。

点对覆盖给 $\lambda_{yz}\ge1$。经过 $y$ 的十二条边中，$F$ 不含 $z$；因此至多其余十一条含 $z$，即 $\lambda_{yz}\le11$。$\square$

将 $x,y,z$ 分别标为0、1、2，并记 $\lambda=\lambda_{yz}$。三点迹为零，两个经过 $x$ 的二点迹各一。因此实际完整迹重数为
$$\ell_7=0,\quad \ell_3=\ell_5=1,\quad \ell_6=\lambda,$$
$$\ell_1=7,\quad \ell_2=11-\lambda,\quad
\ell_4=f-1-\lambda,\quad \ell_0=47-f+\lambda. \tag{2}$$
这恰给 $f\in\{12,13\}$、$\lambda=1,\ldots,11$ 的22个必要型，全部迹重数非负。这是实际选点后的完整域，而不是取自概率试算的通过子集。

#### A2 · 3. 最小单位伙伴为十三时的双九度点

**引理34.9.3。** 若 $e=13$，则存在不同的九度点 $x,z$，共度为二或三。

**证明。** 全部 $A$ 点的度数至少十三，相对九的基线，每个至少花费四个超额单位。因此
$$4u\le90,\qquad u\in\{21,22\}. \tag{3}$$
$A$ 外有 $34-u$ 个点，包括 $x$；其剩余总度超额至多 $90-4u$。每名非九度点至少消耗一个超额单位，所以 $A$ 外九度点至少有
$$(34-u)-(90-4u)=3u-56\ge7. \tag{4}$$
其中一名是 $x$，故至少六名其他九度点存在。它们均不在 $A$，因为 $A$ 中度数至少十三。因此它们与 $x$ 的共度至少二。若这些九度伙伴与 $x$ 的共度全部至少四，仅六名便在式(1)的超额中至少贡献 $6\cdot3=18>12$，矛盾。于是某一名 $z$ 与 $x$ 的共度至多三，结合非单位性恰为二或三。$\square$

两种完整双锁型是
$$\ell_3=\lambda,\quad\ell_1=\ell_2=9-\lambda,\quad
\ell_0=48+\lambda,\qquad\lambda\in\{2,3\}. \tag{5}$$
精确上界分别为 $2964497/2977488$ 和 $37169069/37218600$，均严格。式(3)使用的是每名十三度伙伴花费四个超额单位，不能将其误写成三个。

#### A2 · 4. 精确证书、独立复算与结论

复用 [../small31_33/REPORT.md](#appendix-a1) 引理1和已核 [../independent31_33/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent31_33/REVIEW.md) 的 component 支撑界：任何 $f$ 个不同五元链接在至多 $N$ 点上，实际相交无序边对数至少为相应必要配额 $q_*(f,N)$。本证书只需完整链接池 $N=33$，不依赖共同避点配额的额外加强。

每个锁处，按精确非负双向权重从低到高填充无序迹型格的实际容量，填至 $q_*(f,33)$，所得成本不超过实际坏对成本。将此成本从既有条件排列有向边对界中扣除，再逐位置取端点界／起点界／扣除后的边对界之最小值，即为证书中的失败概率上界。不同锁的位置保持各自对应的真实度数和迹标签，不排序或置换实际证书行。

[check.py](context/propertyb-m6-67-progress-20261029/34_min9/check.py) 先从上述三个选点引理独立重建完整27型，再读取主代理原始试算中的相应实际成功布局；没有导入试算生成器或原概率模块。它使用已经独立审计的下降阶乘注入概率和 bottom-up component 精确边数 DP，自行重建全部迹重数及实际度数／共度边际，并逐项与主代理原二项式概率结果作精确比较。

| 完整分支 | 型数 | 独立复算最大值 |
|---|---:|---:|
|$e=9,10,11$ 的单位双锁|3|1643881/1654160|
|$e=12$ 的无三重交双臂|22|156204893/156318120|
|$e=13$ 的双九度点|2|37169069/37218600|
|合计|27|156204893/156318120|

全部27行均与原有理值精确相等，并严格小于一。由引理34.9.1，每个实际超图都落入这三个完整分支之一；引理34.9.2或34.9.3保证所用局部型来自同一实际超图。故每个实际输入均有失败概率严格小于一的合法条件排列，因而存在成功二染色，得定理34.9。$\square$

完整实际迹、位置和独立上界保存在 [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/34_min9/CERTIFICATE.json)，核查摘要为 [CHECK.json](context/propertyb-m6-67-progress-20261029/34_min9/CHECK.json)。实际运行约0.126 CPU秒。复现命令：

```sh
python3 context/propertyb-m6-67-progress-20261029/34_min9/check.py
```

原值来源为 [../root/PAIRS_PROBE.json](context/propertyb-m6-67-progress-20261029/root/PAIRS_PROBE.json) 和 [../root/TWO_ARM_PROBE.json](context/propertyb-m6-67-progress-20261029/root/TWO_ARM_PROBE.json)。这些探索文件中的其他失败型不进入本证明；这里并未假设所有三锁型都严格，而是先由实际选点强制三重交为零，再覆盖其全部22型。

</details>

<details class="proof-appendix" id="appendix-a3">
<summary>A3 · 34点：最小度十</summary>

### A3 · 34点、实际最小度十的完整分支

**命题。** 设同一实际有限简单六元超图H有34个顶点、66条边、覆盖每个点对，实际最小度为十，则H具有Property B。

**状态。** 完整计算机辅助证明候选；40型精确证书已全部严格。概率计算复用原核，尚待独立算术复算。它只关闭34点最小度十分支，不声称整个34点或m(6)≥67已经完成。

使用总证明草稿第3–4节的实际条件排列概率及坏对扣除机制。完整池相交链接配额为已证组件配额q*(f,N)；仅三个型需要最大避锁扣除max_R，其余用完整池即可。所有配额对应同一个实际坏对对象，max_R不相加。

#### A3 · 引理一：重复十度点直接闭合

若有两个不同十度点x,y，实际共度λ在1–10之间。实际二锁迹为

$$\ell_{xy}=\lambda,\quad\ell_x=\ell_y=10-\lambda,\quad\ell_0=46+\lambda.$$

这十种完整实际类型的完整池概率界全部严格，记录在[CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/34_min10/CERTIFICATE.json)。所以只需考虑唯一十度点x。此后其余33点度数均至少十一。∎

#### A3 · 引理二：唯一十度点的低度伙伴

若x有十一度单位共度邻点y，二锁实际型(10,11,1)在位置(16,17)有完整池界

$$370673/372186<1,$$

于是该支闭合。否则x的全部实际单位共度邻点度数至少十二。

记这些单位邻点数为u。点对覆盖给

$$\sum_{y\ne x}(\lambda_{xy}-1)=50-33=17.$$

因此非单位邻点至多17人，u≥16。唯一十度点和其余点最低十一度的总基线为373；每个单位邻点还需至少一个度数单位，因此

$$396\ge373+u,\qquad16\le u\le23.$$

所有非单位邻点中，至少十名度数恰为十一。证明是：基线外总度超额23，其中单位邻点已经消耗至少u，非单位邻点数为33−u，其中度超过十一的人数至多23−u；相减至少十名十一度点。

在33−u个非单位邻点上，基线共度二已经消耗33−u单位共度超额，剩余只有

$$17-(33-u)=u-16\le7.$$

所以共度至少三的非单位邻点总数至多七。这十名十一度点中，至少三名与x共度恰二。可选其中两个不同点y,z，满足

$$d(x),d(y),d(z)=(10,11,11),\qquad\lambda_{xy}=\lambda_{xz}=2.$$

全部推导均来自同一实际H，没有把必要整数见证当作可实现超图。∎

#### A3 · 引理三：全部实际三锁迹严格

令l=λyz，τ为含x,y,z三点的原边数。完整实际区间为1≤l≤11，0≤τ≤min(2,l)，并要求以下迹重数非负：

$$\ell_{xyz}=\tau,\quad\ell_{xy}=\ell_{xz}=2-\tau,\quad\ell_{yz}=l-\tau,$$

$$\ell_x=6+\tau,\quad\ell_y=\ell_z=9-l+\tau,\quad
\ell_0=66-\sum_{T\ne\varnothing}\ell_T.$$

这些公式完全确定实际重数。其必要局部域恰有29型，全部记录于[CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/34_min10/CERTIFICATE.json)。其中26型用完整池组件配额严格；l=2的三个型用组件配额的最大避锁扣除，在统一位置(16,17,19)分别得到

|τ|严格上界|
|---:|---:|
|0|742709/744372|
|1|7433509/7443720|
|2|927532/930465|

[maxr.py](context/propertyb-m6-67-progress-20261029/34_min10/maxr.py)只针对这三个原失败型完成有界布局查找，6.80CPU秒；[certificate.py](context/propertyb-m6-67-progress-20261029/34_min10/certificate.py)按保留位置重建全部十个十度二锁型、一个十一度单位伙伴型、29个三锁型，共40型，不再搜索。每行含实际迹、实际位置和精确分数，最大413127/413540<1。∎

#### A3 · 原染色结论

若有第二名十度点，用引理一。否则唯一十度点若有十一度单位邻点，用引理二的首支；若没有，引理二保证一组实际三锁，其迹属于引理三的完整29型。因此任何输入都到达严格条件排列失败概率界。有限实际排列空间中必有一次贪心过程成功，其输出对H的全部原边都是合法二染色，证明命题。∎

#### A3 · 复算入口及进口范围

运行`python3 context/propertyb-m6-67-progress-20261029/34_min10/certificate.py`。它导入已有概率核和已证组件配额；不是独立概率实现。原40型由`root/NONUNIT_LOW_PROBE.json`、本目录[MAXR.json](context/propertyb-m6-67-progress-20261029/34_min10/MAXR.json)及单独重算的(10,11,1)型组成，最终入口为本目录[CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/34_min10/CERTIFICATE.json)。

组件配额的三个基础界及完整池/避锁最大扣除已经在各自通用引理中证明；本分支新增的实质选点义务是引理二的唯一十度点预算。这里只使用至多三个锁，没有扩展泛四锁域、整图枚举、Lean或外部模型调用。

</details>

<details class="proof-appendix" id="appendix-a4">
<summary>A4 · 34点：最小度十一</summary>

### A4 · 34点、最小度十一的完整分支候选

**结论。** 固定有限简单六元超图 $H=(V,E)$，假设 $|V|=34$、$|E|=66$、每个点对被某条边覆盖且最小度为十一。下述实际选点分流覆盖全部此类超图。九个必要局部型均有严格小于一的精确失败概率上界，两套既有概率实现给出逐项相同的有理数。因此，在既有条件排列／随机贪心失败上界定理和已证明的 component 配额引理下，这一完整分支可二染。

这不是完整 $m(6)\ge67$ 的验收；本文没有处理其他点数／最小度，没有 Lean 或指定跨家族审阅。当前状态为 same-family / provisional，等待主代理核读和全局装配。

#### A4 · 1. 预算与辅助图

记 $d(x)$ 为实际度数，$\lambda_{xy}$ 为实际共度。总度为 $396$。定义
$$R=\{x:d(x)=11\},\qquad r=|R|,\qquad
A=\{x:d(x)\in\{12,13\}\},\quad a=|A|,$$
$$C=\{x:d(x)\ge14\},\qquad c=|C|,\qquad b=a+c=34-r.$$
相对每点十一的总度超额为 $396-34\cdot11=22$，所以
$$r\ge12,\qquad b\le22,\qquad a+3c\le22,\qquad c\le7. \tag{1}$$

若 $R$ 内有共度一的点对，直接使用第4节的双锁型。以下假设 $R$ 内任意不同两点的共度均至少二。

对每个 $x\in R$，其共度总和为 $5d(x)=55$，故
$$\sum_{y\ne x}(\lambda_{xy}-1)=55-33=22.$$
在33个伙伴中，至多22个共度大于一。因此 $x$ 至少有11个单位共度伙伴；由当前假设它们全部位于 $A\cup C$。设其实际单位伙伴数为 $u_x$，则
$$11\le u_x\le b. \tag{2}$$
特别地，因 $c\le7$，每个 $x\in R$ 在 $A$ 中至少有四个单位伙伴，故 $a>0$。

#### A4 · 2. 低中心楔形或唯一刚性结构

**引理34.11.1。** 在上述假设下，至少有以下一种实际结构：

1. $z\in A$，$x,y\in R$ 为不同点，$\lambda_{zx}=\lambda_{zy}=1$、$\lambda_{xy}=2$；
2. $r=12$，其余22个点的度数全为十二，$R$ 与其余点之间全部共度一，且 $R$ 内全部共度三。

**证明。** 在 $R$ 与 $A$ 之间按共度一连二分图；对 $z\in A$ 记其在该图的度为 $t_z$，只在 $t_z>0$ 时使用倒数。假设第一种结构不存在，则同一个 $z$ 的任意两个 $R$ 邻点的共度至少三，因为 $R$ 内已无共度一的点对。

固定单位边 $xz$。基线为 $x$ 到33个伙伴的共度各二；其恰好 $u_x$ 个单位伙伴各使该基线减一；$z$ 的另 $t_z-1$ 个 $R$ 邻点又各至少增加一。因此
$$55=\sum_{w\ne x}\lambda_{xw}\ge66-u_x+t_z-1,
\qquad t_z\le u_x-10. \tag{3}$$
记 $A_+=\{z\in A:t_z>0\}$，$a_+=|A_+|\le a$。由 (2)，$u_x-10>0$。对全部实际单位边求和，得到
$$a\ge a_+=\sum_{xz}\frac1{t_z}
\ge\sum_{x\in R}\frac{|N(x)\cap A|}{u_x-10}
\ge\sum_{x\in R}\frac{u_x-c}{u_x-10}. \tag{4}$$
这里仅对真实二分图的边求和；$A$ 中可能存在孤立点，因此第一步使用 $a\ge a_+$，并未将孤立点当作正度点。

因为 $u_x\le b$、$c\le7<10$，逐项有
$$\frac{u_x-c}{u_x-10}-\frac{b-c}{b-10}
=\frac{(10-c)(b-u_x)}{(u_x-10)(b-10)}\ge0.$$
又 $b-c=a$，故 (4) 给
$$a\ge\frac{ra}{b-10}.$$
由 $a>0$ 得 $b-10\ge r=34-b$，即 $b\ge22$。结合 (1)，只能 $b=22,r=12$；由于总度超额恰为22，其余22个点的度数全部为十二，故 $a=22,c=0$。

此时 (4) 及其后的界首尾相等。由于 $10-c=10>0$，上面的差式迫使每个 $u_x=b=22$。所以 $R$ 与全部其余点之间均共度一。固定任一其余点，它与全部12个 $R$ 点构成单位边，故不存在第一种结构意味着 $R$ 中任意两点共度至少三。对 $x\in R$，外部共度之和是22，剩余11个 $R$ 伙伴的共度之和为 $55-22=33$；每项至少三，因此每项恰为三，得到第二种结构。$\square$

这个论证不要求事先选定某个最小度点的最小单位伙伴，也不要求所有高于十一的点具有相同度数。

#### A4 · 3. 刚性结构的实际四锁选择与完整迹

**引理34.11.2。** 在引理34.11.1的第二种结构中，可以选三名 $R$ 点 $x_0,x_1,x_2$ 和一名度十二的外点 $z$，使三名 $R$ 点两两共度三，$z$ 到它们分别共度一，且没有原边同时包含 $z$ 和其中两名 $R$ 点。

**证明。** 固定任一外点 $z$。因其与每名 $R$ 点的共度恰一，经过 $z$ 的十二条边将12个 $R$ 点按其唯一共边分成若干不相交的非空组，每组至多五点。一组或两组至多容纳十点，所以至少三组非空。分别取不同三组的一点，即得所需三点。$\square$

将三名 $R$ 点标为0、1、2，$z$ 标为3。令 $\tau$ 为含三名 $R$ 点的原边数，则 $0\le\tau\le3$。引理排除了包含 $z$ 与两个 $R$ 点的任何迹；故没有四点迹，唯一至少三点迹为 $\{0,1,2\}$。所有实际迹重数是
$$\ell_7=\tau,\qquad \ell_3=\ell_5=\ell_6=3-\tau,
\qquad \ell_9=\ell_{10}=\ell_{12}=1,$$
$$\ell_1=\ell_2=\ell_4=4+\tau,\qquad \ell_8=9,
\qquad\ell_0=33-\tau. \tag{5}$$
这里下标是四锁二进制 mask。这四个 $\tau$ 值覆盖全部实际型，不增加三点迹或零迹假设。

在引理34.11.1第一种结构中，将中心标为0、两个十一度端点标为1、2。中心度数 $d\in\{12,13\}$，端点间共度为二，两个中心—端点共度一。实际三重交数 $\tau\in\{0,1\}$。完整迹为
$$\ell_7=\tau,\quad \ell_3=\ell_5=1-\tau,\quad
\ell_6=2-\tau,$$
$$\ell_1=d-2+\tau,\quad\ell_2=\ell_4=8+\tau,
\quad\ell_0=48-d-\tau. \tag{6}$$
因此楔形分支只有四个必要型。

#### A4 · 4. 同一实际坏对上的 component 配额与精确证书

复用 [../small31_33/REPORT.md](#appendix-a1) 引理1及 [../independent31_33/REVIEW.md](context/propertyb-m6-67-progress-20261029/independent31_33/REVIEW.md) 第1节已经证明／核查的 component 支撑下界，记其必要相交边对数为 $q_*(f,N)$。对每个锁 $j$ 和每个 $R'\subseteq S\setminus\{j\}$，经过 $j$ 且避开 $R'$ 的实际边删去 $j$ 后形成 $f$ 个不同五集，支撑至多 $33-|R'|$。因此同一实际坏对向量在避点型格中至少有 $q_*(f,33-|R'|)$ 个单位。

对这个单项配额，按精确非负权重从低到高填充格容量，得到下界 $D_{j,R'}$。所有这些下界约束同一个实际坏对成本，故取
$$D_j=\max_{R'}D_{j,R'}$$
仍为合法下界，绝不将不同 $R'$ 的成本相加。代入原失败概率和
$$\sum_h\min(A_h,B_h,Q_h-D_h)$$
即可使用下表。非锁位置的 $D_h=0$。所有迹重数、锁标签和位置在完整计算中保持对应；四锁位置无需按标签递增。

| 必要型 | 参数 | 实际位置 | 精确失败概率上界 |
|---|---|---|---:|
|十一度单位对|$(11,11),\lambda=1$|$(17,18)$|309781/310155|
|十二度中心楔形|$\tau=0$|$(16,17,18)$|29629/30015|
|十二度中心楔形|$\tau=1$|$(16,17,18)$|3671143/3721860|
|十三度中心楔形|$\tau=0$|$(16,17,18)$|3701201/3721860|
|十三度中心楔形|$\tau=1$|$(16,17,18)$|1419/1426|
|刚性四锁|$\tau=0$|$(16,17,19,18)$|9856/10005|
|刚性四锁|$\tau=1$|$(16,17,19,18)$|118679/120060|
|刚性四锁|$\tau=2$|$(16,17,19,18)$|29804/30015|
|刚性四锁|$\tau=3$|$(16,17,19,18)$|39961/40020|

九型全部严格。最大值为 $309781/310155<1$。因此每个实际超图经完整分流都获得一个成功概率为正的条件排列，故可二染。$\square$

#### A4 · 5. 实际复现与状态

最终证书 [CERTIFICATE.json](context/propertyb-m6-67-progress-20261029/34_min11/CERTIFICATE.json) 由 [certificate.py](context/propertyb-m6-67-progress-20261029/34_min11/certificate.py) 产生，使用既有独立下降阶乘注入计数、独立 bottom-up component 精确边数 DP 和逐项避点配额最大值扣除。九型实际约0.078 CPU秒。

第二脚本 [replay_original.py](context/propertyb-m6-67-progress-20261029/34_min11/replay_original.py) 使用原二项式概率核和原递归 component DP，九型全部复算，21个实际配额输入逐项一致，约0.028 CPU秒。结果保存于 [REPLAY_ORIGINAL.json](context/propertyb-m6-67-progress-20261029/34_min11/REPLAY_ORIGINAL.json)。两套概率计数和两套 component 实现给出相同精确有理数。可分别执行：

```sh
python3 context/propertyb-m6-67-progress-20261029/34_min11/certificate.py
python3 context/propertyb-m6-67-progress-20261029/34_min11/replay_original.py
```

[PAIR_PROBE.json](context/propertyb-m6-67-progress-20261029/34_min11/PAIR_PROBE.json)、[TRIPLE_PROBE.json](context/propertyb-m6-67-progress-20261029/34_min11/TRIPLE_PROBE.json)、[SPECIAL_PROBE.json](context/propertyb-m6-67-progress-20261029/34_min11/SPECIAL_PROBE.json) 及其脚本仅为保留的有界诊断记录，不是最终完整域。最终证明只依赖上述九型和实际选点引理，不依赖未通过的其他试探型，也没有扩大整图枚举。

</details>

<details class="proof-appendix" id="appendix-a5">
<summary>A5 · 35点：最小度九</summary>

### A5 · 35 vertices, minimum degree nine: a complete candidate

Let H be the same simple six-uniform pair-covering hypergraph, with $v=35, M=66$, degree sum396 and actual minimum degree9. The existing adaptive certificate closes the case where a minimum-degree vertex x has a unit-codegree neighbor of degree at most11. Thus fix x of degree9 and assume every member of A={z:lambda(x,z)=1} has degree at least12. Put u=|A|. The x row gives u≥23, while the total excess above degree9 is81, so3u≤81 and u≤27.

#### A5 · Lemma: a low nonunit partner of codegree two exists

There are n=34−u nonunit partners of x. Their total sum of lambda(x,z)−1 is11. Let l be the number with lambda exactly two. The other n−l partners each contribute at least two, so11≥l+2(n−l), or l≥57−2u.

If all these l partners had degree at least11, their degree excess above9, together with A, would be at least

$$3u+2l \ge 114-u \ge 87 >81,$$

contradiction. Hence an actual y outside A∪{x} has degree e∈{9,10} and lambda(x,y)=2.

#### A5 · Lemma: an actual low common unit neighbor exists

The number of nonunit partners of y is at most5e−34. One of them is x, which does not belong to A. Thus the common unit pool C=A∩{z:lambda(y,z)=1} has size

$$|C|\ge u-(5e-35)=u+35-5e.$$

All A vertices have degree at least12. After charging3u excess units to A and e−9 units to y, the remaining degree excess is at most81−3u−(e−9). Therefore C contains z of degree at most

$$12+\operatorname{floor}((81-3u-(e-9))/(u+35-5e)).$$

If e=9, u≥23 makes the numerator at most12 and denominator at least13; hence d(z)=12. If e=10, numerator at most11 and denominator at least8, so d(z)≤13 (and at least12). The denominator is positive in both cases. The three selected vertices are distinct; their codegrees are lambda(z,x)=lambda(z,y)=1, lambda(x,y)=2.

#### A5 · Complete actual traces and arithmetic

Label z as0, x as1, y as2. The only degree triples are (12,9,9), (12,9,10), (13,9,10). Let tau∈{0,1} be the actual triple intersection multiplicity. Their complete trace counts are

$$ell_7=tau, ell_3=ell_5=1-tau, ell_6=2-tau,$$
$$ell_1=d(z)-2+tau, ell_2=6+tau, ell_4=e-3+tau,$$
$$ell_0=66-sum_{T≠0}ell_T.$$

All six complete local types have a strict conditional failure bound using the proven component quota separately for each avoided pool, taking the maximum valid deduction against the same actual bad-pair vector. The submitted exact values and layouts are in LOW_PAIR_CENTER35.json, produced by low_pair_center35.py using component_kernel.py. The largest submitted value is14882237/14887440<1. Together with the imported adaptive cases e≤11 this covers the entire v35, minimum-degree9 branch.

Status: primary-agent paper derivation and exact arithmetic; independent replay and cross-family review pending. This is one internal branch, not the whole m(6)≥67 theorem.

</details>

<details class="proof-appendix" id="appendix-a6">
<summary>A6 · 35点：最小度十</summary>

### A6 · 35 vertices, minimum degree ten: complete candidate

**Theorem.** Every finite simple six-uniform pair-covering hypergraph with exactly $66$ edges, $35$ vertices, and actual minimum degree ten is two-colorable.

**Status.** Complete computer-assisted proof candidate. Independent replay and cross-family review of this final branch are pending. This proof uses the same exact conditional permutation failure mechanism and valid bad-pair deletion imported in [PROOF36_38.md](#appendix-a8). It adds no assumption to the original Property B target: pair coverage and the vertex/degree case are internal counterexample branches.

Let $H$ be this same actual hypergraph. Write $d(x)$ and $\lambda_{xy}$ for its actual degrees and codegrees. Then

$$\sum_xd(x)=396,\qquad d(x)\ge10,\qquad
\sum_{y\ne x}(\lambda_{xy}-1)=5d(x)-34.\tag{1}$$

The total degree excess above ten is $396-35\cdot10=46$. Every degree-ten vertex has at most sixteen nonunit partners, and hence at least eighteen unit-codegree neighbors.

#### A6 · 1. Complete accepted numerical configurations

[CERT35_MIN10.json](context/propertyb-m6-67-progress-20261029/mid34_38/CERT35_MIN10.json) contains only the 102 successful records used in this proof; [finalize_min10_35.py](context/propertyb-m6-67-progress-20261029/mid34_38/finalize_min10_35.py) extracts them from the actual completed calculations and fixes their successful labels, positions, multiplicities and exact rational bounds. These are three complete input domains.

**A. A unit pair of degree-ten vertices.** Suppose $x,y$ both have degree ten and $\lambda_{xy}=1$. The unit neighbors of $x$ other than $y$ number at least seventeen, whereas $y$ has at most sixteen nonunit partners. Thus some actual $z$ has $\lambda_{xz}=\lambda_{yz}=1$. Its degree $f$ lies in $[10,56]$ by the total degree sum. The actual unit triple has one of the two usual complete trace patterns. Nonnegative empty-trace multiplicity imposes $f\le49$ in the separate-edge pattern, and $f\le48$ in the one-triple-edge pattern. Thus precisely $40+39=79$ necessary nonnegative degree/trace types remain. All have strict failure bounds, extracted from [ADAPTIVE_COMPONENT.json](context/propertyb-m6-67-progress-20261029/mid34_38/ADAPTIVE_COMPONENT.json). The broader historical generator also recorded fifteen negative-multiplicity tuples; they are impossible actual inputs and are excluded from the final certificate.

**B. A degree-ten vertex with two degree-eleven unit neighbors.** Here the degrees are $(10,11,11)$, the two codegrees incident to the degree-ten point are one, the other codegree $\lambda$ ranges from one to eleven, and the triple intersection multiplicity $\tau$ is zero or one. Exactly 21 of these tuples have nonnegative actual trace multiplicities; the excluded tuple $\lambda=11,\tau=0$ would require a negative singleton multiplicity. All 21 have strict bounds in [TWO_ARMS35.json](context/propertyb-m6-67-progress-20261029/mid34_38/TWO_ARMS35.json) and are copied into the final certificate.

**C. A degree-twelve common unit center of a codegree-two pair of degree-ten points.** Label the degree-twelve center as zero and the degree-ten points as one and two. The codegrees are $\lambda_{01}=\lambda_{02}=1$, $\lambda_{12}=2$. There are exactly two actual trace patterns, indexed by $\tau\in\{0,1\}$:

$$\ell_7=\tau,\quad\ell_3=\ell_5=1-\tau,\quad\ell_6=2-\tau,$$

$$\ell_1=10+\tau,\quad\ell_2=\ell_4=7+\tau,\quad\ell_0=38-\tau.$$

The actual completed calculation [LOW_PAIR_MIN10_35.json](context/propertyb-m6-67-progress-20261029/mid34_38/LOW_PAIR_MIN10_35.json) gives

$$\tau=0:\quad U=185588/186093<1,\quad p=(17,18,19),$$

$$\tau=1:\quad U=1644827/1654160<1,\quad p=(17,16,18).$$

The lock positions are indexed by the stated labels. These two rows also appear in the final certificate. Each strict configuration produces an actual coloring, regardless of how those actual locks were selected.

#### A6 · 2. Low codegree-two partner

Assume for contradiction that $H$ is not two-colorable. Domain A implies that no degree-ten point has a degree-ten unit neighbor. Domain B implies that no degree-ten point has two degree-eleven unit neighbors.

Fix any degree-ten point $x$ and let $A$ be its unit-neighbor set, of size $u$. Then $u\ge18$. Every member of $A$ has degree at least eleven and at most one has degree eleven. Therefore the degree excess contributed by $A$ is at least $2u-1$. Since the entire excess is 46,

$$18\le u\le23.$$

Let $l$ be the number of actual partners $y$ with $\lambda_{xy}=2$. There are $34-u$ nonunit partners in total. The other $34-u-l$ partners have codegree at least three. By the exact row excess in (1),

$$16\ge l+2(34-u-l),\qquad l\ge52-2u.\tag{2}$$

If all these $l$ partners had degree at least eleven, their contribution to the degree excess, together with that of the disjoint set $A$, would be at least

$$(2u-1)+l\ge(2u-1)+(52-2u)=51>46,$$

contradiction. Hence there is an actual degree-ten point $y$ satisfying $\lambda_{xy}=2$.

#### A6 · 3. An actual degree-twelve common unit center

Let $P=\{z:d(z)\ge12\}$ and write $c=|P|$. Every degree-ten point has at least eighteen unit neighbors, none of degree ten and at most one of degree eleven. Thus it has at least seventeen unit neighbors inside $P$. In particular $c\ge17$. Each member of $P$ contributes at least two units of the total excess, so $c\le23$.

The actual degree-ten points $x,y$ from §2 therefore have at least

$$17+17-c=34-c\ge11$$

common unit neighbors in $P$. Suppose all those common neighbors had degree at least thirteen. Their additional excess beyond twelve is at least $34-c$. Counting the baseline excess two from every member of $P$ would then give

$$46\ge2c+(34-c)=c+34\ge51,$$

contradiction. Hence there is an actual common unit neighbor $z$ of degree exactly twelve. It satisfies

$$d(z)=12,\quad d(x)=d(y)=10,\qquad
\lambda_{zx}=\lambda_{zy}=1,\quad\lambda_{xy}=2.$$

This is precisely accepted numerical domain C. It gives an actual valid coloring of $H$, contradicting the assumption. Therefore the theorem holds. ∎

#### A6 · Reproducibility and scope

The exact final certificate has 79+21+2=102 rows, all with nonnegative actual multiplicities and strict rational upper bounds. Each row records the deletion method it actually used: the first group uses the common integer avoided-subset vector with the previously proved component-support quota; the other groups use the maximum of the valid single-subset component-quota deductions. Neither method adds overlapping deductions.

[finalize_min10_35.py](context/propertyb-m6-67-progress-20261029/mid34_38/finalize_min10_35.py) regenerates the final certificate from the completed source JSON files. The probability kernel is reused from the project; this is not an independent implementation. The final proof uses none of the non-strict or interrupted fourth-lock exploratory domains documented in [STATUS35.md](#appendix-a7).

</details>

<details class="proof-appendix" id="appendix-a7">
<summary>A7 · 35点：最小度十一</summary>

#### A7 · The minimum-eleven case is complete

Assume $v=35$, degree sum $396$, pair coverage, and minimum degree eleven. Set $R=\{x:d(x)=11\}$ and $r=|R|$. Since all other degrees are at least twelve,

$$396\ge11r+12(35-r)=420-r,$$

so $r\ge24$. A point $x\in R$ has at most $55-34=21$ nonunit neighbors. Thus it has a unit neighbor $y\in R$ because $r-1-21\ge2$. For the specified actual unit edge $xy$, the fixed-edge weak-wedge lemma in [PROOF36_38.md](#appendix-a8) applies:

$$5(d(x)+d(y))=110<2\cdot35+2\cdot24-6=112.$$

Consequently there is an actual three-lock weak wedge with all degrees eleven, two unit pairs and the remaining pair of codegree one or two. Its triple intersection multiplicity is zero or one. [min11_35.py](context/propertyb-m6-67-progress-20261029/mid34_38/min11_35.py) generates all eight labelled codegree/trace possibilities (all-unit traces are repeated under the irrelevant doubled-pair label; this redundancy is harmless). Every row in [MIN11_35.json](context/propertyb-m6-67-progress-20261029/mid34_38/MIN11_35.json) is strict. Thus every actual hypergraph in this minimum-degree case is colorable. ∎

</details>

<details class="proof-appendix" id="appendix-a8">
<summary>A8 · 36–38点：完整实际分支</summary>

### A8 · Complete conditional closure at 36,37,38 vertices

#### A8 · Theorem and imports

**Theorem.** Every finite simple six-uniform pair-covering hypergraph with exactly $66$ edges and $v\in\{36,37,38\}$ is two-colorable.

**Status.** Complete computer-assisted proof candidate, conditional only on the explicitly imported probability mechanism below; independent numerical verification pending. This closes these three internal vertex branches of the original $m(6)\ge67$ target. It does not by itself prove that full target.

Write $d(x)$ and $\lambda_{xy}$ for actual degrees and codegrees of this same hypergraph. Pair coverage gives

$$\sum_xd(x)=396,\qquad d(x)\ge\lceil(v-1)/5\rceil,\qquad
\sum_{y\ne x}(\lambda_{xy}-1)=5d(x)-(v-1).\tag{1}$$

The imported conditional random-greedy failure bound, exact endpoint and ordered-pair weights, valid bad-pair deletion, and full actual edge-trace recovery are those in [context/propertyb-m6-66-20261029/PROOF_M6_GE66.md](context/propertyb-m6-66-20261029/PROOF_M6_GE66.md), §§3–4, with the budget $65$ replaced by $66$. Both actual three-unit-lock patterns must be retained. A strict conditional failure bound below one produces an actual successful ordering and hence a valid coloring of the original hypergraph.

[REPORT.md](context/propertyb-m6-67-progress-20261029/mid34_38/REPORT.md), Lemma 1, proves the successive minimum-unit-neighbor selection used below. Its statement and proof are part of this package. The component-support quota and avoided-subset joint vector used in [ADAPTIVE_COMPONENT.json](context/propertyb-m6-67-progress-20261029/mid34_38/ADAPTIVE_COMPONENT.json) are explained and proved there. Their use is a valid strengthening of the original probability bound. The four-lock calculations use the weaker, cheaper deduction $\max_R D_R$, where each $D_R$ is the least possible bad-pair weight within that one avoided-subset pool. Taking a maximum is valid because the actual bad-pair weight is at least each $D_R$; the deductions are never added.

#### A8 · Lemma 2: a weak wedge through one specified actual unit edge

Let $R$ be an actual vertex subset of size $r$, and let $a,b\in R$ satisfy $\lambda_{ab}=1$. If

$$5(d(a)+d(b))<2v+2r-6,\tag{2}$$

then there exists $z\in R\setminus\{a,b\}$ such that either

$$\lambda_{az}=1,\quad\lambda_{bz}\le2,
\qquad\text{or}\qquad
\lambda_{bz}=1,\quad\lambda_{az}\le2.$$

Thus the three actual locks have either all three codegrees one, or exactly one codegree two and the other two one.

**Proof.** For $x\in R$, let $u_x$ be the number of its unit-codegree neighbors in $R$. Suppose no such $z$ exists. Each unit neighbor of $b$ other than $a$ then has codegree at least three with $a$. None of these vertices is a unit neighbor of $a$. Counting all $r-1$ row entries with baseline two, subtracting one for the $u_a$ unit entries and adding one for the $u_b-1$ specified entries, gives

$$\sum_{z\in R\setminus\{a\}}\lambda_{az}
\ge2(r-1)-u_a+(u_b-1).$$

Every vertex outside $R$ has codegree at least one with $a$. Using (1), the left side is at most $5d(a)-(v-r)$. Therefore

$$u_b-u_a\le5d(a)-v-r+3.$$

Interchanging $a,b$ gives the reverse inequality with $d(b)$. Adding contradicts (2). ∎

#### A8 · Lemma 3: an additional lock with total codegree excess at most one

Let $S$ be three actual locks, with degree sum $T$, and let

$$L=\sum_{\{x,y\}\subset S}(\lambda_{xy}-1),\qquad
E=5T-3(v-1)-2L,\qquad n=v-3.$$

Then at least

$$p=n-\lfloor E/2\rfloor\tag{3}$$

outside vertices $w$ satisfy $\sum_{x\in S}(\lambda_{xw}-1)\le1$. If $p>0$ and the actual minimum degree is $\delta$, one such $w$ has degree

$$\delta\le d(w)\le D:=\delta+\left\lfloor\frac{396-T-n\delta}{p}\right\rfloor.\tag{4}$$

**Proof.** Sum the three rows in (1), and remove their internal terms. Every internal excess is counted twice, leaving exactly $E$ as the nonnegative sum of codegree excesses from $S$ to its complement. At most $\lfloor E/2\rfloor$ outside vertices have excess at least two, proving (3). The sum of degree excess over $\delta$ on all outside vertices is $396-T-n\delta$. Among at least $p$ eligible vertices, one has excess at most its quotient by $p$, proving (4). The fourth lock has all three new codegrees one, or one new codegree two and the other two one. ∎

#### A8 · Lemma 4: complete actual trace generation

For four labelled locks, let $\lambda_{ij}$ be their six actual codegrees. Every original edge with at least two selected locks gives a clique block $B\subseteq\{0,1,2,3\}$. The block multiset satisfies

$$\sum_{B\supseteq\{i,j\}}m_B=\lambda_{ij}\quad(i<j),\qquad m_B\in\mathbb N.$$

Conversely, all nonnegative solutions are generated by the function `parts(target)` in [four_repair.py](context/propertyb-m6-67-progress-20261029/mid34_38/four_repair.py). It orders the eleven possible blocks (six pairs, four triples, one quadruple), recursively removes one block only when all its pair capacities are still positive, and allows repetition of the same block. The sorted-index restriction selects one order for every multiset. Every nonempty target solution contains some allowable block, and induction on the total remaining pair capacity proves completeness.

The restriction $B\mapsto B\cap\{0,1,2\}$ must equal the already known parent-triple block multiset; the scripts enforce this equality. Thus the fourth-lock computation preserves, and does not forget, the actual parent trace. For given four degrees and blocks, the singleton multiplicity at lock $i$ is $d_i-\sum_{B\ni i}m_B$ and the empty multiplicity is $66$ minus all nonempty multiplicities. Every actual hypergraph has nonnegative multiplicities, so negative tuples may be discarded.

#### A8 · The 37- and 38-vertex branches

The full minimum-degree domains from (1) and the degree sum are respectively $\delta=8,9,10$. Apply [REPORT.md](context/propertyb-m6-67-progress-20261029/mid34_38/REPORT.md), Lemma 1: choose an actual minimum-degree point, its minimum-degree unit neighbor, and, where necessary, a minimum-degree common unit neighbor. At these two vertex counts, every reached unresolved two-lock branch has strictly positive common-pool bound, so this selection always produces the required actual unit triple. The exact ranges are generated in [adaptive_component.py](context/propertyb-m6-67-progress-20261029/mid34_38/adaptive_component.py) and retained in [ADAPTIVE_COMPONENT.json](context/propertyb-m6-67-progress-20261029/mid34_38/ADAPTIVE_COMPONENT.json) (nine $(\delta,e)$ branches at 37 vertices and six at 38).

Every branch whose two-lock bound is strict is finished there. Otherwise both actual triple traces and the complete degree interval from Lemma 1 are tested. The selected success layouts give strict bounds except for exactly fifteen labelled triple types at 37 vertices and twelve at 38 vertices. No failure is dropped: they are the `failures` records of the corresponding branches.

For each of those twenty-seven types, apply Lemma 3 with $L=0$ and the same actual minimum degree $\delta$. Every resulting $p$ is positive. The complete fourth-degree interval, all four new codegree possibilities, all multiset clique partitions, and the exact restriction to the known parent trace are generated by [four_repair.py](context/propertyb-m6-67-progress-20261029/mid34_38/four_repair.py). Every resulting type has a strict failure bound:

|$v$|parent triple types requiring extension|complete four-lock types|largest bound|
|---:|---:|---:|---:|
|37|15|1452|$1334992/1335015$|
|38|12|855|$7563883/7565085$|

All fractions and actual lock positions are in [FOUR_REPAIR.json](context/propertyb-m6-67-progress-20261029/mid34_38/FOUR_REPAIR.json). Its `coverage` records contain every parent, $p$, $D$, row count and completion flag. The file has `complete=true` and no non-strict row. Therefore every original hypergraph at either vertex count reaches a strict probability bound. ∎

#### A8 · The 36-vertex branch

Here the actual minimum degree ranges over $7,8,9,10,11$.

For $\delta=7,8,9$, use Lemma 1 and the complete corresponding branches of [ADAPTIVE_COMPONENT.json](context/propertyb-m6-67-progress-20261029/mid34_38/ADAPTIVE_COMPONENT.json). All of their two-lock or conditional three-lock types are strict; none has a pool or probability gap.

Suppose $\delta=10$. Let $R=\{x:d(x)\le12\}$. Since vertices of $R$ have degree at least ten and the others at least thirteen,

$$396\ge10r+13(36-r)=468-3r,$$

so $r\ge24$. Fix an actual minimum-degree point $a\in R$. It has at most $50-35=15$ nonunit neighbors by (1). Therefore $a$ has at least $r-1-15\ge8$ unit neighbors inside $R$; choose one, $b$. Since $d(a)+d(b)\le22$,

$$5(d(a)+d(b))\le110<2\cdot36+2\cdot24-6=114.$$

Lemma 2 produces an actual weak unit wedge containing $a$, with degrees $(10,e,f)$ and $10\le e,f\le12$. Reorder the other two labels so that $e\le f$. All three pairs are unit, or one of the three pairs has codegree two. In either case the triple intersection multiplicity is zero or one. These are exactly the $6\cdot4\cdot2=48$ labelled degree/codegree/trace types generated in [min10_36.py](context/propertyb-m6-67-progress-20261029/mid34_38/min10_36.py).

Twenty-nine have a strict triple bound. For each of the nineteen others, Lemma 3 applies with $L=0$ or $1$ as appropriate and $\delta=10$. The smallest resulting $p$ is two among these failed types (the formal generator computes it afresh). The complete four-lock multiset classification, retaining the known parent trace, gives 3048 types. Every one is strict, with largest bound

$$480239/480240<1.$$

[MIN10_36.json](context/propertyb-m6-67-progress-20261029/mid34_38/MIN10_36.json) contains all 48 triple records, all 3048 fourth-lock records, and every completed parent degree interval. It has `complete=true` and no non-strict fourth-lock record.

Finally suppose $\delta=11$. The degree sum forces every one of the 36 degrees to equal eleven. There is an actual unit edge: (1) gives at most twenty nonunit neighbors at every point, leaving at least fifteen unit neighbors. Use $R=V$ in Lemma 2; condition (2) holds because $110<138$. The resulting weak wedge has degrees $(11,11,11)$. Relabel its center as lock zero, so the other pair has codegree one or two. The two all-unit traces have strict bounds, recorded in [WEDGE36.json](context/propertyb-m6-67-progress-20261029/mid34_38/WEDGE36.json). For the two traces with the remaining pair of codegree two, Lemma 3 has

$$E=165-105-2=58,\qquad n=33,\qquad p=4.$$

All outside degrees are eleven, so the fourth lock has degree eleven. The complete four-lock classification consists of 31 types, all strict with maximum $4962203/4962480<1$, recorded in [WEDGE_FOUR36.json](context/propertyb-m6-67-progress-20261029/mid34_38/WEDGE_FOUR36.json) and generated by [wedge_four36.py](context/propertyb-m6-67-progress-20261029/mid34_38/wedge_four36.py).

These cases cover every actual minimum degree. Every input therefore reaches a strict conditional failure bound, yielding a valid coloring. This completes the 36-vertex branch and hence the theorem. ∎

#### A8 · Certificate and reproduction map

- [adaptive_component.py](context/propertyb-m6-67-progress-20261029/mid34_38/adaptive_component.py) / [ADAPTIVE_COMPONENT.json](context/propertyb-m6-67-progress-20261029/mid34_38/ADAPTIVE_COMPONENT.json): minimum-unit-neighbor selection; only the strict two-lock rows or complete strict conditional-three branches are used directly.
- [four_repair.py](context/propertyb-m6-67-progress-20261029/mid34_38/four_repair.py) / [FOUR_REPAIR.json](context/propertyb-m6-67-progress-20261029/mid34_38/FOUR_REPAIR.json): every remaining actual triple at 37 and 38 vertices, fully extended and strict.
- [min10_36.py](context/propertyb-m6-67-progress-20261029/mid34_38/min10_36.py) / [MIN10_36.json](context/propertyb-m6-67-progress-20261029/mid34_38/MIN10_36.json): the complete fixed-edge weak-wedge domain at minimum degree ten.
- [wedge36.py](context/propertyb-m6-67-progress-20261029/mid34_38/wedge36.py) / [WEDGE36.json](context/propertyb-m6-67-progress-20261029/mid34_38/WEDGE36.json): the two successful unit traces in the regular-eleven branch; its two non-strict rows are continued rather than claimed strict.
- [wedge_four36.py](context/propertyb-m6-67-progress-20261029/mid34_38/wedge_four36.py) / [WEDGE_FOUR36.json](context/propertyb-m6-67-progress-20261029/mid34_38/WEDGE_FOUR36.json): those two remaining weak-wedge traces, fully extended and strict.

Every successful row fixes its actual positions, degrees, trace and exact rational upper bound. The Python scripts reuse the original probability kernel; this package does not claim independent arithmetic replay or Lean verification.

</details>

<details class="proof-appendix" id="appendix-a9">
<summary>A9 · 39点：弱四锁分支</summary>

### A9 · M66：39点完整纸面分支候选

本节固定同一实际有限简单六元超图H，恰66边、39点、点对覆盖、总度396。点对覆盖给最低度至少8。沿用上层条件排列失败概率公式，并用[PROOF40_41.md](#appendix-a10)§2的同一实际坏对向量最大避点配额扣除；本文不增加原目标的假设。

#### A9 · 引理1：实际弱四锁的选择

存在三个两两共度1的锁x0,x1,x2，每点度数在8…10。设其度数和为t。还能选第四个不同锁y，使其度数在8…D(t)，且它到原三锁的三个共度均为1，或恰有一个共度为2、另两个为1。其中

$$E(t)=5t-114,\quad p(t)=36-\operatorname{floor}(E(t)/2),\quad D(t)=8+\operatorname{floor}((108-t)/p(t))$$

具体为t24,25,26时D10；t27,28,29时D11；t30时D12。

证明：前三锁存在性由整数Q引理在v39、D10给Z33,Q16，33>2·16。对每个S外点y，令 e_y=Σ_{x∈S}($\lambda_{xy}$−1)，点对覆盖给e_y≥0。前三锁两两共度1，故

$$\sum_{y\notin S}e_y=5t-2\cdot 3-3\cdot 36=5t-114=E(t)$$

于是至多floor(E(t)/2)名外点有e_y≥2；至少p(t)名有e_y≤1。外点的总度数超出最低度8的部分为396−t−36·8=108−t。若这至少p(t)名点的度数全部大于D(t)，超额就严格大于108−t，矛盾。因此其中有y度数至多D(t)。整数非负的三个$\lambda_{xy}$−1之和至多1，给所述共度型。∎

#### A9 · 引理2：完整实际迹分类

将前三锁按度数排列并标为0、1、2，第四锁标为3。任一至少二点迹消耗其包含的全部点对共度单位。引理1给完整K4的六个点对各有一个单位，并允许(0,3)、(1,3)、(2,3)中恰一个点对再有一个单位。至少三点迹的重数不可能超过1，因为其中含有原三锁中的点对，或至少两个到原锁的共度1点对；唯一可重复的至少二点迹就是被加倍的二点迹本身。

因此实际至少二点迹完全对应于上述六维点对重数向量的多重团分解：全单位型有6个带标签分解；每个指定加倍点对各有7个。`parts(target,idx)`按非递减团序递归扣除一个团的各点对单位，当且仅当余向量为零时接收。这枚举每个多重团分解恰一次，覆盖全部实际情况；无整图枚举。剩余单点迹重数由实际度数减去已经列出的含点迹重数决定，空迹为66减去总数。

#### A9 · 定理：39点分支可二染

引理1允许前三度数的全部非递减三元组8…10。对每组，以D(t)作为第四度数完整上限，逐项取第四度数8…D(t)，并列引理2的6+3·7=27种多重团分解，共999个必要局部型。每型的所有实际迹重数均已确定。

对999型，使用同一实际坏对向量最大避点配额扣除后，全有严格失败概率上界小于1，详见[CERT39.json](context/propertyb-m6-67-progress-20261029/tail39_41/CERT39.json)。每行保存前三／第四度数、加倍点对、实际多重迹、迹重数、条件排列布局和精确有理上界。初次使用七种连续四锁布局时965型严格，剩余34型在把加倍点对置于四个连续位置两端后全部严格。最大最终界为113467943/113476275<1。

这些布局允许锁的标签在排列中以任意顺序出现；概率核接收`positions[j]`作为锁j的位置。将加倍点对放在两端只是选择另一个合法条件排列，不改变实际超图、迹或坏对对象。

由原条件排列／贪心失败上界，严格小于1给至少一个成功二染色。因此本节覆盖完整39点实际分支。∎

#### A9 · 复现与范围

先运行`python3 context/propertyb-m6-67-progress-20261029/tail39_41/weak_four39.py`，再运行同目录[weak_repair39.py](context/propertyb-m6-67-progress-20261029/tail39_41/weak_repair39.py)。初次999型17.208 CPU秒，34型修复0.706 CPU秒，共17.914 CPU秒。[CERT39.json](context/propertyb-m6-67-progress-20261029/tail39_41/CERT39.json)合并两次的成功行；原始失败保留于[WEAK_FOUR39.json](context/propertyb-m6-67-progress-20261029/tail39_41/WEAK_FOUR39.json)，但已由[WEAK_REPAIR39.json](context/propertyb-m6-67-progress-20261029/tail39_41/WEAK_REPAIR39.json)逐项严格替代。

计算复用原条件排列权重。它是实际精确运行，并非独立第二实现；本分支仍待主代理核验、独立算术及全目标整合，不把局部候选升级为完整m(6)≥67结果。

</details>

<details class="proof-appendix" id="appendix-a10">
<summary>A10 · 40–41点：重选锁与完整分流</summary>

### A10 · M66：40、41点完整纸面分支候选

令 H 是同一实际有限简单六元超图，恰66边、点对覆盖，总度396。本文只处理 $v=40$、41；这些条件来自上层最小反例归约，而非原目标附加假设。度数下界均为8。冲突图以共度至少2连边，故每点 x 的冲突度至多 5d(x)−(v−1)。独立锁集因此两两共度恰1。本文复用上层条件排列概率及其端点／单交边对计数；没有新Lean结论。

#### A10 · 1. 选锁及完整迹

对 $L=\{x:d(x)\le10\}$，$\sum_{L}(11-d(x))\ge 11v-396$。整数Q选锁引理在 v40 给 Z44,Q14，44>3·14；在v41给Z55,Q12，55>4·12。因此分别存在四、五个度在8…10的实际单位锁。将它们按度数排序，再按此标签记录所有至少两点迹。共度恰1意味着这些迹的二点集恰好划分完整K4或K5的全部点对，每个迹恰有一条原边，故代码的全部6或32种带标签团划分是完整域。每个单点迹重数是该点度数减去含它的团数，空迹为66减去其余重数。

#### A10 · 2. 同一坏对向量上的避点配额

固定锁j及其条件位置h。对每个 $R\subseteq S\setminus\{j\}$，取经过j而避开R的实际边，其数为 f_R。删去j后的五元链接位于最多 v−1−|R| 点上。若其中相交无序边对数为 B_R，则由链接简单性，两条不同链接交集至多4，

$$5f_R\le v-1-|R|+4B_R$$

从而 $q_R=max(0,\operatorname{ceil}((5f_R-v+1+|R|)/4))\le B_R$。

所有R使用同一个实际坏对计数向量 z_{T,U}，其坐标是同时含j的无序迹型格，容量是 binom(ell_T,2) 或 ell_T ell_U，非负权 w_{T,U} 为两种有向条件排列权重之和。给定R，把所有满足$(T∪U)∩R=\varnothing$的格按权重递增填满q_R个单位，所得 D_{j,R} 是该单项配额下的精确最小成本，故不超过实际坏对总权。令 $D_j=\max_R D_{j,R}$，仍不超过同一实际总权。这里取最大值，绝不把不同R的配额成本相加。空R正是原完整池扣除，故只会加强原上界。

于是失败概率至多 $\sum_h min(A_h,B_h,Q_h-D_h)$，非锁点D_h=0。[kernel.py](context/propertyb-m6-67-progress-20261029/tail39_41/kernel.py)实现此式，所有比较为Fraction。

#### A10 · 3. 排除40点唯一失败迹

完整90型中，只有度数(8,8,8,10)、四锁同在一条原边E的型不严格。设其中三名八度锁为a,b,c。每名八度点冲突度至多1。L至少ceil(44/3)=15点，故E外至少9名L点；三名八度点总共至多3个冲突邻点。可取y∈L\E，与a,b,c均共度1。新四锁a,b,c,y不能同在一条原边F：a,b在E中的共边唯一，若F含它们则F=E，但y∉E。因此重选后仍属于同一完整90型域，并已排除唯一失败型。所有其他型的确切布局和严格有理界见证书。

#### A10 · 4. 排除41点所需的五点同边迹

可进一步要求：五个锁若同在一条边E，则其度数总和t必须为50。

证明：若原五锁S位于E且t≤49，首先，若有八度点y∉E，由于其冲突度至多0，它与任意四名S点构成新五个单位锁，且不全在一条原边内。否则E外的L点度数均为9或10。S的总低度权为55−t，E的第六点低度权至多3；故E外L点低度权至少55−(55−t)−3=t−3，每点权至多2，所以其人数至少ceil((t−3)/2)。S到外部的冲突关联总数至多Σ_{x∈S}(5d(x)−40)=5t−200。对40≤t≤49，

$$2ceil((t-3)/2)>5t-200$$

因此有E外低度点y至多与S中一人冲突，取四名非邻点加y。新五锁两两共度1，并不能同在一条原边：所选四名原锁中任一对的唯一共边是E。这个重选同时排除所有t≤49的五点同边迹。t=50的单一型由概率证书严格处理。∎

完整672型的概率表中，所有非严格型均是t≤49的五点同边迹，故全部由该结构重选覆盖。所有非五点同边迹均严格，不依赖度数和。

#### A10 · 5. 精确证书和结论

执行 `python3 context/propertyb-m6-67-progress-20261029/tail39_41/cert40_41.py`。[CERT40_41.json](context/propertyb-m6-67-progress-20261029/tail39_41/CERT40_41.json)保存90+672型的实际迹重数、成功／最佳布局、精确概率界及结构排除标识。完整运行实际CPU约25.303秒；无未闭型。脚本复用原概率原语，尚不是第二实现或独立核验。原始五锁试算和残余最大配额试算分别保留为[FIVE41.json](context/propertyb-m6-67-progress-20261029/tail39_41/FIVE41.json)和[QUOTA_PROBE.json](context/propertyb-m6-67-progress-20261029/tail39_41/QUOTA_PROBE.json)。

由上层实际概率判据，这给出v40、41两支的完整纸面候选。它不单独证明m(6)≥67；原始全域其余分支仍由主代理整合。

</details>

<details class="proof-appendix" id="appendix-a11">
<summary>A11 · 42–44点：尾部锁选择及完整迹</summary>

### A11 · Tail lock-selection review: 42, 43 and 44 vertices

**PASS (same-family / provisional).** The proposed structural selection arguments are valid. They remove every failing pattern recorded in [../pilot/FIVE.json](context/propertyb-m6-67-diagnosis-20261029/pilot/FIVE.json) at $v=42,43,44$, assuming its probability bounds are correct. This review reads those existing rational results and checks their classification/strictness; it does not independently recompute the probability formula, run a new probability table, or close $m(6)\ge67$.

Throughout, $H$ is a finite simple pair-covering six-uniform hypergraph, with at most 66 edges and hence total degree at most 396. Write $\lambda_{xy}$ for actual codegree. For $v\in\{42,43,44\}$, pair coverage implies
$$5d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,$$
so every degree is at least nine. Put $L=\{x:d(x)=9\}$ and $r=|L|$. The degree budget gives
$$396\ge9r+10(v-r)=10v-r,\qquad r\ge10v-396.$$
On $L$, join distinct vertices in the conflict graph $G$ when their codegree is at least two. Then
$$\deg_G(x)\le\sum_{y\ne x}(\lambda_{xy}-1)=45-(v-1)=46-v.$$
A greedy independent set therefore has size at least $\lceil r/(47-v)\rceil$. Every independent set in $G$ consists of actual degree-nine vertices with all pairwise codegrees exactly one. Thus the guaranteed independent-set sizes at $v=42,43,44$ are respectively 5, 9 and 15. At $v=44$, every vertex has degree nine because $9\cdot44=396$ already exhausts the budget.

**Lemma A (42 vertices: exclude a common five-point trace).** There are five degree-nine unit-codegree locks not contained together in any hyperedge.

**Proof.** Choose an independent five-set $S\subseteq L$, which exists because $r\ge24$ and $\Delta(G)\le4$. If no edge contains $S$, the result already holds. Otherwise fix $E\in H$ containing $S$. Since $|E|=6$,
$$|L\setminus E|\ge24-6=18.$$
There are at most $\sum_{x\in S}\deg_G(x)\le20$ conflict incidences between $S$ and $L\setminus E$. If every vertex of $L\setminus E$ had at least two neighbors in $S$, there would be at least 36 such incidences, a contradiction. Choose $y\in L\setminus E$ with at most one neighbor in $S$, and choose four vertices $A\subseteq S$ not adjacent to $y$. Then $T=A\cup\{y\}$ is independent. If an edge $F$ contained $T$, any two vertices of $A$ would lie in both $E$ and $F$. Their codegree is one, so $F=E$, contradicting $y\notin E$. Therefore $T$ has the required property. $\square$

**Lemma B (nine unit-codegree vertices: exclude every trace of size four or five).** If $S_0$ is a set of nine vertices with pairwise codegrees one, there is a five-set $T\subseteq S_0$ with $|F\cap T|\le3$ for every hyperedge $F$.

**Proof.** If every edge already meets $S_0$ in at most three vertices, choose any five of its vertices. Otherwise choose an edge $E$ with $|E\cap S_0|\ge4$. Since $|E|=6$, there are at least three vertices in $S_0\setminus E$. Choose three vertices $A\subseteq E\cap S_0$ and two vertices $B\subseteq S_0\setminus E$, and put $T=A\cup B$. The edge $E$ meets $T$ in exactly three vertices. For any other edge $F\ne E$, one has $|F\cap E\cap S_0|\le1$: two such vertices would have at least two common edges, contradicting unit codegree. Therefore
$$|F\cap T|\le |F\cap A|+|F\cap B|\le1+2=3.$$
This proves the lemma. $\square$

At $v=43$, the independent-set bound supplies nine degree-nine vertices, so Lemma B applies. At $v=44$, it supplies at least fifteen; take any nine and apply Lemma B. All selected vertices retain degree nine and unit pairwise codegree.

#### A11 · Exact correspondence with the existing table

For a labelled five-lock set, a multi-lock trace is encoded by a mask in $\{1,\ldots,31\}$ with at least two set bits. Unit codegree means the clique edge sets associated with these masks form an exact partition of the ten pairs of five labels. Conversely every such partition is a necessary trace pattern; singleton counts are recovered from degree nine and the empty count from the 66-edge budget. Extra global realizability conditions would only remove patterns and are unnecessary for this coverage argument.

A separate short recursive exact-pair-cover calculation rebuilt all 32 labelled partitions and confirmed equality with the 32 distinct masks lists at each of the three vertex counts. This was a classification check, not a new probability calculation. Every stored `strict` flag was checked against `Fraction(U)<1`.

The stored non-strict rows are exactly:

| $v$ | Masks | Stored $U$ |
|---:|---|---:|
|42|`[31]`|2607524/2561251|
|43|`[31]`|2607524/2561251|
|44|`[5,6,12,20,27]`|166491788/166481315|
|44|`[31]`|102923518/99888789|

Mask 31 is a five-point trace, excluded by Lemma A and Lemma B. Mask 27 has four set bits; the other four masks pair the omitted label with the four labels in 27. Thus the second $v=44$ failure is exactly a four-point trace plus its remaining four pairs. Lemma B excludes it, along with all five possible labelled four-point trace patterns. Only one of these five four-point patterns failed in this particular table; excluding all five is a valid stronger structural restriction and avoids relying on positional symmetry.

| $v$ | Structural restriction | Retained labelled patterns | Maximum stored $U$ among retained patterns |
|---:|---|---:|---:|
|42|Every trace has size at most 4|31|1382147533/1383075540|
|43|Every trace has size at most 3|26|48389416/48663769|
|44|Every trace has size at most 3|26|132269531/133185052|

Every retained value is strictly below one. These are exact rational comparisons of the stored numerical output, not a second probability implementation.

**Scope of acceptance.** Both short structural lemmas and their application to the recorded tail patterns pass. This justifies the proposed $v=42,43,44$ repair conditional on the existing certificate formula and table calculation. The task's remaining $31\ldots41$ domain is not addressed; no full new lower bound, Lean proof, or cross-family approval is claimed.

</details>

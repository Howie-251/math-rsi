# 合法根的唯一重gap与共同核：同会话证明稿

日期：2026-11-07。

本文仅整理主会话逐条冻结的证明，状态为 **same-session、未外审、未接受**。用户明确要求无外审、无预设证明预算；本轮没有科研运行、求解、证书重放或独立审核，不创建Goal或wiki。旧进口保留原保证，新增结论不升级验收。

本轮三种关键结果如下：

1. **合法根整类容量与跨chart约束。** 若777母体超过混合分划容量，每个合法chart只有一个重gap、两侧合法根数各至多2；六合法根整类因此人口至多75。四／五根每个chart的开重gap至少40点；在76点母体中，四根对面chart必须选择同一实际三角域，两对选域至少交8点，五根任意两中央gap至少交9点。三／四／五根尚未全排。
2. **Pure regular全路径横截。** 共同核、两份三满域和两侧同时供应落实两个完整实际端口矩形；每个矩形两池之并至多11点，双池均非单点时至多8点，故两远尾各至少14，相关双非单池时至少17。两侧低秩远尾各至多13，给独立26点外跨覆盖，但该余类尚未排除。
3. **严格分离完整条件类排除。** 全量中性低末／高首池至少一侧至多7，结合实际全路径横截式，排除 $|C_-|,|C_+|\ge7$ 的整个临界严格分离类；至少一侧小于7的余类仍开。

后两块的可读完整证明见[COMMON_CORES](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-root-gaps-and-common-cores-20261107/COMMON_CORES.md>)。全局757／766／767／777工作界仍为 **40／49／75／76**，不能将上述局部整类或全路径条件界升级为全局74／75。

## 1. 原对象、容量与准确进口

路径长度按实际点数计，并对子序列遗传；完整有序rank-3 signotope的每个四点packet至多变色一次。weak7比较同一对实际首末点的异色路径，长度和至少9，允许内部共享。

固定一个777母体 $Y$ 及同一交替符号 $\omega$，只使用已经证明合法的蓝根chart。取合法蓝根 $r$，在其chart中删根，得到767母体

$$
X=Y\setminus\{r\},\qquad n=|X|,
$$

即 $X$ 禁止 $B_6,R_7,\mathrm{weak7}$。$C$ 为balanced域（无 $B_6,R_6,\mathrm{weak7}$）的有效人口容量，$b$ 为756及其换色域的共同有效人口容量。本块使用 $b\ge4$；当前有效输入为 $b=25,C\le49$。

承重进口如下，均保持原来的工作证明／接受层级：

- [R20 §§2—4：合法chart及删根运输](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)。
- [完整根循环 §3.6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)：全部合法蓝根构成单一合法循环，数量 $3\le m\le6$，每个根的chart唯一。
- [全ambient合法根结构 §§6.1—6.3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>)：普适蓝中点、相邻根edgefan、闭gap局域。
- [混合分划稿 §4—5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-mixed-partition-bridge-20261106/PROOF.md>)：合法根普适蓝中点，以及实际分隔点两侧各有红六时的全路径混合分划。后者给 $|X|\le C+b$。

记 $\tau(X)$ 为命中 $X$ 中**全部实际红六**的最小顶点集人口。删去这样的横截后得到实际balanced域，所以

$$
n>C+b\quad\Longrightarrow\quad\tau(X)>b.\tag{1}
$$

以下合法根局域结论在反设 $n>C+b$ 下推进；不将条件结论预写为所有人口的全局混合分划桥。

## 2. 每个chart只有一个重gap

把除 $r$ 外的全部合法根按当前chart次序写为

$$
h_1<\cdots<h_{m-1}.
$$

相邻根edgefan保证 $h_1,h_{m-1}$ 分别就是 $X$ 的实际首、末点。每个合法根 $v$ 都是普适蓝中点：对任意 $x<v<y$，有 $\chi(x,v,y)=B$。若实际红六严格跨 $v$，便与同端 $B_3(x,v,y)$ 违反weak7。因此每条实际红六都唯一落在某个相邻闭gap

$$
[h_i,h_{i+1}],\qquad 1\le i\le m-2.
$$

对每个gap，取其**全部实际红六**的最小横截人口 $\tau_i$，称 $\tau_i\ge2$ 的gap为重gap。若全都 $\tau_i\le1$，各gap横截取并即命中全体红六，给

$$
\tau(X)\le m-2\le4\le b,
$$

违反(1)。故至少有一个重gap。

若有两个重gap，在它们之间取一个合法根 $v$。重gap的横截人口至少2，故即使 $v$ 是相应gap边界，各自也有避开 $v$ 的实际红六；于是 $v$ 的严格两侧各有红六。普适蓝中点同时给分隔定理所需的无跨越及蓝桥条件，混合分划迫 $n\le C+b$，矛盾。因此：

$$
\boxed{n>C+b\ \Longrightarrow\ \text{每个合法chart恰有一个重gap}.}\tag{2}
$$

## 3. 重gap外的路径只能贴其两端

固定唯一重gap

$$
[a,b']=[h_j,h_{j+1}],\qquad G=(a,b'),
\qquad k=m-1-j.
$$

这里 $b'$ 是实际右边界根，区别于容量 $b$；$j$ 是包括 $a$ 的左侧合法根数，$k$ 是包括 $b'$ 的右侧合法根数。

若有位于重gap左侧的实际红六不终于 $a$，则它严格位于 $a$ 左侧。重gap横截大于1，故其中存在避开 $a$ 的红六，严格在 $a$ 右侧。以合法根 $a$ 调用分隔定理即矛盾。反序同理，右侧外部红六必须始于 $b'$。所以

$$
\boxed{\text{任何重gap外的实际红六，必终于 }a\text{ 或始于 }b'.}\tag{3}
$$

这不等于全部红六都在重gap内；贴边的外部路径仍可能存在。

记 $\tau_G$ 为实际开域 $G$ 内全部红六的最小横截人口。由(3)，把这样的横截再加 $a,b'$ 即命中 $X$ 全体红六，因此

$$
\tau_G>b-2.\tag{4}
$$

在闭gap中定义实际开源集

$$
S_0=\{x\in G:\text{某条完全位于 }[a,b']\text{ 的实际红六始于 }x\}.
$$

每条见证红六的第二点也在 $G$，因为右端只有一个边界点 $b'$。其首对 $(x,y)$ 必满足

$$
\chi(a,x,y)=B,\tag{5}
$$

否则把 $a$ 前接见证红六便成红七。实际开末点及末对有全序反向的对应结论。

## 4. 重gap两侧合法根数各至多2

反设 $j\ge3$。在 $G$ 上，把 $x<y$ 且 $\chi(a,x,y)=B$ 记为 $x\prec_0 y$。它是传递关系：若 $x\prec_0 y\prec_0 z$，packet $(a,x,y,z)$ 的第一、第三项蓝，至多一次变色迫第二项 $\chi(a,x,z)$ 也蓝。

对任意三点0链 $x\prec_0 y\prec_0 z$，若 $\chi(x,y,z)=B$，则把全部 $j$ 个左侧合法根 $h_1,\ldots,h_j=a$ 前接，形成至少6点蓝路：根间三元组及最后两个根与 $x$ 的三元组来自合法根普适蓝中点，$\chi(a,x,y)=B$ 来自0链，最后一项由假设为蓝。这违反禁 $B_6$。

取任意 $x\in S_0$，以 $(x,y)$ 为一条实际见证红六的首对，故 $x\prec_0 y$。若有0型前驱 $t\prec_0 x$，则 $t,x,y$ 是0链。三元组 $\chi(t,x,y)$ 若红，前接见证红六成红七；若蓝，则由上一段成蓝六。两者都不可能。因此 $S_0$ 的每个点都无0型前驱，特别 $S_0$ 内没有0边。

若 $S_0$ 内有实际红六，其首对由(5)又是一条0边，矛盾。另一方面 $S_0$ 的点均为ambient红六源，不能结束ambient蓝五：蓝五接出红六的桥若蓝就成蓝六，若红就成红七。因此 $S_0$ 也无蓝五。

从 $a$ 前面的合法根中取两个实际点 $h<h'<a$。域 $S_0\cup\{h,h'\}$ 仍无蓝五，因为任何五点路径的末点必在 $S_0$，而该点不能结束ambient蓝五。它也无红六：全部位于 $S_0$ 的情形已排除；使用早根与 $G$ 点的红六会严格跨过合法根 $a$；只用两早根不足六点。于是它是实际756域，容量给

$$
|S_0|+2\le b.
$$

但 $S_0\cup\{a,b'\}$ 命中全部实际红六：重gap外由(3)命中；重gap内避开两端的红六必有源在 $S_0$。这给 $\tau(X)\le b$，违反(1)。故 $j\le2$。全序反向处理开末集同理得 $k\le2$。因此

$$
\boxed{j\le2,\qquad k\le2,\qquad m=j+k+1\le5.}\tag{6}
$$

## 5. 六合法根整类的容量后果

若777母体 $Y$ 恰有六个合法蓝根，反设 $|Y|>C+b+1$，任取合法根删去后 $n>C+b$，由(6)却得 $m\le5$，矛盾。所以整个六根类满足

$$
\boxed{m=6\quad\Longrightarrow\quad |Y|\le C+b+1\le75.}\tag{7}
$$

这里最后一步用当前有效 $C\le49,b=25$。这是六根整类的工作容量界，不是任意777母体的全局F75。

若 $m=5$ 且反设 $n>C+b$，则 $j+k=4$ 与(6)迫 $j=k=2$；所以**每个**合法chart都只有中央gap重。$m=3,4$ 仍未排除；五根的中央重gap共同实现也未闭合。

## 6. 五根中央重gap的三序分离条件

以下仍在 $n>C+b$ 的假设下，固定五合法根的循环次序为

$$
A,B,C,D,E.
$$

本节的根名 $C$ 区别于前文balanced容量 $C$；在提及容量时明确写“容量 $C$”。A-chart的根序为 $B<C<D<E$，中央开gap记作 $G_A=(C,D)$；C-chart的根序为 $D<E<A<B$，中央开gap为 $G_C=(E,A)$。这些是相应合法chart中的实际点域，令 $W=G_A\cup G_C$。

对 $x\in G_A$，A-chart中 $C<x<D$，根性质给 $\omega(A,C,x)=B$。对 $x\in G_C$，C-chart中 $E<x<A$，根色给 $\omega(C,x,A)=B$，循环换序同样得 $\omega(A,C,x)=B$。所以 $W$ 在A-chart中均位于 $C$ 之后。相邻根edgefan另给 $\omega(B,C,x)=B$，$\omega(A,B,x)=B$。

在 $W$ 上定义共同严格次序

$$
u\prec v\quad\Longleftrightarrow\quad
\text{A、B、C三个合法chart都将 }u\text{ 列在 }v\text{ 之前}.
$$

这是三个实际全序的交，因而传递；等价地，三个 $\omega(A,u,v),\omega(B,u,v),\omega(C,u,v)$ 都蓝。若四点 $u\prec v\prec w\prec t$ 形成共同蓝四，则A-chart内

$$
B_7(A,B,C,u,v,w,t)
$$

实际成立：根三元组蓝，$\omega(B,C,u)=B$ 来自edgefan，$\omega(C,u,v)=B$ 来自共同次序，最后两项来自蓝四。这违反母体禁蓝七。

取任意A中央gap的实际红六，其开源 $z\in G_A$ 与第二点 $w\in G_A$ 满足 $z\prec w$。A自身根色给 $\omega(A,z,w)=B$；B、C在该chart中均位于红六之前，若相应首桥为红就延成红七，所以 $\omega(B,z,w)=\omega(C,z,w)=B$。

对偶地，取任意C中央gap实际红六的开末 $y\in G_C$ 和末前驱 $u\in G_C$，有 $u\prec y$。此处必须使用准确根序：C-chart为 $D<E<A<B$，重gap是 $(E,A)$，所以A、B两根都在该红六之后。末帽给 $\omega(u,y,A)=\omega(u,y,B)=B$，循环换序后与C自身根色共同兑现 $u\prec y$。

假使后一个开末与前一个开源满足 $y\prec z$，便有

$$
u\prec y\prec z\prec w.
$$

C-chart中，红六末对 $(u,y)$ 不能后接 $z$，故 $\chi(u,y,z)=B$；A-chart中，红六首对 $(z,w)$ 不能前接 $y$，故 $\chi(y,z,w)=B$。这四点在三个chart中的次序相同，同一交替符号给相同颜色，因此是共同蓝四，与上面的共同蓝七矛盾。由此得到条件分离：

$$
\boxed{\text{不存在C中央开末 }y\text{ 与A中央开源 }z\text{ 满足 }y\prec z.}\tag{8}
$$

这是真实三序关系下的条件不相容，不是两个gap按某个单一chart全序分离；尚未证明它迫使共同横截、人口缺额或五根矛盾。外部红六仍只要求贴中央gap两端，不宣称全在中央gap内。

## 7. 开重gap至少40点与四／五根跨chart共同结构

### 7.1 首对有向图的三层横截

仍假设 $n>C+b$。固定一个chart的实际开重gap $G=(a,b')$，令 $g=|G|$，$t$ 为**全部完全位于开域 $G$ 内**的实际红六的最小横截人口。第3节已给

$$
t>b-2.
$$

图与横截只使用开gap中的完整红六，不把闭gap中贴两边界的路径混入。若有至少两个合法根在 $G$ 左侧，取其中最后两个 $h<a$，$a$ 就是左边界根；右侧至少两根时全序反向。

用 $G$ 内全部实际红六的首对 $(x,y)$ 给递增有向边 $x\to y$。每条有向路都是实际蓝路径：若连续两边 $u\to v\to w$ 满足 $\chi(u,v,w)=R$，把 $u$ 前接那条以 $(v,w)$ 开始、完全在 $G$ 内的红六，就成红七。

每条首边 $(x,y)$ 另有 $\chi(a,x,y)=B$，否则把 $a$ 前接其完整红六见证成红七。普适蓝中点又给 $\chi(h,a,x)=B$。因此两个左合法根可以前接任意最长有向路；若该路有 $d$ 个顶点，就得 $B_{d+2}$。禁蓝六迫 $d\le3$。

删去图中全部孤点后，按各点最长终路的顶点数1、2、3分层，每条边严格升层。每层都不含任何首边；联合全部孤点后，也不含 $G$ 内红六。因此若孤点数为 $i$，选择最大的一层与全部孤点可留下至少 $i+\lceil(g-i)/3\rceil$ 点无红六，其补集为实际横截，给

$$
t\le\left\lfloor\frac{2(g-i)}3\right\rfloor.
$$

因 $t>0$，$g\ge6$。$G$ 最后四个点都是孤点：红六首边的第二点之后还必须有四个 $G$ 点，首点更早；所以最后四点均不可能出现在任何首边的任一端。故 $i\ge4$，进而

$$
\boxed{t\le\left\lfloor\frac{2(g-4)}3\right\rfloor,\qquad
g\ge4+\left\lceil\frac{3t}2\right\rceil
\ge4+\left\lceil\frac{3(b-1)}2\right\rceil.}\tag{9}
$$

当前 $b=25$，$t\ge24$，故 $g\ge40$。四／五根chart总有至少两个合法根在重gap某一侧，因而这个结论对其每个chart都成立。证明不要求图连通，也不要求三层等大。

### 7.2 四根：对面chart同域选择，两对选域至少交8点

现取当前76点777临界候选 $Y$，四合法根的循环为 $A,B,C,D$。对每个合法chart，删根人口75超过当前混合容量，所以以上开重gap下界均适用。

A-chart根序为 $B<C<D$，其重gap只能是 $(B,C)$ 或 $(C,D)$，分别对应实际开三角域 $ABC$ 或 $ACD$。C-chart根序为 $D<A<B$，同两个实际域分别表现为 $(A,B)$ 或 $(D,A)$。

这里的“同一实际域”不是按chart标签猜测：$ABC$ 域由四点包 $\{A,B,C,x\}$ 的唯一少数点恰为非根 $x$ 刻画；相邻根edgefan与[R20少数点的实际身份不变](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)保证它在A、C两个合法chart中确为上述对应开gap。$ACD$ 同理。具体域对应亦见[全ambient根结构 §§6.2—6.3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>)。

两个域分割全部72个非根点。若A、C的重gap选择不同域，则两不交实际域各至少40点，矛盾。因此A、C必须选择**同一物理开三角域**。B、D反序同理，必须在 $BCD$、$BAD$ 中选同一实际域。

两对各自选中的实际域都至少40点，均在72个非根点中，故其交至少8点。这两个三角形总共享一个相邻根边：可能为 $AB,BC,CD,DA$ 中的一条。剩余共同实现是这两份相邻三角域的实际共享，不是四个chart独立选择重gap。

一般地，若每个候选实际域至少 $g_0$ 点，母体非根人口为 $N-4$，且 $2g_0>N-4$，同样迫对面chart同域选择；两对选域交至少 $2g_0-(N-4)$。这里并未排除该共享结构本身。

### 7.3 五根：任意两中央重gap至少交9点

在当前76点五合法根候选中，每个chart仍由第5节具有唯一中央重gap，并由(9)有至少40个实际非根点。共同母体只有71个非根点，所以任意两份中央开gap都满足

$$
\boxed{|G_r\cap G_s|\ge40+40-71=9\qquad(r\ne s).}\tag{10}
$$

这是同一母体中的两两实际交叠，不能推出五份gap有共同交点，也不能把各自横截或人口预算独立相加。一般下界为 $|G_r\cap G_s|\ge2g_0-(N-5)$。第6节三序分离与这里的物理交叠可共同保留，但尚未由此得到五根整类矛盾。

## 8. 共同核第二块与当前边界

本块完成唯一重gap、两侧根数约束、六根整类容量75及五根三序条件分离。它没有关闭五根中央gap共同实现，也没有关闭三／四根范围；不能宣称通用 $Q\le C+b$ 或全局F75。新增结论与旧进口均保持各自保证层级。

第二块已在[COMMON_CORES](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-root-gaps-and-common-cores-20261107/COMMON_CORES.md>)完整编排：§§1—6建立共同核、两份三满域及两侧同时供应；§§7—8给中性端口禁形及前后缀独立数；§§9—12给pure regular端点矩形11／8界、全路径横截与Ferrers条目；§13给严格分离完整横截式及König版本；§14给13＋13的外跨覆盖；§15给全量中性池至少一侧≤7，并关闭两覆盖域各至少7的整个严格分离条件类。

当前未闭的是三合法根范围、四根两相邻三角域的共同实现、五根中央gap的两两共享与三序分离、pure regular大尾的最终同步、至少一侧覆盖域小于7的严格分离余类，以及其他原未覆盖输入。恢复状态见[NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-root-gaps-and-common-cores-20261107/NEXT_SESSION.md>)。未冻结候选不作可用结论，没有外审或接受升级。

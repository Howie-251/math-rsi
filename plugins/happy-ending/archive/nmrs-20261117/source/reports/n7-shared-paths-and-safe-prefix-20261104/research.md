# N7 共享长路径的局部反例与安全前缀补入

日期：2026-11-04。**完整 I 空 r=3 类及一般 I 非空临界 r=2 类仍未排除，全局工作上界仍为 40/50/75/76。** 本轮主要成果是两个明确局部反例（Linux 一次 batch、两例全部验证）阻断错误路线，以及可安全补入前缀点的参数化整类上界；尚未从任意临界母体提取出该安全接口。


本轮从安全接口通向人口的主条件式为

\[
\boxed{n\le M+b-m+h\le3b-m+h,}
\]

其中 M≤2b 为 balanced 域的有效容量上界，m 为可安全补入的实际前缀点数，h 为命中其余全部长红路径所需的额外实际覆盖成本。只有在证明 h≤m−1 时，才排除相应临界类；本稿没有取得无条件 74。

全部新数学由主会话与授权生成协作者形成并冻结，指定原生 Sol/high 文档执行者忠实转写，状态为 **same-session、unreviewed/unaccepted**。反例的机械核验不升级历史接受，不是外部或独立数学评审。本轮执行账为 scientific_runtime_batches=1、fixture_generation=1、validation_cases=2、science_retries=0、solver_calls=0、external_review_calls=0（含 status）。本报告编排不重新运行科研验证。

## 0. 一般模型、容量输入与来源

设 p≥5。完整有序 rank-3 signotope X 对所有递增三元组染色，四点 packet 按 abc、abd、acd、bcd 至多一次变色。B_q、R_q 的长度计实际顶点；单色路径的有序子序列仍为同色路径。母体禁 B_(p+1)、R_(p+2)、weak(p+2)，后者禁止同一对实际首末点的异色路径长度和至少 p+4，不要求内部不交。

记 S、T 为 ambient 实际 R_(p+1) 源、末点，D=X\(S∪T)。沿用源终禁配给出的 T 无 B_p。b 为 N_sig(p+2,p,p+1) 及换色模型的共同有效整数上界；balanced 域（禁 B_(p+1)、R_(p+1)、weak(p+2)）沿用容量 2b。特别，X\T 无 R_(p+1)，所以是 balanced，人口至多 2b。记

\[
c_p=\binom{2p-4}{p-2},
\tag{1}
\]

这是同时无 B_p、R_p 的经典杯帽容量。全文先给一般参数，最后代 p=5、b=25；不新增外部容量输入。

只读数学与证据来源如下：

- [前稿：Hall 实际端点图与临界交换](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-hall-stars-and-critical-exchange-20261104/research.md>)，含 r=3 的实际早根接口和联合闭包。
- [旧 through-clique 完整反例族](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md>)，含经典 13 点校准例。
- [本轮 Linux 结果汇总](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/RESULTS.md>)、[数学规格](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/MATHEMATICAL_SPEC.md>)、[输入清单](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/input-manifest.json>)与 [证据哈希清单](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/artifact-manifest.json>)。
- [本报告起始来源 SHA 清单](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/source-manifest.json>)保护旧报告和全部已完成科学证据；原始文件保持不改。

## 1. 主定理：安全前缀补入

**安全补入定理。** 在上述一般母体中，取实际点 q、点集 A、Q，满足

\[
q<A<Q,\qquad Q\subseteq T,\qquad A\text{ 无 }B_p.
\]

假设：

1. 对所有 x<y∈A∪Q，都有 χ(q,x,y)=R。
2. 对每个 a∈A、t∈Q，都有实际 R_4(a,t)。各对可使用不同、甚至位于 A∪Q 以外的内部点。

则 Z=A∪Q 是实际 N_sig(p+2,p,p+1) 允许配置，因而

\[
\boxed{|A|+|Q|\le b.}
\tag{2}
\]

令 n=|X|、k=|T\Q|，得到

\[
\boxed{n\le3b+k-|A|.}
\tag{3}
\]

**证明。** 若 Z 有实际 R_(p+1)，由第一条件可在其首 pair 前接 q，得到 R_(p+2)，矛盾。

若 Z 有实际 B_p，按其首末点分情况：首点在 Q，则全部路径位于 Q⊆T，与 T 无 B_p 矛盾；首末都在 A，则整条路径位于 A，与 A 无 B_p 矛盾；其余只能首在 A、末在 Q。最后情形与第二条件给出的实际同端 R_4 长度和为 p+4，违反 weak(p+2)。因此 Z 无 B_p、R_(p+1)，并从母体继承无 weak(p+2)，式 (2) 成立。

又 X\T 是 balanced，人口至多 2b，因此

\[
n=|X\setminus T|+|Q|+k\le2b+(b-|A|)+k,
\]

即式 (3)。证毕。

若 m=|A|>k，整个满足该接口的类都不能达到临界人口 3b。这是实际容量证明和完整类排除，不是对任意母体已找到 A/Q 的声明。p=5、b=25 时，m=2、k=1 得

\[
n\le74.
\tag{4}
\]

### 1.1 安全端口与实际覆盖的传播桥

令 M 为 balanced 域的任一有效容量上界，取 M≤2b。设安全补入已经给出一个实际末点域 Q_0⊆T，及 m 个可安全补入的点，因此 |Q_0|≤b−m。若实际点集 H⊆X 命中全部末点不在 Q_0 的 R_(p+1)，则

\[
\boxed{n\le M+|Q_0|+|H\setminus Q_0|
\le M+b-m+h\le3b-m+h,\qquad h=|H\setminus Q_0|.}
\]

**证明。** Q_0∪H 命中全部实际 R_(p+1)：终于 Q_0 的路径由实际末点命中，其余由 H 命中。删除该实际点集后是 balanced 域，人口先由有效容量界为 M。覆盖按实际物理点并集计数，|Q_0∪H|=|Q_0|+|H\Q_0|，得到传播式。证毕。

因此 h≤m−1 的整个接口类至多 3b−1 点。这里 H 必须命中全部相应长路径，不能仅覆盖选定供应或代表路径。


p=5、m=2、h=1 时，限定接口先得到 n≤M+b−1；若保留精确结构容量，则链为

\[
n\le N_{\rm sig}(7,6,6)+N_{\rm sig}(7,5,6)-1
\le50+25-1=74.
\]

这不是任意 767 的无条件递推，仍须安全补入前提与 H 对全部剩余实际长路径的覆盖。
一个实际充分情形是 T 分成例外 E、Q_0、剩余 Q_1，另有源集 R_0 覆盖全部终于 Q_1 的实际 R_(p+1)。此时 H=E∪R_0 可用，额外成本仍为 |(E∪R_0)\Q_0|，不能把角色重合重复相加。

## 2. 共同前缀的可用推论

**共同前缀推论。** 显式要求 Q 非空。若

\[
q<a_1<\cdots<a_m<Q,\qquad \varnothing\ne Q\subseteq T,\qquad 1\le m\le p-3,
\]

且对每个 t∈Q，都有一条以共同前缀 (q,a_1,…,a_m) 开始、终于 t 的实际 R_(p+1)，其余内部点允许随 t 改变，则令 A={a_1,…,a_m}，安全补入定理成立，并有

\[
\boxed{n\le3b+k-m,\qquad k=|T\setminus Q|.}
\tag{5}
\]

**证明。** q 对 A 内部 pair 的三元组红，来自共同前缀本身。对 a_j∈A、t∈Q，实际 R_(p+1)(q,t) 与 weak 禁止同端蓝三，给 χ(q,a_j,t)=R。对 t<t'∈Q，同样用实际 R_(p+1)(q,t') 给 χ(q,t,t')=R。因此满足安全补入的第一条件。

A 人口 m<p，所以无 B_p。对每个 a_j、t，保留原路径从 a_j 到 t 的后缀，其长度为 p+1−j≥4；可保留实际首末点缩短为 R_4。满足第二条件，代入式 (3) 得式 (5)。证毕。

p=5 时，m=2 表示共同前三点 (q,a_1,a_2)。若 Q=T\{σ}，即 k=1，则该整个类至多 74 点。min T=max S=σ 是这种尾域切分的一种情况，不是本推论必需的完整排序假设。

后文 12 点反例的四个尾点 t_j 确有共同前三点 (q,a,b) 的实际红六

\[
(q,a,b,c,d_2,t_j).
\]

因此，保持这种共同前缀的整族不能被放大到 75 点；该机制比要求某中性点对全部尾 pair 统一红色更宽。尚未证明一般临界 r=2 母体必然具有这种共同前缀。

## 3. 新入口：末中性长路径与支持前缀

### 3.1 最大末点长路径入口

先写 p=5 的实际入口。设 d_2=last D>max S，Q=T∩(d_2,∞) 非空，k=|T\Q|。在 I 非空双 D 跳过接口中，这是末中性点入口；不先假定其对 Q 统一红扇。

d_2 后的实际点全部在 T，前稿终点段屏障给出

\[
\chi(d_2,t,u)=B\qquad(t<u\in Q).
\tag{6}
\]

**最大末点路径入口定理。** 若存在任意一条终于 t*=max Q、并经过 d_2 的实际红六，则

\[
\boxed{|Q|\le b-2,\qquad n\le3b+k-2.}
\tag{7}
\]

特别，p5、b25、k≤1 的整个接口类至多 74 点。

**证明。** d_2 必须是该红六的倒数第二点：否则其后至少还有两个 Q 点，与式 (6) 的蓝三元组冲突。记该红六为

\[
(q,a,b,c,d_2,t_*).
\]

任取 t∈Q、t<t*。packet (c,d_2,t,t*) 第二项 χ(c,d_2,t*)=R，末项 χ(d_2,t,t*)=B，迫首项 χ(c,d_2,t)=R。因此同一前五点 (q,a,b,c,d_2) 可后接每个 t∈Q，给出真正共同前三点 (q,a,b) 的红六供应。第 2 节共同前缀推论取 m=2，即得式 (7)。证毕。

若 min T=max S=σ，且 d_2 后的 Q=T\{σ}，则 k=1；12 点反例满足此入口。更一般，只需末中性 d_2 的蓝扇与至少一条最大末点长路径经过 d_2，不需要统一尾红扇。

一般 p≥5 的同样末中性入口中，若 d 后有上述蓝扇且一条终于 max Q 的实际 R_(p+1) 经过 d，则同理 d 为倒数第二点，并把同一前 p 点运输到每个 t∈Q。安全共同前缀可取 m=p−3，得到 n≤3b+k−(p−3)。这只是前两节证明在相同入口下的参数形式，不附加已提取端口的主张。

**剩余全路径量词。** 若 k≤1 的该临界分支仍存在，则全部终于 max Q 的实际红六都必须避开 d_2。仅找到一条跳过 d_2 的路径不能判定入口失败。尚未证明任意临界 r=2 母体都有 k≤1，或必有一条最大末点路径经过 d_2。

### 3.2 支持前缀 Q_0 及其非空入口

仍令 Q=T∩(d_2,∞)，并使用 d_2QQ 全蓝的实际末中性接口。定义

\[
Q_0=\{t\in Q:\ \text{存在以 }d_2\text{ 为倒数第二点的实际 }R_6\text{ 终于 }t\}.
\]

若 Q_0 非空，取 u=max Q_0 及其实际红六 (q,a,b,c,d_2,u)。对任意 t∈Q、t<u，同一个 packet (c,d_2,t,u) 给 χ(c,d_2,t)=R。因此所有 t≤u 的 Q 点都由同一前五点支持，Q_0 恰是 Q 的初段。共同前缀推论给出

\[
\boxed{|Q_0|\le b-2.}
\]

该式只限制被实际末 D 端口支持的前缀 Q_0，不限制整个 Q；Q\Q_0 仍可能非空。

完整双 D 跳过例外也能保证 Q_0 非空。设 σ=max S，σ<d_1<d_2<t_1，其他全部 D 在 σ 前，且有实际红六 P=(σ,d_1,t_1,t_2,t_3,t_4)，跳过 d_2。从红三元组 (d_1,t_1,t_2) 出发，当前中点记 x、末点记 y，取终于 x 的入红六，末前驱为 v。

记入红六的末三点为 (w,v,x)，其末帽给 χ(v,x,y)=B，否则可后接 y 成红七。若 v<d_1，因为 d_1∉T，保留入红六五点前缀后不能以红色接 d_1，故 χ(w,v,d_1)=B；原路径给 χ(w,v,x)=R。packet (w,v,d_1,x) 迫 χ(v,d_1,x)=R，再由 packet (v,d_1,x,y) 的首末红色迫 χ(v,x,y)=R，与末帽矛盾。若 v=d_1，末帽直接与当前红三元组冲突。这两种情形均不可能。

若 v>d_1 且 v∈T，packet (d_1,v,x,y) 将当前红三元组下降为更早中点 v 的红三元组 (d_1,v,x)。因为 (d_1,x) 内唯一可能不在 T 的点是 d_2，有限下降只能停止于 v=d_2。此时得到一条实际 R_6(…,d_2,x)，其中 x≤t_1，故 x∈Q_0，非空成立。

### 3.3 Q_1 非空也可通过低成本覆盖排除

设 I={σ}、min T=max S=σ，Q=T\{σ} 全在 d_2 之后，且 Q_0 非空。前节给 m=2 的安全端口 |Q_0|≤b−2。令 Q_1=Q\Q_0。

若终于 Q_1 的**全部实际红六**都从 σ 启动，则 H={σ} 命中所有末点不在 Q_0 的红六：终于 σ 的路径也由 σ 本身命中。因此额外实际覆盖成本 h=1，安全覆盖传播式给 n≤3b−1，p5、b25 时至多 74。

这覆盖 Q_1 非空但全被同一 through 源控制的整个类，严格强于要求 max Q 的某条路径经过 d_2。尚未证明一般 Q_1 都可如此覆盖；仍可能有 P=S\T 的源向 Q_1 提供实际红六，必须保留。

## 4. 统一红色尾扇的整类容量

**统一红扇定理。** 取 d∈D，令 T_+=T∩(d,∞)、k=|T\T_+|。若

\[
\chi(d,t,t')=R\qquad(t<t'\in T_+),
\tag{8}
\]

则

\[
\boxed{|T_+|\le c_p,\qquad n\le2b+k+c_p.}
\tag{9}
\]

**证明。** 若 T_+ 含 R_p，由式 (8) 可前接 d 得到实际 R_(p+1)，迫 d∈S，与 d∈D 矛盾。T_+ 又是 T 的子集，无 B_p，故经典容量给 |T_+|≤c_p。再用 |X\T|≤2b，得到 n≤2b+k+c_p。证毕。

代 p=5、b=25、c_5=20，得到

\[
n\le70+k.
\tag{10}
\]

因此 k≤4 的整个统一红扇接口类至多 74 点。若 min T=max S=σ，且 σ<d<min(T\{σ})，则 k=1，人口至多 71。

12 点反例中的 d=d_1 满足该红扇，所以保持此结构的放大类已经排除到上述容量。一般 r=2 不能自动假设统一红扇；第 1–2 节的安全补入机制也仍需逐项兑现实际前提。

## 5. I 空 r=3 的真正共同饱和接口仍开放

以下固定 p=5、b=25、|X|=75、I 为空，使用前稿实际三满核。记 t_0=min T，D_− 为其前方 22 个 D，D_+ 为其后方三个 D。F 为全部 t_0 坏源，F_0 为三个早坏源，f=|F|≥10。前稿已给出

\[
K=D_-\cup F_0,
\]

它有 25 点且无 R_5；对每个晚坏源和每个晚 D，K 加入该点后都会迫出从 F_0 到该点的实际 R_5。

置 Z=D∪F。Z 内全部实际 R_5 源恰为 F：每个 f∈F 有私有红五，H_R 的源身份又排除 D。全部末点恰为

\[
(F\setminus F_0)\cup D_+.
\tag{11}
\]

上述 K 增广提供每个晚坏源与晚 D 的入红五；末点不能在 D_−，否则可后接 t_0，使其源成为好源；也不能在 F_0，因为首末在这些最早坏源之间时仅有三个坏源，不足红五。两侧源、末人数均为 f。

删除全部源留下 D 的 25 点；删除全部末留下 K 的 25 点，均无 R_5。更一般地，任一实际端点二部图的 cover，其实际点像删去后无 R_5，容量至多 25；Z 有 25+f 点，所以任何二部 cover 至少 f 个顶点。由此得到实际端点图的 Hall 性质。

再令

\[
J=F\cup D_+,
\]

在 J 上以 Z 内实际 R_5 的首末点关系作为无向边。则

\[
\boxed{\alpha(J)\le3,\qquad |J|=f+3\ge13.}
\tag{12}
\]

**证明。** 若 J 中有四个互不相邻的实际端点，把它们与 D_− 的 22 点合并。该 26 点域无 R_5：否则实际源、末都落在选出的四点中，给出一条端点边，矛盾。它继承相应容量域的其他禁形，违反 25 容量。证毕。

下一项充分结构义务，是从**同一实际共同染色**证明 J 存在四点独立集，或证明 J 可至多四色着色；后者结合 |J|≥13 也给四点独立集。当前没有该结论，不能假定 J perfect、interval 或可四色着色，也不能把下面的 17 点小反例视为这个饱和 Hall 接口的反例。

## 6. 17 点四条顺次红五：完整结构反例

本节使用已机械验证的同一具体 fixture，不改变任何三元组。顺序为

\[
L_4<U_4<\{z\}<V_4<R_4,
\tag{13}
\]

对应点号 L=1..4、U=5..8、z=9、V=10..13、R=14..17。令 M=U∪{z}∪V。

### 6.1 完整染色和中央 packet

各四点块内部红。中央 M 的跨块红三元组为 UUz、UUV、zVV，蓝三元组为 UzV、UVV。

| 中央四点型 | packet |
|---|---|
| UUUU、UUUz、UUUV、zVVV、VVVV | RRRR |
| UUzV、UUVV | RRBB |
| UzVV、UVVV | BBBR |

这九种型穷尽中央四点。中央红高为 5，由 U_4+z、U_4+v、z+V_4 兑现；蓝高至多 3：含 z 的蓝链不能用两个 U 或两个 V，无 z 时两 U 加一 V 为红。

外界规则为：LLx=h(x)（x∈M），其中 h 在 U 为 R、在 z∪V 为 B；xRR=k(x)，其中 k 在 U∪{z} 为 B、在 V 为 R。Lxy、xyR 全蓝；凡同时碰 L、R 的三元组全蓝。

外界全部四点包按块重数归入下列形式：

\[
Rhhh,\quad h(x)h(y)BB,\quad BBBc,\quad cBBB,\quad
BBk(x)k(y),\quad kkkR,
\]
\[
hBBB,\quad BBBk,\quad RBBB,\quad BBBR,\quad BBBB.
\tag{14}
\]

其中 c 为相应内部三元组颜色，h 随序只从 R 变 B，k 只从 B 变 R，故所有包至多一次变色。构造为完整合法 signotope。

### 6.2 两色高度与 weak7

红高至多 5：涉及 L 的三点以上红链只能是 L 的子集加单个 U 点；涉及 R 时对偶；同时碰 L、R 的红路径至多两点。中央红高已为 5。

蓝高至多 5：每个外块至多用两点，M 至多用三点。用两个 L 时，首个 M 点必须在 z∪V，该五点块全红，所以 M 部分至多取两点；用两个 R 时对偶。若同时用两个 L 和两个 R，则 M 首点至少 z、末点至多 z，所以 M 至多一点。其余最多一 L、三 M、一 R，共五点。

weak7 的同端长度按下表覆盖：

| 实际端域 | 红长上界 | 蓝长上界 |
|---|---:|---:|
| 两端在 M；或 L→U、V→R | 5 | 3 |
| L→z/V、U/z→R、L→R | 2 | 5 |
| 同一个外块 | 4 | 2 |

各和均至多 8，故无 weak7；同时无 R_6、B_6。

四条顺次 R_5 为

\[
L_4+u_1,\quad U_4+z,\quad z+V_4,\quad v_4+R_4.
\tag{15}
\]

### 6.3 全部红五、through 与 Hall 失败

全部 R_5 恰为

\[
L_4+u_i,\quad U_4+z,\quad U_4+v_j,\quad
z+V_4,\quad v_j+R_4.
\tag{16}
\]

因此实际源为七点 {l_1,u_1,z,v_1,…,v_4}，末为十点 U_4∪{z}∪V_4∪{r_4}，through 为六点 {u_1,z}∪V_4。V_4 的全部红五都终于同一个 r_4，所以该源终图对 V_4 的 Hall 条件失败。

本例否定“四条顺次 R_5 不可能”的一般命题；仅再要求链源无 incoming B_5 也不能救回，因为任何 balanced 母体的红五源原本就有这一禁配性质。它不反驳用户所需的双极共同饱和、三早根三末端或满 25 框架。

更早的“三条顺次红五不可能”已被旧 L_4<A_5<R_4 的经典 13 点例否定；本轮不把增加链数、再按链重复收费记作进展。

### 6.4 Linux 原始证据

[17 点完整染色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/coloring.tsv>)与 [验证回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/validation.json>)记录：680 三元组、2380 packet、131054 个递增点子集、136 对实际首末点；packet、路径遗传与 weak7 违规均为 0，最长红/蓝 5/5，同端最大长度和 8，四条指定红五全部三元组为红。

原始 [每对端点最大值及见证](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/endpoint-maxima.tsv>)与全部单色路径已保存在证据目录，不重复生成或改写。

## 7. 12 点 I 非空、极端源后两个 D 的完整反例

点序为

\[
q<a<b<c<e<\sigma<d_1<d_2<t_1<t_2<t_3<t_4,
\tag{17}
\]

点号依次 1..12。记 A={a,b,c,e}、H={σ,d_1,d_2}、F={t_1,…,t_4}。默认全红，蓝恰为五族：

1. (q,σ,d_1)。
2. uhh'，其中 u∈A、h<h'∈H。
3. uht，其中 u∈A、h∈{σ,d_1}、t∈F。
4. utt'，其中 u∈A∪{d_2}、t<t'∈F。
5. (ℓ,e,x)，其中 ℓ∈{b,c}、x∈{d_1,d_2}∪F。

这与已验证的五蓝族 fixture 完全相同。

### 7.1 全部 packet 分类

删去 e 后，记 L={q,a,b,c}。全部四点块型及可能 packet 为：

| 四点型 | packet |
|---|---|
| 4L、3L+H、3L+F | RRRR |
| 2L+2H | RRBB、RRRB |
| 2L+H+F | RRRR、RRRB、RRBB |
| 2L+2F | RRRB、RRBB |
| L+3H | BRRR、BBBR |
| L+2H+F | RRRR、BRRR、BBBR、BBRR |
| L+H+2F | RRRR、RRRB、BBBR、RRBB |
| L+3F | RRRR、BBBR |
| 3H+F | RRRR |
| 2H+2F | RRRR、RRRB |
| H+3F | RRRR、BBBR |
| 4F | RRRR |

含 e 时，对 x∈{d_1,d_2}∪F，有

\[
(\chi(q,e,x),\chi(a,e,x),\chi(b,e,x),\chi(c,e,x))=(R,R,B,B),
\]

x=σ 时四项全红。含 e 的全部 packet 为：

| 四点型 | packet |
|---|---|
| 3L+e | RRRR |
| 2L+e+x | RRRR、RRRB、RRBB |
| L+e+2H | RRRB、RRBB、RBBB、BBBB |
| L+e+H+F | RRRB、RRBB、RBBB、BBBB、RRRR、BBRR |
| L+e+2F | RRRB、RRBB、BBBB |
| e+3H | BBBR |
| e+2H+F | BBBR、BBRR |
| e+H+2F | BBBR、RRBB |
| e+3F | BBBR |

所有列出的 packet 均至多一次变色；两表穷尽 495 个实际 packet 的块型，原始逐包记录亦已核验。

### 7.2 红出高、入高和实际源末

逐型红路径的出高、入高为：

| 点 | 红出高 | 红入高 |
|---|---:|---:|
| q | 6 | 1 |
| a | 5 | 2 |
| b | 4 | 3 |
| c | 3 | 4 |
| e | 3 | 5 |
| σ | 6 | 6 |
| d_1 | 5 | 5 |
| d_2 | 2 | 5 |
| t_j（j=1..4） | 5−j | 6 |

最长红路径由 (q,a,b,c,e,σ)、(q,a,b,c,d_2,t_j)、(σ,d_1,t_1,t_2,t_3,t_4) 等兑现。实际红六源末为

\[
S=\{q,\sigma\},\quad T=\{\sigma,t_1,t_2,t_3,t_4\},\quad
I=\{\sigma\},\quad D=\{a,b,c,e,d_1,d_2\}.
\tag{18}
\]

所以 min T=max S=σ，极端源后恰有两个 D；而实际红六

\[
(\sigma,d_1,t_1,t_2,t_3,t_4)
\tag{19}
\]

跳过 d_2。不能由极端源的第二点在 D 就推断其后所有 D 都被路径使用。

### 7.3 蓝高度与 weak7

q 唯一的蓝三是 (q,σ,d_1)，不可延长。蓝路径若至少三点，不能使用 a、b、c 中两个点；从 e 出发的蓝高至多三。H∪F 中蓝三仅 d_2tt'，没有蓝四。因此蓝最长为四。

红五源为 q、a、σ、d_1，它们都没有出蓝四：a 若以 e 为第二点，其桥为红；避开 e 后，剩余后三点唯一可能是 d_2tt'，又被红色 (a,d_2,t) 阻挡。其他三个源同样没有出蓝四。

σ 没有蓝三；q 唯一蓝三末点 d_1 不是任何红六末点。因此没有 R_6+B_3 或 R_5+B_4 的同端组合；又不存在 B_5，故无 weak7。最长红为六，蓝为四，母体是实际 767。

### 7.4 原始核验及不能外推的范围

[12 点完整染色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/coloring-r2.tsv>)与 [验证回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/r2-validation.json>)记录：220 三元组、495 packet、4083 递增子集、66 对实际首末点；packet、路径遗传和 weak7 违规均为 0，最长红/蓝 6/4，同端最大长度和 8。实际 S/T/I/D 与输入逐项一致，指定跳过 d_2 的红六全部三元组为红。

[逐端点最大长度及见证](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/r2-endpoint-maxima.tsv>)及全部单色路径保留在原目录。本例否定相应无条件局部加强，不是 75 点临界反例，也没有满 25 共同饱和。它同时说明：局部 r=2 分支本身不能被空泛的路径必用点论证消去；真正放大到临界的接口还受到第 1–4 节容量约束。

## 8. 未闭合目标与止损边界

本轮没有排除完整 I 空 r=3，也没有排除一般 I 非空临界 r=2。两个小反例只阻断未使用共同饱和的局部命题，不能反向当作这些临界类已存在的证据。

后续优先使用同一母体的完整共同饱和，提取可兑现的安全补入端口，并对剩余末点域证明低成本的全路径实际覆盖；继续实际 r=3 图的四点独立集问题。不得假定图的 perfect/interval/四色性质，不得因四条链存在而重复收取共享 D 点成本；紧 Hall 分量交换中新落于换入域的实际源也仍需处理。

本稿不加入未成熟的 10/14 点蓝高例或猜想串。两个已完整验证的构造足以界定当前止损点；下一成果仍需给出明确整类排除、合法实际操作或新的完整反例。

## 9. 执行账、证据与接受保证

本轮 Linux 原始验证已结束，固定在 /data/ktqiu_hdd/math_agent/tmp/n7_four_r5_chain_20261104。首次单批约 0.60 秒，科学批次 1、构造生成 1、验证例数 2、科学重试 0、solver 0、外审（含 status）0。原先一次 bounded SAT 计划在任何 solver 启动前，经主会话明确指示改为直接验证完整染色；没有 CNF/proof 或 UNSAT 主张。

验证器独立读取 TSV 和数学规格，不导入生成器、CNF 或 solver；枚举全部递增子集，保存所有单色路径，逐端点计算两色最大长度及见证。这种独立性只是原始数据核查方式，不是独立外部数学审查。取回证据时 21 项哈希绑定全部一致，见 [collection-receipt.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/collection-receipt.json>)。

本报告只做文档编排和一次文档核查，不重写或重跑任何 tmp 原始科学文件。既有全局工作上界保持 40/50/75/76，旧输入、人工接受、same-family/provisional 保证、proof/CNF/checker 绑定、assurance、runtime、运行任务与任务指针保持。

[doccheck.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/doccheck.md>)的 PASS_DOCUMENT_ONLY 仅表示冻结文字、公式、链接、编号与来源 SHA 的一致性，不能替代数学审查或人工接受。







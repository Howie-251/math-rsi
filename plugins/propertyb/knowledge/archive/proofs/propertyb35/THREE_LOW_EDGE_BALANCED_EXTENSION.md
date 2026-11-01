# 三个同边六度点的平衡补色定理

这是计算辅助自然语言证明。有限局部引理已有完整域、精确主计算及
不同计数方法的独立重放；本稿给出从原超图到最终Bool染色的连接。

## 定理

设V有25个点，H为35条互异五元边组成的超图，任意两个不同点都被某条
原边共同覆盖。设a,b,c为三个不同的六度点，且
$G=\{a,b,c,u,v\}\in H$。记
$$
D=d_H(u)+d_H(v),\qquad \alpha=\lambda_H(u,v)-1.
$$
若
$$
\boxed{D-5\alpha\le17,}
\tag{1}
$$
则存在 $\operatorname{col}:V\to\operatorname{Bool}$，使每条原边同时
含True点与False点，即H具有Property B。

特别地，若H恰有三个六度点，且它们同属一条原边，则H具有Property B。
定理不要求边临界，也不要求a,b,c是全部六度点。

## 1. 六度点给出同一20点集合的三份划分

对六度点z，点对覆盖及度数双计数给
$$
\lambda_H(z,y)\ge1\quad(y\ne z),\qquad
\sum_{y\ne z}\lambda_H(z,y)=4d_H(z)=24.
$$
共有24项，所以每项恰一；六条z星边删z后，恰好划分其余24点。

令 $S=V\setminus G$，则|S|=20。过a的其他五条原边都不能含G中的
其他点，否则相应a–y点对会被G及另一条边覆盖两次。
删a后它们因而给S的一份五个四块的划分 $\mathcal P_a$。
同理得到同一S上的 $\mathcal P_b,\mathcal P_c$。
G之外没有同时含两个a,b,c的边，所以含至少一个中心的边恰有
$1+3\cdot5=16$ 条，剩余19条原边避开a,b,c。

固定u红、v蓝，在S的
$$
N=\binom{20}{10}=184756
$$
份10红10蓝染色中均匀取一份。G已由u、v保证两色。
一名中心x无法补色，当且仅当 $\mathcal P_x$ 同时有全红块及全蓝块。
记这个冲突事件为 $B_x$。无冲突时，每名中心可分别选一个允许颜色；
除G外没有边同时涉及两名中心，因此三次补色互不耦合。

## 2. 两份划分及一个标记四集的局部引理

对同一20点集的任意两份五四块划分P、Q，令
$$
J=|B_P\cap B_Q|,\qquad A=B_P\cup B_Q.
$$
若四点集T在P、Q中均占四个不同块，称其为共同四横截集。
令 $E_T$ 为T全红事件，并定义
$$
K_{\max}(P,Q)=\max_{T\text{共同四横截}}
 |E_T\cap B_P\cap B_Q|.
$$
此最大值的集合非空：交矩阵各行各列和4，所以任意若干行的非零邻列
至少同样多（其总格量为行数的4倍，而每列容量4）。
Hall定理给五个正格的完美匹配；任取其中四格各一点就是共同四横截集。
所用准确局部结论为
$$
|B_P|=|B_Q|=16980,\qquad J\ge400,
\tag{2}
$$
$$
\boxed{J-15K_{\max}\ge324.}
\tag{3}
$$
令 $e=660-K_{\max}$，则
$$
\boxed{330\le e\le660,\quad
 |E_T\cap A|\ge e\ \text{对每个四点集T成立},\quad
 J+15e\ge10224.}
\tag{4}
$$
同样结论适用于T全蓝，因为全局红蓝互换保留A及平衡样本空间。

先说明单划分数及(4)。单划分同时具有红块与蓝块的容斥为
$$
|B_P|=20\binom{12}{6}-60\binom82+30\binom42=16980.
$$
四点T按五块的占用为1111、211、22、31、4时，
$|E_T\cap B_P|$ 分别为
$$
330,\quad752,\quad1248,\quad1596,\quad3528.
\tag{5}
$$
这些数由对非空且不交的红块集U、蓝块集W作容斥得到
（同一块不能同时指定红与蓝）：
W含T点时该项为零，否则强制红数为
$4+4|U|-\sum_{P_i\in U}|T\cap P_i|$，蓝数为4|W|，
再用二项式补足10红。
若T不是共同四横截，它在至少一份划分的占用非1111，
所以 $|E_T\cap A|\ge752$。
若是共同四横截，两份单冲突交各330，故
$$
|E_T\cap A|=660-|E_T\cap B_P\cap B_Q|
\ge660-K_{\max}.
$$
又 $0\le K_{\max}\le330$，结合(3)即得(4)。

结论 $J\ge400$ 的完整局部证明及实际核验见
[两划分证明](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/PROOF.md)。
(3)的有限域、精确计数公式及独立验算在附录给出。
这里导入的是准确有限算术结论，不是未证的全局选点假设。

## 3. 19条原边的精确概率分组

由于a、b、c与u、v的共度一已由G占用，u或v的所有G外原边均避开
a,b,c。因此19条避中心原边中：

* α条含u及v，因它们反色而恒proper；
* $k=D-2-2\alpha$ 条恰含一个u/v，各有四点在S；
* $\ell=21-D+\alpha$ 条完全落在S。

这些是实际原边的非负整数计数，且 $\alpha+k+\ell=19$。
恰含一个u/v的边单色，当且仅当其S中四点全为指定颜色，
坏样本数为 $\binom{16}{6}=8008$。
完全在S的五边全红或全蓝，坏样本数为
$2\binom{15}{5}=6006$。
三中心冲突与这些原边坏事件的原始概率和，分子为
$$
3\cdot16980+8008k+6006\ell
=161050+2002(D-5\alpha).
\tag{6}
$$
这里准确计算的是概率之和，尚未把它当作坏事件并的准确概率。

## 4. 所有事件相对同一个共同根扣交

在 $\mathcal P_a,\mathcal P_b$ 上应用第2节，令 $A=B_a\cup B_b$，
保留其实际J及e。于是 $|A|=2\cdot16980-J$。
第三中心满足
$$
|B_c\cap A|\ge|B_c\cap B_a|\ge400.
$$
每条k类原边对应的指定单色四点事件F都满足 $|F\cap A|\ge e$。
这对红、蓝两种指定颜色同时成立；同迹或相互重叠的不同原边
始终按原索引保留。

对任意事件族 $F_i$，逐点有
$$
1_{A\cup\bigcup_iF_i}\le1_A+\sum_i1_{F_i\setminus A}.
$$
故可对第三中心及每条k类原边，各扣除它与**同一个A**的交一次；
完全在S的五边仍只用union bound。所得失败样本数上界为
$$
161050+2002q-J-400-k e,\qquad
q=D-5\alpha,\quad k=q-2+3\alpha.
\tag{7}
$$
这是合法的共同根并界；不假设各事件独立，
也没有把任意多对交集相减而遗漏三重交集。

若q≤12，利用 $J\ge400,k\ge0$，(7)至多
$161050+24024-800=184274<N$。
若 $13\le q\le17$，点对覆盖给α≥0，所以k≥q−2。
由于 $2002-e>0$，(7)随q的该上界递增，最坏在q=17：
$$
\begin{aligned}
(7)&\le195084-J-400-15e\\
&=184784-(J-15K_{\max})\\
&\le184460<184756=N.
\end{aligned}
$$
严格余量为296。因此条件(1)下至少存在一份S染色，
使19条原边均proper，且三个中心都无冲突。
这里使用的是k≥q−2；没有假定k≤15，α>0时较多k类边只会改善扣除。

## 5. 最终Bool染色与恰三低共边推论

固定上述一份S染色，蓝为True、红为False，保持u为False、v为True。
对每个 $x\in\{a,b,c\}$：
若 $\mathcal P_x$ 有全红块，就给x取True；否则给x取False。
前一种情况下没有全蓝块，后一种情况下没有全红块，
因此每条非G的x星边都有两色。G由u、v保证两色，另外19条边
已经proper。这给出整个V上的Bool映射，并对每条原边提供
一个True点及一个False点，完成原命题。

若H恰有三个六度点，点对覆盖先给每点度至少六，所以其他22点度至少七。
其总度超额为
$$
\sum_{x\notin\{a,b,c\}}(d_H(x)-7)
=175-18-22\cdot7=3.
$$
若三低同边，则另外u、v的度数和D≤14+3=17，
又α≥0，必满足(1)。这证明了恰三低**共边**整支；
不将三低仅两两共边的另一几何包括在内。

## 附录：标记局部引理的完整证书及验证范围

给两划分的块编号，交矩阵 $M_{ij}=|P_i\cap Q_j|$ 为5×5非负整数矩阵，
各行各列和4。反过来每个这样的矩阵都可由实际两划分实现。
既有[完整域](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/REPRESENTATIVES.json)
按行列置换覆盖全部264轨道及其准确J；
其19834行排序终态域已由独立方法完整核对，J已逐平衡染色重放。
本次标记核验复用这个已验域，不重新生成它。

一个共同四横截集遗漏唯一一行r0和一列c0，另外四行与四列之间给
一个双射；故每矩阵至多 $5\cdot5\cdot4!=600$ 个格支持。
可实现当且仅当四个选格均非空。每格只选一个点，格内任意点标签置换
保留两划分及均匀染色空间，所以K只依赖格支持，不依赖所选标签。
任意原(P,Q,T)经行列编号运输后都落入此域。

在T全红且双冲突时，唯一可能的全蓝行／列为r0、c0，
所以 $B=P_{r0}\cup Q_{c0}$ 必须全蓝，$|B|=8-M_{r0,c0}$。
令 $\mathcal R,\mathcal C$ 为避开B的候选红行／红列，对非空子族U、W写
$$
R(U,W)=T\cup\bigcup_{P_i\in U}P_i\cup\bigcup_{Q_j\in W}Q_j.
$$
精确容斥为
$$
K(T)=\sum_{\varnothing\ne U\subseteq\mathcal R\atop
           \varnothing\ne W\subseteq\mathcal C}
(-1)^{|U|+|W|}
\binom{20-|R(U,W)|-|B|}{10-|R(U,W)|},
\tag{8}
$$
越界二项式取零。最多225项，以20位实际点掩码求并，无浮点近似。
主实现完整算264矩阵的17304个可行格支持，
[逐矩阵最大值及见证](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/RESULT.json)
及[全部支持计数](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/PATTERNS.tsv)
给全域最小 $J-15K_{\max}=324$。
等号见证为
$$
\begin{pmatrix}
0&0&1&1&2\\
1&1&0&1&1\\
1&1&1&0&1\\
1&1&1&1&0\\
1&1&1&1&0
\end{pmatrix},
\qquad J=624,\quad K_{\max}=20.
$$
J−I轨道则J=400、最大K=4，差为340。

[独立核验](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/independent/REPORT.md)
采用不同点编号、递归生成全部正格四匹配，不读取主实现支持模式；
在强制T红、B蓝后，从剩余8至12点中直接选6红，再字面判断红行、
红列，完全不使用(8)。全部17304支持、2239230个六红子集检查完毕。
[逐项比较](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/independent/COMPARISON.json)
为PASS：所有支持键、K、264个最大值及主实现见证都相同。

**17304是格支持数，不是具体点选择数。** 在264个矩阵代表上，各支持
乘四个格大小后共对应112089个带点标签四横截集；
格内标签对称证明为什么每支持计一次K已完整覆盖这些选择。
计数与覆盖的详述、源码及复现入口见
[标记局部证明](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/PROOF.md)。
单划分(5)另由
[精确条件容斥小核](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/SINGLE_MARK_CHECK.json)
逐型核对。

本稿的数值依赖仅为上述有限局部计数，已有主实现与独立确定性验算；
未作Lean形式化，也不将此条件定理记为全部25点或完整m(5)≥36结论。

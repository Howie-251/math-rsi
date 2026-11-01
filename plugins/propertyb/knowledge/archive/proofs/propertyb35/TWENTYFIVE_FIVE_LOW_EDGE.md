# 二十五点全六度原边的平衡补色证明

本稿给出从实际超图到Bool染色的计算辅助纸面证明。
所用两划分局部引理已完成完整主计算、独立逐20点染色核验及root重编重放，
具体证据见第6节。结论包括全五低原边及至少18个六度点的子支。

## 1. 定理与实际低点星

**定理。** 设V有25个点，H为35条互异五元边组成的超图，且任意两个
不同点都同属于某条原边。令
$$
L=\{z\in V:d_H(z)=6\}.
$$
若H有一条边G满足 $G\subseteq L$，则存在
$\operatorname{col}:V\to\operatorname{Bool}$，使每条原边同时含True点及False点。
因此若 $|L|\ge18$，H具有Property B。

对任意低点z及其他点y，记点对共度为 $\lambda_{zy}$。
点对覆盖给 $\lambda_{zy}\ge1$，而
$$
\sum_{y\ne z}\lambda_{zy}=4d_H(z)=24.
$$
共有24项，所以每项恰一。这同时证明：

* 任意两条过z的原边恰交于z；
* 六条过z的边删z后，把其余24点划分为六个四块；
* 任意低点对恰同属一条原边。

这些性质来自实际H，没有额外线性假设。

## 2. 两划分局部引理及完整覆盖入口

令S为任意20点集，$\mathcal P,\mathcal Q$ 为S的两份划分，每份有
五个四元块；两份划分允许相同或部分同块。均匀选10个蓝点，其余红。
令 $B_{\mathcal P}$ 表示 $\mathcal P$ 中同时有全红块及全蓝块，类似定义
$B_{\mathcal Q}$。所调用的局部引理为
$$
\boxed{|B_{\mathcal P}\cap B_{\mathcal Q}|
       \ge400,\qquad N=\binom{20}{10}=184756.}
\tag{1}
$$

其[完整证明与覆盖](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/PROOF.md)
将实际两划分送到非负整数交矩阵
$M_{ij}=|P_i\cap Q_j|$，每行每列和4；反之每个这样的矩阵都可由实际
两划分实现。行排序递归完整产生19834个终态，双字典序保留2056个，
再按全部120个列置换及行排序规范化得到264个完整轨道。
固定矩阵以110种红蓝块容斥状态的两两组合准确计数，不使用概率独立性。
[完整主结果](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/RESULT.json)
核全部264项，最小400；全部矩阵与逐项数见
[REPRESENTATIVES.json](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/REPRESENTATIVES.json)。

对任一单独划分，其冲突数恰为
$$
|B_{\mathcal P}|
=20\binom{12}{6}-60\binom82+30\binom42
=16980.
\tag{2}
$$
证明是在全红块与全蓝块的非空选择上分别作容斥。
10红10蓝下每色至多有两个全色四块，选择块数为
$(1,1),(1,2),(2,1),(2,2)$ 时系数分别20、−30、−30、30，
未强制点的补色数分别 $\binom{12}6,\binom82,\binom82,\binom42$。
因此(2)是准确计数。

## 3. 一般三低同边的实际补色门

先证明稍一般的条件门。设a,b,c为任意三个不同六度点，
$G=\{a,b,c,u,v\}$ 为原边；u,v此时不要求六度。
令 $S=V\setminus G$。过a的其他五条边不能含G的其他点，
否则与G重复覆盖某个a–y点对。因此它们删a后是S的五个四块划分
$\mathcal P_a$。同理得 $\mathcal P_b,\mathcal P_c$，都定义在
**同一个实际20点S上**。

过a、b、c的边除G外彼此不同，因为两个低点共度一，故这部分原边
恰有 $1+3\cdot5=16$ 条；剩余19条原边避开a,b,c。
令u红、v蓝，并在S的N份10蓝10红染色中均匀选择。
G恒proper。若某中心的五块未同时出现全红块与全蓝块，就能给该中心
补一个颜色，使它的五条其他星边全部proper。
这三次补色互不冲突，因为没有G之外同时含两个中心的边。

写 $B_a,B_b,B_c$ 为三个中心的冲突事件。任取其中两份实际划分，
由(1)及(2)，不需任何独立性，即有
$$
\begin{aligned}
\Pr(B_a\cup B_b\cup B_c)
&\le \Pr(B_a)+\Pr(B_b)-\Pr(B_a\cap B_b)+\Pr(B_c)\\
&\le\frac{3\cdot16980-400}{N}.
\end{aligned}
\tag{3}
$$
只减同一对事件的交集一次，是合法的union bound；
没有把三对交集重复扣除，也没有忽略三重交集的符号。

设
$$
D=d_H(u)+d_H(v),\qquad \alpha=\lambda_{uv}-1.
$$
u或v的G外原边均避开a,b,c，因低点与u、v的共度一已由G占用。
因此19条避abc边中：

* α条含u、v，因它们反色而恒proper；
* $D-2-2\alpha$ 条恰含其中一个；
* $21-D+\alpha$ 条两者都不含。

恰含一个的边有四点落在S，单色概率为
$$
p_1=\frac{\binom{16}{6}}{N}
   =\frac{\binom{10}{4}}{\binom{20}{4}}
   =\frac{8008}{N}.
$$
两者都不含的边完全在S，单色概率为
$$
p_0=\frac{2\binom{15}{5}}{N}
   =\frac{2\binom{10}{5}}{\binom{20}{5}}
   =\frac{6006}{N}.
$$
固定同一份S染色，对19条实际边及(3)作union bound，得到
$$
\begin{aligned}
\Pr(\text{有避abc单色边或有中心无法补色})
&\le\frac{3\cdot16980-400+
          8008(D-2-2\alpha)+6006(21-D+\alpha)}{N}\\
&=\frac{160650+2002(D-5\alpha)}{184756}.
\end{aligned}
\tag{4}
$$
故已证条件门
$$
\boxed{D-5\alpha\le12\quad\Longrightarrow\quad H\text{具有Property B}.}
\tag{5}
$$
这是任意含这三个实际六度点同边的H的门，不要求全图恰有三个低点。
没有声称所有三低同边输入都自动满足(5)。

## 4. 全五低原边闭合及实际Bool染色

现在G的五点都六度，任取其中三点作a,b,c，另外两点作u,v。
第1节给 $\lambda_{uv}=1$，所以
$$
D=12,\qquad\alpha=0.
$$
式(4)的失败分子为
$$
3\cdot16980-400+10\cdot8008+9\cdot6006
=184674<184756,
$$
余量为82。故至少存在一份S的10蓝10红染色，同时使19条避abc原边
proper，并使三个中心都无冲突。

固定这样一份染色，令蓝为True、红为False。
保持u为False、v为True。对每个 $x\in\{a,b,c\}$：
若它的划分有全红块，就给x取True；否则若有全蓝块，就给x取False；
若两种全色块都没有，则任取False。
冲突已被排除，所以第一种情形没有全蓝块，第二种情形没有全红块，
第三种情形每块自身已有两色。因此每条非G的x星边都含True及False。
G由u、v保证两色，其他19条原边早已proper。
这定义了整个V上的 $\operatorname{col}:V\to\operatorname{Bool}$，
且对每条 $e\in H$ 都存在 $p,q\in e$ 使
$\operatorname{col}(p)=\mathrm{True}$、
$\operatorname{col}(q)=\mathrm{False}$，即原始Property B结论。

## 5. 至少18个六度点必选到全五低原边

令r=|L|≥18，对原边e写 $\ell(e)=|e\cap L|$。
低点各度六、低点对共度一给同一H上的准确双计数
$$
\sum_{e\in H}\ell(e)=6r,\qquad
\sum_{e\in H}\binom{\ell(e)}2=\binom r2.
$$
若没有全五低原边，则 $\ell(e)\le4$，逐边有
$\binom{\ell(e)}2\le3\ell(e)/2$，故
$$
\binom r2\le\frac32\,6r=9r,\qquad r\le19,
$$
所以r≥20时已矛盾。余下r=18、19可保留逐低点的唯一覆盖信息加强。
对每个低点z，其六条入射边满足
$$
\sum_{e\ni z}(\ell(e)-1)=r-1,
\tag{6}
$$
因为其他低点各与z共度一。若仍无全五低原边，每项至多3。

**r=19。** 式(6)的六项和18，故全等于3，所有含低点原边均有ℓ=4。
于是 $4n_4=\sum_e\ell(e)=6\cdot19=114$，不被4整除，矛盾。

**r=18。** 六项和17、各至多3，故恰一项为2、其余五项为3，
即每个低点恰在一条ℓ=3边及五条ℓ=4边。
因此 $3n_3=18$、$3n_3+4n_4=108$，得 $4n_4=90$，矛盾。

三种范围均迫同一个原H有全五低原边，再由第4节得Bool染色。
这里没有使用度谱枚举，r≥20也无需按其具体值分支。

## 6. 验证状态与精确依赖

本证明只导入第2节的有限局部交叠引理，其余均为原H的解析归约与计数。
该局部引理已通过三层实际核验：

* 主实现完整生成19834个行排序终态及264个轨道，以整数容斥逐项计数，
  最小交叠400。
* [独立实现报告](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/independent/REPORT.md)
  从全部19834终态直接规范化，独立核对完整轨道域；逐20点平衡红集
  直接判断事件，重放全部48,775,584个代表／染色对，不使用主实现容斥。
  [逐项比较](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/independent/COMPARISON.json)
  为PASS，全部264个键、计数及直方图一致。
* [Root重编重放](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/root_replay/ROOT_REPLAY.json)
  编译并实际执行独立源码，19834终态、264轨道及每项计数再次一致，PASS。

单中心16980、8008/6006及一个J−I原型的400另有
[小核与解析报告](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/REPORT.md)。
Gemini 4 Argon (High)/high在同一线程的两轮有效SUCCESS中，
静态全文／手算认可三低条件门、全五低边及r≥18结论；
局部有限算术作为声明进口，没有由Gemini执行程序。
原始回复、准确范围与处置见
[Gemini审阅记录](../../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_RECONCILIATION.md)。
Grok对本范围的审阅仍在途，本记录不称双模型通过。
本稿未作Lean形式化；r≤17、一般25点及完整m(5)≥36不在本次结论内。

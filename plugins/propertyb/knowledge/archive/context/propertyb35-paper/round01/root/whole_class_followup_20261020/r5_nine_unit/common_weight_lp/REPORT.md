# r5三K5例外：共享W与完整实际连接

2026-10-21最终补充：**完整三K5选锁例外已有纸面候选闭合**，主入口[K5_EXCEPTION_COMPLETE.md](K5_EXCEPTION_COMPLETE.md)。新增五锁明确布局使每个w3点对的共同低中心数≤1，六种Y权图由均匀解析定理及五份精确有理证书全部覆盖；无SciPy独立核PASS。r5九锁主域仍未闭，不称r5或全25完成。新链尚待root／跨家族scope审阅。

以下保留2026-10-20首轮记录：初始共享原边LP在均匀Y权二时最优135，单纯连续矩不足；加入真实低星约束分析其小松弛面后，获得[完整解析均匀Y定理](UNIFORM_Y_THEOREM.md)，证明存在低点W≤25。

## 实际输入与精确公式

高点分A/B/C三个七度K5及Y五八度，低点五名；每条原边型为(ℓ,a,b,c,Ysubset)，ℓ=0/1/2，和为五。全部512型，按一条真实原边的类型计非负重数x。原H必映入该域，反向实现不保证。

50条等式包括：n0/n1/n2=15/10/10；三个七度组各总度35；每个Y点度八；各七度组内部pair关联20；组间pair关联25；每组与每个Y点关联五；每个Y对关联三；低–各七度组关联25；低–每个Y点关联五。

均匀Y超额w2时精确目标是

\[
S=\sum_{z\in L}W_z
=\sum_{types}\ell\left[\binom a2+\binom b2+\binom c2+2\binom{|Ysubset|}{2}\right]x.
\]

二低原边在这里确实支付两次，没有旧q≤λ错误。未加组合容量上界或其他17权图。

## 实际执行

初始LP0.021593 CPU秒；保存40个正的有理权重，完整50条等式精确相等、目标135。有理dual也逐512类型核非负松弛、目标135，因此135是此必要连续松弛的精确最优值，不只是浮点结果。另有一个八轨道对称有理135见证，见FACE_RESULT。

独立短dual及slack核后的一次整数聚合pilot，加入四类零松弛二低边各至多二、S≥130条件，求解器报不可行；CPU1.897665。这个状态本身没有精确整数不可行证书，原数据如实保留，未把它当成H不存在证明。

随后解析补齐了实际义务：S=135−总gap；S≥130迫四类零gap二低边各两条及另两条gap2/3边；十五条纯高边都含1/2名Y。共同Y矩迫一低边Y对关联≥15，而五个实际低点的两私有四块只容≤10，矛盾。完整逐步证明与宏星进口在UNIFORM_Y_THEOREM，无需程序验不可行。

## 完整slack，而非偶性假设

令j=|Ysubset|、U=C(a,2)+C(b,2)+C(c,2)。逐边gap是：ℓ0为U+j(j−2)，ℓ1恒零，ℓ2为3−U−j(j−2)。所有结构轨道的准确值保存在[FACE_RESULT.json](FACE_RESULT.json)。尤其gap并不全偶：

|ℓ|j|七度组分布（允许排列）|gap|
|---:|---:|---|---:|
|0|0|500/410/320/311/221|10/6/4/3/2|
|0|1|400/310/220/211|5/2/1/0|
|0|2|300/210/111|3/1/0|
|0|3|200/110|4/3|
|0|4/5|100/000|8/15|
|1|任意|全部合法类型|0|
|2|0|300/210/111|0/2/3|
|2|1|200/110|3/4|
|2|2/3|100/000|3/0|

因此S≥130面包含总gap4与5，不能只排偶gap4面。正文统一处理了两者。

## 附加四个真实三锁profile

按root新指令，另只核一个六度z、两八度x/y，λzx=λzy=1，λxy=c∈{4,5}，inclusive triple t∈{0,1}的全部四profile。原度方程恢复所有八个迹，普通ABC小DP只用于发现一组具体位置；所有quota下界主动置零，最终位置由BareLayout和独立组合行计数相等核对。

统一位置(z,x,y)=(13,11,25)。c4/t0与t1分别157925/149226、7501/7106，均未过；c5/t0与t1都strict（完整数值在[LOW_EIGHT_PAIR_RESULT.json](LOW_EIGHT_PAIR_RESULT.json)），其中t1为24680/24871。四profile总0.068196 CPU秒。非strict不叫实际H反例；没有自动加第二六度锁。

结合[先前两八度原门](../K5_EXCEPTION_GATE.md)对c6/7/8严格，这个三锁阶段能从实际非B例外排c≥5，故Y内w≤3。当时仍允许λ4/w3，不能由行和八强迫均匀w2；以下后续小门补齐了这个缺口。

## 后续四／五锁与全部非均匀权图

[完整四锁七型及两个唯一五锁profile](two_low_gate/REPORT.md)用普通ABC、具体布局及独立25行重放得到：λY4的共同边不能含两低；若共同边覆盖至少两低，则可取两名共同低点加一名不共同低点，五锁布局给4116/4199<1。因此实际非B的每个w3点对有q_xy≤1，q为真正按低迹大小计费的共同低中心数。

Y的每行w和八、0≤w≤3，完整148带标签图／六个S5轨道；一均匀型已有解析定理，另五型的同一共享原边矩加q约束得到三个有理上界1477/12、740/7、171/2（均<130），两份右端−1/2的Farkas证书。不是依据浮点不可行状态。

生成器[NONUNIFORM_CHECK.py](NONUNIFORM_CHECK.py)/[NONUNIFORM_RESULT.json](NONUNIFORM_RESULT.json)保存每份全部有理乘子。独立[VERIFY_NONUNIFORM.py](VERIFY_NONUNIFORM.py)不导入SciPy或生产者矩阵，另生成148／6域，按实际计数定义解码全部证书，逐5×512类型精确核非负系数及右端，[回执PASS](VERIFY_NONUNIFORM_RESULT.json)，CPU0.285639。完整actualcaller、重标号与宏星结论见最终主入口。

证据：[CHECK.py](CHECK.py)/[RESULT.json](RESULT.json)、[FACE_CHECK.py](FACE_CHECK.py)/[FACE_RESULT.json](FACE_RESULT.json)、[LOW_EIGHT_PAIR_CHECK.py](LOW_EIGHT_PAIR_CHECK.py)/[LOW_EIGHT_PAIR_RESULT.json](LOW_EIGHT_PAIR_RESULT.json)。没有原H搜索、九锁全扫、导航或wiki修改。数学与程序审阅为same-family/provisional，新条件定理尚待root及跨家族scope验收。

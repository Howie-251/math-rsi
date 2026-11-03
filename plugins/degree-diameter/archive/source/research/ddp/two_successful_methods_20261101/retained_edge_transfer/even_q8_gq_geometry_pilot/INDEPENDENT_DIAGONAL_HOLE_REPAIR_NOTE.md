# 独立结论：omit至多五个diagonal clones不能用净增一点批次修复

**预测在指定diagonal-hole模型内成立。** 下列推导覆盖任意diagonal子集I，有限实验只取每case一个b5子集作对照，未把单一子集外推为一般证明。唯一实际诊断1.594204674 CPU秒／15秒预算，无field／旧GQ projection重验、大图、BFS、Lean或solver。

源H为已接受q8 filledsource，C=O×spread，D为diagonal centers。每center原拟一copy，但省略I⊂D的b个clone；cap仍Δ=δ+1。只加入t=b+1个可任意互连的helpers，不改已有边，目标比完整one-copy多一点。

## 1. 新的自由点与没有遗漏的clone捷径

原完整中心邻域互不交且union为H\D。省略x_d（d∈I）以后，旧自由点恰为D与各N(d)，这些集合互不交，每点都只剩一个degree。其他旧点仍饱和；现有clones也各剩一个degree。

N(d)中的每个旧pin只邻接C中的那个d。因此它不邻接任何剩余clone：唯一能使用它的clone恰已省略。D本来也不邻接任何clone。故计算一个旧freepin到目标的≤2路线时，不会漏掉经现有clone的新二步路线。若路径经新helper，最后一条边不能接下文仍饱和的目标center。

## 2. 任意I的outside目标：每hole恰好一个旧pin

用σ(i)表示o_i的真实spreadowner，取i∉I、j∉σ(I)、j≠σ(i)的目标c=(o_i,S_j)。目标数为(R−b)(R−b−1)。固定hole d_h=(o_h,S_σ(h))。

其oldpair pins为v=(p,L)，满足p∈S_σ(h)、o_h∈L，排除d_h自身。v与c没有直接边。一个共同oldpair邻居w=(q,M)恰要求

\[q\in L\cap S_j,\qquad p,o_i\in M.\]

因为o_i不在hole的spreadline，广义四边形投影唯一确定p=p*（o_i在S_σ(h)上的投影）。又因o_h不在S_j，唯一确定L=L*（过o_h及其S_j投影q*的线）。所以唯一可用pin为(p*,L*)，共同邻居为(q*,M*)，其中M*是o_i到p*的connector线。

o_i、o_h是不同ovoid点，不能共线，故p*≠o_h。S_j与S_σ(h)不同且不交，故L*≠S_σ(h)，p*不在L*。得到的pin不是被删掉的d_h，也不是flag。路线的两条边不是loop：q*与p*处于不同spreadline；q*≠o_i因为目标off-diagonal。于是确有一个genuine二步source路线，且没有其他oldpair pin。

Freed fill f_σ(h)若两步到c，必须有一个flag，其point同时位于S_σ(h)和S_j，因spread不交而不可能。目标c不是flag，也不直接邻fill。所有旧D点到off-diagonal c原本无1／2步路线。不同holes的邻域互不交，故每个outside目标恰有b个不同的旧freepins在两步内，每hole一个。

这一步使用任意I、fullovoid和spread的通用唯一性，没有假设选定holes是对称对象，也没有把σ当恒等置换。

## 3. 对任意helper内部图的计数

每个上述旧freepin只有一个spare degree，最多分给一个helper。它只能帮助直接pin它的那个helper到c：增加一条内部helper边后，剩余长度不够，而且freepin根本不直接邻outside c。因此t=b+1个helper中，每个outside目标至少留下一个helper-target缺口。

再看现有clone x_e。其唯一owner可以借共享N(e)在三步到base e；若e是off-diagonal，还可以用x_e到mate T(e)的旧边，为owner及其内部邻helpers提供路线。对其他center无路线，因为不同中心N不交、目标饱和。故一个clone pin最多填补

\[1+(\deg_B(\operatorname{owner}(e))+1)\le t+1\]

个helper-target缺口。Diagonal clones对本目标集没有额外收益，忽略这一点只使上界更宽松。一个clone只有一个spare slot，不能分给多个helpers。

即使完全忽略旧pin和内部helper边消耗的degree，总clone-pin edges也至多tΔ。所有outside目标至少各缺一对，因而必要条件是

\[(R-b)(R-b-1)\le t(t+1)\Delta=(b+1)(b+2)\Delta.\]

分类没有漏掉多helper链：两条内部helper边后不能直接接饱和c；一条内部边加旧freepin也不能接c；一条内部边加clone的mate路线已计入t+1。经现有clone绕行的free-oldpin路线已由第1节排除。

## 4. 一次b5实际小表

两case均只选literal ovoid indices I=[0,1,2,3,4]，其实际σ(I)是**[0,8,38,46,50]**，不是前五列。读取既有完整projection CSV中所需的600／590行作p*、L*预测，不重做projection验证；从已接受Inc枚举每个freedoldpin的实际二步路线。

|实测|balanced|Payne|
|---|---:|---:|
|outside目标|3540|3422|
|oldpair pin候选检查|1416000|1351690|
|实际正路线pins|17700|17110|
|每目标／每hole|5／1|5／1|
|freed fill／D捷径|0／0|0／0|

所有positive pins与继承projection给出的坐标完全一致，且五pins各异。Freedpins的唯一C-owner均为对应省略diagonal，排除remaining-clone捷径。D路线使用已接受selected matrices对当前targets作lookup，不读旧source边表。数据保存为两个B5_ROUTE_PINS.tsv、B5_TARGETS.csv及RESULT.json。

## 5. 结论及范围

|b|balanced LHS／RHS|Payne LHS／RHS|
|---:|---:|---:|
|1|4032／492|3906／486|
|2|3906／984|3782／972|
|3|3782／1640|3660／1620|
|4|3660／2460|3540／2430|
|5|3540／3444|3422／3402|

两case在b1..5均违反必要条件，因此任意这样的diagonal子集都不能修出净增一点；最接近的Payne b5仍差20个必需缺口覆盖。单一选定子集的实测支持了结构预测，但普遍结论来自第2、3节的证明。

这个限制是diagonal holes、每剩余center一copy、capδ+1、t=b+1、旧边不动的模型。Off-diagonal holes可能释放旧off-diagonal center及新的直接路线，不能按同一计数排除；k≥2、不同code、改旧边或提高cap也不在结论内。本轮没有运行b6，也不因粗界未排除就自动续算。

生成策略上的改变是：不能把少量diagonal omissions当成同cap批次修补的有效余度来源；每个目标每hole只给一个不能跨helper传播的旧pin，而不是一般可复用的连接自由度。应停止本模型b≤5的repair搜索，不把它扩大为整个A线无望。旧单helper／jointbatch文档和根状态未修改。

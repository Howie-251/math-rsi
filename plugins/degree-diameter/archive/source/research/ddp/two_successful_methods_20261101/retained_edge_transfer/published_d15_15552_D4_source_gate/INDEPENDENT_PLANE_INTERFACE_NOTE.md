# 独立纸面攻击：实际15552源的27点平面接口

2026-11-01。**所声明的局部injectivity与disjoint-T充分接口成立，但必须补上输出噪声与像空间分离这一前提。实际表的Q_v规范化已给出该前提，无需重跑rank。** 这份note只支持当前固定源、固定W及控制器目标不交规则的条件数学接口；不是新图验收、packing最大性、全点级排除、形式化或外审。

我只读了本gate的NOTE／CONTROL_PACKING_PRED、旧实际affine relation certificate／generator、表中实际坐标约定和首个控制层的五种literal关系，以及旧kernel profile。没有运行generator、局部27-code、packing、旧rank／field／77760行证书、图或BFS／Lean／solver／query／paidreview；没有修改gq或root文件、source17、Wiki、专家稿或冻结包。

## 实际输入及需要区分的两个B

本题源是15552点、116316边、192个81点fiber的固定简单无向图。既有source profile给degree14:648、degree15:14904；它不是15regular。旧`affine_relation_recovery/RESULT.json`已实际逐行绑定960个有向controller arc、77760个完整三点rowsets到该源的loop-completed关系，本note继承而不重验。D≤4沿用该固定公开源的结果，affine拟合证书本身不独立证明直径。

准确旧目录是`research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/`，主要文件为`source15552_AFFINE_RELATIONS.json`、`ANALYSIS_AFFINE_CERTIFICATE.md`、`RESULT.json`和`generator.py`。其全局标签为81*a+sum_i x_i*3^i，所有坐标运算在F3。

旧分析先将输出按非零方向v作商：取pivot r满足v_r=1，Q_v(y)记录y_k-v_k*y_r（k≠r）。这个商坐标矩阵是3×4。实际generator使用的**4×4 B**是将商输出嵌回pivot坐标为0的代表后得到的矩阵，关系为

    y = Bx + c + t v,  t∈F3.

因此不能把“商矩阵rank3”误当成“4×4 B可逆”。需要的是保存的rank3／一维input kernel及其与W的横截关系。五种实际literal(B,v,c)在各controller仅重排，故在controller0识别的五种输入kernel适用于整个指定表；这依赖当前表身份，而不是从15552因式分解猜出affine结构。

## kernel横截单独不够；实际pivot结构补齐关键一步

若W横截ker(B)，仅凭这一点，两个邻域线相交仍只能推出

    B(x-x') = (t'-t)v,

不能直接推出x-x'∈ker(B)。当v∈im(B)时，非零噪声差可以与中心差互相抵消。例如B=diag(1,0,1,1)、W={x1=0}、v=e0，W虽横截ker(B)=span(e1)，但中心0与e0产生同一条输出线。这是纸面说明缺失假设的反例，不是对实际源的实验或反例。

对**实际规范化B**，pivot整行是0，所以im(B)⊆{z:z_r=0}；而v_r=1。若λv∈im(B)，取第r坐标即得λ=0，故

    im(B) ∩ span(v) = {0}.

也可直接在两个相等输出的第r坐标上看：c相同并相消，得到t=t'；继而B(x-x')=0。这个论证不要求c为零，即使换用同一关系的另一仿射代表，常数项仍相消。本题实际首五种关系确是这种pivot-zero／normalized-v表示；旧Q_v证书说明该表示来自完整relation，而不是仅匹配basis的拟合。

另一条可用的继承理由是：该固定loop-completed无向关系在每个target点都有来自对应source fiber的三个reverse neighbors，因此im(B)+span(v)=F3^4；再结合继承的rankB=3可知v不在im(B)。但“无向”四字本身不够，还需每个target行向反向source fiber完整三点这一实际分区／rowset前提。这里优先使用更直接的pivot坐标论证，既不重算augmented rank，也不将普通simple图的degree14误当成reverse三点不完整的反例。

## W={x1=0}确实给当前每个arc的27条互斥邻域线

旧profile的五个一维input-kernel代表为

    (1,2,1,0), (1,1,1,1), (1,2,1,2),
    (1,2,2,0), (0,1,0,1).

坐标index1（第二坐标）均非零。因此W与每条kernel line的交只有0。若x,x'∈W有共同完成邻点，上一节先得t=t'，再得x-x'∈ker(B)∩W={0}，故x=x'。又因v非零，同一x的三个t输出互异。于是W×F3到一个目标fiber的81个输出是单射，也就是双射；这是一条维数／计数后果，不是新增rank计算。

同一controller的五个to值在真实table中互不相同，因此不同arc落在不同fiber；不能仅由“有五种B”推断这一点，但旧五目标分区及实际T(0)=[0,11,59,79,180]已提供它。故同一W的27个完成邻域互不交。原simple邻域是完成邻域的子集，删virtual-self后仍互不交。

## virtual-self必须在源中心处删除，不能随clone重新解释

恢复简单源时，只有输出的**完整全局标签等于输入源中心标签**才删除。相同local offset位于另一controller时是真边；self-controller arc里不同local offset也是真边。不能删掉整个self-controller关系，也不能把T(a)中的a直接扔掉后当ordinary open-neighborhood packing使用。

复制时必须先取源中心c的真实simple开邻域N_S(c)，再将该集合冻结给新clone。特别是：原virtual-self输出c已经从N_S(c)删除；不能因为新clone的标签不同于c，就将那一项重新加为clone--c边。后一种做法变成了复制loop-completed／闭邻域的另一规则，既不符合本次声明，也会改变pin负载和degree计数。

这样处理后，degree14中心的clone有14条边，degree15中心的clone有15条边。原648个degree14点在cap16有2个spare，14904个degree15点有1个spare；当前load≤1只是保守地每点用一个，不是说所有旧点本来只有一个余度。

删除virtual-self只减少各个完成邻域，不会凭空制造共用pin。它会使块的实际总pin数少于27*15，具体少多少取决于本块哪些中心原有virtual-self，不能预设每块都是405pin或把所有新点当degree15。

## disjoint-T拼块、D4真Walk及前缀

用T(a)表示完成关系中from=a的全部五个actual to标签，包括实际self-membership。每个中心的真实simple邻域都落在这些fiber里。若选出的controller满足T(a)两两不交，则不同所选层的全部真实pin也必不相交；结合层内27-code得到全体load≤1。

这里**只证明并使用disjoint-T的充分性**，不自动宣称它是任意合法中心集合的必要条件。尤其不能把控制器门的负结果外推为任意point-level／partial-plane／不同center set不可行，也不能排除利用degree14点load2的规则。无论这一次packing返回FOUND、完整负结果或UNKNOWN，都应保留此范围。第一张31集合也只证明threshold存在，不是最大packing的证明。

若有31个有效T，则中心数为31*27=837，条件阶数为15552+837=16389；这并不等于已经产出合法图。源边数116316须全部保留，新边数为各837个中心真实degree14／15之和；不可直接当837*15。旧点degree最多15+1=16，新点degree最多15，且源最小degree14保证非孤立。

对D≤4与每个前缀：旧旧点对保留源Walk。新x_c到旧v≠c，用源c→v最短路替换首边；到自己的c用任一共同旧邻点走两步。两新点对应源中心距离2、3或4时替换两端；若中心相邻，用x_c--d--c--x_d三步。所有内部点都是原15552源中的点，不依赖将来加入的clone，且3≤4。因此generic fullN Walk桥在本非regular源和D4上适用，既不需中心独立，也不需原源所有点degree15。每个完整clone前缀的旧负载仍≤1。

## 处置

当前实际表的规范化已补齐v与im(B)分离，未发现阻止固定27-plane／disjoint-T门的纸面漏洞。更准确的局部证明应先用pivot坐标消掉noise，再用input-kernel横截，不能省略前一步。本note不重复gq的27行局部字面比对或192点packing，也不将其回执当作本人的独立实验。

后续若root选择threshold31实例，还需其完整simple源／候选绑定、实际全pin负载与degree、source-D4来源及新的公开比较和独立图级验收。当前纸面接口不把16389计作图、参数、method或Lean成果。root、gq、Wiki、source17、专家与冻结文件均未修改；本任务停止，不扩field、plane或packing规则。

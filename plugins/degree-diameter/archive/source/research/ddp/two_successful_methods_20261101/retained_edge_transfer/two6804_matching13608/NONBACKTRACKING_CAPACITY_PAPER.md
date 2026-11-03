# 24phase equitable quotient：非回退容量的26/38常数

状态：纯paper公式确认，不计算ordinary π的实际NB矩阵，不读/验证source、field或BFS，不运行solver/Lean/外审。root已保存ordinary容量π及实际min573，这不是实际13608图；本paper不预判该π能否通过下面的新门。

## 1. equitable quotient为何足以给每root精确NB计数

设实际两copy图X是simple14regular：每copy为13regular旧源，新增perfect matching一条。wholephase排列π使24个cells（copy×12phase）构成equitable partition，每个cell567点。按row-source convention，其weighted邻接为

    R = [[Q,P], [P^T,Q]]， P=Pπ。

每个实际顶点到每cell的邻点数只取决于自己的cell，因此固定root的长度k普通walk按终cell聚合恰为R^k的对应行。无需相位内bijection保fibre几何、是affine或是源automorphism。

对任意simple d-regular图，按实际vertices计非立即回退walk的矩阵满足

    B0=I，B1=A，B2=A²−dI，
    Bk=A B(k−1)−(d−1)B(k−2)（k≥3）。

起始B2减d而后续减d−1，不能从第一步就统一减13。d=14时展开为

    B2=A²−14I，
    B3=A³−27A，
    B4=A⁴−40A²+182I。

聚合ordinary powers后，同一多项式作用于R即给**每个实际root到每cell的精确NBwalk数**。虽然quotient不是simple graph，不能把R当一张24点simple图直接套degree14论证；这里先在真实simple14regular X上证明多项式，再利用equitable聚合，故没有该漏洞。root本身贡献I时只落其所属cell，聚合与减项一致。

## 2. cross block展开

令

    S=QP+PQ，
    T2=Q²P+QPQ+PQ²，
    T3=Q³P+Q²PQ+QPQ²+PQ³。

P是permutation，所以PP^T=P^TP=I；两copy旧Q相同。于是

    R_cross=P，
    (R²)_cross=S，
    (R³)_cross=T2+P，
    (R⁴)_cross=T3+2S。

R³额外P对应三次连续cross；R⁴的三个cross/一个old的四个位置分别化为QP、PQ、QP、PQ，合2S。这里没有假设P与Q交换。

代回NB多项式（I的cross block为零）：

    (B1)_cross=P，
    (B2)_cross=S，
    (B3)_cross=T2−26P，
    (B4)_cross=T3−38S。

先前ordinary一次cross矩阵C=P+S+T2+T3，故

    N_cross(≤4) = C−26P−38(QP+PQ)。

**26与38均正确**：B3=R³−27R中，R³的三cross +P与−27P合成−26P；−40R²与R⁴的+2S合成−38S。不能在ordinary一次cross的C上直接减27P或40S。

也可在旧13regular图的one-cross分段中解释：旧NB2为Q²−13I，旧NB3为Q³−25Q。length3一次cross有两个“2旧步在同侧”的位置，各删13P，总26P；length4两个“3旧步同侧”各删25，另两个2+1分段各删13，QP/PQ每侧各合38。这只解释同一公式，不新增数值检验。

## 3. rowtotal与必要性

Q行和13，P行和1，S行和26。root已有ordinary rowtotal9322，因此

    NBcross rowtotal=9322−26−38·26=8308。

以上是显示代数恒等式，不是本paper执行实际矩阵。NB仍可能包含长环重复vertex或多个walk落同一target；只有立即回退被消去。因此D≤4仍要求全部144项N[i,j]≥567，但该必要门不证明distinct567points可达。最短路必NB，所以用NB计数作上界不会漏掉实际shortest route。

任意≤4跨copy NBwalk也只能有一次cross：三cross加至多一old必出现相邻两cross，而perfect matching的相邻cross即回退。这与上面的cross block消项相符，未遗漏三cross的合法NB收益。

## 4. 新模型范围与沿用归一化

N仍对P线性，可用同一144binary permutation域，但容量行改为该精确NB表达式。它是由实际反馈驱动的更强约束，不是原ordinary模型加时/换seed。普通π min573是否过新门，必须读root实际NB整数结果，不能从573自动判通过。

输出phase平移T_k与Q可交换，所以N(P T_k)=N(P)T_k；前一paper的π(0)=0容量归一化仍不丢解。Q对称与a/b求和对称使N(P^T)=N(P)^T，reverse方向无需再强制π自逆或加另一套不同域。

若新门feasible，只说明phase NB容量，不是normal/fibre compatibility或实际14/D4图。若必要模型被排，只排固定源上wholephase deterministicπ的perfect-matching族，不能排把同一phase的不同points送到多个output phases的匹配。时限无结论保持UNKNOWN，无secondwindow；normal/fibre下一阶段不在本批。

本paper完成即停，0actualgraph/parameter/Lean/record计数。

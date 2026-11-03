# 任意perfect matching的点覆盖上界：13个最小交集

最新状态：实际全source R2/R3数据支持**任意point perfect matching全族NO**。这里只读一次 `OVERLAP_RESULT.json`、`overlap_gate.cpp`及 `OVERLAP_SHELL_PROFILES.tsv` 摘要核对实现，不运行DP、球交集、排序、source/field/BFS验证、solver或Lean。先前统一profile前提已被actual反驳，以下保留其历史并使用实际maxima纠正；不需要Aut代表或matching对称性。

## 1. 不再限制phase π的exact cross union

两份同一simple13regular源G（6804点），仅加一个任意perfect matching。把copy0→copy1的bijection记为M，不要求phase-preserving、affine、group-equivariant或源automorphism。

前文“一次cross”论证仍成立：≤4跨copy路线若有3cross，至多1条旧边，必有相邻matching边沿同一边回退，可消去。因此从任一copy0 root u到copy1的闭R4点集精确是

    U(u)=union_(a=0..3) union_(x∈S_a^G(u)) B_(3−a)^G(Mx)。

这里按prefix的**最短距离**分层：任何一次cross路线的cross旧端点x都有d_G(u,x)≤其prefix步数，改用最短prefix只增加可用suffix预算；反向该最短prefix、cross及球内suffix直接给≤4真Walk。故上述不是只列部分路线的充分条件，而是exact target union。

## 2. 旧统一profile反驳与实际安全总界6984

先前继承的“每root sphere profile均为(1,13,138,1400,5252)”断言不正确。该profile是实际root0的一行，不能当全source上界；实际TSV root1给B2=154/B3=1586，root2给B2=154/B3=1588，直接反驳统一断言。旧推算

    1552+13·152+138·14+1400=6860

仅是基于错误统一前提的历史预测，不用于当前No证明。正确方法无需uniform profile，统一使用

    Umax=B3max+13·B2max+S2max·B1max+S3max。

root当前已将R2和R3都扩展到**全部6804个source roots**，实际maxima为

    B2max=154，S2max=140，B3max=1588，S3max=1434，B1=14。

因此安全总界是

    Umax=1588+13·154+140·14+1434=6984。

这些maxima可来自不同roots，分别取最大只会放宽上界，不需要它们同时在一个root实现。source13regular保证a=1球族恰有13个；若换非regular源需改变“13最小项”论证，不在当前scope。新的数据是本路线support DP，不是又做sourceD4有效性BFS。

## 3. 扣除与A0重叠不会多扣

暂时忽略后面138个/1400个球的额外交集，对A0及13个Ai有

    |A0 ∪ A1 ∪...∪ A13| ≤ |A0|+sum_i |Ai\A0|
                          = |A0|+sum_i|Ai|−sum_i|A0∩Ai|。

同一个target可能同时落A0与多个Ai，不构成过度扣除：它在原size sum中本来被count 1+k次，扣k次后正好留下A0的1次。A0之外的Ai之间碰撞仍被重复计数，所以只会使上界更宽松。再加其余球的全部大小也是安全上界。

令y=Mu，定义全source物理顶点上的

    L(y)=13个最小值之和，值来自
         {|B3(y)∩B2(z)| : z∈V(G), z≠y}。

因为M是bijection，13个不同旧邻点x∈N_G(u)的Mx互不相同，并且都不是Mu=y。它们对应的13项交集总和必不小于全局13个最小项的和。因此

    |U(u)| ≤ Umax−L(Mu)。

不需要每个pair交集至少5；不需要M(N(u))仍是source邻居集。排序必须按不同**actual vertices z**，不是phase或orbit代表；z=y须从13项选择域排除。

## 4. 一个实际y已足够：260个重叠给6724

原事前“min_y L(y)≥57”使用了已被反驳的6860统一总界。actual最大总界6984对应的整数阈值应为

    L(y)≥6984−6804+1=181。

查询并未证明全source的Lmin，因为实际第一y已足够而立即停止；不能把未计算的all-y Lmin写成已验。

只需**存在一个y满足L(y)≥181**。实际y=0对全部6803个其它actual centres求交/排序，13个最小值各为20，故L(0)=260。任意bijection M都存在唯一preimage u=M^−1(0)；无论u是谁，均服从全source最大总界6984，因此

    |U(u)|≤6984−260=6724<6804。

这严格排任意M的D≤4；该root至少漏80个对面target。既不要求M保phase/affine，也不要求M与任何source action commute。实际13项的labels与20值在 `OVERLAP_RESULT.json` 保存；这里不重算。原uniform-profile预测失败没有破坏第3节的集合证明，而是由实际maxima正确替换了数值前提。

## 5. 早期Aut84想法不是当前No的前提

早期81个identity-fibre代表的准备保留为历史；若使用source automorphism，它确会同时保持球/交集multiset，而不要求matching对称。但当前上界maxima直接由全6804 R2/R3得到，witness0也枚完全部6803个z；主证明不再依赖Aut84或81个代表覆盖全部source。C++虽保留最多尝试y0..80的循环，实际第一个y0就达阈值，存在性证书已完备，无需all-y扫描。

本次只读代码确认：closed r1含自身及old邻点；r2/r3逐邻点OR前一半径；maxes对全部6804行取；交集用popcount(r3[0]&r2[z])、排z=0并按(overlap,label)排序取13。bitsets仅设置actual0..6803位，尾部未用位不会贡献count。没有运行代码或第二次数值验证。

## 6. 结论的实际边界

新数据query只产生这个新cross-route overlap support，不是重做旧sourceD4全有效性验收。实际L/maxes已支持阈值，负结论覆盖**同一6804源的两份全保边、仅加任意perfect matching**，包括mixed-phase point matchings；不是一般14/D4上界，亦不排改旧边、另加copy内oldold边、非matching跨连接、其它source等规则。

若源D≤4也已继承，任何这样的双copy图都有D≤5：先从root跨其matching边，再走对面源≤4步；同copy沿源≤4步。故上述负结论成立时该构造只能D5，仍不生成/验收或登记新的13608图。

ordinary phase容量π仍是实际FEASIBLE，NB容量模型仍是8秒无incumbent UNKNOWN；不能将更强的actualgraph族NO反向改写成NB必要模型INFEASIBLE。root line累计13.170781895/15CPU，含最初format/header失败及81→all6804范围修正；本review只读回执，不重置/重跑。完成即停，0新图/参数/Lean。

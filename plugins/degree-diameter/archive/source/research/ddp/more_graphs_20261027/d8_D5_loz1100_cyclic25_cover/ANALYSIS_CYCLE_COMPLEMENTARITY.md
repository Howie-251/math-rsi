# cyclic C25 模块的五圈互补：正向覆盖证明

本文件只审已冻结的Loz1100→5500普通五覆盖，不枚词、不构图、不BFS。固定source、25项规范化及实际检验范围见 [ROOT_PREDICTION.md](ROOT_PREDICTION.md)、[ANALYSIS_NORMALIZATION.md](ANALYSIS_NORMALIZATION.md)。sourceD4验证继承，不重跑。

## 1. 模型与合法性

沿用RIGHT law
(j,n)(k,t)=(j+k,n·2^k+t)，phase20、normal Z275。

2^20=1 mod275；例如在mod11已成立，在mod25可用(2^4)^5=(1+15)^5≡1。因而这是合法群，order5500。投影n mod55给已验Loz1100 quotient；kernel为K=55Z275≅C5。

规范正元固定为
g1=(1,0)，g2=(12,33+55s)，g3=(11,1)，g4=(16,19+55t)，s,t∈F5，
及其目标群真逆。该定义没有改变phase/frame，也不试其它模数。连通性可由g1^-11g3=(0,1)直接得全normal，再由g1得全部phase；度8由八个不同非零phase保证。规范化完整性由另一paper负责，本文件不重复其25类计算。

## 2. 为什么两个几何和都等于55

j=12或16时，r=2^j在mod11为非单位一的五阶元，因此
1+r+r²+r³+r⁴≡0 mod11。

在mod25，因j是4的倍数，有r=1+5c。于是
sum(k=0..4)r^k≡5+5c(0+1+2+3+4)≡5 mod25。

CRT给这个几何和恰为55 mod275。这个证明不依赖s、t，也不需要枚举word或大幂。

RIGHT法中(j,n)^5的normal为n乘该几何和，phase为5j=0。因此

g2^5=(0,165)，g4^5=(0,220)，

因为(33+55s)55≡165、(19+55t)55≡220 mod275；55²是275的倍数，参数项全部消失。取逆又给(0,110)、(0,55)。这四个normal正好是K的全部非零元素。

源quotient上这两类generator是order5；full lift中它们五次幂是非零order5 kernel，故自身升为order25。这里的五次幂确实携带短kernel位移。

## 3. 这是整个same-fibre类的覆盖保证

identity到K每个非零点都有长度5的显式word，identity本身用空word。对任意g，Cayley左平移把这些路径送成g到gK的路径。因此所有投影到同一quotient vertex的点对都≤5。

没有把K当中央子群；K是normal，gK正是该quotient fibre，已足够。四个显式word独立于s、t，所以这个整类覆盖对全部25规范设置都成立。

## 4. 它没有自动给full D5

quotient源D4给每个base target一条至多四步路线，但其lift只能先到该fibre某一个点；再附加上面的kernel五步路线，直接拼接仅给≤9，不给≤5。要成功D5，非identity quotient fibres仍必须在总五步预算内达到全部五个deck状态；实际producer的完整identityR5就是检验这项全局条件。

因而“same-fibre≤5”是真实正向覆盖定理，而“存在完整D5设置”仍是主producer冻结预测，不能提前填成功或actualD。

## 5. 与Jordan elementary-abelian模块的精确区别

在前一Jordan F5²模型，对相同order5 phase类别，A^j=I+cN且N²=0；其五项和为5I+c(0+1+2+3+4)N=0。因此相应五圈可能仍完全闭合，不能从shear存在推出kernel短路。

这里normal的5-primary部分是cyclic Z25，模25中的5不为零，几何和给55这个非零kernel元素；它与F5²中被特征五消掉的和不同。这解释的是本五圈holonomy机制，完整图的D5仍按各自冻结frame实际验收。

本分析新增参数评价、word枚举、graph、BFS、solver均为零。不扩其它phase、坐标ring或prime。

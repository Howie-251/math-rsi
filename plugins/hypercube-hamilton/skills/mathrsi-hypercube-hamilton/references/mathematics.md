# Marked matching extension: exact tools

原[研究报告](../../../archive/source/Ruskey-Savage_Q6_研究报告.md)、[P6总装](../../../archive/source/research/six_directions/P6_FULL_CLOSURE.md)与各层closure是证明主体。以下保留插件使用时需要的实际数学接口。

## P6、圈与六方向

**P6。** 任意Q6短边匹配M、任意u∉V(M)、任意与u异奇偶v（可覆盖），有含M的Hamilton u–v路。

**推论。** Q6任意短边匹配含于Hamilton圈。非完美M选自由u及短邻点v，P6路加uv闭圈；完美匹配用Fink已发表定理。故最终圈没有自由根限制。

**提升。** Fink–Hotmar原文Theorem5将维数d完整自由根路径命题提升到任意维至多d方向的匹配圈延拓。代d=6即六方向结果；不是任意方向的原猜想。原文定位见[six_directions/paper.txt](../../../archive/source/research/six_directions/paper.txt)和随包文献。局部任意长边完全匹配是辅助域，不使P6变成Q6完全图版。

## 保根包含极大化

给M和自由u，在Q6−u逐条加短边直至包含极大L。若u所有邻点覆盖，L全图极大；否则取自由邻点a，L+ua全图极大。导入Havel–Křivánek1982 Theorem2：全Q6包含极大匹配≥24。故|L|≥23且≤31，自由顶点数为2,4,…,18。

这不是最大基数匹配定理。临时ua不成为规定边；同一u/v不变，v可能被补全覆盖，所以每层须有covered-target量词。全部层接口在P6总装表；12⇒14⇒16⇒18是有向依赖，不能循环。

## 全称森林秩门

在V={0,…,31}固定H={0,1,2,4,8,15,23,27,29,30}，K=V−H有22点。令S为Q5−0短森林，K点度1、H−0点度2。无圈意味着十一条不交路径，端点正好K；配对每路径两端得P(S)。对任意K完全匹配F，F+P(S)单圈时展开S给V−0的31点简单圈，新增边全短且保留F。若F/P有共同边，其标记二重边会成为独立2圈，不可能全连通，故无重复边漏洞。

定义H22所有完全匹配间的二元连通矩阵，连通=其带标号并为单个交替圈。导入Cygan–Kratsch–Nederlof *Fast Hamiltonicity checking via bases of perfect matchings*, JACM65(3),2018 Cor3.5/Theorem3.4：`rank_GF2 H22≤1024`。精确版本/页码见[原定位](../../../archive/source/research/six_directions/A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md)，其域允许长边及同奇偶端点。

**有限充分准则。** 1024合法S_i与1024合法完全匹配列X_j，A_ij=h(P(S_i),X_j)满秩1024，则每个F都与至少一个P(S_i)连通。

**证明。** 完整选中行因限制矩阵满秩而独立，进口上界使它们张成全部行空间。任意F的列非零：按F边(a_i,b_i)循环取R={(b_i,a_{i+1})}，F+R是一圈。若选中行在F列全0，则全部行在此列0，矛盾。展开对应森林即结论。□

准则不要求17496来源池穷尽；只需选中1024森林合法。缺秩不否定原命题。该几何的坐标稳定子大小24，轨道120/24=5；同时运输0/H/F，覆盖最后五个标记几何，不能当整个P6已复算。

## 局部极大正证书的运输

十二孔原内部L在固定二分图G内加短边为L*且保mandatory T覆盖。若目标v在L*被内部覆盖，h*=L*(v)用于修改为w−h*；若原目标跨边，其实际伙伴h不必等h*。正确关系是`L'⊆L*'`。

给局部极大证书P和补全D*，用`D=D*∪(L*'−L')`，于是`C_A=P∪L'∪D`仍是同一圈。所有补全新增边最后删去；恢复原边时用实际h。这使每个原L只需找到任意极大超匹配，而有限域只量化全部L*。

独立DP与逐证书唯一/合法/同总数负责有限穷尽。原[归约](../../../archive/source/research/six_directions/TWELVE_STAR_MAXIMAL_A_REDUCTION.md)、[正证书证明](../../../archive/source/research/six_directions/TWELVE_STAR_MAXIMAL_A_FINITE_PROOF.md)及对应checker保留；大流省略，现克隆不声称重算3620052条。

## 计数与保证的使用边界

几何覆盖≠每个实现匹配覆盖，正域可交叠≠可把计数相加。十孔用实际集合并与补集；十四孔20/5轨道需精确不交；十六孔30根星形+118双源互补是同一148源记录的分割。

最终[P6_FULL_REVIEW.json](../../../archive/source/research/six_directions/P6_FULL_REVIEW.json)为same-family/provisional，显式文献进口、无Lean、无同行评议认证。本轮有限A10独立复算只更新工具使用证据，不改整题状态。

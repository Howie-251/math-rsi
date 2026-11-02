# Jordan F5²：路线直觉、h-fibre结果及准确时序

该固定族1550项已终态：1544项不能填满最薄h-fibre，6项填满25状态，但六项实际R5检查都失败，完整D5命中0。范围为两固定Jordan actor、source的phase/11分量及完整775规范normal设置；本轮停止，不按缺项继续改参数。

## 判断的时序

主producer的 [PREDICTION.json](PREDICTION.json) 在实验前冻结“存在完整D5图”，最终被 [RESULT.json](RESULT.json) 反驳。h-fibre满25是这项主预测的必要子目标，六项局部成功只作为其分解证据。

本agent另写“至少一个设置填满h-fibre”的文件时间为2026-10-28 00:32:57.700255 UTC；Root已经于00:32:43读取完整producer结果。因此它只能记录为**此agent尚未见结果时的盲判断，不能称全局实验前的新预测**。保留原timestamp，不改造时序。该盲判断与六项局部结果相符，但不是独立的新pre-experiment预测成果。[ANALYSIS_ROUTE_PREDICTION.json](ANALYSIS_ROUTE_PREDICTION.json) 已据此标终态，pending为空。

## Shear确实产生二维方向，五步覆盖仍需短路

令N=[[0,1],[0,0]]，Aλ=λI+N，λ=2或3。N²=0，所以
A^k=λ^k I+kλ^(k-1)N；
A2^4=I+2N，A3^4=I+3N，Aλ^10=-I，Aλ阶20。

对v=(x,y)，det(v,Av)=-y²。y非零时v和Av张成V=F5²，说明shear是实际二维作用；若全部normals落在不变线E=<e1>，normal方向不会离开E。完整规范化及连通性由 [ANALYSIS_NORMALIZATION.md](ANALYSIS_NORMALIZATION.md) 给出。

但其pureV隔离使用zi^11等群字，证明的是生成整个群，不是五步内可使用这些方向。不能仅凭A^4非平凡就把group连通升为D5。producer的六个满25 h-fibre设置给出更直接事实：在这个指定controller槽，五步内确实达到了全部二维状态；其它槽仍失败。

## h10的78条路线与39上界

220商群最薄位置为h=(phase10,normal11=0)，raw NB≤5为78条。由于2^10=1且A^10=-I，π^-1(h)中每个(V,h)都是involution。一个word与其逆word因此到同一endpoint。去掉原involution边后的四inversepairs没有自逆字母，非空reducedword与其形式逆不同，所以78条word至少成39对；distinctendpoint≤39。

39仍大于25，不能单凭这个上界排除满覆盖。实际两λ各有三项满25，全部在首cyclic normal为v2=e2的stratum；其余1544项被thin gate拒。没有把39形式、六局部pass或普通坏对混为同一计数，也不将局部SUPPORTED写成完整图成功。

## quotient的边界

群G=(F11×V)⋊C20的commutator包含全normal：2−1在F11可逆，A−I也可逆。因此最大交换商只是C20；既存220 controller数据已在五步覆盖其phase商，没有从这里得到类似大交换商的uniform阻断。

另一个商是V/E的一维scalar quotient，阶1100。775规范类也可看作31个projective y-vector、每类25个x-lifts；标量quotient可给某个y-setting的必要障碍，但不能从其存在直接推出全部1550不可行。λ2对应的群类型与既有Loz1100同型，不过Loz成功D4使用另一固定phase/attachment，不能继承到这里。没有新开该旧phaseframe或额外quotient数值。

对Loz对照的order5 phases12、16（一般类j=4,8,12,16），A^j=I+cN。于F5中
sum(k=0..4)(A^j)^k=5I+c(0+1+2+3+4)N=0。
相应11分量的几何和也为零。因此这些order5 cycles在Jordan elementary-abelian lift中可以、且对这些phase始终仍闭合成w^5=1，不自动携带kernel位移。不能用“有shear”替代短cycle的实际holonomy检查。后续C275规则另有独立paper/producer范围，本族不续。

本分析没有参数评价、DP、word枚举、graph、BFS或solver。数据均引用已有producer；actual_global_D与普通无序坏对仍为空。

# 第二规模346516候选：独立验收预测，先登记

2026-11-01。继承小规模7532的实际成功，但不把它当大规模已通过。

本次只测原balanced H342290/13862745与old346515基础上的唯一候选。完整H、old346515、new346516各单stream。预期仅删65条实际diagonal clone–ownF边，添hub346515到342225..342289的65条边；H全部13862745边不变，4225clones各自恰连N_H(center)∩U，U为0..342224。diagonal j取ovoid的实际spreadowner，不假j=i。

预期n346516/m14204970，degree65:1、80:65、81:4225、82:342225。全部4225 clone邻居从这一次H stream独立绑定；实际U pins必须两两不交。只对65个改动的diagonal clones及hub进行66次普通radius3 BFS，预测分别(1,80,5250,341185)、(1,65,5265,341185)。4160 offdiagonal根BFS=0，其预测(1,81,5329,341105)不冒充实际测量。

完整全点对由保留H的old-old、全部clone的U-only endpoint路线、clone到fillers的首步U/ownF绕行、hub的flag路线共同证明；最终BFS不能被用来删顶点倒推小prefix。prefix从H直接添加modified clones、hub最后。特别检查diagonal遗漏ownF后是否仍有两步flag绕行。

从66个授权BFS内保存一个实际distance3 pair和Walk，旧根0。hist预测与数学覆盖分别记账；出现差异不更改预测。40CPU总预算含prep/compile、单worker，0旧field/geometry/projection/旧根/off4160 BFS/Lean/solver/付费审阅，0其他q/k/候选。实际candidate关闭后才运行。

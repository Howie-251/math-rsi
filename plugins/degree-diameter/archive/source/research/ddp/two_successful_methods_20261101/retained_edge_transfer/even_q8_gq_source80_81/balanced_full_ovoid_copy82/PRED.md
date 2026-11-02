# Degree82 balanced fullO×spread immutable-N onecopy：事前预测

2026-11-01。root仅授权这一完整终图，生产总30CPU、单worker，含准备、编译、源一次parse和输出；独立验收另由fresh代理负责。本批不增加accepted计数，不生成83+、不重验旧field/geometry/projection/sourceBFS/Lean，不修改parent完整Lean队列。

源是已独验balanced81 filled graph：342290点、13862745边、全81度（不是Payne源）。采用原物理顺序的OVOID65.tsv和SPREAD65.tsv，o_i为第i点、S_j为第j spreadline。中心c_ij=o_i*585+S_j；index=65*i+j；新label=342290+index。

每个clone只接不可变source的完整N81(c_ij)：原Cartesian product linePoints[S_j]×pointLines[o_i]，移除自环；若j=owner(o_i)，补原source填点342225+j。不使用currentN、不加clone-clone边。C_off不是独立集，预期诱导2080条matching边、65个diagonal孤点，不能遗漏matching端点路线。

具体可推翻预测：全部4225个expectedN81与一次实际sourceparse抽出的actualN81逐行一致且两两不交。pinunion恰342225=source\D65，每个非D旧点负载1、65个旧D负载0。完整终图n346515、m14204970，保源13862745边不变，新增342225条old-new边/0new-new。最终degree81有4290点(65旧D+4225clones)、degree82有342225点。每个prefix cap82，输出全部4226个prefix的degree/load表。

root在本实验前给出的待freshBFS检验预测：65个diagonal新根hist=(1,81,5249,341184)，4160个off-diagonal新根hist=(1,81,5329,341104)。源R2公式分别73²−81=5248、73²−1=5328；newroot的R2加旧center自身1，不加其他clone（完整N两两不交）。这些只保存为预测，producer不运行source或newroot BFS，不以代入式冒实际预测验证。

公开竞争门已实际定位346450，故条件候选多65；exactsourcefill优先权UNKNOWN/JGT缺口继承。若同fill及复制接口已公开，优势归0，绝不称global record。

生产须返回：有n m header且body strictlex的完整边表、ordered expected/actual N81、center/owner/diagonal物理绑定、sourceparse计数1、prefix表、真实RESULT/TERMINAL和含全部CPU的driver receipt。发现生成/接口不符或预算耗尽即终态停止，不自行续跑/接受图/派下一端点。

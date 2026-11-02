# Source17：实际 dart 运输与共同 slab 坐标预测

2026-11-01。先登记预测，之后只运行一次小代数批次，总预算5 CPU秒、单worker。

固定 retained4=[31,59,60,72]，其余全部15个 admissible source 为
[16,17,30,32,35,42,43,44,45,58,61,64,71,73,74]。不更换层、W、域或参数，不求解 packing。

**可推翻预测 P1。** source17 与这些其他层共享 target 时，两族完整线不交的标量条件拉回 source17 后，其线性泛函张成 F9³ 的三维对偶空间。因此任何二维源平面都不能令全部这些限制只沿同一个非零 projective direction 变化。若实际 span 不满，或有合格平面得到一种方向，立即记录反例，不把此预测当前提。

**实际检验。** 只读已接受 source54 的 PARAMETERS.json 及已有 admissible 接口。共享 target 的两条 dart 为 x↦M17*x+t*d17、y↦Mw*y+s*dw；取 n=cross(d17,dw)，记录真实矩阵、noise、n、f17=n^T*M17、fw=n^T*Mw。两条异向完整线相交 iff f17*x=fw*y，因此两族不交 iff 两个实际 scalar image 集合不交。规范化同一等式两侧时使用同一个非零倍数。

枚举且只枚举 PG(2,9) 的91个 plane normals。每个 W_a=ker(a) 都记录六条 source17 dart 的 M^-1*d 是否落在 W_a；只把六条都不落入的平面计为逐 dart transversal。记录每个平面上所有 f17 的二维限制、非零 projective direction 数及限制张成秩。比较原 W={x2=4*x0} 与最优合格平面；保存完整91表和一个最优平面的 basis/真实系数。

**边界。** 这是局部 pair 不交条件及一个 source 的跨 dart 坐标耦合诊断。不能从单一坐标失败推出无 packing；两坐标支持、非线性点集、其他 source 耦合均未求解。不读56862边表，不复验 field laws/旧 all-rank，不跑 source BFS、Lean、solver、大点搜索或其他层的平面枚举。终态保存 NOTE/RESULT/TERMINAL 后停止。

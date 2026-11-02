# p109固定phase全部自由A/B：71286项完整无解

本轮只解除canonical低系数A/B约束，保留同一三点底图、p109、M36、原phases及C1。全部六个primitive18 actions、全部A/B共71286项完整结束，D9端点覆盖解零；没有UNKNOWN、未试、新图或BFS。事前至少一项完整成功的预测被推翻。

## 新范围与完整判据

此前唯一实际canonical N109/r4/A29/B92图在首轨道根失败。互补诊断发现端点差−2−r³−r⁵在109产生源73没有的碰撞，因此root授权解除本次人为选定的polynomial A/B关系。不是换prime、phase或依据坏对下降续搜。

[PREDICTION.json](PREDICTION.json) 在参数求值前固定六个r={4,34,43,71,82,93}、全部A,B∈F109，以及C=(1,6)、loop=(0,3)。0→1电压为e、(A,10)、(B,14)，0→2为e，1→2为C。包括A=B=0，共6×109²=71286项。每项都定义simple4regular11772/23544图；C与loop的commutator产生非零normal平移，phase3及10生成C36，故连通也不依赖A/B非零。

互补代理只导出 [genericforms](../phase_analysis/generic_ab109_forms/generic_ab109.meta.json)，不搜索A/B。ABF1输入含1944槽、656320个去重field triples；每个三元系数表示一条≤9非回退路由的normal端点ua*A+ub*B+uc mod109。每action的324槽为三种rootbase、三种endbase、36phases。

普通≤9路径可消去立即逆向回退，因此完整非回退词给全部可达端点。一项D≤9当且仅当324槽全部覆盖109个域元素。程序按不同forms数、再localid排序作必要筛；形式数量只决定检查顺序，不能当覆盖充分条件。

输入生成任务已用现存canonical r4/A29/B92控制，108个root0槽缺集逐点MATCH既有347缺项；没有重跑旧图BFS。只有全部324槽通过才实际生成图并验证三个identity-fibre根，本批未进入该阶段。

## 实际计数与三槽解释

| r | 已处理A/B | 数值槽求值次数 |
| --- | ---: | ---: |
| 4 | 11881 | 12543 |
| 34 | 11881 | 11936 |
| 43 | 11881 | 11926 |
| 71 | 11881 | 11926 |
| 82 | 11881 | 12543 |
| 93 | 11881 | 11936 |
| 合计 | 71286 | 72810 |

全部71286项实际数值求值，capacity预剪零；fullsurvivor零，未试/UNKNOWN零，最终cursor r93/A108/B108。native0.155001CPU秒，编译1.045843CPU秒，整批1.203281CPU秒；forms准备由互补代理另外耗时0.868743CPU秒。

只读 [FIRST_FAIL_SLOT_COUNTS.json](FIRST_FAIL_SLOT_COUNTS.json)，全部参数首失败仅落在三个必要层：

~~~
localid303 = root2 → end2, phase15;
localid306 = root2 → end2, phase18;
localid9   = root0 → end0, phase9.
~~~

所以这三层联合全覆盖已不相容；没有声称每层单独无解，也没有声称其余321槽已逐项求值。必要条件提前失败足以拒绝完整参数，无需生成71286张图。

证据为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)、[search.cpp](search.cpp)、[run.py](run.py)、[search.log](search.log)。实际新图n/D、普通无序坏对均为null；72810是槽求值次数，不是图坏对。没有保存或优化最小坏对分数。

已闭范围仅为p109/M36、六个primitive18 actions、固定底图/phases10/14/6/loop3、normalized C1及全部A/B。其它prime、phase、C0或一般11772点四价D9图均未排。按约停止，不自动扩大参数或追加局部修补。

后续更大但仍固定的阶十八phase族已另完成，见 [phase_order18_family/REPORT.md](../phase_order18_family/REPORT.md)；本报告的原(10,14)计算不重跑。

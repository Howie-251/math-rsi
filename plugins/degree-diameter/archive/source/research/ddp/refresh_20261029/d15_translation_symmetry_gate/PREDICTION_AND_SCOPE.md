# 15552源的完整fiber-preserving平移核：事前范围

只研究字面标签 `81*u+x`、x为F3^4低位优先三进制坐标下的平移
`(u,x) -> (u,x+h_u)`，不改变controller、不寻一般线性/仿射自同构。
输入为已逐77760个arc-input邻集绑定的 `source15552_AFFINE_RELATIONS.json`。
不重读literal源边表、不BFS、不重复旧图验收。

旧账本对应15552 source-gap条目以及loop-completed各相关说明只保存：c=0所给的
取负自同构、完整取负不变/affine-line邻域范围、二择rank1反射兼容性结果。
其中“translation为0”说的是弧常数c，不是本次768未知h的平移核；未见本范围
同步线性系统已被计算。本次不重跑上述旧任务。

唯一系统为全部960弧的 `B_e h_from - h_to ∈ span(v_e)`。选择v非零pivot p，
对每i≠p加 `v_p*(B_i h_from-h_to_i) - v_i*(B_p h_from-h_to_p)=0`，恰2880行、
768未知。自弧的同一变量必须累加后模3，不能覆盖。c消去，不固定任何h_0。

预测是可能存在非零同步平移，但不预设维数、freefiber满秩或648端口传递。
一次GF3消元得完整kernel，逐basis核全部原方程；以各fiber投影子空间计算实际
648端口轨道。投影可以相关，不能把每fiber的平移独立施加于同一全局候选。

总CPU≤15秒、单worker。0solver、0新球/图、0源D4验收。只报告有证据的对称归约
范围；若核或端口作用无效，停止，不续旧K2 timer，不固定A0。

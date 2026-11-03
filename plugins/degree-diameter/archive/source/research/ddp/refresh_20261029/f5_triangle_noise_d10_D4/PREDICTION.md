# 将三分支配给三角闭路的预测

冻结于2026-10-29，新域图生成之前。上一global-port100图已经实际失败；本批不重跑或改写其结果。

保留source30、F5³、所有Tport与方向。使用source已保存十个disjointK3和external六C5的真实edge分类：triangle边每向3个系数，external边每向2个，故每顶点度2×3+2×2=10，n3750/m18750。每无向edge按controller label u<v选公共类型集合A_tri或A_ext，反向取负，确保真逆关系。

真实变更是分支量沿不同闭路的分配，不是对旧global inverseportpair的100项再调值。source0的triangle端口为0/2；旧global域不能把其三角形三条边都设为3分支。

局部可推翻预测：任三元A_tri⊂F5都有A_tri−A_tri=F5；经同一triangle边的两步往返可得到整条输入轴。同root两个triangle端口连续往返四步覆盖其两轴平面。因此root0至(1,0,1)（全标签26）在本100域全部可达，另一个旧首反例52同在该平面。不能把这两个点的修复当全图覆盖。

联合存在预测：100=C(5,3)×C(5,2)个类型系数集合中至少一项完整D4。先测对称A_tri={0,1,4},A_ext={1,4}，其余lex一次。生成完整图并检查simple/degree/symmetry，每项到第一root反例即停；只有全部3750roots通过才保存hit并安排独立边表验证。

预算单worker45CPU（44CPU保存游标，45/46软硬限）；无seed/score/加时循环。全无hit即停止此类型分配域，不自动添第三噪声种类或换field；有明确新认识再作决策。

当前(10,4)公开基线2485已primary核，未标最优；3750若合法可超过1265。本批未声称保护原20度图旧旧路径，D4义务全部从新图核对。

# N11 全 Q(6,9) 非H9奇异直线度数筛：24个可接线像

固定当前Dhar37628点、205296边、最大度11图，使用已恢复的实际37471点核心fold映射（4074个split fibers），完成全部66430个flat-plane中心的几何线范围。**得到24个不同degree-feasible mandatory pinsets，全部10点，各只剩1个anchor名额。** 完整pool已立即交 `/root/debruijn_check` 接精确0/1anchor补全；本任务没有BFS、anchors优化或新图生成，不把度数可行称为新的N11图。

## 全域范围和旧失败复用

当前122个source pencils的完整恢复记录中，118条为非H9 Q-lines，其118个中心的9558条线已由另一代理完成degree筛，pool为空。输入source和actual fold映射均未改变，因此直接复用该终态证据，**不重复这118个已失败中心**。本次新枚举其余66312个未用中心；两部分合计66430中心、5380830条原几何线，范围完整而不是把partial profile外推成全类结果。

旧证据为 `../h9_other_degrees/degree11_geometry_result.json`、`degree11_line_witnesses.json`，映射校准为 `mapping11_result.json`。映射二进制是 `point_to_core11.u16.bin`，66430个native uint16，原point顺序与已保存66430×7坐标一致、core labels0..37470。没有沿用旧3075-split witness，也未假定它是current4074的子集。

## 实际生成规则

原生C++使用F9=F3[t]/(t²+1)，a+bt编码a+3b。对每个normalized singular point y，以六个H9 Plücker方程加polar行

`[y4,y5,y6,y3,y0,y1,y2]`

求核Π_y，逐中心确认核维数3。选择含y的基(y,x,z)，检查基向量的Q值及两两polar值均为0，确认平面totally singular。所有81个 `(a,b)∈F9²` 给外线

`span(x−a*y,z−b*y)`。

每条均直接检查不满足H9 line六式。非H9奇异线具有唯一flat-plane中心，故各中心一次、dual(1,a,b)一次不重复原lines。folded pinsets仍可能重合，使用排序去重后的完整pin tuple作canonical key，保留至少一份完整原10-point line witness。

逐线先生成无穷点，再生成t=0..8的其余9点。**只有某个实际生成的pin已满degree11时才早拒绝**；首点未满不等于成功，所有保留线都检查完整10点。早拒绝位置计数和实际检查point数保存 `RESULT.json`；最后两个拒绝实例直到第10点才发现饱和，因此实现没有将first-point筛误作完整线筛。

## 全部计数与成本

| 项目 | 数量 |
|---|---:|
| 新枚举中心 | 66312，全部完成 |
| 新枚举原lines | 5371272 |
| 新degree拒绝原lines | 5371248 |
| 新degree可行原lines | 24 |
| 加上旧9558零池后覆盖的原lines | 5380830 |
| 全域degree拒绝原lines | 5380806 |
| 不同可行pinsets / feasible重复fold tuples | 24 / 0 |
| 全部可行pinsets大小 | 10:24 |
| 实际生成并检查的point数 | 5628279 |

首1000个**新**中心的profile包含在同一轮枚举中，不重跑pilot：0.008485CPU秒，投影完整native0.613115秒，符合180CPU预算，因此直接完成剩余中心。实际native0.604824CPU秒；编译1.635860CPU秒，读取/准备与全部child进程合计2.245675CPU秒。一个worker，无新依赖，无全H9 incidence生成。

额外只对24个保留witness做一次轻量Python API对照：逐条重新从两点生成完整10个normalized points，原labels、foldedpins及current degree全部MATCH，CPU0.103928秒，见 `pool_calibration.json`。未重复全域枚举或任何距离计算。两阶段实测合计约2.350CPU秒。

## 交接和结论边界

`pool.json` 沿用格式 `records[{pins,anchor_cap,geometric_witnesses}]`，每条有 `anchor_cap=1`、center、Π_y basis、dual坐标、normalized line basis和完整10个原point labels。可用已有坐标cache读取每个point坐标，不需重建几何或原source邻接来生成line。另一代理已获pool路径和全部24项规模。

已确认：在**固定当前37628 source、actual4074-split fold、全部非H9 Q-singular lines**内，完整line像mandatory pins满足当前degree<11的候选恰为这24组。没有7/8/9-pin的degree-feasible项，也没有额外更大anchor额度可藏在这个范围内。

未确认：24组是否对整个当前base保D5、能否加一个anchor、可否产生37629点图；这些由后续精确补全与root最终独立验收负责。degree筛的拒绝只排除该固定source中原样添加完整line像，不能排除改变source、删边/删点、别的attachment机制、其他degree或一般N(11,5)构造。

终态 `COMPLETE_GLOBAL_DEGREE_SCREEN`，`pending=[]`；冻结预测的“unused centers中有新degree候选”获得支持。未扩N12，未进行候选排序优化或全源BFS。源图与理论credit仍属Dharunish Yugeswardeenoo及其采用的Rishabh Rajiv H9/partial-fold基础。本次新贡献为该明确有限参数域的完整degree筛和可复用24项pool。

复现：从项目root执行 `python research/ddp/more_graphs_20261027/h9_global_line_pool/run.py`。源码、profile、native计数、完整pool、旧零池中心清单和全部输入出处都保留本目录；不生成哈希或校验清单。

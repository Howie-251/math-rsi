# 指定q11表示的全部normalprojective族：新1463项无解

本轮没有新图。保留q11表示、H/C17生成元部分及A0，只解除B/C向量共线限制，全部1463个新projective设置均在完整端点条件失败；已验控制(0,1,0,2)直接继承实际D9，不重跑。因此这个指定族全部1464个非零projective类已经关闭，零tuple本来只生成816 component。

## 范围与预测

源F5模作用传遍24个非零方向，指定F11模作用只有12个方向一轨。此前控制C_V=2B_V会额外合并路线，因此root授权全部独立B_V,C_V。这是改变normal连接自由度，非按986个旧缺项作修补。

[PREDICTION.json](PREDICTION.json) 在参数求值前冻结至少一个新设置D≤8的预测。alpha=[[7,5],[1,4]]、beta=[[0,10],[1,10]]已VALID；chi17=5^v，H=beta^u alpha^v，A normal0，B/C的c,u,v仍为(1,1,12)/(5,2,11)。

F11*统一缩放四个normal坐标是群自同构，故非零tuple规范firstnonzero1共有11³+11²+11+1=1464类。删去唯一已验控制后，本轮1463类按pivot及suffix字典序完整处理；没有新q11表示、gauge或H/c17生成元变化。

## 精确generic端点筛

互补任务 [q11_generic_forms](../q11_generic_forms/q11_matrix_forms.meta.json) 导出全部585937条≤8非回退词的439258个不同2×4 coefficient matrices，按816个quotient端点分槽。每个矩阵作用于(VBx,VBy,VCx,VCy)给出该词的normal端点。

某设置D≤8当且仅当全部816槽都覆盖121个normal向量。不同matrix数量最少359>121，只用于检查顺序，不能当覆盖充分条件。程序对每个设置按少forms槽先查，第一槽不满121即拒绝；只有完整survivor才实际建图并BFS。

| 项目 | 实际值 |
| --- | ---: |
| 新projective设置 | 1463 |
| 实际数值求值 | 1463 |
| capacity预剪 | 0 |
| 必要槽求值 | 2511 |
| 完整survivor | 0 |
| 新图 / 新BFS | 0 / 0 |
| 已验控制重跑 | 0 |
| 未试 / UNKNOWN | 0 / 0 |
| native CPU秒 | 0.014773 |
| 编译CPU秒 | 1.042403 |
| 整批CPU秒 | 1.059654 |

结果为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)，参数为 [parameters.txt](parameters.txt)，代码为 [search.cpp](search.cpp)、[run.py](run.py)。959个设置首先在quotient identity槽失败；这只是first-failure分布，不是959个图坏对，也未据此继续优化。

完整排除不要求在必要条件已失败后再运行BFS。实际n/D及普通无序坏对总数保持null；98736只是这批候选的固定条件性阶数。旧控制actualD9及其一次BFS只见 [q11_D8_control](../q11_D8_control/REPORT.md)，不计作本批新验收。

预测REFUTED。已闭仅为指定q11表示、固定H/C17部分、A0及全部B/C向量；不排其它表示、quotient或一般98736点D8图。按约停止，不更q11rep/gauge或追逐失败槽。

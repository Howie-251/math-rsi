# F5删顶点机制的限定静态反例攻击

请只做静态数学审阅，不运行程序/搜索/安装/修改文件。本轮目标是从已有3750点20正则D3图删顶点，找超过1920点、最大度16、D3的诱导图。不是已排除的保全3750点纯删边，也不重新审查全部历史或公开纪录。

请读取：

1. research/ddp/refresh_20261029/f5_induced_transversal_deletion/DERIVATION.md
2. research/ddp/refresh_20261029/f5_induced_retention_closure/MODEL_CODE.md
3. 若需核字面控制器端口，读取research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json。

重点攻击两条承重推断：

一、任意每fiber删除25点、且对四个方向ell0..ell3的每条平行线恰命中一点的删除集，留下3000点16正则图，但不能D3。控制器0→5无≤2路线且唯一三步词为0→18→29→5，端口[0,2,1]，已有全36turn满秩证书保证每对纤维端点沿它只有一个3walk。固定retained y5，反向两步像为fiber18中含ell2方向的25点平面，遇至少5个deleted z；每z的fiber0逆首边是ell0五点线，含4 retained x。请核有没有遗漏替代路线、矩阵逆/方向错误、把单BFS当全图论证、或错误外推一般诱导子图。实际固定平面例的(1,626)新距离4，仅为对照。

二、一般retention模型的压缩必要closure：对距离3且控制词u-a-b-v唯一的控制点对，固定fiber a中z，字面邻接得L=N(z)∩fiber u(5点)，P=union_{w∈N(z)∩fiber b}(N(w)∩fiber v)(25点)。由于L×P的所有端点对在原完整图中唯一3路都过z，诱导D3要求 keep[z]∨¬OR keep[L]∨¬OR keep[P]。258个有序控制词（反向覆盖第二中间点）共32250条，等价压缩4031250条端点蕴含。OR门双向绑定。请查这个biclique压缩是否真等价、是否误强迫整fiber保留、是否以恰1921替代至少1921（当前未替代）。模型仍只是必要松弛，SAT须实际完整D3检查，失败则加该缺对全部原2/3路线的精确OR/AND cuts。

返回每条PASS或精确反例/缺口及其作用域。不要把数学审阅当作对CNF实现、数值BFS、Lean或公开新颖性的认证。

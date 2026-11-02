# H19 port assignment：模型与raw终态范围复核

**静态review支持模型；六orbit结果仍严格保留RAW_UNSAT_NOT_PROOFCHECKED。** 已读本目录 `run_once.py`、`RESULT.json`、`remaining_orbit5/run_once.py`及RESULT、`coverage_split_diagnostic/run_once.py`及RESULT，未运行solver、CNF复测、BFS或proof checker。

## 模型对应与容量编码

532个selector为 `x(port,helper)=19*portindex+helper+1`。28个port各一个positive ALO与atmost1；19个helper分别atmost1或2，总capacity28。故全部port恰一次时各helper自动满额，未误放松成少量未挂接ports或超容量helper。

`atmost` 的aux含义可取“前缀已有至少j个真值”。若输入≤k，以真实前缀计数赋aux即可满足全部条款；若输入≥k+1，forward/increment条款强制第k+1个真值之前的第k阈值为真，overflow条款矛盾。因此该编码是精确atmostk。首个前缀高阶aux没有显式置false不造成漏解或假UNSAT：上述最小threshold扩展仍存在，超额输入仍被强制排除。这里k只为1/2。

`orbit0/MODEL.json` 实际为1848总vars、10528clauses，其中6916=19×364个coverage clauses。source R0/R1/R2/R3/R4的取法与 [assignment exactness paper](../ASSIGNMENT_EXACTNESS_PAPER.md) 一致：旧 `PORT_BINDING.json` 明确将naturalhost绑定到 `Q_data.json['H3_graph']`，所以R1取该邻接+self；其它缓存采用同升序28ports、同old labels。每条coverage的条件是 `t∈B_(4−dH)(p)` 的positive OR，没有把重叠算成不同覆盖，也没有source/target混层。完整D5的last-entry证明与旧old-old/Hdiam4保证原样适用。

## 全六metric轨道实际完成，但没有新图或形式负证书

保存的 `HELPER_ORBITS.json` 给235个Hdiam4 labelled patterns在120个Petersen automorphisms下的六轨道，大小10/30/120/40/20/15，代表pattern25/65/306/328/1283/1284。helper同构只重标helper索引，保capacity和H距离，可转移自由port assignment，不要求oldsource自同构。

初批只执行representatives[:5]；remaining脚本只执行[5:6]，没有重跑前五或重置40CPU总账。六次均有合法solver exit20与 `s UNSATISFIABLE`，status为raw UNSAT，`proof_logged=false, proof_checked=false`；非CLI失败或timeout冒UNSAT。未输出383图、source/target383 BFS、Lean或ARIS。

这支持“固定Petersen九edge subdivision骨架的六metric轨道均未取得assignment、全部返回raw UNSAT，暂停该骨架”的计算结论。不能升级为proof-checked严格NO、一般19-helper或一般(4,5)不可能；旧k≤14的独立严格范围也不扩大到此。其它不满足Hdiam4的patterns由之前metric必要门处理，不是这六次SAT逐一执行。

## orbit0覆盖二分诊断的准确含义

诊断保留**全部**portexactone/helpercapacity前缀，只删选定helper的coverage blocks。按结果：

| 保留coverage helpers | 状态 | solver CPU |
|---|---|---:|
| 0..8 | raw UNSAT | 0.017582 |
| 0..3 | raw UNSAT | 0.118558 |
| 0..1 | UNKNOWN | 2.001128 |

所以当前定位仅为：0..3四个覆盖要求与完整分配容量已经出现raw solver冲突，最后已知raw-UNSAT集合仍是0..3。不能说0..1不可行、某个单helper已判NO，或两组各自SAT但没有共同assignment；`incompatible_split=null`，本批没有观察到后者。其它helpers虽不要求coverage，其slot约束仍在，诊断不能改述为“完全孤立的四helper局部几何无解”。按PRED到UNKNOWN即停，未继续二分或重求。

最后orbit后累计6.842230253/40CPU；包含此次三子模型诊断的最新累计为9.371241682/40，均沿原账。review只读CPU0.000921737秒，未改原结果或root/Wiki/页面，未新solve/DRAT/球/源/图，新增图、参数、Lean均0。

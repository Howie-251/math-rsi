# K19实际点匹配：三个窗口未给构造，当前仍UNKNOWN

本case0新图/参数/Lean。用两份已绑定684点7度D4源保全部旧边，目标1368点/8度/D4。旧全H342对称233928范围NO继续继承，不套给只保K19的更大域。

## 实际预测与实验

左乘旧exact-length缓存得到36个K轨道的端点集合，构建完整24624选择／24624实际跨点义务。全文模型73800变量、172800子句、29499552覆盖literals、166236739B，无空point子句；t0=0 gauge由目标全局K平移证明，sigma0不固定、不要求sigma自逆。唯一60秒CaDiCaL实际c UNKNOWN，无SAT／UNSAT，不是族NO。

依据长point OR与全局配对/shift耦合的搜索反馈，改成先配轨道再平移。5秒MIP返回一张容量minimum19的真实整数sigma（rawTimeLimit、非最优证明）；冻结这一张后，模型缩至1332变量／26586子句／819432覆盖literals。它仍是完整该sigma的实际点覆盖条件。唯一20秒CaDiCaL仍UNKNOWN；无sigma2。容量提高不计为graph结果。

随后预测“容量恰19的代表行不能独立铺满”。实际只一条紧行28→28，且可铺满（DFS5节点），预测被反驳，不能再把当前困难归因为这条行缺路线。其余行和全部平移的共同相容性仍未判清。tight19行的全覆盖又强制所选packet两两不重叠，因此显式添加2603条原CNF逻辑后果，不变更解域。最后5秒传播加强窗口仍UNKNOWN。不是以局部铺砌假装整个图存在，也没有证明global不相容。

## 停止与保存

三SAT窗口实际60/20/5秒，一次assignment MIP5秒；整个case96.356641619/100CPU包含readgate、准备、编译、模型构建、独立验收草稿、诊断及父子成本，没有重置。所有数值终态，不再sigma2、seed或同timer续算。RAW UNKNOWN保持，K19完整域仍开放。source literal parse／oldDP／旧D4BFS／candidateBFS／field／新Lean／ARIS均0。conditional independent verifier仅草稿，未运行数据。

CNF、A/B端点缓存、变量坐标、冻结sigma与全部原始状态已保存，可供未来有具体新问题时复用。本轮下一换实际source，读经典Cayley672的有限rightmatching域；不把未找到构造当整族无望。

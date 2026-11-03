# 给定T的八色源码，未运行

父批唯一backbone MILP已结束UNKNOWN_NO_ACCEPTED_BACKBONE，没有64端口T。因此本目录仅保留源码，没有CNF、目标行转置、SAT调用或候选图，不能登记着色失败。

`coloring.py prepare --backbone <BACKBONE_CANDIDATE.json>` 的未来明确输入必须是root保存的VALID_INTEGER_BACKBONE_NOT_COLOURED对象，含selected_columns和selected_old_labels。程序从既有R2/R3转置重新绑定64个literal端口，对全部15552目标分离共同R2已覆盖部分和残余U，仅合并相同64bit残余R3支持，保留每个原target的rowmap。

64位置每个恰一色；各色atmost8，因总64及8色，实际每色恰8。每条残余hyperedge对每色一个OR子句。颜色按首次出现排序只消去helper全置换：先把首出现颜色命名0，第二命名1，以此类推；没有固定任意原图端口/fiber为锚，也没有假设平移自同构。

atmost8使用forward前缀阈值计数器：每个真实第9个真selector触发overflow；≤8时令辅助变量等于真实前缀阈值即可满足，所以existential-equivalent。完整覆盖条件为每个helper i的 R3(A_i)∪R2(T)=V。

`decode --solution <literal model>` 只解析既有模型、重检64点恰一色/每色8及全部残余hyperedges，保存8组literal旧标签；程序不调用solver、不构图。只有未来明确授权且有真实T时才可执行。根负责实际新图度数和八个新根的独立验收。

本次执行数：源码写入1，prepare0，SAT0，球/BFS0，图0；父backbone UNKNOWN不外推为不存在K8解。

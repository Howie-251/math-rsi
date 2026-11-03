# 14-helper 终态：拓扑域完整性与固定源关闭范围

**支持本次完整NO。** 只读了 `unicyclic_topology_gate/run_once.py`、[RESULT](unicyclic_topology_gate/RESULT.json) 和TERMINAL；没有重枚任何拓扑、距离、port assignment、旧mask或source。必要门的数学前提沿用 [HELPER14_TOPOLOGY_INTERFACE](HELPER14_TOPOLOGY_INTERFACE.md)。

## 生成域没有漏掉合法单环H

- 14点simple connected unicyclic H有唯一cycle；前述owner距离门迫c=3..7，attachment深度分别≤3/2/2/1/1。
- 非cycle点有一个parent，因此最多3个children。`rooted` 用递归canonical children **multiset**（`combinations_with_replacement`，允许相同子树重复）覆盖全部此类树，以node budget剪枝不漏可用子树。
- cycle点已有两个cycle邻点，`attachments`容许0..2个branches；branch tree传入depth−1，所以加上cycle到branch的第一边后恰为规定总深度。全部attachment weights之和被严格固定为14−c。
- `canonical`比较cycle decoration序列的全部rotations和reversals；唯一cycle的任一图同构只能在cycle上作这个dihedral作用并匹配同构rooted decorations，所以此归一化完整。
- first-min剪枝只禁止后续decoration index小于首项。任何canonical序列的首项必为其最小项；相同最小项仍允许。因此剪枝不会删除全部代表，更不要求后续序列有序。

程序构图后检查n14、degree≤4、degree和28，以及 `Σ(4−d)=28`，均与tight spoke预算一致。未强加均衡branch、port标签或额外对称性。

## 两门的实际实现与结果

owners为 `d_H<4`，即恰有spokes的点。G1对**所有14个helper到所有owners**筛distance>4；不是只筛owner-owner。G2仅对leaf且parent degree≥3筛owner distance≥4；通过G1后这恰为distance4反例。没有错误应用到有两个ports的degree2 parent。

| cycle c | 深度界 | canonical H | G1排 | G2排 | 幸存 |
|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 1117 | 1110 | 7 | 0 |
| 4 | 2 | 275 | 270 | 5 | 0 |
| 5 | 2 | 494 | 486 | 8 | 0 |
| 6 | 1 | 12 | 12 | 0 | 0 |
| 7 | 1 | 32 | 32 | 0 | 0 |

实际1930个canonical topologies全部被必要门排除（G1为1910、G2为20），没有port assignment或完整378点图可继续。14-node抽象拓扑距离计算属于本批；它不等于source BFS或新目标图验收。

`raw_ordered_size14_decorations` 在初始输出中的正确语义是**经过first-min restriction的ordered计数**，不是全部未剪枝ordered decorations。仅修字段标签即可；它未用于数学排除或1930个canonical终态判断，无需rerun或修改数值。

## 合并后的准确结论

旧1..12 degree/port-spacing障碍、旧13-helper uniform-cell NO及14-tree纸面NO均继承、不重跑；本批完整单环NO补齐14剩余域。因此关闭：

**固定自然364/714源，max4、D≤5，保留所有源边、无新增old-old边，添加1..14个helper及允许的spokes/new-new边。**

不是任意有限H全部关闭；k≥15、更改/删除源边、新增old-old边、其它源、一般(4,5)图均未排。原自然364图本身不是NO，本结论关于非空增广。没有成功378图、新下界、参数或Lean，也不自动进入k15。

原RESULT实际caseCPU0.880238423/10（新增枚举0.130238423）保持。此次仅代码/终态只读CPU0.000263270秒；未改原程序/RESULT、root/Wiki或页面。完成即停。

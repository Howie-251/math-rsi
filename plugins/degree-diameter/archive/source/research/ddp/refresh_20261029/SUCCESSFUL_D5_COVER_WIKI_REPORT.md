# 成功D5源的ordinary-cover容量与保边prefix扩展

这是同一ordinary graph-cover transfer家族的一条新聚合实验，含三个source变体，不是新独立方法。实际只读三张final图、做5个规定根的NB弧消息DP；0BFS/cover图/solver，总编译+运行0.838358CPU。

D6：37631源0→13489的NB≤6为4，排k≥5；42402源42324→796为8，排k≥9；51457源49949→1574为2，排k≥3，因此排所有可越保存D6比较值所需的k≥11。保存比较值为186033/364032/538740，所需最小层数为5/9/11，非本次查新。

D5：root0到102/53/191各只有一条NB≤5，故三final源任何非平凡普通cover均不能D5。计数单位是NB走步，不是普通坏点对，也不声称所有target仅一条路或源只有空闭路。

普通覆盖的短路径投影必NB，每条基图走步从固定liftroot唯一提升，故c条走步至多命中targetfiber的c个点。小于k便严格阻断D≤D；适用于不正则source及非Galois普通cover。

prefix扩展已由静态单调性确认：全部见证标签在原publicbase内，103逐步保旧边，因此任意早期base/prefix的NB走步集合包含于final的相应集合。较小阶数要越同一保存D6界所需k不会小于final所需5/9/11。故相同界逻辑覆盖103成功prefix+3public bases；R5任意非平凡cover也全排。这不是106张图的新读数或重验。

独立6具体pair的MITM证据核对现已PASS，完整17条NB走步逐组匹配，另0.245694CPU，无BFS/DP重跑。数学构造104/4、confirmed103/3、Lean1不变。此实验使账本由371增372条记录，不增加独立方法数；普通cover之外的改边/分支映射与一般D6格未排。root负责最终状态后最后query。

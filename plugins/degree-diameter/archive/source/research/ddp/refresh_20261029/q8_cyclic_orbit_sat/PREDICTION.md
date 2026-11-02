# 以循环边轨道联合选择完整辅助连接

q8的条件目标仍1088/degree13/D3。pi_twist的反极点和集覆盖已揭示整族半周障碍；新(013)(457)(26)闭环4的14406族补半周但全失败，均停止，不换seed/延长旧模型。

本批不预选pi或电压：固定8个Q3，要求额外2factor在deck平移(a,l)→(a+1,l)下不变。允许pencil内额外边、跨pencil边和半周matching，包含不能用一个与deck交换的有向sigma表示的2factor；没有声称一般辅助K64必有此对称性。

全部额外无向edge orbit共244：不同label l<m相位d∈Z8有224，删12个d0 cube orbit得212；同label±d，d1/2/3每orbit贡献2邻居、d4贡献1，各8个label共32。每源label有60个实际extra邻居occurrence，恰2约束保留同orbit重复输入。

R2仅需256个无向pair orbit，R3只需228个跨pencil pair orbit，逐中介顶点的真实路径等价编码不变。与前轮197152变量无对称全模型的区别是这次使用真实deck自同构压缩且包含pencil内extra，不重用其timer。

连接性必要条件迫至少一条odd-phase边；用cube全局平移/坐标置换与deck单位乘法，可规范为四orbit(0,0,1),(0,1,1),(0,3,1),(0,7,1)中至少一个。只加四选一OR，不固定某一个，不继承旧0–8/0–16规范。代理已独立核对轨道计数、重复度数和该WLOG。

预测：这个紧凑完整对称域有K64/D3；SAT须按实际64行邻接检查全部64根，非只信轨道约束。若命中则立即造1088主图并独验；UNSAT未认证或UNKNOWN仍按实际证据标记，不排无此对称性的辅助图。

一次既存CaDiCaL，wall120秒、CPU硬限140秒，全批≤150CPU。无自动第二次seed/timer/子case；旧仿射、旧pi、旧1792模型、published纯删除域均不重跑。

# 统一H九仿射相位：跨source法向必要门事前预测

只固定已经在u0成功的H={(-z,0,a,b,z)}，不搜索新H。相位c∈W=<e0,e1>共九个，每个source最多选一个27中心块。候选source先限无self-port/P的336个，再排M非仿射的source；不根据数量相同假定异常集合相同。

先分开记录每source的9相位局部是否可行：ordinary四目标互异、每目标为81点仿射超平面；用真实M的27个像检查是否与其普通目标超平面重合。只有至少一相位局部通过的source进入跨source门。相位只改目标超平面常数，不改法向。

预测的全局真必要条件：同一target中，来自不同source的81点超平面若法向不同，则必交27点，不能同时入选；若法向相同，也最多选三个不同常数层。对每target将可用incoming source按法向分组，令h_b为最大组的source数，则ordinary入选数至多min(3,h_b)。每块有四个ordinary目标，故4T≤sum_b min(3,h_b)。如右侧给出的T上界<213，严格关闭这个统一H/九phase/指定source域，不运行无意义packing求解器。

这是必要门，不把体积或法向分组当充分性；M/P跨块容量和不同target的共同相位也可能更严。单worker总CPU≤30秒；0solver、0源BFS、0全88k图或新克隆图。不重跑81块域、原点线性域或729补空间。

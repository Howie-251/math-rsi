# (11,4)3645源的固定双边吸收：2673项完整测试，未生成3646图

本批2673个合法候选全部结束，0命中、0未试、0UNKNOWN。2626项不能覆盖新root；其余47项的新root能在4步到达全部旧点，但每项均出现旧旧点对距离>4。因此事前“至少一个候选给出完整3646/D4”的预测被反驳。没有以局部遗漏下降追加修补。

## 冻结的实际操作

基图为[当前3645点完整源](../source3645.header.edges)，20044边、最大度11，继承作者公开D4。原7个空余点

    3456,3489,3564,3571,3583,3603,3643

均为degree10，其R3联合已知覆盖2902点、遗漏743个旧3444层顶点，新增201层已全覆盖。这份既有精确结果在本批直接复用，没有重算7球或重验基图直径。

对每个几何点p，在其两份pointcopy各选一个当前相邻的spread-twin或spread-linecopy host。删除这两条不相交旧边F，再新增x，邻集S固定为四个删边端点T加全部7个空余点。新点degree11；四端点删后加回恢复degree11，七free从10升至11，所以每个展开候选都是3646/20053的11正则图。

scout从820×4=3280个原始模板中排去607个当前cut-edge不全存在的非法输入，冻结其余2673项。顺序为p递增，每copy host按T后L；实际affected旧根数37–44。几何恢复没有由producer重复，见[HOST_BINDING.json](HOST_BINDING.json)、[frozen.json](frozen.json)和[PROOF.md](PROOF.md)。

## 两项承重覆盖判定

所有删除边的两个端点都在S中。任意旧点到S的最短路径在第一次进入S时即可停止，不能需要一条位于S内部的删边。因此

    dist_(G-F)(v,S) = dist_G(v,S).

于是新root的完整D4条件，精确等价于sourceR3(S)覆盖全部3645点。将已保存free7联合与四个端点球取并即可；不存在“删边后旧free球路径可能破坏而未计入”的遗漏，因为最近S路径已由上述等式保证。

旧旧点对需要额外检查。取A=closedR1_G(T)。若旧点u,v均不在A内，则它们到T距离均≥2；任何使用删边F的路径长度至少2+1+2=5。因此旧图原有≤4路径不会使用F，仍保留。只有至少一端在A的旧对可能失去D4路径。

故完整验收检查每个A根和新x到全图的距离即可，不是对称抽样。理论至多49根；程序在每个已通过新root筛选的候选上先完整检查x，再按冻结顺序检查受影响旧根，遇到首个确定反例即拒绝。若有候选全部通过，才可导出并交root首次独立全图验收。

## 实际范围与成本

|量|实测|
|---|---:|
|冻结合法候选|2673|
|sourceR3新root筛失败|2626|
|新root筛通过|47|
|上述47中旧旧D4失败|47|
|modified-root BFS总数|1432|
|单候选实际已执行最多根数|44|
|一次预备endpoint sourceR3球|1964|
|free7联合重新计算|0|
|native CPU秒|0.100774|
|含编译及预备总CPU秒|2.599767662|
|未试 / UNKNOWN / 导出图|0 / 0 / 0|

既有free7联合转存为[free_R3.u64le.bin](free_R3.u64le.bin)。端点球缓存[endpoint_R3.u64le.bin](endpoint_R3.u64le.bin)按[ENDPOINT_CACHE.json](ENDPOINT_CACHE.json)顺序保存，全部完整。sourceR3计算是这批构造的新搜索数据，不是重复已知源的全直径验收。

每个候选的筛选结果、首个失败旧根/目标和执行根数见[RESULT.json](RESULT.json)的rows。[probe.cpp](probe.cpp)、[run.py](run.py)和[candidates.txt](candidates.txt)可复现本批，不需几何重建或新依赖。

首个通过新root筛的候选为ordinal127、p=40；它的新root到全部旧点≤4，但旧点3352到2244的距离>4。[first_oldpair_witness.json](first_oldpair_witness.json)保存该候选的两条F和完整11邻集；没有把>4猜成确切5或全图坏对总数。

47个新root成功不是47个完整图，也不是某一张图的47个普通坏对；它们各自被确定的旧旧反例否定。普通全图无序坏对数未计算，实际成功图n/D为null。

[terminal.json](terminal.json)已终态，pending为空。结论关闭这张固定3645源、同一点两copy的T/L host、指定两条cut-edge及原7free固定邻集这项完整有限范围；不排除其它删边、其它host/邻集或一般3646点图。按约停止，不增加删边、改free组合、换host队列或启动SAT。

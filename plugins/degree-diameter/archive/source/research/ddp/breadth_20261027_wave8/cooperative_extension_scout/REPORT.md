# 两点合作扩张：仅来源准备完成，尚未执行构造

旧“8 pins”指八个初始profile，不是degree预算。42342点源码`record42342_single_extension/probe.cpp:58`实际补足12个邻居；37628点源码同一行补足11个。两源码`:63–66`均对全部坐标作一次替换，连起始pin也可被换掉。八个起点没有给任何“最多八邻居”的数学限制。

|源图|degree cap|spare顶点|总degree slots|deficit≥2可共享点|双新点各自old pins上限|
|---|---:|---:|---:|---:|---:|
|42342|12|14396|17670|3206|11|
|37628|11|2504|3316|315|10|

旧12/11邻居的最好单点状态仍漏648/115点。37628全局单点MILP确实包含全部2504候选并约束sum≤11，终态UNKNOWN、无incumbent、无不可行证明；不是只搜索八个候选，也不能当UNSAT。本轮不恢复它。

## 新模板的完整条件

保留全部旧边，添加新点a、b和a-b边；a接old集合A，b接old集合B。必须有|A|,|B|≤Δ−1，并对每个旧点v满足1_A(v)+1_B(v)≤Δ−d_G(v)。集合内部不能重复使用一个pin；两集合共享pin时必须有至少2个旧degree slots。a-b-v形成的三角允许，目标没有girth限制。

对旧点t，精确距离为

    d_new(a,t)=min(1+d_G(A,t), 2+d_G(B,t))，b对称。

若一条从a到t的最短路使用b，其a→b前缀可用直接a-b替代；不使用b时只能沿A进入旧图。因此上式没有遗漏经新点合作的更短路线。在旧源D≤5条件下，old-old对仍合格，a-b距离1；完整D5条件恰为

    R4(A)∪R3(B)=V(G)，R4(B)∪R3(A)=V(G)。

这与两个彼此独立single-vertex覆盖不同，也没有在现有记录中找到同一模板的已执行试验。

## 是否有立即障碍

未发现degree总量或全部spare集合的立即障碍，整体可行性仍UNKNOWN。双新点最多用22/20条old spokes，而在每个old点最多供两新点使用的有效总容量分别17602/2819。此数量宽裕不说明有限小集合能覆盖。

利用旧best-set已有的R4覆盖证书，只对其保存的遗漏点检查直接邻接链：42342的648点分别有256点自身spare、384点有spare邻点、8点两步可达spare；37628的115点有114点在两步内到spare，另30950有旧路径30950–906–22927–33253到spare。故两个源的全部spare集合之R4并集都覆盖所有旧点，没有“连所有spare都够不着某点”的障碍。没有因此声称11/10个pin可行，也没有新BFS。

## 可复用文件和下一次成本

源邻接：`wave4/pencil_source/deg12_diam5_n42342.txt`、`deg11_diam5_n37628.txt`。

37628的全部候选编号、旧度与deficit在`wave4/record37628_single_extension/source_profile.json`；42342度统计在`wave4/pencil_source/degree_capacity_42342.json`，候选可直接按源行度<12恢复。旧best集合与遗漏点在各single-extension的`result.json`和`independent_cover_check.json`。

没有现成持久化R3/R4球矩阵：旧probe的R4 bitsets只在RAM，37628 global CSC临时数组已删除。`record37628_global_cover/matrix_metadata.json`只保留2504个R4球大小、索引与规模，不是覆盖列。重建双半径bitsets分别需152482432字节（约145.4 MiB）/23557632字节（约22.5 MiB）；旧R4准备CPU约1.581/0.310秒，仅为历史成本参照，不能当本次新profile计时。

`SCOUT.json`保存完整项目相对路径和条件；`source42342_profile.json`、`source37628_profile.json`仅是来源与局部spare见证，不是新邻居方案。本轮未写MILP、未执行新构造或搜索、未重下载或跑全BFS。新profile需另行有限预算，本轮到此停止。

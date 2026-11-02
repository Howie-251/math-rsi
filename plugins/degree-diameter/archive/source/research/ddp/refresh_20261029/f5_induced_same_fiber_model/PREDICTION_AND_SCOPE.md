# 同fiber完整短路线模型：事前预测与执行边界

固定已验F5源及其邻接缓存，仅增加同fiber不同端点的完整距离≤3必要条件。
父模型为 `../f5_induced_shared_routes_model/model.cnf`，315221变量、1290903子句，
其body只读复制，不重建旧门或重启旧solver。

全部30个fiber各125点，共30*C(125,2)=232500个无序点对。
每对直接枚举全部两步与三步源walk：预期三步恰两条，四个中间点互异；
两步路径或者0条（202500对），或者5条（30000对）。有5个共同邻点时，
用恢复的原OR5 flag z表示其保留OR。无两步路时不使用z。

两条三步路中间点为(a,b)、(c,d)。对保留端点x,y，其精确条件为
`keep(x)&keep(y) => [z OR (keep(a)&keep(b)) OR (keep(c)&keep(d))]`。
分配展开为4条clause，每条含两个端点负literal、可选z及两组中间点的一个
cross组合。预期新增930000子句、零变量，完整315221变量、2220903子句。

原邻接缓存读取一次，不读源边表、不做源图BFS、不生成实际候选。
OR5映射只读 `../f5_induced_shared_routes_model/RESTORED_OR_FLAGS.json`。
保存逐fiber路线计数、字面校准例及全部路径记录，可重建每条新clause。

单worker，总compile/native/driver≤15 CPU秒。若路径数、四中间点不交性、
OR5存在性或最终计数不符，或达到预算，立即保存实际阶段/cursor并停止，
不冒准备成功。只prepare，不写runner、不运行solver。

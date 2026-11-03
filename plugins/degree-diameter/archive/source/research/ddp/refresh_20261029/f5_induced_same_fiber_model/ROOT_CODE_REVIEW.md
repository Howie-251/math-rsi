# 同层与H65合并执行审阅

Root已读prepare_native.cpp/prepare_once.py和H65_CNF/prepare.py及PROOF。完整930000同层子句为精确两条AND路线加可选OR5的分配律；父OR5编号3000项均复用。H65 fresh range315222..333551与同层增量0新变量不冲突。各125点exact求和与65阈值双向绑定；条件整线及Tp运输有两个high共同guard。存在高依赖n≥1921，非全高依赖已读均匀高排除，不假定每层固定大小。

合并header333551/2316695，新增4片段实际95792行逐文件与header一致。原same-fiber-only CNF与MODEL已保留，未篡改旧shared模型或60秒UNKNOWN终态。H65最新Gemini静态审阅还在同线程处理中；root与作者已完成纸面/代码核对，先按已授权发现预算执行，外审若报实质错误须修正归约。

runner继承已审原逻辑，仅预算为300 solver/360 whole CPU、最多3calls、单窗≤180；UNKNOWN立即停，观察超时只轮询同PID。SAT后按真实度数/连通分量/全根距离检验并用全部2/3路径精确cut。仍非完整全点对D3 CNF；候选接受需root从边表独立验收。

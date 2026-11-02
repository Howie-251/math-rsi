# 真正383点候选：Petersen19合作骨架的完整端口分配

同族5005细分pattern已有235个Hdiam4；其余4770已因必要距离5排除。先按原Petersen的全部automorphisms归235个patterns为orbits；这仅重标helper，不对旧port假定任何对称。保存全部orbit代表和members。

变量x[p,j]表示28实际freeport p唯一接H的helper j。每oldport exactly1；10个原helper capacity1、9个细分helper capacity2，总容量28，因此atmost capacities自动使每helper恰填满。总383点766边，全4regular，oldedges全保留。

对每h∈H及每t∈old364加正OR：存在x[p,j]使d_H(h,j)≤4且t∈sourceclosedB_(4−dH(h,j))(p)。oldfreeports彼此源距5，≤5路不能穿oldhost再回H（至少7），所以这些coverage正是新helper到old的完整距离条件；helper之间Hdiam4，oldold继承源D5。全部assignment满足即为完整383 D5候选，不只是新根必要门。

球数据直接复用R2 cells/R3R4 bitmasks，R0self、R1已有Q_data actual H3adj+self；不新sourceBFS。exact-one/atmost-k用顺序计数器：s_i,j表示前缀至少j个真，传播和overflow保证≤k；合法prefix计数提供反向存在性。每port有atleastone。不给freeport或helper额外未经证明的对称固定。

单批最多5个不同orbit代表，每个唯一次CaDiCaL -t5窗口，不resume timer、无seed梯。若orbits超过5，其余明确未测。预测：至少一个完整assignment可行；实际SAT后直接核对28port容量与所有19×364覆盖，再保存383点完整edgefile。UNSAT仅按原始solver范围记（无proofchecked不包装形式化全族NO）；timeout仍UNKNOWN。

累计本族先前1.550420978CPU＋inputread.5＋prep.25＋实际parent/models/native，上限40CPU，每solver墙10秒/CPU6硬限。hit后另做最新baseline、独立图验收、Lean/ARIS。无hit则停止本批，不续任何5sec旧窗口；保模型和UNKNOWN以新结构反馈重评。

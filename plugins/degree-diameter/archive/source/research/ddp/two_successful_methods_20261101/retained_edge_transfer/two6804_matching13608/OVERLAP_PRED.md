# 事前预测：必然重复覆盖能否排任意perfect matching

普通phase π的NB窗口8秒4112nodes无incumbent，UNKNOWN；不续原timer。新问题直接检验点球集重叠，仍在同line15CPU内，继承10.347290774。

一次cross≤4可按旧prefix最短距离a分层。actual源球profile给cross覆盖并集的未扣重上界1552+13*152+138*14+1400=6860。定义L(y)为所有z≠y的|B3(y)∩B2(z)|中13个最小值之和。M注入使M(N(u))是13不同centre且避Mu，故覆盖≤6860−L(Mu)。只要存在y使L(y)≥57，对任何M取u=M^-1(y)，cross覆盖≤6803，排整个任意perfectmatching二copy族。

预测至少一个y可给57；先y=0，成功立即停，不为找到更好数值而继续。sourceAut84把任意root(g,x)送identity x，labels0..80为已绑定代表（旧vertex-split PRED），只为核prefix sphere统一上界读取81个R3和全部R2。查询是新matching覆盖数据，不sourceD4验证BFS/field。若81都不给57，仅此重叠界未成，不排任意matching。

一次C++编译/native；prep保守.3；继承旧10.347290774＋实际compile/parent/native≤15；native硬2CPU。保存每root球大小、L值、最小13centres。全图/参数/Lean计数0。

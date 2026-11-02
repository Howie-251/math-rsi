# 条件五删边gadget接口：spread前提已失败，未启动producer

本文件保留条件接口与完整检查理由。它不是已执行候选。共享结构计算已完成：固定p=0及已绑定σ的32条旧core边(u,σu)，每条的两个S-block并集都含16个非p ports；但选四条来exactcover全部64个非p ports的完整搜索为零解，MRV17节点，0.001002951CPU秒。证据为 [sigma_edge_spread/RESULT.json](../sigma_edge_spread/RESULT.json) 及 [SIGMA_EDGES.json](../sigma_edge_spread/SIGMA_EDGES.json)。

所以没有冻结spread输入，没有producer脚本、编译、图生成或候选BFS。本接口的前提失败，不是某张586点图的直径失败；不寻找新的σ、第五条spread边或局部补洞。

## 只有在spread存在时才有的数据接口

输入须由共享source结构任务给出，不在producer内重新找几何：

~~~
source_file: 已验585/2600源
source_D3_receipt: 继承证据
fixed_port: p
sigma_file: 585点实际图自同构，固定p并配对其余64ports
spread_edges: 四条互不相交旧core边(u,sigma(u))
anchor_set: 八个端点A
port_unions: 每条spread edge的S(u)∪S(sigma(u))
exactcover64: true
~~~

四个16-port并集须两两不交，覆盖P\\{p}。每个anchor的S都不含p，所以A在旧R2(p)之外。

给定这一个spread，固定枚举全部合法有向b,w：

~~~
b是旧core，b∈R2_G(p)，b∉A；
w是b的旧core邻点，w∉N_G(p)∪A。
~~~

顺序为b标签递增、再w递增；不以坏点分数排序或增加spread。R2(p)除p含72个core：八个N(p)中的b各至多八个core邻点；另64个distance2 b各恰有一个N(p)中的core邻点要排除。因此合法参数至多

~~~
8*8+64*7=512
~~~

再排除w∈A只会减少。这里不是把72个b误记为64个。

## 完整边修改与度数

令F为四条spread edges再加b—w。A、b、w互异，F为五条matching边。删除F；新增点x=585连接A及b，共九条边；再加w—p；其余64个port按σ配成32条边。

所有旧core的度九保持不变：A各删一加一，b删一加一，w删一加一。p由w—p用掉唯一空位，其余64个port由matching各用掉一个空位，新x度九。w∉N(p)保证w—p是新边，旧port独立保证σmatching都是新边。最终若构造将为586点、2637边、全九正则简单图：

~~~
2600−5+9+1+32=2637.
~~~

## port覆盖为什么条件式成立

任意非p port q原有某anchor a到q的至多二步路。四条A内被删边若恰为该路第一边a—σ(a)，另一端本身也是新根邻点，改用x—σ(a)—q更短；port末点保证A内core边不能是原二步路的末边。额外b—w的两端均非A且为core，因此不会出现在任何A到port的至多二步路中。

对p，b∈R2(p)给至多二步旧路。若删除b—w会破坏这样的路，则w必须属于N(p)，已被排除；四条A内边也不碰b。这保证新根到全部65个port至多三步。它尚不保证520个core覆盖或全部旧旧点对。

## 完整候选检查接口

若前提曾成立，程序须在实际改图上先检查新根R3覆盖全部585个旧点，不能只凭port覆盖接受。通过后，BFS源图中R1_G(T)的全部旧根，其中T为F的十个端点，并加新根。

任意两个旧端点都在R1_G(T)外时，任何使用F的源路径至少2+1+2=5步，故继承的D3路径不可能使用被删边，仍保留。新增边只缩短距离。因此上述根集是完整旧旧覆盖判据，不是对称抽样。T有十点且已有五条matching边，所以其闭R1至多90点，加新根至多91根。

原定预算为唯一spread下至多512项、10CPU秒、首完整命中停止；现在spread不存在，这些候选计数与预算均未执行，不登记为失败图或UNKNOWN搜索。

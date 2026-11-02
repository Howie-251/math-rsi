# 新结构侦察：线性码的Hamming商图在27格全部达不到已有下界

## 本次实际范围

先读取方法账本的说明与35家族目录，再定向检索Hamming、hypercube、covering/linear code、coset graph和distance-regular词条；未找到此前同一syndrome/coset生成入口的记录。未续跑deBruijn、ordinary voltage cover、31-chart或HS/H9等profile。

选择的是有精确全局路由解释的组合机制：按线性码划分Hamming图顶点，quotient的距离恰为码的coset leader weight。它是新的明确来源/表示入口，但仍处在广义阿贝尔Cayley类中，不将其包装成新的独立构造大类或原创方法。

状态：来源和生成规则恢复；理论必要筛已完成；27格无过线参数，停止。没有生成候选图、码矩阵或运行BFS。

## 已读primary来源

J. Borges、J. Rifà、V. A. Zinoviev，[*On nested completely regular codes and distance regular graphs*, ACCT2014, pp85–90](https://ddd.uab.cat/pub/poncom/2014/142913/intworalg_a2014p85.pdf)。实际读到covering-radius定义、§2 Lemma1/2、嵌套码的矩阵构造及§4 Theorem3，不仅使用摘要。

[印刷p87的Lemma1](https://ddd.uab.cat/pub/poncom/2014/142913/intworalg_a2014p85.pdf#page=3)说明：二元线性完全正则码的coset graph为distance-regular，直径等于covering radius。[印刷p89的Theorem3](https://ddd.uab.cat/pub/poncom/2014/142913/intworalg_a2014p85.pdf#page=5)给明确嵌套族：偶数m≥4、1≤i≤m/2时，阶数2^(m+i)、degree=2^m−1、D3。因此这个具体族最小degree15，已超出本Goal；其extended D4版本degree至少16，也不应拿到4–12范围里搜。

下面一般F_q的syndrome生成和距离公式独立直接推导；不把该论文的二元distance-regularity定理擅自扩成任意q/任意码也distance-regular。

## 完整V/E、点数与degree

取满行秩矩阵H∈F_q^(r×s)，非零列h_1,…,h_s两两不成比例。顶点为V=F_q^r，全部边为

    {x, x+a h_i}，x∈F_q^r，i=1,…,s，a∈F_q*。

所有反向增量已包含，所以图无向。非零且不成比例保证无loop和不同方向邻点不重复；H满秩保证连通。故n=q^r、degree=s(q−1)，边数n·s(q−1)/2。

它等价于码C=ker(H)的coset graph。若初始矩阵有零列或比例列，删除这些列并保留一列方向，不改变简单图的邻居集合；因此不能靠重复列制造“长度很大但degree较小”的漏洞。

## 全局路由保证与有限必要容量

一个syndrome y的距离恰为min{wt(e):He=y}：wt(e)=k给出按其k个非零坐标依次相加的k步路；反过来任意k步路可把同一方向系数合并，得到至多k个非零坐标。平移保持全部边，因此全图diam恰为C的covering radius。

所以选用covering radius≤D的码就会给出真正的全对D保证，不是仅部分控制点对的rank条件。然而相同的可交换性强制

    q^r ≤ V_q(s,D) = Σ_{j=0}^{min(s,D)} binom(s,j)(q−1)^j。

这是端点数上界：给至多D个不同列方向，各选一个非零系数。不同选择仍可能产生同syndrome，故容量通过不代表存在；必要界只用于止损。

当degree≤Δ≤12时，q−1≤12，因此q只需2、3、4、5、7、8、9、11、13，且1≤s≤floor(Δ/(q−1))。这给出一项完整有限算术筛：27格共495个(q,s,Δ,D)比较。还使用n必须是q的幂以及r≤s，记录界允许的最大q-power；没有枚举H的域赋值。

不依赖q的较松包络为Σ_{j≤D}binom(Δ,j)：每个有效坐标方向的q−1个非零选项视为一个block，合法选择每个block至多取一项，属于至多D项的子集，因此计数不超过Δ个形式选项的二元子集总数。这个较松包络在全部27格也已经低于保存下界。

## 27格比较

下表每格是“必要界允许的最大q-power阶数上界 / savedL”；上界不承诺可达到。savedL取项目27格保存快照，不冒充刚刷新的公开表；既有图下界已足以停止这个更小的类。

|Δ|D3|D4|D5|
|---:|---:|---:|---:|
|4|9 / 41|16 / 104|16 / 364|
|5|16 / 72|16 / 252|32 / 650|
|6|32 / 120|32 / 441|32 / 1518|
|7|64 / 170|64 / 684|64 / 2810|
|8|64 / 253|128 / 1100|128 / 5334|
|9|128 / 585|256 / 1768|256 / 9020|
|10|128 / 650|256 / 2485|512 / 33397|
|11|128 / 715|512 / 3444|1024 / 37628|
|12|256 / 810|512 / 5832|1024 / 42342|

例如(12,3)较松体积上界299、q-power上界256，仍低于810；(8,4)分别为163和128，低于1100。全27格存活0。

作为路由公式的一个纸面实例，二元H=[I_6|1]的kernel为长度7的重复码；coset中两个词的重量为w和7−w，最小值最大3。所以完整V/E规则给出64点7正则D3图。但64低于保存170，未展开或把这个已知folded-cube结构记作新成果。

## 结论、范围与产物

`screen.py`重现495项必要算术，`RESULT.json`保留每项q/s/degree/体积界、27格savedL和差距、来源阅读范围。计算CPU约0.002秒，0矩阵赋值、0码搜索、0候选图、0BFS。root没有待终验的大图。

排除范围是：所有线性码的标准coset/syndrome图，边由每个坐标方向的全部非零倍数给出；包含完全正则/距离正则的这些子类。没有排除非线性顶点分块、任意图商、部分选择标量的其他边规则或非交换构造。增加码长度、换H矩阵或再选完美码名称都不能突破该统一上界；若改变这些边/分块条件，那是需要新路由论证的另一结构，不能作为本profile追加seed。

本次止损不是新上界发现，也没有新下界或全局Goal完成。未写Wiki，交root统一持久化，pending为空。

# 四blocker donor转接与五helper协作：精确纸面门

状态：所提容量及加权距离接口成立，以下给出必要前提与完整性边界。只读继承accepted16416/fullN构造及local完整profile；没有数值、图/BFS、field、Lean、solver或外审。本文件独占paper，不改sole数值owner的输入/代码/回执。

## 1. 冻结的旧对象与每个v的候选规则

记原15552简单图为G。accepted当前图C有864个full-N clones：clone c_i的邻集恰冻结的N_G(a_i)，a_i为其旧source中心；无clone–clone边，全部G边保留。C的旧source点负载L0∈{0,1}，因此

    deg_C(w)=deg_G(w)+L0(w),  deg_G(w)∈{14,15}。

对一个未选旧source中心v，记N_v=N_G(v)，blocked点为

    W_v={w∈N_v : R0(w)=16−deg_C(w)=0}。

继承的342个selected-profile候选均有恰四个不同owner roles：每个w∈W_v由唯一当前clone c_i邻接，四个owner集合为S_v。每个这样的w都必为原degree15/currentdegree16；不是原degree14/cap2点。

每个候选都从同一accepted C独立开始，不能把上一v的删边累积到下个v。删除每条c_i–w（w∈W_v且owner为i）；不删除G的任何边。新Z连完整冻结N_v。四个donor保留邻集

    P_i=N_G(a_i)\{w∈W_v : owner(w)=i},

Z的邻集P_Z=N_v，均只含原15552source中的旧点。再在四donor和Z这五个helpers之间添任意simple H，其他860clones保持完整旧N。

## 2. 容量账与olddegree14重叠

对blocked w，原C度16；唯一donor边删掉使其度15，接Z后恢复16。对N_v中的非blocked点，当前度≤15，接Z一次后≤16；没有把degree14原点的load2机会禁止。特别是原degree14/currentdegree15的点即便仍在某donor的保留P_i中，也可同时接Z而成为degree16，这种P_i∩P_Z必须保留，不能用邻域不交筛掉。

令donor旧度d_i=|N_G(a_i)|∈{14,15}、删去b_i条donor边，则其最终度为

    d_i−b_i+deg_H(i)，要求deg_H(i)≤16−d_i+b_i。

Z最终度为d_G(v)+deg_H(Z)，要求deg_H(Z)≤16−d_G(v)（1或2）。五点simple graph另自然有度≤4，可将各容量截为min(4,上述数)。其余当前source点/860个clone的度账不变。H的边两端都为helper，不额外占用旧source slot。

故这些五个helper容量与oldslot交换检查同时成立时，最终16417图最大度≤16。边数为

    129240−sum_i b_i+d_G(v)+|E(H)|。

这条新规则会删当前C的部分donor边，不再是保留全部C边的普通append；但原G的116316旧边全部保留。

## 3. 移去四donor后base的距离确实保持

令B为C删去四donor**顶点**后的诱导图，故|B|=16412：它就是原G加其余860个完整full-N clones。定义r:C→B，把四个被移去donor c_i送到旧中心a_i，固定B的全部点。每条被移去donor–oldsource边映成G中同一中心的真边；没有clone–clone边需额外处理。因此r是固定B的graph retraction，B又是C的子图。

对所有稳定点x,y∈B，有

    d_B(x,y)=d_C(x,y)。

这是全点对的距离等式，并不只是B仍D≤4：C的任何Walk可由r映入B且长度相同，反向由旧嵌入保持。B的D≤4也可直接由已闭sourceG/fullN generic真Walk引理继承，无需旧BFS。

所以对任意P_i⊆V(G)及radius r，cached当前C闭球`B_r^C(P_i)`去除四donor目标后，恰为base闭球`B_r^B(P_i)`。cached路径若经过removed donor，在需要真实base Walk witness时应把该点映成旧source中心；不能把失效donor边直接当base边。

**缓存范围提醒：** 旧available-pin gate只计算4050个currentdegree<16的pin球时，该缓存不自动覆盖本问题的P_i；P_i可含currentdegree16的旧source点。距离等式允许复用已有完整缓存，但不允许把未保存的port球当空。需要的0..3半径信息必须确实来自本范围已保存的数据或sole owner明确的新准备，不能声称已经由4050行覆盖。

## 4. 五helper加权商图与Floyd

K为四donor加Z。所有K到base的边恰为h–p（p∈P_h），helper内部边恰H。定义加权图Q：

* 对H边赋cost1；
* 对不同h,g，base excursion的cost为 `2+d_B(P_h,P_g)`，其中集合间距离取最小；两类cost取最小；
* 对角cost0；空port集的相应excursion为∞。

为判≤4，只需集合间旧腿距离0/1/2，对应cost2/3/4；大于4的边可截为∞。允许P_h与P_g重叠时的cost2，这对olddegree14共用slot尤其重要。用Floyd求最短加权距离q(h,g)。

任何最终helper→helper路径，在连续helper出现点之间要么走一条H边，要么整段内部只在base，后一段至少是`1+d_B(P_h,P_g)+1`。反过来每条Q边都可由一条真实最终Walk实现，拼接亦可实现。因此

    q(h,g)≤4 iff 最终图d(h,g)≤4。

截断后只主张≤4阈值等价；不把∞解释为实际最终图不连通或真实距离无限。这个分解完整覆盖交替多次进出base/helper的路线，并非只准一段base excursion。

## 5. 按最后helper分解的base覆盖恰为充要

对任意helper h与base目标x，任意路径取最后出现的helper g，其后一定是一条g–P_g边再接纯base路径。因此精确有

    d_final(h,x)=min_g [q_full(h,g)+1+d_B(P_g,x)]。

反向不要求拼接所得Walk是无重复最短路；真实Walk长度已足够给上界。即使Q最短段曾经过目标x，拼接仍不产生虚假的短Walk。对≤4阈值，只使用q≤3，因此前述cost≤4截断足够，得到

    h可在4步内到达全部base
    iff union_{g:q(h,g)≤3} B^B_(3−q(h,g))(P_g)=V(B)。

这里g=h的q=0必须包含，使用本helper自己的闭R3；负半径项不加入。闭R0(P_g)=P_g，不能删掉port自身。结合第3节，可以用当前C的相同闭球，最后屏蔽四donor目标。

B内部全部点对已≤4，所以对于某个实际H，**完整最终图D≤4恰等价于**：

1. 全部helper pairs满足q≤4；
2. 每个helper的上述base覆盖为全部16412个稳定点。

任一项不能省略。只检查helper-to-base覆盖而不检查helper pairs，或只检查加权helper pairs而不检查base覆盖，都不是全D4证明。若后续对实际完整候选运行全部五helper的ordinary BFS并全到达16417点且半径≤4，结合B的已证D4即可验全部最终点对；无需再做16412个稳定root的重复D4验收。

## 6. 为什么只枚所有 inclusion-maximal H 不丢成功者

固定v和五个port集后，H只受simplegraph与各helper度容量限制。添加一条仍合法H边，不改oldslot，不增加任何距离，且保持maxdegree≤16。任意成功非maximal H都可逐条加合法边直到inclusion-maximal，仍成功。故完整枚举所有inclusion-maximal可行H足够。

这里maximal指**任一缺边都不能再加**，等价于每条缺边至少一个端点的helper度已达其容量；不是只枚边数全局最大的H，也不是每v任意挑一个greedy maximal H。10条可能helper边的完整有限枚举后保留此条件即可；本文件没有执行枚举。

若342个实际v及各自全部maximal H完整失败，负结论只排当前accepted I32/864-clone incumbent上、恰四blocker roles、只转接N_v内blocked donor边、Z完整冻结N_v及五helper任意H的指定规则。预算中断只能UNKNOWN，不能排此范围；更不能排5-blocker、多helper、任意oldoldrepair或一般16/D4。

## 7. exactD4与形式化边界

任意通过degree账的最终图有16417点、最大度16。D≤3时三次闭邻域增长至多 `(16+1)^3=4913<16417`，已足以数学排D3；无需最紧Moore3857，也不应沿用任意H下可能失效的旧source witness。该例行宽界不计新突破；当前不为它新编译。

原G及其860个完整clones构成base的真Walk接口可复用已闭缓存；四donor/新Z的短路径只来自实际ports/H，未来具体目标仍须无用户certificate前提、actuallabels与新finite cover/degree输入闭合。当前只完成paper，不借旧16416审阅/Lean PASS认证新的16417图，图/参数/Lean增量0，完成即停。

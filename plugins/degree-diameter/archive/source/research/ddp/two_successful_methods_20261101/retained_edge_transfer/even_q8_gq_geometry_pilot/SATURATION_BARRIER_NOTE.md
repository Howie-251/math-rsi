# Full-ovoid×spread饱和后的单helper障碍

**原预测成立，并可加强：在固定degree cap δ+k、k≥1时，任何只向既有图连边的新单helper，若要距全部现有点至多3，至少需要R²个pins。** q8 balanced为4225，Payne为4096；原先4160／4032的下界仍成立。一次选定集合诊断PASS，0.145388401 CPU秒／5秒预算。

这里研究的是声明的filledsource及其完整邻域clone结构。342290点／327744点的源尚未生产或验收，本文不是新完整图或纪录。不存在1／2步路线和必要degree下界不依赖源的D3上界；“距离恰为3”以及整个扩张图的D3仍以前者的D3接口成立为条件。

## 1. Pin union为何恰好漏掉D

设O={o_i}是大小R=st+1的full ovoid，{S_j}是full spread。记σ(i)为o_i的唯一spreadowner。令

\[C=\{c_{ij}=(o_i,S_j)\},\quad D=\{d_i=(o_i,S_{\sigma(i)})\}.\]

源的旧pair顶点为w=(p,L)。按声明的邻接式，w若有一个C中的邻居，必须同时满足o_i∈L和p∈S_j。Full ovoid和spread分别使i、j唯一。因此其唯一候选邻居是

\[\operatorname{owner}(p,L)=(\text{L上的唯一O点},\ \text{p的spreadline}).\]

只有当w本身就是d_i时，这个候选等于w，自环被删除，故w没有C邻居。其他旧pair恰有一个C邻居。对fill点f_j，C中与它相邻的中心必须是flag，因而是某个d_i；o_i∈S_j又唯一确定σ(i)=j。每个fill也恰有一个C邻居。

所以各N(c)两两不交，且

\[\bigcup_{c\in C}N(c)=V(H)\setminus D.\]

每个off-diagonal center不是flag，旧degree为δ=(s+1)(t+1)。每个diagonal center的旧pair邻域因删loop少1，但其fill补回1，故所有center都是full Nδ。旧pair各flag也被唯一fill补回1，而fill的degree为(s+1)(t+1)，因此声明的filledsource是δregular。这些是从小几何性质与邻接定义推出的条件结构事实，没有枚举或生成全部源顶点／边。

数量相容：balanced δR²=81×65²=342225，filledorder342290，只漏65个D；Payne δR²=80×64²=327680，filledorder327744，只漏64个D。

## 2. D到其他center没有1／2步路线

取off-diagonal c=(o_i,S_j)，j≠σ(i)，和d_r=(o_r,S_σ(r))。

相邻必须同时有o_r∈S_j和o_i∈S_σ(r)，这会强迫j=σ(r)=σ(i)，矛盾。

若旧pair w=(p,L)是共同邻居，就必须

\[p\in S_j\cap S_{\sigma(r)},\quad o_i,o_r\in L.\]

若j≠σ(r)，spread两线不交；若j=σ(r)，off-diagonal条件使i≠r，而ovoid两点不共线。两种情况都不可能。c不是flag，没有fill邻居，也就没有经fill的二步路线。

不同d_i、d_r同样不相邻；它们的spreadline不同，故没有共同旧pair；各自唯一fill也不同，故没有共同fill。因此每个D点到所有其他center都没有1／2步路线，只有到自身center距离0。若源D3成立，这些不同点对才可进一步写成距离恰3。

## 3. FullN copies以后，自由pin为什么只能服务一个cloneclass

每个c∈C已有k个clone，全部只邻接不可变的源N(c)，不同basecenter之间的N互不交。固定cap为δ+k。

源中每个非D点恰被一个basecenter使用，所以新增load为k，degree恰δ+k，已经饱和。D没有clone load，degree仍δ。每个clone的degree也是δ。因此新增单helper的合法pin只能取自

\[F=D\ \cup\ \{\text{全部已有clones}\}.\]

不同basecenter的clones之间既没有边，也没有共同邻居，因而没有1／2步路线。同basecenter的clones共有非空Nδ，距离为2。旧d_i与其自身diagonal cloneclass有二步路线；到其他cloneclass的1／2步路线则会给出源中d_i到对应center的短路线，已在上一节排除。Clones的邻居都在旧source，已有clone也不能补出遗漏的二步捷径。

于是每个合法freepin只能在两步内服务**一个**clonebaseclass：clonepin服务自己的class，旧d_i服务自己的diagonal class。若新helper的pin集合是S，要在3步内达到一个class中的clone，必须有一个S成员在那个clone的两步球里。因此所有R²个class各至少需要一个pin：

\[|S|\ge R^2.\]

原预测只使用off-diagonal classes，得到R(R−1)，也是正确的。补上D之间的短路线排除后，下界加强为R²。

## 4. 限制必须写清楚；极大cap下这个下界甚至可达

当前小degree目标满足δ+k≪R²，所以固定cap下任何下一单helper都不可能，不限于fullN生成方式。具体地，balanced k≤4143、Payne k≤4015时均严格排除。

不能把这句话扩大成对任意巨大k都不可能。若cap≥R²，纸面上可选每个class的一个现有clone作为helper pins。每个非D旧点两步可达；每个d_i经其diagonal class的selected clone和一个旧邻居三步可达；同class的其他clone经共享旧邻居三步可达。若原完整图已有D3，这样加helper仍有D3，并且其degree正好R²、被选clone只增1度。这只是说明边界的条件纸面例子，没有生成该巨大k图。

结论也不排除同时加入多个相互连接的helpers、修改旧边、换初始code，或提高degree cap后开始下一整轮复制。本任务不转成greedy、SAT或其他q搜索。

## 5. 实际对照检验

PRED.md中的新预测先于本次程序记录。程序仅读取已有O／spread／incidence，构造O点共线计数矩阵、spread交点矩阵和实际owner置换；它没有生成几十万个sourcepair，也没有重跑field、projection、BFS或Lean。

|选定集合|balanced q8|Payne q8|
|---|---:|---:|
|off-diagonal center数|4160|4032|
|实际C_off×D路线对|270400|258048|
|实际相邻／共同旧pair／共同fill|0／0／0|0／0／0|
|额外不同D点对|2080|2016|
|D点对的1／2步路线|0|0|
|必要helper degree|4225|4096|

全部8192个off-diagonal center均保存逐center汇总；小矩阵和三种结构类型的具体witness也保存。数据在SATURATION_BARRIER_RESULT.json、SATURATION_SELECTED_GEOMETRY_MATRICES.json及两个OFFDIAGONAL_TO_D.csv；终态CPU回执为SATURATION_BARRIER_TERMINAL.json。未出现反例，预测被支持，且加强得到一个精确的自由pin分类。

这改变下一步：若未来源和fullproductcopies实际完成，不能再把D里“还剩R个自由旧点”当作普通单helper的机会；这些点只能服务diagonal cloneclasses，无法弥补off-diagonal classes。应直接停止固定cap下的逐点fill尝试，而不是继续局部调pins。是否生产这些源、选择哪个公开竞争窗口、是否探索jointbatch或其他code，仍由root另行决定，本次不派发新任务、不计新图。

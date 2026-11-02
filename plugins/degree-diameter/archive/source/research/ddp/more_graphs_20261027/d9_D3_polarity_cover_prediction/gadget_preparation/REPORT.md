# 八anchor重接gadget：度数合法，但新根统一漏八个port

本准备任务只读取既存BLOCKS与结构结论，没有解析旧边表、寻找σ、运行候选或BFS。下面的障碍先于σ：指定规则无论使用哪个合法involution，甚至无论怎样匹配剩余56个port，都不能达到D3。

## 固定源与parallelclasses

继承上一任务已验证的源事实：585点、2600边；65个port构成独立集，旧度八，其余520个core点旧度九且各有唯一port邻点。对core点u，

~~~
S(u)=R2_G(u) ∩ P
~~~

恰含九个port，520个S(u)为Steiner3-(65,9,1)。证据为上一层 [RESULT.json](../RESULT.json)、[BLOCKS.json](../BLOCKS.json)，不重验这些事实。

固定port p，包含p的72个circle删去p，得到64点的72条八点线。两条不同circle属于同一parallelclass，当且仅当交集恰为{p}。因此每个class有八个circle，删去p后互不相交并覆盖其余64个port，共九个class。算法可直接对BLOCKS中含p的72行分组；[parallel_classes.py](parallel_classes.py) 保存纯函数，尚未执行。

须由实际source绑定识别哪一class恰为N_G(p)，不能从数值标签猜测。排除它后至多八个class可用。若某class在给定σ下不稳定，就跳过该class。σ若只固定p一个port，则任一anchor也不可能固定，否则它的唯一port邻点也被固定并等于p，与该class不等于N(p)矛盾。

八个anchor因而形成四个σ对。每个anchor有七个合法core邻点choice，保存的同步规则是在每个σ对较小标签anchor上取其第j个合法邻点，再取σ像作为另一半，四对共用同一j∈{0,...,6}。这是七个明确同步choice，不是全部7^4种等变选择；最多8×7=56项是预定有限范围。

## 所有新增度数及简单性

令八个anchor为u_i，其唯一port邻点为p_i。它们的S(u_i)两两只交p。

由于每个core点有八个core邻点，而S(u_i)的大小达到最大值九，这八个core邻点的唯一port必须两两不同，且都不同于p_i。因此对每个u_i，恰有一个core邻点属于N(p)，排除它后恰余七个合法w_i。也因此p_i—w_i原来不是边。

这些p_i互异且都不等于p。若两个anchor相邻，则后一anchor的唯一port会同时属于两者的block，矛盾；故anchor彼此不邻接。若w_i=w_j，该点的唯一port同属两个block，只能为p，但w_i∉N(p)，矛盾。因此八个w_i互异且均不是anchor。

删除八条u_i—w_i，添加八条p_i—w_i，然后让新点x连八个anchor及p；再将其余56个port配成28条matching。所有新增边都不是旧边，也不彼此重复。各u_i删一加一，各w_i删一加一；p及八个p_i用掉一个旧空位，余56个port各由matching用掉一个空位。其余旧core不变，新点度九。最终确为586点、2637边、全九正则的简单图。

σ等变只用于给剩余56port提供一个确定matching，并不自动给直径保证。度数与简单性成立，仍不足以成为D3图。

## 统一新根障碍

令q_i为w_i的唯一旧port邻点。由上述满值计数，q_i≠p_i；由w_i∉N(p)，q_i≠p。又因不同S(u_i)只交p，八个q_i互异，且都不在使用的九个port

~~~
U={p,p_1,...,p_8}
~~~

中。对每个q_i，源中u_i到q_i的唯一二步路为u_i—w_i—q_i；别的anchor与q_i没有至多二步路。删除u_i—w_i，恰好破坏了新根到q_i的三步路。

完整检查可能的新三步路：

1. 从x走向p：p和q_i是不同旧port，原来没有共同邻点；重接没有给p增加旧邻点，所以不存在x—p—y—q_i。
2. 从x走向某anchor u_j，末步用q_i的旧core邻点：其余u_j原本没有到q_i的二步路；u_i唯一的中间点w_i已经断开。重接的p_j—w_j不会增加任何anchor邻点。
3. 末步用q_i的新增matching边：matching只连接P\\U中的port。x在至多两步可达的旧port恰为U；所有anchor仍只有原来的port邻点p_j，p的邻点仍为core。因此matching的另一端不能在两步内从x到达。

新增p_i—w_i给出的路为

~~~
x—u_i—p_i—w_i—q_i
~~~

长度四，不能补足D3。故每个q_i都与x距离大于三，至少八个不同port统一缺失。证明不需要σ，也不依赖七个同步choice的数值。

## 结果范围与停止

[PREDICTION.json](PREDICTION.json) 在任何σ或候选查询前冻结了“至少八个newroot缺port”的可反驳预测；此处给出源前提下的纸面证明。没有实际生成586点图，没有普通无序坏对总数，也未把56项记作数值枚举。

若仍作实现校准，完整旧旧检查的充分根集为删边端点T的旧闭R1加新根：两端都在R1(T)外的旧点对，任何使用删边的旧路至少2+1+2=5步，故源原有至多三步路不会被删。这是完整覆盖根集，不是对称性抽样。但本规则已在新根必要条件失败，无需为此运行后续BFS。

结论只关闭这条“八条anchor边转移到其唯一port、再匹配unusedports”的固定规则。它不排除不同的连接机制或一般586点D3图。下一步若改变机制，必须让这些失去唯一入口的q_i获得真正三步路，不能把σ对称性或正则度数当作替代。

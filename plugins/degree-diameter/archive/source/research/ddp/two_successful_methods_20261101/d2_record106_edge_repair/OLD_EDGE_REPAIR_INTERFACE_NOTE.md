# 允许old-old补边的一个具体接口：critical endpoint relocation

本note只读本case已保存的SOURCE_RESULT、CRITICAL_EDGE_PROFILES、MINIMAL4_FORCING_CERTIFICATE及source邻接必要行，作纸面路线与度数分析。不生成或遍历候选，不重新2hop/BFS、不调用solver、field/rank、Lean、查询或旧Brown/n61框架。沿root已授权的M5+one old-old R，避免另开不关联的手工trade。

## 最小4失败的范围

当前公开源H有106点、582边，degree10仅T={34,54}，其余104点degree11，D2的单次源检查已完成并继承。只删4条matching旧边、加入一个10度点z且N(z)=T加8个删边端点、无old-old补边的范围，已由21条候选边的K={7,23,46,59}不可用pin证书严格关闭。这里不重算21条或5985组合，也不把这份负结论扩成一般107点D2不存在。

## 唯一新规则及其度预算

选择一条已记录critical旧边e={a,b}，其中k是a在源中仅经b两步到达的非邻点。于是a-k是原nonedge，且b-k是原edge。选择另一条原旧边{k,l}，四端点a,b,k,l互异、均不在T。先作

    H0 = H − {a-b, k-l} + {a-k}.

这是真正改变旧边：把a和k各一个旧degree槽改用于repair边a-k，而不是只尝试新点接不同pins。a、k仍degree11，不连接z；b、l降到10，与原T组成四个待补槽。

随后只删三条互不相交的旧边F3，其六端点与{a,b,k,l}及T均不交，并且不得删掉新repair边a-k。添加新点z，令

    S = N(z) = {34,54,b,l} ∪ endpoints(F3).

S恰10点。全部五条删除边形成matching，a、k是两处专用于old-old repair的端点，其余删边端点与T专用于z。最终

    G_old = H − F5 + {a-k},       G = G_old + z—S,
    n=107, m=582−5+1+10=588.

每个旧点最终degree11，新z degree10，simple性要求各端点互异、F5为原edge、a-k为原nonedge、z为新标签。以上度数只是规则的代数结果，不是已生成107图的实际验收。若放开matching或允许其他old-old repairs，需要重新写度预算，不能继续借这份具体参数的结论。

## repair边能且只能直接修好哪些旧点对

先在D=H−F5中考虑添加a-k。除直接修复a/k这一对以外，它提供的两步路恰为

    a—k—v,  v∈N_D(k),
    k—a—v,  v∈N_D(a).

所以添加一条old-old edge只能新增“至少一个端点是a或k”的长度≤2旧点对覆盖。它不能修复两个端点都不在{a,k}的旧点对，也不能因为邻域规模看起来大就声称覆盖完整。新边的作用必须对保存的critical PAIRS判断，不能只拿required vertex union计数。

具体地，删除a-b使a丢失的某个critical目标v：若v=k，repair直接连通；若k-v仍是D的旧edge，repair给a-k-v两步；若两者均不成立，a/v还未被这条repair修好。对删除k-l所破坏的k端点义务同理：新邻居a只补N_D(a)内的目标。删除多个边可能另外破坏原本有多个common neighbors的点对，不能只并合单删profiles便声称已完成全部旧旧验证。

## H0的a/k提前必要筛严格成立

root当前先检H0中a及k是否仍在两步内覆盖全部106旧点，是一个有效的必要门。以后仅再删F3，旧点间已有edge和common-neighbor集合只能减少；唯一新增点z又不邻接a或k，所以z不可能成为a/v或k/v的共同邻居。若H0中a到某旧v距离>2，则任意后续F3/S都不能补救该点对，k同理。

这个筛通过并不充分：后续F3可能删除a/k的旧两步路线；其他旧旧点对也可能损坏，新z自身还必须覆盖全部旧点。因此最终仍需下面的exact义务，不能把“两个anchor根通过”当作107图D2。

## 一个保存数据已足够判断的预测，不运行手工trade

作为必要筛的纸面sanity case，取(a,b,k)=(64,0,7)，不指定或搜索l。实际保存的edge0-64 profile为

    u=0:  unique_via64 targets [34,67],
    v=64: unique_via0 targets [5,7].

添加64-7直接修好旧对{64,7}。但source邻接必要行

    N_H(7)={0,17,35,46,54,62,86,87,93,98,105}

不含5。因此删除64-0后失去的{64,5}不会由64-7-5修好。再删7-l只会去掉路线。由于64按此规则不接z，最终也不能经z两步到5。

**可被当前实际anchor筛核对的精确预测：所有(a,b,k)=(64,0,7)的l分支都必须因旧对{64,5}拒绝。** 这是从已保存critical profile与一个邻接行推出的纸面必拒例，不是新的候选图实验。它展示了old-old repair确实修好一个被K阻断的点对，同时会留下另一项不能用同一个repair补的义务；不能只看到“选中了强迫K”就判成功。其他anchor不由此一例排除。

## 完整107点D2的exact补边义务

给定实际F5和S，定义Q=H−F5+{a-k}。在上述simple/degree/label条件下，G精确满足D≤2，当且仅当：

1. 新旧点对全部覆盖：对每个旧v，v∈S或N_Q(v)∩S非空，即S的闭1邻域为全部106旧点。这里用删除/repair之后的Q，不用原H距离掩码冒代。
2. 对每个不同旧u,v，至少一项成立：Q中u-v直接相邻；N_Q(u)∩N_Q(v)非空；或u,v都在S。最后一项才是新z能修复的旧旧点对。

这两个条件是exact，不只是充分模板。它明确把repair边负责的a/k路线、新z负责的S×S路线、以及必须保留的其他旧common-neighbor路线分开。G中不存在其他新点或其他新old-old edge，所以没有被遗漏的长度2路线类别。若D≤2成立，107点最大度≤11不可能是完全图，因此实际直径恰2。

本scope中a/k不在S，故其点对只能靠Q；新点不能掩盖它们的旧路损坏。对不在S的其他旧点同理，最终common-neighbor检查需要完整，不能只查profiles中曾经唯一的源两步路。

## 当前最小问题及停止边界

暂不指定一套未经测量的F3。第一项最小不确定性，正是root授权的所有有据anchor H0是否有a/k完整2hop通过者。通过时保存具体(a,b,k,l)、它真正修好的critical pairs与仍必须进入S的目标，再在同一既定批次考虑三条matching的exact义务；不是先随手给出107图、再逐点修坏对。

若所有anchor被这个必要门拒绝，严格关闭的只是“5matching删除＋1条old-old repair＋1个10度新点、repair端点不接新点”的规则。它比旧minimal4范围更宽且确实修改旧边，但仍不是所有old-old修复或一般107/D2图的排除。用户希望改造现有图的方向没有被这两个局部负结果否定；本note不据此自动停止整个D2，也不擅自再开另一种repair、solver、timer或新模板。

原始入口均在本case：SOURCE_RESULT.json、CRITICAL_EDGE_PROFILES.json、MINIMAL4_FORCING_CERTIFICATE.json、source106.author.adjlist.txt及root/gq当前M5必要门。未重写旧证据、root计数或Wiki。

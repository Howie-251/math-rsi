# 全域centre失败的范围：任意六端点2+2+2配对均被排

状态：仅paper scope校正，0数值、source/矩阵/BFS读取、field、Lean、ARIS或Wiki写入。使用root已实际接受的global终态：锚定的全部1743779三matching-cut参数均在**centre门**失败；并非有些靠leaf门才失败。

## 与leaf分组无关的exact距离

仍固定同一Conder1250源G，删三条两两顶点不交的旧边F，令T=G−F，P为其全部六个不同端点。任意把P分成三个无序2点集P0/P1/P2，各接一个newleaf，centre c只接三个leaves，helper图仍K1,3。

对任何旧target t，centre到最后出现的leaf的prefix至少1步；其后要出一条spoke，再在T中行走。因此任何路线长至少

    2+min_i d_T(Pi,t)=2+d_T(P,t)。

反向直接c→对应leaf→最近pin，再接T路径即可达到此长度。因此即使允许重复进出helper/base，精确有

    d_final(c,t)=2+d_T(P,t)。

F每条边的两端都在P，从P到t的最短G路不能使用任何F边：若使用，可从该边后一端重新起步得到更短路。因此

    d_T(P,t)=d_G(P,t)，
    centre闭R10覆盖全部old iff R8_G(P)=V(G)。

这个条件只取决于三条旧cut及其六端点P，完全不依赖六端点怎样分成三组。

## actual global NO的正确推论与计数

root实际全域中，每个cuttriple都有 `R8_G(P)≠V(G)` 的centre反例。因此同一target对该cuttriple的**任意**2+2+2分组都使centre距离>10。每个六端点集合有15种unordered pairings，原whole-cut配对只是其中一种；它们现在被同一个分组无关的必要门同时排除。

数值visited仍是 **1743779个anchored matching-cuttriples**，没有另枚15倍图或新增参数。扩大的结论来自这一paper deduction，不冒作又执行了约2600万候选/BFS。source edge-transitivity仍把任意三matchingcuts送到该锚定域，并将任意端点partition送到相应partition；新candidate不需vertex-transitive。

因此当前严格No范围是：**固定source、删任意三条disjoint旧边、用其全部六端点各一次、任意分成三对接三leaf、再加只连三leaf的centre（K1,3），不作其它修改。** 所有旧点和四newhelpers仍3度、1254/1881，但D≤10不可能。

## 保留原positive公式的范围

`STAR_ROUTE_PAPER.md`/`GLOBAL_DOMAIN_PAPER.md`中的leaf weighted-G公式和E9/E7精确门，仍只在“每条旧cut完整两端同归一leaf”的先前已证明范围使用。不能因centre扩scope而将那些leaf式套到跨cut配对；本更强negative只用centre，完全无需跨配leaf公式。

不扩到shared-endpoint cuts、P4或其它helper拓扑、更多cuts/oldoldrepair、其它source或一般(3,10)。这不是新独立方法、新数值批、图/参数/Lean成果；完成scope校正即停止。

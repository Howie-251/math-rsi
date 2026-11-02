# forced pin-cover 枚举的完备性与最终排除范围

本证明只读既存结构、critical证书、搜索源码和终态，不重算A²/A³，不重枚候选，不运行图或 BFS。源为 d3d4_transfer/source650.implicit_adj.txt，实际650/3250全10正则，公开D3继承。

## 1. 最大端点邻集的无损化与前置排除

记 C 为删除的至多五条源边，S(C) 为全部不同端点。允许新hub只连其中一个子集时，可以无损地补齐到S(C)：每个端点至少失去一条旧边，补一条spoke后度≤10；|S(C)|≤10，新hub也不超度数。补边只缩短距离。因此完整检查“hub邻全部端点”足以排除所有端点子集。源全10正则，未删边的点也没有额外oldpin槽。

没有FF cut时，已有结构证明给 |R2(S)∩P|≤5·24=120<130，新根不可能三步覆盖全部P。有FF cut时，所有FF critical图的实际matching至少7。对于锚uv，u/v不属于critical图，S\{u,v}必须cover它，故|S|≥9。删≤4条边只有≤8个端点，也不可能。matching9的1952条FF边进一步要求≥11个端点，均已禁止。

因此任何幸存者都必然恰删五条边，含至少一条128条matching7或8的FF锚，且完整端点集S大小只可能9或10。以全部128条边分别作锚可能重复，但不遗漏任何候选。

## 2. 为什么 L子集+强迫R 穷尽全部 S

对一个锚uv，L=N(u)\{v}，R=N(v)\{u}，critical二部图记B。共同物理顶点只能对应孤立row/column：否则会有两步旧路，不能是distance3的criticalpair。所以B中的matching7/8也是实际旧点互异的matching，vertexcover下界可按真实顶点数使用。

枚举所有L子集X，定义

Y=N_B(L\X)，C0=X∪Y。

这里N_B必须是critical图邻集，绝非源图邻集；X、Y按真实old IDs取并去重。C0自动cover全部critical边。大于8者不能属于S\{u,v}，小于7者由实际matching下界不存在。

反之，取任意可能候选的C=S\{u,v}，|C|为7或8。令X=C∩L，则所有未选L的critical邻居都必须在C中，所以Y⊆C，C0⊆C且|C0|≥7。因此只有：

- |C0|=8：C=C0，直接得到S10；
- |C0|=7：得到S9；若实际C有8点，则只差一个任意oldvertex，遍历所有不在S9中的旧点即可得到该S10。

故7-cover后的extra必须允许全部其余旧点，不可只限L∪R。源码确实遍历0..649，且每个anchor内按真实S集合去重。matching8的锚只有8-cover；matching7的7/8两种均保留。这样穷尽全部必要pin sets，而非对某个matching选一组端点。

## 3. 源R2 gate与实际新根条件

所有cut都在S内部。对任意旧点t，从集合S出发的最短源路径可以选成除了起点以外不再访问S；否则从最后一个S点重新开始会更短。因此它不使用任何S内部cut：

d_(G-C)(S,t)=d_G(S,t)。

新hub z 的最短路径出发后不需再次经过z，故

d_new(z,t)=1+d_(G-C)(S,t)=1+d_G(S,t)。

所以完整sourceR2(S)=V不只是松必要条件，在此full-endpoint模型中也是精确的新根D3条件。该gate不能证明全部旧旧对仍D3。

## 4. 五边端点实现的完整类型

S10中五条simple cut边覆盖十个顶点，所有cut-degree都必须为1，故必为五边perfectmatching。固定已选锚后，枚其余八点的全部perfectmatching即可。

S9中五条边的cut-degree总和10，九个顶点各至少1；所以恰一个点cut-degree2，其余点degree1。cut graph因此恰为P3加三条独立P2。枚全部P3中心与两条不同腿，再匹配余六点，穷尽其实现。锚既可能是P3一条腿，也可能是独立P2；源码允许两类，不强迫锚在P3中。

每条可能cut e还要求S vertex-cover其旧critical图；这是必要过滤。多个删除可能共同破坏原本有多条短路的旧点对，所以逐边criticalcover并不充分。只有真正实现出的改图再进行全部651根R3检查，才能给出完整D3成功。当前没有任何实现通过必要过滤，故无需改图BFS。

## 5. 实际终态与可以关闭的范围

[RESULT.json](RESULT.json) 为complete=true、hit=false、CPU0.035215秒：

- 128条FF锚全部处理；
- 4个size7、274个size8 cover生成项（跨锚计数）；
- 每锚内部去重后2820项(anchor,S)，不声称全局不同S有2820个；
- 260项完整sourceR2通过；
- 含锚且每条cut均被S cover的五边端点实现为0；
- 实际改图与BFS为0，无未试项或UNKNOWN。

结合第1节，这严格关闭当前650源上“删除≤5条任意旧边，其余旧边保留；加入一个hub并接任意合法端点子集，无其它新增边”的整个规则。不是只测五条disjoint edges。没有实际651图，因此actual_n/actual_D/普通无序坏对为空。

此结论不排任意651点图，不排其它source、删除六条以上但复用端点、增添其它旧旧边或多个helper。未被首轮criticalmatching禁止的边也没有被称为安全删边。

证据：[初始结构](../STRUCTURE_ROOT.json)、[实际critical结果](../RESULT.json)、[128锚接口](../UNEXCLUDED_FF_EDGES.json)、[搜索源码](search.cpp)、[本批终态](RESULT.json)。本独立paper核对新增数值枚举/图/BFS/solver均为零。

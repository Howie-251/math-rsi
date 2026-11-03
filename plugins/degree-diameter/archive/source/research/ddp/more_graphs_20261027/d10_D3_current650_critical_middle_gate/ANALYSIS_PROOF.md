# (10,3)650：critical-middle 与 P 覆盖的条件性定理

初始“全部FF都被matching9禁止”的条件未被当前source满足。实际1952条FF边被禁止，另128条仍需处理。下文的条件定理、24/12界和matching论证有效；完整≤5cut族现由后续 [forced-pin枚举证明](forced_pin_cover_search/ANALYSIS_PROOF.md) 关闭。

本文件只核数学逻辑，不枚边、不算球、不 BFS、不构图。实际数据由唯一 producer/Root 提供；源650公开D3继承，不重复旧全源 BFS。

## 固定操作与待验条件

在给定650点源 G 中，删一个最多五条旧边的集合 C，加入新 hub z，令 z 的邻集 S 为这些边的全部不同端点。因此 |S|≤10；不另加旧旧边或 helper，不要求所删边是 matching。所问只是这个固定源和操作能否给651点、最大度10、D≤3。

条件为：

1. V=P⊔F，|P|=130、|F|=520；每个顶点恰有8个F邻居和2个P邻居。
2. P 上有无不动点配对 p↔p*，且 NF(p)=NF(p*) 为相同的8个点。每个 f∈F 的两个P邻居正是某一对 p,p*。
3. 对每条FF边 uv，其下面定义的 criticalpair graph 有9条真正端点互异的 matching。

以下结论均以这些条件实际成立为前提。

## 1. criticalpair graph 给每条 cut 的 pin-cover 条件

对旧边 uv，取 L=N(u)\{v}、R=N(v)\{u}。在 p∈L、q∈R 之间放边，当且仅当旧 dG(p,q)=3，且唯一三步路径是 p-u-v-q。

若 uv 被删，G-C 中已无该对的三步以内路径：原距离为3，原唯一三步路径又已断。任何新图中的替代路径都必须使用 z。若 p,q 都不在 S，则经过 z 的路径至少四步，因为进入与离开 z 的两条 spoke 之外，两端各至少还要一条旧边。所以 S 必须 vertex-cover 每条被删边的 criticalpair graph。

共同邻点不会伪造 matching：若 t∈N(u)∩N(v)，则将 t 作为 L-row 时，t-v-q 已长≤2；将其作为 R-column 时，p-u-t 已长≤2。故相应 critical row/column 必为孤立。特别地，若9×9 critical graph有perfectmatching9，则活跃左右端点没有跨侧重合，这9条边就是18个不同实际旧点的matching，不只是 bipartite-copy 意义上的matching。

同时 u、v 不属于 critical graph 的任何顶点，而 u,v∈S，因此 S\{u,v} 至多8点，不能 cover 一个9-edge matching。这说明有上述证书的FF边不能出现在任何成功的 cut集合中。只用源中的旧 critical paths 即足够，不需逐 cut-set 重算距离。

## 2. 从局部 P/F 配额推出22、24、12

以下 R2 均为源 G 中闭球（距离≤2），不是恰好距离二。

对 f∈F，R2(f)∩P 的来源只有：

- 自己的两个P邻居：至多2；
- 八个F邻居各自的两个P邻居：至多16；
- 自己两个P邻居各自的两个P邻居：至多4。

所以 |R2(f)∩P|≤22。各来源的重合只能降低此上界。

对 p∈P，经任何F邻居再到P只能得到 p 或 p*。沿 G[P] 的闭R2至多给 p、两个P邻居、两个非回退P第二邻居，再加 p*，故 |R2(p)∩P|≤6。

若 fp 是FP边，f的闭R2已含 p、p* 及全部 NP(p)。R2(p) 可能额外提供的P只有上述两个非回退P第二邻居。因此

|(R2(f)∪R2(p))∩P|≤22+2=24。

这个“最多额外2”不需要假设 G[P] 是长圈，也不把两球总数直接相加成28。对PP边，简单地各端≤6即得两端并≤12，已足够本问题。

## 3. uniform cut-set 障碍

若候选删了FF边，第1节已经给出一个不可在三步内修复的旧旧点对。

否则全部 cut 都是FP或PP。S 是最多五条 cut 的端点并，所以按第2节

|R2_G(S)∩P|≤24·#FPcut+12·#PPcut≤120<130。

删边只能使距离不减。新hub要在三步内到达全部旧点，至少必须有 R2_G(S) 覆盖全部P；这已不可能。于是没有FF cut时，新根至少漏10个P目标；该数量是对假设族的必要覆盖下界，不是实际生成图的普通无序坏对统计。

所以一旦全部待验条件被数据支持，这个固定源上“删≤5条边并以端点接一个hub”的整个操作被排除。两种分支合起来不要求 disjoint cuts，也不依赖挑一个最优 cut-set。

## 适用范围与未验事项

本定理不排一般651点图、删六条以上但端点重用的操作、其它source、其它旧旧新边或多个helper。这里没有任何候选边表、actualD或全图坏对；不能给假设651图填实际直径。

可被实际数据反驳的预言与条件见 [ANALYSIS_PREDICTION.json](ANALYSIS_PREDICTION.json)。当前状态为 PAPER_VALID_CONDITIONAL_ON_SOURCE_STRUCTURE_AND_CRITICAL_CERTIFICATES；实际统计到位后才可把这个条件定理绑定到 source650。


## 实际结构绑定进度：条件1、2已验证，FF证书仍待定

Root 的 [STRUCTURE_ROOT.json](STRUCTURE_ROOT.json) 已确认当前literal650/3250具有130个P、520个F、65个配对，完整8F+2P配额及twin-star关系成立。实际边数FF2080、FP1040、PP130；P闭R2与P交全部为6，F为19..22，endpoint球并的实际最大值FP24、PP8（后者比本证明所需12更紧）。

这些既存数据支持第2节上界及其源绑定；本分析没有重复算球或读源邻接。还不能将整个≤5cut族标为关闭：只有全部2080条FF边的criticalmatching9证书到位后，第3节的两分支论证才完整。当前整体状态保持条件性，不填写actualfamilyclosed=true。


## 后续实际critical结果与完整封口

实际FF2080中有1952条matching9、126条matching8、2条matching7，首个不满9为(1,9)。FP1040、PP130的criticalmatching均为零。因此本文件初始“若全部FF为9”的统一分支不能直接应用，120<130本身也不能关闭含剩余128条FF的情况；这些128条只是未被此必要条件禁止，并非安全cut。

后续完整 [forced_pin_cover_search/RESULT.json](forced_pin_cover_search/RESULT.json) 处理了全部128锚：4个size7与274个size8 cover生成项，锚内去重后2820项(anchor,S)，260项完整sourceR2通过，却没有任何含锚、逐cut满足criticalcover的五边端点实现。因此在下述完整枚举证明下，最终关闭固定source的≤5cut单hub规则。没有生成651点图或运行改图BFS；不能把此结论外推一般651点图。

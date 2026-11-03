# (14,3)1141 的 balanced vertex split：路径引理与完整拒绝

当前源的全部1141个点都有一个 distance3 target，其所有三步 geodesic 只从同一个首邻居出发。因此本次固定操作“把一个旧点拆为相邻两点、旧14邻集按7/7分配”全部被必要条件拒绝；没有 colouring、候选图或改图 BFS。

实际统计由唯一 producer 保存于 [RESULT.json](RESULT.json) 和 [VERTEX_FIRST_SUPPORTS.jsonl](VERTEX_FIRST_SUPPORTS.jsonl)。本文只读缓存与核对数学，不重新计算 A²/A³、BFS、word 或图。公开源 D3继承，未使用 Cayley 或 vertex-transitive 假设。

## 1. 操作和收缩映射

给定源 G 与旧点 v，令 N(v)=A⊔B，|A|=|B|=7。删除 v，加入相邻的 vA、vB；vA连A，vB连B，其余旧边保留。新阶1142，两新点degree8，其余旧点仍degree14，最大degree14；若实际生成，边数应为7988，但本轮没有生成该图。

将 vA、vB 都收缩为源 v，记映射φ。每条新边除 vA-vB 之外，都映成一条源边；bridge映成长度零。故任意长度≤3的新walk若使用bridge，收缩后给长度≤2的旧walk。

## 2. 新根到远点的精确条件

设旧 t 满足 dG(v,t)=3，定义

H_v(t)={n∈N(v): 存在一条 v-n-a-t 的源三步 geodesic}。

若从任一新child到t的≤3路径使用bridge，收缩后有旧 v→t 长≤2的walk，与dG(v,t)=3矛盾。因此这样的路径不能使用bridge；它必对应一个首邻居属于该child的H_v(t)路径。反过来，任何此类源geodesic都直接lift到对应child，长度仍为3。因此

d_new(vA,t)≤3 ⇔ H_v(t)∩A≠∅，
d_new(vB,t)≤3 ⇔ H_v(t)∩B≠∅。

两新child到t都达标，恰好要求H_v(t)非单色。若H_v(t)只有一个元素，该元素无论放哪一侧，另一child都不能三步到t，故整个v的所有7/7 partitions被拒绝。singleton support不要求源三步路径唯一，只要求它们的第一邻居唯一。

源 dG(v,t)≤2 的旧target也已被处理：若一条旧短路的第一邻居分到A，则vA直接走长度≤2，vB先bridge再走，长度≤3；第一邻居在B时对称。两newchild之间本身相邻。因此远点H双侧命中恰为“两新根覆盖全部旧target”的条件，而非整个图的D3证书。

## 3. 旧旧点对与same-side条件

旧旧 source distance≤2的点对自动仍≤3：一条旧≤2路径若经过v，最多因跨两child多一步，其余路径完全保留。

对旧旧 p、q且dG(p,q)=3，任何新≤3路径若使用bridge，也会收缩成旧≤2的walk，矛盾。所以所有可能的new≤3路径必须对应旧三步geodesic，并且若旧路径经过v，其两条相邻于v的邻居必须落在同一侧。

特别地，若旧 p、q 有唯一三步geodesic，且它在v内经过相邻的两个旧邻居a,b，则a、b必须同侧。这些 equality constraints 可合并成N(v)上的components；balanced split必须把每个component整体分侧，且两侧总大小7。

这些 unique-path components 只给必要约束。若一个旧点对有多条三步geodesic、全部经过v，则需要至少一条geodesic的邻居pair同侧，是一个OR条件，不能把它误写成所有pair均同侧。更精确地，旧distance3点对被保留当且仅当存在一条避开v的旧geodesic，或存在一条经过v且邻居pair同侧的旧geodesic。新根H条件本身不能取代这些旧旧检查。

## 4. 实际缓存如何完整封口

缓存全图共1,087,886个有序distance3点对；其中357,347个是 singleton-first-support，不是候选图的普通坏对。逐点 minimum support histogram给 min=1 的旧点1141个，其余为零；eligible_vertices_without_singleton为空。

首个见证是 v=0、t=23、H_0(23)={6}。任意7/7分配都只能将邻居6放在一侧，另一child无法在三步内到t。相同证据为全部1141个v逐项保存，故不靠对称性或只查一个代表点。

所以无需展开7/7 colouring、计算old-old equality components或构图，整个本次balanced split族已拒绝。singleton引理本身与平衡大小无关；本条正式实验范围保持为所授权的固定源7/7拆点，不扩成一般1142点图不存在。

## 5. 容量与结论口径

粗新根 Moore 容量为1+8(1+13+169)=1465≥1142；利用bridge partner也只有degree8，可收紧为2+7(1+13+169)+7(1+13)=1381，仍未在容量上排除。这说明选择本参数并非已被简单根容量自动阻断，实际关闭来自 geodesic 首邻互补不足。

本分析没有新增图、BFS、wordscan、source矩阵计算或solver。source实际1141/7987；1142/7988仅是若生成该操作的假设阶/边数，actualmodified_n、actualmodified_D及普通无序坏对均为空。缓存中“critical-middle matching13=0”是另一必要条件统计，不作为本拆点排除的依据，也不自动触发hub搜索。

证据：[本分析字段](ANALYSIS_RESULT.json)、[原cache schema](CACHE_SCHEMA.json)、[producer统计](RESULT.json)、[逐点singleton见证](VERTEX_FIRST_SUPPORTS.jsonl)。

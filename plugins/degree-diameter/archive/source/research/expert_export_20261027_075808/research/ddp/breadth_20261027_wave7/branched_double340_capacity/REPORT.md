# Branched double cover：任意matching最多击中2810条，目标需5130条

## Claim and Status

在固定170点7正则D3基图上，用base-edge matching $B$ 的边连接两端fiber的 $K_{2,2}$，其余基边保留任意Z2 signed单匹配，只对未被 $B$ 覆盖的基点加vertical matching。无论选择哪个 $B$ 及其余签名，340点图都不能达到D3。

状态：PROVABLE AS STATED。该机制真正改变了上次的单parity路径，但matching的覆盖总量不足。

## Assumptions and Notation

源边、唯一三路数据直接读取相邻目录`signed_double340/`的`source.edges`和`distance3_paths.json`，没有重复源BFS。取其中5130个不同的、各仅有一条三路的点对，记这些路径组成集合 $\mathcal U$。关闭结论只需这5130个证书有效，不要求它们穷尽原图全部唯一三路。

定义 $w_e=|\{P\in\mathcal U:e\in P\}|$，以及每个基点的 $m_v=\max_{e\ni v}w_e$。

## Proof Strategy

若D3成立，$B$必须击中 $\mathcal U$ 的每条路径；用逐点最大边权给所有matching统一覆盖上界，避免搜索matching或signing。

## Proof

**1. 度数及必要覆盖。** 基点若被matching覆盖，恰有一个旧邻点的单匹配换成 $K_{2,2}$，每个lift点度数从7增至8，不再加vertical；未覆盖基点保留7条horizontal邻边并加1条vertical，也恰为8。两类fiber内部可分别经branched邻点两步或vertical一步到另一sheet，但这不保证距离2基点对的全部sheet能在三步内到达。

取 $P\in\mathcal U$，端点旧距离为3。任何至多3步的lift路径都不能使用vertical，否则投影最多只有2条旧边。若 $P\cap B=\varnothing$，唯一可用的三步投影沿途都仅有单匹配，因而只到达一个sheet parity，另一个sheet在三步内不可达。因此D3的必要条件是 $B$ 击中全部5130条路径。只击中它们并非本稿宣称的充分条件。

**2. Matching覆盖上界。** 路径被多条 $B$ 边击中时可能重复计数，所以实际击中数至多 $\sum_{e\in B}w_e$。对任意边 $uv$，有 $w_{uv}\le m_u$ 且 $w_{uv}\le m_v$，故 $2w_{uv}\le m_u+m_v$。由于 $B$ 为matching，其端点各至多出现一次，所有权重又非负，得到

$$
|\{P\in\mathcal U:P\cap B\ne\varnothing\}|
\le\sum_{e\in B}w_e
\le\left\lfloor\frac{\sum_v m_v}{2}\right\rfloor.
$$

**3. 明确整数证书。** 从5130条唯一三路逐边计数得到 $\sum_e w_e=15390=3\cdot5130$，最大边权为40。每个matching最多85条边，所以粗界为 $85\cdot40=3400<5130$，已经排除全覆盖。

更细的逐点数据为 $m_v=31$ 共120点、$m_v=35$ 共20点、$m_v=40$ 共30点。因此

$$
\sum_v m_v=120\cdot31+20\cdot35+30\cdot40=5620,
\qquad
\left\lfloor\frac{5620}{2}\right\rfloor=2810<5130.
$$

任意matching至少漏掉 $5130-2810=2320$ 条唯一三路，故D3不可能。每条未击中路径的两个fiber间有两个无序sheet点对必漏，因此该机制每张图至少有4640个无序D3坏对；这是统一下界，不是某个实际图的BFS评分。∎

## Certificate and Scope

`check_weights.py`从保存的唯一三路数据计算所有595个 $w_e$、所有170个 $m_v$，并逐边检查全部 $2w_{uv}\le m_u+m_v$。`RESULT.json`保存完整整数值、每个最大值的取到边、histogram和两项上界，CPU约0.027秒。

root已保存[certificate.independent_check.json](certificate.independent_check.json)：对全部5130个不同pair逐个检查无1/2步路且两个邻集间只有一条crossedge，并据此独立重算595个边权、170个maxima和全部整数不等式。sumw=15390、sum_m=5620、upper=2810全部吻合，CPU约0.0493秒；该检查未重复BFS或搜索matching。这样证书无需依赖原unique枚举的完整性，这5130条已验必需路径本身就足够矛盾。

本次没有搜索matching、signing或MILP，没有生成340图，没有重复BFS。结论只关闭此固定170源、分支边必须为matching、vertical仅加在未覆盖fiber的这一机制；不排除其他分支集合或基图。当前pending为空，无后续队列。

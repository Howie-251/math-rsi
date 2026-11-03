# p0-owner cuts：导出 affine plane 与仅剩 k=1 的必要接口

状态：纸面推导支持。继承实际585源、Steiner block绑定与 [SOURCE585_FOURCUT_PAPER.md](SOURCE585_FOURCUT_PAPER.md)，不修改 [PORT16_RESULT.json](PORT16_RESULT.json) 的历史限定域，不新枚举、BFS、field、候选图、Lean 或外审。

固定 p0=实际顶点0。仍删四条顶点不交的旧 core 边，新点 z 连八个 core 端点及 p0，A\{p0} 加任意 perfect matching M。令 k 为其中具有 p0-owner 端点的 cut 数。旧源中不可能有两个端点都 owner=p0 的 core 边，因此每条此类 cut 有唯一 p0-owner 端点。

## 1. 在 p0 导出 64 点 affine plane

原 block 系统为 Steiner 3-(65,9,1)。取全部含 p0 的 C(b)，删除 p0 后得到 2-(64,8,1)：任意两个其他 A 点与 p0 恰属一个原 block。该 2-design 是 order 8 的 affine plane。

八个 u∈N_G(p0) 的 L_u=C(u)\{p0} 两两不交：若某 a≠p0 同在两块，就会给 p0→a 两条不同旧 3 路，违反 A-root Moore 饱和所给唯一性。它们每块8点，因而 partition A\{p0}，组成一个 parallel class。

若 core cut u–v 有 o(u)=p0、o(v)=a，则 C(u)∩C(v)={p0,a}。所以 T_v=C(v)\{p0} 与 L_u 是两条不同且非平行的 affine lines，交于 a；

    D_(uv)\{p0} = L_u ∪ T_v,   |D_(uv)|=16。

这里不要求任何新 field 坐标，只使用已绑定 design 与源的唯一旧 A–A 3 路。

## 2. 两条 p0-owner cuts 强制额外交叠

取两条顶点不交的 p0-owner cuts u_i–v_i、u_j–v_j。其 u_i≠u_j，因此 L_i、L_j 是该 parallel class 的两条不同线。T_i 非平行于整个 parallel class，故 T_i∩L_j 有唯一一点；同理 T_j∩L_i 有唯一一点。这两点分别落在不交的 L_j、L_i，因而互异，且均在 D_i∩D_j。再加共同点 p0，得到

    |D_i∩D_j|≥3。

这不是把两个不同的交点误算为同一 owner；parallel lines 的不交性正好保证它们不同。

## 3. k≥2 全部排除

记 U 为四个 D-mask 的并。四个 mask 各16点。先合并任意两条 p0-owner cuts，交叠至少3；其余每条 p0-owner mask 至少再次包含已出现的 p0。其余非-owner mask 暂宽松允许完全不交，故

    |U| ≤ 4·16 − 3 − (k−2) = 63−k。

新根三步 A-target 的完整分类仍是

    R3(z)∩A = {p0} ∪ U ∪ M(O\{p0}),

其中 O 是八个 core pins 的 owner 集。因 k≥1，有 p0∈U。每条不含 p0-owner 的 cut 仍强制其两个 owner 互为 matching partner，因此这些 owner 的 mate 已在 U。只有至多 k 个 p0-owner cuts 的另一端 owner 可能有 U 外 mate；若这些 owner 重复，或同时受另一条 cut 的强制匹配约束，只会减少此数。因此

    |R3(z)∩A| ≤ |U|+k ≤ 63 <65。

故 k≥2 的规则全部失败。这一结论不依赖非-owner cut 的 owner 是否彼此重复；忽略冲突是在给候选更宽松上界。

## 4. k=1 的精确必要形状与 owner 重复问题

设唯一 p0-owner cut 为 u–v，o(u)=p0、o(v)=a。其余三 cut 不含 p0-owner，分别强制三对 owner 匹配。至多只有 a 的 mate 能增加 U 外的 A-target。因此要覆盖65个 A，必须同时有：

1. 四个16-mask两两不交，|U|=64；p0 位于第一块，另外三块均避开 p0。
2. 唯一遗漏绝对点 t=A\U 必须满足 M(a)=t。
3. 其余三条 cut 的 owner pairs 必须直接成为 M 的三对。

解释第一项：若 |U|≤63，则加至多一个 U 外 mate 仍不足65。反之，四块总大小64，所以 |U|=64 等价于它们两两不交。该条件也自动排除任意跨 cut 的 owner 重复：每条 cut 的两个 owner 都在自身 D-mask 中；若它们出现在另一 cut 中，两 mask 必交。因此 a 不会又被三条非-owner cuts 强制匹配，六个 forced owners 也互不相同。t 在 U 外，更不可能是任何 forced owner。

在纯 matching 一致性层面，这些条件没有额外奇偶障碍：三对 forced pairs 加 a–t 共覆盖8个 A\{p0} 点，剩下56点可配成28对；A 原独立，故这些新增 matching 边不会与旧边重复。这里仅证明 matching 可以延拓，**不证明延拓后的图 D3**。

所以 k=1 的下一必要门可固定一条真实 p0-owner cut 的16-mask，再问三条真实非-owner core cuts 的16-mask能否与它及彼此不交；必须保持四条 cut 实际顶点不交，并保存唯一遗漏 t 及强制匹配 a–t。任何可行 mask 数据仍只完成新根到 A 的覆盖，不处理 core targets 或旧旧点对。

## 5. 与历史结果的衔接和停止范围

* k=0：固定 p0=0 的 owner-avoiding 域已由 PORT16_RESULT 完整 NO；保留其原始 scope 与成本。
* k≥2：由上面的 affine-plane 交叠与新根 A-target 容量纸面排除。
* k=1：仅剩上述必要接口，当前未执行数值；不能宣称有图，也不能宣称该域 NO。

这不排一般585源重连、其他 old-old repair、一般586/D3或一般(9,3)。不重算旧 fixed-sigma 域，不把本 paper 另计图、参数、独立方法或 Lean 成果。完成纸面接口后停止。

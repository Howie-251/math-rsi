# Actual585：四 core-cut 原型的必要 16-block partition

状态：纸面推导支持下述限定原型的必要门。没有枚举 cut、匹配或候选图，没有新 BFS、field、源 D3 验收或 Lean。实际源与字面标签继承 [SOURCE585_READ_GATE.md](SOURCE585_READ_GATE.md)，下一有限门以 [PRED.md](PRED.md) 为准。

## 1. 固定原型及度数账

继承的实际源 G 有 585 点、2600 边，分为独立绝对点集 A（65 个、各度 8）与 core B（520 个、各度 9）。每个 b∈B 恰有一个 A 邻点，记为 o(b)，另有八个 B 邻点。固定 p0∈A；本门 p0 是实际顶点 0。

删四条顶点不交的 B–B 边 e_i=u_i v_i。令 P 为八个 core 端点。新增 z，邻接 P∪{p0}；另给 A\{p0} 加一个 perfect matching M。不作其他改动。**本原型额外限定每个 p∈P 都有 o(p)≠p0。**

每个 core pin 删一边、添一边；其余 core 不变。p0 添 z，其余 64 个 A 点各添一条匹配边；z 度 9。因此候选为 586 点、2600−4+9+32=2637 边、全 9 度。A 原独立，所以匹配不会重复旧边。该度数账不证明 D3。

## 2. 唯一旧 3 路强制每个 cut-owner pair 被匹配

任意 a∈A 的根 Moore 上界为 1+8+8·8+8·8²=585，且实际源 D3，故此界饱和。相异 A 点之间距离为 3，且其旧 3 路唯一。对旧 core 边 u–v，记 a=o(u)、b=o(v)。有 a≠b，且 a–u–v–b 正是这一唯一旧 3 路。

在本原型 a,b≠p0，因此删除 u–v 后，任何经 z 的 a→b 路至少长 4：a、b 都不直接邻接 z。长度至多 3 的路若使用新增 A-matching，则也不能连接任意不同于 mate 的两个 A 点：两个相异 A 在旧图没有长度 ≤2 的路；两个 matching 步立即回到原点，三个 matching 步仍只到 mate。因此 a,b 要保持距离 ≤3，必须有 M(a)=b。

每条 cut 都强制其 owner pair 成为 M 的一对。若不同 cut 对同一 owner 提出不同 partner，候选立即不可能。反过来，本必要结论不是全部旧旧距离的充分条件。

## 3. 新根到 A 的所有三步路线

令 C(p)={a∈A : d_G(p,a)≤2}。继承实际 BLOCKS：每个 C(p) 有 9 点，520 个不同 block 构成 Steiner 3-(65,9,1)。令 O={o(p):p∈P}，U=⋃_{p∈P} C(p)。

因为所有删边的两端都在 P，从 P 出发的最短距离不变：任何经过某条删边的最短 P→target 路，可以从该边的后一端重新作为起点，得到更短路。因此 d_(G−cuts)(P,x)=d_G(P,x)。这仅用于此八 pin 的并集，不宣称每个单独 pin 的 C 都不变。

从 z 到 A、长度 ≤3 的路线恰只能给出

    {p0} ∪ U ∪ M(O)。

这里 z→core pin 后的两步旧路给 U；z→core pin→owner→mate 给 M(O)。z→p0 后的两步旧路只可回到 p0，p0 没有匹配边。经 z 的重复步也不产生别的 A 端点。

第 2 节的强制匹配使 M(O)=O，而 O⊆U，故该原型实际有

    R3(z) ∩ A = {p0} ∪ U。

匹配不能补上 U 外的新绝对点。

## 4. 每条 cut 给 16-mask，四 mask 必须精确分割

对 core 边 u–v，两个 owner a,b 同时属于 C(u)∩C(v)。Steiner 3-design 的不同 block 不可能有三个公共点，故

    C(u)∩C(v)={a,b},   |D_e|=16,   D_e=C(u)∪C(v)。

于是四条 cut 的 U=⋃_i D_(e_i) 至多有 64 点。要令 z 三步到达全部 65 个 A，必且就 A-target 而言充分的是：

* 每个 D_(e_i) 避开 p0；
* 四个 16-mask 两两不交，恰好 partition A\{p0}。

因此先筛 C(u)、C(v) 都不含 p0，再做四块 exact cover，是本原型不丢解的必要过滤。若 owner 均非 p0，但 p0 仍出现在某个 C block 中，则 p0∈U，覆盖至多 64，严格失败。mask partition 若通过，仍须使用实际四条顶点不交的旧 core 边；不能以相同 mask 的抽象对象代替字面 cut。实际 source 的原始 labels 与 block compressed indices 须由已有绑定保持一致。

该门仅处理新根到 A 的必要条件。新根到 520 个 core、全部旧旧点对，以及剩余匹配如何选择，均未由此证明；partition 成功不等于存在合法 586/D3 图。

## 5. 不能外推到 p0-owner cuts

若某条 cut 的 owner 是 p0 与 a，则原受损 pair 可由 p0–z–v–a 三步修复，不能强制 M(p0)=a（p0 本来就不匹配）。a 的自由 mate 可能在 U 外，经 z–v–a–M(a) 提供额外覆盖。因此一般四 cut 规则的 z→A 集合仍须保留 M(O)，不能只用 raw 72−4·2=64 排除。**含 p0-owner 的规则保留 OPEN；本文件的 partition NO 若发生，只关闭所限定原型。**

## 6. 旧 fixed-sigma 子域与新 exact-cover 域

旧 fixed-sigma 32 边子域的完整 NO 可继承，不能冒作全部 2080 条 core 边的 NO。新的 unrestricted-edge 门必须保留每条旧 sigma 边及其与非-sigma 边的混合组合。仅当四条所选边全部落入已完整排除的同一旧 sigma 子域时，才可跳过该完整四元组；不得删除单条 sigma 边或一切包含 sigma 边的组合。新完整域负结论也只覆盖固定 p0、owner-avoiding 的本原型。

纸面结论：支持执行该有限必要门；不运行数值，不新增图、参数、方法或 Lean 成果。

## 7. 随后实际门的终态（只读回执）

数值 owner 的 [PORT16_RESULT.json](PORT16_RESULT.json) 已返回完整 NO：从全部 2080 条实际 core 边导出 1568 条 eligible 边，涉及 448 个 core、其 eligible 度均为 7；保留 32 条旧 sigma 边参与混合域，3697 个 DFS 状态完整结束、无 partition、无预算截断。旧全四 sigma 子域继承而未重跑。该回执 wholecase 为 1.881081201/20 CPU 秒，0 新 BFS、core-R2、匹配、候选图或 solver。本文件仅只读引用，不独立重算此枚举。

由第 1–6 节，实际负结论严格关闭 **p0=实际顶点 0、所有 cut-owner 避开 p0 的四 core-cut 原型**。它不关闭含 p0-owner 的 cut、其他 p0 选择、其他旧旧 repair 或一般 586/D3；停止当前原型，不自动继续换 p0 或匹配搜索。

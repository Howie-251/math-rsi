# k=1：新根 core 门与剩余 matching 的精确接口

状态：纸面推导支持；0新数值、field、BFS、solver、Lean或外审。沿用 [OWNER_P0_NEXT_INTERFACE.md](OWNER_P0_NEXT_INTERFACE.md) 的实际源与 k=1 必要形状，不修改已有数值结果。

令 G 为实际585源，A/B 为其65个绝对点/520个core，F 为四条顶点不交 core cuts，H=G−F。新根 z 的邻集 P 是八个 core cut端点加 p0。M 是 A\{p0} 上的 perfect matching；最终图 J=H+M+{zp:p∈P}。本文件中所有 H 距离或 H 的两步 A-target 集都按**删边后**的 H 解释。

## 1. 新根到 core 的覆盖与 M 无关

任何 z→B、长度≤3的路均不能使用 A–A matching：从 z 的唯一 A 邻点 p0 出发不能接 matching，因为 p0 未匹配；从 z 的 core pin 先到 A-owner 再走 matching，第三步仍在 A，尚未到 core。重复经过 z 不增加可达 core。

因此精确有

    R3_J(z)∩B = {b∈B : d_H(P,b)≤2}
                 = {b∈B : d_G(P,b)≤2}。

最后一个等式成立，因为每条删除边的两个端点都在 P：一条最短 P→target 路若经过删除边，可从其后一端重新起步，故删去这些 P 内部边不改变到 P 的最短距离。这是**pin-set 的最小距离**结论，不是各单独 pin 的距离都不变。

具体旧步类别是：p0→core（可再走一步 core–core）；core pin→core（可再走一步 core–core）；core pin→A-owner→同 owner 的另一个 core，以及长度0/1的退化情形。它们的并就是上述旧 B2(P)∩B。

若一个 A-mask packing 通过却遗漏 core b，则在固定这四 cuts、p0 和八 pins 后，选择其余56个 A 点的 matching 不能修复 z→b。经 matching 的相关路线最早为 z–corepin–owner–mate–core，长4。要补该缺失必须改变当前 pin/旧边数据，不能把它交给剩余 matching 选择；本文件不另派这样的规则。

## 2. 长度≤3路线的互斥分类

对两个旧顶点 x,y，任何长度≤3的最短路属于以下之一：

1. 完全在 H 中；
2. 经过 z，因而使用两条 star 边，剩余旧步总数≤1；
3. 使用恰一条 M 边，其两侧 H 旧步总数≤2。

第2类不能同时使用 M：唯一可能把 matching 边紧贴 star 的 A 端点是 p0，但 p0 未匹配。第3类也不能有两条不同的 matching 边：连续两个 M 步立即回退；若两条不同 M 边之间只有一个旧步，该旧步须为 A–A，而 H 的 A 独立。三个 M 步只反复同一对，并无额外短路。

令

    Base(x,y) := [d_H(x,y)≤3]
                  OR [d_H(x,P)+2+d_H(y,P)≤3]。

则精确有

    d_J(x,y)≤3
    iff Base(x,y)
        OR 存在 {a,b}∈M，使
           d_H(x,a)+1+d_H(b,y)≤3
           或 d_H(x,b)+1+d_H(a,y)≤3。

这是旧旧点对检验的充分且必要分类。star 类中的旧腿也必须是 H 旧腿；不能在 Base 中暗自使用 matching 后的距离。

## 3. 三种旧旧类型给 matching 的约束

只需对 Base 为假的旧点对加入约束；Base 为真的点对已覆盖。

### B–B

对 core u,v，matching 路必须有一条旧 owner 边作为两侧各1步，不能再加旧步。因此精确修复条件是

    M(o(u))=o(v)。

owner 边均未被 F 删除，因为 F 只含 core–core 边。若 owner=p0，则该侧无 matching，不能用此类路线修复。相同 owner 的两个 core 本来就有 H 中的2路，故不会成为 Base-false 的待修点对。

### A–B

对 a∈A、b∈B，定义实际删边后的

    C_H(b)={c∈A : d_H(b,c)≤2}。

matching 路必须从 a 直接走 M，再以至多2条 H 旧边到 b：源 A 之间没有长度1或2的旧路，而 b 到某个 A 至少需1步。因此精确修复条件是

    a≠p0 且 M(a)∈C_H(b)。

这里不能盲用旧 C_G(b)。例如 b 为 cut端点时，原来 b–另一端–其owner 的两步路径可能已被删掉。pin-set 的最小距离不变引理不适用于这个单独 b 的 C_H。若 a=p0 且 Base 为假，则当前规则立即失败，余下 matching 无法补。

### A–A

对相异 a,b∈A，H 中不同 A 的旧距离至少3；故一条长度≤3的 matching 路只能直接使用 M(a)=b。特别是

    Base(a,b) 为假 ⇒ 必须直接匹配 a,b。

若任一端是 p0，此要求不合法，因而该 Base-false pair 直接排除候选。k=1 的三条非-owner cut 强制三对 matching；唯一 p0-owner cut 的旧 owner-pair 则由 p0–z–corepin–owner 三步覆盖，不强制错误的 p0 matching。

## 4. k=1 固定部分与剩余56点问题

若四个16-mask互不相交，设唯一 p0-owner cut 的自由 owner 为 a，唯一遗漏绝对点为 t，则新根到 A 的覆盖强制 M(a)=t；另三条 cut 强制三对 owner pairs。八个非 p0 绝对点因此已有四条固定 matching 边，剩下56点待匹配。

mask 不交自动保证上述 owners 不重复、t 在全部 masks 之外，故固定部分匹配一致。对涉及固定 mate 的 Base-false 旧点对，可直接代入上节条件；它们若失败，不能通过剩余56点挽救。其余约束是：B–B/A–A 的指定 mate，A–B 的 mate 允许集合，并须同时形成剩余56点的 perfect matching。多个约束须取交，不能逐点对各选一条互不一致的 mate。

这给出一个**精确的有限 matching 可行性接口**，但当前未生成或求解它。若未来固定 cut 数据满足新根 A 与 core 覆盖，且某同一个 M 满足全部 Base-false 点对约束，则所有最终点对均距≤3；反之任何此规则的 D3 图都必须满足这些约束。不能把“每类存在某个可用 matching”冒作存在共同 M。

结论：先前 A-packing 是必要前置门；固定 packing 的新根 core 门完全独立于 remaining matching；随后必须使用 H 的实际旧腿进行一致的全旧旧约束检验。完成纸面接口后停止，不启动 solver、重建 core-R2 或候选 BFS。

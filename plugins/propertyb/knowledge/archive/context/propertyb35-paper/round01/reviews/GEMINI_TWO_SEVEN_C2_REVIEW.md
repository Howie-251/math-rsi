# 原始模型回应

### 20点、35边、$\delta=7$、恰两七度点且共度二（$r_7=2, c=2$）分支的独立静态审阅

**审阅范围与结论：** 本次对 [DELTA7_R2_C2_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/DELTA7_R2_C2_PROOF.md)、[C2_STRUCTURE.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/C2_STRUCTURE.md) 以及独立复算代码与证据 [replay_a4.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/replay_a4.py)、[replay_mixed.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/replay_mixed.py)、[replay_c2_structure.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_c2_structure.py)、[SELECTION_MAP.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/SELECTION_MAP.json)、[A4_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/A4_REPLAY.json)、[MIXED_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c2_selection/MIXED_REPLAY.json) 执行只读静态数学核查（未重新运行脚本，依赖已有独立重放证据与项目的条件排列／真实坏对配额及弱对偶一般引理）。**在该条件接口下，本分支从实际输入 $H$ 到六类 $Q$ 点归约、双星匹配上界、四种解析选点分流及五/六锁域恢复的逻辑链完整严密，未发现隐藏假设、漏选情形或包含排除计数错误。** 本结论仅覆盖 $v=20, M=35, \delta=7, r_7=2, \lambda(x_1,x_2)=2$ 这一具体子支，不声称整个 20 点 $\delta=7$ 或全局 $m(5)\ge 36$ 已闭合。

---

### 核心覆盖与推导步骤核查

1. **实际 $H$ 的全局预算与 $Q$ 内 $w=1$ 点的完全排除（六类 $Q$ 点归约）：**
   - 设 $x_1,x_2$ 为仅有的两个 7 度点，$\lambda(x_1,x_2)=2$。其余 18 个外点度数 $\ge 8$，总度数为 $175-14=161$。记 $Q$ 为 8/9 度外点集（$q=|Q|$，其中 9 度点 $b_9$ 个），其余 $18-q$ 个高外点度数 $\ge 10$，总超额度数 $e=\sum_{u\notin Q\cup\{x_1,x_2\}}(d(u)-10)=161-8q-b_9-10(18-q)=2q-19-b_9\ge 0$，准确给出 $q\ge 10$ 及 $b_9\le 2q-19$。
   - 每个低点对全体 18 个外点的共度盈余为 $(4\times 7-19)-(\lambda(x_1,x_2)-1)=9-1=8$，故 $\sum_{u\notin\{x_1,x_2\}} w(u)=16$（其中 $w(u)=\lambda(x_1,u)+\lambda(x_2,u)-2\ge 0$）；两条 $x_1x_2$ 共边各含 3 个外点位置，故 $\sum_{u\notin\{x_1,x_2\}}\tau(u)=6$。
   - 经双锁（共度 $\ge 4$）与三锁（$\lambda(x_1,x_2)=2$ 且低外共度含 $3$）严格排除后，$Q$ 中每点满足 $w(u)\in\{0,1,2\}$。由 $q\ge 10$ 与 $\sum_Q w(u)\le 16$，集合 $T=\{u\in Q: w(u)\le 1\}$ 必满足 $t=|T|\ge 2$。
   - 在 $\{x_1,x_2\}$ 加两名 $T$ 点与一名 $Q$ 点的共同三视图五锁域（1068 轨道，1030 严格，余 38 残型）中，$T$ 三元组仅允许 $\{AAA,AAB,AAC,AAD,ABC,CDF,DEE,DEF\}$，两 $T$ 加一 $w=2$ 点仅允许 $\{AAZ_8,AAZ_9,ABZ_9,ACZ_9,ADZ_9,BBZ_9,DEZ_9\}$。
   - **排除 $E,F$（$w=1$）：**
     - 若 $t\ge 4$ 且含 $x_0\in\{E,F\}$，则 $T\setminus\{x_0\}$ 中任意三点两两与 $x_0$ 组成的三元组均属于 $\{CDF,DEE,DEF\}$，迫使这三点中每对都恰含一个 $D$ 和一个非 $D$（即 $K_3$ 二部化），矛盾；
     - 若 $t=2$ 且含 $E/F$，由 $q\ge 10$ 知 $|Q\setminus T|\ge 8$，唯一含 $E/F$ 的带 $Z$ 型为 $DEZ_9$，故 $T=\{D,E\}$（$w$ 和为 $1$），总盈余 $\ge 1+2\times 8=17>16$，矛盾；
     - 若 $t=3$ 且含 $E/F$，则 $T\in\{CDF,DEE,DEF\}$（$w$ 和 $\ge 1$），由 $1+2(q-3)\le 16$ 迫使 $q=10$ 且 $b_9\le 2(10)-19=1$，直接排除含两个 9 度点的 $CDF,DEF$；而 $DEE$ 与 $Q\setminus T$ 组合需 $EEZ$ 型，不在允许列表中。
     故 $Q$ 中无 $w=1$ 点，$T$ 恰为 $Q$ 中双 unit 点集（类型 $A,B,C,D$），$Q\setminus T$ 全为 $Z_8,Z_9$（$w=2,\tau=0$）。

2. **$A$ 池的双星匹配结构与 $a=|A|\le 6$：**
   对任意三名 $A$ 点，38 残型中仅有的 4 个 $AAA$ 源（`8281,8461,8465,8472`）给出：高点两两共度均为 2，且两侧非共中心边（每侧 $7-2=5$ 条）在三点上诱导的划分至多在一侧出现单个二元块（无三元块、无同对两侧重块、无同侧或异侧相邻二元块）。因此在整个 $A$ 池上，两侧同块点对的并集 $M_1\cup M_2$ 构成匹配（$|M_1|+|M_2|\le\lfloor a/2\rfloor$），每侧块数 $a-|M_r|\le 5$（$r=1,2$），求和得 $2a-\lfloor a/2\rfloor\le 10\implies a\le 6$。且任意三名 $A$ 点中必有两名在两侧 star 中均位于不同块。

3. **四种解析选点分流的完备性（无需将 76 型表作为前提）：**
   由 $z=|Q\setminus T|\le 8$ 与 $q\ge 10, t\le 8$ 知 $Q\setminus T\ne\varnothing$。若存在 $Z_8$，则仅 $AAZ_8$ 允许，迫使 $T=A^a$；若 $Q\setminus T$ 全为 $Z_9$，则 $T=BB$（给出 $q\le 10$ 与 $b_9=q-2\le 2q-19\implies q\ge 17$ 矛盾）、$T=A^a$，或 $T=A^a\cup\{K\}$（$K\in\{B,C,D\}$，此时 $b_9=q-t+\kappa\le 2q-19$ 与 $q\le t+8$ 给出 $2t\ge 11+\kappa\implies t\ge 6\implies a=t-1\ge 5$）。
   因此，**凡 $a<4$ 必有 $T=A^a$（$t=a$）且 $b_9=Z_9$**，結合 $q=a+z\ge 10$ 与 $z\le 8$ 穷尽为四个分支：
   - **情形 I（$a\ge 4$）：** 选 4 个 $A$ 点进入 `A4` 六锁域。
   - **情形 II（$a=2$）：** $t=2\implies q=10, z=8$。8 个高外点总 $w$ 为 $16-16=0$（全为双 unit），超额度数 $e=1-b_9\in\{0,1\}$（度数全 10 或七个 10、一个 11）。因 $\sum\tau=6$，至少 $8-6=2$ 个高外点 unpaired（$\tau=0$），与 1 个 $A$ 点构成 `u8_10_10` 或 `u8_10_11`。
   - **情形 III（$a=3, q=11$）：** $t=3, z=8$。7 个高外点全为双 unit，$e=3-b_9\le 3$；12/13 度双 unit 点已由 `{x1,x2,h}` 三锁严格排除，故全为 10/11 度，且至少 $7-6=1$ 人 unpaired，与两名两侧分开的 $A$ 点构成 `u8_8_10` 或 `u8_8_11`。
   - **情形 IV（$a=3, q=10$）：** $t=3, z=7$。8 个高外点总 $w=2$、$e=1-b_9\le 1$（至多一人 11 度），至少 6 人为双 unit。若有 unpaired 双 unit 高点则归入情形 III；否则恰好 6 个双 unit 高点全为 paired（$\tau=1$，耗尽 $\sum\tau=6$），其中至少 $6-1=5$ 人为 10 度，取其一 $h$ 与两名两侧分开的 $A$ 点构成 `p8_8_10`。

4. **双星中心边扣除、paired 加回修正与高点共度截断：**
   - 两个低中心的边并集共 $7+7-2=12$ 条中心边，非中心边共 $35-12=23$ 条。
   - 当所选高点全为 unpaired（$\tau=0$）时，它们均不在两条 $x_1x_2$ 共边上，故 $x_1$ 侧与 $x_2$ 侧含高点的中心边集互不相交。对任意非空高点子集 $S$，中心边贡献恰为 $p_1(S)+p_2(S)$；特别在 `u8_10_10`、`u8_10_11` 中，若同一高点对 $\{i,j\}$ 在两侧均同块，它们对应两条不同的中心边，公式 $J_{ij}=I_{ij}-p_1(ij)-p_2(ij)=I_{ij}-2$ 准确扣除 2 次。
   - 在 `p8_8_10` 中，paired 点 $h$（$\tau(h)=1, \lambda(x_1,h)=\lambda(x_2,h)=1$）与 $x_1,x_2$ 的唯一连边是**同一条**低低共边 $\{x_1,x_2,h\}$，而两个 $A$ 点 $u,v$ 满足 $\tau=0$ 且在两侧分开。因此 12 条中心边分解为 $\mu(x_1x_2h)=1, \mu(x_1x_2)=1, \mu(x_ru)=\mu(x_rv)=1, \mu(x_r)=3$（$r=1,2$）；对非中心边单点计数，仅 $h$ 在两侧星中被同一共边计入两次，包含排除 $J_S=I_S-p_1(S)-p_2(S)+r(S)$（仅 $r(\{h\})=1$）给出 $J_u=6, J_v=6, J_h=10-2+1=9$，与 `replay_mixed.py` 完全一致。
   - 24 份高点对共度 $\ge 5$ 的双锁证书（含 (8,8), (8,10), (8,11), (10,10), (10,11)）已全部严格排除，保证 $I_{ij}\in\{1,2,3,4\}$；五/六锁域的全部固定位置证书与共享实际坏对向量的联合弱对偶证书（最大界 $428/429<1$）经独立重放验证通过，严格蕴含原超图 $H$ 可二染色。


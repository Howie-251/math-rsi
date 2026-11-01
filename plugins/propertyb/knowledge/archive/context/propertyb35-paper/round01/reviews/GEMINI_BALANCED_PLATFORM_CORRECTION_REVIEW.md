# 原始模型回应

### 一、前轮两步引理的三处量词精确修正

1. **$D_{\text{swap}}(e^*)$ 的一般上界与多数色正规化的区分：**
   在原 30 个同组交换下，若唯一坏边 $e^*$ 的颜色 $A$ 为全局少数色（$|A|=12$），则三个 $|A^c\cap G_i|=3$ 的组共有 $3\times 2=6\ge 5$ 个 $A$ 色点，$e^*$ 的 5 个点可全部落在这三组中（组组成 $2+2+1$），此时 $D_{\text{swap}}(e^*)=5\times 3=15$。仅当 $e^*$ 的颜色 $A$ 已正规化为全局多数色（$|A|=13$，此时仅两个组有 $|A^c\cap G_i|=3$ 且各组至多含 $e^*$ 的 2 个点）时，才有 $10\le D_{\text{swap}}(e^*)\le 2\times 3+2\times 3+1\times 2=14$；而在 `BALANCED_FLEXIBLE_REPAIR.md` 的 39 动作族中，$|A|=13$ 时每个 $|A\cap G_i|=3$ 组中的坏边点恰好补上 1 个允许单翻，使 39 动作总销毁重数恒为 **$D_{39}(e^*)=5\times 3=15$**。

2. **自由解阻交换 $s_1\in\mathcal{S}_{\text{free}}(e^*)$ 的无条件存在性（修补 $(f\setminus G_i)\setminus e^*=\varnothing$ 的边界情形）：**
   设 $e^*$ 全为颜色 $A$，修复交换 $s_2=\{u_2,v_2\}\subseteq G_i$（$v_2\in e^*\cap G_i\subseteq A$，$u_2\in A^c\cap G_i$）被 $1$ 个 $A^c$、$4$ 个 $A$ 的临界边 $f$（唯一 $A^c$ 点为 $u_2\in f\cap G_i$，且 $v_2\notin f$）阻塞：
   - **情形 A（$(f\setminus G_i)\setminus e^*\ne\varnothing$）：** 任取 $w_1\in(f\setminus G_i)\setminus e^*$（设属于 $G_j, j\ne i$）及任意 $u_1\in A^c\cap G_j$，因 $f$ 的唯一 $A^c$ 点在 $G_i$ 内，必有 $u_1\notin f$，故跨组自由交换 $s_1=\{u_1,w_1\}\in\mathcal{S}_{\text{free}}(e^*)$ 使 $f$ 的 $A^c$ 点数从 $1$ 升为 $2$，消除 $f$ 的临界性。
   - **情形 B（$(f\setminus G_i)\setminus e^*=\varnothing$，即 $f\setminus G_i\subseteq e^*$）：**
     首先证明 $|f\cap G_i|\ge 4$ **不可能**：若 $|f\cap G_i|\ge 4$，则 $f\cap G_i$ 含 $u_2\in A^c$ 及至少 $3$ 个 $A$ 色点，加上 $v_2\in (A\cap G_i)\setminus f$，迫使 $|A\cap G_i|\ge 4$，与组内配额 $|A\cap G_i|\in\{2,3\}$ 矛盾！
     因此必有 $|f\cap G_i|\in\{2,3\}$，从而 $|f\setminus G_i|=|f\cap e^*\setminus G_i|\in\{2,3\}$。由异组点对共度 $\lambda=1$，两条不同边 $f\ne e^*$ 交至少 2 点迫使 $f\cap e^*$ 完全落在一个组 $G_j$（$j\ne i$）内，故 **$(f\cap G_i)\cap e^*=\varnothing$**。
     于是 $(f\cap G_i)\setminus\{u_2\}$ 含有 $|f\cap G_i|-1\ge 1$ 个位于 $e^*$ 外的 $A$ 色点 $w\in (A\cap G_i)\setminus e^*$；同时因 $|A^c\cap G_i|\ge 2$ 且 $f$ 仅含唯一 $A^c$ 点 $u_2$，必存在 $u'\in (A^c\cap G_i)\setminus f$。此时 **$G_i$ 内部的自由交换 $s_1=\{u',w\}\in\mathcal{S}_{\text{free}}(e^*)$**（两端均不在 $e^*$ 内）将 $w\in f$ 翻为 $A^c$、$u'\notin f$ 翻为 $A$，同样使 $f$ 变为 $2/3$ 平衡边而解阻！
   （注：若 $f$ 为 $4$ 个 $A^c$、$1$ 个 $A$ 且唯一 $A$ 点为 $v_2\in e^*\cap G_i$，则 $f\setminus G_i\subseteq A^c$ 与全 $A$ 边 $e^*$ 天然不交，$(f\setminus G_i)\setminus e^*=f\setminus G_i\ne\varnothing$ 恒成立。）

3. **两步次生单色边的充要条件修正：**
   跨组交换对 $s_1=\{u_1,w_1\}\subseteq G_j$ 与 $s_2=\{u_2,v_2\}\subseteq G_i$（$j\ne i, u_1,u_2\in A^c, w_1,v_2\in A$）使原本 $2/3$ 平衡边 $g$ 变为单色，**当且仅当**：
   - $g$ 原有 $2$ 个 $A^c$ 点、$3$ 个 $A$ 点，其两个 $A^c$ 点恰为跨组对 $\{u_1,u_2\}$（由 $\lambda=1$ 唯一确定 $g=e(u_1,u_2)$），**且反向端点 $w_1\notin g, v_2\notin g$**；或
   - $g$ 原有 $3$ 个 $A^c$ 点、$2$ 个 $A$ 点，其两个 $A$ 点恰为跨组对 $\{w_1,v_2\}$（由 $\lambda=1$ 唯一确定 $g=e(w_1,v_2)$），**且反向端点 $u_1\notin g, u_2\notin g$**。

---

### 二、`BALANCED_FLEXIBLE_REPAIR.md` 核查与平台极值态分析

[BALANCED_FLEXIBLE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/BALANCED_FLEXIBLE_REPAIR.md) 第 1–4 节的 39 动作重数计数（每条临界边新造总次数仍为 $C_{39}(f)=4-t\le 3$ 或 $q-(t-1)\le 3$，多数色坏边销毁总次数恒为 $D_{39}(e^*)=15$）与多数色正规化引理（$|A|=12$ 时 $84\ge 64+3x\implies x\le 6$，至少 $9-x\ge 3$ 个零变化单翻将坏边颜色升为全局多数 $13$）完全正确。

以下针对“在 $c=1$ 平台连通分量 $\mathcal{P}$ 内选择使阻塞重数 $\Psi$ 或坏边组组成极小的态能否强制出口”给出精确数学推导：

#### 1. 多数色坏边在 39 动作下的精确阻塞分解定理
设 $\sigma\in\mathcal{P}$ 已正规化为 $|A(\sigma)|=13$（唯一坏边 $e^*$ 全为 $A$ 色）。记 $s_i=|e^*\cap G_i|$，$m(e^*)=\max_i s_i\in\{1,2,3\}$。将 9 条临界边分为 $\mathcal{F}_4$（$x$ 条，含 $4$ 个 $A$ 点、$1$ 个 $A^c$ 点）与 $\mathcal{F}_1$（$9-x$ 条，含 $1$ 个 $A$ 点、$4$ 个 $A^c$ 点）。对每条临界边 $f$，记 $B_{\text{rep}}(f)$ 为它在 $e^*$ 的 15 个修复动作 $\mathcal{A}_{\text{rep}}(e^*)$ 中阻塞的动作数：

**定理（修复阻塞的组组成受限性）：**
1. 对任意 $f\in\mathcal{F}_1$（唯一 $A$ 点为 $y_f\in G_i$）：因 $e^*$ 的任何修复动作（单翻 $v\in e^*$ 或交换 $\{u,v\}$）仅将 $v\in e^*$ 从 $A$ 变为 $A^c$，故若 $y_f\notin e^*$ 则 **$B_{\text{rep}}(f)=0$**；若 $y_f=v\in e^*\cap G_i$，则 $f$ 仅阻塞 $v$ 处的修复动作，且 $B_{\text{rep}}(f)=4-|f\cap G_i|\le 3$。
2. 对任意 $f\in\mathcal{F}_4$（唯一 $A^c$ 点为 $u_f\in G_i$）：单翻动作不将 $u_f$ 变为 $A$；仅当 $v\in (e^*\cap G_i)\setminus f$ 时，修复交换 $\{u_f,v\}$ 使 $f$ 全为 $A$。故
   $$B_{\text{rep}}(f) = |(e^*\cap G_i)\setminus f| \le \min\bigl(s_i,\ |A\cap G_i|-|f\cap G_i|+1\bigr) \le m(e^*).$$
   特别地，若 $u_f$ 所在组与 $e^*$ 不交（$s_i=0$），则 **$B_{\text{rep}}(f)=0$**；若 $e^*$ 为横截边 `11111`（$m(e^*)=1$），则**每条 $f\in\mathcal{F}_4$ 至多阻塞 $e^*$ 的 1 个修复动作（$B_{\text{rep}}(f)\le 1$）**。
3. 汇总全部 9 条临界边，15 个修复动作上的总阻塞重数 $\Psi(\sigma)=\sum_{a\in\mathcal{A}_{\text{rep}}(e^*)} n(a)=\sum_f B_{\text{rep}}(f)$ 满足
   $$\Psi(\sigma) \le 3(9-x) + m(e^*)\,x = 27 - \bigl(3 - m(e^*)\bigr)x.$$

#### 2. 极小化坏边组组成 $m(e^*)$ 与极小化 $\Psi(\sigma)$ 的精确作用与边界
- **坏边转移动作的必然存在性：** 若 $\sigma$ 为一步陷阱（$\forall a\in\mathcal{A}_{\text{rep}}(e^*), n(a)\ge 1$），则仅被**唯一**临界边阻塞（$n(a)=1$，从而 $\Delta c(a)=0$）的修复动作数至少为
  $$\#\{a\in\mathcal{A}_{\text{rep}}(e^*): n(a)=1\} \ge 30 - \Psi(\sigma) \ge 3 + \bigl(3 - m(e^*)\bigr)x \ge 3.$$
  每个 $n(a)=1$ 的修复动作 $a$ 本身就是平台内的零变化移动，执行后将唯一坏边从 $e^*$ 替换为阻塞它的临界边 $f_a$（若 $f_a\in\mathcal{F}_1$ 使新坏边为 12 点色，再接一次第 3 节的自由单翻即可恢复 13 点多数色且不改坏边）。
- **为什么单靠极小化坏边组组成 $m(e^*)$ 不能直接导出一步矛盾：** 即使平台可到达 $m(e^*)=1$（`11111` 型坏边），上界收紧为 $\Psi(\sigma)\le 27-2x$；当 $1\le x\le 6$ 时仍有 $27-2x\ge 15$，不直接违反一步陷阱条件 $\Psi(\sigma)\ge 15$，但保证至少有 $3+2x\ge 5$ 个坏边转移出口。
- **在 $\mathcal{P}$ 中取 $\Psi(\sigma)$ 极小态的精确约化：** 取 $\mathcal{P}$ 中满足 $|A(\sigma)|=13$ 且 $\Psi(\sigma)$ 最小的状态 $\sigma^*$。若 $\Psi(\sigma^*)<15$，由抽屉原理必有某 $a\in\mathcal{A}_{\text{rep}}(e^*)$ 满足 $n(a)=0$（已一步走通）。若 $\Psi(\sigma^*)\ge 15$，对任意不碰 $e^*$ 的自由零变化交换 $s_1\in\mathcal{S}_{\text{free}}(e^*)$（$n(s_1)=0$），若 $s_1$ 位于 $e^*$ 外的组（$s_j=0$），则 $\mathcal{A}_{\text{rep}}(e^*)$ 的 15 个动作在 $s_1$ 前后完全不变；$\Psi(\sigma^*)$ 的极小性迫使：**任何消除某条临界边 $f$ 阻塞贡献 $B_{\text{rep}}(f)\ge 1$ 的零变化自由交换 $s_1$，必须同时将某些 $2/3$ 边变为新临界边 $g$ 且其对 $e^*$ 的新增阻塞满足 $\sum_g B_{\text{rep}}(g)\ge B_{\text{rep}}(f)$**。因此，证明平台必有出口等价于排除这种“零变化自由动作下 $\mathcal{A}_{\text{rep}}(e^*)$ 阻塞重数处处自锁補償”的局部构型。


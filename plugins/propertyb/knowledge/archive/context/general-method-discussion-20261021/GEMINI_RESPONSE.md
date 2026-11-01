### 实际读取文件
1. [CK2013_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/general-method-discussion-20261021/CK2013_FULLTEXT.txt)（对应 [cherkashin_kozik_2015_random_greedy.pdf](file:///Users/rfy_naiveai/Desktop/aris4math/ref/cherkashin_kozik_2015_random_greedy.pdf)）
2. [propertyB_m6_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m6_proof.md)
3. [propertyB_m7_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m7_proof.md)
4. [propertyB_k8_k9_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_k8_k9_proof.md)
5. [PROPERTY_B_SMALL_K_TRANSFER.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)
6. [PROPERTY_B_REUSABLE_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)（L1–L12）

---

### 三类目标的直接结论（HERO）

* **A（一般的有限参数可染判据／统一定理）：对。** $k=6,7,8,9$（对应 $M=64,129,265,541$）的证明共享完全同构的数学骨架，可严格提炼为一个量词明确的**有限参数条件贪心可染定理**，无例外地解释四组共 $4,173$ 个有理检验分支（及 $k=10,11$ 扩展分支）。
* **B（适用于所有充分大 $k$ 的新显式下界或更佳渐近常数）：未知。** 有限 $k$ 框架比 Cherkashin–Kozik (2013) 多出离散超几何精确计数、逐位置 $\min$ 截断与共度坏对扣除，可给固定 $k$ 更紧的显式判据；但文件内未做大 $k$ 渐近展开，且关键过渡区极窄，尚无证据表明它能直接改写渐近首项常数。
* **C（突破 CK/RS 的 $\Omega(2^k\sqrt{k/\ln k})$ 渐近阶／去 $\log$）：不对。** 仅靠常数个锁点与单位置并界极难突破该阶，不可从 $k=5\dots 9$ 的有限数值推进外推渐近阶改进。

---

### 一、正面提炼：统一的有限参数可染定理（层次 A）

从 [propertyB_m6_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m6_proof.md)、[propertyB_m7_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_m7_proof.md) 与 [propertyB_k8_k9_proof.md](file:///Users/rfy_naiveai/Desktop/aris4math/propertyB_small_k/propertyB_k8_k9_proof.md) 可合法抽象出如下统一元定理：

**定理（0–3 锁条件排列可染判据）。** 设整数 $k\ge 3, M\ge 1$。定义顶点数有效窗口
$$V_{k,M} := \left\{v\in\mathbb{Z} : v\ge 2k-1,\ v\Bigl\lceil\frac{v-1}{k-1}\Bigr\rceil \le kM,\ M\frac{\binom{\lfloor v/2\rfloor}{k}+\binom{\lceil v/2\rceil}{k}}{\binom{v}{k}} \ge 1\right\}.$$
若对每个 $v\in V_{k,M}$，均满足 $\binom{v}{k}\ge M$，且对每个最小度 $d\in \bigl[d_0(v),\lfloor kM/v\rfloor\bigr]$（其中 $d_0(v)=\lceil(v-1)/(k-1)\rceil$），存在锁阶 $s\in\{0,1,2,3\}$ 与锁位置 $1\le t_1<\dots<t_s\le v$，使得下述对应锁型族 $\mathcal{L}_s(v,d)$ 中的所有迹重数向量 $\ell=(\ell_T)_{T\subseteq[s]}$ 均满足
$$U_k(v,t,\ell) := \sum_{h=1}^v \min\bigl\{A_h(\ell),\, B_h(\ell),\, C_h(\ell)-D_h(\ell)\bigr\} < 1,$$
则任意边数 $\le M$ 的有限简单 $k$-一致超图均有 Property B（即 $m(k)\ge M+1$）。

**其中各项的精确定义与生成条件为：**
1. **局部概率与坏对扣除**：在位置 $h$（前/后自由槽数 $a_h,b_h$，前/后锁集 $I_h^-,I_h^+$），$r_T=k-|T|$，$N=v-s$。$A_h,B_h$ 为单边在 $h$ 终止/起始的精确超几何概率和；$C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf{1}_{T=U})w_h(T,U)$ 为有序类型对的临界权重和。
   * 当 $s=0$ 时，令 $Q_v=\max\bigl\{0,\bigl\lceil(M\binom{k}{2}-\binom{v}{2})/\binom{k-1}{2}\bigr\rceil\bigr\}$，取 $C_h=(M(M-1)-2Q_v)w_h(\varnothing,\varnothing)$，$D_h=0$。
   * 当 $s\ge 1$ 时，自由位置取 $D_h=0$；锁点位置 $h=t_j$ 处，过第 $j$ 个锁点的边有度数 $d_j=\sum_{T\ni j}\ell_T$，必存在至少 $q_j=\bigl\lceil((k-1)d_j-(v-1))/(k-2)\bigr\rceil$ 个中心外再相交的无序坏对。在所有满足 $j\in T\cap U$ 的无序类型格 $\{T,U\}$（容量 $\binom{\ell_T}{2}$ 或 $\ell_T\ell_U$，单对双向权 $w_{t_j}(T,U)+w_{t_j}(U,T)$）中，按权重升序装满 $q_j$ 对所得总权即为 $D_{t_j}$。
2. **四阶锁型族 $\mathcal{L}_s(v,d)$ 的合法选点条件**：
   * **$s=0$**：唯一向量 $\ell_\varnothing=M$。
   * **$s=1$**：单向量 $\ell_{\{1\}}=d,\ \ell_\varnothing=M-d$。
   * **$s=2$**：前提为 $s_1 := 2(v-1)-(k-1)d > 0$。令 $B=\min\{b\ge d : vd+s_1(b+1-d)>kM\}$，遍历 $d_2\in[d,B]$，生成 $\ell_{12}=1,\ \ell_1=d-1,\ \ell_2=d_2-1,\ \ell_\varnothing=M-d-d_2+1$。
   * **$s=3$**：前提为存在整数 $D\ge d_0(v)$ 使 $Z=(D+1)v-kM>0$ 且满足统一判据 $2(k-1)Z > ((k-1)(D+1)-v+2)^2$。遍历 $d_0(v)\le d_1\le d_2\le d_3\le D$，生成两类单位共度迹型：(i) 单三元边 $\ell_{123}=1,\ \ell_i=d_i-1,\ \ell_\varnothing=M-\sum d_i+2$；(ii) 三二元边 $\ell_{12}=\ell_{13}=\ell_{23}=1,\ \ell_i=d_i-2,\ \ell_\varnothing=M-\sum d_i+3$。

**对 $k=6\dots 9$ 实例的统一解释：**
$k=7,8,9$ 直接按 $v$ 分段指派 $s\in\{0,1,2,3\}$（$k=7$ 在 $v=71\dots 73, D=12$ 处同样满足上述二次判据 $12Z > (9,8,7)^2$）；$k=6$ 在 $v=35,36$ 处利用定理中对 $(v,d)$ 的量化，对 $d\le 9$ 取 $s=1$、对 $d=10$ 取 $s=2$，其余 $v$ 按段取 $s\in\{0,1,2,3\}$。故四篇证明完全是同一有限参数定理在不同 $(k,M)$ 下的实例化。

---

### 二、相对 CK2013 的新分析内容 vs 已知技术组合

* **属于已知技术组合的部分**：
  1. 随机排列贪心染色及“无全红边、全蓝边必由单交临界对 $(A,B)$ 见证”（Pluhár 2009 / [CK2013_FULLTEXT.txt](file:///Users/rfy_naiveai/Desktop/aris4math/context/general-method-discussion-20261021/CK2013_FULLTEXT.txt#L108-L120)）。
  2. 最小反例粘合非共边点对归约到点对覆盖 $\lambda_{xy}\ge 1$（[PROPERTY_B_REUSABLE_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md#L39-L50) L1）、度数与共度超额双计数（L2）、小点数平衡二分染色（CK Remark 4）及在冲突图上用 Caro–Wei 不等式取独立集。
* **相对 CK2013 的实质新分析内容**：
  1. **有限点数窗口上的无放回超几何精确计数**：CK 在 $[0,1]$ 上独立采样出生时间，对顶点数 $v$ 不敏感，且在式 (1.2) 中将积分 $\int_{-p/2}^{p/2}(1-4x^2)^{k-1}dx$ 粗放为区间长度 $p$（导致 $k=5,M=35$ 时 CK 式 (1.3) 最小值为 $1.671787>1$）；新框架在点对覆盖锁定的有限窗口 $V_{k,M}$ 上做无放回联合计数（L3）。
  2. **逐位置动态取 $\min(A_h,B_h,C_h-D_h)$**：CK 硬性将 $[0,1]$ 切成 $B,P,R$ 三段并把两侧一阶矩与中间二阶矩相加；新框架在每个离散位置 $h$ 取单边终止、起始与临界对上界的最小值，消除了分段拼接损耗。
  3. **条件锁点分流 + 局部 link 坏对容量弱对偶扣除 $D_h$（L6/L7）**：CK 将全部 $M^2$ 个有序边对视为潜在危险对；新框架把低度单位共度点锁在中点附近，使高危位置的临界事件集中于锁点，并利用中心外再相交边对不能成为单交临界对的性质，按类型容量贪心扣除必存的 $q_j$ 个坏对权重。

---

### 三、目前未接的一项关键数学义务

若将该框架继续推向更紧的边数阈值（如 $m(5)\ge 36$ 或 $m(7)\ge 131$），**目前未接通的关键数学义务是：当 0–3 锁单布局判据失效时，高阶锁（$s\ge 4$）完备迹分类与多布局共享坏对对偶（L8）的普适选点衔接**。
如 [PROPERTY_B_SMALL_K_TRANSFER.md](file:///Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md#L106-L123) 所验证：在 $k=5,M=35$ 时，$v=18$ 处三锁判据差值恒为 $-16(D-7.5)^2-500<0$，无法由总度预算保证单位三锁；而 $v=25,D=7$ 处三锁固定在中央位置 $(11,12,13)$ 的精确界为 $U_{\text{separate}}=29451/24871>1$ 与 $U_{\text{triple}}=4214/3553>1$（$k=7,M=130,v=66$ 的双锁同样以 $\approx 1.0000263>1$ 越界）。此时必须引入更多锁点（处理大迹相交 packing）或跨多个锁点布局共享同一真实坏对向量 $z$（L8），而这类高阶结构的普适存在性引理尚未闭合成一般 $k$ 的统一定理。

---

### 四、改进渐近常数与去 $\log$ 障碍评价（层次 B、C）

1. **渐近常数（层次 B）**：
   * **已有证据**：有限 $k$ 下，点对覆盖将顶点数限制在 $v = O(k\sqrt{M})$，故全局重交扣除 $2Q_v$ 与逐位置 $\min(A_h,B_h,C_h)$ 能实质压低有限 $k$ 的失败上界。
   * **可行猜测与边界**：在 $k\to\infty$、$M=\Theta(2^k\sqrt{k/\ln k})$ 时，CK 的中间窗口宽度为 $p \sim \frac{\ln k}{2k} \ll k^{-1/2}$。在此窄窗内 $(1-4x^2)^{k-1} = 1 - O(\frac{\ln^2 k}{k}) \sim 1$，且一阶矩 $A_h,B_h$ 在边界 $t=\frac{1\pm p}{2}$ 处跨越 $1$ 的过渡区宽度仅为 $O(1/k) = o(p)$。因此，仅把 CK 的三区间分段改为逐位置 $\min$ 或精确计算中心二阶矩积分，在 $k\to\infty$ 时只会带来 $1+o(1)$ 的次主项修正；若想真正提升 $\sqrt{2}$ 渐近常数，必须证明在全窗口 $v\in V_{k,M}$ 上高共度坏对扣除 $D_h$ 占 $C_h$ 的非零渐近比例，这在目前文件中尚无大 $k$ 证明。
2. **去 $\sqrt{\ln k}$ 障碍（层次 C）**：
   $\sqrt{\ln k}$ 源于单遍随机贪心中“压低两侧全同色边一阶矩”要求中间窗口宽度 $p \ge \frac{\ln k}{2k}$，而对中间 $\Theta(v p)$ 个位置直接做一阶并界（$\sum_h C_h$）会产生 $p \cdot (M/2^k)^2$ 的累积惩罚。固定常数个锁点 $s=O(1)$ 只能精确控制 $O(1)$ 个位置，无法改变中间 $\Theta(v\frac{\ln k}{k})$ 个自由位置上的并界加和结构。因此，不突破位置间的事件一阶并界（如引入高阶相关消去或新随机过程），该框架不可能消去 $\sqrt{\ln k}$。

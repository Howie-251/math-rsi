# 原始模型回应

### `GROUP5_EXTERNAL_STAR.md`（五点组加实际外点单位星）的独立静态敌对审阅

**审阅方式与结论边界：** 本次对 [GROUP5_EXTERNAL_STAR.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/GROUP5_EXTERNAL_STAR.md)、[GROUP5_EXTERNAL_STAR_REPLAY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/GROUP5_EXTERNAL_STAR_REPLAY.py)、[GROUP5_EXTERNAL_STAR_REPLAY.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/GROUP5_EXTERNAL_STAR_REPLAY.json)、[GROUP5_EXTERNAL_STAR_FULL_EDGE_PILOT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/GROUP5_EXTERNAL_STAR_FULL_EDGE_PILOT.json) 及 [GROUP5_CATALOGUE.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/GROUP5_CATALOGUE.json) 实施只读静态数学与代码核查（未重新运行 Python 脚本，直接核对重放代码逻辑与保存的精确有理证书及目录数据）。**在已验证的 22 个单组存活库存入口与项目的条件排列／真实坏对配额引理下，全部 5 个核心推导环节完全严密，无量词倒置、运输漏项或配额方向错误。** 本结果将 $a=5$ 无组边单组库存压至 7 类（`1,5,7,8,9,10,18`）、有组边库存压至 3 类（`23,24,26`），并严格证明不可染 $a=5$ 超图中不存在任何 `4+1` 组组成边；但尚未闭合整个 $a=5$ 分支或全局 $m(5)\ge 36$。

---

### 一、五个核心逻辑与算术接口的逐项核查

1. **实际输入 $H$ 到六锁 $S=G\cup\{x\}$ 精确迹的唯一恢复与 51 划分域完备性：**
   设 $G=\{0,1,2,3,4\}$ 为 $H$ 的任一五点组，$x\in V\setminus G$ 为任意实际外点（无需指定 $x$ 所属外组）。因跨组共度 $\lambda(x,g)=1$（$\forall g\in G$），每个 $g\in G$ 恰属于 $x$ 的 7 条关联边中的唯一一条；按共边关系将 $G$ 分块，即得 $G$ 的唯一集合划分 $\Pi_x$。因边大小为 5，任何含 $x$ 的边至多含 $G$ 中 4 点，故整块划分 $\{G\}$（掩码 `31`）不可能出现，$\Pi_x$ 必属于其余 $52-1=51$ 种划分之一（块数 $k=|\Pi_x|\in\{2,3,4,5\}$）。
   - 含 $x$ 的 7 条边精确分解为：$k$ 条满足 $e\cap S=T\cup\{x\}$（$T\in\Pi_x$，重数各 1），以及 $7-k$ 条与 $G$ 不交的纯 $\{x\}$ 迹边（$n_{\{x\}}=7-k$）。
   - 不含 $x$ 的 28 条边在 $S$ 上的迹即其在 $G$ 上的迹，重数唯一恢复为 $n_T=\mu_T-\mathbf{1}\{T\in\Pi_x\}$（$\varnothing\ne T\subseteq G$）及 $n_\varnothing=\mu_\varnothing-(7-k)$。
   - 非负性充要条件为 $\forall T\in\Pi_x, \mu_T\ge 1$ 且 $\mu_\varnothing\ge 7-k$。`GROUP5_EXTERNAL_STAR_REPLAY.py`（第 79–82 行）独立验证 18 个 $\mu_G=0$ 代表的所有满足此条件的划分无重无漏，共 245 个有效对。

2. **$S_5$ 换标号运输与“存在真迹 $T^*\to$ 任取边外点 $x\to$ 强制 $T^*\in\Pi_x$”的量词方向：**
   - 若实际组 $G$ 的迹库存经双射 $\sigma: G\to\{0,1,2,3,4\}$ 映为代表 $\mu$，则任何外点 $x$ 的实际划分同步映为 $\sigma(\Pi_x)$；反之，代表上的严格位置证书经 $\sigma^{-1}$（保持第 6 锁 $x$ 不变）直接拉回为原图 $G\cup\{x\}$ 的严格证书。
   - **选 $T^*$ 的量词核查：** 对给定代表 $\mu$，只需**存在一个**非空真迹 $T^*\subsetneq G$（$1\le |T^*|\le 4$）满足 $\mu_{T^*}\ge 1$，且使**所有包含 $T^*$ 的可用划分 $\Pi\ni T^*$** 均严格（$U(\mu,\Pi)<1$）。调用时：因 $\mu_{T^*}\ge 1$，实际 $H$ 中必存在一条边 $e^*$ 满足 $\sigma(e^*\cap G)=T^*$；又因 $|T^*|\le 4$，必可取实际外点 $x\in e^*\setminus G\ne\varnothing$。该 $x$ 与 $T^*$ 中各点的唯一共边正是 $e^*$，故其实际划分 $\Pi_x$ **必然以 $T^*$ 为一个整块**（$T^*\in\Pi_x$），从而必落入已全部严格的 $\{\Pi\text{ 可用}: T^*\in\Pi\}$ 中，直接给出 $H$ 的二染色。
   - 经与 `GROUP5_CATALOGUE.json` 手工逐一比对，被排除的 10 个代表（`11,13,14,15,16,17,19,20,21,22`）所选 $T^*$ 均满足 $1\le|T^*|\le 4$ 且 $\mu_{T^*}=1>0$，所有含 $T^*$ 的可用划分之最大界均严格小于 1。

3. **代表 12 的 20 外点边际整数分离证书（§4）：**
   手工核对 `GROUP5_CATALOGUE.json` 中 `id=12` 的非单点迹：二元迹为 `3,5,6`（重数各 1）与 `9`（重数 2），总重数 5；三元迹为 `14,19,21,26,28`（重数各 1），总重数 5；无四元或五元迹。故在全部 20 个外点的划分中，非单点块总出现次数为
   $$\sum_{|T|\ge 2}\nu_T = \sum_{|T|=2} 3\mu_T + \sum_{|T|=3} 2\mu_T = 3\times 5 + 2\times 5 = 25,\qquad \nu_6 = 3\mu_6 = 3.$$
   另一方面，逐一检查 `id=12` 仅存的 11 个非严格划分（`REPLAY.json` 第 289–350 行），唯一含 2 个非单点块的划分为 `{9,6,16}`（含块 `6`），其余 10 个划分至多含 1 个非单点块。故对每个保留划分 $P$ 恒有 $\mathrm{nonsingle}(P)\le 1+\mathbf{1}\{6\in P\}$。若 $H$ 不可染，20 个外点划分均在保留列表中，求和得 $25 \le 20 + \nu_6 = 23$，矛盾。

4. **代表 25 的严格排除、“无四点组迹”全局推论与六锁配额方向（§5–§6）：**
   - 手工核查 `GROUP5_CATALOGUE.json` 中剩余 7 个无组边代表（`1,5,7,8,9,10,18`）及 4 个有组边代表（`23,24,25,26`）：除 `id=25` 含唯一四元迹 `30={1,2,3,4}`（$\mu_{30}=1$）外，其余 10 个代表的所有非零迹掩码均不含 4 元集（bit_count 均 $\ne 4$）。
   - 对 `id=25`，取 $\mu_{30}=1$ 对应边的唯一外点 $x\in e^*\setminus G$，其划分必含块 `30`，余下一点 `{0}`（掩码 `1`）只能成单点块，故 $\Pi_x=\{1,30\}$ 唯一。在位置 `[12,11,22,23,24,25]` 下，即使不计任何坏对扣除（全部 `loss = 0`），原始 $\sum_k\min(A_k,B_k,C_k)=1634011/1662804<1$ 已严格成立。由此**任何不可染 $a=5$ 超图中均不存在 $|e\cap G_i|=4$ 的边（`4+1` 组成被完全排除）**。
   - **配额方向核查：** 在 `GROUP5_EXTERNAL_STAR_REPLAY.py`（第 55–70 行）中，6 锁（$N=19$）每中心度数 7 覆盖其余 24 点，总坏对配额 $q_{\text{total}}=\lceil(28-24)/3\rceil=2$；纯单点迹配额 $q_{\text{pure}}=\max(0,\lceil(4s_i-19)/3\rceil)$ 先从纯单点槽扣除，余量 $2-q_{\text{pure}}$ 再从包含零权槽（`t&u != pivot`）的全体无序迹对槽中取**最小权重**，方向完全保守有效。

---

### 二、一个真正不同的下一步清晰数学义务

注意当前 245 个输入仅使用了**单一固定布局**与最基本的总/纯单迹配额，且对任意三元真迹 $T^*\subseteq G$（$|T^*|=3$），因 $|G\setminus T^*|=2$，**包含 $T^*$ 的集合划分至多只有 2 个**（即 $\{T^*,\{u,v\}\}$ 与 $\{T^*,\{u\},\{v\}\}$）。

在剩余 7 个无组边代表（`1,5,7,8,9,10,18`）中，由恒等式 $3t_3(G)-5=\sum_{v\in G}\mu_G(\{v\})$，每个代表都含有 $t_3(G)\in\{3,4,5\}$ 条三元真迹 $T^*$。建议下一步直接执行以下**低成本、非 LP 矩的局部闭合义务**：
- **针对剩余 7 类中的三元迹 $T^*$（每个 $T^*$ 仅需同时关闭至多 2 个划分 $\Pi\ni T^*$），在六锁 $G\cup\{x\}$ 上引入中心 $x$ 的避块配额与有理联合布局（Joint Layout Dual）：**
  因 $\lambda(x,g)=1$（$\forall g\in G$），过外点 $x$ 的 7 条边在 $G$ 上的迹两两不交，故在枢轴 $x$ 处**任何两条不同 $x$-边的交集恒为 $t\cap u=\{x\}$（不存在跨锁零权槽）**！除纯单迹配额（避开 $G$ 全部 5 点，$f=7-k$）外，当 $T^*\in\Pi_x$（$|T^*|=3$）时，$x$ 的其余 $f=7-1=6$ 条边完全避开 $R=T^*$（$|R|=3$，可用点 $24-3=21$），在枢轴 $x$ 处额外给出精确避锁坏对配额：
  $$q_{T^*}(x) = \left\lceil\frac{4\times 6 - (24-3)}{3}\right\rceil = 1.$$
  结合该非零权新配额与共享实际坏对向量的有理联合布局（或直接将 $|T^*|=3$ 所在边的**两个**外点 $e^*\setminus G=\{x,y\}$ 同时加入构成单固定输入的七锁 $G\cup\{x,y\}$），有望直接继续筛除剩余 7 个无组边代表。


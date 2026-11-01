threadId: 4b6783b6-d75b-47f1-b4c9-838f6d9462ba

### 审阅结论：引理完全成立（`SOUND_MODULO_DECLARED_IMPORTS`），并附一条同框架精确加强

- **审阅范围**：
  - 全文精读与静态核对：[vertex_flag_capacity_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/PROOF.md)（1–79 行）、[PILOT.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/PILOT.py)（1–39 行），并抽样核对输出 [RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/RESULT.json)（前 250 行及末尾汇总行）与上游输入说明 [FINAL_LAMBDA4_REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/FINAL_LAMBDA4_REPORT.md)、[tau_shared_capacities_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/PROOF.md)。
  - 声明进口：[GLOBAL_TWO_FLIP_PATH_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md) 与 [GLOBAL_TWO_FLIP_SHARED_MIDDLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)。
  - 执行声明：**纯静态数学推导与代码核对（未执行任何程序或 Shell 命令，CPU 0 秒；未运行 Lean；未访问 `v2`）**。

---

### 一、 逐项攻击与数学核对

1. **前提独立性（未暗借 $\lambda\le 4$ 或 $e\le 4$）与简单性最大交 4（§1）**：
   - 设 $H$ 是 $21$ 点、$35$ 条边的简单五元超图，覆盖所有点对。对任意顶点 $v$（度 $d_v$），含 $v$ 的 $\binom{d_v}{2}$ 个无序原边对精确划分为单交对 $t_v$（$F\cap G=\{v\}$）与多交对 $r_v$（$v\in F\cap G, |F\cap G|\ge 2$），即 $t_v+r_v=\binom{d_v}{2}$。
   - 因 $H$ 简单且五元，任意两条不同原边满足 $|F\cap G|\le 4\implies |F\cap G|-1\le 3$。
   - 对任意整数 $\lambda\ge 1$，恒有 $\binom{\lambda}{2}=(\lambda-1)+\binom{\lambda-1}{2}$。由五元性 $\sum_{w\neq v}\lambda(v,w)=4d_v$、顶点数 $|\{w\neq v\}|=20$ 及点对覆盖 $\lambda(v,w)\ge 1\implies\binom{\lambda(v,w)-1}{2}\ge 0$，双计数给出精确恒等式：
     $$\sum_{\substack{\{F,G\}\subset H\\v\in F\cap G}}(|F\cap G|-1)=\sum_{w\neq v}\binom{\lambda(v,w)}{2}=4d_v-20+\sum_{w\neq v}\binom{\lambda(v,w)-1}{2}\ge 4d_v-20.$$
   - 左侧仅 $r_v$ 个多交对有正贡献且每对至多 $3$，故 $3r_v\ge 4d_v-20\implies r_v\ge\max(0,\lceil(4d_v-20)/3\rceil)$，得式 (1)：
     $$t_v\le p_v:=\binom{d_v}{2}-\max\left(0,\left\lceil\frac{4d_v-20}{3}\right\rceil\right).$$
     **全过程仅用简单性、五元性、21 点与点对覆盖，完全不依赖 $\lambda(u,v)\le 4$ 或高点超额 $e\le 4$**。

2. **同一关联的两个方向计数与 $B_d(t)$ 的整数凸优化（§2）**：
   - 在同一个原超图 $H$ 中，令 $x_{F,v}=\#\{G\in H:F\cap G=\{v\}\}$。
   - **顶点方向**：每个单交无序对 $\{F,G\}$（$F\cap G=\{v\}$）在 $F$ 处计入 $x_{F,v}$、在 $G$ 处计入 $x_{G,v}$，故 $\sum_{F\ni v}x_{F,v}=2t_v$。将 $2t_v$ 均分为 $d_v$ 个非负整数（$2t_v=ad_v+b, 0\le b<d_v$），离散凸性给出 $\sum_{F\ni v}x_{F,v}^2\ge B_{d_v}(t_v)=(d_v-b)a^2+b(a+1)^2$。因 $2t_v\le d_v(d_v-1)$，极小化向量的各分量自动满足 $\le d_v-1$。
   - **边方向**：以 $F$ 为合法中间边的无序外边对数恰为 $P_F=\sum_{\{u,v\}\subset F}x_{F,u}x_{F,v}=\frac{1}{2}(s_F^2-\sum_{v\in F}x_{F,v}^2)$。对所有 $F\in H$ 求和并在同一 $H$ 上交换求和次序，得到**精确恒等式**：
     $$P=\sum_{j=0}^4 C_j=\sum_{F\in H}P_F=\frac{1}{2}\left(\sum_{F\in H}s_F^2-\sum_{v\in V}\sum_{F\ni v}x_{F,v}^2\right).$$
   - **贪心前缀求 $B_*(n_1)$ 的精确性**：令 $g_d(S)$ 为和为 $S$ 的 $d$ 个整数的最小平方和，其逐单位增量为 $g_d(S+1)-g_d(S)=2\lfloor S/d\rfloor+1$（关于 $S$ 单调不减）。故 $B_d(t)=g_d(2t)$ 关于 $t$ 的逐单位增量为
     $$B_d(t)-B_d(t-1)=\left(2\left\lfloor\frac{2t-2}{d}\right\rfloor+1\right)+\left(2\left\lfloor\frac{2t-1}{d}\right\rfloor+1\right),$$
     关于 $t\ge 1$ 单调不减。因此在盒约束 $0\le z_v\le p_v$、$\sum_{v\in V}z_v=n_1$ 下极小化可分离凸目标 $\sum_{v\in V}B_{d_v}(z_v)$，直接对全体 $\sum_v p_v$ 个增量排序取最小前 $n_1$ 项之和即得**精确整数最优值 $B_*(n_1)$**。

3. **上界方向与共享 $P$ 无重复扣除（§3 & `PILOT.py`）**：
   - 当 $\delta(\Gamma)\ge 4$ 时，$0\le s_F\le 30$ 且 $\sum_F s_F=2n_1$；凸函数 $s^2$ 在盒约束下的最大值由端点填充给出 $\sum_F s_F^2\le 900q+r^2$（$q=\lfloor 2n_1/30\rfloor, r=2n_1-30q$）。
   - 被减项取下界 $\sum_{v,F}x_{F,v}^2\ge B_*(n_1)$，方向完全一致，故式 (4)
     $$P\le \left\lfloor\frac{900q+r^2-B_*(n_1)}{2}\right\rfloor$$
     是合法上界。
   - [PILOT.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/PILOT.py#L30) 中 `p = min(oldP(n1), (900*q+r*r-prefix[n1])//2)` 是对同一个标量 $P$ 的两个独立合法上界取交集（$\min$），**没有把两者的节省量叠加扣除**，量词与不等式方向完全正确。在 [RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/RESULT.json#L3611-L3620) 中，该引理将 99 个低超额谱的 119 个残余矩键直接消去 66 个（新增 6 个整谱 `50, 53, 78, 81, 84, 86` 全严格），仅余 53 键。

---

### 二、 一条有实质收益的同框架进一步加强（无需新增任何外部假设）

在当前 `PILOT.py` 中，对于 $n_1=525$ 的残余键，贪心求 $B_*(n_1)$ 时之所以仍有 53 键未过，是因为算法将几乎所有低/中度点（$d_v\in\{7,8,9\}$）取满到 $t_v=p_v$（边际增量 $\le 26$），而将几乎全部非单交配额 $r_v=\binom{d_v}{2}-t_v$ 堆到了 1～2 个高度点（$d_v\in\{10,11,12,13\}$）上，避开了高度点在 $t > 3d_v+3$ 处边际增量 $\ge 28\text{--}42$ 的高成本区。

利用本文 §1 **完全相同的顶点关联恒等式**，可以在不引入任何新假设的前提下，从两个方向直接锁死这一松弛：

1. **高度点自身的无条件行下界 $\tau_v\ge \max(0,4d_v-40)$ 直接收紧 $p_v$**：
   由于 $\binom{\lambda-1}{2}\ge \lambda-2$ 对一切整数 $\lambda\ge 1$ 成立，任何度为 $d_v$ 的顶点必满足 $\tau_v=\sum_{w\neq v}\binom{\lambda(v,w)-1}{2}\ge \max(0,4d_v-40)$。直接代入 §1 式 (1) 得无条件加强：
   $$t_v\le p_v^{\mathrm{exact}}:=\binom{d_v}{2}-\max\left(0,\left\lceil\frac{4d_v-20+\max(0,4d_v-40)}{3}\right\rceil\right),$$
   这将 $d=11,12,13$ 的 $p_v$ 分别从 $47,56,67$ 压至 **$45,54,63$**。（同时，将 $t_v\le p_v^{\mathrm{exact}}$ 代入 $C_1\le 35n_1-\sum_v d_v t_v$ 的最小费用填充 $K_d(n_1)$，也无条件收紧了 $C_1$ 容量上界。）

2. **由精确恒等式 $2(t_v-b'_{d_v})=r_{4,v}-r_{2,v}-\tau_v$ 给出的 $(n_2,n_4,\tau)$ 双向耦合（保持纯排序贪心可解）**：
   记 $r_{j,v}$ 为含 $v$ 且交大小为 $j\in\{2,3,4\}$ 的无序原边对数，则 $r_v=r_{2,v}+r_{3,v}+r_{4,v}=\binom{d_v}{2}-t_v$，且 §1 恒等式即 $r_{2,v}+2r_{3,v}+3r_{4,v}=4d_v-20+\tau_v$。两式消去 $r_{3,v}$（后式减前式之二倍），对**每个顶点 $v\in V$** 给出精确恒等式：
   $$2(t_v - b'_{d_v}) = r_{4,v} - r_{2,v} - \tau_v, \qquad b'_d := \binom{d}{2} - 2d + 10.$$
   由此在同一原超图 $H$ 的每个矩键 $(n_0,n_1,n_2,n_3,n_4,\tau)$ 上同时得到两条精确整数约束：
   - **正部受 $n_4$ 约束（限制低/中度点多取 $t_v$）**：若 $t_v > b'_{d_v}$，则 $r_{4,v}\ge 2(t_v-b'_{d_v})$。因单点 $r_{4,v}\le n_4$ 且全图 $\sum_{v\in V}r_{4,v}=4n_4$，必有
     $$t_v\le \min\left(p_v^{\mathrm{exact}},\ b'_{d_v}+\left\lfloor\frac{n_4}{2}\right\rfloor\right),\qquad \sum_{v\in V}(t_v-b'_{d_v})_+\le \sum_{v\in V}\left\lfloor\frac{r_{4,v}}{2}\right\rfloor\le 2n_4.$$
   - **负部受 $\tau+n_2$ 约束（禁止高度点少取 $t_v$）**：若 $t_v < b'_{d_v}$，则 $2(b'_{d_v}-t_v)\le \tau_v+r_{2,v}$（更紧地，对 $b_d:=\binom{d}{2}-2d+10-\max(0,2d-20)$，有 $2(b_{d_v}-t_v)\le (\tau_v-\max(0,4d_v-40))+r_{2,v}$）。因单点 $r_{2,v}\le n_2$、$\tau_v-\max(0,4d_v-40)\le \tau-\sum_{w\in V}\max(0,4d_w-40)$（至少 $\tau_v\le \tau$），必有**逐点下界**：
     $$t_v \ge \underline{t}_v := \max\left(0,\ b_{d_v} - \left\lfloor\frac{\tau-\max(0,4d_v-40)+n_2}{2}\right\rfloor\right).$$
   - **算法实现仍为 $O(1)$ 纯贪心前缀**：先将每个顶点 $v$ 固定取满必选前缀 $\underline{t}_v$，再把剩余增量分为基线池 $\mathcal{M}_0=\{\underline{t}_v < t \le b'_{d_v}\}$ 与超额池 $\mathcal{M}_1=\{b'_{d_v} < t \le \min(p_v^{\mathrm{exact}},b'_{d_v}+\lfloor n_4/2\rfloor)\}$；因每个点内部增量单调不减，只需取 $\mathcal{M}_0 \cup \mathrm{smallest}_{2n_4}(\mathcal{M}_1)$ 中最小的 $n_1-\sum_v \underline{t}_v$ 项即可得到精确整数下界！
   - **实例验证**：例如在 [RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/RESULT.json#L87-L111) 第一个未过键（Spectrum 52：`7^8,8,9^{10},10,11`，$n=(29,525,0,33,8),\tau=7$）上，$11$ 度点有 $b_{11}=41, \tau-4+n_2=3\implies \underline{t}_{11}=41-1=40$，直接迫使 $11$ 度点吃下 $t=39,40$（增量 $28,30$）并把超额池上限锁在 $2n_4=16$。


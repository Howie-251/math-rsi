threadId: 4b6783b6-d75b-47f1-b4c9-838f6d9462ba

### 审阅结论：新差核容量引理与最后两键调用完全成立（`SOUND_MODULO_DECLARED_IMPORTS`）

- **实际阅读范围**：
  - 全文精读与静态核对：[dense_four_kernel_capacity_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/dense_four_kernel_capacity_20261020/PROOF.md)（1–77 行）、[BAD_KERNEL_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/BAD_KERNEL_CHECK.py)（1–52 行）、[BAD_KERNEL_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/BAD_KERNEL_CHECK.json)（首尾 288 行），以及上游局部连接说明 [min_degree_seven_residual_cap12_pilot_20261020/PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/PROOF.md)、[LOW_TAU_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/LOW_TAU_PROOF.md)、[NEWP_REFINEMENT.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/NEWP_REFINEMENT.py)、[independent/AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/independent/AUDIT.md) 与 [IMPLICATED_THREE_KEYS.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/IMPLICATED_THREE_KEYS.json)（前 200 行）。
  - 执行声明：**纯静态数学推导与证书/脚本核对（未执行任何程序或 Shell 命令，CPU 0 秒；未运行 Lean；未访问 `v2`）**。

---

### 一、 核心攻击点逐项核查

1. **同一差核 $K$ 与二二划分 $\{A,B\}$ 的原边对重数（§1）**：
   - 证明未将每个差核 $K=(G\setminus J)\cup(J\setminus G)$ 的三交外边对重数误设为 $1$。固定四元集 $K$ 及其一个无序二二划分 $\{A,B\}$（$|A|=|B|=2$），任何以 $\{A,B\}$ 为两侧差集的三交无序原边对 $\{G,J\}$ 必有形状 $G=T\cup A, J=T\cup B$，其中 $T=G\cap J\subset V\setminus K$（$|T|=3$）。
   - 由五元超图 $H$ 的简单性，给定含 $A$ 的原边 $G$，其补集 $T=G\setminus A$ 唯一确定，从而 $J=T\cup B$ 唯一确定（反之对 $J\supset B$ 同理）。因此同一个 $(K,\{A,B\})$ 可产生的无序外边对 $\{G,J\}$ 数量（即共享三元组 $T$ 的数量）精确受控于式 (3)：
     $$\#\{T: T\cup A\in H,\ T\cup B\in H\} \le \min(\lambda_A, \lambda_B),$$
     且因 $\{G,J\}$ 与 $\{A,B\}$ 均为无序对，不存在遗漏的方向因子 $2$。

2. **困难差核集合族 $\mathcal{K}$ 分类与共同点对成本计数（§2）**：
   - 设 $\mathcal{K}$ 为所有满足 $c(G,J)=13$ 的三交原边对产生的不同四元差核之族。由进口条件，每个 $K\in\mathcal{K}$ 满足 $w(K)=\sum_{\{u,v\}\subset K}\kappa_{uv}\ge 8$，且全局 $\tau=\sum_{\{u,v\}\subset V}\kappa_{uv}\le 10$（其中 $\kappa_{uv}=\binom{\lambda_{uv}-1}{2}\in\{0,1,3\}$）。
   - **两两交集恰为 3**：若不同 $K,L\in\mathcal{K}$ 满足 $|K\cap L|\le 2$，则 $\binom{K}{2}\cap\binom{L}{2}=\binom{K\cap L}{2}$ 至多含 $1$ 个点对（成本 $\le 3$），故 $\tau\ge w(K)+w(L)-w(K\cap L)\ge 8+8-3=13>10$，矛盾。
   - **三核及以上必共享同一三元核 $S$**：若 $K_1=S\cup\{a\}, K_2=S\cup\{b\}$（$|S|=3, a\neq b$），而第三核 $K_3$ 不含 $S$，则 $|K_3\cap K_1|=|K_3\cap K_2|=3$ 迫使 $|K_3\cap S|=2$ 且 $a,b\in K_3$，故 $|K_1\cap K_2\cap K_3|=2$。此时全图仅共同交集里的 **唯一一个点对** 在三核中出现 $3$ 次（成本 $\le 3$），其余点对至多出现 $2$ 次，从而
     $$24 \le w(K_1)+w(K_2)+w(K_3) \le 2\tau + 3 \le 23,$$
     矛盾。若 $|\mathcal{K}|\ge 4$，任何不含 $S$ 的第四核会与 $K_1,K_2$ 构成上述不可能三元组，故全体 $K\in\mathcal{K}$ 必呈向日葵型 $S\cup\{z_i\}$（$i=1,\dots,t$）。
   - **$|\mathcal{K}|\le 3$ 且三核时必有 $w(K)=8$**：记 $c=w(S)\in\{0,1,2,3,4,5,6,7,9\}$（因 $3$ 个 $\{0,1,3\}$ 之和不可能为 $8$）。对每个 $K_i=S\cup\{z_i\}$，若 $\sum_{s\in S}\kappa_{z_is}=0$，则 $\forall s\in S, \lambda_{z_is}\le 2$，任何二二划分的四条跨侧对中必有两条含 $z_i$（$\le 2$）、两条在 $S$ 内（$\le 4$），跨侧共度和 $\le 2\cdot 4+2\cdot 2=12<13$，矛盾。故每个 $z_i$ 向 $S$ 的三条边成本和 $\ge \max(1,8-c)$，且不同 $z_i$ 的外部点对互不相交：
     $$10 \ge \tau \ge c + t\max(1,8-c).$$
     当 $c\le 5$ 时 $t\ge 2$ 已 $\ge 11$；当 $c=6$ 时 $t\ge 3\implies 6+6=12>10$；当 $c=9$ 时 $t\ge 2\implies 9+2=11>10$；仅 $c=7, t=3$ 可行（$7+3\cdot 1=10$），且迫使三核各自的成本皆满足 $w(K_i)=7+1=8$；$t\ge 4$ 无解。

3. **单核重数上界与总超额 $\le 18$（§3）**：
   - 对 $\ell\in\{1,2,3,4\}$ 恒有 $\kappa(\ell)\ge 2\ell-5$，故对 $K$ 的六条边求和得 $w(K)\ge 2L-30\implies L=\sum_{e\subset K}\lambda_e \le 15+\lfloor w(K)/2\rfloor$。
   - **当 $w(K)\le 10$ 时**：$L\le 20$。若某二二划分 $\{A,B\}$ 满足跨侧和 $L-(\lambda_A+\lambda_B)\ge 13$，则 $\lambda_A+\lambda_B\le 7\implies \min(\lambda_A,\lambda_B)\le 3$；三个划分合计至多 $3\times 3=9$。
   - **当 $w(K)=8$ 时**：正文按 $3a+b=8$ 分 $(a,b)=(1,5),(2,2)$ 两类的证法与您提示的短证法完全等价且均严密——因 $L\le 19$，若三个二二划分的跨侧和皆 $\ge 13$，则三组同侧对之和满足 $L=\sum_{i=1}^3(\lambda_{A_i}+\lambda_{B_i})\le 3(L-13)\implies 2L\ge 39\implies L\ge 20$，矛盾；故至多两个划分的跨侧和 $\ge 13$，每个满足 $\lambda_{A_i}+\lambda_{B_i}\le 19-13=6\implies\min(\lambda_{A_i},\lambda_{B_i})\le 3$，单核贡献至多 $2\times 3=6$。
   - 综上，$|\mathcal{K}|\le 2$ 时总重数 $\le 2\times 9=18$；$|\mathcal{K}|=3$ 时三核皆有 $w(K)=8$，总重数 $\le 3\times 6=18$。由于每个 $c(G,J)=13$ 的无序三交边对唯一确定其差核 $K=G\triangle J$ 与二二划分 $\{G\setminus J,J\setminus G\}$，结合已证 $c(G,J)\le 13$ 即得 $C_3\le 12n_3+18$。

4. **最后两键的实际 Caller 与重分配算术复核（§4）**：
   - 在 13 个全 $\lambda\le 4$ 残余谱的 63 键中，49 键已由 $\tau$-可行局部 $c_{13}$ 门直接给 $C_3\le 12n_3$（闭合 48 键），合并新顶点平方损失 $P$ 后再闭 12 键，S95 的 $\tau=8$ 键由 [LOW_TAU_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/LOW_TAU_PROOF.md) 的真实七度外点 15 视图星门闭合（$2L=5431764<5445440$），精确只剩 ID 90（$\tau=10$）与 ID 95（$\tau=9$）两键。
   - 核查 [IMPLICATED_THREE_KEYS.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/IMPLICATED_THREE_KEYS.json) 与 [BAD_KERNEL_CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/min_degree_seven_residual_cap12_pilot_20261020/BAD_KERNEL_CHECK.json#L53326-L53384)：这两键上未通过固定四锁门的 $\tau$-可行库存（分别 13 份与 10 份）全部满足 $w(K)\ge 8$，且 $\tau\le 10$、$c(G,J)\le 13$ 均已具备，满足本引理全部调用前提。
   - **独立手算复核最后两键的完整重分配（释放的 $C_3$ 预算转入 $C_1$）**：
     - **ID 90**（`7^8,8^2,9^8,10^2,11`，$n=(29,525,0,32,9),\tau=10,\mathrm{newP}=12552$）：
       $C_3\le 12(32)+18=402$，贪心分配 $(\hat{C}_0,\dots,\hat{C}_4)=(0,12114,0,402,36)$，
       $$2L = 6864(525)+120(12114)+792(402)+1716(36) = 5437440 < 5445440\quad(\text{余量 }8000).$$
     - **ID 95**（`7^9,9^9,10^2,11`，$n=(28,525,2,31,9),\tau=9,\mathrm{newP}=12546$）：
       $C_3\le 12(31)+18=390$，贪心分配 $(\hat{C}_0,\dots,\hat{C}_4)=(0,12068,52,390,36)$，
       $$2L = 6864(525)+120(12068)+330(52)+792(390)+1716(36) = 5439576 < 5445440\quad(\text{余量 }5864).$$

---

### 二、 实质问题列表

- **无任何数学漏洞或量词缺口（0 项）**。引理及最后两键 caller 完整闭合了全部 81 个具备全 $\lambda\le 4$ 门的 $\delta(H)=7, e\le 4$ 度谱（以及 18 个例外谱的 $\lambda\le 4$ 子情形）。


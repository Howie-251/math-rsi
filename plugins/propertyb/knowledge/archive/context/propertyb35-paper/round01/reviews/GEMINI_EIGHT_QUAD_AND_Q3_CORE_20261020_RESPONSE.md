### 跨家族对抗式数学审阅报告

#### 1. 实际文件读取范围与执行状态
* **已完整读取文件**：
  1. [TWENTYONE_A1_FOUR_EIGHT_CORE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_FOUR_EIGHT_CORE.md)
  2. [TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md)
  3. [high_four_core_generic_20261020/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/REPORT.md)、[PROFILE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/PROFILE.py)、[EXTEND.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/EXTEND.py)、[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/VERIFY.py)
  4. [high_four_core_mixed_q3_20261020/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_mixed_q3_20261020/REPORT.md)、[GENERATE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_mixed_q3_20261020/GENERATE.py)、[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_mixed_q3_20261020/VERIFY.py)
  5. 进口接口核对：[high_edge_intersection_repair_20261020/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/REPORT.md)、[PROBABILITY_LEMMAS.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md)、[twentyone-delta5/replay.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-delta5/replay.py)
* **程序执行状态**：**未执行任何程序或命令**（纯静态数学与代码逻辑审阅）。

---

#### 2. 定理①审阅：21点A1四交核全为八度点（[TWENTYONE_A1_FOUR_EIGHT_CORE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_A1_FOUR_EIGHT_CORE.md)）
* **审阅结论**：**局部数学逻辑与接口严密通过（未发现反例或漏洞）**。
* **已核对的关键量词与同一 $H$ 连接**：
  1. **强点对门进口与四锁完整必要域（2119标签 / 174轨道）**：对任意非Property B的A1超图 $H$，若存在两条不同原边 $E,F$ 满足 $K=E\cap F$（$|K|=4$）且 $K$ 全为八度点，则由A1已验强pair门（八度点对共度 $\ge 5$ 可染）知 $\forall \{i,j\}\subset K,\ c_{ij}\le 4$。因 $E\neq F$ 均含 $K$，故 $q=\mu_{15}\in\{2,3,4\}$；任一三迹 $T$ 含于其内点对共度，故 $t_T\in\{0,1,2\}$；二迹由剩余容量 $r_P=4-q-\sum_{T\supset P}t_T\ge 0$ 界定，单迹与空迹由 $d_i=8$ 及 $|E(H)|=35$ 唯一恢复。行盈余 $\sum_{j\in K\setminus\{i\}}(c_{ij}-1)\le 4\cdot 8-20=12$ 为点对覆盖且非核点 $\lambda_{ij}\ge 1$ 的必然推论（因 $c_{ij}\le 4$，左端恒 $\le 9\le 12$）。四核同度同上限，全群 $S_4$ 作用保域，[PROFILE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/PROFILE.py) 与 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/VERIFY.py) 的拉回/前推轨道因 $S_4$ 对求逆封闭而完全等价。
  2. **未假设八度锁点为 $x$ 的单位邻点**：在对两份四锁残型（原型I：$\mu_0=9,\mu_{\{i\}}=6,\mu_K=2$；原型II：$\mu_0=11,\mu_{\{i\}}=5,\text{matching}=1,\mu_K=2$）做同一 $H$ 的六度点 $x$ 星扩张时，约束为 $\sum_{T\ni i}h_T=\lambda_H(x,i)\in\{1,2\}$（[EXTEND.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/EXTEND.py#L21-L22) 与 [VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_generic_20261020/VERIFY.py#L44-L45) 的 `role in range(16)` 遍历了 $K$ 中4点属于 $U$/$B$ 的全部 $2^4=16$ 种指派），涵盖 $K$ 含任意数目二重邻点 $B$ 的情形。
  3. **$h_K\le 1$ 的简单性来源**：因 $x\notin K$（$d(x)=6\neq 8$），若过 $x$ 的原边包含四核 $K$，则该五元边必等于 $\{x\}\cup K$。由原 $H$ 含35条**互异**五元边（简单超图），$\{x\}\cup K$ 至多出现一次，故 $h_{15}=\nu_{31}\le 1$。
  4. **真稳定子运输与同一 $H$ 原染色返回**：先用 $\pi_1\in S_4$ 将实际 $H$ 的四核重标号至原型I或II，此时同一 $H$ 的 $x$ 星给出 $h$；再用 $\sigma\in\mathrm{Stab}_{S_4}(\mu)$（阶分别为24和8）重标号 $K$ 并固定 $x$，则 $\sigma(\mu)=\mu$ 不变，而 $h$ 运至36份五锁代表之一。五锁库存 $\nu_{2T+1}=h_T,\ \nu_{2T}=\mu_T-h_T$ 是同一 $H$ 的35条原边在 $\{x\}\cup K$ 上的精确迹，固定排列概率界 $\max B=581/585<1$ 直接给出原 $H$ 存在无 critical-pair 的排列，由贪心算法 P1 得到原 $H$ 的合法二染色。

---

#### 3. 定理②审阅：21点八／九度四核三重以上原边覆盖（[TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md)）
* **审阅结论**：**局部数学逻辑与接口严密通过（未发现反例或漏洞）**。
* **已核对的关键量词与同一 $H$ 连接**：
  1. **无隐藏 A1 或全局最大度前提**：定理仅要求 $|V|=21,|E|=35$（简单5-uniform）、覆盖全部点对、指定四核 $K$ 满足 $d_i\in\{8,9\}$、核内6个点对 $\lambda_{ij}\le 4$ 且 $\mu_K\ge 3$。证明全程为 $K$ 上的纯四锁分析，不依赖六度点 $x$ 的存在，也不限制 $V\setminus K$ 中其余17点的度数上限。
  2. **97种高迹域与非负恒等式**：由 $q=\mu_K\ge 3$ 及 $c_P\le 4$ 知 $q\in\{3,4\}$。$q=4$ 时余项全0（1种）；$q=3$ 时任意两三迹交于一点对，若同时出现则该对共度 $\ge 3+1+1=5$ 矛盾，故至多一个三迹：无三迹时6个二迹各取 $0/1$（$2^6=64$种），恰一三迹时4种位置、其内3对二迹必为0、外3对二迹各取 $0/1$（$4\times 2^3=32$种），合计 $64+32+1=97$ 种且无遗漏。单迹 $\mu_{\{i\}}\ge d_i-6\ge 2$，空迹在三类情形下精确恒等式分别为 $35-\sum d_i+9+P\ge 8$、$35-\sum d_i+11+P\ge 10$、$47-\sum d_i\ge 11$，均严格为正。
  3. **嵌套配额调用与度保持排序运输**：对实际 $H$，先将 $K$ 按度数非降序排入5种度谱（`8888`至`9999`，共 $97\times 5=485$ 标签），再仅按保持度数向量 $d$ 的子群 $\mathrm{Stab}_{S_4}(d)$（阶24/6/4/6/24）取商得135个代表（[GENERATE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_mixed_q3_20261020/GENERATE.py#L13)、[VERIFY.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/high_four_core_mixed_q3_20261020/VERIFY.py#L28) 均显式限制 `ds[p[i]]==ds[i]`，未混用八/九度交换）。在 [replay.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyone-delta5/replay.py#L17-L23) 中，总配额 $q_i=\lceil(4d_i-20)/3\rceil$ 由点对覆盖与5-边简单性（link交 $\le 3$）保证，纯单迹配额 $q_i^{\mathrm{pure}}=\max(0,\lceil(4\mu_{\{i\}}-17)/3\rceil)$ 由 $\mu_{\{i\}}$ 条纯单迹边在17个自由点上的占用盈余保证；先在纯单迹槽内取最小非负双方向权，再在剩余槽补足 $\max(0,q_i-q_i^{\mathrm{pure}})$，且各锁点仅在各自锁定位置 $k=\mathrm{pos}(s_i)$ 扣除，无重复计数。135代表界全部 $<1$（最大 $12003/12155$），直接返回同一实际 $H$ 的 proper 2-染色。

---

#### 4. 边界声明
* **算术核验与模型意见分离**：上述结论为对纸面推导、量词边界与生成/验证代码结构的静态数学审阅；确定性算术证书由主代理已执行的 `VERIFY.py` 承担。
* **范围界定**：两份定理分别闭合了“21点A1四交核全为八度点（$q\ge 2$）”与“21点八/九度四核 $q\ge 3$（核内共度 $\le 4$）”两个具体子类；包含至少一个九度核点的 $q=2$ 混合四核、高三核剩余部分及 $m(5)\ge 36$ 其余开放分支仍保持开放。


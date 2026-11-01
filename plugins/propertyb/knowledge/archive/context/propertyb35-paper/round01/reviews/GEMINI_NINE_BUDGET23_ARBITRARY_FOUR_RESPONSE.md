### 审阅结论
**无实质问题（数学推导、域差分与精确有理证书链路完全严密成立，无必须修改项）。**

---

### 一、实际读取文件范围与执行状态
- **读取文件**（纯静态审阅，未执行任何 Python 脚本、LP 求解器或 Lean）：
  1. [NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md#L1-L671)（第 1–60 行主定理声明，第 500–671 行预算 21 与预算 23 扩展及任意负四数量推论）；
  2. [COROLLARY_BUDGET23.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/COROLLARY_BUDGET23.md#L1-L110)（全文）；
  3. [DIFFERENCE.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/DIFFERENCE.py#L1-L40) 与 [DIFFERENCE.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/DIFFERENCE.json#L1-L200)；
  4. [VERIFY_NEW.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.py#L1-L89) 与 [VERIFY_NEW.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.json#L1-L57)；
  5. [CHECK_SCALARS.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/CHECK_SCALARS.py#L1-L43) 与 [CHECK_SCALARS.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/CHECK_SCALARS.json#L1-L200)；
  6. [SOLVE_NEW.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/SOLVE_NEW.json#L1-L900) 及第 1400–1565 行（顶层信息与首份完整有理证书结构）。
- **未核部分**：未重新运行 SciPy LP 求解器，也未逐行通读 `SOLVE_NEW.json` 全部 28,382 行文本（已由 [VERIFY_NEW.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.py#L29-L64) 的精确 `Fraction` 校验逻辑与 [VERIFY_NEW.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.json#L1-L57) 覆盖）。

---

### 二、五项重点攻击核验

1. **总关联不等式 $36+3t+4b\le 126,\ t\le 3 \implies t+b\le 23$ 的量词与重复索引**：
   - 定理前提为 $|L|\le 18$、恰 9 个带索引正四集、$t\le 3$ 个带索引负三集、$b$ 个带索引负四集，且每点在全部正负索引中总出现 $\le 7$。
   - 每个正四集、负三集、负四集本身为 $L$ 的 $4,3,4$ 元子集（内部无重点），不同索引可对应同一集合。对 $v\in L$ 按索引重数求和得：
     $$36 + 3t + 4b = \sum_{v\in L}\mathrm{deg}(v) \le 7|L| \le 126 \implies 3t + 4b \le 90.$$
   - 对整数 $t\in\{0,1,2,3\}$，$b\le \lfloor(90-3t)/4\rfloor$ 依次给出 $b\le 22, 21, 21, 20$，从而 $t+b\le 22, 22, 23, 23 \le 23$。全程直接作用于原带索引计数 $t,b$，无需任何去重假设。

2. **基础全部解析分支的预算更新（无遗漏依赖 $b$ 处）**：
   - **$a\le 2$**：坏概率上界 $tp^3+bp^4$（$p=7/16$），因 $p^3>p^4$，在 $t\le 3,\ t+b\le 23$ 下取 $t=3,b=20$ 达最大：$3(7/16)^3+20(7/16)^4 = 16121/16384 < 1$。
   - **$a\ge 5$**：固定 $a_x\ge 5$ 的 $x$ 红（$u+v\le 2$）。余 $\le 3$ 族或余 $4$ 族相交时，所有候选大小 $\le 4$ 且含 $x$（或含 $\{x,y\}$），不含核点的负四集因大小 $4$ 无法包含于候选，完全不依赖总 $b$；仅余 $4$ 族两两不交的 $256$ 份五红候选依赖 $b$，堵数 $16u+4(t-u)+4v+(b-v)\le 56 < 256$。
   - **$a=4$（附录 A）**：余五族有三重点 $y$ 时候选大小 $\le 4$ 且含 $\{x,y\}$，不依赖 $b$；余五族最大出现 $\le 2$ 时，$M_2\ge 7$ 用四红候选（含 $x$）堵数 $\le 12<14$ 不依赖 $b$；$M_2=0$ 星/三角堵数 $65\to 68<80$；$1\le M_2\le 6$ 旧 86 型堵数 $155\to 158<178$；$E=3$ 七型各自 $C_4$ 与 $S_u,h_3$ 不变，$b$ 上限加 3 使每型最大堵数恰加 3，最小余量 $23\to 20>0$（[CHECK_SCALARS.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/CHECK_SCALARS.py#L18-L24) 逐型核对）。
   - **$a=3$ 双三中心（附录 B）**：$n\le 2$ 时，三/四红候选含 $\{x,y\}$，五红候选 $\{x,y,a_1,b_1,c_1\}$ 在 $\{x,y\}$ 外仅有 3 点，故**无核负四集无法包含于任何候选**，所有堵界仅依赖核发生预算 $8$ 与 $t\le 3$，完全独立于总 $b$；$n=3$ 换色调用的六混合辅助门本就允许任意数量负四集。
   - **$a=3$ 六标签图域（§5 及附录 C、D）**：$M_3\ge 14$ 用四红候选（含 $x$）堵数 $\le 13<14$ 不依赖 $b$；两孤立标签（附录 C）中 $K\ge 5$（$68\to 71<80$）、$K=4,u\le 2$（$59\to 62<64$）、$u=3$ 非三互异最大目标（$60\to 63<64$）均严格，而余 16 候选共享 $Z$ 分支仅用 $Z$ 点负预算 $\le 5$ 与 $v\le 1$（$\le 9<16$），不依赖 $b$；唯一整数型（附录 D）仅用 $u+s\le 3,\ u+v\le 4$ 及 $z$ 的负容量 $\le 5$，从未用 $t+b$。

3. **981 轨道在预算 23 下的精确键集分区**：
   - 在 $t+b\le 23$ 下，最坏参数 $b=23-t\ge 20\ge 4\ge v$ 仍支配全部合法 $b$，使 $B_3$ 不变、$B_4$ 恰增 3（即原 `C4_margin <= 3` 为新失败条件）。
   - [VERIFY_NEW.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.py#L15-L23) 与第 73–80 行直接对 981 个轨道 key 验证集合分拆：`raw_sum_strict`（883 轨道 / 374,923 图）、`two_isolates_extra`（2 轨道 / 270 图）、`olddual`（76 轨道 / 34,035 图）、`integer`（1 轨道 / 60 图）、`newdual`（19 轨道 / 8,040 图）五类两两不交且并集严格等于全部 981 个轨道 key。

4. **旧 76 成本更新、新 19 全部 63,036 条列不等式与 $T_3/Bx_3$ 分离**：
   - 旧 76 份证书的列不等式与 $\gamma=\varnothing$ 不变，总负数右端 $20\to 23$ 使目标上界精确增加 $3\beta_{\text{total}}$（`3 * F(c['budget_weights'][2])`，已含原舍入修补项），全部 76 份仍 $<1$，最大仍为 $10/11$。
   - 新 19 份证书由 [VERIFY_NEW.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/budget23_exploration/VERIFY_NEW.py#L29-L64) 独立重建六正集与 $C_3\cup C_4$ 候选，验证 $\alpha_R\ge 0,\ \sum\alpha_R=1,\ \beta\ge 0,\ \gamma=\varnothing$，并遍历 $U$ 的全部二元（`N2`）、三元（`T3` 与 `Bx3` 分别核验，不混用 $T$ 预算 $\beta_0$ 与 $x$ 预算 $\beta_1$）、四元（`N4`）子集共 **63,036 条**有理不等式，预算 `[3,4,23] + [7-g_v]` 下成本全部严格 $<1$（最大 $436/629$）。

5. **真实输入到图域及证书的运输**：
   - 同一次 $S_6$ 标签置换与共享/私有点双射同时运输正集、横截候选、四类负目标及点容量 $7-g_v$。
   - 已由 $x$ 命中的三个正集若含 $v\in U$，只会使 $v$ 的真实剩余负容量 $\le 7-f_v \le 7-g_v$；因点乘子 $\beta_{3+v}\ge 0$，用 $7-g_v$ 只会放大上界（更安全）。$U$ 外点不在任何候选 $R\subseteq U$ 中，含 $U$ 外点的负目标对候选阻断权重为 $0$ 且只消耗非负预算，忽略完全安全；$\gamma=\varnothing$ 保证重复负索引可直接按原重数相加。


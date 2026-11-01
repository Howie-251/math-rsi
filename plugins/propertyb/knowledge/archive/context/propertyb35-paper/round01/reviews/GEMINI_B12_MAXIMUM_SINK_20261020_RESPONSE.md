### 审阅结论：通过（局部源态结构排除成立，无反例或量词漏洞）

在同一个 25 点、35 边、简单、点对覆盖、含六度点且非 Property B 的 5-uniform 超图 $H$ 上，在所有“唯一坏边 $G$ 含至少一个六度点、规范 $G \subseteq R$”的二染色源中，先全局最小化蓝点数 $b = 12$，再二级最小化 $u = N_1 - 12$。若该二级最优源满足跨色点对超额 $c = 0$，则必有
$$u + N_2 \ge 4 \quad (\text{等价于 } \delta_B + 2u \le 14).$$
这一结论是**同一超图 $H$ 在二级最优源上的局部源态界**，不声称任意最小蓝 12 源均满足此界，也不声称已将原超图 $H$ 二染色或闭合 $m(5) \ge 36$。

---

### 逐项核对记录

1. **二级最小 $u$ 基础界与 $u > 0$ 三端、A 型三角汇点排除（[SECONDARY_MIN_U.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/b12_red_sink_20261020/SECONDARY_MIN_U.md)、[B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md)）**
   - **二级最小 $u + N_2 \ge 3$**：[SECONDARY_MIN_U.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/b12_red_sink_20261020/SECONDARY_MIN_U.md#L13-L76) 在不要求 $c = 0$ 的一般情形下排除 $(u, N_2) \in \{(0, 2), (1, 1), (2, 0)\}$。交换 $h \in Z$ 与唯一私有蓝邻点 $y$ 保持 $G$ 为唯一坏边且 $b = 12$，精确迁移 $u' = u - (a - 1) + \nu_2(y, \bar{h})$ 与二级最小性 $u' \ge u$ 迫使所有汇点度数 $\ge 7$，再由跨色共度预算 $\sum_{h \in Z} \kappa_h \le 2c$ 导出严格矛盾（包括 $(2, 0)$ 中 $a = 4$ 必含两个双私有蓝点各共度 $\ge 2$ 得 $\kappa_h \ge 2$）。
   - **$c = 0$ 下 $u + N_2 = 3$ 的三个 $u > 0$ 端**：[B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md#L22-L44) 中 $(3, 0)$ 给 $u' = -2 < 0$，$(2, 1)$ 给 $u' \le 1 < 2$，$(1, 2)$ 迫使 $|S| \ge 2$ 且每个汇点必为 $(2, 2, 2, 0)$，从而两个汇点同在两条 $N_2$ 中违反 $\lambda(h_1, h_2) = 1$。
   - **$(u, N_2) = (0, 3)$ 下 A 型汇点 $(3, 0, 3, 0)$ 的排除**：[B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md#L53-L81) 对 A 型汇点 $h$，交换 $h$ 与 $y \in Y_h$ 的 $u' \ge 0$ 迫使 $\nu_2(y, \bar{h}) = 2$，故三条 $N_2$ 的蓝二元迹在 $|Y_h| = 3$ 上构成三角形，且 $2 n_3(y) + n_4(y) = 3, n_3(y) + n_4(y) \ge 3$ 直接迫使 $y$ 为 $(1, 2, 0, 3), d_H(y) = 6$。对每个 $y \in Y_h$ 作 $(h, y)$ 交换，因无B 型汇点，任何不属 $X_h$ 的原 $N_4$ 属主若丢失一条 $N_4$ 就会产生新B 型或度 $\ge 7$ 汇点，故 $Y_h$ 的全部 $9$ 次 $N_4$ 关联只能落在 $|X_h| = 3$（每个 $x \in X_h$ 恰 $n_4(x) = 1$）中，迫使每条 $Q(x)$ 含整个 $Y_h$，与 $Y_h$ 已在 $N_2$ 中成三角形矛盾。

2. **每次交换保持全局 / 二级 / 第三级域及 $y \in Y_i$ 的 $(1, 1, 2, 2)$ 刚性（[B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L41-L58)）**
   - **全局与二级域保持（含一处可顺手写明的 1 行衔接）**：对 B 型汇点 $h_i$ $(2, 2, 2, 0)$ 与 $y \in Y_i$，交换 $(h_i, y)$ 不触碰 $G$（因 $h_i \notin G, y \in B$），无新全蓝边（$n_4(h_i) = 0$），无新全红边（$u = 0$ 使 $F_y$ 唯一且 $h_i \in F_y$），$b' = 12$，且 $u' = 0 - 1 + \nu_2(y, \bar{h}_i) \ge 0 \implies \nu_2(y, \bar{h}_i) = 1$（即 $y \in E_i$）且 $u' = 0$。
   - **为何 $y \in Y_i$ 必有 $d_H(y) = 6$ 与 $(1, 1, 2, 2)$（从而保证 $c' = 0, N'_2 = 3, \delta'_B = 15$）**：
     在 [B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md#L55-L64)（及 [CHECK_B12_MATCHING_SINK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/CHECK_B12_MATCHING_SINK.py#L16-L24) 第 21 行直接写 `1 + n2 + n3 + n4 == 6`）中，仅由 $n_1(y) = n_2(y) = 1$、红蓝单位共度 $2 n_3(y) + n_4(y) = 6$ 和 $d_H(y) = 2 + n_3(y) + n_4(y) \ge 6$，整数解本有 $(n_3(y), n_4(y)) \in \{(2, 2), (1, 4), (0, 6)\}$。但因为交换 $(h_i, y)$ 后的新源 $(R', B')$ 已有 $b' = 12, u' = 0$，它本身就是同一 $H$ 的**二级最小 $u$ 源**；其精确新 $N'_2$ 数为
     $$N'_2 = N_2 + (a - 1) - \nu_2(y, \bar{h}_i) - b_{h_i} + \nu_3(y, \bar{h}_i) = 3 + 1 - 1 - 2 + n_3(y) = 1 + n_3(y).$$
     直接调用已导入的 [SECONDARY_MIN_U.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/b12_red_sink_20261020/SECONDARY_MIN_U.md#L9) 主定理（对任意二级最小 $u$ 源无需 $c' = 0$ 恒有 $u' + N'_2 \ge 3$），立得 $1 + n_3(y) \ge 3 \implies n_3(y) \ge 2$，从而唯一迫使 $(n_3(y), n_4(y)) = (2, 2), d_H(y) = 6$，并同时保证交换后 $N'_2 = 3, N'_4 = 14 - n_4(y) = 12, c' = n_4(y) - 2 = 0, \delta'_B = 15 - 6 + 6 = 15$。因此交换严格保持 (1) 的全部条件。
   - **第三级汇点集 $S$ 的迁移与最大性约束**：
     - $h_j \in S \setminus \{h_i\}$ 与 $h_i$ 已在某条 $N_2$ 中同现，由 $d_H(h_i) = 6 \implies \lambda(h_i, h_j) = 1$ 知过 $h_i$ 的两条 $N_3$ 不含 $h_j$，故 $X_i \cap S = \varnothing$ 且 $|X_i| = 2$，$S \setminus \{h_i\}$ 仍为汇点；
     - $y$ 与 $h_i$ 已在 $F_y$ 中同现，不过 $h_i$ 的 $N_3$，且原无全蓝五边，故 $n'_4(y) = 0$，$y$ 必成为新汇点；
     - 对任意 $v \in R \setminus \{h_i\}$，精确变化为 $n'_4(v) = n_4(v) + \mathbf{1}_{v \in X_i} - \mathbf{1}_{y \in Q(v)}$。因此 $X_i$ 中点不可能变为汇点，而在 $R \setminus (S \cup X_i)$ 中任何含 $y$ 的单 $N_4$ 属主（$n_4(v) = 1$）都会变为新汇点使 $|S'| > s$。由 $s$ 的第三级最大性，含 $y \in Y_i$ 的任何单 $N_4$ 属主必属于 $X_i$，且此时 $|S'| = s$ 保持第三级最大。

3. **单 / 双 $N_4$ 属主结构与 $s = 1$ 排除（[B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L50-L65)）**
   - 由 $a + 2b + 3 d_3 + 4k = 12$ 与 $a + b + d_3 + k + \mathbf{1}_{v \in G} \ge 6$ 得 $k \le 2$；当 $k = 2$ 时 $b + 2 d_3 \le 1 \implies d_3 = 0, b \le 1$，且 $b = 1 \implies a = 2, v \in G \cap L$。
   - 因 $d_3 = 0$，双属主永不属于 $X_i$；$13 - s$ 个非汇点分担 $N_4 = 12$ 给出恰 $s - 1$ 个双属主与 $14 - 2s$ 个单属主。
   - 因每个 $y \in Y_i$ 均有 $d_H(y) = 6$，故 $\lambda(y_{i,1}, y_{i,2}) = 1$ 已由 $E_i$ 用尽，**任何 $N_4$ 边至多含 $Y_i$ 中一点**。
   - $s = 1$ 时无双属主，$|X_1| = 2$ 个单属主对 $Y_1$ 至多提供 $2 < 4$ 次 $N_4$ 关联，直接矛盾。

4. **$s = 2$ 唯一双属主重复调用与 $X_1 \cup X_2$ 的第二 / 第三条 $N_3$ 穷尽覆盖（[B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L67-L95)）**
   - **原唯一双属主 $p \in G \cap L$**：$Y_1, Y_2$ 各需 4 次 $N_4$ 关联，迫使 $p$ 的两条 $N_4$ 各含 $Y_1, Y_2$ 中一点（耗尽 $p$ 与 $Y_1 \cup Y_2$ 的全部 4 个点对），且每个 $x \in X_i$ 的唯一 $Q(x)$ 恰含 $Y_i$ 中一点（两点 $x_{i,1}, x_{i,2}$ 分别含 $Y_i$ 的两个不同点）。于是 $(p, h_1), (p, h_2)$ 不能由 $N_1$ 覆盖（否则 $p$ 与某 $y \in Y_i$ 重现），也不能由 $N_3, N_4$ 覆盖（$d_3(p) = n_4(h_i) = 0$），只能由同一条 $N_2$ 边 $E_3$ 覆盖，故 $b(p) = 1 \implies p \in G \cap L$。
   - **新双属主证明的可重复调用**：对 $x_{i,1}, x_{i,2} \in X_i$，取 $y \in Q(x_{i,1}) \cap Y_i$（故 $y \notin Q(x_{i,2})$）执行 $(h_i, y)$ 交换。新源 $(R', B')$ 仍满足 (1) 且汇点数仍为最大 $s' = 2$，其中 $x_{i,2}$ 原有 $Q(x_{i,2})$ 未失、又因过 $\{h_i, x_{i,2}\}$ 的 $N_3$ 升格而净得 $n'_4(x_{i,2}) = 2$，成为 $(R', B')$ 的唯一双属主（同时 $n'_4(p) = 1, n'_4(x_{i,1}) = 1$）。由于 $G$ 和原图度数 $L$ 在交换下不变，将 (6) 应用于 $(R', B')$ 即得 $x_{i,2} \in G \cap L$；对 $Y_i$ 另一点同理得 $x_{i,1} \in G \cap L$，故 $X_1 \cup X_2 \subseteq G \cap L$。
   - **$X_i$ 的第二 / 第三条 $N_3$ 穷尽覆盖（含两处可顺手补强的 1 行说明）**：
     - 对 $x \in X_i$ 及 $y'_i \in Y_i \setminus Q(x)$，点对 $(x, y'_i)$ 不能由 $F_{y'_i}$ 覆盖（$h_i \in F_{y'_i}$ 与过 $\{h_i, x\}$ 的 $N_3$ 冲突），也不能由 $E_i$ 覆盖：一方面如 §6 第 117 行所指出，$E_i \cap B = Y_i$ 已含 $Q(x) \cap Y_i$ 中的点，若 $x \in E_i$ 则与该点共度 $\ge 2$；另一方面 $x \in G \cap L, k(x) = 1$ 给 $b(x) + 2 d_3(x) = 4$，因 $x$ 不能入过 $h_i$ 的两条 $N_2$ 故 $b(x) \le 1$，奇偶性直接迫使 $b(x) = 0, d_3(x) = 2$。
     - 若 $x \in X_1 \cap X_2$，为何覆盖 $(x, y'_1)$ 的 $N_3$ 不能就是过 $\{x, h_2\}$ 的那条 $N_3$？因为 $h_2 \in E_1$ 且 $y'_1 \in Y_1 \subseteq E_1$，点对 $(h_2, y'_1)$ **已在 $E_1 \in N_2$ 中覆盖**，由 $\lambda(h_2, y'_1) = 1$ 知过 $h_2$ 的任何 $N_3$ 都不能含 $y'_1$。故 $x \in X_1 \cap X_2$ 必有第 3 条 $N_3$，得 $4(1) + 3(3) = 13 > 12$ 矛盾。
     - 从而 $|X_1 \cup X_2| = 4$ 个不同点全在 $G \cap L$ 中且各有 $d_3(x) = 2$；因 $G$ 已覆盖它们之间的全部点对，这 8 次 $N_3$ 关联对应的 $N_3$ 边两两不同，给出 $N_3 \ge 8 > 7$ 矛盾。

5. **$s = 3$ 双属主共同容量上下饱和与 $N_3$ 关联计数（[B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L97-L125)）**
   - 两个双属主 $p, q$ 若有 $b = 1$（如属于 $E_3$），则与 $h_3 \notin E_3$ 的点对只能由某 $F_{y_3}$ ($y_3 \in Y_3$) 覆盖，但 $Y_3 \subseteq E_3$ 导致 $(p, y_3)$ 在 $F_{y_3}$ 与 $E_3$ 中重现，故 $b(p) = b(q) = 0, a(p) = a(q) = 4$。
   - 每个双属主与 $h_1, h_2, h_3$ 的点对各耗去 $Y_1, Y_2, Y_3$ 中一个蓝点的 $F_y$，该蓝点不能再入该双属主的两条 $N_4$，故每个双属主对 $Y_1 \cup Y_2 \cup Y_3$ 至多提供 $6 - 3 = 3$ 次 $N_4$ 关联，两双属主合计 $\le 6$ 次，与下界 $3 \times (4 - 2) = 6$ 上下饱和，迫使每个 $x \in X_i$ 均有 $|Q(x) \cap Y_i| = 1$。
   - 由此每个 $x \in X_i$ 不能属于 $E_i$（否则与 $Q(x) \cap Y_i$ 共度 $\ge 2$），覆盖 $(x, y'_i)$ 迫使 $d_3(x) \ge 2$；同上，因 $(h_j, y'_i)$ ($j \neq i$) 已由 $E_i$ 覆盖，过 $h_j$ 的 $N_3$ 不含 $y'_i$，故 $X_1, X_2, X_3$ 两两不交（否则 $d_3(x) \ge 3 \implies 4 + 9 = 13 > 12$）。
   - $6$ 个 $X_1 \cup X_2 \cup X_3$ 红点与 $3$ 个汇点 $S$ 共 $9$ 个不同红点各有 $d_3 \ge 2$，给出红 / $N_3$ 关联至少 $18 > 14 = 2 N_3$，矛盾。

---

### 可选文字润色建议（非漏洞，供成稿顺手补足）
1. 在 [B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md#L62-L64)（或 [B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L31-L37)）补半句：B 型汇点的 $y \in Y_h$ 交换后得二级最小 $u' = 0$ 源且 $N'_2 = 1 + n_3(y)$，由 $u' + N'_2 \ge 3$ 迫 $n_3(y) \ge 2$，结合 $2 n_3(y) + n_4(y) = 6$ 排除 $(1, 1, 1, 4), (1, 1, 0, 6)$，唯一得 $(1, 1, 2, 2)$、$d_H(y) = 6$ 及交换后 $c' = n_4(y) - 2 = 0$。
2. 在 [B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md#L89-L93) §5 中，排除 $x \in E_i$ 可直接复用 §6 第 117 行的 $|Q(x) \cap Y_i| = 1$ 共度冲突（或补一句 $x$ 不入过 $h_i$ 的两条 $N_2$ 故 $b(x) \le 1$，由 $b(x) + 2 d_3(x) = 4$ 得 $b(x) = 0$），并在 $x \in X_i \cap X_j$ 处注明 $(h_j, y'_i)$ 已由 $E_i$ 覆盖故不入过 $h_j$ 的 $N_3$。

---

### 实际阅读范围与执行说明
- **已全文只读**：
  - [B12_MATCHING_SINK_MAXIMIZATION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_MATCHING_SINK_MAXIMIZATION.md)（1–132 行）
  - [B12_NEXT_UNIFIED_DIAGNOSIS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/B12_NEXT_UNIFIED_DIAGNOSIS.md)（1–105 行）
  - [SECONDARY_MIN_U.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/b12_red_sink_20261020/SECONDARY_MIN_U.md)（1–91 行）
  - [CHECK_B12_MATCHING_SINK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/CHECK_B12_MATCHING_SINK.py)（1–61 行）与 [CHECK_B12_MATCHING_SINK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfive/source-selection/CHECK_B12_MATCHING_SINK.json)（1–486 行）
- **未执行项**：纯静态只读审阅，未运行任何 Python 脚本、外部程序或 Lean，未修改任何文件。


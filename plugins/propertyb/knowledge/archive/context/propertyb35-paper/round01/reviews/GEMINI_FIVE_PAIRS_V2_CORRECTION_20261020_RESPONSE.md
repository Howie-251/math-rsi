### 有界复核报告：$r=2, v=2$ 修正核查

**读取文件与执行声明：**
* **已读取当前版本（只读未修改）：**
  1. [FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md) 第 4 节（第 35–60 行，特别是第 48 行新版 $v=2$）
  2. [CORRECTION.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/five_negative_pairs_two_triples_20261020/CORRECTION.md)
  3. [INDEPENDENT_AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/root/five_negative_pairs_two_triples_20261020/INDEPENDENT_AUDIT.md) 第 1 节（第 1–22 行）。
* **执行情况：** 纯静态数学复核，**未执行任何程序或 Lean**。

---

### 1. 明确承认初稿 $r=2, v=2$ 子断言反例与上轮漏检

* 上轮我在 09:38:45 读取的是修改前的初稿第 48 行，并在复述时沿用了“若 $K$ 存在第 3 条不含 $f$ 的边，因 $d_K(g) \ge 2$ 且 $g$ 在含 $f$ 的两条边中至多出现一次，该边必含 $g$”这一**错误断言**。
* 该断言在 $\{f,g\}$ 为平行重边时不成立：具体反例为多重集
  $$K = \{\{f,g\}, \{f,g\}, \{a,b\}\}\qquad (a,b \notin \{f,g\}),$$
  此时 $d_K(f) = d_K(g) = 2$ 且 $|K|=3$，但第 3 条负二 $\{a,b\}$ 不含 $f$ 亦不含 $g$，不能因 $g$ 染蓝而消去。初稿该句确有漏洞，上轮静态审阅对此处的通过结论撤回。

---

### 2. 当前新版 $r=2, v=2$ 修法的完整性核查

核对更新后的 [FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md#L48) 第 48 行：
1. **邻点禁集与剩余正集大小：** 由 $2 = v = d_K(f) \le d_K(g)$ 及 $|K| \le 3$，有 $d_K(f)+d_K(g) \ge 4 > |K|$，故 $K$ 中至少有一份 $\{f,g\}$。因此 $f$ 在 $K$ 中的两份关联除 $g$ 外至多涉及另一个邻点 $w$。取 $f$ 红、$f$ 的全部 $K$-邻点（$g$ 及至多一点 $w$）蓝；因 $g \notin A \cup B$，$A'' = A \setminus \{x,w\}$ 与 $B'' = B \setminus \{x,w\}$ 各至多损失 $\{x,w\}$ 两点，大小均 $\ge 4 - 2 = 2$。
2. **剩余负二保留计费：** $K$ 中含 $f$ 的两份负二因邻点全蓝而满足；因 $|K| \le 3$ 且 $d_K(f)=2$，$K$ 中**不含 $f$ 的负二至多 $3 - 2 = 1$ 份**（如反例中的 $\{a,b\}$）。新版不再声称它含 $g$，而是完整保留该负二。
3. **相交与不交两分支：**
   * **若 $A'' \cap B'' \ne \varnothing$：** 取交点 $y \in A'' \cap B''$ 得二元红集 $R = \{f,y\}$。含 $x$ 的负二因 $x$ 蓝安全，含 $f$ 的负二因 $f$ 邻点全蓝安全，唯一可能剩余的不含 $f$ 的 $K$ 边不可能等于含 $f$ 的二元集 $\{f,y\}$，负三及以上大小 $\ge 3$，故 $R=\{f,y\}$ 安全。
   * **若 $A'' \cap B'' = \varnothing$：** 各取一点加 $f$ 得至少 $2 \times 2 = 4$ 个互异三红候选 $\{f,a,b\}$。唯一可能剩余的不含 $f$ 的负二至多堵 1 份（当其恰等于 $\{a,b\}$ 时），至多 $t \le 2$ 个负三各至多堵 1 份，总堵数至多 $1 + 2 = 3 < 4$，必有未堵候选。

---

### 3. 复核结论与范围

* **结论：** 经上述第 48 行局部修正后，[FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FOUR_LARGE_POSITIVE_FIVE_PAIRS_TWO_TRIPLES_REPAIR.md) 的 $r=2, v=2$ 分支（含平行 $\{f,g\}$ 情形）及全文证明严密闭合，未发现其他数学问题。
* **边界声明：** 本次仅针对该通用修复门的修正做静态复核，未执行程序或 Lean，不扩展至实际 caller 或 $m(5) \ge 36$ 全题。


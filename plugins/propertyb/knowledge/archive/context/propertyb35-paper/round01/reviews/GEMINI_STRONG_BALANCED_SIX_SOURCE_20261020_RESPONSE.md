# GEMINI_STRONG_BALANCED_SIX_SOURCE_20261020

### 审阅结论

**PASS（无实质数学缺陷）**。[BALANCED_DELETED_STAR_SOURCE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L88-L184) 末节“21点六度中心：两色各一单色link的加强”的解析推导与算术完全严密，证明了局部源选择引理（未声称完整21点或 $m(5)\ge 36$ 已解决）。

---

### 五项重点独立核算

1. **总重复成本 $4$ 的五种分拆覆盖性（[L92-L96](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L92-L96), [L118-L142](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L118-L142)）**
   - 由点对覆盖，其余 $20$ 点与 $x$ 的点对均被过 $x$ 的六条五元边覆盖，故每个 $v\in V(H)\setminus\{x\}$ 在六条四元 link $L_1,\dots,L_6$ 中的出现重数 $r_v\ge 1$。
   - 由 $\sum_{v\neq x} r_v = \sum_{i=1}^6 |L_i| = 24$，必有 $\sum_{v\neq x}(r_v-1)=24-20=4$。
   - $r_v=1$ 的点对交数 $m_{ij}=|L_i\cap L_j|$ 贡献为 $0$；正整数分拆 $p(4)=5$ 恰为 $1+1+1+1$、$2+1+1$、$2+2$、$3+1$、$4$，完整穷尽任意实际六度中心星的重复点重数分布。

2. **每对 link 交数 $m_{ij}\le 3$ 与简单性（[L99](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L99)）**
   - 若某对 $i<j$ 满足 $m_{ij}=4$，因 $|L_i|=|L_j|=4$，必有 $L_i=L_j$，从而两条过 $x$ 的原五元边 $L_i\cup\{x\}=L_j\cup\{x\}$ 重合，与“35条互异五元边”矛盾。故 $m_{ij}\in\{0,1,2,3\}$ 完全由超图简单性保证（事实上后四种分拆至多 $3$ 个重复点，自动满足 $m_{ij}\le 3$；简单性排除 $1+1+1+1$ 中四点支持同为 $\{i,j\}$ 的情形）。

3. **$\max(A,B)\ge 2$ 并界与五种最大分子（[L99-L142](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L99-L142)）**
   - 固定 $i<j$，$|L_i\cup L_j|=8-m_{ij}\le 8$，在 $20$ 点中均匀选 $10$ 红、$10$ 蓝时，$L_i\cup L_j$ 全红（或全蓝）的染色数均为 $f(m_{ij})=\binom{20-(8-m_{ij})}{10-(8-m_{ij})}=\binom{12+m_{ij}}{2+m_{ij}}$。
   - 对 $\binom{6}{2}=15$ 个无序对与红蓝两色作并界，分子上界为 $2\sum_{1\le i<j\le 6}f(m_{ij})$。
   - 独立复算：$f(0)=66,\ f(1)=286,\ f(2)=1001,\ f(3)=3003$，一阶差分 $220,715,2002$ 严格递增（严格凸）：
     - **$1+1+1+1$**：$\sum m_{ij}=4,\ m_{ij}\le 3$，由凸性在 $(3,1,0^{13})$ 达最大，$2(3003+286+13\times 66)=8294$。
     - **$2+1+1$**：基态 $K_3$（三边重 $1$）加两条边，叠在同一 $K_3$ 边增量 $f(3)-f(1)=2717$，分落两条 $K_3$ 边增量 $2(f(2)-f(1))=1430$，其余含空边分配增量 $\le 935$；最坏 $(3,1,1,0^{12})$ 给 $2(3003+2\times 286+12\times 66)=8734$。
     - **$2+2$**：两 $K_3$ 支持交大小 $s\in\{0,1,2,3\}$，公共边数 $\binom{s}{2}\in\{0,1,3\}$，对应分子 $4620,5610,7590$，最大 $2(3\times 1001+12\times 66)=7590$。
     - **$3+1$**：$K_4$（六边重 $1$）加一边，落入 $K_4$ 内较大，$(2,1^5,0^9)$ 给 $2(1001+5\times 286+9\times 66)=6050$（落外部为 $5060$）。
     - **$4$**：单一 $K_5$（十边重 $1$），$(1^{10},0^5)$ 给 $2(10\times 286+5\times 66)=6380$。
   - 全局最大分子确为 $8734$。

4. **联合并界与分数化简（[L144-L161](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L144-L161), [L173-L179](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L173-L179)）**
   - 同一 $10/10$ 平衡染色下，$H-x$ 的 $29$ 条五元边每条单色染色数为 $2\binom{15}{5}=6006$。
   - 联合坏染色数至多 $29\times 6006+8734=174174+8734=182908 < \binom{20}{10}=184756$，余量 $1848$ 份，$\frac{182908}{184756}=\frac{4157}{4199}<1$（分子分母同除以 $44$）。
   - A1 角色（分拆 $1+1+1+1$）为 $\frac{174174+8294}{184756}=\frac{182468}{184756}=\frac{319}{323}<1$（同除以 $572$），余量 $2288$ 份。

5. **非 B 下 $N_4(x)=1$、$F\cap G=\{x\}$ 及反向源接口（[L163-L169](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L163-L169)）**
   - 在 $H-x$ proper 且 $A,B\le 1$ 的 $10/10$ 染色下，若 $A=0$（或 $B=0$），给 $x$ 染红（或蓝）即得 $H$ 的 proper 二染色，故非 B 必迫使 $A=B=1$。
   - 令 $x$ 染红（全局 $11$ 红 $10$ 蓝）：唯一全红 link $L_{i_R}$ 给出唯一全红坏边 $G=L_{i_R}\cup\{x\}$；过 $x$ 的 $1$ 红 $4$ 蓝边由于 $x$ 为红，其 link 必全蓝，故由 $B=1$ 唯一确定为 $F=L_{i_B}\cup\{x\}$，即 $N_4(x)=1$。
   - 因 $L_{i_R}\subseteq R,\ L_{i_B}\subseteq B$ 在 $V(H)\setminus\{x\}$ 上颜色互斥，$L_{i_R}\cap L_{i_B}=\emptyset$，故 $F\cap G=\{x\}$。
   - 将 $x$ 翻蓝并全局红蓝互换，限制在 $V(H)\setminus\{x\}$ 上仍是 $A=B=1$ 的 $10/10$ proper 染色，此时 $F$ 变为唯一全红坏边、$G$ 变为过 $x$ 的唯一 $1$ 红 $4$ 蓝边，确仍留在该源域内。

---

### 实际读取范围与未核范围

- **实际读取范围**：完整读取 [BALANCED_DELETED_STAR_SOURCE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/BALANCED_DELETED_STAR_SOURCE.md#L1-L184) 全文（第 1–184 行），并独立手算核对了末节（第 88–184 行）及前置一般引理（第 5–86 行）的全部组合恒等式、凸性极值与概率并界。
- **未核范围**：未读取或运行外部脚本 `CHECK.py`、`CHECK_GENERAL.py` 及 `REPORT.md`；未核验后续利用该源进行私有边交换修复的下游分支，亦未评估 21 点其余分支或 $m(5)\ge 36$ 其它义务。


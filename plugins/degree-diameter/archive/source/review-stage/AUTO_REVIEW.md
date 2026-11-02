# Current V3 checkpoint — 2026-10-13 16:32 UTC

Goal ACTIVE, 57<=N(8,2)<=61 unchanged. No target above57 and no whole58–61 exclusion. Current sole plan DD82_V3_ARIS_GEMINI_PLAN_20261013.md; old62–65/Lean frozen.

New main mechanism dd82-v3-polarity73-reduction-20261013, obligation prompts/26101316-1/task.md: choose ANY58/59 survivors of the classical73-point GF(8) orthogonal polarity graph, retain all old surviving edges, add arbitrary missing edges. Ambient geometry and monotonicity are artificial construction restrictions; no fixed deletion set or automorphism. Prior internal-double loop remains closed4/4 and is not reset.

Actual short geometry.py generation produced73vertices324edges, degrees8x9/9x64, max common-neighbor count1,84triangles, nine7-point outer fibers. geometry.edges/json under computations/dd82/construction/polarity73_reduction_run/ are ambient data, NOT a degree8 target. Writer/root derivation POLARITY73_REDUCTION_CANDIDATE.md excludes all monotone60/61 by triangle counting and retained-nucleus degree9, excludes deletion of the whole absolute line, and proves58/59 need at least8deleted outer points. Fresh source/mathematical same-family provisional check by internal_double_source_check found no blockers; no external acceptance yet.

Additional actual two_fiber_examples.json diagnostics: selected two-fiber58 has301badpairs and28required newedges;59 has282badpairs and24newedges. Pure local coverage excludes the59 deletion shape. At58 all7 whole-fiber perfect codes fail, other perfect codes not yet enumerated. A one-shot <=5CPU-second/1e6-node exact-cover diagnostic has been assigned for this specific58 shape; no target or general-family inference. No SAT encoder or solver launched.

Gemini round1 direction review IN FLIGHT functions.exec cell1024, rawdestination reviews/dd82/20261013_V3_polarity73_direction.json, actualthreadIDpending. Requestedgemini-3.8-flash-high/high; wait actual result, no duplicate. Frozen actualprompt .aris/traces/auto-review-loop/dd82-v3-polarity73-reduction-20261013/001-direction-prompt.md. Max4substantive rounds withfullmemory; nextdecision mustuse actualreview and observations, notautomaticbiggerdelete/repairladder.

Parallel bounded writer task completed proofs/dd82/n61/INTERNAL_DOUBLE_GLOBAL_RUN_STRUCTURE.md: globaldisjoint internal-D witness sets, their exact neighborhood defect patterns and induced weighted path/double-edge structure. Writer-only, root-read, NO freshproof-checker orGemini acceptance and no61contradiction. It is notpartofpolarityreview orreason toresetoldSAT.

Current ARIS DD82 adaptation uses local2026-10-08 research-pipeline/idea-discovery/formula-derivation/proof-writer/experiment-bridge and same-mechanism auto-review-loop, existingAntigravityonly. No hashes,newCLI,scoring,rendering,scheduler. AGENTSquestionalreadyanswered withspecificV2omissionsversusconditional/laterrequirements; do notappendanothercomplianceaudit.


## Actual round1 returned; decision

# Round1 root decision and actual review scope

Run dd82-v3-polarity73-reduction-20261013, thread 836dc422-ed04-4f1d-99f2-216fb8d7bae5. Actual existing Antigravity result status SUCCESS; requested and CLI-reported gemini-3.8-flash-high/high, selected label Gemini 3.8 Flash (High); not independent backend attestation. Full raw response reviews/dd82/20261013_V3_polarity73_direction.json.

The reviewer actually reports reading the classical Brown source pp350–352, geometry.py, only the start of geometry.json, and V3plan lines1–150. It did not report reading the now-complete POLARITY73_REDUCTION_CANDIDATE.md or new two-fiber exact-cover result. Its positive verdict accepts the provided60/61 pure monotone obstruction, all-absolute-deletion obstruction and saturated-neighbor rule. It supports one bounded full-deletion necessary-condition screen. It does not accept the newer f>=8 proof, specific59 proof or complete7-code58 result yet.

Root decision: implement the full73 deletion domain screen at58/59 once each, with exact survivor and saturation guards; no fixed deletion set, automorphism or edge completion restriction besides this necessary screen. The local f>=8 proof received a separate fresh same-family provisional mathematical check and will be explicitly submitted at next review. The source will be checked and semantic sanity run before solving. A SAT screen assignment remains a deletion candidate, not a target. On UNSAT require exact-input LRAT and coverage before family exclusion.

Corrections retained for next same-thread review:
- The assertion of guaranteed sub-second SAT is unsupported; use measured bounded profiles. 73 are primary deletion variables, not the total after exact auxiliary encodings.
- The response's aggregate saturated-vertex linear relaxation is unproved and is NOT used. Absolute saturated vertices may have no deleted neighbor, so simple incidence counting needs care.
- The proposed singleton-deleted-neighbor rule must explicitly include retained endpoints and their original degrees. Our exact sat indicators enforce retainedness, count1 for degree9, count0 for degree8, followed by the general deleted-common-neighbor clause.
- SAT of necessary conditions is not feasibility of the final monotone graph; UNKNOWN and unfinished proof logs give no exclusion.

Actual additional work while review ran: all7 whole-fiber codes failed in selected58 deletion; then exhaustive exact-cover diagnostic completed98nodes7codes in0.002408CPU/0.008827wall, all eliminated by exact per-code matching-capacity test. NoSAT, no target, only the saved fixed a=1,b=8 shape. The selected59 shape has a complete pure coverage contradiction. These are new objects and deductions, not selection-only paperwork.

Fresh local check of geometry and note sections1–5 returned PASS same-family provisional from internal_double_source_check after direct file reading, without executing source or solver; its full message is preserved below:
"GF(8) multiplication/projective normalization and ambient counts correct;60/61 f>=13 contradiction valid; f=7 equalities force an entire outer fiber, while at least5/6 deleted-parent fibers need distinct core vertices but only3/2 remain; deficit, lost-pair and saturation rules valid. Scope strictly monotone, screenSAT not a graph." Later section6/source deltas remain separately pending.



## dd82-n61-global-spectral-20261019

# 本次外审处置

2026-10-19 11:32:48 UTC。实际Antigravity线程 3dc745b1-1a9a-4d06-810e-32310f2b9dab，请求与返回 gemini-3.8-flash-high / high，SUCCESS。模型名仅按工具元数据记录。

范围内接受：完整因子提升、同一整数重数与混合迹、T=40排除、关联L满秩及投影必要界。其结论不是整个n61完成，也不是Lean验收。

根拒绝三项超出证据的表述：
- “K is NOT A-invariant”未被证明；准确说法为尚未证明K不变。K甚至可能为零，不能由存在跨类邻边直接断言所有流都外泄。
- “strict subspace”未被证明；只能写K⊆E。
- “defect-free”不适用于d=0：它仅无双重缺陷，B仍行和4。

关于E/K注入低三角坐标的建议成立；但维数夹逼和偶性本身尚无矛盾。根在研究中已继续证明准确闭包K+AK及外泄恒等式，见稿§6.1，单独记本地纸面推导，未借这份回执扩充接受范围。后续不自动枚举T=39或35–39。

本次有界检查在第1轮结束，不为了泛化措辞另开追问。所有原始意见保留，未把意见共识当数学证明。整体Goal ACTIVE。



### 原始回执

### 1. Mathematical Review Verdict: SCOPED ACCEPT

The mathematical claims in [`GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n61/GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md) are **SCOPED ACCEPT**. Every stated necessary theorem, algebraic identity, moment reduction, combinatorial bound, and matrix inequality is verified to be mathematically rigorous and free of false claims.

#### Specific Verification of Stated Claims:
1. **Arbitrary Irreducible-Factor Square Criterion (Theorem 1, §1):**
   - *Verified.* For an arbitrary degree $d_i$ irreducible factor $f_i \in \mathbb{Q}[t]$ of $q_B$, the condition $D_i = 29 + 4\beta_i \in K_i^2$ where $K_i = \mathbb{Q}(\beta_i)$ is exact. Because all conjugates of $\beta_i$ lie in $[-4, 4]$ from the graph degree bound, $D_i \ge 13 > 0$ is totally positive and non-zero.
   - When $D_i \notin K_i^2$, $[K_i(\alpha_i) : K_i] = 2$, proving $f_i(x^2+x-7)$ is irreducible of degree $2d_i$ over $\mathbb{Q}$.
   - When $D_i \in K_i^2$, $\alpha_i \in K_i$ has rational degree $d_i$. The roots partition into two disjoint Galois orbits of size $d_i$ because $2\alpha_i + 1 = \sqrt{D_i} \neq 0$ prevents self-duality ($g_i \neq g_i^*$). Factorization into two distinct monic integer irreducible polynomials $g_i, g_i^*$ of degree $d_i$ is airtight.
2. **Full Integer Lifting Multiplicities and Trace 44 (Theorem 2 & §2):**
   - *Verified.* Unsplit factors $f_i \circ \phi$ ($i \in N$) are self-dual under $x \mapsto -1-x$, forcing their multiplicity $m_i$ in $q_B$ to be **even**, and their contribution to $r_A(x)$ is $(f_i \circ \phi)^{m_i/2}$. In the non-principal subspace $W = \mathbf{1}^\perp$, their $X$-eigenvalues pairwise cancel ($\gamma - \gamma = 0$), contributing exactly $0$ to $\operatorname{tr}(X|_W)$.
   - Split factors ($i \in S$) allow integer multiplicities $u_i, v_i \ge 0$ with $u_i + v_i = m_i$, giving net trace $(u_i - v_i) \operatorname{Tr}_{K_i/\mathbb{Q}}(\gamma_i) = k_i t_{i,0}$. The identity $\sum_{i \in S} k_i t_{i,0} = 44$ with $k_i \equiv m_i \pmod 2$ and $t_{i,0} \equiv d_i \pmod 2$ is exact.
3. **Redundancy of Second Moment (§3):**
   - *Verified.* Since $\operatorname{tr}(B|_W) = -4$, the identity $\operatorname{tr}(X^2|_W) = 29 \times 60 + 4(-4) = 1724$ is automatically fixed by the graph degree. Combining $\operatorname{tr}(X|_W) = 44$ and $A = (X-I)/2$ algebraically forces $\operatorname{tr}(A^2|_W) = \frac{1}{4}(1724 - 88 + 60) = 424$. The draft's explicit classification of $\operatorname{tr}(A^2|_W) = 424$ as a redundant dependent relation (rather than an independent obstruction) is mathematically rigorous.
4. **Mixed-Trace Constants and Row-Support Bounds (§3–5):**
   - *Verified.* For all powers $j \ge 0$, the exact same integer vector $k = (k_i)_{i \in S}$ governs the mixed moments: $M_j = \operatorname{tr}(X B^j|_W) = \sum_{i \in S} k_i t_{i,j}$.
   - For $j = 1$: $\operatorname{tr}(AB) = 6T$, yielding $M_1 = 12T - 68$.
   - 4-cycle and triangle relation: $2C_4 + 3T = 122 + d$ with $2d + 3T \le 122$ and $T \equiv d \pmod 2$ is verified from the absence of edge-sharing triangles ($(A^2)_{uv} \le 1$ on edges).
   - For $j = 2$: Closed walk counts $\operatorname{tr}(A^4) = 7808 + 4d - 12T$, $\operatorname{tr}(A^5) = 10C_5 + 210T$ and $w = \operatorname{tr}(AB^2) = 10C_5 + 108T + 8d - 24888$ are exact.
   - The row-support bound $w_v \le 12 - 2a_v - 4t_v$ correctly yields $6T \le w \le \min(488 + 2h_1, 732 - 4d - 12T)$ and the two-sided bounds on $M_2$.
5. **Universal $T = 40$ Exclusion and Full-Rank Triangle Incidence (§6):**
   - *Verified.* The decomposition $B + 2I = L L^T + \operatorname{diag}(2-t) + R$ with $R \ge 0, R\mathbf{1} = 4\mathbf{1} - 2t$, and $R_{uv} > 0 \implies A_{uv} = 0$ is exact.
   - For $T = 40$, $\sum (2-t_v) = 2$. If one vertex has $t_v = 0$, its row sum in $R$ is 4 while all other 60 vertices have row sum 0, impossible for a non-negative symmetric matrix. If two vertices have $t = 1$, they force $R_{uv} = 2$ and $d = 1$, contradicting the parity constraint $d \equiv T \pmod 2 \equiv 0 \pmod 2$. This universally closes $T = 40$.
   - The incidence Gramian $L^TL = 3I_T + F$ has maximum degree $\le 3$. Any non-trivial kernel requires a 3-regular bipartite component in $F$ where all vertices have $t_v = 2$, forming a disconnected component in $B$. Because $B$ is proven connected on 61 vertices, this would force $3T = 122$, which is impossible ($122 \not\equiv 0 \pmod 3$). Hence $\operatorname{rank}(L) = T$ full column rank.
   - *No Unproved $A$-Invariance:* The draft explicitly designates $\mathcal{K} = \{z : \operatorname{supp}(z) \subseteq V_2, L^T z = 0\}$ as a strict subspace of $\ker(B+2I)$ and explicitly refuses to claim $A$-invariance of $\mathcal{K}$ (§6, lines 279–282: "承重缺口...不能因此宣称它本身A不变...不把空间维数下界当作已有矛盾").
6. **Projector Inequality with Repeated Spectra (§7):**
   - *Verified.* The identity $Y = X - \frac{17}{61}J = \sum_\beta s_\beta(2P_\beta - E_\beta)$ with $\operatorname{diag}(Y) = \frac{44}{61}\mathbf{1}$ and the Ky Fan trace bounds against diagonal test matrices $D$ are mathematically sound. The draft correctly notes that unsplit factor spaces cannot be dropped pointwise because their pointwise diagonal contributions do not vanish.

---

### 2. Precise Ranges Closed vs. Still Open

#### Truly Closed by These Results:
1. **The Entire All-Unsplit Factor Class ($S = \emptyset$):**
   - Any 61-vertex graph whose $B$ has only unsplit irreducible factors ($D_i \notin K_i^2$ for all $i$) is **completely and universally ruled out**. Either an odd multiplicity contradicts Theorem 2, or all even multiplicities force $\operatorname{tr}(X|_W) = 0 \neq 44$ (equivalently non-principal $A$-trace $-30 \neq -8$).
2. **Universal High-Triangle Extremum $T = 40$:**
   - No 61-vertex graph can have $T = 40$ triangles, irrespective of whether double defects exist or are absent ($d \ge 0$).
   - For defect-free graphs ($d = 0$), $T$ is even, hence $T \le 38$ is universally established.
3. **Any Factor Multiplicity Assignment Violating the Joint Integer Trace System:**
   - Any candidate spectrum failing $\sum_{i \in S} k_i t_{i,0} = 44$, $\sum_{i \in S} k_i t_{i,1} = 12T - 68$, or the two-sided bounds on $M_2 = \sum_{i \in S} k_i t_{i,2}$ under the **same** integer vector $k$ is definitively excluded.

#### Still Open:
1. **General Split Factors ($S \neq \emptyset$) with $T \le 39$:**
   - Polynomials $q_B$ possessing at least one split factor with $T \in [0, 39]$ (or $T \in [0, 38]$ for $d=0$) satisfying the joint trace conditions.
2. **General Non-Adjacent Double-Defect Families ($h_5$, open $h_6$ sub-branches):**
   - While adjacent double defect is closed and $h_6$ single-$W$ / $h_7$ are paper-closed, the remaining non-adjacent branches remain open.
3. **Defect-Free Graph Class ($d = 0$):**
   - Graphs with $B_{xy} \in \{0, 1\}$ and $T \le 38$ remain open.
4. **Whole $n=61$ Existence / Non-Existence:**
   - Fully open; no whole-graph non-existence claim is made.

---

### 3. Assessment of Main Unresolved Question & Concrete Next Derivation

#### Analysis of the Triangle-Incidence / Residual-Defect Representation:
- **Status of $\mathcal{K}$:** The subspace $\mathcal{K} = \{z : \operatorname{supp}(z) \subseteq V_2, L^T z = 0\}$ is **not** $A$-invariant. The operator $A$ leaks vectors from $\mathcal{K}$ into the low-triangle vertex set $V_{\le 1} = \{v : t_v \le 1\}$ because the neighbors of $V_2$ include vertices in $V_{\le 1}$.
- **The Genuine Invariant Space:** The ambient eigenspace $E_{-2}(B) = \ker(B + 2I)$ **is** strictly $A$-invariant (since $AB = BA$). On $E_{-2}(B)$, $A^2 + A - 7I = -2I \implies A^2 + A - 5I = 0$. The polynomial $x^2 + x - 5$ has discriminant $21 \notin \mathbb{Q}^2$, which is unsplit over $\mathbb{Q}$. Therefore:
  - The multiplicity $m_{-2} = \dim E_{-2}(B)$ must be an **even integer**.
  - $A|_{E_{-2}(B)}$ has eigenvalues $\frac{-1 \pm \sqrt{21}}{2}$ with equal multiplicity $m_{-2}/2$, so $\operatorname{tr}(A|_{E_{-2}(B)}) = -m_{-2}/2$.
- **The Controlled Compression Bridge:**
  Any vector $y \in E_{-2}(B)$ satisfies $(B + 2I) y = 0$, which by formula (16) expands to:
  $$\|L^T y\|^2 + \sum_{v \in V_{\le 1}} (2 - t_v) y_v^2 + y_{V_{\le 1}}^T R_{V_{\le 1}, V_{\le 1}} y_{V_{\le 1}} = 0.$$
  Because $R e_v = 0$ for all $v \in V_2$, the matrix $R$ is supported entirely on $V_{\le 1} \times V_{\le 1}$. Consequently, if $y \in E_{-2}(B)$ vanishes on $V_{\le 1}$, then $(2-t_v)y_v = 0$ and $Ry = 0$, forcing $L L^Ty = 0 \implies L^Ty = 0$.
  Thus, $\ker(y \mapsto y|_{V_{\le 1}}) \cap E_{-2}(B) = \mathcal{K}$ exactly!
  This yields an exact injection:
  $$E_{-2}(B) / \mathcal{K} \hookrightarrow \mathbb{R}^{V_{\le 1}}.$$
  Therefore, the dimension of the true $A$-invariant space is bounded by:
  $$\dim \mathcal{K} \le m_{-2} \le \dim \mathcal{K} + |V_{\le 1}| = \dim \mathcal{K} + (61 - n_2).$$
  Since $|V_{\le 1}| = 122 - 3T - n_0$, when $T$ is high (e.g. $T = 39$), $|V_{\le 1}| \le 5$, meaning the leakage of the invariant space away from $\mathcal{K}$ has dimension at most 5.

#### Justified Next Mathematical Derivation:
- **Continued investigation of this whole-graph quantity is justified.**
- **The exact missing bridge to derive:**
  Evaluate whether the parity constraint ($m_{-2}$ must be even) combined with the sandwich $\dim \mathcal{K} \le m_{-2} \le \dim \mathcal{K} + (61 - n_2)$ and the quadratic form identity on $E_{-2}(B)$:
  $$\|L^T y\|^2 + \sum_{v \in V_{\le 1}} (2 - t_v) y_v^2 = - y_{V_{\le 1}}^T R_{V_{\le 1}, V_{\le 1}} y_{V_{\le 1}}$$
  forces an arithmetic or rank obstruction when combined with the trace system $M_1 = 12T - 68$ and $M_2$ row-support bounds for high $T \in [35, 39]$.

---

### 4. Reviewer Memory Update

```markdown
### Reviewer Memory (auto-review-loop round 1)
- Mechanism: DD82 mathematical adaptation, round 1 of at most 2.
- Evaluated artifact: proofs/dd82/n61/GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md.
- Verdict: SCOPED ACCEPT for stated necessary theorems.
- Verified findings:
  * Complete factor lifting (Theorem 1) and integer multiplicity rules (Theorem 2) are verified.
  * All-unsplit spectrum class (S = empty) is universally ruled out by trace 44.
  * Second moment tr(A^2|_W) = 424 is verified redundant once trace 44 is imposed.
  * Universal T = 40 triangle count is ruled out via the residual matrix R and parity d = T (mod 2).
  * Incidence matrix L has full column rank T.
  * Subspace K is NOT A-invariant (admitted in text); the genuine A-invariant space is E_{-2}(B) with even multiplicity m_{-2}.
  * Projector inequality (19) correctly retains unsplit diagonal contributions.
- Proved bounds: 0 <= T <= 39, 2d + 3T <= 122, d = T (mod 2), M_1 = 12T - 68 with unified integer vector k.
- Open scopes: S != empty with T <= 39, defect-free graphs (d = 0, T <= 38), remaining h5/h6 non-adjacent branches, whole n61 existence.
- Authorized next step: investigate the quotient injection E_{-2}(B) / K -> R^{V_{\le 1}} and its parity/trace compatibility under the unified vector k, without random sampling, broad tables, or Lean work.
```




# 第2轮处置：精确低点核归约

2026-10-19 11:49:32 UTC。同线程3dc745b1-1a9a-4d06-810e-32310f2b9dab，请求/返回gemini-3.8-flash-high/high，SUCCESS。实际接受§1修正及§6.1–6.3；本机制最终2/2轮结束。

接受本轮承重结论：E低坐标满射ker S，核为K；完整−2重数=dimK+nullity S；每点有三角形而F无二部分量的完整范围被奇偶矛盾排除；压缩Q不自动保持整数格。此前K不变性及d0术语的纠正已获原审阅者明确承认。

根不采纳两处夸张解释：旧问题从来是有限61维，不能叫infinite-dimensional；n0>0或b(F)>0的补集仅尚未被统一排除，不是其中每个S自动通过奇偶。这不影响原稿中的精确必要定理。没有第3轮，无新求解、样本或Lean。

新全图范围为n0=0且b(F)=0；不是n0=0整域，也不是一般n61。继续主线是S的精确算术与剩余可拆谱和同一0/1矩阵实现，低T时S仍可能61阶，不许将此称为已经可完成的全域枚举。


## 第2轮原始回执

### 1. Scope and History Corrections Acknowledged

We explicitly adopt the following corrections to prior scope statements:
1. **Status of $\mathcal{K}$:** The executor never asserted that $\mathcal{K}$ is provably not $A$-invariant or provably a strict subspace of $E$. The correct mathematical status is that **$A$-invariance of $\mathcal{K}$ is not established** (and $\mathcal{K}$ can be trivial or coincide with $E$ in specific degenerate structures). It is not a negative theorem.
2. **Defect Terminology ($d = 0$):** $d = 0$ designates graphs with **no double defects** (i.e., all entries of $B$ are in $\{0, 1\}$; weight-2 pairs absent). It does not mean the graph is defect-free (the total defect sum remains $122$, distributed entirely on weight-1 pairs).
3. **Receipt Boundary:** Sections 6.1, 6.2, and 6.3 are new local derivations and are inspected directly below.

---

### 2. Mathematical Review Verdict: SCOPED ACCEPT

The new derivations in §1 (corrected $g \neq g^*$), §6.1, §6.2, and §6.3 of [`GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md`](file:///inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n61/GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md) are **SCOPED ACCEPT**.

#### Specific Verification:
1. **Separation of $g$ and $g^*$ (§1, line 58):**
   - *Verified.* If $g = g^*$, there exists a $\mathbb{Q}$-embedding $\sigma: K \to \mathbb{C}$ sending $\alpha \mapsto -1-\alpha$. Since $\beta = \phi(\alpha)$, $\sigma(\beta) = \phi(-1-\alpha) = \phi(\alpha) = \beta$. Because $K = \mathbb{Q}(\beta)$, $\sigma$ fixes $K$ pointwise, forcing $\alpha = -1-\alpha \implies 2\alpha + 1 = 0 \implies D = 0$. Since $D \ge 13 > 0$, this is an airtight contradiction.
2. **Exact Reduction of Multiplicity $m_{-2}(B)$ (Theorem 4, §6.2):**
   - *Verified.* Block decomposition:
     $$B + 2I = \begin{pmatrix} N N^T & N M^T \\ M N^T & M M^T + D_U + R_U \end{pmatrix}.$$
     For any $(x, y) \in E = \ker(B+2I)$, $a = N^T x + M^T y \in \ker N$. Projecting by $\Pi$ onto $\ker N$ gives $a = \Pi a = \Pi M^T y$ (since $\Pi N^T = 0$). Equation 2 then becomes $(D_U + R_U + M \Pi M^T) y = S y = 0$.
     Conversely, for any $y \in \ker S$, the equation $N^T x = -(I - \Pi) M^T y$ is solvable because $-(I - \Pi) M^T y \in (\ker N)^\perp = \operatorname{im} N^T$. The fiber of solutions is precisely $\ker N^T = \mathcal{K}$.
   - Thus, the low-coordinate restriction $E \to \ker S$ is surjective with kernel $\mathcal{K}$, proving the exact two-way identity:
     $$\boxed{m_{-2}(B) = \dim \mathcal{K} + \operatorname{nullity} S = n_2 - T + b(F) + \operatorname{nullity} S.}$$
     This holds for arbitrary $n_0$, handles bipartite components (including isolated triangles), requires no positive-semidefiniteness of $R_U$, and is an exact identity rather than a dimension bound.
3. **Parity Constraint and Corollary 5 (§6.2):**
   - *Verified.* Since $n_2 - T = 2T - 61 + n_0 \equiv 1 + n_0 \pmod 2$ and nonsquare lifting forces $m_{-2}(B) \equiv 0 \pmod 2$, we have:
     $$\operatorname{nullity} S \equiv 1 - n_0 - b(F) \pmod 2.$$
   - When $n_0 = 0$ and $b(F) = 0$: $S = I + R_U$. The residual matrix $R_U$ on $U$ has zero diagonal, non-negative integer entries $\le 2$, and row sum 2. Each connected component of $R_U$ is either a double $K_2$ (eigenvalues $\pm 2$, nullity of $I+R_U$ is 0) or a simple cycle $C_k$ (eigenvalue $-1$ occurs iff $3 \mid k$, with multiplicity exactly 2). Hence $\operatorname{nullity}(I + R_U)$ is **always even**.
   - But the parity identity requires $\operatorname{nullity} S \equiv 1 - 0 - 0 = 1 \pmod 2$ (odd).
   - This exact contradiction proves **Corollary 5**: *Every 61-vertex graph with $n_0 = 0$ must have at least one bipartite component in its triangle intersection graph $F$ ($b(F) \ge 1$)*.
4. **Structural Constraints on Non-Triangle Edges and Projector Stop (§6.3):**
   - *Verified.* Vertices in $V_2$ lie on no 4-cycles in $A$. All $H = A - C$ edges avoid $C$-graph distance $\le 3$.
   - The maximal $A$-invariant subspace inside $\mathcal{K}$ is $\mathcal{K}_0 = \ker V$, and $r = \operatorname{rank} V \le \operatorname{nullity} S \le \ell$.
   - *Discontinuation of Integer Flow Assumption:* The draft explicitly stops assuming that $P_K$ preserves an integer lattice, recognizing $P_K$ as purely rational (§6.3, lines 396–397). This avoids false integral compression claims.

---

### 3. Precise Ranges Closed vs. Open

#### Truly Closed by These Results:
1. **The Structural Subclass $n_0 = 0 \land b(F) = 0$:**
   - Any graph where every vertex lies in at least one triangle ($n_0 = 0$) and the triangle intersection graph $F$ has no bipartite components ($b(F) = 0$) is **completely and rigorously excluded**.
2. **All-Unsplit Factor Spectrum Class ($S = \emptyset$):**
   - Confirmed closed from Round 1.
3. **Universal $T = 40$ Triangle Count:**
   - Confirmed closed from Round 1.

#### Still Open:
1. **Graphs with $n_0 = 0$ having $b(F) \ge 1$:**
   - Parity of $\operatorname{nullity} S$ matches $1 - b(F) \pmod 2$.
2. **Graphs with $n_0 > 0$:**
   - Vertices without triangles allow $\operatorname{nullity} S \equiv 1 - n_0 - b(F) \pmod 2$ to be even.
3. **General Split Factors ($S \neq \emptyset$) with $T \le 39$:**
   - Unresolved integer vector $k$ combinations.
4. **No-Double-Defect Graphs ($d = 0$) with $T \le 38$:**
   - Open.
5. **Whole $n = 61$ Existence / Non-Existence:**
   - Open.

---

### 4. Progress Evaluation: Substantive Advance vs. Renaming

- **Substantive Progress:** This does **not** merely rename the obstruction. Theorem 4 replaces an intractable infinite-dimensional or unspecified leakage by an explicit, finite $\ell \times \ell$ boundary matrix $S = D_U + R_U + M \Pi M^T$. This directly produced Corollary 5, proving a concrete, previously unknown global structural necessity ($b(F) \ge 1$ whenever $n_0 = 0$) using purely universal spectral lifting and cycle parities.
- **Exact Remaining Gap:**
  When $n_0 > 0$ or $b(F) \ge 1$, $\operatorname{nullity} S$ is parity-compatible with an even $m_{-2}(B)$. The remaining gap is the **joint realizability** of $(S, \Pi, R_U)$ alongside:
  1. The unified mixed-trace identity $M_1 = \sum_{i \in S} k_i t_{i,1} = 12T - 68$;
  2. The row-support bounds on $M_2$;
  3. The existence of a valid 0/1 adjacency matrix $A$ realizing both $C$ and $H$.

---

### 5. Reviewer Memory Update & Loop Closure

```markdown
### Reviewer Memory (auto-review-loop round 2 / final)
- Mechanism: DD82 mathematical adaptation, round 2 of 2 (LOOP CLOSED).
- Evaluated artifact: proofs/dd82/n61/GLOBAL_SPECTRAL_FACTOR_ARITHMETIC.md (§1, §6.1, §6.2, §6.3).
- Verdict: SCOPED ACCEPT for stated necessary theorems.
- Corrected Scope Definitions:
  * Invariance of K under A is NOT established (not a negative theorem; K can be non-invariant or trivial).
  * d = 0 denotes "no double defects" (weight-2 entries absent; total defect sum 122 on weight-1 entries remains).
- Verified New Findings:
  * Theorem 1 Galois separation g != g* in §1 is verified complete via D >= 13 > 0.
  * Exact reduction (Theorem 4): m_{-2}(B) = n_2 - T + b(F) + nullity(S) where S = D_U + R_U + M Pi M^T.
  * Exact parity relation: nullity(S) = 1 - n_0 - b(F) (mod 2).
  * Corollary 5: If n_0 = 0, F must have at least one bipartite component (b(F) >= 1); the subcase n_0 = 0 and b(F) = 0 is completely ruled out.
  * Structural constraints: V_2 contains no 4-cycle vertices; non-triangle edges H avoid C-distance <= 3.
  * Projector boundary stop: P_K is purely rational; integer-lattice preservation claims on Q are stopped.
- Open scopes: n_0 > 0; n_0 = 0 with b(F) >= 1; S != empty with T <= 39; no-double-defect graphs (d = 0, T <= 38); whole n61 existence.
- Status: Auto-review loop completed at max round 2. No Lean certification or whole-61 closure claimed.
```



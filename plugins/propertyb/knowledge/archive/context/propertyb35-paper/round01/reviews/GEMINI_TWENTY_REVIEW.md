# Gemini4：20点δ6静态审阅原回应

实际CLI选择 gemini-4-argon-high / high；SUCCESS。仅本分支，无新程序或Lean执行。

### Independent Mathematical Assessment: $v=20, M=35$, Pair-Covering, $\delta=6$ Branch

**Scope & Verdict:** Read-only static mathematical review of [DELTA6_PROOF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/twenty_remaining/DELTA6_PROOF.md), [AUDIT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/delta6-audit/AUDIT.md), and [UNIT_STAR_RECOVERY.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/UNIT_STAR_RECOVERY.md). Within the conditional scope of the project's general conditional-permutation / greedy failure-event domination and bad-pair quota lemmas, and the independently replayed rational certificates (`2634` fixed-position witnesses and `83` joint duals), **no mathematical gap, hidden selection assumption, or circular inference was found in the $v=20, \delta=6$ branch.** This assessment applies strictly to the reduced $(v=20, M=35, \delta=6)$ branch and does not constitute a global pass for $m(5) \ge 36$.

---

### Verification of Key Coverage and Logical Steps

1. **Unique Degree-6 Center and Minimum Unit-Neighbour Degree ($\ge 8$):**
   Let $x \in V$ have minimum degree $d(x)=6$. By pair covering and 5-uniformity, any other vertex $y \neq x$ with $d(y)=6$ has codegree $c = \lambda(x,y) \in \{1,\dots,6\}$. The 2-lock exact trace inventory on $\{x,y\}$ is uniquely determined by $c$ as $(\mu_\varnothing, \mu_x, \mu_y, \mu_{xy}) = (23+c, 6-c, 6-c, c)$, and all 6 types are strictly $<1$. Thus $x$ is the unique degree-6 vertex, and all other 19 vertices have degree $\ge 7$. Similarly, if $x$ has a unit neighbour $y$ ($\lambda(x,y)=1$) of degree $7$, the unique 2-lock inventory $(24, 5, 6, 1)$ is strictly $<1$ ($1094/1105$). Consequently, in any uncolored $H$, every unit neighbour $u \in U = \{u \neq x : \lambda(x,u)=1\}$ satisfies $d(u) \ge 8$, while non-unit neighbours outside $U \cup \{x\}$ only require $d(v) \ge 7$.

2. **Unit-Neighbour Count ($h \ge 14$) and Selection Budget ($2a+b \ge 3h-36 \ge 6$):**
   Pair covering gives $\lambda(x,v) \ge 1$ for all $v \neq x$, so the codegree surplus at $x$ is $\sum_{v \neq x}(\lambda(x,v)-1) = 4d(x)-19 = 5$. At most 5 vertices can have $\lambda(x,v) \ge 2$, forcing $h = |U| \ge 19-5 = 14$.
   Let $a, b$ be the counts of degree-8 and degree-9 vertices in $U$. The remaining $h-a-b$ vertices in $U$ have degree $\ge 10$, while the $19-h$ vertices in $V \setminus (U \cup \{x\})$ have degree $\ge 7$. Comparing the lower and upper bounds on $\sum_{u \in U} d(u)$ via $\sum_{v \in V} d(v) = 175$:
   $$10h - 2a - b \le \sum_{u \in U} d(u) \le 175 - 6 - 7(19-h) = 36 + 7h \implies 2a + b \ge 3h - 36 \ge 6.$$
   This exhaustively splits into four non-negative integer regimes without unproved low-degree existence assumptions:
   - $a \ge 3$: three unit neighbours with degree vector `888` exist ($116$ inventories, all strict at $s=3$).
   - $a = 2, b = 2$: equality exception (checked below).
   - $a = 2, b \ge 3$ and $a = 1, b \ge 4$: five unit neighbours with sorted degree vector `88999` or `89999` exist ($45$ and $126$ inventories, all strict at $s=5$).
   - $a = 0, b \ge 6$: six unit neighbours with degree vector `999999` exist ($255$ inventories, all strict at $s=6$, max $701/715$).

3. **The $a=2, b=2$ Equality Exception:**
   When $a=2, b=2$, $6 = 2a+b \ge 3h-36 \ge 6$ forces $h=14$ and equality in every degree bound: the $19-14=5$ vertices outside $U \cup \{x\}$ all have degree $7$, and since 5 non-unit neighbours exhaust the surplus $\sum_{v \notin U\cup\{x\}}(\lambda(x,v)-1)=5$, each has $\lambda(x,v)=2$.
   - For any two such degree-7 vertices $p,q$, standard 3-set Möbius inversion on $\{x,p,q\}$ with $d=(6,7,7)$ and $\lambda(x,p)=\lambda(x,q)=2$ depends only on $\lambda(p,q) \in \{1,\dots,7\}$ and $\tau(x,p,q) \in \{0,1,2\}$. Non-negativity ($\mu_p = \mu_q = 5 - \lambda(p,q) + \tau \ge 0$ and $\tau \le \lambda(p,q)$) yields $5+6+6=17$ valid inventories; 14 are strict, leaving only $\lambda(p,q)=2$ ($\tau \in \{0,1,2\}$).
   - Thus all $\binom{5}{2}$ pairs among the five degree-7 vertices must have $\lambda(p,q)=2$. Taking any four of them (with $d=(7,7,7,7)$ and all six pairwise codegrees $2$), non-negativity of the pair traces $\mu_{ij} = 2 - t_{ijk} - t_{ijl} + q_4 \ge 0$ yields $20 + 5 + 1 = 26$ labeled $(t_1,t_2,t_3,t_4; q_4)$ inventories, all 26 of which are strict (max $12829/12870$).

4. **Shared Unit-Star Partition $\Pi$, Constraints, and Relational Join Completeness:**
   For any $s$ unit neighbours $Y = (y_1,\dots,y_s)$ of $x$ sorted by non-decreasing degree, each $y_i$ lies in a unique $x$-edge, inducing a unique partition $\Pi$ of $[s]$ into $|\Pi| \le 6$ blocks.
   - **Block & Simplicity Constraints:** Since each $x$-edge has size 5 and contains $x$, every block $B \in \Pi$ satisfies $|B| \le 4$. After subtracting $p_T = \mathbf{1}\{\exists B \in \Pi : T \subseteq B\}$ from the inclusive counts $I_T$, Möbius inversion uniquely recovers the non-$x$ trace counts $\mu_0(T)$ with $\sum_T \mu_0(T) = 35-6 = 29$. For $|A|=5$, $p_A=0$ (as $|B|\le 4$) and simplicity of 5-edges forces $I_A = \mu_0(A) \in \{0,1\}$; for $|A|=6$, 5-uniformity forces $I_A = 0$.
   - **Order-Preserving Sub-Tuple Coverage:** Every order-preserving $(s-1)$-subset of a sorted tuple in `{8899, 8999, 9999}` ($s=4$), `{88999, 89999, 99999}` ($s=5$), or `{999999}` ($s=6$) remains sorted and falls strictly within the residual degree vectors tabulated at level $s-1$ (`8888` and `8889` are empty at $s=4$ because every `888` projection at $s=3$ is strict). Because an actual uncolored hypergraph $H$ furnishes a single global partition $\Pi$ on $Y$ and a single consistent family of inclusive counts $(I_T)_{T \subseteq Y}$ whose restrictions to all sub-tuples must simultaneously lie in the uncolored residual sets, the relational join is exact and cannot prune away any valid actual $H$.

5. **Fixed and Joint Certificate Soundness:**
   For fixed layouts, $U < 1$ implies a valid 2-coloring of $H$ by the conditional-permutation lemma. For the $83$ joint certificates, the weak-duality bound uses a single shared actual bad-pair vector $z_j \in [0, c_j]$ across layouts $\ell$ and centers $i$; since $0 \le \beta_{i\ell} \le \gamma_\ell$, $\sum_\ell \gamma_\ell = 1$, and $\delta_R \ge 0$, the inequality $\sum_\ell \gamma_\ell U_\ell(z) \le \sum_{i,\ell}((\gamma_\ell-\beta_{i\ell})A_{i\ell} + \beta_{i\ell}C_{i\ell}) - \sum_R \delta_R q_R + \sum_j c_j \max(0, D_j - W_j) < 1$ rigorously guarantees some layout $\ell$ has $U_\ell(z) < 1$ without double-counting bad-pair deductions across layouts.


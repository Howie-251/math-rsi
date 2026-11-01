# 原始模型数学回应

threadId: a0384e32-0db0-41a2-ad60-fa0d06c0222b

First, we note the transcription correction on the $(d_x,d_y,\lambda)=(6,7,1)$ 2-lock inventory in the $v=20,\delta=6$ review: $\mu_\varnothing = 35-6-7+1 = 23$, so the inventory is $(23,5,6,1)$ (matching `PAIRS.json` and the verified bound $1094/1105$).

---

### Structural Analysis and Obstruction for the $v=25, M=35, a=5$ Branch

Let $H=(V,E)$ be any simple $5$-uniform hypergraph on $25$ vertices partitioned into five $5$-element groups $G_1,\dots,G_5$, with $|E|=35$, $d(v)=7$ for all $v\in V$, $\lambda(u,v)=2$ for distinct $u,v$ in the same group, and $\lambda(u,v)=1$ for $u,v$ in different groups.

#### 1. Exact Anchor-Star Decomposition and Intersection Lemma

Fix a group $G_k$ (say $G_1$) and an anchor vertex $x \in G_1$. Let $E_x = \{e_1,\dots,e_7\}$ be the $7$ edges incident to $x$. For each $i \in \{1,\dots,7\}$, define the internal trace $A_i = e_i \cap G_1$, the reduced internal trace $A_i' = A_i \setminus \{x\}$, and the external anchor block $L_i = e_i \setminus G_1$.

**Lemma 1 (Anchor-Star Exclusivity and Trace Identities).** *In any actual $a=5$ hypergraph $H$, for any $x \in G_1$:*
1. *(Partition and Multigraph Dual):* $\{L_1,\dots,L_7\}$ partitions $V \setminus G_1$ ($20$ vertices), while $\{A_1',\dots,A_7'\}$ covers each of the $4$ vertices in $G_1 \setminus \{x\}$ with multiplicity $2$, so $\sum_{i=1}^7 |A_i'| = 8$ and $|L_i| = 4 - |A_i'|$.
2. *(Exact Singleton-Trace Identity):* The number of anchor edges with $A_i' = \varnothing$ (i.e., $e_i \cap G_1 = \{x\}$ and $|L_i|=4$) is the singleton $G_1$-trace count $\mu_{G_1}(\{x\})$, which satisfies the exact identity
   $$\mu_{G_1}(\{x\}) = \sum_{T \ni x,\ T \subseteq G_1,\ |T| \ge 3} (|T| - 2)\,\mu_{G_1}(T) - 1.$$
   In particular, since $\mu_{G_1}(\{x\}) \ge 0$, every vertex $x \in V$ belongs to at least one edge $e \in E$ with $|e \cap G_k| \ge 3$ (where $x \in G_k$). Moreover, whenever $G_k \in E$ and every other edge meets $G_k$ in at most $2$ points, $\mu_{G_k}(\{x\}) = (5-2)\cdot 1 - 1 = 2$ for all $x \in G_k$.
3. *(Cross-Group and Intra-Group Anchor Exclusivity):* For every non-$x$ edge $f \in E \setminus E_x$ and every label $i \in \{1,\dots,7\}$:
   - **Internal–External Mutual Exclusion:** If $f \cap A_i' \neq \varnothing$, then $f \cap L_i = \varnothing$.
   - **Single-Group Concentration of Label Repeats:** If $|f \cap L_i| \ge 2$, there is a unique external group $G_m$ ($m \in \{2,3,4,5\}$) such that $f \cap L_i \subseteq L_i \cap G_m$.
   - **Exact Non-$x$ Edge Incidence:** Let $q(L_i) = \sum_{m=2}^5 \binom{|L_i \cap G_m|}{2}$. Across the $28$ non-$x$ edges $f \in E \setminus E_x$,
     $$\sum_{f \in E \setminus E_x} |f \cap L_i| = 6|L_i| = 24 - 6|A_i'|, \qquad \sum_{f \in E \setminus E_x} \binom{|f \cap L_i|}{2} = q(L_i).$$

*Proof.*
(1) Each $y \in V \setminus G_1$ has $\lambda(x,y)=1$, so $y$ lies in a unique $e_i \in E_x$; each $u \in G_1 \setminus \{x\}$ has $\lambda(x,u)=2$, so $u$ lies in exactly two $A_i'$.
(2) Subtracting $d(x) = \mu_{G_1}(\{x\}) + \sum_{T \ni x, |T|\ge 2} \mu_{G_1}(T) = 7$ from $\sum_{u \in G_1 \setminus \{x\}} \lambda(x,u) = \sum_{T \ni x, |T|\ge 2} (|T|-1)\mu_{G_1}(T) = 8$ yields the formula for $\mu_{G_1}(\{x\})$.
(3) Any two distinct edges $f \neq e_i$ with $|f \cap e_i| \ge 2$ must have $f \cap e_i \subseteq G_m$ for a single group $G_m$, since cross-group pairs have $\lambda=1$. Because $f \cap e_i = (f \cap A_i') \cup (f \cap L_i)$ with $A_i' \subseteq G_1$ and $L_i \subseteq V \setminus G_1$, $f \cap A_i' \neq \varnothing$ forces $f \cap e_i \subseteq G_1$, hence $f \cap L_i = \varnothing$; similarly $|f \cap L_i| \ge 2$ forces $f \cap L_i \subseteq G_m$ for a single $m \in \{2,3,4,5\}$. Finally, each $y \in L_i$ lies in $d(y)-1 = 6$ edges of $E \setminus E_x$, and each intra-group pair in $L_i \cap G_m$ has $\lambda=2$ and already lies in $e_i$, so it lies in a unique $f \in E \setminus E_x$. $\blacksquare$

---

#### 2. Adversarial Obstruction to the Universal Anchor-Label Coloring Family

We now test the proposed coloring family $\mathcal{C}_x$: fix $x \in G_1$ (colored $0$), assign label bits $(c_1,\dots,c_7) \in \{0,1\}^7$ to $L_1,\dots,L_7$, choose the $4$ bits of $G_1 \setminus \{x\}$ in $\{0,1\}^4$ independently, and optionally reverse all colors in at most one external group $G^* \in \{\varnothing, G_2, G_3, G_4, G_5\}$.

First observe a general construction principle for **actual** $a=5$ hypergraphs: let $\mathcal{B}_0$ be the $30$ lines of $AG(2,5)$ on $V = \mathbb{F}_5^2$ (where every vertex has degree $6$ and every pair has codegree $1$), and let $\mathcal{G} = \{G_1,\dots,G_5\}$ be **any** partition of $V$ into five $5$-sets such that $G_k \notin \mathcal{B}_0$ for all $k$. Then $H = (V, \mathcal{B}_0 \cup \mathcal{G})$ is a simple $5$-uniform hypergraph with $35$ edges, $d(v)=7$, intra-group codegree $1+1=2$, and inter-group codegree $1+0=1$.

**Proposition 2 (Actual-Hypergraph Obstruction to $\mathcal{C}_x$).** *There exist actual simple $5$-uniform $a=5$ hypergraphs $H$ for which:*
1. *(Two-Red-Labels Obstruction with $221$ / Oval Groups):* Even when $G_1$ is the parabola oval (so $\mu_{G_1}(\{x\})=2$, $|L_5|=|L_6|=4$, $|L_1|=\dots=|L_4|=3$) and $|e \cap G_k| \le 2$ for every $e \notin \mathcal{G}$, the prescription $c_5=c_6=1, c_1=c_2=c_3=c_4=0$ (which is forced by $e_5,e_6$ whenever $L_5 \cup L_6$ is unreversed) fails for all choices of $G_1 \setminus \{x\}$ and $G^*$.
2. *(Full Family Obstruction):* For a valid partition $\mathcal{G}$ of $AG(2,5)$, **every** coloring in $\mathcal{C}_x$ (all $2^7 \times 2^4 \times 5 = 10{,}240$ configurations) leaves at least one edge of $H$ monochromatic.

*Proof.* Let $e_1,\dots,e_6$ be the $6$ lines of $AG(2,5)$ through $x$, and $e_7 = G_1$ ($L_7 = \varnothing$).
- For (1), take $G_1$ to be the parabola oval through $x$, so $A_5'=A_6'=\varnothing$ ($|L_5|=|L_6|=4$) and $|L_1|=\dots=|L_4|=3$. Partition $L_5$ into $2$ points of $G_2$ and $2$ of $G_3$, and $L_6$ into $2$ points of $G_2$ and $2$ of $G_3$; place the remaining $1$ point of $G_2$, $1$ of $G_3$, $5$ of $G_4$, and $5$ of $G_5$ into $L_1 \cup L_2 \cup L_3 \cup L_4$ so that $|G_k \cap e_i| \le 2$ and no $G_k$ is a line of $AG(2,5)$. Under $c_5=c_6=1$ and $c_1=c_2=c_3=c_4=0$, both $G_4$ and $G_5$ lie entirely in $L_1 \cup L_2 \cup L_3 \cup L_4$ (all color $0$). Since at most one group $G^*$ is reversed, at least one of $G_4, G_5$ remains unreversed and monochromatic $0$.
- For (2), choose $G_1 = \{x, u_1, u_2, u_3, u_4\}$ with $u_1,u_2 \in e_5 \setminus \{x\}$ and $u_3,u_4 \in e_6 \setminus \{x\}$ ($|G_1 \cap e_5|=3 \implies G_1 \notin \mathcal{B}_0$). Then $A_1'=A_2'=A_3'=A_4'=\varnothing$, so $e_i = \{x\} \cup L_i$ with $|L_i|=4$ for $i=1,2,3,4$, and $|L_5|=|L_6|=2$. Partition $V \setminus G_1$ as:
  - $G_2$: $3$ points in $L_1$, $2$ in $L_2$ ($G_2 \subseteq L_1 \cup L_2$, $|G_2 \cap e_1|=3 \implies G_2 \notin \mathcal{B}_0$);
  - $G_3$: $1$ point in $L_1$, $2$ in $L_2$, $1$ in $L_5$, $1$ in $L_6$ ($|G_3 \cap e_2|=2 \implies G_3 \notin \mathcal{B}_0$);
  - $G_4$: $3$ points in $L_3$, $2$ in $L_4$ ($G_4 \subseteq L_3 \cup L_4$, $|G_4 \cap e_3|=3 \implies G_4 \notin \mathcal{B}_0$);
  - $G_5$: $1$ point in $L_3$, $2$ in $L_4$, $1$ in $L_5$, $1$ in $L_6$ ($|G_5 \cap e_4|=2 \implies G_5 \notin \mathcal{B}_0$).
  Here $L_1 \cup L_2 \subseteq G_2 \cup G_3$ and $L_3 \cup L_4 \subseteq G_4 \cup G_5$. For any choice of at most one reversed external group $G^*$, either $G^* \notin \{G_2,G_3\}$ or $G^* \notin \{G_4,G_5\}$:
  - If $G^* \notin \{G_2,G_3\}$, no vertex in $L_1 \cup L_2$ is reversed. Since $x=0$ and $e_1 = \{x\}\cup L_1$, $e_2 = \{x\}\cup L_2$ contain no vertices of $G_1 \setminus \{x\}$, avoiding monochromatic $0$ on $e_1,e_2$ forces $c_1 = c_2 = 1$. Then $G_2 \subseteq L_1 \cup L_2$ is monochromatic $1$.
  - If $G^* \notin \{G_4,G_5\}$, no vertex in $L_3 \cup L_4$ is reversed. Then $e_3 = \{x\}\cup L_3$ and $e_4 = \{x\}\cup L_4$ force $c_3 = c_4 = 1$, making $G_4 \subseteq L_3 \cup L_4$ monochromatic $1$. $\blacksquare$

---

#### 3. Exact Remaining Step

Proposition 2 proves that constant coloring on each external anchor block $L_i$ (even with independent $G_1$ coloring and single-group reversal) is **too rigid**: whenever $L_i \cup L_j$ concentrates inside two external groups while other external groups lie in the remaining $L_r$'s, constant-on-$L_i$ assignments create conflicting monochromatic constraints between anchor edges $\{x\}\cup L_i$ and external group-heavy edges.

To close the $a=5$ branch, the coloring must **split the $4$-element blocks $L_i$ internally** (using the 2-anchor intersection grid $L_i \cap L_j'$ across two anchors $x \in G_1, y \in G_2$, where $|L_i \cap L_j'| \le 1$ whenever $e_i \cap e_j'$ is not intra-group), or apply the project's conditional-permutation / bad-pair framework to a multi-group lock set using Lemma 1(3)'s exact non-$x$ incidence and cross-group exclusivity constraints.


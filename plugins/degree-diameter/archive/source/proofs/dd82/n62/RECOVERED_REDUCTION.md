# Recovered order-62 reduction

**Current preferred triple-repeat proof (2026-10-11):**
[TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md](TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md)
retains the original-graph reductions in Steps 1–3 below and replaces
Steps 4–5 by an analytic component/trace contradiction. Fresh full-chain
review and Gemini B28 accepted this replacement. No matrix enumeration
or final row-support parity table is needed in that proof. The older
finite route and its historical execution records below are preserved.
The new full implication is a paper proof; its entire original-graph
bridge has not yet been assembled in Lean.

## Claim and status

The original target is nonexistence of a finite simple undirected graph on 62 vertices with maximum degree at most 8 and diameter at most 2.

**Target status: NOT CURRENTLY JUSTIFIED.** The archived RAW_UNSAT records do not certify this target.

**Recovered reduction status: PROVABLE AS STATED, with a small exact enumeration explicitly identified below.** Every original candidate has no triple edge in its repeat matrix and can be relabeled into one of the seven archived templates. The original-graph-to-enumeration derivation, which was only outlined in the handoff, is supplied here. The small archived enumeration was rerun successfully in this task; the total single-process wall time, including a second inspection of its final case, was 3.97 seconds. No SAT solver was run.

This is a paper-level proof with an exact finite check, not a Lean theorem. The final exclusion still needs certified branch contradictions or replacement mathematics.

## Sources and scope

All archival paths below are relative to `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/` in this project. No old external project path was accessed.

* `theory/n62/handoff.md`, especially Sections 2–4.
* `theory/n62/n62_triple_edge_elimination.py` and its archived output.
* `theory/n62/n62_root_templates.py` and `.json`.
* `materials/n62/20260824_baseline_and_transition.md` and the three README files.
* `code/n62/n62_ab_resume_partition.py`, with limited inspection of `n62_ab_cnf.py`.
* `evidence/n62/interrupted_ab_pilot_progress.json` and `final_s_disjoint_progress.json`.

The initial handoff's label PROVED is a historical assertion. This document distinguishes the derivation recovered below from unchecked CNF equivalence and uncertified solver output.

## Assumptions, notation, and dependency map

Assume an original candidate $G$ exists. Its adjacency matrix is $A$, its common-neighbor count is $c_{xy}$, and $J$ is the all-ones matrix. Define

$$B=A^2+A-7I-J.$$

The dependencies are:

1. Original graph assumptions imply regularity, the repeat-matrix identities, and at most one triangle per vertex.
2. A hypothetical triple edge implies the five-cell structure and finite matrix objects in Steps 2–5.
3. The explicit bounded enumeration plus the final parity contradiction eliminates those objects.
4. The four-cycle count and elementary root relabeling then give the seven templates.
5. Excluding these seven templates would exclude the original graph. That final step is presently supported only by RAW_UNSAT evidence and is not asserted here.

## Proof

### Step 1. Identities directly from the original graph

If a vertex has degree at most 7, at most $1+7+7\cdot7=57$ vertices are at distance at most 2 from it. Thus $G$ is 8-regular. Consequently $B$ is symmetric, nonnegative integral, has zero diagonal, and satisfies

$$B\mathbf1=3\mathbf1,\qquad AB=BA,\qquad c_{xy}+A_{xy}=1+B_{xy}\quad(x\ne y).$$

If $t(x)$ counts triangles containing $x$, then

$$2t(x)=\sum_{y\in N_G(x)}B_{xy}\le3,$$

so $t(x)\le1$. In particular every adjacent pair has $B_{xy}=c_{xy}\le1$, and the three edges of each triangle have repeat weight 1.

We repeatedly use a basic consequence of nonnegative symmetric row-sum-3 matrices: if $Bf=3f$, then $f$ is constant on every connected component of the support of $B$. One proof is

$$f^T(3I-B)f=\frac12\sum_{x,y}B_{xy}(f_x-f_y)^2=0.$$

Thus vertices at distinct values of $f$ cannot have a positive $B$ entry between them. This observation applies to actual integer vectors below; no numerical spectrum is used.

### Step 2. A triple edge forces five cells

Suppose $B_{uv}=3$. Its two rows have no other positive entries. The pair $u,v$ is nonadjacent, since an adjacent repeat weight is at most 1. Moreover $t(u)=t(v)=0$. Set

$$S=N(u)\cap N(v),\qquad E^+=N(u)\setminus S,\qquad E^-=N(v)\setminus S.$$

Then $|S|=4$ and $|E^+|=|E^-|=4$. Both neighborhoods $N(u)$ and $N(v)$ are independent.

Every two distinct points of $S$ already have common neighbors $u,v$, and are nonadjacent. Hence all three other points of $S$ have positive repeat weight from a given point of $S$. The row sum 3 forces $B[S]=J_4-I_4$, with no positive repeat entries leaving $S$, and forces exactly two common neighbors for every pair in $S$. In particular no vertex outside $\{u,v\}$ has two neighbors in $S$.

For $x\in E^+$, the pair $x,v$ has exactly one common neighbor, because $B_{xv}=0$. There are no edges from $x$ to $S$, so $x$ has exactly one neighbor in $E^-$. The analogous statement holds from $E^-$, making the original-graph edges between these sets a perfect matching. Label them

$$E^+=\{e^+_0,\ldots,e^+_3\},\quad E^-=\{e^-_0,\ldots,e^-_3\},\quad e^+_p\sim e^-_p.$$

The vector $f=A(e_u+e_v)$ obeys $Bf=3f$ and takes values 2 on $S$, 1 on $E=E^+\cup E^-$, and 0 elsewhere. Thus $B$ has no entries between these three level sets. The vector $g=A(e_u-e_v)$ obeys $Bg=-3g$. On $E$ it takes values $+1,-1$. Its row equation forces every repeat edge from $E^+$ to go to $E^-$, and conversely.

Each vertex of $S$ has six neighbors outside $\{u,v\}$. The preceding common-neighbor argument makes all these 24 vertices distinct. Let their union be $U$, partitioned into four sets $U_s$ of size 6 by their unique neighbor $s\in S$. Let $V$ be the remaining 24 vertices.

The vector $h=A\mathbf1_S$ has value 4 on $\{u,v\}$, 1 on $U$, and 0 elsewhere, and satisfies $Bh=3h$ because $B\mathbf1_S=3\mathbf1_S$. Combining this with the already separated cells shows that $B$ has no entries between any two of

$$\{u,v\},\quad S,\quad E,\quad U,\quad V.$$

A point of $U$ has one neighbor in $S$. Counting its common neighbors with $u$ and $v$ therefore shows it has no neighbor in either $E^+$ or $E^-$. A point of $V$ has exactly one neighbor in each of $E^+$ and $E^-$. Every point of $E$ has its one neighbor in $\{u,v\}$, its matching partner in $E$, and six neighbors in $V$.

Finally, the point-pair identity between $s\in S$ and a point $z\in U_s$ gives no neighbor of $z$ in its own $U_s$; for each $s'\ne s$ it gives exactly one neighbor in $U_{s'}$. Between $s\in S$ and $z\in V$, it gives exactly one neighbor of $z$ in $U_s$. Hence points of $U$ have three neighbors in $U$ and four in $V$, while points of $V$ have four neighbors in $U$ and two in $V$.

This proves the asserted equitable original-graph quotient, with cell sizes $(2,4,8,24,24)$:

$$R=\begin{pmatrix}
0&4&4&0&0\\
2&0&0&6&0\\
1&0&1&0&6\\
0&1&0&3&4\\
0&0&2&4&2
\end{pmatrix}.$$

### Step 3. The three four-by-four types, and direct elimination of two

Write the repeat block on $E^+\cup E^-$ as

$$B_E=\begin{pmatrix}0&N\\N^T&0\end{pmatrix},\qquad A_E=\begin{pmatrix}0&I\\I&0\end{pmatrix}.$$

Since $B$ has no entries leaving $E$, the $E,E$ block of $AB=BA$ implies $N=N^T$. Its row sums are 3. The only original-graph neighbor of $e^+_p$ in its repeat support is $e^-_p$. Therefore $N_{pp}=2t(e^+_p)$ is even, while adjacency implies $N_{pp}\le1$; it is zero.

A symmetric zero-diagonal four-by-four matrix with row sum 3 has equal opposite entries. To see this, write its six entries as $a=N_{01},b=N_{02},c=N_{03},d=N_{12},e=N_{13},f=N_{23}$. The four row sums give $a=f,b=e,c=d$ and $a+b+c=3$. Permuting the four labels permits permuting the three opposite-edge pairs. Thus the only types are $(a,b,c)=(3,0,0),(2,1,0),(1,1,1)$.

Label a point of $V$ by $(p,q)$ if its neighbors in $E$ are $e^+_p,e^-_q$. Counting common neighbors of this pair gives

$$|V_{pq}|=1+N_{pq}-\delta_{pq}.$$

Thus $V_{pp}$ is empty, and $|V_{pq}|=1+N_{pq}$ for $p\ne q$.

Let $L=A[V]$ and $Q=B[V]$. The first is simple 2-regular; the second is a nonnegative integral symmetric row-sum-3 matrix. For $z\in V_{pq}$, counting common neighbors with each $e^+_r$ and $e^-_s$ gives

$$\#(N_L(z)\cap \{\text{first label }r\})=1-\delta_{rp}-\delta_{rq},$$
$$\#(N_L(z)\cap \{\text{second label }s\})=1-\delta_{sp}-\delta_{sq}.$$

Therefore its two $L$-neighbors have both labels in the complementary pair to $\{p,q\}$, one of each first label and one of each second label. In particular $L$ is a union of bipartite blocks between complementary unordered label pairs and has no triangle.

No triangle can cross the five cells, since an original edge in a triangle has positive repeat weight. Hence a point of $V$ lies in no original triangle at all, and

$$L_{zz'}Q_{zz'}=0\quad\text{for all }z,z'.$$

The $E,V$ block of $AB=BA$ gives the weighted label marginals of $Q$:

$$\sum_{z':\,\text{first}(z')=r}Q_{zz'}=N_{rq},\qquad
\sum_{z':\,\text{second}(z')=s}Q_{zz'}=N_{sp}.$$

These already exclude the first two types:

* If $N_{01}=N_{23}=3$ and the other four off-diagonal entries vanish, take the unique point of type $(0,2)$. Its $Q$ row is concentrated with weight 3 at the unique point of type $(3,1)$, by the two marginals. That point is one of its forced $L$ neighbors, a contradiction.
* If $N_{01}=N_{23}=2$, $N_{02}=N_{13}=1$, and $N_{03}=N_{12}=0$, take the unique point of type $(0,3)$. Its only possible $Q$ targets are the unique points of types $(2,1)$ and $(1,2)$, with weights 2 and 1: equal-label targets do not exist. Both are its forced $L$ neighbors, again a contradiction.

It remains that $N=J_4-I_4$ and every ordered type $(p,q)$ has exactly two points.

### Step 4. Exact derivation of the finite checker's inputs

Assign the two points of each ordered type copy labels 0 and 1. In each complementary-pair block, the four adjacencies between ordered types are perfect matchings of two-point sets. Relabeling the copies at its four types makes three matchings identities; the fourth is identity or swap. The three blocks have disjoint type sets, so all possibilities are represented by the eight bit strings in $\{0,1\}^3$ used by `make_l`.

The $Q$ label marginals above are now 1 for each first label other than $q$, and for each second label other than $p$. They force $Q$ to be simple. It is cubic, disjoint from $L$, and the $V,V$ block of $AB=BA$ gives $LQ=QL$. These are exactly `q_row_domains` and `matrices_commute` in the checker.

Let $C=A[E,V]$ and $D=A[U,V]$. Both row and column sums of $D$ are 4. For vertices of $V$ of types $(p,q)$ and $(r,s)$,

$$ (C^TC)_{(p,q),(r,s)}=\delta_{pr}+\delta_{qs}.$$

The $V,V$ block of $A^2+A=7I+J+B$ gives the exact Gram constraint

$$D^TD=7I+J+Q-C^TC-L^2-L.$$

Consequently the right side has diagonal 4, nonnegative entries at most 4, and row sum 16. These are necessary conditions; relaxing to them does not discard a genuine graph.

The $E,U$ point-pair equation gives $CD^T=J$. Hence each row support of $D$ has one point of every first label and one point of every second label. It is a derangement of the four labels, with four chosen copy bits; every pair in the support must have positive Gram entry. This is exactly the list built by `candidate_d_rows`.

For any fixed $s\in S$, the six rows of $D$ belonging to $U_s$ must partition $V$: each $z\in V$ has exactly one neighbor in $U_s$. Thus the final no-resolution question is a necessary condition on the original graph, not an additional structural assumption.

The exhaustive table is:

| Number of swap bits | Bit strings | Symmetric commuting $Q$ per string | Gram survivors per string |
|---:|---:|---:|---:|
| 0 | 1 | 13 | 0 |
| 1 | 3 | 5 | 0 |
| 2 | 3 | 1 | 0 |
| 3 | 1 | 1 | 1 |

This is the sole finite enumeration used in the triple-edge proof. Its completeness is transparent in the source: every allowable cubic row neighborhood is listed, branching tries every row choice, propagation removes only failures of symmetry, and each completed symmetric matrix is tested for commutation. The eight lifted $L$ graphs cover all copy gauges as proved above. The Gram filter is only a necessary condition. The run reproduced every count in the archived output.

### Step 5. The final parity contradiction, including its missing multiplicity premise

For the unique surviving case, the 24 allowable row supports have the following six label permutations, with four copy patterns each. Positions in each bit string are first labels $0,1,2,3$.

| Name | Permutation | Allowed copy strings |
|---|---|---|
| A | $(1,2,3,0)$ | 0011, 0110, 1001, 1100 |
| B | $(1,3,0,2)$ | 0011, 0101, 1010, 1100 |
| C | $(2,0,3,1)$ | 0011, 0101, 1010, 1100 |
| D | $(2,3,1,0)$ | 0100, 0111, 1000, 1011 |
| E | $(3,0,1,2)$ | 0010, 0111, 1000, 1101 |
| F | $(3,2,0,1)$ | 0100, 0111, 1000, 1011 |

Any resolution must use each named permutation exactly once. Indeed let their multiplicities be $a,b,c,d,e,f$. Covering both copies of types $01,13,30$ gives $a+b=b+d=a+d=2$, so $a=b=d=1$. Types $23,03,12$ then give $c=e=f=1$.

This premise is needed before writing one copy bit for each named permutation; the archived parity subroutine did not separately state it. It follows from the displayed support table and is now explicit.

For a putative resolution write $x_{A,i}$ for the copy bit at first label $i$ in its A row, and analogously for D, E, F. The support table forces

$$x_{A,1}+x_{A,3}=1,\quad x_{D,2}+x_{D,3}=0,\quad
x_{E,0}+x_{E,2}=1,\quad x_{F,0}+x_{F,1}=1$$

over $\mathbb F_2$. Covering the two copies of types $03,12,21,30$ forces

$$x_{E,0}+x_{F,0}=1,\quad x_{A,1}+x_{F,1}=1,\quad
x_{D,2}+x_{E,2}=1,\quad x_{A,3}+x_{D,3}=1.$$

Adding these eight equations gives $0=1$. Thus no resolution exists, contradicting the six rows in any $U_s$. The triple-edge hypothesis is impossible:

$$\boxed{B_{xy}\le2\text{ for all }x\ne y.}$$

### Step 6. Parity and the complete seven-template reduction

Let $d$ be the number of double edges of $B$, $T$ the number of original triangles, and $Q_4$ the number of original four-cycles. A double repeat edge is nonadjacent in $G$ and has three common neighbors. There are $93-2d$ repeat edges of weight 1, exactly $3T$ of which are original edges. The remaining ones have two common neighbors. Counting opposite pairs of four-cycles gives

$$2Q_4=(93-2d-3T)+3d=93+d-3T,$$

and hence $d-T\equiv1\pmod2$. In particular if $B$ is simple, $T$ is odd and some triangle exists.

Fix a root $0$, its eight neighbors $X$, and the remaining 53 vertices $Y$. Write $P(y)=N(y)\cap X$. Every such parent set is nonempty. If $t(0)$ is 0 or 1, edge counting from $X$ gives

$$\sum_{y\in Y}(|P(y)|-1)=3-2t(0).$$

If $B$ has a double edge, choose its endpoint as root and its mate as $w$. The root is triangle-free: its double edge is nonadjacent, and the only remaining repeat weight is 1, whereas a triangle needs two incident repeat weights on adjacent pairs. Therefore $X$ is independent and the parent excesses are exactly a triple parent set $S=P(w)$ and a double parent set $P(a)$. Relabel $S=\{1,2,3\}$ and put $R=X\setminus S$.

Both $0$ and $w$ are triangle-free, so $w$ cannot have a neighbor in $Y$ whose parent set meets $S$. It has five neighbors $Y_w=N(w)\setminus S$. If $x\in R$, then $x,w$ are nonadjacent and have $1+B_{wx}$ common neighbors, all in $Y_w$. Conversely a point $y\in Y_w$ has $1+B_{0y}$ parents, all in $R$.

If $a\notin Y_w$, each of the five points of $Y_w$ has just one parent. Each of five labels in $R$ must occur, so there is exactly one neighbor of $w$ in every singleton class of $R$.

If $a\in Y_w$, its two parents lie in $R$ and the other four points are singleton-parent points. The six incidences over five labels force the unique simple repeat of $w$ to be a label $b\in R$. A label $x$ occurs $1+\mathbf1_{x=b}$ times, of which $\mathbf1_{x\in P(a)}$ is supplied by $a$. Thus the singleton counts are exactly

$$1+\mathbf1_{x=b}-\mathbf1_{x\in P(a)}.$$

Under permutations preserving $S$ and $P(a)$, $b$ has the two orbits inside or outside $P(a)$. This proves the detailed local constraints, not just the number of branches.

If $B$ is simple, choose root on a triangle and label the edge in $X$ as $\{1,2\}$. The parent excess is 1, so there is one double-parent point $w$. Its parents cannot be exactly $\{1,2\}$, which would put a second triangle on that edge. They meet that edge in either one point or none.

The seven representatives and singleton sizes are therefore:

| Template | Root triangle edge | Exceptional parent sets | Additional choice | Singleton sizes |
|---|---|---|---|---|
| D0_MATCH | none | $123,45$ | $w\not\sim a$ | $(6,6,6,6,6,7,7,7)$ |
| D0_EDGE_BIN | none | $123,45$ | $w\sim a$, $b=4$ | same |
| D0_EDGE_BOUT | none | $123,45$ | $w\sim a$, $b=6$ | same |
| D1_MATCH | none | $123,14$ | $w\not\sim a$ | $(5,6,6,6,7,7,7,7)$ |
| D2_MATCH | none | $123,12$ | $w\not\sim a$ | $(5,5,6,7,7,7,7,7)$ |
| S_TOUCH | $12$ | $13$ | $B$ simple | $(5,6,6,7,7,7,7,7)$ |
| S_DISJOINT | $12$ | $34$ | $B$ simple | $(6,6,6,6,7,7,7,7)$ |

Each singleton count is $7-\deg_{G[X]}(x)$ minus the number of exceptional parent incidences at $x$. The three parent-set intersections in the double branch and the two intersections in the simple branch exhaust all possibilities under the appropriate symmetric groups. Ordering vertices inside singleton classes is only relabeling. No automorphism of the original graph is assumed.

This proves the full original-graph coverage theorem: every candidate has a relabeling satisfying one of these seven templates. It proves no template impossible by itself.

## Recovery of the S_DISJOINT 80-case coverage

This additional recovery explains the small canonical split independently of the solver's results.

Use the archived labels: root triangle $012$, exceptional point $w=9$ with parents $3,4$. For each of the six other root labels $1,2,5,6,7,8$, a common neighbor with $w$ is required. The six remaining neighbors of $w$ are all singleton-parent points, each covering just one such label. Hence there is exactly one neighbor in each of those six classes and none in classes 3 or 4. Relabeling within each class fixes its $Y$-neighbor set to

$$A_w=\{10,16,34,41,48,55\}.$$

All repeat entries from $w$ to $X$ are now zero, and $B_{0w}=1$. Thus its two other repeat neighbors $b,c$ lie in $Y$. Since $2t(w)=\mathbf1_{b\in A_w}+\mathbf1_{c\in A_w}$, they are either both in $A_w$ or both outside it.

The stabilizer divides parent labels into three groups: H=$\{1,2\}$, P=$\{3,4\}$, F=$\{5,6,7,8\}$. Within a group, labels can be exchanged; within a singleton class, the distinguished member of $A_w$ is fixed and the other members can be exchanged. This gives exactly twelve unordered-pair orbits:

* In $A_w$: H–H, H–F, F–F (three orbits).
* Outside $A_w$: two H–H orbits, two P–P, two F–F, according as the parent label is equal or different; and H–P, H–F, P–F (nine orbits).

Four of the twelve have endpoints in different groups and do not admit an endpoint swap within this stabilizer. They require all four triangle-membership bit pairs. The other eight admit a swap and require only $00,01,11$. Finally splitting the original edge $bc$ into its two possible values gives

$$4\cdot4\cdot2+8\cdot3\cdot2=80$$

canonical cases. The twelve representatives in `n62_ab_resume_partition.py` agree with these orbit signatures. This proves coverage up to relabeling of actual graphs. It does not certify the generated CNF variable mapping, an exact historical DIMACS instance, or any solver answer. Calling these representatives a literal partition of all labeled graphs would be inaccurate: the coverage is by symmetry representatives, followed by Boolean case splits.

The eight S_TOUCH pilot leaves were described as a depth-three complementary literal split. The supplied progress JSON records eight UNSAT answers, but this extracted archive does not include those exact eight leaf assumptions and proof traces. The generic fact that three complementary Boolean splits cover a formula cannot identify absent historical clauses.

## What is proved, inherited, and missing

| Item | Recovered status |
|---|---|
| Regularity, repeat identity, triangle bound | Direct original-graph proof above |
| Triple-edge five-cell reduction and matrix constraints | Direct original-graph proof above |
| Eight lifted $L$ cases and finite $Q$/Gram counts | Exact complete small enumeration, rerun successfully; no SAT |
| Final no-resolution claim | Explicit support table and parity proof above |
| Seven-template coverage | Direct proof above, using the now-recovered triple-edge exclusion |
| S_DISJOINT 80 symmetry cases | Direct orbit coverage above; historical CNF correspondence remains separate |
| S_TOUCH 8 answers | Historical RAW_UNSAT only |
| S_DISJOINT 80 answers | Historical RAW_UNSAT only |
| Exclusion of all double-repeat templates | Historical RAW_UNSAT only |
| Full order-62 exclusion / Lean theorem | Not established |

The pilot record has 45 of 56 RAW_UNSAT leaves: D0_EDGE_BIN 8, D0_EDGE_BOUT 8, D0_MATCH 7, D1_MATCH 7, D2_MATCH 7, and S_TOUCH 8. Its RUNNING label is historical, not a current process. The final S_DISJOINT record has 80 of 80 RAW_UNSAT canonical roots, no live solvers, and approximately 473.684 seconds of queue wall time. Neither JSON is a proof trace.

The old single-instance results for rooted parent classes 02, 03, 04 would cover all five double-repeat templates after the proved relabeling, but those results are also RAW. Therefore certifying only S_TOUCH and S_DISJOINT would still leave the double-repeat region uncertified.

## Minimum remaining route to an order-62 upper bound

The smallest recovered *mathematical* gap is no longer the triple-edge lemma or seven-template classification. The remaining obligations are:

1. Close the five double-repeat templates by mathematics or independently checkable UNSAT proofs. The three old parent classes 02–04 are an alternative covering family if their actual encodings and proof traces can be recovered or generated.
2. Close S_TOUCH and S_DISJOINT by mathematics or checked UNSAT proofs. The 80-case S_DISJOINT symmetry coverage is recovered above; its RAW answers need certificates. The exact S_TOUCH leaf split must accompany any leaf certificates, or its unsplit base can be certified instead.
3. Connect the original graph templates to the selected CNF encoding by an explicit satisfiability-preservation proof. A proof checker verifies a formula's contradiction, not the formula's relation to arbitrary graphs. The archived A+B source is available, but this bounded task did not audit every counter encoding and variable map.
4. For the project's final standard, formalize or reflect the reduction, finite enumeration, encoding bridge, and selected contradiction certificates in Lean. No new axiom or completed formal upper bound is claimed here.

No short structural contradiction for S_TOUCH or S_DISJOINT was obtained in this bounded review. Their local constraints give the useful canonical coordinates above but leave unknown edges among 53 vertices; the RAW status supplies no mathematical lemma that can simply be substituted into a proof. The order-63 cyclotomic argument also does not transfer directly: the repeat matrix here is cubic rather than a union of cycles, so its eigenvalue fields are not covered by the conductor-63 norm table.

## Open risks and non-claims

The recovered triple-edge proof should receive an independent mathematical review, especially the original-graph block derivation and the finite checker's completeness argument. Its small checked computation can be formalized independently of any large SAT run. The historical solver records establish neither nonexistence nor existence. This document does not change any archived input or status file, restart an old search, claim a graph construction, or establish the exact value of $N(8,2)$.

## New branch closure, 2026-10-11

S_TOUCH is now excluded by the independent pure saturated-row argument in S_TOUCH_SATURATED_ROW_EXCLUSION.md (fresh delta PASS8, Gemini B13). It does not rely on the archived RAW leaves or the fresh UNKNOWN runs. The earlier seven-template coverage remains valid; six templates remain open. No whole-order62 exclusion follows.

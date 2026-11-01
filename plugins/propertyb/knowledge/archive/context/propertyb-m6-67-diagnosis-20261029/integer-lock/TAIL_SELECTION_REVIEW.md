# Tail lock-selection review: 42, 43 and 44 vertices

**PASS (same-family / provisional).** The proposed structural selection arguments are valid. They remove every failing pattern recorded in `../pilot/FIVE.json` at $v=42,43,44$, assuming its probability bounds are correct. This review reads those existing rational results and checks their classification/strictness; it does not independently recompute the probability formula, run a new probability table, or close $m(6)\ge67$.

Throughout, $H$ is a finite simple pair-covering six-uniform hypergraph, with at most 66 edges and hence total degree at most 396. Write $\lambda_{xy}$ for actual codegree. For $v\in\{42,43,44\}$, pair coverage implies
\[
5d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,
\]
so every degree is at least nine. Put $L=\{x:d(x)=9\}$ and $r=|L|$. The degree budget gives
\[
396\ge9r+10(v-r)=10v-r,\qquad r\ge10v-396.
\]
On $L$, join distinct vertices in the conflict graph $G$ when their codegree is at least two. Then
\[
\deg_G(x)\le\sum_{y\ne x}(\lambda_{xy}-1)=45-(v-1)=46-v.
\]
A greedy independent set therefore has size at least $\lceil r/(47-v)\rceil$. Every independent set in $G$ consists of actual degree-nine vertices with all pairwise codegrees exactly one. Thus the guaranteed independent-set sizes at $v=42,43,44$ are respectively 5, 9 and 15. At $v=44$, every vertex has degree nine because $9\cdot44=396$ already exhausts the budget.

**Lemma A (42 vertices: exclude a common five-point trace).** There are five degree-nine unit-codegree locks not contained together in any hyperedge.

**Proof.** Choose an independent five-set $S\subseteq L$, which exists because $r\ge24$ and $\Delta(G)\le4$. If no edge contains $S$, the result already holds. Otherwise fix $E\in H$ containing $S$. Since $|E|=6$,
\[
|L\setminus E|\ge24-6=18.
\]
There are at most $\sum_{x\in S}\deg_G(x)\le20$ conflict incidences between $S$ and $L\setminus E$. If every vertex of $L\setminus E$ had at least two neighbors in $S$, there would be at least 36 such incidences, a contradiction. Choose $y\in L\setminus E$ with at most one neighbor in $S$, and choose four vertices $A\subseteq S$ not adjacent to $y$. Then $T=A\cup\{y\}$ is independent. If an edge $F$ contained $T$, any two vertices of $A$ would lie in both $E$ and $F$. Their codegree is one, so $F=E$, contradicting $y\notin E$. Therefore $T$ has the required property. $\square$

**Lemma B (nine unit-codegree vertices: exclude every trace of size four or five).** If $S_0$ is a set of nine vertices with pairwise codegrees one, there is a five-set $T\subseteq S_0$ with $|F\cap T|\le3$ for every hyperedge $F$.

**Proof.** If every edge already meets $S_0$ in at most three vertices, choose any five of its vertices. Otherwise choose an edge $E$ with $|E\cap S_0|\ge4$. Since $|E|=6$, there are at least three vertices in $S_0\setminus E$. Choose three vertices $A\subseteq E\cap S_0$ and two vertices $B\subseteq S_0\setminus E$, and put $T=A\cup B$. The edge $E$ meets $T$ in exactly three vertices. For any other edge $F\ne E$, one has $|F\cap E\cap S_0|\le1$: two such vertices would have at least two common edges, contradicting unit codegree. Therefore
\[
|F\cap T|\le |F\cap A|+|F\cap B|\le1+2=3.
\]
This proves the lemma. $\square$

At $v=43$, the independent-set bound supplies nine degree-nine vertices, so Lemma B applies. At $v=44$, it supplies at least fifteen; take any nine and apply Lemma B. All selected vertices retain degree nine and unit pairwise codegree.

## Exact correspondence with the existing table

For a labelled five-lock set, a multi-lock trace is encoded by a mask in $\{1,\ldots,31\}$ with at least two set bits. Unit codegree means the clique edge sets associated with these masks form an exact partition of the ten pairs of five labels. Conversely every such partition is a necessary trace pattern; singleton counts are recovered from degree nine and the empty count from the 66-edge budget. Extra global realizability conditions would only remove patterns and are unnecessary for this coverage argument.

A separate short recursive exact-pair-cover calculation rebuilt all 32 labelled partitions and confirmed equality with the 32 distinct masks lists at each of the three vertex counts. This was a classification check, not a new probability calculation. Every stored `strict` flag was checked against `Fraction(U)<1`.

The stored non-strict rows are exactly:

| $v$ | Masks | Stored $U$ |
|---:|---|---:|
|42|`[31]`|2607524/2561251|
|43|`[31]`|2607524/2561251|
|44|`[5,6,12,20,27]`|166491788/166481315|
|44|`[31]`|102923518/99888789|

Mask 31 is a five-point trace, excluded by Lemma A and Lemma B. Mask 27 has four set bits; the other four masks pair the omitted label with the four labels in 27. Thus the second $v=44$ failure is exactly a four-point trace plus its remaining four pairs. Lemma B excludes it, along with all five possible labelled four-point trace patterns. Only one of these five four-point patterns failed in this particular table; excluding all five is a valid stronger structural restriction and avoids relying on positional symmetry.

| $v$ | Structural restriction | Retained labelled patterns | Maximum stored $U$ among retained patterns |
|---:|---|---:|---:|
|42|Every trace has size at most 4|31|1382147533/1383075540|
|43|Every trace has size at most 3|26|48389416/48663769|
|44|Every trace has size at most 3|26|132269531/133185052|

Every retained value is strictly below one. These are exact rational comparisons of the stored numerical output, not a second probability implementation.

**Scope of acceptance.** Both short structural lemmas and their application to the recorded tail patterns pass. This justifies the proposed $v=42,43,44$ repair conditional on the existing certificate formula and table calculation. The task's remaining $31\ldots41$ domain is not addressed; no full new lower bound, Lean proof, or cross-family approval is claimed.

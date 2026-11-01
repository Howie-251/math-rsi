# Independent audit of the complete 39-point branch

**PASS (same-family / provisional).** The weak-four-lock selection in `../tail39_41/PROOF39.md` is valid, the complete necessary degree/trace domain has exactly 999 labelled types, and all 999 recorded layouts independently reproduce the submitted exact rational bound, strictly below one. The largest value is
\[
\frac{113467943}{113476275}<1.
\]
The actual replay took 3.999240 CPU seconds and approximately 4.318 wall seconds. It is a local 39-point branch result under the declared upper-level reduction and conditional-permutation probability theorem; it does not assert the full bound $m(6)\ge67$.

## Selection and actual-input coverage

Fix the same actual simple six-uniform, pair-covering hypergraph on 39 vertices with exactly 66 edges. Pair coverage gives $5d(x)\ge38$, hence $d(x)\ge8$. For the integer low-degree selection lemma with cutoff $D=10$, one has
\[
Z=11\cdot39-396=33,\qquad
Q=\max_{d=8,9,10}(5d-37)(11-d)=\max(9,16,13)=16.
\]
Since $33>2\cdot16$, there are three distinct vertices with degrees in $8,9,10$ and all three codegrees one. This follows from the conflict graph argument and integer reciprocal lower bound already proved in `context/propertyb-m6-67-diagnosis-20261029/integer-lock/REVIEW.md`, Lemma 2. It does not assume the desired fourth lock.

Let this actual triple be $S$ and let $t$ be its total degree. For each of the 36 vertices outside $S$, set
\[
e_y=\sum_{x\in S}(\lambda_{xy}-1)\ge0.
\]
Each original pair inside $S$ has codegree one and contributes twice to the sum of the three incidence counts. Consequently,
\[
\sum_{y\notin S}e_y=5t-6-3\cdot36=5t-114=:E.
\]
At most $\lfloor E/2\rfloor$ external vertices have $e_y\ge2$, so at least $p=36-\lfloor E/2\rfloor$ have $e_y\le1$. Their degrees are still at least eight. The total degree excess above eight among all external vertices is exactly
\[
396-t-36\cdot8=108-t.
\]
Thus at least one of the eligible external vertices has degree at most $D_4=8+\lfloor(108-t)/p\rfloor$. Otherwise the eligible vertices alone contribute at least $p(D_4+1-8)>108-t$ excess, a contradiction. This vertex is explicitly outside $S$, hence distinct from all original locks. Its nonnegative integer excess $e_y\le1$ means its three codegrees to $S$ are either all one, or exactly one is two and the other two are one.

All integer calculations are:

| $t$ | $E$ | $p$ | External degree surplus $108-t$ | $D_4$ |
|---:|---:|---:|---:|---:|
|24|6|33|84|10|
|25|11|31|83|10|
|26|16|28|82|10|
|27|21|26|81|11|
|28|26|23|80|11|
|29|31|21|79|11|
|30|36|18|78|12|

The ten nondecreasing triples from $\{8,9,10\}$, each paired with every fourth degree from eight through its corresponding $D_4$, give 37 distinguished-fourth degree tuples. No ordering constraint is imposed between the fourth degree and the first three. Sorting the original triple only relabels actual vertices and preserves all its possible doubled-pair locations.

## Independent multiset-trace classification

Each at-least-two-point trace on the four locks consumes one unit of every pair contained in that trace. The pair-capacity vector is either $(1,1,1,1,1,1)$ or has exactly one capacity two at an original-lock/fourth-lock pair. Every trace of size at least three contains an original-triple pair of capacity one, so cannot repeat. The doubled two-point trace itself may occur twice, and must be treated as a multiset rather than discarded as a duplicate.

The independent program does not import the submitted `parts` generator. It processes all eleven clique masks in increasing numerical order, and maintains a forward dynamic program on the six used-pair capacities. At each clique it independently takes every multiplicity from zero through the remaining capacity minimum on that clique. Each multiset is represented exactly once because each clique is processed once, and a final state is accepted exactly when all target capacities are filled. Any actual trace multiset follows one of these decisions, so coverage is complete.

This reconstructs six all-unit patterns and seven patterns for each of the three doubled-pair locations. Each necessary degree tuple has $6+3\cdot7=27$ patterns, giving exactly $37\cdot27=999$ types. The certificate has exactly 999 rows, no duplicate keys, and its complete key set equals this independently reconstructed domain. Every recorded empty/singleton/multilock trace count was rebuilt from the multiset and degrees; total count 66, nonnegativity, all four actual degree marginals, and all six requested pair-codegree marginals were checked.

## Independent exact probability replay

`check.py` imports the guarded `bound` function in `../root/independent40_41.py`; that module only extracts the pre-existing independent falling-factorial injection kernel from `context/propertyb-m6-66-20261029/independent/check.py`. Neither the old checker's main body nor the guarded 40/41 replay executes. No submitted 39-point probability module or classification generator is imported.

For each actual recorded position vector, the independent kernel counts injections of named free vertices directly. Four positions need not appear in increasing label order: label $j$ remains attached to `positions[j]`, its degree and every trace mask bit throughout. All positions are distinct and in $1,\ldots,39$. In particular, all 34 rows with nonmonotone label positions were replayed without sorting; these are the repaired layouts.

The independently implemented deletion enumerates every $R\subseteq S\setminus\{j\}$. If $f_R$ actual edges contain $j$ and avoid $R$, their distinct five-point links lie on at most $38-|R|$ vertices. Counting link vertex repetitions gives
\[
5f_R\le38-|R|+4B_R,
\]
because two distinct links intersect in at most four vertices. Thus $B_R\ge q_R=\max(0,\lceil(5f_R-38+|R|)/4\rceil)$. For that $R$, filling available unordered trace cells in increasing exact cost order for $q_R$ units gives a lower bound on the same actual bad-pair weight. Taking the maximum over $R$ preserves the lower-bound direction; it does not add overlapping costs. The independent replay uses this maximum, complete cell capacities and both directed weights, matching the claimed mathematical criterion.

All 999 bounds satisfy the exact checks
\[
U_{\mathrm{independent}}=U_{\mathrm{CERT39}}<1.
\]
Full rows, selection arithmetic, reconstructed patterns, comparison results and measured execution times are in `CHECK.json`.

Reproduce from the project root:

```sh
python3 context/propertyb-m6-67-progress-20261029/independent39/check.py
```

The program has a 60 CPU-second / 150 wall-second limit. This audit provides full local arithmetic and classification evidence, with the usual software trust and the declared upstream mathematical imports. There was no Lean execution or new external-model review in this audit.

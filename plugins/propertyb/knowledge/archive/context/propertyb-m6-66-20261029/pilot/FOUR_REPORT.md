# Four unit locks close the M65 high-vertex profile domain

All 132 necessary four-lock profiles for v=40…43 have strict exact Fraction bounds under the **original** end/start/critical-pair formula and full-pool bad-link deletion. No strengthened subtraction, five locks, or position search was needed. This closes this conditional high-vertex arithmetic domain; it does not alone assert the whole m(6)≥66 theorem.

## Selection of four pairwise-codegree-one vertices

The root supplied the general low-degree selection inequality; here is its substitution in this domain. Assume the same padded pair-covering 65-edge simple 6-uniform hypergraph as in REPORT.md. Let L={x:d(x)≤D}, r=|L|, and let G connect pairs in L of codegree at least two. Set

`Z=(D+1)v−390`, `T=5(D+1)−v+2`.

Since vertices outside L have degree at least D+1,

`sum_{x∈L} d(x) ≤390−(D+1)(v−r)`.

Pair coverage implies deg_G(x)≤5d(x)−(v−1), and hence

`r+2e(G) ≤ Tr−5Z`.

Caro–Wei and Cauchy give α(G)≥r²/(r+2e(G))≥r²/(Tr−5Z). The denominator is positive because it is at least r>0 for an actual hypergraph. For four independent vertices it suffices that r²>3(Tr−5Z). Completing the square shows this for every real r if 20Z>3T². The following exact substitutions hold:

|v|D|min degree d0|r≥ceil(Z/(D+1−d0))|Z|T|20Z|3T²|
|---|---|---|---|---|---|---|---|
|40|10|8|17|50|17|1000|867|
|41|9|8|10|20|11|400|363|
|42|9|9|30|30|10|600|300|
|43|9|9|40|40|9|800|243|

Thus each actual hypergraph in these vertex ranges admits four locked vertices of pairwise codegree one, with degrees respectively in [8,10], [8,9], {9}, {9}. The selected vertices may be relabeled to give nondecreasing degrees.

## Complete four-lock incidence classification

For a fixed set of four pairwise-codegree-one vertices, every pair belongs to exactly one original hyperedge. Each original edge meeting the locks in at least two vertices defines a clique on that intersection. These cliques partition the six edges of K4: no pair repeats, and every pair appears. Conversely the only clique partitions are:

1. All six 2-cliques.
2. One 3-clique and its three complementary 2-cliques, with four choices of the 3-clique.
3. One 4-clique.

This gives six **labelled** patterns. For each pattern, put ell_T=1 for each clique block T, and ell_{i}=d_i−number of blocks containing i. The remaining empty type is ell_0=65−sum_{T≠0}ell_T. These are all true edge types. `FOUR.py` generates clique partitions by recursively covering the first uncovered K4 pair with a clique whose whole pair-set is uncovered. This gives exactly six distinct outputs. It enumerates every nondecreasing degree tuple in each degree interval and all six labelled patterns, so the relabeling of unequal degrees does not lose incidence configurations.

## Exact numerical results

The four positions are the consecutive slots

`floor(v/2)−1, floor(v/2), floor(v/2)+1, floor(v/2)+2`.

|v|necessary profiles|maximum U|worst degrees|worst pattern|
|---|---|---|---|---|
|40|90|3141/3190|10,10,10,10|one four-lock edge|
|41|30|1375025/1397046|8,8,8,9|one four-lock edge|
|42|6|241664898/243318845|9,9,9,9|one four-lock edge|
|43|6|12775536/12806255|9,9,9,9|one four-lock edge|

Every displayed rational is strictly below one. All rows are saved in FOUR.json. The run used 0.44848 CPU seconds. Reproduce from project root with:

```
python3 context/propertyb-m6-66-20261029/pilot/FOUR.py
```

No original files, Lean files, wiki, AGENTS, or v2 files were changed. This is deterministic arithmetic plus an explicit finite local classification and selection proof; it has not been independently reimplemented or formally checked in Lean.

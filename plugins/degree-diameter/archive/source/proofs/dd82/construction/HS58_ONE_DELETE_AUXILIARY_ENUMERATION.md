# Four necessary order-eight auxiliary domains for the HS58 one-deletion model

Date: 2026-10-12.

One complete enumeration closes three of the four stated necessary
auxiliary domains. The remaining domain has **870 labelled auxiliary
graphs**. These are necessary candidates, not completed order-58 graphs.
The mathematical bridge from an HS58 target to these domains belongs to
`HS58_ONE_DELETE_ARBITRARY_ADDITIONS.md`.

## Inputs and complete results

Let $m\in\{4,5\}$. The auxiliary graph $H$ has vertex set $\{0,\ldots,7\}$
and $6+m$ edges. The two endpoint attachment sets are $U=\{0,1\}$ and
either $V=\{0,1\}$ or $V=\{0,2\}$. Every pair at distance greater than
two in $H$ must be the pair $U$ or the pair $V$. Disconnected pairs are
included as bad pairs. The degree bounds are

$$d_H(a)\le
\begin{cases}
6,&a\in U\cap V,\\
7-m,&a\in U\mathbin{\triangle}V,\\
8-m,&a\notin U\cup V.
\end{cases}$$

These bounds count endpoint attachments and the at least $m$ attachments
from $R$ required for each color outside $U\cap V$. The HS proof author
confirmed the input conditions and the completeness of the two possible
intersection types before the run. No additional orbit assumption about
old HS vertices was imposed.

| $m$ | $|U\cap V|$ | Degree-bounded graphs checked | Survivors |
|---:|---:|---:|---:|
| 4 | 2 | 10350991 | 0 |
| 4 | 1 | 6721718 | 0 |
| 5 | 2 | 1978650 | 870 |
| 5 | 1 | 102256 | 0 |

All four enumerations completed in a single process, using approximately
0.70 CPU seconds under one shared ten-second cap. The process used one
thread and 8388 KiB maximum resident memory. No cap was reached.

## Why the finite edge domain is complete

The C++ source lists all 28 unordered pairs of distinct labels in
lexicographic order. Its recursion branches on including or excluding
the next edge, keeping the number of edges still required. It prunes
only when too few pairs remain, or when inclusion would exceed one of
the supplied endpoint degree caps. Since degrees only increase, the
latter branch cannot extend to an admissible graph.

When no further edges are required, the remaining pairs are absent and
the complete graph is checked. Thus every labelled graph with the exact
edge count and degree bounds occurs exactly once. There is no
isomorphism pruning, triangle restriction, connectivity assumption or
heuristic selection.

At each leaf, the radius-two set at vertex $a$ is computed exactly as

$$\{a\}\cup N_H(a)\cup\bigcup_{b\in N_H(a)}N_H(b).$$

Any missing label must be the other endpoint of the allowed pair $U$
or $V$ involving $a$. This implements precisely the supplied bad-pair
condition. The saved completion flags are true for all four cases,
and the shared timeout flag is false. The three zero counts therefore
close their entire stated labelled domains.

## Saved examples, symmetry recovery and verification scope

The initial run saved the first 100 complete edge lists from the
870-survivor case, as allowed by its declared output limit. It did not
save all 870 graphs.

Applying the permutations of labels $2,\ldots,7$ and optionally
interchanging labels 0 and 1 to those examples recovers **510 distinct
graphs**, in three orbits of sizes 30, 120 and 360. Exact sorted edge
sequences are used for orbit deduplication. The degree caps, exact edge
count and all pairwise distances of every recovered graph were checked
independently by Python BFS. This does not repeat the 28-edge enumeration.

The other **360 counted survivors were not recovered**. No assumption is
made about their isomorphism types or further properties. In particular,
`all_survivors.json` explicitly marks its 510-graph list as incomplete.

The later necessary condition
$d_H(0)+d_H(1)\in\{9,10\}$ was recorded but not used in the four-domain
enumeration. Filtering the recovered 510 graphs by that condition leaves
150 examples, in the 30- and 120-element orbits. This is only a filter of
the recovered subset; it is **not a certified complete filtered count
for all 870 graphs**. No new enumeration was run to resolve that question.

## Files and reproduction

The actual enumeration source and runner are
`computations/dd82/construction/hs58_one_delete_auxiliary.cpp` and `.py`.
The independent verifier and symmetry recovery are in
`hs58_one_delete_auxiliary_verify.py`.

The directory `computations/dd82/construction/hs58_one_delete_auxiliary_run/`
contains:

- `enumeration.json`: complete four-domain counts, degree bounds,
  completion flags and the first 100 survivor edge lists;
- `enumeration.log`, `resources.json`: process and resource records;
- `all_survivors.json`: 510 recovered graphs, explicitly marked incomplete;
- `verification.json`: orbit representatives and independent checks of all 510;
- `common_degree_filtered_examples.json`: 150 examples from the recovered
  subset, explicitly without a global completeness claim.

From the project root:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/hs58_one_delete_auxiliary.cpp -o computations/dd82/construction/hs58_one_delete_auxiliary.bin
python computations/dd82/construction/hs58_one_delete_auxiliary.py
python computations/dd82/construction/hs58_one_delete_auxiliary_verify.py
```

The enumeration establishes only these necessary auxiliary-domain
results. Any whole HS58-family conclusion additionally requires the
mathematical reductions and closure of the surviving case.

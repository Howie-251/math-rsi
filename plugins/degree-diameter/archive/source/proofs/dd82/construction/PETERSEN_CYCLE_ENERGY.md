# An exact short-cycle energy for six Petersen fibers

## Claim and status

**PROVABLE AS STATED.** For every graph formed from six induced Petersen graphs and one perfect matching between each pair of fibers, let $T$ be its number of triangles and $F$ its number of unoriented simple four-cycles. Then

$$\boxed{E=2F+3T-150\geq0,\qquad E=0\ \Longleftrightarrow\ \operatorname{diam}(G)\leq2.}$$

This gives a new exact objective for construction search, coupling missing pairs to excessive route multiplicity. It is not a nonexistence proof for the full six-fiber family.

## Assumptions and notation

All graphs are simple and undirected. There are sixty vertices, eight neighbors per vertex, and $240$ edges. Write $A$ for adjacency, $J$ for the all-ones matrix, and

$$B=A^2+A-7I-J.$$

For distinct vertices $u,v$, let $c_{uv}=|N(u)\cap N(v)|$ and $b_{uv}=c_{uv}+A_{uv}-1$. Thus $b_{uv}$ is one less than the number of direct-edge and two-step route slots joining the pair. The diagonal entries of $B$ are zero.

## Proof

### 1. Defect blocks have fixed integral margins even before diameter two

Every within-fiber block of $B$ is zero. The Petersen graph has no common neighbor for adjacent vertices and exactly one for nonadjacent distinct vertices; a vertex in another fiber cannot be adjacent to two vertices of the original fiber because the connecting edges form a matching.

Every cross-fiber block of $B$ has every row and column summing to one. The direct edge and the two internal-neighbor triples give seven route slots, and the other four fibers give four more slots; subtracting the ten entries of $J$ leaves sum one. This assertion does not assume that all targets are covered.

If integers $z_1,\ldots,z_{10}$ sum to one, then $\sum z_i^2\geq1$, with equality exactly when one is one and the others zero. There are $60\cdot5=300$ cross-block rows. Consequently

$$\operatorname{tr}(B^2)=\sum_{u,v}B_{uv}^2\geq300.$$

Equality holds exactly when all thirty directed cross blocks are permutation matrices. Equivalently all cross route counts are positive, which is exactly diameter at most two since within-fiber pairs are already covered.

### 2. Express the squared defect through short cycles

For an eight-regular graph on sixty vertices,

$$\operatorname{tr}(A^2)=480,\qquad
\operatorname{tr}(A^3)=6T,\qquad
\operatorname{tr}(A^4)=7200+8F.$$

The fourth-power identity separates the closed walks using only one or two edges, contributing $60\cdot8(2\cdot8-1)=7200$, from the eight oriented closed walks on each four-cycle. Expanding $B^2$, using $AJ=8J$, $J^2=60J$, and $\operatorname{tr}(A)=0$, gives

$$\operatorname{tr}(B^2)=\operatorname{tr}(A^4)+2\operatorname{tr}(A^3)-7500
=8F+12T-300.$$

It follows that

$$E=2F+3T-150=\frac{\operatorname{tr}(B^2)-300}{4}.$$

The preceding step proves nonnegativity and the equivalence with diameter two. $\square$

## Exact interpretation of the new energy

Every row of $B$ sums to five, so $\sum_{u,v}B_{uv}=300$. Therefore

$$E=\sum_{u<v}\frac{b_{uv}(b_{uv}-1)}2.$$

The only negative possible value of $b_{uv}$ is $-1$, occurring exactly when the pair is neither adjacent nor has a common neighbor. Values zero and one contribute nothing. Hence

$$\boxed{E=\#\{\text{bad unordered pairs}\}
 +\sum_{u<v:\ b_{uv}\geq2}\binom{b_{uv}}2.}$$

A pair with three route slots has penalty one; four route slots have penalty three; five route slots have penalty six. Thus a move that merely concentrates repeat routes can reduce the number of bad pairs without improving this energy. Both objectives vanish exactly on valid target graphs, but their nonzero landscapes differ.

For an implementation using common-neighbor counts, the directly incremental expression is

$$\boxed{E=\sum_{u<v}\left[\binom{c_{uv}}2+A_{uv}c_{uv}\right]-150.}$$

Indeed each four-cycle contributes to two opposite pairs, while each triangle contributes on its three edges. A switch affecting four vertex neighborhoods changes only pair contributions with at least one endpoint among those four vertices. Deduplicate those pairs and recompute their integer contributions before and after the move.

## Local and global necessary conditions on a target

Let $t_v$ and $f_v$ be the numbers of triangles and four-cycles containing $v$. The same diagonal calculation gives, for every construction candidate,

$$e_v=f_v+2t_v-5=\frac{(B^2)_{vv}-5}{2}\geq0,\qquad \sum_v e_v=2E.$$

At a target, every $e_v=0$, so

$$f_v+2t_v=5,\qquad t_v\in\{0,1,2\},\qquad f_v\in\{5,3,1\}.$$

In particular the number of triangles is even and at most forty, and

$$F=75-\frac{3T}{2}.$$

For each pair matching, let $q_{ij}$ be the number of shared edges between the source Petersen graph and the pulled-back target Petersen graph, as in `PETERSEN_MATCHING_CONSTRAINT.md`. Each such edge gives a distinct four-cycle using exactly those two fibers. Therefore

$$\sum_{i<j}q_{ij}\leq F,\qquad 2\sum_{i<j}q_{ij}+3T\leq150$$

for a target. Triangles use three distinct fibers. Four-cycles use two, three, or four fibers, so the energy can also be evaluated through short matching compositions on small sets of fibers.

## Actual saved candidates

The independent expanded-edge reader `computations/dd82/construction/petersen_cycle_energy.py` rebuilds all common-neighbor counts, verifies the six-fiber degree pattern and defect block margins, and evaluates both formulas for the energy. It records:

| Expanded candidate | Bad pairs | Triangles | Four-cycles | Extra crowding penalty | $E$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| `petersen_six_fibers.best.edges` | 50 | 0 | 100 | 0 | 50 |
| `petersen_all_matchings_run/snapshot20.json` | 20 | 0 | 100 | 30 | 50 |
| `petersen_all_matchings_run/candidate.best.edges` | 20 | 0 | 100 | 30 | 50 |

The old fifty-bad-pair graph has fifty vertices with $e_v=2$ and ten with $e_v=0$. The twenty-bad-pair graph has twenty vertices with $e_v=5$ and forty with $e_v=0$. Its ten pairs with $b_{uv}=3$ each contribute three units of crowding penalty. All three have $\operatorname{tr}(B^2)=500$ and total pair-matching overlap zero.

The exact reports are in `computations/dd82/construction/petersen_cycle_energy.json`.

## Immediate bounded experiment using the new objective

Root applied the proved energy in `petersen_all_matchings.cpp`, using exact
pair-contribution changes at the four or eight affected vertex rows. Every
4096 proposals, the incremental value was checked against a full integer
recomputation; all checks passed. The new run retains all fifteen independent
matchings, starts from the twenty-bad-pair candidate, and makes both ordinary
and missing-route-guided matching switches. Energy is primary and bad-pair
count breaks ties between saved best candidates.

One run used 90.0014 CPU seconds, 90.0801 wall seconds and 37220352 proposals.
It did not improve the initial E=50, twenty-bad-pair candidate. The final
expanded graph was independently checked by BFS and by the separate Python
cycle counter: T=0, F=100, E=50, extra crowding=30, diameter=3. Artifacts are
under `computations/dd82/construction/petersen_cycle_energy_run/`, including
`candidate.search.json`, `run.json`, `candidate.best.verification.json`, and
`independent_cycle_check.json`. The run completed normally; it is not a lower
bound on possible energy and should not be repeated unchanged.

## Spectral boundary and remaining gap

For a target, $B$ is a five-regular cover of $K_6$ and commutes with $A$. On the six-dimensional fiber-constant subspace, $A$ has eigenvalues $8,2,2,2,2,2$. On its orthogonal complement, an $A$ eigenvalue $\lambda$ satisfies

$$-5\leq\lambda^2+\lambda-7\leq5,$$

so $\lambda\in[-4,-2]\cup[1,3]$. The trace argument above converts the squared-defect constraint into a directly executable exact objective. It does not prove that every possible collection of fifteen matchings has $E>0$. Establishing that positive lower bound, or finding $E=0$, remains the actual construction question; the spectral interval alone does not close it.

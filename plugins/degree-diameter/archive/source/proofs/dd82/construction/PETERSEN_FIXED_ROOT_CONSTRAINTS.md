# Fixed Petersen root: exact residual permutations and a small matching catalog

## Claim and status

**PROVABLE AS STATED:** with the five saved root matchings fixed, their
normalization produces the same internal Petersen graph $Q$ in every
external fiber. Root-to-external distance-two coverage is equivalent to a
residual-permutation identity. Combining that identity with the already
available root path gives a stronger necessary condition on every external
matching. Complete enumeration leaves $18624$ possibilities instead of the
$611400$ permitted by the internal-neighbor-overlap condition alone.

This is a necessary-condition reduction, not a contradiction for the fixed
root. A further three-involution subfamily was exhaustively tested and has
at least $80$ bad pairs among the assignments satisfying root coverage.
Neither result excludes general six-Petersen-fiber graphs or order $60$.

## Assumptions and notation

Use the saved

```text
A = [5,9,8,7,6,3,2,1,0,4]
```

and fix the five root matchings $M_{\infty,i}=AR^{-i}$ from the preceding
[Petersen construction](PETERSEN_SIX_FIBERS.md). In each original fiber,
$P$ has vertices $(e,x)$ for $e\in\{0,1\}$ and $x\in\mathbb F_5$, with
steps $\pm1$ in layer $0$, steps $\pm2$ in layer $1$, and equal-coordinate
spokes. Thus

$$A(0,x)=(1,-x),\qquad A(1,x)=(0,-x+3),\qquad R(e,x)=(e,x+1).$$

All matrix conventions below use the source as row and target as column.
The symbol for a matching also denotes its permutation matrix.

## Proof strategy and dependency map

1. Check the coordinate change and the fixed matrices $P,Q,T$.
2. Count the eleven root-to-fiber path slots to identify the exact residual.
3. Count the eight already determined paths between two external fibers;
   only three further intermediate fibers remain.
4. Enumerate the resulting local permutation condition, retaining its full
   table. Separately test a finite three-involution subfamily to show the
   root conditions themselves are consistent.

## 1. Coordinate normalization

Change coordinates in external fiber $i$ by

$$v\longmapsto R^iA^{-1}v.$$

Every root matching becomes the identity. Directly from the displayed rule
for $A$,

$$ARA^{-1}=R^{-1}.$$

Since $P$ is preserved by $R$, the transformed internal graph in fiber $i$
is

$$R^iA^{-1}PA R^{-i}=A^{-1}PA=:Q,$$

independent of $i$. Concretely, $Q$ has steps $\pm2$ in layer $0$, steps
$\pm1$ in layer $1$, and spokes $(0,x)\sim(1,x+3)$.
The root fiber retains $P$.

The graphs $P$ and $Q$ share no edge. Consequently

$$T=J-I-P-Q$$

is a simple cubic bipartite graph, with

$$N_T(0,x)=\{(1,x+1),(1,x+2),(1,x+4)\}.$$

The reverse neighbor differences are the negatives of these offsets.

## 2. Root coverage is an exact residual-permutation identity

Write $M_{ij}$ for any of the now arbitrary external matchings, with
$M_{ji}=M_{ij}^{\mathsf T}$. For root source $u$ and target fiber $i$, the
direct route, the two internal routes and the other four external middle
fibers give the path-count matrix

$$I+P+Q+\sum_{j\ne i}M_{ji}=J-T+\sum_{j\ne i}M_{ji}.$$

Thus root coverage is equivalent to
$\sum_{j\ne i}M_{ji}\ge T$ entrywise. Transposing and using symmetry of
$T$ gives the outgoing version. Each side of the difference has row and
column sums $4-3=1$, so

$$\boxed{\sum_{j\ne i}M_{ij}=T+S_i},$$

where $S_i$ is a permutation matrix. This is also sufficient for all root
pairs to be covered. It is stronger than merely counting at least three
$T$-edges: the three distinct $T$ neighbors must all occur once, and the
fourth coordinate is exactly $S_i(u)$.

Since $M_{ji}=M_{ij}^{\mathsf T}$, another necessary compatibility identity is

$$\sum_i S_i=\left(\sum_i S_i\right)^{\mathsf T}.$$

For any $T$-edge $uv$, the graph between its five copies of coordinate $u$
and five copies of coordinate $v$ has every degree one or two. Its degree-
two vertices on the $u$ side are precisely the fibers satisfying
$S_i(u)=v$; the analogous description holds on the $v$ side. In particular
these two counts must agree. Minimum degree one alone does not imply that
this bipartite graph contains a perfect matching; no such additional claim
is used.

Let $t(M)$ be the number of its ten matched edges lying in $T$. Every fiber
has forty external edge incidences, at least thirty of which lie in $T$.
Hence

$$\sum_{j\ne i}t(M_{ij})\ge30,\qquad
\sum_{i<j}t(M_{ij})\ge75.$$

Equivalently, the total cost $\sum_{i<j}(10-t(M_{ij}))$ is at most $25$.
These are necessary numerical summaries of the stronger entrywise identity.

## 3. A stronger condition on each external matching

For a pair of external fibers, let their matching be $M$. The direct edge,
a middle vertex in either endpoint fiber, and the now fixed root route
supply the nonnegative path-count matrix

$$H(M)=I+M+QM+MQ.$$

Every row and column has eight slots. Exactly three further intermediate
fibers remain, supplying at most three new targets per source. Thus every
row of $H(M)$ must have at least seven nonzero entries. Reversing the pair
gives the same requirement on its columns:

$$\boxed{\#\operatorname{supp}H(M)_{u,*}\ge7,\qquad
\#\operatorname{supp}H(M)_{*,u}\ge7\quad\text{for all }u.}$$

In map notation, the row test is

$$\left|\{u,M(u)\}\cup N_Q(M(u))\cup M(N_Q(u))\right|\ge7.$$

This records the collision with the root label as well as the collision
between the two internal triples. For example, if the triples intersect
once, the root label must be outside their union and the direct target.
Checking only that their intersection is at most one misses this condition.

There is a useful exact continuation constraint: whenever the known union
has size seven, the three remaining middle-fiber images must be distinct
and must equal its three-element complement. When its size is eight, those
three images must cover its two-element complement. These are direct
necessary and sufficient row conditions once all ten external matchings
are chosen; they are not independent existence statements about the rows.

A special consequence concerns a same-coordinate pair. Such a pair already
has a root common neighbor. The matching's directed $Q$-edges cannot meet
head-to-tail at a coordinate, since the two internal routes would then
supply two further common neighbors. Thus the arcs $u\to M(u)$ with
$u\sim_Q M(u)$ have pairwise disjoint endpoints. This consequence is
included in the stronger support test above.

## 4. Complete local enumeration and reusable table

`petersen_fixed_root_catalog.cpp` exhausts all $10!=3628800$ permutations.
For each one it evaluates the displayed row test for both $M$ and $M^{-1}$,
which is the row-and-column test. The initial run took $0.068$ CPU seconds;
the retained run also wrote the full table and took $0.077$ CPU seconds.
There are $27864$ permutations passing the forward test and $18624$ passing
both directions. The complete accepted table is
`computations/dd82/construction/petersen_fixed_root_catalog.perms.txt`, one
permutation per line in the fixed normalized coordinate order.

The numbers by $t(M)$ are:

| $t(M)$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Accepted matchings | 233 | 850 | 2290 | 3900 | 3825 | 3512 | 2585 | 700 | 670 | 30 | 29 |

Thus high-$T$ matchings are a small explicit part of the local table, while
the total cost budget forces the ten selected matchings to be concentrated
toward that end. It does not force every individual matching to have seven
or more $T$-edges. The JSON also retains the layer-preservation and internal-
overlap distributions.

This table is a substantially smaller domain than the $611400$ permutations
satisfying the original internal-overlap bound. Selecting mutually
compatible table entries on all ten fiber pairs remains an unsolved joint
obligation; counting the entries does not discharge it.

## 5. A finite compatible-root subfamily and its failure

For $t\in\{1,2,4\}$ define the involution

$$U_t(0,x)=(1,x+t),\qquad U_t(1,x)=(0,x-t).$$

All its edges lie in $T$, and it passes the local support test. Assign one
of these three matchings independently to each of the ten external fiber
pairs. Root coverage holds exactly when every vertex of the fiber-level
$K_5$ is incident to all three colors. This is an exact reformulation of
the residual identity for this restricted choice of matchings.

A complete enumeration of $3^{10}=59049$ color assignments found $900$
satisfying root coverage. This supplies explicit evidence that the root
identities and the stronger local table are jointly consistent at this
level; they do not themselves prove the fixed-root family impossible.

All $900$ resulting graphs were expanded and their complete two-step unions
were counted. Their bad-pair histogram is

| Bad pairs | 80 | 90 | 100 | 120 | 130 | 140 |
|---|---:|---:|---:|---:|---:|---:|
| Assignments | 120 | 240 | 180 | 180 | 120 | 60 |

The saved minimum candidate was separately read back from its edge file
and checked by all-source BFS; all root pairs are covered and exactly
$80$ external pairs fail. Its complete bad-pair witnesses are retained.
The whole enumeration plus this BFS took $0.221$ CPU seconds.
The claimed minimum $80$ concerns the $900$ root-covering assignments; the
remaining assignments already fail required root coverage.

Files are `computations/dd82/construction/petersen_fixed_root_three_shifts.py`,
`.json`, `.best.edges`, and `.best.verification.json`.
No SAT or repeated annealing was run in this subtask.

## Corrections, boundaries and open risks

- The incoming root coverage statement becomes the outgoing per-vertex
  statement by transposition, using symmetry of $T$; it is not a change of
  direction by convention alone.
- The gauge uses the specific fixed $A$ and its normalization of $R$.
  Releasing the root matchings generally produces different internal
  matrices $Q_i$, so this table and its fixed $T$ cannot automatically be
  applied to that larger experiment.
- No contradiction for all fixed-$A$ matchings is obtained. The completed
  finite exclusion concerns only the three chosen involutions.
- No unrestricted order-$60$ conclusion follows, and no Lean work is
  needed for the current bounded construction analysis.

## External construction discussion C3

Gemini read the substantive argument above and found no gap, using the existing Antigravity thread and requested/CLI-selected gemini-3.8-flash-high/high. Raw response: `reviews/dd82/20261011_C3_petersen_hs59.json`. Root independently read the argument and retained exact result scopes. This discussion is provisional corroboration, not a Lean proof or backend model attestation.
C3 wording limits are recorded in `reviews/dd82/20261011_C3_root_notes.md`; route caps are necessary only and equal energy at two candidates is not a conservation law.

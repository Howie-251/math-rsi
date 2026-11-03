# Six Petersen fibers: explicit construction, failed candidate, and a small-family obstruction

## Claim and status

**PROVABLE AS STATED:** the construction below produces a simple $60$-vertex,
$8$-regular graph with $240$ edges from three permutations in $S_{10}$; its
remaining diameter-two obligation is exactly the three displayed coverage
relations. The further reflection/translation subfamily in Section 5 has at
least $50$ uncovered unordered pairs, and this bound is attained.

**Not established:** existence or nonexistence in the full three-permutation
family, the larger six-Petersen-fiber family, or arbitrary order-$60$ graphs.
The saved candidate has diameter $3$ and is not a lower-bound improvement.

## Assumptions and notation

Write the Petersen vertices as $(e,x)$ with $e\in\{0,1\}$ and
$x\in\mathbb F_5$. Layer $0$ has steps $\pm1$, layer $1$ has steps $\pm2$,
and $(0,x)$ is joined to $(1,x)$. In files, $(e,x)$ is vertex $5e+x$.
Let $P$ denote this graph and $N_P(u)$ its three neighbors.
The permutation $R(e,x)=(e,x+1)$ is an order-five automorphism: it preserves
both within-layer difference rules and the spokes, and has no fixed points.
Composition acts right to left.

There are fibers indexed by $\infty,0,1,2,3,4$, each inducing $P$.
A map $M_{ij}$ sends coordinates in fiber $i$ to matched coordinates in fiber
$j$, and $M_{ji}=M_{ij}^{-1}$.

## Proof strategy and dependency map

1. The matching definitions prove degree, simplicity and the order-five
   symmetry directly.
2. Enumerating the possible middle fiber gives exact cross-fiber coverage.
3. This symmetry reduces the search objective to three fiber-pair types.
4. Independent BFS checks the expanded saved edge lists.
5. The additional reflection/translation rule reduces the three coverage
   relations to three six-element multisets over $\mathbb F_5$; their
   incompatibility proves a strict small-subfamily obstruction.

## 1. Consistent generation rule

Choose arbitrary $A,B,C\in S_{10}$ and set

$$M_{\infty,i}=AR^{-i},\qquad M_{i,i+1}=B,\qquad M_{i,i+2}=C.$$

Indices on the external fibers are modulo $5$; reverse directions use
inverses. The five unordered pairs $\{i,i+1\}$ and the five unordered pairs
$\{i,i+2\}$ are distinct and exhaust the ten external fiber pairs. In
particular, neither rule assigns both orientations of any pair. The five
remaining pairs involve $\infty$. Thus the rule is consistent.

Every vertex has three neighbors in its own fiber and one in each other
fiber. There are no loops or duplicate edges, so the graph is simple,
$8$-regular, and has $60\cdot8/2=240$ edges.
The map $\sigma$ acts as $R$ on fiber $\infty$ and sends $(i,u)$ to $(i+1,u)$
on the external fibers. The identity
$AR^{-(i+1)}R=AR^{-i}$ verifies the infinity matchings, while the external
rules depend only on the fiber difference. Hence $\sigma$ is an order-five
automorphism. The expander checks $R$ directly; the BFS checker verifies
$\sigma$ directly on the expanded edge set.

## 2. Exact coverage and defect condition

Within a fiber, distance at most two is automatic from the Petersen graph.
For different fibers $i,j$ and source $u$, the reachable targets in at most
two steps are exactly

$$\{M_{ij}u\}\ \cup\ N_P(M_{ij}u)\ \cup\ M_{ij}N_P(u)
\ \cup\ \{M_{kj}M_{ik}u:k\notin\{i,j\}\}.$$

The terms account respectively for a direct edge, a middle vertex in fiber
$j$, a middle vertex in fiber $i$, and the four other middle fibers. There
are eleven path slots for ten targets. Diameter two is equivalent to their
union being all ten targets for every row.

Consequently the two triples must intersect in at most one point; requiring
intersection zero is stronger than necessary. If all ten targets are
covered, exactly one target appears twice and every other target once.

For a matrix statement, use row-source matching matrices $Q_{ij}$, and let
$P$ also denote the Petersen adjacency matrix. The cross-fiber path-count
matrix is

$$K_{ij}=Q_{ij}+PQ_{ij}+Q_{ij}P+
\sum_{k\notin\{i,j\}}Q_{ik}Q_{kj}.$$

Every row and column of $K_{ij}$ sums to $11$. Therefore diameter two is
equivalent to every $K_{ij}-J_{10}$ being a permutation matrix: entrywise
nonnegativity plus integral row and column sums one proves this assertion.
The within-fiber blocks have no defects, since a different fiber cannot
contain a common neighbor of two distinct vertices in the original fiber.

## 3. Three exact coverage relations used by the search

The fifteen unordered fiber pairs have three $\sigma$-orbits, represented by
$(\infty,0),(0,1),(0,2)$. For a representative source $u$, use the direct
matching $A,B,C$, respectively, the corresponding two internal triples,
and these four intermediate-fiber images:

| Representative pair | Four intermediate-fiber images |
|---|---|
| $(\infty,0)$ | $BARu,\ B^{-1}AR^{-1}u,\ CAR^2u,\ C^{-1}AR^{-2}u$ |
| $(0,1)$ | $AR^{-1}A^{-1}u,\ B^{-1}Cu,\ C^{-2}u,\ CB^{-1}u$ |
| $(0,2)$ | $AR^{-2}A^{-1}u,\ B^2u,\ B^{-1}C^{-1}u,\ C^{-1}B^{-1}u$ |

The sum of missing targets in these thirty rows is exactly one fifth of
the full number of uncovered unordered vertex pairs. This is the actual
search objective, rather than a surrogate overlap penalty.

## 4. Bounded experiment and independently checked object

The C++ search makes only transpositions within $A,B,C$. One predeclared
run used seed $20261011$, a $40000$-proposal cooling cycle, and four
transpositions of the best saved parameters between cycles. It used one
thread and $80.004$ search CPU seconds; the wrapper recorded approximately
$80.007$ total child CPU seconds and $8440$ KiB maximum RSS. The CPU hard
limit was $90$ seconds and address-space limit $4$ GiB. The run is not a
complete enumeration. It ended with the following parameters:

```text
A = [5,9,8,7,6,3,2,1,0,4]
B = [7,8,9,5,6,3,4,0,1,2]
C = [6,7,8,9,5,3,4,0,1,2]
```

The initial and best candidates are both expanded and independently checked
by full BFS from all sixty vertices, reading only the edge lists. The
initial candidate has $380$ bad pairs. The best has $240$ pairs at distance
one, $1480$ at distance two, and $50$ at distance three. Its bad pairs occur
only between external fibers whose difference is $\pm2$; each such fiber
pair has ten bad vertex pairs. All $150$ internal-neighbor-triple overlaps
are zero. Thus this particular failure lies in the remaining composite
matching images, not in violation of the local overlap condition.

All bad pairs, their distances, common neighbors and both neighbor lists
are preserved in the verification JSON files. The search score agrees
with the independent BFS counts. No valid degree-eight diameter-two graph
was produced.

Artifacts under `computations/dd82/construction/`:

- `petersen_six_fibers.cpp`, `.bin`, `.log`, `.search.json`, `.resources.json`;
- `petersen_six_fibers_expand.py`, `petersen_six_fibers_check.py`;
- `petersen_six_fibers.initial.params.json`, `.initial.edges`, `.initial.verification.json`;
- `petersen_six_fibers.best.params.json`, `.best.edges`, `.best.verification.json`.

## 5. Sharp obstruction for the additional reflection/translation subfamily

The saved parameters have extra structure. Suppose, more generally, that
$A$ swaps layers and reflects coordinates, while $B,C$ swap layers and
translate coordinates. After rotating the infinity coordinate, write

$$A(0,x)=(1,-x),\qquad A(1,x)=(0,-x+d),$$
$$B(e,x)=(1-e,x+b_e),\qquad C(e,x)=(1-e,x+c_e),$$

where $d,b_0,b_1,c_0,c_1\in\mathbb F_5$. The normalization loses no member
of this stated subfamily: replacing $A$ by $AR^t$ subtracts the same $t$
from its two reflection offsets and merely relabels the infinity fiber.

In each of the three coverage relations, the direct edge and the two
internal triples cover all five targets in the layer opposite to the
source. The remaining same-layer targets are, after translating the
source coordinate, the following sets:

$$S_A=\{0,d,b_1-1,1-b_0,c_1-2,2-c_0\},$$
$$S_B=\{b_0,b_1,1,c_0-b_0,-c_0-c_1,c_1-b_1\},$$
$$S_C=\{c_0,c_1,2,b_0+b_1,-b_0-c_1,-b_1-c_0\}.$$

For the second source layer, the first set is negated and the latter two
sets are unchanged. Hence the exact number of uncovered unordered pairs is

$$50\bigl((5-|S_A|)+(5-|S_B|)+(5-|S_C|)\bigr).$$

We prove that all three sets cannot have size five. This also proves the
uncovered-pair count is at least $50$ throughout this subfamily.

**Step 1: full $B,C$ coverage forces their parameters.** The sum of the six
listed entries of $S_B$, with multiplicity, is $1$. If they cover all five
field elements, the duplicated entry is therefore $1$, since
$\sum_{x\in\mathbb F_5}x=0$. Removing the explicitly listed $1$ leaves

$$(b_0,b_1,c_0-b_0,-c_0-c_1,c_1-b_1)$$

as a permutation of $\mathbb F_5$. The corresponding sum for $S_C$ is $2$,
so removing its listed $2$ leaves

$$(c_0,c_1,b_0+b_1,-b_0-c_1,-b_1-c_0)$$

as a permutation. In particular $b_0\ne b_1$.

These two five-entry permutation conditions are preserved by

$$(b_0,b_1,c_0,c_1)\longmapsto
(\lambda b_0+t,\lambda b_1+t,\lambda c_0+2t,\lambda c_1+2t),$$

for $\lambda\ne0$: the first tuple is scaled by $\lambda$ and translated
by $t$, and the second by $2t$. Normalize $b_0=0,b_1=1$.
The first permutation condition permits exactly

$$(c_0,c_1)\in\{(2,4),(2,0),(3,3),(3,0),(4,3),(4,4)\}.$$

This is obtained by assigning the last three entries to $2,3,4$. Substitution
in the second condition leaves only $(4,3)$. Undoing the normalization gives

$$c_0=3b_0-b_1,\qquad c_1=-b_0+3b_1.$$

**Step 2: the infinity matching cannot then cover its same-layer targets.**
Put $x=b_1-1$ and $y=1-b_0$. Then $x+y=b_1-b_0\ne0$, and the five fixed
entries of $S_A$, excluding $d$, are

$$T=\{0,x,y,3x+y,x+3y\}.$$

Scaling by $(x+y)^{-1}$ reduces to $y=1-x$. For $x=0,1,2,3,4$, the resulting
sets are respectively

$$\{0,1,3\},\quad\{0,1,3\},\quad\{0,2,4\},\quad
\{0,2,3\},\quad\{0,2,4\}.$$

Thus $|T|=3$ in all cases and adding $d$ gives $|S_A|\le4$. This contradicts
full coverage. Therefore the subfamily has at least $50$ bad pairs. The
saved example has $(d,b_0,b_1,c_0,c_1)=(3,2,3,1,3)$ and exactly $50$ bad
pairs, so the bound is sharp. $\square$

The independent set-based script `petersen_six_fibers_translation.py`
exhausted all $5^5=3125$ parameter choices in $0.083$ CPU seconds and found
minimum $50$, attained $120$ times. Its JSON retains the complete score
histogram and all minimizers. The proof above does not depend on trusting
this finite enumeration.

## 6. Root's structural repair experiment

A separate root experiment retained all six Petersen internal graphs and
the ten saved $A/B$ matchings, while allowing the five former $C$ matchings
to become five independent arbitrary permutations, breaking the external
$C_5$ symmetry in that part. The resulting input had $1500$ variables and
$8150$ clauses; CaDiCaL returned UNSAT in $0.020146$ CPU seconds and the
saved LRAT was independently verified. See
`computations/dd82/construction/petersen_release_five_matchings.py` and
`computations/dd82/construction/petersen_release_five_matchings/result.json`,
with the input, proof and checker log in that directory.

This rules out repairing the saved graph by changing only those five
matchings. It does not rule out changing the fixed $A/B$ matchings, the
full three-permutation family, or the general six-fiber family. This
subtask records the root's result and inspected result metadata; the root
is responsible for the SAT encoding review.

### Wider ten-matching repair: unresolved

Root then retained only the six internal Petersen graphs and the five saved
infinity-to-external matchings, allowing all ten external pair matchings to
vary independently. This has28000 variables and91250 clauses. One30-second
run used29.854 CPU seconds and returned UNKNOWN. The new necessary
overlap≤1 condition from PETERSEN_MATCHING_CONSTRAINT.md was then added
directly as18000 ternary clauses: for a matched u→v, two different Petersen
neighbors of u cannot both map to Petersen neighbors of v. The strengthened
input has109250 clauses and also returned UNKNOWN after29.552 CPU seconds.

Artifacts are petersen_release_ten_matchings/ and
petersen_release_ten_matchings_overlap/ under computations/dd82/construction/.
Both use petersen_release_five_matchings.py with --release ten, the latter
also with --local-overlap-cuts. These are distinct bounded inputs; the second
tests an explicit newly derived necessary cut. Neither partial LRAT is an
UNSAT certificate. No unrestricted matching or graph family was closed by
these two runs. Both processes have exited; do not restart unchanged inputs.

## Corrections, boundaries and open risks

- The necessary triple-overlap bound is at most one, not necessarily zero.
- The $50$-pair optimum is proved only for the additional
  reflection/translation subfamily; the randomized search provides no
  global minimum claim for arbitrary $A,B,C$.
- The fixed-$A/B$ repair result is confined to its saved edge choices.
- A new attempt must change a concrete retained restriction. Merely
  repeating this stochastic run with another seed has no demonstrated
  rationale from the present evidence.
- No arbitrary order-$60$ exclusion and no new lower bound follows.

## External construction discussion C3

Gemini read the reflection/translation proof in Section 5 and found no gap, using the existing Antigravity thread and requested/CLI-selected gemini-3.8-flash-high/high. Raw response: `reviews/dd82/20261011_C3_petersen_hs59.json`. Root independently read the argument and retained exact result scopes. This discussion is provisional corroboration, not a Lean proof or backend model attestation.
C3 wording limits are recorded in `reviews/dd82/20261011_C3_root_notes.md`; route caps are necessary only and equal energy at two candidates is not a conservation law.

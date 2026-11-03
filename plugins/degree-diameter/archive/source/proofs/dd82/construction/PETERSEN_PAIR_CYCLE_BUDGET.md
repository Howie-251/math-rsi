# Pairwise cycle budgets and the double-HS energy plateau

Date: 2026-10-12. The new results here are a fifteen-block refinement of
the existing cycle energy, a small joint compatibility domain using
three-fiber data, and a quantitative energy bound for the actual double-HS
seed mechanism. No matching enumeration, graph optimization, SAT call,
or BFS was run. The impossibility of retaining an induced HS50 was
already established in
[HOFFMAN_SINGLETON_AUGMENTATION.md](HOFFMAN_SINGLETON_AUGMENTATION.md);
the double-HS calculation below is not presented as a new exclusion range.

## Notation for the complete six-Petersen model

Let $G$ consist of six induced Petersen fibers $F_0,\ldots,F_5$, with one
arbitrary perfect matching between each pair. Write $M_{ij}$ for the
oriented matching, so $M_{ji}=M_{ij}^T$. All sixty vertices have degree
eight. Every cross block of

$$B=A^2+A-7I-J$$

has all row and column sums one, even when the graph fails diameter two.
Every within-fiber block is zero. These facts and the total energy
$E=2F+3T-150$ are from
[PETERSEN_CYCLE_ENERGY.md](PETERSEN_CYCLE_ENERGY.md).

For distinct fibers $i,j$, let $q_{ij}$ count preserved Petersen edges
under $M_{ij}$. It is exactly the number of four-cycles using just these
two fibers. On a target its preserved-edge graph must be a matching,
so $0\le q_{ij}\le5$, as proved in
[PETERSEN_MATCHING_CONSTRAINT.md](PETERSEN_MATCHING_CONSTRAINT.md).

For each unordered triple $\{i,j,k\}$ define:

* $t_{ijk}$: triangles using those three fibers;
* $a^i_{ijk}$: four-cycles using exactly those fibers, whose unique
  within-fiber edge lies in $F_i$; define $a^j,a^k$ similarly.

A triangle cannot have two vertices in one fiber: an external vertex has
only one neighbor in that fiber. A three-fiber four-cycle likewise has
its two same-fiber vertices consecutive, since an external common
neighbor of two vertices in one fiber is impossible. Thus these definitions
cover all three-fiber short cycles without ambiguity.

Finally, for two disjoint unordered fiber pairs $ij$ and $kl$, let
$c_{ij\mid kl}$ count four-cycles with opposite vertices in fibers $i,j$
and with the other opposite vertices in fibers $k,l$. There are 45 such
types. Put

$$c_{ij}=\sum_{\{k,l\}\subseteq\{0,\ldots,5\}\setminus\{i,j\}}
c_{ij\mid kl}.$$

All these counts are directly available from short matching products.
For an orientation $i\to j\to k\to i$, let $h_i$ be its permutation of
the ten coordinates of fiber $i$. Then

$$t_{ijk}=|\{u:h_i(u)=u\}|,\qquad
a^i_{ijk}=|\{u:u\sim_{P_i}h_i(u)\}|.$$

The analogous cyclic products at $j,k$ give their respective $a$ counts.
Choosing one orientation counts each cycle once. Also

$$c_{ij\mid kl}=\operatorname{fix}(M_{ik}M_{kj}M_{jl}M_{li}),$$

with products interpreted in the source-row convention. Reversing or
cyclically rotating the route leaves the fixed-point count unchanged.

## Fifteen exact energy identities

For a vertex pair $u\in F_i,v\in F_j$, write
$c_{uv}=|N(u)\cap N(v)|$ and $b_{uv}=c_{uv}+A_{uv}-1$. Define the block
energy

$$E_{ij}=\sum_{u\in F_i,v\in F_j}\frac{b_{uv}(b_{uv}-1)}2.$$

Each summand is nonnegative. It is one for a bad pair ($b=-1$), zero for
one or two route slots ($b=0,1$), and $\binom b2$ for an overcrowded pair
($b\ge2$). Hence $E_{ij}=0$ precisely when the entire block is covered
and has no route count above two. The fixed block margins make this
equivalent to that block being a permutation defect matrix.

The total route count in the block is 110. Expanding the summands gives

$$E_{ij}=\sum_{u\in F_i,v\in F_j}
 \left[\binom{c_{uv}}2+A_{uv}c_{uv}\right]-10.$$

The term $A_{uv}c_{uv}$ counts triangles on an interface edge. The other
term counts four-cycles with $u,v$ opposite. A two-fiber four-cycle
contributes two such pairs; a three-fiber four-cycle contributes one
exactly when its doubled fiber is $i$ or $j$. Therefore

$$\boxed{
E_{ij}=2q_{ij}
 +\sum_{k\ne i,j}\bigl(t_{ijk}+a^i_{ijk}+a^j_{ijk}\bigr)
 +c_{ij}-10\ge0.}\tag{1}$$

This identity holds for every construction candidate. Summing over the
fifteen blocks recovers $E=2F+3T-150$.

Define the quantity determined only by single matching and triple data

$$r_{ij}=10-2q_{ij}
 -\sum_{k\ne i,j}\bigl(t_{ijk}+a^i_{ijk}+a^j_{ijk}\bigr).\tag{2}$$

Then always $c_{ij}-r_{ij}=E_{ij}$. In particular a diameter-two target
must satisfy **all fifteen** exact equations

$$\boxed{c_{ij}=r_{ij}\ge0.}\tag{3}$$

For an approximate graph, (3) is not asserted: the difference is exactly
its bad-pair and overcrowding penalty in that block.

## A new joint domain available before four-fiber assembly

Treat the fifteen fiber pairs as the vertices of $KG(6,2)$, where two
pairs are adjacent precisely when they are disjoint. The 45 nonnegative
integers $c_{ij\mid kl}$ are weights on its edges. Equation (3) says that
the degree vector of this integer-weighted graph must be $(r_{ij})$.
This is a compact candidate-preserving compatibility condition linking
all fifteen matching interfaces through their twenty triple products.

Some immediate necessary tests are:

$$r_{ij}\ge0,\qquad \sum_{i<j}r_{ij}\text{ is even},$$
$$r_{ij}\le\sum_{kl:\{k,l\}\cap\{i,j\}=\varnothing}r_{kl},$$
$$\sum_{j\ne i}r_{ij}\le\frac12\sum_{a<b}r_{ab},\qquad
r_{ij}+r_{ik}+r_{jk}\le\frac12\sum_{a<b}r_{ab}.$$

The last two inequalities use independent sets of the Kneser graph:
all pairs incident to one fiber, or the three pairs of a fiber triangle.
Each weighted edge can meet such an independent set at most once. These
tests are necessary; their success alone is not claimed to prove integer
feasibility, much less realizability by matching products.

## One actual saved-seed diagnostic

The [diagnostic source](../../../computations/dd82/construction/petersen_pair_cycle_budget.py)
reads only
[the saved twenty-bad-pair graph](../../../computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges).
It reconstructs all fifteen matchings, counts the triple and four-fiber
cycles by their actual products, and verifies the cycle totals using
direct common-neighbor counts. It evaluates every block energy separately
and records every bad and crowded pair. It does not run BFS or change
any edge. CPU time was **0.003547598 seconds**.

The [complete result](../../../computations/dd82/construction/petersen_pair_cycle_budget.json)
gives

$$T=0,\qquad F_2=0,\qquad F_3=16,\qquad F_4=84,\qquad E=50.$$

The sixteen three-fiber four-cycles are four on each triple $\{a,4,5\}$
for $a\in\{0,1,2,3\}$, with the unique internal edge in fiber $a$.
The pair budgets are:

| Fiber pairs | Number of pairs | $r_{ij}$ required | Actual $c_{ij}$ | $E_{ij}$ |
| --- | ---: | ---: | ---: | ---: |
| $ij\subseteq\{0,1,2,3\}$ | 6 | 10 | 10 | 0 |
| $a4$ or $a5$, $a\in\{0,1,2,3\}$ | 8 | 6 | 6 | 0 |
| $45$ | 1 | 10 | 60 | 50 |

Thus no nonnegativity or simple Kneser inequality fails. The failed exact
condition is uniquely $c_{45}=r_{45}$: its actual value is sixty instead
of ten. The six terms $c_{ab\mid45}$ for $ab\subseteq\{0,1,2,3\}$ are
each ten. Block 45 has 20 pairs with zero route slots, 70 with one, and
10 with four. These yield twenty bad pairs plus thirty units of crowding.
All individual vertex pairs and their common neighbors are retained in
the result; no nonzero energy is treated as a successful construction.

In fact this particular $r$ vector is feasible as an abstract Kneser
degree vector, so its obstacle is the actual matching compositions.
Here is an explicit integer weighting, using $ab$ for an old fiber pair:

* give each of $01\mid23$, $02\mid13$, $03\mid12$ weight 8;
* give $ab\mid45$ weight 2 for every old pair except $01,23$, which
  each receive weight 1;
* give $01\mid24$ and $23\mid05$ weight 1;
* give $a4\mid b5$, for distinct $a,b\in\{0,1,2,3\}$, weight 2,
  except $24\mid05$, which receives weight 1;
* give all other edges weight zero.

Each old-pair vertex has weighted degree ten, each $a4/a5$ vertex degree
six, and vertex 45 degree ten. The total weight is $24+10+2+23=59$.
This is only an abstract count witness, not a set of actual interfaces.

## Quantitative explanation of the double-HS plateau

Suppose, more generally, that deleting fiber 4 or deleting fiber 5 from
a six-Petersen candidate both yield Hoffman--Singleton graphs. The
matching between fibers 4 and 5 is arbitrary. Every pair except those
between fibers 4 and 5 lies in at least one induced HS50. Within that HS
there is exactly one direct or two-step route, since it has diameter two
and girth five. Reintroducing the omitted fiber adds at most one route,
because each endpoint has only one neighbor in that fiber. Thus

$$E_{ij}=0\qquad\text{for }ij\ne45.\tag{4}$$

For two of the four shared fibers $a,b\in\{0,1,2,3\}$, the induced
forty-vertex core provides exactly nine route slots from a source to the
ten targets: one direct, six using internal Petersen edges, and two
through the other core fibers. These nine slots are distinct, as they
belong to an HS50 of girth five. Each source therefore misses exactly
one target in fiber $b$ inside the core. That missing pair has a unique
common neighbor in fiber 4 and a unique common neighbor in fiber 5,
by the two HS completions. It gives exactly one four-cycle with opposite
fiber pairs $ab$ and 45. Conversely every such four-cycle arises this way.
Hence

$$c_{ab\mid45}=10\quad\text{for all six old pairs }ab,
\qquad c_{45}=60.\tag{5}$$

This count is independent of the matching $M_{45}$. Combining (1), (4)
and (5), and writing
$t_{45}=\sum_{k=0}^3t_{45k}$ and
$a_{45}=\sum_{k=0}^3(a^4_{45k}+a^5_{45k})$, gives

$$\boxed{E=E_{45}=50+2q_{45}+t_{45}+a_{45}\ge50.}\tag{6}$$

The saved twenty-bad-pair seed attains this bound: all three extra terms
vanish. It is therefore already an energy minimizer within the entire
double-HS mechanism, not merely with one interface fixed.

The older induced-HS augmentation theorem already excludes such a target
graph, so (6) does not enlarge the excluded range. Its construction value
is quantitative: it explains the observed $E=50$ plateau. Changing the
4--5 matching alone, or changing any interfaces while preserving both
induced HS50 subgraphs, cannot lower the energy below fifty. A successful
future construction must break those preserved structures; that necessity
is already implied more broadly by the older induced-HS theorem.

The new pairwise and Kneser constraints remain applicable to arbitrary
fifteen-matching data outside this special seed mechanism. No broader
search or follow-up optimization was launched here.

Root and C16 checked the complete derivation, diagnostic source and
actual results. C16 accepted the stated identities and quantitative
bound. See reviews/dd82/20261012_C16_* for raw response and exact scope.

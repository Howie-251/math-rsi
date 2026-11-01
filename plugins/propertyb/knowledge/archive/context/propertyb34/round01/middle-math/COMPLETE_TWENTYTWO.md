# Complete 22-vertex candidate for T34

## Claim and status

Every simple five-uniform hypergraph $H$ on $22$ vertices, with exactly $34$
edges and covering every vertex pair, has Property B.

**PROVABLE AS STATED**, as a complete paper candidate using finite exact local
certificates. The original unrestricted T34 is unchanged; Lean implementation
of this branch and cross-family review of its new low-degree parts remain.

## Notation and dependency map

Write $r$ for the number of degree-six vertices and $t$ for the number of
degree-seven vertices. Pair coverage gives $d(x)\ge6$, and

$$\sum_xd(x)=170,\qquad
\sum_{y\ne x}(\lambda(x,y)-1)=4d(x)-21,\qquad 2r+t\ge6.$$

Thus six-, seven- and eight-degree points have codegree excess $3,7,11$.
The last inequality follows from $170\ge6r+7t+8(22-r-t)$.
All uses of a unit pair mean actual codegree one.

The proof splits into $r=0$, $r\ge3$, $r=2$, and $r=1$. The first two are
already proved in `CANDIDATE_TWENTYTWO_SEVEN.md` and
`CANDIDATE_LOW_BRANCHES.md`. This note proves the remaining two cases.
The locked-permutation probability bounds, exact bad-pair quotas and the
mixed-layout weak-dual inequality are the shared dependencies.

## 1. Local inventories and how their finite checks cover actual inputs

For four locks of specified degrees, exact triples and the exact quadruple
are nonnegative integers bounded by the actual pair codegrees. Exact pair,
singleton and empty counts are recovered by subtracting their larger traces,
then enforcing the specified degrees and $34$ total edges. The codegree-excess
identity bounds every internal pair budget. Every actual input satisfies these
identities and occurs in this domain. Canonicalization uses all permutations
preserving the degree roles; it is an explicit relabeling, not a test of
realizability of a whole hypergraph.

Seven-seven codegrees at least four already have strict two-lock bounds from
the frozen first-hour thresholds. Consequently a hypothetical counterexample
has all seven-seven codegrees at most three. A six-point codegree is at most
four by its excess three. These are the only additional upper bounds used in
the initial four-lock domains.

Adding a new lock promotes $p_T$ actual edges from each old positive trace $T$
of size at most four, where $0\le p_T\le n_T$. The new singleton count is
$d_{\rm new}-\sum_Tp_T$ and is subtracted from the old empty count. Its
codegrees are $\sum_{T\ni i}p_T$. The old and new excess budgets, any proved
unit conditions, nonnegativity and degree bounds are enforced. This enumerates
every actual extension because those are its literal edge counts.
Projection onto a smaller lock set sums exact multiplicities. A projected
strict profile already supplies a coloring, so only residual projections need
to be retained in a counterexample.

Every retained strict certificate below was independently checked by labelled
injections for A/B/C. Shared-layout certificates additionally had all rational
weights, actual profile counts, both directed slot weights, quota multipliers
and capacity penalties replayed by `verify_joint_layout.verify` with the
actual vertex count and degree tuple. Floating-point LP output is a proposal;
the accepted inequality is an exact rational inequality.

## 2. Exactly two six-degree points

Let the lows be $a,b$. Here $t\ge2$. The complete four-lock domain on
$(a,b,y,z)$ with two seven-degree vertices has $1302$ colored orbits.
All but nine are strict; see `MIXED_QUAD_FULL_22_2.json`.

### 2a. At least four seven-degree vertices

Adding a third seven to those residuals and requiring every two-seven
projection to remain residual leaves $24$ five-lock orbits. Twenty-two are
strict. Both residuals have all pair codegrees one, no common edge containing
a low and two sevens, and either one exact three-seven trace or only pair
traces among the sevens.

These restrictions hold for every three selected sevens. Add a fourth seven.
All its selected codegrees are therefore one, and every three-seven projection
is one of the two residues. Complete promotion leaves three six-lock profiles,
all strict, with maximum $129/130$. This handles $t\ge4$.

### 2b. Exactly three seven-degree vertices

The remaining seventeen vertices have degrees at least eight and sum to
$170-2\cdot6-3\cdot7=137$. Hence exactly sixteen are degree eight and one is
degree nine. At most six of those sixteen eights can be nonunit with either
low. Choose an eight-degree point unit with both lows; at least ten exist.

Its codegrees with the three sevens are not assumed unit. Promoting it into
each of the two five-lock residues above, using only its actual degree and
the two chosen unit incidences, gives $765$ colored six-lock profiles. Every
one is strict. This proves the $t=3$ case.

### 2c. Exactly two seven-degree vertices

All other eighteen vertices have degree eight because their degree sum is
$170-12-14=144$. At least twelve eights are unit with both lows; denote all
such eights by $U$.

Adding any $u\in U$ to the four-lock residual domain gives $1267$ colored
five-lock profiles. All but one are strict. The unique residue has

$$\lambda(a,b)=2,\qquad \lambda(y,z)=2,$$

and every other selected pair unit, with all selected traces of size at least
three absent. Therefore, in a counterexample, each point of $U$ is unit with
both sevens. The low-low codegree two consumes one excess unit at each low;
each has at most two nonunit eight-degree neighbors. Hence $|U|\ge14$.

Fix $u\in U$. It has total excess eleven, so among the at least thirteen other
members of $U$ there is $w$ with $\lambda(u,w)=1$. Both $u,w$ are also unit with
the lows and the two sevens. Adding this actual $w$ to the unique five-lock
residue leaves twelve six-lock colored profiles, all strict. This completes
$r=2$.

The finite evidence for Sections 2a–2c is:

| File | Domain / strict conclusion |
|---|---|
| `EXTEND_MIXED22_2_7.json` | 24 profiles, two residuals |
| `SECOND_MIXED22_2_7_7.json` | three profiles, all strict |
| `SECOND_MIXED22_2_7_8.json` | 765 profiles, all strict |
| `EXTEND_MIXED22_2_8.json` | 1267 profiles, one residual |
| `SECOND_MIXED22_2_8_8.json` | twelve profiles, all strict |

## 3. Exactly one six-degree point

Let $x$ be the low. Now $t\ge4$. The domain on $x$ and three sevens has
$1260$ colored orbits; all but ten are strict. Adding a fourth seven and
requiring every three-seven projection to remain residual leaves eight
five-lock profiles, of which six are strict.

Both residuals have all selected pairs unit and no edge containing $x$ and
two selected sevens. Their high traces consist either entirely of pairs, or
of one exact four-seven trace. If there were a fifth seven, every four-seven
projection would have to be one of these two profiles. Thus all new selected
pairs are unit. The complete extension/filter leaves two six-lock profiles,
both strict, with bounds $3805/4004$ and $35463/40040$.

It remains that $t=4$. The other seventeen vertices all have degree eight,
since their degree sum is $170-6-4\cdot7=136$. At most three are nonunit with
$x$, so select an eight-degree $u$ unit with $x$. No unit assumption is imposed
between $u$ and the sevens. Complete promotion into the two five-lock residues
gives $18814$ labelled extensions and $1060$ colored orbits. Every one has a
strict exact certificate. This proves the unique-low case.

Evidence: `MIXED_QUAD_FULL_22_1.json`, `EXTEND_MIXED22_1_7.json`,
`SECOND_MIXED22_1_7_7.json`, and `SECOND_MIXED22_1_7_8.json`.

## 4. Conclusion and remaining formal work

Pair coverage guarantees minimum degree at least six. The four disjoint cases
$r=0$, $r=1$, $r=2$, and $r\ge3$ have all been covered. In each case a concrete
layout has conditional failure probability below one, or an impossible
simultaneous residual configuration has been derived. Therefore an actual
proper two-coloring exists.

Lean must still connect these degree identities, actual selections, exact
trace inventories, complete promotion/projection coverage and mixed-layout
inequalities to the original coloring conclusion. The tables enumerate local
lock traces only, not all 22-vertex hypergraphs. Cross-model approval and
independent arithmetic are recorded separately from that formal obligation.

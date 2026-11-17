# Four same-parity holes in Q5: avoiding any prescribed two

Date: 2026-11-01. ARIS proof-writer draft. Proposed complete proof relative
to the specified Q4 certificates and preceding gluing lemmas. Independent
proof-checker audit pending; full P6 and full Q5 T15 remain open.

## Claim T44_5

For every matching F of K(Q5) with exactly four uncovered vertices, all
of one parity, and every specified pair of distinct holes x,y, there is
a cycle through exactly Q5 minus {x,y}, containing F and having every
edge outside F short. Thus the cycle has 30 vertices. Original required
edges are arbitrary, including long and same-parity edges.

## Inputs and dependency map

1. Q4 N14 (two same-parity holes, omit one) and T44_4 (four same-parity
   holes, omit two), certified in Q4_CORE_AND_A4_SPLIT.md and
   Q4_TWO_AVOIDED_TRANSFER.md with their independent reviews.
2. Q4_RICH_GLUING.md, reviewed PASS in Q4_RICH_GLUING_REVIEW.md/.json:
   two avoided Q4 cycles with opposite LOCAL forbidden parities have
   intersecting optional-new-edge unions in the stated two-hole cases.
3. T44_SAMEFACE_ZERO_CROSSING.md: all four holes in one face and no
   crossings are handled by two local paths and two short bridges.
   It uses the complete Q4 perfect-endpoint classification and the
   311850 four-hole path certificates. Its separate audit is required.
4. Complete Q4 opposite-parity two-avoided circle tables, already audited
   in CANONICAL_COMPLETION_REVIEW.md. There are 51 negative matchings
   for holes 0,1 and 53 for holes 0,7; all positives have explicit circles
   and all negatives have exhaustive complementary-short-matching checks.
5. The finite completion/root accounting of Section 5 below, independently
   checkable from those complete tables. No Q5 T15 or Q6 theorem is used.

## 1. Reduction to two geometries

Translate the first forbidden hole to 0. The second forbidden hole is
even, so by coordinate permutations it is 3 or 15. Let s,t be the two
other holes. A coordinate splitting both the forbidden pair and {s,t}
puts two same-parity holes in each face. Such a coordinate exists exactly
when supp(x xor y) intersects supp(s xor t).

In that case the claim follows for positive crossing count by pairing
the first-face ports, using N14 there, deleting the artificial pairs,
attaching crossings, compressing on the second face, using N14 there,
and expanding. The crossing count is even because each face has two
original holes. At zero crossings, Q4_RICH_GLUING supplies common
optional edges; deleting them and adding the two corresponding short
crossings joins the two 15-cycles into the desired 30-cycle.

If the forbidden distance is four, the support of s xor t is nonempty
and has even size, hence cannot be confined to the sole coordinate
outside the forbidden difference. Thus this split always exists.

For forbidden holes 0,3 and no such split, s and t agree in coordinates
0 and 1 and differ in two of the other three. The subgroup preserving
the unordered pair {0,3} consists of translations by 0 or 3, permutations
of coordinates 0,1, and permutations of coordinates 2,3,4. Its 18 eligible
unordered pairs {s,t} fall into three orbits of size six, represented by

    {12,20}, {5,9}, {5,29}.

This finite geometric claim can also be checked by enumerating all 91
pairs of remaining even vertices, as in t15_analytic_geometry.py/.json.
For {5,9}, all four holes lie in one coordinate face. More generally any
such same-face geometry is handled as follows. At positive crossings,
pair ports in the hole face, use Q4 T44_4, delete the nonempty artificial
matching, transfer and compress onto the other face, and use Fink's
perfect-matching circle extension there. At zero crossings use input 3.

Only the representatives {0,3,12,20} and {0,3,5,29}, forbidden {0,3},
remain. Section 2 puts both into a common canonical cut description.

## 2. The canonical one-hole/three-hole cut

In the first representative split coordinate 0 and let A be the odd
face. It has the sole hole 3, which is forbidden. Drop coordinate 0 and
translate both faces by local vector 1. In their common Q4 labels A has
sole forbidden hole 0; B has holes {1,7,11}, with 1 forbidden.

In the second representative split coordinate 0 and let A be the even
face, whose sole forbidden hole is 0. Dropping that coordinate without
translation gives B holes {1,2,14}, with 1 forbidden.

Thus it suffices to handle either target pair (f,g)=(7,11) or (2,14),
with A's sole original hole 0, B's original holes {1,f,g}, and 0_A,1_B
the prescribed forbidden vertices. The B holes are all odd in the shared
local labeling. The A forbidden hole is even locally; their global
parities agree as required. New bridges join equal local labels.

Write C for original crossing edges, X_A,X_B for their endpoint sets,
and c=|C|. Then c is odd and positive: the original matching covers 15
vertices in A. Also c<=13 because B has three holes. Required crossing
edges may connect arbitrary labels; their actual partners are retained.

## 3. Local path availability from the complete tables

Choose d in X_A and a perfect matching D on X_A minus {d}. Put
L=F_A union D, whose holes are 0,d. For any odd z different from d, z is
covered by L; write k=L(z) and set

    T_z = L - {zk} + {dk}.

Its holes are 0,z. A 14-cycle on Q4 minus {0,z}, containing T_z and
using short new edges, yields a 15-vertex d--z path on A minus 0:
delete dk to open the cycle between d,k and append the original edge kz.
Conversely any such path ends at z via zk, since zk is its required
matching edge; removing z and adding dk gives the 14-cycle. The new edge
dk is artificial and is removed in the forward construction.

Consequently the audited Q4 tables decide exactly which (d,D,z) work.
For z=d the path with equal endpoints is disallowed. If z is one of
f,g and some choice works, the safe free-hole transfer in Section 4
already proves the canonical claim. Otherwise use the full availability
classification in Section 5.

## 4. Safe and occupied endpoint transfers

Suppose a path P as above has been chosen with odd endpoint z != 1.
Delete D and attach all original crossing edges. Also attach the new
short bridge from z_A to z_B. All A vertices except 0 have degree two:
at d the crossing edge supplies the missing endpoint degree; at z the
bridge supplies it. If z is itself a port, deleting D removes its sole
path edge, so z is temporarily isolated; its original crossing plus
the bridge restore degree two. This boundary is included, not excluded.

### Safe endpoint z outside X_B

The attached B vertices are distinct. The graph is a path forest with
endpoints X_B union {z_B}, and its interiors partition A minus 0.
Compress it to a matching R on that endpoint set.

If z is f or g, F_B union R is a matching with precisely two same-parity
holes, including 1. Q4 N14 omits 1 and gives a 15-cycle; expanding R
produces the required 30-cycle.

If z is not f or g, it is internally covered by F_B, since z != 1 and
z is not a port. Write k=F_B(z), q=R(z). Suppress the two-edge path
k--z--q by replacing zk,zq with kq. The resulting matching has holes
{1,f,g,z}, four odd vertices. Q4 T44_4 avoids 1,z. Expanding kq restores
z and its original matching edge together with the transfer path;
expanding all remaining R edges restores A minus 0. The result has
14+1+15=30 vertices and omits exactly 0_A,1_B.

### Occupied endpoint z in X_B

Assume c>=3 and choose the root d to be the original A partner of z_B.
Availability in Section 3 ensures d != z. The matching D is nonempty.
Every edge of D occurs on P, so deleting D separates P's endpoints d,z
into different components, even when z is a port and becomes isolated.
After all original crossings have been attached, these components remain
different: each attachment adds a distinct B endpoint. Adding bridge
z_A z_B joins the z component to the endpoint z_B already attached at d.
It creates no cycle. If z is an A port, its separate original crossing
attaches at another B port because the crossing partners of d and z are
distinct. Thus the temporarily isolated case also gives a path, not a
closed component.

All resulting components are paths with endpoints X_B minus {z_B},
and their interiors partition (A minus 0) union {z_B}. Compress to R.
Now F_B union R has exactly the four odd holes {1,f,g,z}; apply Q4 T44_4
avoiding 1,z and expand. Again this gives the required 30-cycle.

Only c=1 is excluded from occupied transfer: D would be empty and the
two attachments would close a separate A-side cycle. Section 5 always
provides a safe endpoint when c=1.

## 5. Complete finite coverage of choices of roots and pairings

For each odd z, inverse-enumerate the bad near-perfect states (d,L) from
the audited negative tables. Given a negative T with holes 0,z and any
oriented edge dk of T, the inverse state is

    L = T - {dk} + {zk}, with root d.

Every failed state with z != d is included, by the forward equivalence
in Section 3. Add the special failure z=d when testing availability.
To fail both fixed targets f,g, at least one of them is different from
d; therefore the union of these two inverse lists contains every possible
double-failure state. Intersecting the two failure conditions gives 256
states for (7,11) and 187 for (2,14).

For a fixed odd crossing count c, an internal partial matching F_A has
(15-c)/2 edges. Its completions are the c choices of d and the
(c-2)!! pairings D of the other ports, totaling c(c-2)!! distinct states.
The convention (-1)!!=1 applies for c=1. Each completion (d,L) contains
F_A. Enumerate every submatching of the double-failure states of the
required size and count its occurrences. It is a stalled partial
matching exactly when the count is c(c-2)!!; any partial not enumerated
or with a smaller count has a successful fixed-target completion.

The complete stalled partial counts are:

| c | 1 | 3 | 5 | 7 | 9 | 11 | 13 |
|---|---:|---:|---:|---:|---:|---:|---:|
| f,g=7,11 |256|210|42|2|0|0|0|
| f,g=2,14 |187|110|21|1|0|0|0|

For each stalled F_A and each odd z, count failed completions separately
for each root d. At a fixed d there are (c-2)!! completions; d is a good
root for z exactly when z != d and fewer than all those completions are
in the inverse negative list. This respects the necessary quantifier:
for a good root one may then select an appropriate D.

Let G be all odd z != 1 with at least one good root. If |G|>c, some
z in G is outside X_B, and the safe transfer works. This holds for all
stalled inputs with c=1.

For the remaining inputs, c>=3. If any z in G lies outside X_B we again
use the safe transfer. Otherwise G is a subset of X_B. The original
crossing partners define an injective map phi:G -> X_A. If phi(z) is a
good root for any z, the occupied transfer applies. Failure would require
an injection assigning EVERY z in G to one of its bad roots.

`t44_canonical_completion_probe.py` exhaustively tests this finite
injection condition for every stalled partial in the table. In every
case either |G|>c or no such bad-root injection exists. The unresolved
count is zero at every c for both target pairs. It stores all partials,
all good-root sets, exact failed-completion counts, and the injection
test outcome in `t44_canonical_completion_probe.json`.

This checks all possible crossing endpoint sets and all partner bijections
without enumerating them: if G is not contained in X_B a safe endpoint
exists, and if it is contained there its actual partner map is one of the
injections ruled out above. No assumption of short original crossing
edges is used. No random matching test supplies a universal step.

## Conclusion and scope

The split lemma, same-face lemma and the two canonical completion
arguments exhaust the normalized four-hole geometries, proving T44_5
relative to the stated finite certificates and gluing inputs, subject to
their independent audits. In particular the canonical occupied transfer
allows an endpoint that is itself an A port, a boundary not needed in
the earlier, more restrictive A4 canonical proof.

T44_5 gives the adjacent-hole reduction for Q5 T15: if its minority hole
is short-adjacent to a nonforbidden majority hole, add that short edge
and apply T44_5 to the remaining four majority holes, avoiding the
prescribed two. It does not prove the nonadjacent T15 core or EP0, and
does not close full eight-hole P6 or the higher 10--18-hole layers.

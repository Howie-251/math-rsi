# Polarity73 deletion and monotone completion: derivation and first screen

## Target and status

**COHERENT AS STATED as a restricted construction domain; writer-checked
mathematical deductions, not an externally reviewed theorem or target graph.**
Start with the orthogonal polarity graph H on PG(2,8), delete 12–15 vertices,
and add edges between surviving vertices to obtain an actual degree-eight,
diameter-two graph. No surviving H edge may be removed in this domain.
All deletion sets are variable; no particular seed, hub, retained HS50,
old bad-pair boundary, or edit radius is selected.

The derivation rules out **every monotone completion at orders60/61**, and
every deletion containing the whole absolute line at orders58–61. At58/59
at least eight nonabsolute, nonnucleus points must be deleted. The remaining
domain is not shown feasible or impossible. These exclusions do not apply
to arbitrary rewiring after deletion, or to arbitrary graphs of these orders.

This is a bounded formula-derivation assessment, not completion of the full
idea-discovery/review workflow. A small ambient generator was specifically
authorized and executed, followed by one bounded perfect-code enumeration
for the fixed two-fiber58 sample. No deletion-set search, SAT input or solver
was run.

## Local context actually examined

The search of `proofs/dd82`, `context/dd82`, `research-wiki` and construction
sources found no previous PG(2,8)/73-point deletion implementation or claim.
This is a statement about the inspected project records, not literature
novelty. The relevant sources read were:

- [BROWN57_PROOF.md](BROWN57_PROOF.md), its explicit F7 orthogonality model,
  and the locally saved Brown-construction discussion in
  `large_graphs_diameter_two.txt`.
- [BROWN_EXTENSION_OBSTRUCTION.md](BROWN_EXTENSION_OBSTRUCTION.md): adding a
  new point to the 57-point graph requires changing old edges; that proof
  concerns a different order, field and operation.
- [HOFFMAN_SINGLETON_AUGMENTATION.md](HOFFMAN_SINGLETON_AUGMENTATION.md):
  retaining an induced HS50 is impossible; its deletion/attachment repairs
  and small auxiliary cores are historical scoped domains.
- [JOINT_BOUNDARY_COMPLETION_DIRECTION.md](JOINT_BOUNDARY_COMPLETION_DIRECTION.md),
  `context/dd82/CONSTRUCTION_PROGRESS_20261013.md`, `context/dd82/NEXT_SESSION.md`,
  and `research-wiki/ideas/dd82-brown57-extension.md`: the recent full58/full60
  work retained an outside induced subgraph of existing failed targets.

The present difference is a new degree-nine ambient geometry with variable
vertex deletion and exact degree deficits. It still imposes the substantial
restriction that every surviving ambient edge is kept. Describing this as
unrestricted graph reconstruction would be incorrect.

## Invariant object, assumptions and notation

Use K=F2[t]/(t³+t+1). Represent the projective points by
`(1,a,b)` for a,b in K, `(0,1,a)` for a in K, and `(0,0,1)`.
Distinct points x,y are adjacent exactly when their ordinary three-coordinate
dot product is zero. There are73 points. Nondegeneracy of this bilinear form
gives a unique projective common solution of x·z=y·z=0 for distinct x,y.
Thus any two vertices have at most one common graph neighbor, and every
nonadjacent pair has exactly one. H has diameter two and no four-cycle.

In characteristic two, x·x=(x0+x1+x2)². The nine absolute points form
the line L: x0+x1+x2=0. The nucleus nu=(1,1,1) is not absolute and
N_H(nu)=L. Put R=V(H) minus (L union {nu}); |R|=63.
An absolute point has degree8; all other points have degree9.

For l in L, let C_l=N_H(l) minus {nu}. These are nine disjoint
seven-point sets partitioning R. Each external point x has the unique
absolute neighbor l(x). Write J=H[R].

The graph being constructed is always one original simple graph A on the
survivors S=V(H) minus D. All degrees, common neighbors and new edges below
refer to that A, not to an independent quotient or defect matrix.

## Derivation strategy and map

1. Derive the absolute-line/fiber structure and local triangles of H.
2. Use the target's degree and triangle budgets to constrain D.
3. Express the exact deficits and all lost two-step witnesses.
4. Test necessary conditions on the **whole deletion family** before spending
   time on a full original-A completion model. No approximation enters.

## 1. Exact ambient fiber and triangle structure

The restriction of the bilinear form to l-perp has radical span(l).
For distinct nonabsolute points of that projective line, normalize coordinate
sum to1. Their difference is a multiple of l, so their dot product is1.
Consequently C_l is independent. For any x in C_l and any different
absolute point m, x-perp and m-perp meet in a unique point of C_m.
Thus each pair of fibers induces a perfect matching, and J is8-regular.

Two points in the same fiber have only l as a common neighbor in H and
no common neighbor in J. Two points in different fibers have their unique
common neighbor in R: it cannot be nu, and an absolute common neighbor
would make their fibers identical. In particular each J edge is in exactly
one triangle. At every x in R the eight J neighbors induce four disjoint
edges, so x lies in exactly four triangles. Points of L and nu lie in none.

The concrete authorized diagnostic is
`computations/dd82/construction/polarity73_reduction_run/geometry.py`, with
`geometry.edges` and `geometry.json`. The executed exact checks found:
73 vertices,324 edges, degree histogram {8:9,9:64}, maximum common-neighbor
count1,84 triangles, and exactly189 uncovered pairs in J, precisely its
same-fiber pairs. This verifies the finite ambient structure only; H has
maximum degree9 and is not a target construction. No old Brown57 run was
repeated and no order63 nonexistence computation was performed.

## 2. All monotone60/61 completions are excluded

Every target above57 is8-regular: a degree-at-most7 vertex could reach at
most1+7+7·7=57 vertices in two steps. If t_A(x) is its triangle count,
the same radius-two incidence count gives n<=65−2t_A(x). Therefore
t_A(x)<=2 at n=60,61, and t_A(x)<=3 at n=58,59.

Write F=D intersect R, f=|F|, and e_J(F) for its internal edge count.
At60/61 each retained x in R must lose at least two of its four ambient
triangles. Since all surviving old edges remain and every such triangle is
inside R, x needs at least two neighbors in F. Summing gives

    8f − 2e_J(F) >= 2(63−f), hence 10f − 2e_J(F) >= 126.

Thus f>=13. At61 only12 vertices are deleted, a contradiction. At60
exactly13 are deleted, so all are in R. The nucleus and all nine absolute
neighbors then survive, leaving nucleus degree9, which additions cannot
reduce. This is again impossible.

## 3. At58/59, f>=8 and the whole absolute line cannot be deleted

Here each retained external vertex must lose at least one old triangle,
so it needs at least one F neighbor. Put f_l=|F intersect C_l|. Each
member of F outside C_l has exactly one neighbor in C_l, while members
inside have none. To reach its7−f_l retained points requires
f−f_l>=7−f_l, hence f>=7.

Equality f=7 is rigid. In each fiber the available7−f_l incidences must
all hit distinct surviving points. Hence F has no internal edges and
every retained point has exactly one F neighbor. If two F points belonged
to different fibers, their unique common neighbor in R could neither lie
in F (independence) nor survive (it would have two F neighbors). Therefore
F is precisely one complete seven-point fiber.

Then56 external points remain, each with internal degree7. There are only
k=n−56=2 or3 surviving core points from L union {nu}. Consider any
remaining full fiber C_l whose absolute point was deleted. Its seven
vertices have no retained core neighbor and each can receive just one new
edge. Suppose r of them use their new edge toward an external vertex,
and the other7−r use core vertices in groups of sizes s_i.

An external new-neighbor choice can cover at most one same-fiber pair
through a new-old path, because between-fiber old edges form matchings;
the bound r also covers new direct within-fiber edges. Two-new-edge paths
through an external vertex are impossible since each external vertex has
only one additional incidence. A common core covers exactly the pairs
within its attachment group. Thus the21 same-fiber pairs require

    21 <= r + sum_i binom(s_i,2),   sum_i s_i=7−r.

If r>=1, the right side is at most r+binom(7−r,2)<21. If r=0,
equality forces all seven vertices onto the same core point. Distinct
seven-point fibers need distinct core points because target degree is8.

Let a=|D intersect L| and eta=1[nu in D]. Since d=73−n=7+a+eta,
there are at least a−1 deleted-absolute fibers that still contain seven
external points: at least6 when n=58, and at least5 when n=59. This exceeds
k=2 or3. Hence f=7 is also impossible, proving f>=8.

Deleting all nine absolute points leaves f=d−9−eta<=6 at58–61.
It is therefore impossible throughout this monotone domain. The tempting
operation “delete L and the nucleus, then two to five more points” is a
special case of this obstruction, not a construction candidate to run.

## 4. Exact remaining degree deficits and lost coverage

The open cases have n=58 or59, d=15 or14, and

    d=a+eta+f;  f>=8;
    if eta=0 then a>=1 (the retained nucleus must lose a neighbor).

Thus f ranges8..14 at58 and8..13 at59. Let I=D intersect L,
t_F(x)=|N_J(x) intersect F|. For surviving vertices the exact remaining
degrees and required new degrees delta are:

| Surviving vertex | Retained original degree | delta=8−degree |
|---|---:|---:|
| x in C_l minus F | 9−1[l in I]−t_F(x) | t_F(x)+1[l in I]−1 |
| l in L minus I | 8−eta−f_l | eta+f_l |
| nucleus, if retained | 9−a | a−1 |

Every delta must be nonnegative. The necessary triangle screen additionally
requires that F hit at least one of the four disjoint neighbor-pairs forming
old triangles at each retained external x; merely deleting its absolute
neighbor does not destroy a triangle. The formula t_F(x)>=1 is necessary
but the actual four-pair condition is the direct geometric version.

Let e_H(D) be the actual internal deletion-set edge count. Then

    e_H(D)=eta*a + sum_{l in I} f_l + e_J(F),
    new_edges = 5d−32−a−e_H(D),
    sum_{x in S} delta(x) = 2*new_edges.

These follow by subtracting the retained edge count
324−9d+a+e_H(D) from the required4(73−d). They are identities, not
independently chosen budgets.

For every nonadjacent surviving pair x,y let m(x,y) denote its unique H
common neighbor. It loses its old coverage exactly when m(x,y) lies in D.
The exact number of such pairs is

    sum_{z in D} [ binom(|N_H(z) intersect S|,2)
                    − e_H(N_H(z) intersect S) ].

No pair is counted twice, by uniqueness of the old common neighbor.
All old direct edges remain; every lost pair must be repaired by the actual
new adjacency or an actual new-old or new-new path.

## 5. Saturated-vertex screen and an honest first executable test

Let Z0={x in S: delta(x)=0}. No added edge can touch these vertices.
For any deleted z, two nonadjacent points of N_H(z) intersect Z0 would
lose their sole old common neighbor and can never gain a direct edge or
a new two-step path: every such new path contains a new edge incident to
one of the two endpoints. Therefore N_H(z) intersect Z0 must be a clique.

For external z its old neighborhood is four disjoint edges plus its
isolated absolute neighbor, so it contains at most two Z0 vertices and two
must be adjacent. For z absolute **or nucleus**, its neighborhood is
independent, so it contains at most one Z0 vertex. This is a strong exact
necessary screen, not an arbitrary choice of a repair boundary. It has not
yet yielded a uniform contradiction for all f>=8 deletion sets.

The smallest meaningful next test is a **variable deletion-set screen** at
58, not a fixed-seed completion: all15-subsets D of the73 actual vertices,
with the proved f>=8/nucleus conditions, exact nonnegative deficits, old
triangle-hit conditions and the Z0-neighborhood constraints above. It can
be expressed as a small Boolean/counting instance on the73 deletion bits
and exact derived indicators, with no graph-edge completion variables.
A single bounded profile would either find a concrete surviving deletion
set for further assessment or, only with a checked complete contradiction,
exclude this necessary-condition domain. SAT at this stage is not a graph.
**No such encoder or run is authorized or implemented by this note.**

If this screen supplies a reason to invest further, the complete family has
an exact simultaneous encoding: retain73 survivor indicators with exactly
n true; use one actual A bit for every unordered original pair; force it
zero if either endpoint is deleted and force each H edge true when both
survive. Require degree8 at every survivor, degree0 at deleted vertices,
and all surviving pairs covered by an actual A edge or one of the71 real
two-edge paths. Non-H edges between survivors are otherwise free. This
joint domain covers all deletion sets and all monotone completions without
freezing a port, deletion shape or target boundary. A saved SAT graph is
decoded to n vertices and independently checked. UNKNOWN proves nothing.

## 6. Two direct fiber-deletion examples, not selected main branches

The root proposed two concrete geometries for a cheap diagnostic. They were
evaluated from the saved ambient edge list, without a solver or deletion-set
enumeration. The exact record is
`computations/dd82/construction/polarity73_reduction_run/two_fiber_examples.json`.
The sample uses absolute labels a=1,b=8 and the first labeled x in C_b.
Both samples pass the saturated-pair screen, illustrating that it is only
a necessary condition.

**Order59: D=C_a union (C_b minus {x}) union {a}.** The retained graph
has42 vertices of degree7,16 of degree8, and the absolute vertex b of
degree2. It has282 uncovered pairs and requires24 new edges. Apart from
b all positive deficits are one. Its six new neighbors must be external;
the other36 deficient external points would be paired by18 new edges.

This geometry is in fact impossible, for every such a,b,x, by the following
uniform count. Write O for its50 surviving external points. The old
neighbors of b are nu and x, so old b coverage in O is
E={x} union (N_J(x) intersect O), of size8. All42 other external points
have deficit one. If Q is the six new neighbors of b, no other new edge
can touch Q. Consequently b can gain coverage only through the six old
O-closed neighborhoods of Q, each of size7. To cover all42 missing points,
those neighborhoods must be disjoint and avoid E.

Let f0 be the unique neighbor of x in deleted C_a. An eligible q must have
old distance greater than two from x within O. Its unique H common neighbor
with x must therefore be f0: all other external neighbors of x survive,
and q lies in a different fiber from x. Conversely a retained external
neighbor of f0 other than x or the triangle mate m of edge xf0 satisfies
this condition. Thus the only six choices are

    Q = (N_J(f0) intersect O) minus {x,m}.

The eight J neighbors of f0 induce four disjoint edges, one being xm.
The six forced choices therefore induce three old edges. Their closed
neighborhoods overlap, contradicting the required disjoint cover.
The sample's direct union size was36, leaving six of the42 points uncovered.
The uniform contradiction does not depend on that numerical union value.

**Order58: D=C_a union C_b union {a}.** There are49 external vertices
of degree7, the absolute b of degree1, and8 saturated core points. There
are301 uncovered pairs, and28 new edges are needed: b takes seven new
external neighbors Q, and the other42 external points receive a matching.
The retained external graph J[O] has49 vertices and degree6. Its old
b coverage is empty, so the seven seven-point closed neighborhoods centered
at Q must partition O. Thus Q is an arbitrary perfect one-code of this
particular graph. This necessity does not prove all such codes are fibers.

Every surviving whole fiber is indeed such a perfect code. The direct
sample diagnostic checked all seven of those choices; each has72 uncovered
old Q-to-(O minus Q) pairs. Once Q attaches to b, no other new edge touches
Q. For y outside Q, its single new matching neighbor has exactly one old
Q neighbor, by the perfect-code property. Hence at most one missing Q-y
pair can be repaired for each of the42 vertices y. The72 required repairs
exceed42, excluding all seven whole-fiber code choices in this sample.

For a general perfect code Q the same argument supplies the necessary
condition that every y outside Q have at most one uncovered old partner
in Q, and hence at most42 such uncovered cross pairs in total. Equivalently
for the opposite incidence count, a fixed center c has just six old external
neighbors. Their six new matching edges can repair at most six old bad
c-to-(O minus Q) pairs. A center with more than six such pairs excludes Q.

The root then authorized one exhaustive exact-cover diagnostic, capped at
five CPU seconds or one million nodes, for this saved sample only.
`polarity73_reduction_run/perfect_codes58.py` treats the49 seven-point closed
neighborhoods as exact-cover rows. At each node it chooses the smallest
uncovered vertex and branches on **every** row containing it that is
disjoint from the already covered vertices. Each complete cover has seven
rows; the procedure assumes no symmetry. The first-uncovered rule covers
every possible perfect code, and sorted code tuples are checked for duplicates.

The single actual run finished exhaustively after98 nodes, finding exactly
seven codes, all seven surviving whole fibers. It used0.002408 CPU seconds
and0.008827 wall seconds including the result write, with no truncation.
`perfect_codes58.json` retains every code, the exact-cover completeness flag,
limits, node count, the independently recomputed original bad-pair counts,
and the measured pre-output computation times. In every code one center has
12 old bad external partners and the other six have10, all exceeding6.
There are zero unresolved codes. No continuation or SAT call was made.

Thus the diagnostic plus the explicit coverage implication excludes this
**saved labeled order58 two-fiber deletion sample**, subject to source and
mathematical review. It does not classify perfect codes in other deletion
geometries, prove automorphism coverage over all choices a,b, or exclude
the complete73-point monotone58 family. This closed small example supplies
negative selection evidence, not a new construction or a main search branch.

## 7. The first two actual variable-screen candidates fail completion

The root later ran the necessary deletion screen once at58 and once at59.
Both returned checked SAT assignments, which mean only that their deletion
sets meet the encoded necessary conditions. The actual saved objects are
`polarity73_reduction_run/n58/deletion_candidate.json` and its n59 counterpart.
This analysis recomputed each retained graph directly from `geometry.edges`,
confirmed its saved degrees and all bad pairs, and found the following
writer-checked local contradictions. No completion solver was used and no
new deletion set was enumerated. The exact source sets and witnesses are in
the respective `candidate_analysis.json` files.

**General one-new-neighbor rule.** If delta(x)=1, write p for its unique
new neighbor. If s is saturated and (x,s) is an old bad pair, s keeps its
entire old neighborhood. The only possible new two-step path is x-p-s;
therefore p must lie in N_G(s) and have positive deficit. For several such
s simultaneously, p must lie in the intersection of these neighborhoods.
An empty permissible intersection excludes this fixed deletion set.

**Actual n58 candidate.** The retained graph has330 bad pairs and32
unit-deficit vertices; nine of their permissible domains are empty.
One sufficient witness is x=8, with old degree7. The vertices16 and40
both have degree8, and both pairs (8,16),(8,40) are old bad pairs. Their
complete fixed neighborhoods are

    N_G(16)={40,41,42,43,44,45,46,47},
    N_G(40)={16,17,18,19,20,21,22,23}.

These are disjoint. The sole new neighbor of8 cannot repair both pairs.

**Actual n59 candidate.** The retained graph has415 bad pairs and25
unit-deficit vertices; six of their permissible domains are empty.
Take x=20, of old degree7, and the two saturated vertices16 and42.
Both pairs (20,16),(20,42) are old bad pairs, and

    N_G(16)={41,42,43,44,45,46,47,72},
    N_G(42)={5,16,31,36,43,49,62,71}.

Their intersection is {43}. But43 also has degree8, so the forced new
edge20-43 is impossible. This excludes the second saved deletion set.

These short contradictions explain why screen SAT did not produce a
construction. They do not exclude the variable deletion family: the current
screen had constrained bad pairs between two saturated vertices, but had
not encoded the simultaneous repair requirements at unit-deficit vertices.
Adding that new family-wide consequence would require a separately reviewed
substantive screen change, not an unchanged rerun or a claim that either
SAT result already decided completion.

## Boundaries and open risks

The new mechanism is concrete, but the most natural absolute-line deletion
and both higher-order targets have already failed mathematically. No
positive empirical signal exists for58/59. The source diagnostic confirms
the ambient data, not the deletion-family lemmas or feasibility. Root-owned
mathematical/external direction review should decide whether the small
screen is justified. Allowing deletion of surviving ambient edges changes
the domain and invalidates the monotone obstructions; that broader search
has not been analyzed here and is not a reason to restart old graph repairs.

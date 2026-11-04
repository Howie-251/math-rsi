# Eight T15 hole orbits with a singleton avoided face

Date: 2026-11-01. ARIS proof-writer package.
Status: PROVABLE AS STATED relative to the listed Q4 finite certificates;
independent audit pending. Full T15 and full P6 remain unproved.

## Exact claim

Let $F$ be any matching of the complete graph on $V(Q_5)$, with holes
$\{a,x,y,b_1,b_2,b_3\}$, where $a$ has parity opposite to all five other
holes. The specified omitted holes are $x,y$. For every input whose marked
hole geometry is a cube-automorphic image of any of the eight rows below,
there is a simple cycle on $Q_5-\{x,y\}$ containing $F$, with only short
edges outside $F$. The cycle has exactly $30$ vertices.

The eight rows refer to zero-based orbit IDs in
`t15_analytic_geometry.json` and are equivalently specified by the local
table below. The original minority hole is normalized to $0$ before
reading the orbit IDs. The claim is for **every** matching realizing each
geometry; required edges may be long or join equal parities.

## Normalization, notation and dependencies

Choose the indicated cut. Its one-face $A$ contains exactly one original
hole, the omitted vertex $y$; the other face $B$ contains the other five
holes. Delete the cut coordinate and translate the common local labels by
the local label of $y$, so $y_A=0$. The corresponding vertex of $B$ has
the same local label and is joined by a short bridge. In these labels the
minority hole in $B$ is even, its other four holes are odd. Both coordinate
deletion and the common translation preserve adjacency within faces and
the correspondence across the cut.

| orbit | cut (zero-based) | B minority $a$ | B omitted $x$ | B included holes $I$ |
|---:|---:|---:|---:|---|
|13|1|0|1|7,11,13|
|14|1|0|1|7,11,14|
|19|2|3|2|4,8,14|
|31|3|6|7|1,11,13|
|32|3|6|7|1,8,13|
|35|3|6|7|8,11,13|
|37|0|0|7|11,13,14|
|38|4|15|14|2,4,8|

Write $F_A,F_B$ for the internal restrictions, $C$ for the original
crossing edges, $X_A,X_B$ for their endpoint sets, and $c=|C|$.
There are $15$ covered original vertices in $A$ and $11$ in $B$.
Consequently $c$ is odd and $1\le c\le11$.

Dependencies, with no use of Q5 T15 or P6:

1. Complete Q4 two-opposite-hole cycle tables, including their certified
   $51+53$ exceptions (`q4_distance1_avoided_table_verification.json` and
   `q4_distance3_avoided_table_verification.json`), decide the A paths below.
2. Q4 A4: holes $1:3$, omit a specified majority hole, obtain a 15-cycle
   (`Q4_CORE_AND_A4_SPLIT.md`).
3. Exact Q4 T15 classification (`Q4_T15_CLASSIFICATION.md`): for holes
   $1:5$, omitting two majority holes fails precisely when both omitted
   vertices neighbor the minority and the required matching joins its
   other two neighbors. In particular it succeeds if either omitted
   vertex is not a neighbor of the minority.
4. Finite completion accounting in `t15_single_avoided_face_probe.py/.json`.
5. Positive optional-edge spectra in `t15_single_crossing_spectra.json`,
   whose paths/cycles are independently checkable without trusting search.

Every application below specifies the resulting hole set and omitted
vertices. These are finite statements; no asymptotic or limiting argument
is used. All local degree-two contractions are expanded at the end.

## 1. The exact A path test

Choose $d\in X_A$ and a perfect pairing $D$ on $X_A-\{d\}$.
Then $L=F_A\cup D$ is a matching on $Q_4$ with holes $0,d$.
For an odd vertex $z\ne d$, let $k=L(z)$. Define
$T_z=L-\{zk\}+\{dk\}$, a matching with holes $0,z$.

A 14-cycle on $Q_4-\{0,z\}$ containing $T_z$ is equivalent to a
15-vertex $d$--$z$ path on $A-\{0\}$ containing $L$ and using short
new edges. In the forward direction delete $dk$, then append $kz$.
In the reverse direction $zk$ must be the last edge, since $z$ is covered
by $L$ and is an endpoint; delete $z$ and add $dk$. Both graphs are simple:
$d,k,z,0$ are distinct, and adding an edge between endpoints of a
14-vertex path cannot duplicate one already in that path. The case $z=d$
is declared unavailable. Thus the complete Q4 tables give an exact test.

## 2. Transfers for safe and occupied endpoints

Set
$$S=\{z\in O(Q_4):z\ne x,\ d(a,x)\ne1\text{ or }d(a,z)\ne1\}.$$
The three vertices in $I$ belong to $S$ in every row. Suppose Section 1
gives an A path $P$ with endpoint $z\in S$. Delete $D$, attach all original
crossings $C$, and add the short bridge $z_Az_B$.

### 2a. Safe endpoint: $z_B\notin X_B$

This is a path forest with endpoint set $X_B\cup\{z_B\}$ and interiors
partitioning $A-\{0\}$. If $z_A$ itself is a port different from $d$,
its mandatory edge belongs to $D$ and is the last edge of $P$; deleting
it isolates $z_A$ temporarily. Its original crossing and its new bridge
restore degree two, yielding a valid path component. No original matching
edge is lost. Compress each path to obtain a matching $R$ on the endpoint
set.

If $z\in I$, the matching $F_B\cup R$ has holes
$\{a,x\}\cup(I-\{z\})$, of type $1:3$. Q4 A4 omits $x$, giving a
15-cycle. Expand $R$ to obtain the desired $15+15=30$ cycle.

Otherwise $z_B$ is internally covered, since it is neither an original
hole nor a port. Write $k=F_B(z)$ and $q=R(z)$.
The sets of internal matching endpoints and crossing ports are disjoint,
so $k\ne q$ and replacing $kz,zq$ by $kq$ creates a matching $L_B$.
Its holes are $\{a,x\}\cup I\cup\{z\}$, of type $1:5$.
At least one of $x,z$ is nonadjacent to $a$ by the definition of $S$.
The exact Q4 T15 theorem therefore gives a 14-cycle omitting $x,z$.
Expand $kq$ and the remaining compressed edges. This restores $z_B$ and
all $15$ A vertices, producing a single $14+1+15=30$ cycle.

### 2b. Occupied endpoint: $z_B\in X_B$, $c\ge3$

Here require $d=C^{-1}(z_B)$ to be a good root for $z$ in Section 1.
Then $d\ne z$ and $D$ is nonempty. Deleting $D$ from $P$ separates its
two endpoints. Attaching the original crossings adds distinct B leaves.
The bridge $z_Az_B$ joins the two different endpoint components, because
$z_B$ was attached at $d$. It creates no cycle. If $z_A$ is also a port,
its separate crossing ends at a different B port; the temporary isolated
vertex boundary is covered by the same argument.

The resulting forest has endpoints $X_B-\{z_B\}$ and interiors precisely
$(A-\{0\})\cup\{z_B\}$. Compress it to $R$. Now $F_B\cup R$ is a
matching with holes $\{a,x\}\cup I\cup\{z\}$. Apply the same Q4 T15
theorem omitting $x,z$ and expand. The resulting cycle has $30$ vertices.
All artificial edges are deleted or expanded, so all surviving new edges
are short. Section 4 treats the excluded case $c=1$ separately.

## 3. Complete accounting of roots and port pairings

For each odd $z$, inverse-enumerate every failing state $(d,L)$ with
$z\ne d$ from the negative Q4 table for holes $0,z$. For every such
negative matching $T$ and oriented edge $dk$ of $T$, the inverse is
$L=T-\{dk\}+\{zk\}$. Set storage removes duplicates. These inverses are
complete by Section 1; $d=z$ is handled separately in each test.

Any state failing all three fixed targets $I$ belongs to the union of
their inverse lists, since at most one target equals $d$. Test all three
conditions in that union. There are $105$ failed states for each of
orbits $13,14,31,35,37$, and none for $19,32,38$.

For fixed $c$, a partial $F_A$ has $(15-c)/2$ edges. It has exactly
$c(c-2)!!$ states $(d,F_A\cup D)$, with $(-1)!!=1$.
Count appearances of each submatching of that size in all failed states.
It is stalled exactly when the count equals $c(c-2)!!$; smaller counts
leave a successful fixed-target choice. Every stalled partial is listed
this way, including those not selected by any prior construction.

For each of the five nonempty rows the stalled counts at
$c=1,3,5,7,9,11$ are respectively $105,105,21,1,0,0$.
For each stalled partial and root $d$, there are $(c-2)!!$ pairings.
For each $z\in S$, count failed completions at that root. A root is good
exactly when $d\ne z$ and this count is smaller than $(c-2)!!$.

Let $G$ be the endpoints in $S$ with at least one good root. If $|G|>c$,
some endpoint is safe. Otherwise, failure of both transfers would require
$G\subseteq X_B$ and an injective assignment $z\mapsto C^{-1}(z_B)$
mapping every $z$ to a bad root. The finite check tests Hall's condition
on these bad-root sets and stores a deficient subset whenever no such
injection exists. For every stalled partial at $c\ge3$, there is either
a safe endpoint by $|G|>c$ or no bad-root injection. Thus Section 2 applies
to every actual crossing endpoint set and every actual crossing bijection.

For orbit $37$ the same check gives a safe endpoint also at $c=1$.
For the other four rows $13,14,31,35$, the only usable endpoint in each
$c=1$ stalled state is the following $h$:

|orbit|13|14|31|35|
|---:|---:|---:|---:|---:|
|$h$|14|13|8|1|

If $X_B\ne\{h\}$, $h$ is safe and Section 2a applies.
The only remaining case is $X_B=\{h\}$, treated next.

## 4. One crossing: two cycles and a certified common optional edge

Fix one of the four rows and one of its $105$ stalled A matchings.
The only crossing is $d_Ah_B$. The available A path $P$ goes from $d_A$
to $h_A$ through all of $A-\{0\}$. Add $d_Ah_B$ and the short bridge
$h_Ah_B$ to close a simple 16-cycle $C_A$ whose support is
$(A-\{0\})\cup\{h_B\}$. The endpoints $d,h$ are distinct.

The B matching has holes $\{a,x,h\}\cup I$ and five edges, since its
only port is $h$. Thus there are exactly $9!!=945$ possible $F_B$.
Since $h$ is not a neighbor of $a$, Q4 T15 gives a 14-cycle $C_B$ on
$B-\{x,h\}$ containing $F_B$.

It remains to choose $P,C_B$ with a common optional short edge in their
local coordinates. This is a finite positive-certificate assertion:
for each of the $105$ A matchings, retain a collection of valid $d$--$h$
paths, and for each of the $945$ B matchings retain valid 14-cycles.
Let $U_A,U_B$ be the unions of their short edges outside $F_A,F_B$.
Every one of the $105\cdot945$ pairs has $U_A\cap U_B\ne\varnothing$.
The minimum intersection sizes, by row $13,14,31,35$, are $7,5,9,6$.
The four rows comprise $396900$ pairs, with no empty intersection.

The files `t15_single_crossing_spectrum_inputs.json` and
`t15_single_crossing_spectra.json` contain all $4200$ matching inputs and
the witnessing paths/cycles. `t15_single_crossing_spectra.py` checks
every witness's exact support, endpoints, matching containment and
shortness, reconstructs every stored union, and tests every pairwise
intersection. Completeness of the B matching lists is by all pairings of
their ten covered vertices; completeness of the A lists is Section 3.
Only these **lower bounds** on optional-edge unions are needed; no failed
search or assertion of maximality of a spectrum is used in the proof.

Choose $st\in U_A\cap U_B$, and choose its witnessing $P,C_B$.
Build $C_A$ from that $P$ as above. Delete $s_At_A$ from $C_A$ and
$s_Bt_B$ from $C_B$, then insert the two short bridges $s_As_B,t_At_B$.
The cycles were vertex-disjoint. The deleted edges belong to neither
original matching, and $s,t$ are distinct and avoid $0,x,h$ because
they occur in both local supports. The two opened paths joined by the
two bridges form one simple cycle on their union. It covers precisely
$Q_5-\{0_A,x_B\}$, retains $F_A,F_B,d_Ah_B$, and all added edges are
short. This resolves the last one-crossing case.

## Conclusion and limits

Sections 2--4 exhaust all roots, pairings, crossing counts and internal
matchings for all eight displayed marked geometries, so the exact claim
follows relative to the listed finite inputs. Undo their normalizations
and any cube automorphism to cover their entire marked-hole orbits.

This does not prove all T15 geometries. It does not address Q6 EP0 or
claim full eight-hole P6. Its concrete Q6 coverage must be recomputed
against all allowed cuts before updating any remaining-parent count.
The prescribed-edge route remains a separate unproved connectivity route.

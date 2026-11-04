# Eight-hole covered endpoints: a two-bridge core and an exposed-port reduction

Date: 2026-11-01. ARIS proof-writer working draft; independent review pending.
This file changes no earlier proof or main research state.

## Claim and status

The original objective remains the Hamilton path from a free even root $u$ to a
covered odd target $v$ containing an arbitrary eight-hole short matching of $Q_6$.
**NOT CURRENTLY JUSTIFIED** for all covered targets, even with A6 available.

The new conditional results proved below are:

1. Any cut with $(a,b)=(2,1)$ is solved by the explicit $Q_5$ core T15 defined below.
2. Any cut with $(a,b)=(2,0)$ is solved by T15 plus the explicitly quantified
   exposed-port path condition EP0 at that cut.
3. The endpoint-position branches in both transfers can be handled by one tagged
   closure and simultaneous path compression. No unproved terminal-mirror shortcut
   is needed.
4. EP0 cannot be justified merely by choosing an arbitrary $(2,0)$ cut: for each of
   21 cuts of seven listed exceptional geometries, an explicit realizing short
   matching has no eligible exposed-port edge at all. Across all three cuts of each
   of those seven geometries, however, at least one eligible edge always exists.
   The latter is certified by explicit Hall obstructions, not a Hamilton sample.

Results 1--2 have status **PROVABLE AFTER EXTRA ASSUMPTION**, namely T15 and, for
result 2, EP0. Neither new core is claimed proved. The combinatorial transfer proof
below uses N10 and elementary compression; it does not use A6. A6 is available for
the previously established nine good rows and free-target theorem.

## 1. Imports, notation and exact new obligations

Use the eight-hole notation of `EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md`:
$u=0$, three other even holes $Z$, four odd holes $W$, and $Z\cup W$ independent.
The target $v$ is odd and covered. In cut coordinate $i$, let $A$ contain $v$,
let $B$ be the opposite face, and put
$a=|Z\cap A|$, $b=|W\cap A|$, $\delta=\boldsymbol1[u\in A]$.
Let $M_A,M_B$ be internal matching edges and $X_A,X_B$ the crossing-port sets.
Write $\bar x=x\oplus e_i$ for the short mirror. All crossing edges are short,
so each crossing port is matched to its mirror.

Import N10 from `GENERAL_NEAR_PERFECT.md`: an arbitrary matching of $K(Q_5)$ with
holes $r,q$ has a Hamilton $r$--$v$ extension with short new edges whenever
$v\ne r$ has the parity of $q$. Long and same-parity edges of an artificial
completion matching are allowed. Import the established five-direction free-root
endpoint theorem to dispose of $c=0$. Full A6, if used outside this file, retains
its separate audit and dependency scope.

**T15, an unproved $Q_5$ two-avoidance core.** For every matching $L$ of $K(Q_5)$
with exactly one even and five odd holes, and every specified pair of distinct odd
holes $y_1,y_2$, require a cycle through exactly
$V(Q_5)\setminus\{y_1,y_2\}$ containing $L$, with short new edges.
The assertion includes its parity reversal. This is a 30-vertex cycle assertion.
It does not follow from A6 by merely changing the omitted-hole count.

For an $(a,b)=(2,0)$ cut write $Z\cap A=\{z_1,z_2\}$ and
$S=\{\bar w:w\in W\}\subset A$. Each $s\in S$ is even; independence gives
$S\cap\{z_1,z_2\}=\varnothing$. Since its mirror is an original free vertex,
$s$ is not a crossing port. It is internally covered by $M_A$, except that
$s=u$ is possible when $\delta=1$.

**EP0, a local sufficient condition, not an established universal lemma.**
Choose $r=u$ if $\delta=1$; if $\delta=0$, choose either member of
$\{z_1,z_2\}$ as $r$. Require the existence, in this order, of

$$
q\in X_A\cap O,\qquad
D\text{ a perfect matching on }(X_A\setminus\{q\})
     \cup(\{z_1,z_2\}\setminus\{r\}),
$$

and a Hamilton $r$--$v$ path $P$ containing $M_A\cup D$, with short new edges,
such that $qs\in E(P)$ for some $s\in S$. All quantifiers are existential
after the cut and original matching are fixed. The formula removes $r$ from
$\{z_1,z_2\}$ only when it belongs to that set. The port $q$ may equal $v$
when $v$ is a crossing port. The vertex $s$ may equal $u$ when $\delta=1$.

The matching $M_A\cup D$ has exactly the holes $r,q$. Thus N10 guarantees some
such $r$--$v$ path, for every admissible choice of $q,D$; it does **not** guarantee
the additional edge $qs$. The existential edge requirement is precisely the
unproved part of EP0. In particular $X_A\cap O$ merely containing a neighbor of
$S$ is weaker than EP0.

Dependency map: N10 plus the selected completions -> first A path; a short bridge
at each consumed nonroot even hole -> two odd internally covered mirrors in B;
tagged terminal closure plus two-vertex compression -> an arbitrary $K(Q_5)$
matching with hole counts $(1,5)$; T15 -> final global path. EP0 adds one optional
edge deletion and a bridge to an original B hole, which preserves the same final
hole counts in the $(2,0)$ row.

## 2. A unified closure and two-conflict compression

The constructions below start from an A path, delete artificial edges, and attach
each real crossing edge plus specified bridges. Their attached B vertices are all
distinct. They therefore form a path forest, whose A interiors are disjoint and
cover A. Every A vertex has degree two except the specified global endpoints that
lie in A. The covered target $v$ may belong to $X_A$: removing its D edge can
isolate it, after which attaching its real crossing edge gives its terminal segment.

When $\delta=1$, there are two different terminal segments, from $u$ and $v$ to
B; removing a nonempty D from the first A path separates the original endpoints.
When $\delta=0$, there is one terminal segment from $v$ to B; $u$ is still a free
B vertex. Temporarily join the global endpoints by a **tagged artificial edge**
$uv$. For $\delta=1$ this joins the two terminal segments into a B-to-B path;
for $\delta=0$ it extends the terminal segment to the B endpoint $u$.
Compress this tagged path and all other B-to-B segments. They give a matching
$T$ on their distinct B endpoints. The tag belongs to exactly one compressed edge.
This is a proof device: $uv$ is removed at the end, so its length is immaterial.

In both applications the only overlap of covered vertices between $T$ and $M_B$
is the set $Y=\{y_1,y_2\}$ of the two odd bridge mirrors. Each $y_j$ is internally
covered by an original edge $y_jk_j$, where $k_j$ is an even internally covered B
vertex outside the endpoint set of $T$. The two $k_j$ are distinct. Since $Y$
has one parity and $M_B$ is short, no $M_B$ edge joins the two members of $Y$.

The union $M_B\cup T$ thus has degree two exactly on $Y$, and degree at most one
elsewhere. Every component containing a member of $Y$ is a path: it has the
degree-one neighbor $k_j$ at the end of its M_B edge. If $T$ pairs $y_1$ with
$y_2$, the component is $k_1-y_1-y_2-k_2$. Otherwise each conflict gives its
own three-vertex path, or a path with its T segment already compressed.
Compress all these paths, removing $Y$ from the local vertex set, into single
edges. The resulting edge family $L$ is a matching of $K(B)$, with both $y_j$
as holes. Any original M_B edge in such a path is recorded for expansion.
If a compressed edge carries the tag, its expansion preserves the tag.

T15 gives a single circle on $B\setminus Y$ containing $L$. Expand its recorded
paths and then every original transferred segment. This restores $Y$ once and
all A vertices once, retaining every original edge. The result is a single
64-vertex circle with the tagged $uv$ edge. Deleting that edge gives the required
Hamilton $u$--$v$ path. Every surviving new edge is short.

This proof covers terminal and nonterminal bridge mirrors at once. No application
of a local endpoint theorem at a covered mirror is concealed in it.

## 3. The $(2,1)$ row reduces to T15

Let $Z\cap A=\{z_1,z_2\}$ and let $w$ be the sole member of $W\cap A$.
For each $j$ bridge $z_j$ to $y_j=\bar z_j$. The mirrors are odd and distinct.
They are not W holes by independence, cannot be the even root, and cannot be
crossing ports because $z_j$ is free. Thus both are internally covered by $M_B$.

If $\delta=1$, set $r=u$ and choose D to pair $X_A\cup\{z_1,z_2\}$.
The original A holes are $u,z_1,z_2,w$, so the number $c$ of crossing ports is
even. The set paired by D has positive even size. The holes of $M_A\cup D$
are exactly $r,w$.

If $\delta=0$, set $r=z_1$ and choose D to pair $X_A\cup\{z_2\}$.
Here the original A holes are $z_1,z_2,w$, so $c$ is odd and positive; D is
nonempty. Its completed matching again has exactly the opposite-parity holes
$r,w$. This choice needs **no even crossing port**.

In either case N10 gives a Hamilton $r$--$v$ path containing $M_A\cup D$.
Delete D, attach all real crossedges, and attach both short bridges $z_jy_j$.
For $\delta=0$ the bridge at $r=z_1$ attaches to the initial path endpoint;
its degree becomes two, as required because it is not the global root.
For $\delta=1$ the global root retains degree one. All other degree and forest
requirements of Section 2 follow from distinct B attachments.

For $\delta=1$, the original B holes have counts $(1,3)$. The matching T consumes
all crossing ports and covers both internally matched $y_j$. After conflict
compression its holes are the original B holes together with $Y$, hence $(1,5)$.
For $\delta=0$, the original B holes have counts $(2,3)$ and include $u$.
The tagged closure consumes $u$, while the two conflict compressions expose $Y$.
Thus the new holes are $(H_B\setminus\{u\})\cup Y$, again $(1,5)$.
T15 avoiding $Y$ applies, and Section 2 completes the path.

## 4. The $(2,0)$ row reduces to T15 under EP0

Suppose EP0 supplies $r,q,D,P,s$, and set $t=\bar s\in W\subset B$.
The odd crossing-port surplus is $2+\delta$, so such ports exist.
For $\delta=1$, $c$ is odd and at least three, and D has size $(c+1)/2$.
For $\delta=0$, $c$ is even and at least two, and D has size $c/2$.
In both cases D is nonempty, avoids $r,q$, and $M_A\cup D$ has holes $r,q$.

Delete D and the short new edge $qs$ from P. Attach all real crossing edges;
attach both bridges $z_jy_j$ as in Section 3; and attach the short bridge $st$.
The vertex $s$ is outside $X_A\cup\{z_1,z_2\}$, so this extra deletion does not
interact with D or a preexisting bridge at $s$.

If $q\ne v$, it loses one of its two new path edges and gains its real crossing
edge, so its degree remains two. If $q=v$, deletion isolates the path endpoint,
and its real crossing edge gives it degree one. If $s\ne u$, it is internally
covered by $M_A$, loses one new edge, and gains $st$, so it retains degree two.
If $s=u$ (only possible for $\delta=1$), it loses its unique path edge and gains
$ut$, retaining degree one. These include all endpoint boundaries.

The new B endpoint $t$ is an original odd hole, distinct from $X_B$ and from $Y$.
It is distinct from $Y$ because a coincidence would give an edge between a
nonroot even hole and a member of W. Attachments therefore remain distinct,
and Section 2's tagged closure and conflict compression apply.

For $\delta=1$, original B hole counts are $(1,4)$. The transfer consumes the
odd hole $t$ and the conflicts expose $Y$: the final hole set is
$(H_B\setminus\{t\})\cup Y$, with counts $(1,5)$.
For $\delta=0$, original B hole counts are $(2,4)$; the closure also consumes $u$.
The final hole set is $(H_B\setminus\{u,t\})\cup Y$, again $(1,5)$.
T15 avoids precisely $Y$, and expansion completes the required global path.

## 5. What finite probes establish, and what they do not

The independent geometry work in `COVERED_EIGHT_GEOMETRY_CENSUS.md` reports that
each residual has a $(2,0)$ or $(2,1)$ cut. That complete geometric classification
is an external input to any future global use of this draft; this file does not
recertify it. In particular there are 50 normalized geometries, represented by
seven target-preserving permutation orbits, whose splitting cuts are all $(2,0)$.

The diagnostic script `eight_hole_covered_next_probe.py` constructs actual short
matchings on the covered vertices of the following seven representatives. For each
of their three $(2,0)$ cuts separately, it finds a 28-edge matching such that

$$E(Q_5)\cap\bigl((X_A\cap O)\times S\bigr)=\varnothing.$$

Every such output is verified directly as a matching with the exact eight holes.
There are 21 such positive witnesses, fully recorded in the JSON. Consequently
EP0 fails for arbitrary fixed cuts; it cannot be universally asserted in that form.

There is a useful weaker selection fact across cuts. In each representative,
simultaneously delete every short edge that would create an eligible $q$--$s$
adjacency in any of its three cuts. The resulting graph of covered vertices has
the isolated even vertices listed in the last column. Each such vertex is covered
in any realizing matching, so a realizing matching must contain a deleted edge.
That edge gives an eligible adjacency at at least one of the three cuts.

| $v$ | $Z$ | $W$ | $(2,0)$ coordinates | isolated even vertices after all deletions |
|---:|---|---|---|---|
| 1 | 3,5,9 | 14,31,47,62 | 1,2,3 | 15,30,46,63 |
| 7 | 3,5,6 | 8,16,32,56 | 0,1,2 | 24,40,48 |
| 7 | 3,5,15 | 8,25,41,56 | 1,2,3 | 9,24,40,57 |
| 7 | 3,15,23 | 25,26,56,59 | 2,3,4 | 24,27,57,58 |
| 7 | 15,23,39 | 56,59,61,62 | 3,4,5 | 57,58,60,63 |
| 31 | 15,23,27 | 1,2,32,35 | 2,3,4 | 3,33,34 |
| 31 | 15,23,63 | 32,35,37,38 | 3,4,5 | 33,34,36,39 |

Coordinates are numbered from zero. The script explicitly verifies the full
neighbor set of each listed Hall subset is empty in the deletion graph.
This proves the adjacency fact for all realizing matchings of each listed
geometry, and cube symmetries give it for their images. It is not a sample-based
Hamilton assertion. It still does not prove that the N10 path can contain that
eligible edge. That optional-edge prescription is the present barrier.

The parent agent separately verified all 21 positive matching witnesses and all
seven Hall certificates using the solver-free checker
`verify_eight_exposure_obstructions.py`; its result is recorded in
`eight_exposure_obstructions_verification.json`. This independent finite check
does not constitute semantic acceptance of the transfer draft or of either core.

The Q4 analogue of T15 must not be imported without qualification: prior diagnostic
files `q4_six_hole_two_avoided.cpp` and `q4_six_two_avoided_results.json` report actual
negative instances for some pairs of prescribed avoided majority holes. The Q5
statement T15 remains a separate conjectural core in this document.

## 6. Remaining exact research obligations

T15 is a standalone unproved complete-graph-matching extension theorem. EP0 is a
genuine extra path-edge condition. A global route through these reductions requires
a proved choice of cut satisfying $(2,1)$ or satisfying $(2,0)$ together with EP0;
mere availability of a $(2,0)$ cut is insufficient. The seven-orbit exceptional
incidence check supplies an eligible edge in some cut, but not EP0.

No conclusion here closes R8-covered. Closing T15 alone would nevertheless close
all $(2,1)$-cut inputs, regardless of the other cut rows, via the full quantified
transfer in Section 3. Independent proof-checker review of this draft is still needed.

# Eight-hole reduction: complete free-target branch and exact covered residual

Date: 2026-11-01. Authoring route: ARIS proof-writer. Independent proof-checker
review is still required. This document does not close eight holes or full P6.

## Claim

Let $M\subseteq E(Q_6)$ have exactly eight holes, let $u$ be a free root,
and let $v$ have the opposite parity. The original objective is a Hamilton
$u$--$v$ path containing $M$.

The claims proved here are:

1. Assuming Q5 A6, the objective holds for **every free target** $v$.
2. Assuming Q5 A6, it holds for every covered target satisfying the
   explicit nine-row cut criterion below, or the preliminary augmentation.
3. Assuming Q5 A6, full eight-hole P6 is equivalent to the additional
   universal residual obligation R8-covered stated in Section 7.

The third statement is a complete domain partition, not a claim that
A6 already implies R8-covered. R8-covered is nonempty, even among realizable
short-matchings, as witnessed in Section 8.

## Status

**PROVABLE AFTER EXTRA ASSUMPTION**, for claims 1--3, relative to the
explicit imports and the exhaustive geometry certificate below.
**NOT CURRENTLY JUSTIFIED**, for the implication A6 alone implies full
eight-hole P6. No such implication is asserted.

## Assumptions and notation

Import full six-hole Q6 P6 from `SIX_HOLE_CLOSED.md`, full Q5 A4 from
`CANONICAL_A4_CLOSURE.md`, and Q5 N10/N14/K4 from their recorded proofs.
The A4 closure audit is `CANONICAL_COMPLETION_REVIEW.json`; its PASS is
relative to imported theorems and finite certificates, with same-family,
provisional assurance. Older six-hole proof files retain historical open-A4
wording; this document uses the later closure, not that historical status.
Import the established five-direction free-root endpoint theorem.

**A6**, the only new auxiliary assumption, says that every matching of
$K(Q_5)$ with hole counts $2,4$ extends, using only short new edges, to a
circle covering exactly $Q_5-v$ for each specified majority-parity hole $v$.
The matching edges may be arbitrary, including long same-parity edges.

Use a cube automorphism to put $u=0$ and hence make $u$ even. Write the
other even holes as $Z=\{z_1,z_2,z_3\}$ and all odd holes as $W$, $|W|=4$.
The target $v$ is odd and may or may not belong to $W$.
For a coordinate $i$, let $A$ be the face containing $v$, and $B$ the other.
Set

$$a=|Z\cap A|,\quad b=|W\cap A|,\quad
\delta=\boldsymbol1[u\in A].$$

Thus the original hole counts in $A$ are $(a+\delta,b)$ and those in $B$
are $(4-a-\delta,4-b)$, in the order even/odd. Let $M_A,M_B$ be internal
matching edges, let $C$ be the matching edges crossing the cut, and let
$X_A,X_B$ be their endpoint sets. Put $c=|C|$.

## Dependency map

1. A6 plus A4/N14/K4/N10 gives the general local endpoint lemma in Section 1.
2. That lemma gives all nine-row cut transfers in Sections 3--5.
3. A finite complete hole-geometry check gives every free-target input
   one of these cuts; Section 6 handles its one root-bridge boundary case.
4. Covered inputs outside these reductions are exactly R8-covered.

## Proof

### 1. General local endpoint lemma

For a vertex $x$, write $\epsilon(x)=1$ for even and $-1$ for odd. Let
$F\subseteq K(Q_5)$ have $2t$ holes, $1\le t\le3$, with even-minus-odd
hole count $h\in\{-2,0,2\}$. If $r$ is free and $y\ne r$ satisfies

$$\epsilon(r)+\epsilon(y)=h,$$

then $F$ has a Hamilton $r$--$y$ extension with only short new edges.
For $h=0$ this includes arbitrary opposite-parity targets. For $h=\pm2$
both endpoints have the majority hole parity.

If $y$ is free, add the auxiliary edge $ry$. The remaining holes are
balanced and number $2t-2\in\{0,2,4\}$. A full circle extension follows
respectively from the perfect-matching theorem, N10, or K4. Delete $ry$.
If $y$ is covered, put $k=F(y)$ and $F'=F-yk+kr$. Its hole imbalance is
$2\epsilon(y)$: this follows by subtracting the free root and adding
the new free target to the old holes. Its total hole count remains $2t$.
Apply N14, A4, or A6 for $t=1,2,3$, avoiding $y$. Delete $kr$ and append
the original edge $ky$. Every introduced long edge has been deleted.

In particular, balanced matchings with $2,4,6$ holes have full circle
extensions: take any free root and a short neighbor as target in this
lemma, and close the resulting Hamilton path. The edge between the two
ends is not already in a path on 32 vertices. All these statements allow
arbitrary required matching edges, so they apply to compressed transfers.

### 2. Preprocessing and forest bookkeeping

If any two vertices of $Z\cup W$ are adjacent, add their short edge to
$M$. This preserves the free root and yields six holes. Full six-hole P6
solves the original endpoint problem. Hence assume $Z\cup W$ independent.

If $v\in W$ and $uv$ is short, add $uv$ to $M$ and apply six-hole P6 to
obtain a full circle containing this enlarged matching: use any remaining
free root, a short neighbor as its target, and close the Hamilton path.
Delete $uv$. Thus in the free-target census $d(u,v)$ is 3 or 5.

If $c=0$ for any selected cut, all original matching edges use at most
five directions. The imported five-direction theorem solves the original
endpoint problem. Below $c>0$.

In each transfer choose an artificial matching $D$ in $A$. A Hamilton
path $P_A$ supplied by Section 1 contains $M_A+D$. When $u\in A$, its
ends are $u,v$; when $u\in B$, its ends are an even port $p\in X_A$ and
$v$. Delete $D$, attach all real crossedges, and optionally one bridge
$xy$ from an original hole $x\in A$ to its mirror $y\in B$.

The resulting graph is a path forest. Each newly attached $B$ vertex is
distinct and attached once. If the covered target $v$ belongs to $X_A$,
deleting its incident $D$ edge can isolate it, but attaching its original
crossedge immediately gives its terminal segment. All other artificial
edges avoid path endpoints. The degrees in $A$ become two except for
the actual endpoints $u,v$ that lie there.

For $\delta=1$, $D$ is nonempty, so there are two distinct terminal
segments $u$--$r$ and $s$--$v$, with $r,s\in B$; compress the other
segments into a matching $R$. For $\delta=0$, there is one terminal
segment $r$--$v$; compress the others into $R$. If a bridge is present,
these $B$ segment endpoints are in $X_B\cup\{y\}$; otherwise in $X_B$.

An internal bridge endpoint $y$ is internally matched by $M_B$. If it
belongs to $R$, it produces exactly one conflict. With $k=M_B(y)$ and
$d=R(y)$ replace the two edges by

$$F_B=(M_B-yk)\cup(R-yd)\cup\{kd\}.$$

This is a matching because $k$ is internally covered and $d$ is a
different crossport. Ultimately expand $kd$ to the original $ky$ followed
by the corresponding $y$--$d$ transfer segment. This restores $y$ once.
Other compressed edges expand into their disjoint segments.

### 3. Zero bridges: $b=a+1$, $a\in\{0,1,2\}$

If $\delta=1$, pair all of $X_A$ into $D$. Its size is even: internal
short edges give $|X_A\cap E|-|X_A\cap O|=b-a-1=0$.
Since $c>0$, $D$ is nonempty. The holes of $M_A+D$ are balanced,
$(a+1,a+1)$, so Section 1 gives the $u$--$v$ path in $A$.
After transfer $M_B+R+rs$ is a matching with balanced holes
$(3-a,3-a)$. Use its full circle, delete $rs$, expand and attach the
two terminal segments.

If $\delta=0$, the same port difference is $b-a=1$, so an even port
$p$ exists. Pair $X_A-\{p\}$ into $D$. The holes become balanced
$(a+1,a+1)$; use the $p$--$v$ path. Now $M_B+R+ur$ has balanced holes
$(3-a,3-a)$: the extra free $B$ root $u$ is consumed by $ur$.
Its circle, with $ur$ deleted, expands to the required path.

The values $a=0,1,2$ ensure all the local balanced matchings have at
most six holes. Artificial $rs$ or $ur$ joins distinct free vertices.

### 4. One even hole consumed: $b=a$, $a\in\{1,2,3\}$

Choose $x\in Z\cap A$, and let $y=x\oplus e_i$ in $B$. Independence
of $Z\cup W$ implies $y\notin W$. It cannot equal even root $u$.
As its cross-cut neighbor is the free vertex $x$, $y$ is internally
covered by $M_B$. The bridge $xy$ is short and $y$ is odd.

If $\delta=1$, pair $X_A\cup\{x\}$ into $D$; the port difference is
$-1$, so $c$ is odd. If $\delta=0$, the port classes are equal and
$c>0$, so choose an even port $p$ and pair
$(X_A-\{p\})\cup\{x\}$ into $D$. In both cases $D$ is nonempty,
and the resulting holes in $A$ are balanced $(a,a)$. Section 1 applies.

If $y$ is not a terminal segment endpoint, perform the single-conflict
compression and add $rs$ ($\delta=1$) or $ur$ ($\delta=0$). The holes
are exactly $(3-a,5-a)$ and include $y$ in the odd majority. Apply
A6/A4/N14 for $a=1/2/3$, avoiding $y$, then delete the auxiliary
endpoint edge and expand the conflict to restore $y$.

If $y$ is a terminal endpoint and $\delta=1$, write $q$ for the other
terminal endpoint. The matching $L=M_B+R$ has original $B$ holes
$(3-a,4-a)$ plus $q$, while $y$ is covered. Its total hole count is
$8-2a\le6$. The imbalance is $0$ when $q$ is even and $-2$ when $q$
is odd; Section 1 gives a $q$--$y$ path in either case. If
$\delta=0$ and $y$ is the terminal endpoint, $L=M_B+R$ has balanced
holes $(4-a,4-a)$, also at most six, and Section 1 gives $u$--$y$.
Expand and attach the terminal segment(s). These are all possible
positions of $y$.

### 5. One odd hole consumed: $b=a+2$, $a\in\{0,1,2\}$

Choose $x\in W\cap A$ different from $v$ if $v$ is free, such that
$y=x\oplus e_i\ne u$. Independence implies $y\notin Z$; because
$x$ is free its mirror $y$ is internally covered by $M_B$. Thus $y$
is even. For a covered target there are at least two choices of $x$,
at most one with mirror $u$. For a free target and $a\ge1$ there are
again at least two choices after excluding $v$. For $a=0$, the only
failure of this choice is treated separately in Section 6.

If $\delta=1$, pair $X_A\cup\{x\}$ into $D$. The port difference is
$1$, so $c$ is positive odd and $D$ is nonempty. If $\delta=0$, port
difference is $2$; choose an even port $p$ and pair
$(X_A-\{p\})\cup\{x\}$ into $D$. In both cases the $A$ holes are
balanced $(a+1,a+1)$; Section 1 supplies the required path.

If $y$ is not terminal, conflict compression followed by $rs$ or $ur$
leaves exactly $(4-a,2-a)$ holes, with $y$ in the even majority.
Apply A6/A4/N14 for $a=0/1/2$, avoiding $y$, delete the auxiliary
endpoint edge, and expand to restore $y$.

If $y$ is terminal and $\delta=1$, the matching $L=M_B+R$ has holes
$(3-a,2-a)$ plus the other terminal endpoint $q$. Its total hole count
is $6-2a$. The imbalance is $2$ for even $q$ and $0$ for odd $q$;
Section 1 gives a $q$--$y$ path. For $\delta=0$ and terminal $y$,
$L=M_B+R$ has holes $(4-a,2-a)$ and Section 1 gives $u$--$y$.
Expand and attach the terminal segments.

Thus the good cut rows proved in Sections 3--5 are precisely

| $a$ | allowed $b$ |
|---:|---|
| 0 | 1,2 |
| 1 | 1,2,3 |
| 2 | 2,3,4 |
| 3 | 3 |

In every branch all added edges remaining after expansion are short.
The forest followed by a single local path gives one global Hamilton
path, rather than merely satisfying the required vertex degrees.

### 6. Free targets: exceptional root bridge and exhaustive geometry

The bridge-choice exception from Section 5 has $a=0,b=2,\delta=0$,
$W\cap A=\{v,x\}$, and $x\oplus e_i=u$. Here use a different first
path: pair **all** $X_A$ into $D$. The holes in $M_A+D$ are exactly
$x,v$, both odd. N10 gives a Hamilton $x$--$v$ path. The port imbalance
is $2$, so $c\ge2$ is even and $D$ is nonempty. Delete $D$, attach
the crossedges, and attach $ux$. There are two distinct terminal
segments $u$--$r$ and $s$--$v$, and a matching $R$ on all other
crossports. Now

$$L_B=M_B+R+rs$$

has exactly four even holes, including $u$, and two odd holes. A6
avoiding $u$ gives a circle on $B-u$. Delete $rs$, expand $R$, and
attach the two terminal segments, the first of which restores $u$
via its bridge. This covers all vertices once and preserves $M$.

It remains a **pure geometry statement** that a good cut always exists
for free targets after preprocessing. The executable certificate is
`eight_hole_free_cut_census.cpp`. Normalize $u=0$. An odd free target
at distance 1 was settled in Section 2. Permuting coordinates sends
every distance-3 target to $v=7$ and every distance-5 target to $v=31$.
For each of these two targets the certificate enumerates:

1. Every unordered triple of distinct nonzero even vertices $Z$, none
   adjacent to $v$.
2. Every unordered triple of odd vertices different from $v$ and
   nonadjacent to every member of $Z$; adding $v$ forms $W$.
3. Every one of the six cuts, testing membership in the displayed table.

No root-other-hole adjacency is excluded. Same-parity pairs cannot be
adjacent, so these loops enumerate exactly every geometry remaining
after Section 2, with no realizability assumption or missing matching
quantifier. In particular they may include geometries admitting no
short matching, which only strengthens the coverage assertion.

Compiled using `g++ -O3 -std=c++17`; observed output:

```
v=7 total=1300674 bad=0
v=31 total=1287690 bad=0
```

The census certifies a cut property only. The transfer proofs work for
every short matching realizing the holes, without enumerating matchings.
They also handle the exceptional root bridge just proved. Therefore
A6 implies the original eight-hole statement for **all free targets**.

### 7. Exact residual covered-target obligation

Define **R8-covered** as follows. For every $M\subseteq E(Q_6)$ with
holes $\{0\}\cup Z\cup W$, where $Z$ consists of three distinct nonzero
even vertices, $W$ consists of four odd vertices, and $Z\cup W$ is
independent, and every odd **covered** target $v\notin W$, assume that
for every coordinate $i$, the counts in the face containing $v$ obey

$$
(a_i,b_i)\in\mathcal B
 =\{(0,0),(0,3),(0,4),(1,0),(1,4),
       (2,0),(2,1),(3,0),(3,1),(3,2),(3,4)\}.
$$

Then require a Hamilton $0$--$v$ path containing $M$.
One may additionally assume that $M$ uses all six directions; the
five-direction theorem already handles the others.

The set $\mathcal B$ is the exact complement of the nine good rows
inside $\{0,1,2,3\}\times\{0,1,2,3,4\}$. Thus every eight-hole input
is covered by exactly the following exhaustive decision:

- a nonroot adjacent hole pair: six-hole reduction;
- a free target: Section 6;
- a covered target with at least one good cut: Sections 3--5;
- a covered target with no good cut: R8-covered.

Consequently A6 plus R8-covered suffices for full eight-hole P6. Conversely,
full eight-hole P6 implies R8-covered just by specialization. This is
the claimed exact additional obligation for this reduction scheme;
it is not a proof that R8-covered is logically independent of A6.

### 8. Realizable obstruction to completeness of the nine-row transfer

Let $u=0$, $Z=\{6,17,53\}$, $W=\{11,35,41,47\}$, and $v=4$.
The six rows $(a_i,b_i)$, in bit order $i=0,\ldots,5$, are

$$ (1,0),(2,1),(2,1),(3,1),(1,4),(2,1). $$

All belong to $\mathcal B$, and $Z\cup W$ is independent. These holes
are realized by the following short 28-edge matching (each pair has
Hamming distance one):

```
(3,1) (5,4) (9,13) (10,2) (12,14) (15,31) (18,16)
(20,21) (23,22) (24,26) (27,19) (29,25) (30,28) (33,49)
(34,32) (36,38) (39,7) (40,8) (43,42) (45,37) (46,44)
(48,50) (51,55) (54,52) (57,56) (58,59) (60,61) (63,62)
```

Thus it would be false to say that the nine-row cut argument by itself
covers all eight-hole inputs. This is an obstruction to that argument,
not a counterexample to P6 or to the possible sufficiency of A6.

## Corrections or missing assumptions

A6 is still open. R8-covered is not proved here. The available proofs
establish full free-target coverage conditional on A6 and a precise
nonempty residual for covered targets; they do not establish an A6-only
reduction for every covered target.

## Open risks

- This is an unaudited draft; the complete geometry certificate needs an
  independent domain-coverage and implementation review.
- Imported closure results retain their documented assurance scope.
- Eight-hole closure would still leave the 10--18-hole levels of P6.

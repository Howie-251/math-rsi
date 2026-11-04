# Q5 A8 proof package: three complete transfer branches and five residual orbits

Date: 2026-11-01. ARIS proof-writer output; independent review pending.

## Claim

Let $F$ be any matching of the complete graph on $V(Q_5)$ with exactly
eight holes, three of one parity and five of the other. For every specified
hole $v$ in the larger class, there is a simple cycle on exactly
$V(Q_5)\setminus\{v\}$ containing $F$, with every edge outside $F$ short.
Required edges may be arbitrary long edges and may join equal parities.

## Status

**NOT CURRENTLY JUSTIFIED.** The original statement is unchanged. This
package proves the augmentation branch and every instance admitting a
coordinate cut of imbalance $1,2,$ or $3$. A complete census reduces the
remaining hole geometries to five explicitly listed orbits; their arbitrary
matching instances remain open. No failed search is presented as a
counterexample, and no sampled success is used to assert a universal claim.

## Assumptions and dependency map

1. Q5 A6, established in `A6_CLOSURE_DRAFT.md` and its closure reviews.
2. GQ4-avoid and GQ4-cycle in `Q4_GENERAL_AUGMENTATION.md`, for arbitrary
   hole counts of imbalance two and zero, respectively.
3. The four-hole optional edge bounds O15 and O18 in Section 2 of
   `A6_CLOSURE_DRAFT.md`, with their certified finite inputs.
4. The residual geometry census is the new independent deterministic
   program `A8_geometry_census.py`. It enumerates hole sets only, never
   matching instances. Its output is `A8_geometry_census.json`.

Items 1--3 are imported results, not new assumptions on $F$. The partial
proof below uses no Q5 A8/A10, higher-hole P6 claim, or Q5 T15 result.

## Notation and proof strategy

Call majority parity $O$ and minority parity $E$; these are labels, not
fixed numerical parities. For a coordinate cut let $A$ contain $v$ and
$B$ be the other face. Write $F_A,F_B$ for the internal matching edges,
$C$ for the crossing matching, $c=|C|$, and $X_A,X_B$ for its endpoint
sets. Let $H_A,H_B$ be the original holes, and set
$\delta=|H_A\cap O|-|H_A\cap E|$. For $t\in A$, write $\bar t$ for its
short mirror in $B$, which need not be its required partner.

We add short edges between opposite-parity holes when possible. Otherwise
we use a face cycle or a face path, remove an artificial matching, attach
the original crossings and selected short bridges, and compress the resulting
paths into a matching on the opposite face.

## Proof

### Step 1. Augmentation and a local geometric fact

If a minority hole is short-adjacent to a majority hole other than $v$,
add that short edge. The augmented matching has two minority and four
majority holes and still has $v$ free. Q5 A6 gives the desired cycle;
the added edge is short relative to the original matching. Hence we may
assume

$$E\cap H\text{ has no short edge to }(O\cap H)\setminus\{v\}.\tag{I}$$

In $Q_4$, any two distinct same-parity vertices have at least six distinct
neighbors: at distance two they have two common neighbors, and at distance
four none. Therefore two such vertices cannot simultaneously avoid three
vertices of the other parity. We use this fact in each face with its
global parity labels.

The identity $2|F_A|+c=16-|H_A|$ determines the parity of $c$.

### Step 2. Transfer conventions

If a cycle contains a nonempty matching $D$, deleting $D$ leaves a path
forest with endpoint set $V(D)$. Restoring any proper subset of these
removed edges, possibly as internally disjoint paths, leaves a path
forest: otherwise the restored subset and the undeleted part of the
original cycle would contain a cycle while an edge of the original
cycle remained missing. Thus no component closes prematurely in the
constructions below.

Compressing disjoint paths to edges gives a matching on their endpoints.
If a cycle on the other face contains this matching and avoids its
internal vertices, expansion gives one simple cycle. This preserves all
required edges, and the only newly added edges outside artificial paths
are short edges. Any artificial edge is deleted or expanded.

### Step 3. All cuts with $\delta=2$

Here $c$ is even. If $c>0$, choose any perfect matching $D$ on $X_A$.
The holes of $F_A\cup D$ are exactly $H_A$, of majority excess two.
GQ4-avoid gives an $A-v$ cycle containing it. Delete $D$, attach every
edge of $C$, and compress to $R$ on $X_B$. The matching $F_B\cup R$
has holes exactly $H_B$, which are balanced because the total excess
is two. GQ4-cycle gives its full $B$ cycle, and expansion finishes.

Suppose $c=0$, and put $k=|H_A\cap E|$. The hole counts in $A$ are
$(k,k+2)$ and in $B$ are $(3-k,3-k)$. If $k=0$, the $B$ face has three
minority and three nonforbidden majority holes, contradicting (I) and
the two-versus-three geometric fact. If $k\ge2$, $A$ has two minority
holes and at least three majority holes other than $v$, with the same
contradiction. Consequently $k=1$. The $A$ holes have counts $(1,3)$,
and the $B$ holes $(2,2)$. O15 supplies at least 15 short optional
edges among the extending $A-v$ cycles; O18 supplies at least 18 among
the full extending $B$ cycles. Under the mirror identification both
unions lie in the 32 edges of $Q_4$. Their intersection is nonempty,
since $15+18>32$. Choose corresponding optional edges in two witnessing
cycles, delete these two edges, and join their corresponding endpoints
by two short edges across the cut. The result is the required single
cycle. The optional edge union argument asserts the existence of
separate witnessing cycles for the chosen edge; it does not prescribe
many optional edges simultaneously.

### Step 4. All cuts with $\delta=3$

The crossing number $c$ is odd and positive. There are at least two
nonforbidden majority holes in $A$. Choose one, $t$, whose mirror
$w=\bar t$ is not the unique $B$ port when $c=1$; two candidates ensure
this choice exists. For $c\ge3$ choose any such hole. By (I), $w$ is
covered in the original matching, and has minority parity.

Choose a perfect matching $D$ on $X_A\cup\{t\}$. Adding $D$ reduces
the majority excess in the remaining $A$ holes from three to two, so
GQ4-avoid gives an $A-v$ cycle. If $w$ is a port, prescribe $tx\in D$,
where $x$ is the original $A$ partner of $w$; this is possible because
$t$ is a hole and $x$ is a port.

If $w$ is internal to $F_B$, delete $D$, attach $C$ and the bridge $tw$,
and compress to $R$ on $X_B\cup\{w\}$. Let $wk\in F_B$ and $wq\in R$.
Suppress these two edges into $kq$. All other edges remain disjoint,
and the holes of the resulting matching are $H_B\cup\{w\}$. The original
$B$ majority excess is $2-3=-1$; adding the minority hole $w$ gives
excess $-2$. GQ4-avoid therefore applies with minority parity as the
larger class and avoids $w$. Expand $kq$ via $kw$ and the transferred
path; expand every other compressed edge.

If $w$ is a port, then $c\ge3$ by the choice for $c=1$, and $|D|\ge2$.
Delete $D$. The endpoints $t,x$ of its prescribed edge lie in different
path components. Attaching $tw,xw$ restores just that gap through $w$;
at least one other gap remains. Attach all other crossings. Compress
the resulting forest onto $X_B\setminus\{w\}$; its interiors contain
$A-v$ and $w$. Together with $F_B$ this is a matching whose holes are
$H_B\cup\{w\}$, again of excess $-2$. Apply GQ4-avoid avoiding $w$
and expand. This also gives the required cycle.

### Step 5. All cuts with $\delta=1$

Put $k=|H_A\cap E|$, so $|H_A\cap O|=k+1$. If $k=0$ or $1$, the
$B$ hole counts are $(3-k,4-k)$, containing two minority and three
majority holes, none equal to $v$. This contradicts (I). Hence $k\ge2$.
The crossing number $c$ is odd and positive.

Choose a minority hole $y\in A$. When $c=1$, choose $y$ whose mirror
$w=\bar y$ is not the unique $B$ port; at least two choices of $y$ exist.
For $c\ge3$ any $y$ may be used. By (I), $w$ is covered and has
majority parity. Select a root port $d\in X_A$ and a perfect matching
$D$ on $X_A\setminus\{d\}$. The matching

$$F_A\cup D\cup\{dy\}$$

has original holes $H_A\setminus\{y\}$ of majority excess two and
contains the free forbidden hole $v$. GQ4-avoid supplies an $A-v$
cycle containing $dy$; deleting $dy$ gives an $A-v$ path from $d$ to $y$.

If $w$ is internal to $F_B$, delete $D$ from the path, attach all
crossings and $yw$, compress, and suppress the unique overlap $w$ as
in Step 4. The resulting matching has holes $H_B\cup\{w\}$. The original
$B$ excess is one; adding majority hole $w$ gives excess two.
GQ4-avoid avoiding $w$ and expansion complete the cycle.

If $w$ is a port, $c\ge3$. Choose $d$ to be its original crossing
partner. Then $D$ is nonempty. Deleting $D$ from the $d$--$y$ path
separates its endpoints into different components, since at least one
edge of that path was removed. Attach $dw,yw$ and the other crossings;
the two endpoint components join through $w$ without closing a cycle.
Compress onto $X_B\setminus\{w\}$ and apply GQ4-avoid to the matching
with holes $H_B\cup\{w\}$, avoiding $w$. Expansion finishes.

In particular the exceptional $k=c=1$ endpoint lemma required in the
A6 proof never arises in A8. No new finite endpoint input is needed.

### Step 6. Exact remaining geometric obligation

Translate $v$ to $0$; this makes the majority parity the numerical even
parity. Let $Z$ be the four other even holes and $W$ the three odd holes.
Condition (I) says every $z\in Z$ is nonadjacent to every $w\in W$.
There are only $\binom{15}{4}$ possibilities for $Z$. For each one the
program lists all odd vertices nonadjacent to $Z$ and all their triples
$W$. This gives exactly 2700 configurations. For coordinate $i$, the
face containing $0$ is its zero face, and the program directly computes

$$\delta_i=1+|\{z\in Z:z_i=0\}|-|\{w\in W:w_i=0\}|.$$

Exactly 2540 configurations have some $\delta_i\in\{1,2,3\}$ and are
proved by Steps 3--5. For every other configuration the program takes
the lexicographically smallest pair $(\pi Z,\pi W)$ over all 120
coordinate permutations. The remaining 160 configurations have exactly
the following five representatives:

| $Z$ | $W$ | orbit size | ordered $(\delta_0,\ldots,\delta_4)$ at this representative |
|---|---|---:|---|
| $3,5,6,15$ | $8,25,26$ | 60 | $0,0,-1,4,4$ |
| $3,5,6,15$ | $25,26,28$ | 20 | $0,0,0,4,5$ |
| $3,5,15,23$ | $25,26,28$ | 30 | $-1,0,0,4,4$ |
| $15,23,27,29$ | $1,2,4$ | 30 | $-1,0,0,-1,-1$ |
| $15,23,27,29$ | $2,4,8$ | 20 | $-2,0,0,0,-1$ |

The census output includes every residual member and its computed
deltas, so both coverage and orbit membership are inspectable. Orbit
sizes sum to 160. The normalization preserves arbitrary matching edges,
the specified forbidden hole, and shortness. The enumerated domain is
therefore a complete geometry reduction, not a finite test of selected
matching instances.

## Corrections or missing assumptions

To prove the original A8 claim it suffices to prove it for every arbitrary
matching on the 24 covered vertices in each of the five rows. No matching
condition may be silently imposed in that residual theorem.

## Open risks

The five residual rows remain open. Delta-zero and delta-four double-bridge
transfers can leave a Q4 T15 instance with its genuine triangle obstruction;
the existence of Q4 T15 positive cases does not remove this obstruction.
The separate `A8_DOUBLE_BRIDGE_SUFFICIENT.md` proves a sufficient mechanism
to avoid it in many matching instances, without asserting complete coverage.
No full A8 or full higher-hole P6 closure is claimed by this package.

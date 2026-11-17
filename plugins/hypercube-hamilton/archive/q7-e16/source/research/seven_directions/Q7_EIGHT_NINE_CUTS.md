# Seven-dimensional eight-hole nine-cut transfer theorem

Date: 2026-11-02. ARIS proof-writer. Complete proof draft; independent review pending.

## Exact claim and scope

Let $M\subseteq E(Q_7)$ be a short matching with eight holes, $u$ a free root,
and $v$ of opposite parity, free or covered. Normalize $u=0$. Write the other
even holes as $Z$ (three vertices), and the four odd holes as $W$.
The required Hamilton $u$–$v$ path exists if any of the following holds:

1. Two vertices of $Z\cup W$ are adjacent.
2. $v\in W$ and $uv$ is short.
3. A direction has no edge of $M$.
4. In some coordinate face $A$ containing $v$, the pair
   $(a,b)=(|Z\cap A|,|W\cap A|)$ lies in
   $$\mathcal G=\{(0,1),(0,2),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3)\}.$$

No claim is made that these conditions exhaust free or covered targets.
In Q7, both residual domains must be addressed separately.

## Inputs and notation

- Full Q7 six-hole path theorem: `Q7_SIX_HOLE_CLOSURE.md` and its transfer
  appendix, accepted in `Q7_SIX_HOLE_REVIEW.json`.
- Zero-crossing Z7: `ZERO_CROSSING_PATHS.md`, accepted in `ZERO_CROSSING_REVIEW.json`.
- Six-dimensional A4 and balanced four-hole paths/circles K4 (=B2/C2):
  `A4_FULL_CLOSURE.md`, `A4_FULL_REVIEW.json`.
- Six-dimensional A6 (two minority and four majority holes; any marked
  majority omission): `A6_FINAL_REDUCTION.md`, `A6_FULL_REVIEW.json`.
  All local matchings here are arbitrary edges of $K(Q_6)$, not only short edges.
- N10: any two-hole matching on $K(Q_6)$ with free holes $r,s$ has a Hamilton
  path from $r$ to any $y\ne r$ of the parity of $s$. N14: two same-parity
  holes admit a cycle omitting either hole. These are the general-dimensional
  literature corollaries recorded in `PROOF_PACKAGE.md` and the six-hole proof.
  A balanced two-hole circle follows by taking a short-neighbor target in N10
  and closing the path. Zero-hole circles use the perfect-matching theorem.

Put $B=Q_7-A$, $\delta=\boldsymbol1[u\in A]$. Original holes in $A,B$ are
$(a+\delta,b)$ and $(4-a-\delta,4-b)$ in even/odd order. Internal original
matchings are $M_A,M_B$; crossing edges form $C$ with endpoints $X_A,X_B$;
$c=|C|$. Every artificial edge is removed or expanded. Only new short edges
survive in the final Q7 path.

## Proof

### 1. General local endpoint lemma

For a vertex $x$, write $\epsilon(x)=1$ for even and $-1$ for odd. Let
$F\subseteq K(Q_6)$ have $2t$ holes, $1\le t\le3$, with even-minus-odd
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
ends is not already in a path on 64 vertices. All these statements allow
arbitrary required matching edges, so they apply to compressed transfers.

### 2. Preprocessing and forest bookkeeping

If any two vertices of $Z\cup W$ are adjacent, add their short edge to
$M$. This preserves the free root and yields six holes. Full six-hole Q7 theorem
solves the original endpoint problem. Hence assume $Z\cup W$ independent.

If $v\in W$ and $uv$ is short, add $uv$ to $M$ and apply six-hole Q7 theorem to
obtain a full circle containing this enlarged matching: use any remaining
free root, a short neighbor as its target, and close the Hamilton path.
Delete $uv$. Thus in the free-target census $d(u,v)$ is 3, 5, or 7.

If $c=0$ for any selected cut, all original matching edges use at most
six directions. The proved zero-crossing theorem Z7 solves the original
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

### 6. Exceptional free-target root bridge

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


## Exact remaining obligation

After the first three reductions, one may assume $Z\cup W$ independent,
all seven directions used, and, if $v$ is free, $d(0,v)\in\{3,5,7\}$.
The cut complement is
$$\mathcal B=\{(0,0),(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),
 (3,0),(3,1),(3,2),(3,4)\}.$$
The remaining obligation is the original Hamilton path assertion for **every**
such matching and every free or covered target for which every coordinate
gives a pair in $\mathcal B$. This is an exact logical partition, not a proof
of either residual domain. Realizable free-target residual examples occur in
`Q7_EIGHT_CUT_OBSTRUCTION_WITNESSES.json`.

The earlier Q6 free-target geometric exhaustion is not imported: its
dimension-dependent coverage fails in Q7. Local transfer formulas above are
given in full; no lower-dimensional finite census is used in this theorem.

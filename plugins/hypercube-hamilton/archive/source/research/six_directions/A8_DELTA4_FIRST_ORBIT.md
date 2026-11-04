# A8: delta-four transfer with one minority hole in the target face

Date: 2026-11-01. ARIS proof-writer draft. Independent review pending.

## Claim

Let $F$ be an arbitrary matching of $K(Q_5)$ with three minority and five
majority holes, and let $v$ be a specified majority hole. Assume no minority
hole is short-adjacent to any other majority hole. If a coordinate face
$A$ containing $v$ contains all five majority holes and exactly one minority
hole, then $F$ extends to a simple cycle on exactly $Q_5-v$ using only short
new edges.

## Status

**PROVABLE AS STATED**, relative to GQ4-avoid and Q4 T44. This closes the
first residual orbit of `A8_PARTIAL_PROOF_PACKAGE.md`; it does not close
the four other residual orbits or full A8.

## Assumptions, notation, and dependency map

Use the global majority/minority parity labels on both faces. Write $B$
for the other face, $C$ for the original crossing matching, $c=|C|$, and
$X_A,X_B$ for its endpoint sets. The internal matchings are $F_A,F_B$.
For $t\in A$ its short mirror in $B$ is $\bar t$.

The imported results are GQ4-avoid in `Q4_GENERAL_AUGMENTATION.md` and
T44 in `Q4_TWO_AVOIDED_TRANSFER.md`, with their prior audit packages.
GQ4-avoid supplies the $A-v$ cycle after two bridges are prepared.
T44 supplies the cycle on $B$ avoiding the two bridge vertices after
compression. The path-forest argument below justifies all compression.

## Proof strategy

Two of the four available majority holes in $A$ provide short bridges.
They are chosen so that an artificial matching can encode every forced
joining at a bridge vertex while leaving at least one unfilled gap in the
$A$ cycle. The remaining $A$ holes have imbalance two; the remaining $B$
matching has four same-parity holes and two prescribed avoided holes.

## Proof

### Step 1. Choice of the two bridges

There are four candidate majority holes in $A$ other than $v$. Their
mirrors are distinct minority-parity vertices in $B$. None is an original
hole: the only original $B$ holes are two minority holes, and a minority
hole cannot be adjacent to a nonforbidden majority hole under the stated
nonadjacency assumption. Thus all four mirrors are covered. Also $c$ is
even because $A$ has six original holes and
$2|F_A|+c=16-6=10$.

Choose candidates $t,s$ with mirrors $w=\bar t,z=\bar s$ as follows.

* If both internal vertices and ports occur among the four mirrors,
  choose one of each. Then $c\ge2$ and exactly one selected mirror is a port.
* If all four mirrors are internal to $F_B$, choose two not paired by
  $F_B$. Such a choice exists because a matching on four vertices has
  at most two edges, whereas there are six pairs.
* If all four mirrors are ports, then $c\ge4$. Choose any two of them.

These three alternatives exhaust the possibilities. In particular the
case of two mirror ports with $c=2$ belongs to the first alternative,
where a port and an internal vertex are chosen.

### Step 2. An artificial matching in the target face

Let $T=X_A\cup\{t,s\}$. For each chosen mirror that is a port, prescribe
in a matching $D$ the edge joining its hole $t$ or $s$ to that port's
original crossing partner in $X_A$. These prescriptions are disjoint.
Complete them to a perfect matching $D$ on $T$, which has even size
$c+2$. Put $d=|D|=(c+2)/2$, and let $p$ be the number of selected mirrors
that are ports. In the three alternatives of Step 1, respectively,

$$ (p,d)=(1,d\ge2),\quad(0,d\ge1),\quad(2,d\ge3). $$

In every alternative $d>p$. The holes of $F_A\cup D$ are the original
six $A$ holes with $t,s$ removed, namely one minority hole and three
majority holes including $v$. GQ4-avoid gives an $A-v$ cycle $K$
containing $F_A\cup D$.

### Step 3. Compression and the absence of a closed component

Delete $D$ from $K$, attach all original crossings, and attach the short
bridges $tw,sz$. At each selected port mirror the two incident edges
join the endpoints of its prescribed edge of $D$ by a two-edge path.
This restores exactly $p$ of the $d$ removed gaps. Since $p<d$, the
result is a path forest. Its interiors include $A-v$ and each selected
mirror that is a port. Its endpoints consist of all other $B$ ports
and the selected mirrors that are internal to $F_B$.

Compress this forest to an endpoint matching $R$. Consider $F_B\cup R$.
The only vertices where these two matchings overlap are the selected
internal mirrors, at most two vertices. If exactly one mirror is
internal, a closed component cannot exist: every other vertex has degree
at most one. If neither is internal, the union is already a matching.
If both are internal, a closed component would have to alternate
between $F_B$ and $R$ using only the two degree-two vertices $w,z$.
It would require $wz\in F_B$ and $wz\in R$. Step 1 chose
$wz\notin F_B$, so this is impossible.

Suppress every selected internal mirror along its path component in
$F_B\cup R$. The resulting graph $L$ is therefore a matching of $K(B)$.
Its holes are exactly the two original $B$ holes together with $w,z$.
All four have minority parity.

### Step 4. Completion in the other face

T44 supplies a simple cycle on exactly $B\setminus\{w,z\}$ containing
$L$, with all other edges short. Undo all suppressions and compressed
paths. The two avoided mirror vertices are restored exactly once: an
internal mirror lies on its suppressed path, and a port mirror lies in
the transferred path forest. All vertices of $A-v$ are also restored
exactly once. The expanded cycle has vertex set $Q_5-v$, contains every
edge of $F_A,F_B,C$, and its new edges are short. This proves the claim.

### Step 5. Application to the first residual orbit

The first representative in `A8_geometry_census.json` has

$$v=0,\quad Z=\{3,5,6,15\},\quad W=\{8,25,26\}.$$

Here majority parity is numerical even parity. Cut at coordinate $4$
(the bit of value $16$) and take its zero face as $A$. All five majority
holes lie in $A$, and the only minority hole in $A$ is $8$; the other
minority holes $25,26$ lie in $B$. This is exactly the proved condition.
Coordinate permutations preserve the condition and transfer the whole
arbitrary matching, so all 60 geometries in this orbit are covered.

## Corrections or missing assumptions

None for the stated claim. The nonadjacency hypothesis is the residual
hypothesis after short-edge augmentation to A6; it is explicitly assumed
here and guarantees the bridges end at covered vertices.

## Open risks

This is a new proof awaiting independent review. Combined with the three
cut branches, it leaves four residual orbits of sizes $20,30,30,20$,
totaling 100 normalized hole geometries. It asserts no closure of their
matching instances, of full A8, or of any full higher-hole P6 layer.

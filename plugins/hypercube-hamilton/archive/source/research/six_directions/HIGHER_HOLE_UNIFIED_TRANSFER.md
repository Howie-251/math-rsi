# A uniform cut transfer for the remaining P6 layers

2026-11-01. ARIS proof-writer. Proposed proof relative to explicit imports;
independent review pending. Full P6 and the 10--18-hole layers remain open.

## Claim, assumptions, and notation

Let $M$ be a short matching in $Q_6$ with $2k$ holes, let $u$ be a free
even root, and let $v$ be any odd target, covered or free. Write the holes
as $\{u\}\cup Z\cup W$, where $|Z|=k-1$, $|W|=k$, all members of $Z$
are even and all members of $W$ are odd. Assume $Z\cup W$ is independent.
This assumption is a legitimate induction reduction only after the
$(2k-2)$-hole theorem is available; it is not currently a proof of that
predecessor theorem for $k\ge6$.

Choose a coordinate cut $A,B$ with $v\in A$. Put
$a=|Z\cap A|$, $b=|W\cap A|$, and $\delta=1$ if $u\in A$, otherwise $0$.
Let $C$ be the original crossing matching, $c=|C|$, $X_A,X_B$ its port sets,
and $M_A,M_B$ the internal matching restrictions. The mirror of a vertex
across this coordinate is denoted by $\bar x$.

Import the established five-direction free-root endpoint theorem for $c=0$.
For $c>0$, import the full $Q_5$ local endpoint lemma for arbitrary complete-
graph matchings with balanced $2,4,6$ holes: any free even root and any odd
target have a spanning path containing the matching with only short new
edges. Import full-cycle extensions for balanced $0,2,4,6$ holes; omit-one
extensions for hole counts $(j,j+2)$, $j=0,1,2$, at every specified majority
hole; and T44_5 for four same-parity holes, omitting any specified two.
These are the accepted A6/N14/A4, perfect-matching, and T44_5 consequences
in `EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md` Section 1 and the final
reviews cited by `EIGHT_HOLE_FULL_CLOSURE.md`. No higher-hole P6 theorem
is imported.

The following transfer is conditional on the exact B-side cycle theorem
specified below. In the corollary table all its local inputs are already
proved, so those cut classes are unconditional relative to the imports.

## 1. Excess even holes in A

Suppose $1\le b\le3$ and $s=a+1-b\ge0$. Choose any $s$ members $S$ of
$Z\cap A$; this is possible because $b\ge1$. The desired B-side input is
the cycle-extension theorem for hole counts

$$ (k-a-1,\ k-b+s), $$

omitting exactly the $s$ odd holes $Y=\{\bar x:x\in S\}$.
This input must hold for the actual marked hole geometry and **every**
arbitrary complete-graph matching on its complement.

If $\delta=1$, pair $X_A\cup S$ arbitrarily into a matching $D$ and take
$r=u$. The holes of $M_A+D$ are $(b,b)$ and include $r$.
Indeed $c+s$ is even, since $c\equiv a+1+b\pmod2$.

If $\delta=0$ and $s\ge1$, choose $r\in S$ and pair
$X_A\cup(S\setminus\{r\})$ into $D$. Its cardinality is even since
$c\equiv a+b\pmod2$. The holes are again $(b,b)$ and include $r$.
There is no requirement for an even crossing port in this case.

If $\delta=0$ and $s=0$, then $b=a+1$. Shortness of $M_A$ gives
$|X_A\cap E|-|X_A\cap O|=b-a=1$. Choose an even port $r$ and pair
$X_A\setminus\{r\}$ into $D$. The completed holes are $(b,b)$.

Use the imported endpoint theorem for a spanning $r$--$v$ path in A.
Delete $D$, attach every original crossing edge, and attach the short
bridges $x\bar x$ for all $x\in S$. If $r\in S$, its bridge makes it
an interior vertex; if $r\in X_A$, its original crossing edge does so.
If $r=u$, it remains the true global endpoint. The other endpoint is $v$.
This remains true when $v$ is a crossing port or a free vertex.

Every $y\in Y$ is internally covered by $M_B$: independence excludes an
original odd hole at $y$, its even mirror $x$ is free so it is not a
crossing port, and $y\ne u$ by parity. The bridges are mutually distinct.

## 2. Excess odd holes in A

Suppose $0\le a\le2$ and $t=b-a-1\ge1$. Choose a set $S\subset W\cap A$
of size $t$ that excludes $v$ (if free) and excludes the vertex $\bar u$
(if it lies in A). This existence is an explicit hypothesis of this branch.
It always holds for covered targets, since $b-t=a+1\ge1$; it also always
holds for free targets when $a\ge1$, since at most two vertices are excluded.

The required B-side cycle input has hole counts

$$ (k-a-1+t,\ k-b), $$

and omits exactly the $t$ even holes $Y=\{\bar x:x\in S\}$.

For $\delta=1$, take $r=u$ and pair $X_A\cup S$ into $D$.
For $\delta=0$, the port difference is $b-a=t+1>0$, so choose an even
port $r$ and pair $(X_A\setminus\{r\})\cup S$ into $D$.
The parity identities above show these sets have even size. The holes
of $M_A+D$ are $(a+1,a+1)$; $r$ is free, and $v$ remains a legal odd
target. Apply the local endpoint theorem, delete $D$, and attach crossings
and all bridges at $S$ as in Section 1.

Each $y\in Y$ is internally covered by $M_B$: independence excludes $Z$,
the choice of $S$ excludes $u$, and a free mirror excludes crossing ports.
All bridge conflicts now have even parity.

## 3. Tagged closure and simultaneous conflict compression

In both branches all A vertices have their intended final degrees. Deleting
$D$ from one A path leaves a path forest; all attachments are at distinct
B vertices. If $u\in A$, $D$ is nonempty ($c>0$, and the pairing set has
positive even size), so the two true endpoint segments are distinct.
If $u\in B$, it has not been attached. Add a tagged artificial edge $uv$.
For $u\in A$ this joins the two different terminal segments; for $u\in B$
it extends the single terminal segment to $u$. The result remains a forest.
Compress all A-interior paths into a matching $T$ on distinct B endpoints.
Exactly one edge of $T$ carries the tag.

The only degree conflicts in $T\cup M_B$ occur at $Y$. Each $y\in Y$
has a distinct original mate $h_y$ of the opposite parity. Every $h_y$ is
outside the endpoints of $T$: it is internally covered, is not a crossing
port or the free root, and cannot be in the same-parity set $Y$. Thus the
conflict components are paths, each with an original pendant endpoint
$h_y$; they cannot be cycles. Suppress every $y\in Y$ in these components,
recording the paths and any tag, to obtain an arbitrary matching $L$ on B.

The endpoints of $T$ are exactly $X_B\cup Y$ and additionally $u$ when
$u\in B$. Consequently the holes of $L$ are precisely

$$ (H_B\setminus\{u\})\cup Y, $$

where $u$ is removed only when it belongs to B. These give the counts in
Sections 1--2. Applying the specified B theorem produces a single cycle
on $B\setminus Y$ containing $L$. Expand each suppressed conflict path,
then each transferred A path. The result is one spanning cycle on $Q_6$
containing the tag and every original matching edge. Delete the tagged
$uv$ edge to obtain the required Hamilton $u$--$v$ path. All remaining
new edges are short: artificial completion edges were deleted, and all
compressed edges were expanded. This proves the conditional transfer.

## 4. Already available cut classes for ten and twelve holes

The following rows work for **both free and covered** odd targets.
All odd-consumption rows have $a\ge1$, so their selection condition holds.
The zero-crossing case is handled by the five-direction import.

| total holes | $(a,b)$ | A balanced holes | B hole counts; omitted holes | input |
|---:|---|---:|---|---|
|10|(1,2)|(2,2)|(3,3); none|balanced six-hole cycle|
|10|(2,3)|(3,3)|(2,2); none|balanced four-hole cycle|
|10|(2,2)|(2,2)|(2,4); one odd|A6|
|10|(3,3)|(3,3)|(1,3); one odd|A4|
|10|(1,3)|(2,2)|(4,2); one even|A6 reversed|
|10|(2,4)|(3,3)|(3,1); one even|A4 reversed|
|10|(4,3)|(3,3)|(0,4); two odd|T44_5|
|10|(2,5)|(3,3)|(4,0); two even|T44_5 reversed|
|12|(2,3)|(3,3)|(3,3); none|balanced six-hole cycle|
|12|(3,3)|(3,3)|(2,4); one odd|A6|
|12|(2,4)|(3,3)|(4,2); one even|A6 reversed|

The marked T15 cases provide further **conditional geometric** entries:
ten holes $(3,2)$ or $(1,4)$, and twelve holes $(4,3)$ or $(2,5)$.
Their A hole counts are respectively $(2,2)$ or $(3,3)$ and the B counts
are $(1,5)$ or $(5,1)$, omitting two majority holes. Only the already
audited marked T15 geometries may be used; unrestricted T15 is not proved.

## 5. Remaining obligations and scope

No assertion is made that every ten- or twelve-hole geometry has a row
in this table. A complete census must account for all free/covered targets,
and any further T15 use must track the actual marked omissions. For 14--18
holes this particular table supplies no complete route. The original full
P6 objective is unchanged, and the proven eight-hole package is not edited.

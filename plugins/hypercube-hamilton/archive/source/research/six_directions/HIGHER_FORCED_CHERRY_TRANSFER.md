# Uniform transfer through one or several forced cherries

2026-11-01. ARIS proof-writer candidate. Status: **PROVABLE AS STATED
relative to the explicit local inputs below**; fresh independent review is
required. This is a sufficient-route theorem, not a closure of any higher
hole layer or unrestricted local geometry.

## Claim and assumptions

Let $M$ be any short matching in $Q_6$ with holes
$H=\{u\}\cup Z\cup W$, where $u$ is even and free,
$|Z|=k-1$, $|W|=k$, $Z$ is even, $W$ is odd, and $Z\cup W$ is independent.
Let $v$ be any odd target, covered or free. Choose a coordinate cut $A,B$
with $v\in A$; put $a=|Z\cap A|$, $b=|W\cap A|$,
$\delta=\mathbf1[u\in A]$. Let $C$ be the original crossing matching,
$c=|C|$, and $X_A,X_B$ its port sets.

Consider either of the following branches with $s\ge3$:

* **Even consumption:** $b\ge1$, $s=a+1-b$, and choose any
  $S\subset Z\cap A$ of size $s$.
* **Odd consumption:** $s=b-a-1$, and choose
  $S\subset(W\cap A)\setminus\{v,\bar u\}$ of size $s$.
  The exclusion of $v$ matters only when $v$ is free, and that of $\bar u$
  only when $u\in B$. Existence of this precise $S$ is a hypothesis.

Here $\bar x$ means the mirror across the cut and $Y=\{\bar x:x\in S\}$.
The intended B matching has hole set
$H_*=(H\cap B)\setminus\{u\}\ \cup Y$ and covered set $K=B\setminus H_*$.
In even consumption its hole counts (global even,odd) are
$(k-a-1,k-b+s)$; in odd consumption they are
$(k-a-1+s,k-b)$. It must admit a local cycle on precisely $B\setminus Y$.

**Single-cherry hypothesis.** Suppose $p,q\in K$ are distinct, have the
same global parity as $Y$, and $u\notin\{p,q\}$. Suppose the actual marked
B geometry has the local classification: for every arbitrary perfect
matching $F$ on $K$, it has a cycle on $B\setminus Y$ containing $F$,
with only short new edges, if and only if $pq\notin F$.
Then $M$ has a Hamilton $u$--$v$ extension with only short new edges.

This statement holds for every feasible $k$, in particular $k=6,7,8,9$
(twelve through eighteen holes); it does not supply the assumed marked
local classification or the existence of a useful cut.

The multi-cherry version and a precise rank criterion supplying its local
classification are proved in Sections5--6. All graph unions retain edge
labels: a common matching pair is a two-edge cycle, not a single edge.

## Imports and strategy

Import the accepted balanced-hole Q5 endpoint theorem for arbitrary
complete-graph matching edges and every feasible balanced hole count:
any free root and opposite-parity covered or free target have a Hamilton
path through that matching, with only short new edges. The full A10
assembly and `Q5_A10_FULL_REVIEW.json` accept the consequences of
`Q5_HIGHER_HOLE_REDUCTION.md`, together with full A8 and the named earlier
inputs. Thus the old uniform transfer's small balanced-hole range need
not restrict $a,b$ here. Global parity is restricted to a face; choosing
face coordinates may reverse both parity names, which the import allows.

Import the established five-direction free-root endpoint theorem for
$c=0$, exactly as in `HIGHER_HOLE_UNIFIED_TRANSFER.md`.
For $c>0$ we prove the forest construction directly. Its degree accounting,
tag and simultaneous suppression agree with that accepted uniform
transfer. The single-cherry avoidance extends the accepted
`Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md`; that frozen text is not modified.

Dependency map: all-balanced Q5 endpoints -> A Hamilton path -> controlled
deletion forest -> actual compressed B matching avoids the local obstruction
-> assumed B classification -> expansion. In Section5 the optional local
input is obtained from independently verified forest ranks and the generic
complete-graph matching-connectivity rank upper bound. No Q6 higher layer
is an input to this proof.

## 1. Legal completions and uniform gap lower bounds

If $c=0$, invoke the explicit five-direction import and finish. Assume
$c>0$. Shortness of the internal matching $M_A$ gives

$$|X_A\cap E|-|X_A\cap O|=b-a-\delta,
\qquad c\equiv a+b+\delta\pmod2.$$

Choose root $r$ and the set $V_D$ to be paired as follows:

| Branch | Root face | $r$ | $V_D$ | A holes after completion |
|---|---|---|---|---|
|even|$\delta=1$|$u$|$X_A\cup S$|$(b,b)$|
|even|$\delta=0$|any member of $S$|$X_A\cup(S\setminus\{r\})$|$(b,b)$|
|odd|$\delta=1$|$u$|$X_A\cup S$|$(a+1,a+1)$|
|odd|$\delta=0$|any even port|$(X_A\setminus\{r\})\cup S$|$(a+1,a+1)$|

For the last row the even-port surplus is $b-a=s+1$, so such a port
exists and $c\ge s+1$. Every $V_D$ has even cardinality by the congruence
above. Its vertices are free for $M_A$, distinct from $r$, and do not
include a free target $v$ by the source exclusions. A covered target can
belong to $V_D$ only when it is a crossing port.

Let $D$ be any perfect pairing of $V_D$ for now, and write $d=|D|$.
When $\delta=1$, $d=(c+s)/2\ge2$ since $c\ge1$, $s\ge3$.
When $\delta=0$, $d=(c+s-1)/2$. In even consumption $c+s-1\ge3$ and is
even, hence $d\ge2$. In odd consumption $c\ge s+1$ gives $d\ge s\ge3$.

The A matching $M_A+D$ has exactly the balanced hole counts in the table,
with $r$ free and even and $v$ an odd legal target. Apply the all-balanced
endpoint import to obtain a simple Hamilton $r$--$v$ path $P_A$ containing
every edge of $M_A+D$. Artificial $D$ edges may be long or same-parity;
all other new local edges are short.

## 2. Actual transfer and suppression

Each $y\in Y$ is originally internally matched in B. Indeed its source
mirror is originally free, so it cannot be a crossing port; independence
of $Z\cup W$ excludes any original nonroot hole at $y$; and $y\ne u$ by
parity in even consumption and the explicit root-mirror exclusion in odd
consumption. Put $h_y=M_B(y)$. These mates are distinct and have parity
opposite to $Y$. Being internally covered, they are not ports or the
root; their parity also puts them outside $Y$.

Delete $D$ from $P_A$, attach every original crossing and all short bridges
$x\bar x$ for $x\in S$, and add tagged edge $uv$. If $u\in A$, one can
equivalently first add $uv$ to $P_A$, obtaining one simple32-cycle, then
delete $D$. Its endpoint edge was not already on $P_A$. Since $d\ge2$,
at least one cycle edge was removed and the result is a forest. If $u\in B$,
start with a path forest; all attachments, including the previously free
root at $v$, are distinct B leaves and create no cycle.

Degree accounting leaves all A vertices with degree two: the missing
degree at $r$ is supplied by its source bridge or crossing when $r\ne u$;
the tag supplies the true endpoint degree at $v$ and at $u$ when $u\in A$.
Each deleted D endpoint receives one attachment. If a covered target is a
port and loses its only A path edge, its crossing and tag restore degree
two. A free target is not in $D$ and keeps its A path edge plus the tag.
Thus compression gives a perfect matching $T$ on
$X_B\cup Y\cup(\{u\}\cap B)$, with exactly one tag-carrying path.

The only degree conflicts in $T+M_B$ are at $Y$, with the distinct pendant
mates $h_y$ described above. A conflict component contains one T edge and
at most one pendant original edge at each endpoint. It cannot be a cycle.
Suppress $Y$ in every such component and carry along the actual paths and
tag. The result is a perfect matching $L$ on $K$, with hole set exactly
$H_*$, including $Y$ as omitted holes. It may have arbitrary long or
same-parity edges; its precise edges, not just $M_B$, must satisfy the B
input.

## 3. One cherry: preventing the actual compressed pair

Both $p,q$ are originally covered: they are outside $H_*$ and $Y$, and
the only original hole removed from $H\cap B$ was $u$, which is excluded.
They have $Y$'s parity. Consequently $pq\notin M_B$ by shortness.

If an obstruction endpoint is not a port, it is not a T endpoint either:
it is outside $Y$ and the root. Its original internal matching edge stays
unchanged. Its opposite-parity mate is not in $Y$, cannot be a port or free
root, and is not the other obstruction endpoint. If a T edge ends in $Y$,
suppression moves that end to $h_y$ of opposite parity, and a Y--Y edge
becomes an edge between two such mates. An edge to $u$ remains incident
with that distinct root. These cases prove

$$pq\in L\ \Longrightarrow\ p,q\in X_B\text{ and }pq\in T.$$

If either vertex is not a port, any legal $D$ therefore works. Otherwise
let $p',q'$ be their actual original A crossing partners and prescribe
$p'q'\in D$. This is legal: in even consumption $r$ is the originally
free root or a source hole, never a port. In odd consumption with
$\delta=0$, the B obstruction endpoints are even, their crossing partners
are odd, and $r$ was chosen even. For $\delta=1$, $r=u$ is originally free.
The prescribed endpoints are distinct from all source holes, so the
remaining even number of vertices in $V_D$ can be paired arbitrarily.

For $\delta=1$, the tagged A cycle loses $p'q'$ and at least one other
D edge. Its direct $p'$--$q'$ arc and its complementary arc are both cut.
Hence $p',q'$ lie in different remaining A components. B leaf attachments
cannot merge those components, so $p,q$ are not one T pair.
For $\delta=0$, deleting $p'q'$ from a simple A path already separates
its endpoints. Further deletions and distinct B leaf attachments cannot
reconnect them. Thus again $pq\notin T$, and hence $pq\notin L$.

The covered target-port boundary is included: if $v$ is incident with the
prescribed D edge, deletion may isolate $v$ in the A path. For $\delta=1$
the retained tag is part of the tagged-cycle proof. For $\delta=0$ the
segment is $u-v-\bar v$, which cannot have endpoints $p,q$ because the
root is excluded. For a free target this degeneracy cannot occur because
$v\notin V_D$.

Apply the assumed B classification to the actual $L$. Expand its cycle
through the suppressed mirrors $Y$ and transferred A paths. These paths
are disjoint except for their prescribed cycle endpoints; no physical edge
is reused. Expansion gives a tagged spanning64-cycle containing all
original M edges. Delete the tag. All D edges had been deleted, all
compressed edges were expanded, and every remaining new edge is a local
cube edge or selected short bridge. This proves the single-cherry theorem.

## 4. Source existence for free targets

In even consumption $b\ge1$ implies $s=a+1-b\le a$; sources exist and
cannot be the odd target. In odd consumption the exact existence condition is

$$b-|(W\cap A)\cap\{v,\bar u\}|\ge s=b-a-1.$$

For covered targets at most the root mirror is excluded, so this always
holds. For free targets with $a\ge1$ at most two holes are excluded and
it also holds. With a free target and $a=0$, two distinct excluded holes
can leave too few sources; $Z\cup W$ independence alone does not remove
this possibility. No route is claimed without legal sources.

If the full original hole set $H=\{u\}\cup Z\cup W$ is independent, then
$\bar u\notin W$, so at most $v$ is excluded; the odd source set exists
even when $a=0$. This is a useful free-target corollary under a declared
stronger geometry hypothesis. It is not silently inferred from
$Z\cup W$ independence, nor from an unproved predecessor hole layer.

## 5. Several cherries: exact local rank criterion

This section is a general local lemma on one Q5 face. Let $H_*$ be its
holes, $Y\subset H_*$ its specified omissions, and $K$ its $2n$ covered
terminals. Assume $n\ge2$. A legal short-complement forest has degree zero
on $Y$, two on $H_*\setminus Y$, one on $K$, and consists of paths whose
endpoints partition $K$. Write $P$ for its endpoint perfect matching.

Let $R$ be a fixed matching of $r$ pairs on $K$, with $1\le r<n$.
Suppose every legal short-complement forest has endpoint pairing containing
$R$. To prove the positive direction it suffices to supply a selected
family of such forests whose reduced pairings $P^-=P\setminus R$,
on $K^-=K\setminus V(R)$, have rank $2^{n-r-1}$ against any supplied
perfect-matching columns in the connectivity matrix on these $2(n-r)$
labels. The generic upper bound for that matrix is the only rank import.

Then, for every arbitrary perfect matching $F$ on $K$,

$$\text{a required local cycle exists}
\quad\Longleftrightarrow\quad F+R\text{ has no labeled cycle}.$$

**Necessity.** Any local cycle through $F$, after deleting $F$, gives one
of the legal complement forests and hence a pairing containing $R$.
A cycle in $F+R$ is a full component of $F+P$, because all its vertices
already have one F and one R edge. It misses the nonempty set $K^-$,
so $F+P$ cannot be a single alternating cycle. This contradiction proves
necessity; a common pair $F\cap R$ is included as a two-edge obstruction.

**Sufficiency.** If $F+R$ has no cycle, it is a disjoint union of paths.
Every vertex of $V(R)$ has degree two and every other vertex of $K$ has
degree one, so its path endpoints are exactly $K^-$. Suppressing all
internal $V(R)$ vertices produces an arbitrary perfect matching $F^-$ on
$K^-$. For any selected $P=R\cup P^-$, replacing those internally
disjoint F/R paths by single edges preserves connectedness of the labeled
unions:

$$F+P\text{ is one alternating cycle}
\quad\Longleftrightarrow\quad F^-+P^-\text{ is one alternating cycle}.$$

The verified reduced rank and upper bound make the selected rows span
the full connectivity row space. The column of every $F^-$ is nonzero:
cyclically join consecutive F-minus edges; for two residual terminals
use the labeled double-edge cycle convention. Some selected row connects
it. Undo the suppressions and expand the selected short forest to obtain
the required local cycle. Since the original full terminal domain has
at least four vertices, a shared physical F/forest edge would form a
proper two-edge component and could not have passed connectedness.

For $r=1$, acyclicity of $F+R$ is exactly absence of that one pair in F.
For $r\ge2$, absence of the individual R edges is insufficient. For
example $R=\{01,23\}$ and $F=\{12,30,45\}$ have no common pair but contain
the alternating cycle $0-1-2-3-0$. The other endpoints ensure it is a
proper component. The case $r=n$ is deliberately excluded: there are no
residual endpoints, $F+R$ always has cycles, and the stated necessity
argument would not exclude one Hamilton alternating component.

## 6. Multi-cherry transfer: the extra gap is automatic

Return to the global setup, with the same legal sources and $s\ge3$.
Let $R$ be a matching of local covered B vertices, all of whose endpoints
have the parity of $Y$, lie outside $Y$, and exclude $u$.
Assume the actual marked B geometry has the local classification

$$\text{cycle on }B\setminus Y\text{ through arbitrary }F
\quad\Longleftrightarrow\quad F+R\text{ is acyclic}.$$

Section5 is one sufficient way to establish this input; a fresh audited
alternative proof is also allowed. Let

$$J_B=\{pq\in R:p,q\in X_B\},\qquad j=|J_B|,$$

and let $J_A$ be the matching of their actual crossing partners in A.
These j edges are pairwise disjoint and are all legal completion pairs
by the same parity/root argument as in Section3. Prescribe $J_A\subset D$
and pair the rest of $V_D$ arbitrarily.

Under precisely the stated hypotheses a Hamilton $u$--$v$ extension
exists. No additional bound on $|R|$ and no matching-dependent extra-gap
hypothesis are needed. Because R is a matching, every edge of $J_B$
consumes two distinct ports, and therefore

$$j\le\lfloor c/2\rfloor.$$

For $\delta=1$, $d=(c+s)/2>\lfloor c/2\rfloor$; for $\delta=0$,
$d=(c+s-1)/2>\lfloor c/2\rfloor$. Both strict inequalities follow from
$s\ge3$. Thus $d>j$ holds automatically in both root faces, and at least
one D edge remains outside the prescribed set $J_A$. The actual bound is
on both-port obstruction pairs, not on the total number of cherries.

To prove the claim, every cycle in $L+R$ would alternate L and R edges,
and all its vertices would belong to $V(R)$, which has Y's parity.
Section3's suppression analysis now applies to each possible L edge
within $V(R)$: such an edge can only be an unchanged direct T pairing
between two ports. Original internal edges and suppressed bridge-mate
edges end outside this parity class. An edge to the root cannot belong
to the cycle because $u\notin V(R)$. Thus the putative cycle lies in
$T+J_B$.

Lift every T edge of that cycle to its actual transferred A path and
the crossing attachments at its port endpoints. Replace every J-B edge
by its prescribed A pair in $J_A$, deleting the now-superfluous B port
leaves and crossings along this cycle. This gives a cycle in the graph
obtained from the tagged A graph by deleting $D$ and restoring $J_A$.
The lifted paths are internally disjoint, so this operation does not
create a merely closed walk with repeated interior vertices.

If $\delta=1$, write $Q=P_A+uv$, a simple cycle. The graph in question is

$$Q-(D\setminus J_A).$$

Since $d>j$, it is a proper edge-deleted subgraph of a simple cycle,
and therefore a forest. If $\delta=0$, ignore the tag's root leaf, which
cannot participate in the putative cycle. The graph in question is

$$P_A-(D\setminus J_A),$$

a subgraph of a simple path, hence a forest even when $D=J_A$.
Both conclusions contradict the lifted cycle. Consequently $L+R$ is
acyclic and the assumed local classification and tagged expansion finish.
The argument includes a covered target port isolated after deleting D;
the tag either belongs to Q or has the excluded root as a leaf.

The extra-gap distinction is real for the abstract graph argument. If
$\delta=1$ and
$D=J_A$, restoring all prescribed pairs restores the entire tagged A
cycle. Upon path compression this can produce a full alternating
$T+J_B$ cycle even though no individual R pair is a T edge. This is a
failure of this prescription argument, not a counterexample to the
global endpoint theorem. The port count excludes this event under the
present hypotheses. Outside those hypotheses no claim is made that a
different D or cut cannot work. In the $\delta=0$ path case restoration
of all D edges would still be acyclic, providing a stronger abstract fact
than the uniform extra-gap bound used here.

## Boundaries and outstanding work

The new results are complete conditional proofs, submitted for fresh
review. Higher marked local rank certificates, actual useful cut/source
coverage, and whole twelve-to-eighteen-hole closure are not provided.
Root-in-obstruction cases, mixed-parity obstruction endpoints, and
transfers outside the declared source/consumption hypotheses are not
covered. In particular, general tagged-cycle prescriptions without any
unprescribed gap are not justified by this argument; the present port
bound guarantees that gap. Source shortage for a free target under only
nonroot independence
must be handled by another route or an explicit stronger hypothesis.
No unconditional predecessor induction is introduced. The proposed
single-cherry result specializes to the accepted ten-hole two-row lemma,
and the multi-cherry result strictly tracks cycles of the whole F+R
union, not just membership of individual pairs.

## Author sanity evidence, not independent acceptance

`HIGHER_FORCED_CHERRY_author_check.py` exhausts all perfect F matchings
on four, six, eight and ten terminals for every nonempty fixed partial R
with at least two residual terminals. It compares119238 full/reduced
connectivity instances and checks both directions of the contraction
criterion. It also checks8640 integer port/gap parameter cases and the
two explicit alternating-cycle boundary examples above. All pass.
These finite checks support the argument but do not prove its universal
quantifiers or replace the requested fresh proof review.

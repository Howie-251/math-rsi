# Forced T17 transfer when the global root is outside the obstruction pair

2026-11-01. ARIS proof-writer candidate; fresh independent review required.

## Claim, imports and status

Let $M$ be a short matching of $Q_6$ with ten holes, free even root $u$,
and covered odd target $v$. Write the other even holes as $Z$, the odd
holes as $W$, and assume $Z\cup W$ independent. Choose a cut $A,B$ with
$v\in A$ and $(a,b)=(|Z\cap A|,|W\cap A|)$ equal to $(3,1)$ or $(0,4)$.
Select a legal triple of bridge sources as in the uniform transfer.
Suppose its actual B marked geometry is one of the seven forced T17
inputs in `Q5_T17_RANK_BATCH_PROOF.md`, with forced pair $pq$, and
suppose $u\notin\{p,q\}$. Then $M$ has a Hamilton $u$--$v$ extension.

**PROVABLE AS STATED relative to the accepted uniform transfer, its
balanced-two-hole local endpoint input, and the proposed independently
checkable forced-T17 conditional classifications.** The universal
completion-avoidance proof below is new and requires fresh review.
No root-in-obstruction claim is made.

## Notation and dependency map

Let $C$ be the original crossing matching with port sets $X_A,X_B$ and
$c=|C|$. Let $M_A,M_B$ be the internal restrictions. Let $S$ be the three
selected A holes, and $Y$ their short B mirrors. The final B input has
one minority hole and seven majority holes, omitting exactly $Y$.
The forced pair $p,q$ consists of the two remaining short neighbors of
the minority. In particular $p,q$ have the same parity as $Y$, are outside
$Y$, and are covered in the final B matching. The root exclusion and
original independence also make them originally covered.

The proof uses the exact uniform completion and forest construction. It
adds at most one prescribed edge to its artificial matching $D$. The local
endpoint theorem allows every arbitrary $D$, including long same-parity
edges. The forced local classification is used only after proving that
the actual compressed matching avoids $pq$.

## Proof

### 1. Legal roots, completions and a lower bound on deleted gaps

If $c=0$, use the already declared five-direction endpoint theorem on
the original short matching and finish. Assume $c>0$ and let
$\delta=\mathbf1[u\in A]$.

For $(a,b)=(3,1)$ all three members of $Z\cap A$ are sources. If
$\delta=1$, take $r=u$ and pair $X_A\cup S$. Here $c$ is odd and
$d=|D|=(c+3)/2\ge2$. If $\delta=0$, choose any $r\in S$ and pair
$X_A\cup(S\setminus\{r\})$. Here $c$ is positive even and
$d=(c+2)/2\ge2$. No even crossing port is needed in this case.

For $(a,b)=(0,4)$ choose any three members of $W\cap A$ excluding the
mirror of $u$. This is possible because the target is covered and at
most one of the four hole sources is excluded. If $\delta=1$, take
$r=u$ and pair $X_A\cup S$, again with positive odd $c$ and
$d=(c+3)/2\ge2$. If $\delta=0$, the original even-port surplus is
$b-a=4$. Choose an even port $r$ and pair
$(X_A\setminus\{r\})\cup S$. Then $c\ge4$ is even and
$d=(c+2)/2\ge3$.

In every case $M_A+D$ has one even and one odd hole, with $r$ even/free.
The prescribed target $v$ remains a legal covered odd target. The local
endpoint theorem supplies a Hamilton $r$--$v$ path $P_A$ containing all
of $M_A+D$, with only short new edges.

### 2. Suppression cannot create the obstruction through a bridge mate

Every $y\in Y$ is originally internally matched in B: its mirror source
was free, independence excludes an original opposite hole, and source
selection excludes the B root. Write $h_y=M_B(y)$. Since $M_B$ is short,
$h_y$ has parity opposite to $Y$. The vertices $h_y$ are distinct and
are not B ports, original holes, the free root, or members of $Y$.

After tagging and transferring the A forest, its matching $T$ has
endpoint set $X_B\cup Y$ and additionally $u$ when $u\in B$. Its only
overlaps with $M_B$ are the vertices $Y$. Suppression extends an endpoint
at $y$ to the pendant mate $h_y$, or replaces a transferred Y--Y path by
a path between its two pendant mates. All these mates have parity
opposite to $p,q$. Also $pq\notin M_B$ because its endpoints have the
same parity and every original B matching edge is short.

We claim that the final matching $L$ can contain $pq$ only if both
$p,q\in X_B$ and $pq\in T$ before suppression. If, for example, $p$
is not a transferred endpoint, it retains its original B matching edge
to a vertex of opposite parity. That mate is internally covered, cannot
be a port or free root, and cannot be in $Y$ by parity; this edge is an
unchanged isolated component. It cannot end at $q$.

Since $p,q$ are outside $Y$ and the root, their being transferred endpoints
therefore means they are ports. A transferred edge from a port to $Y$
can only have its other endpoint changed by suppression to an opposite-
parity $h_y$, never to $p$ or $q$. A transferred edge to the B root
stays attached to that distinct root. Other port--port edges are unchanged.
A Y--Y component has only opposite-parity pendant endpoints. These cases
exhaust all components. Thus a newly compressed $pq$ can arise only from
the direct transferred pairing of those two ports, as claimed.

### 3. Prescribe a gap when both obstruction vertices are ports

If either obstruction vertex is not a B port, Step2 already proves
$pq\notin L$ for any legal completion. Otherwise let $p',q'\in X_A$
be their actual original crossing partners. Prescribe $p'q'\in D$.

This prescription is legal. In the even-source row, $r$ is $u$ or an
original hole in $S$, hence never a port. In the odd-source row with
$u\in B$, the B obstruction vertices are even, so their crossing
partners $p',q'$ are odd, whereas $r$ was chosen even. In the other
root-face cases $r=u$ is originally free. Thus neither prescribed
endpoint was excluded from the completion set. Both are distinct and
disjoint from all source holes; the remaining even number of completion
vertices can be paired arbitrarily. The local theorem allows this $D$.

### 4. The prescribed ports never become one transferred segment

First suppose $u\in A$. Add the tagged artificial edge $uv$ to the local
Hamilton path. This is one simple cycle on all A vertices; the tag was
not already a path edge since a Hamilton path on thirty-two vertices
cannot contain its endpoint edge. The matching $D$ lies on this cycle.
By Step1, at least two D edges are removed. The endpoints $p',q'$ of
the prescribed removed D edge lie in different remaining components:
their direct arc was removed, and the other arc contains another removed
D edge. Attaching original crossings and the short source bridges merely
adds distinct B leaves to these components and cannot merge them.
Hence their B leaves $p,q$ cannot be paired by one transferred segment.

Now suppose $u\in B$. Start from the local simple $r$--$v$ path and
delete $D$, including its edge $p'q'$. Removing that edge from a path
separates $p',q'$ into different components; deleting other edges cannot
rejoin them. Adding the tag $uv$ only attaches the previously untouched
B root as a leaf at $v$. Each original crossing and each bridge likewise
attaches a distinct B vertex. No two A components are joined. This remains
true in the even-source case $r\in S$: its short bridge attaches a new
covered B leaf, rather than connecting two A components. Therefore
$p,q$ are again in different transferred segments.

The target-port boundary is included. If $v$ is a crossing port and
$p'q'$ is incident with $v$, deletion of $D$ from the Hamilton path
can isolate $v$. With $u\in A$, the tag remains at $v$ and the tagged-
cycle proof above applies without any exception. With $u\in B$, the
tag and the original crossing give the segment $u-v-\bar v$, where
the original crossing partner is the actual B port. This segment has
one endpoint $u$; since $u\notin\{p,q\}$, it is not a $p$--$q$ segment.
The prescribed partner on the other side of the removed gap stays in
a different A component. No claim that the deleted-edge forest lacks
isolated A vertices is needed.

We have proved $pq\notin T$. Step2 then proves $pq\notin L$ after
all bridge conflicts are suppressed.

### 5. Apply the conditional local theorem and expand

The holes of $L$ are exactly the actual one-minority/seven-majority
marked geometry. The vertices $p,q$ are covered and the omitted triple
is $Y$. Its proposed rank classification applies because its sole
obstruction edge was just excluded in the actual compressed matching.
Its $29$-cycle on $B\setminus Y$ expands to one global tagged cycle:
the thirty-two A vertices and the three suppressed bridge mirrors
restore the full sixty-four vertices. Every original edge of $M$ survives.
All artificial D and compressed edges disappear, and the other new
edges are local short edges or chosen short bridges. Removing the tagged
$uv$ edge yields the prescribed Hamilton $u$--$v$ path through $M$.

## Scope and unproved boundaries

The root exclusion is essential to this proof. If the B obstruction is
$\{u,\bar v\}$ and $v$ is an original crossing port, tagging after
deleting its D edge forces the transferred segment $u-v-\bar v$.
No choice of $D$ removes that particular obstruction. Such a fixed-cut
template failure is not a global P6 counterexample. It is not used in
the application below, which chooses another actual safe projection.

The retained `Q5_T17_RANK_forced_safe_witnesses.json` gives a root-not-OB
projection for every one of the $1036$ forced-only records remaining
after the unforced T17 union. This is a separate finite geometry assertion
requiring fresh independent reconstruction. Combined acceptance of that
assertion, this transfer and the seven conditional local classifications
is required before any global class is promoted. Full P6 is not claimed.

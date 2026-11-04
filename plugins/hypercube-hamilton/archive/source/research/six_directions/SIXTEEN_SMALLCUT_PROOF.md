# Sixteen-hole small-cut forced-edge certificate: new118 sufficient cases

2026-11-02. Role: proof-writer / computational producer.
Status: **PROVABLE AS STATED relative to the new explicit finite local
certificate and accepted imports; fresh independent review required.**
No producer self-acceptance or production-ledger edit is made.

The accepted source `SIXTEEN_LOCAL_REVIEW.json` leaves148 covered-target
geometries and zero free-target geometries, **conditionally on complete
fourteen-hole extension**. This package proposes a sufficient construction
for118 of those actual records, for every realizing original short matching.
Its exact candidate complement is the30 root-star records, all at target31.
It does not prove complete fourteen holes, complete sixteen holes, or full
$P_6$. The source's predecessor condition is not discharged by this package.

## 1. Exact new local theorem

In $Q_5$, put
$$H_E=\{0,3,5\},\quad H_O=\{1,2,14,22,25,26,28\},\quad
U=\{1,2\},\quad K=V(Q_5)\setminus(H_E\cup H_O).$$
Let $e=\{30,31\}$ and $R=\{13,21\}$. The claim is:

For **every perfect matching $F$ of the complete graph on the22 vertices
$K$**, if $e\in F$ and $R\notin F$, then there is one cycle on exactly
$V(Q_5)\setminus U$ retaining $F$ and adding only cube edges.

This is a sufficient implication, not a local iff classification. No
assertion that every possible complement forest forces $R$ is required.
The old unrestricted rank896/1024 for this marked geometry did not prove
its arbitrary-matching universality and is not used as such a premise.

### Explicit finite premise

`SIXTEEN_SMALLCUT_local.json` and its four binary files supply256 selected
short forests $P_i^{phys}$. Each has degree0 at $U$, degree2 at
$(H_E\cup H_O)\setminus U$, degree1 at $K$, and no cycle. Its path
endpoint pairing $P_i$ is on $K$. It does not contain $e$.
Add $e$ to $P_i$ and suppress30,31, obtaining a perfect matching $Q_i$
on20 labels. Each selected $Q_i$ contains $R$. Delete $R$ to obtain
$Q_i^-$ on
$$K^-=K\setminus\{13,21,30,31\},\qquad |K^-|=18.$$
Against256 supplied arbitrary perfect-matching columns on $K^-$, the
connectivity rows $Q_i^-$ have GF(2) rank256.

These are direct finite witness conditions. The raw source is
`Q5_T37_INDEPENDENT_orbit_00_forests.bin`; it is used only as a pool of
candidate physical forests. No old rank, exhaustiveness, or accepted local
domain is imported for the new statement. The producer independently
reconstructs its selected physical forest pairings as sanity, but a fresh
reviewer must verify all witness conditions and matrix entries.

### Mathematical proof from the premise

The complete matching-connectivity matrix on18 labels has GF(2) rank
$2^{18/2-1}=256$, by the generic theorem already sourced in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. Thus the256 selected rows span
its whole row space. Every column of the complete matrix is nonzero:
cyclically joining the nine edges of the column matching gives a connected
opposite pairing. Consequently for every perfect matching $G$ on $K^-$,
some selected $Q_i^-+G$ is connected.

For the arbitrary $F$ in the local claim, put $F_{20}=F\setminus\{e\}$.
Since $R\notin F$, the mates $a=F_{20}(13)$ and $b=F_{20}(21)$ are distinct
and lie outside $R$. Delete $13a,21b$ and insert $ab$, giving a perfect
matching $G$ on $K^-$. For each selected row, contraction of the path
through the required edge $e$, followed by contraction of
$a$--13--21--$b$, gives
$$P_i+F\text{ connected}\iff Q_i+F_{20}\text{ connected}
\iff Q_i^-+G\text{ connected}.$$
Choose the row furnished by the full reduced rank and expand its physical
short forest. This yields the required cycle on30 vertices. A common
physical required/forest edge would constitute an isolated labelled
two-edge component, impossible in this connected union, so no duplicated
physical edge is used. Only the supplied complement edges are new, and
they are short. This proves the stated local implication.

## 2. New $s=2$ actual transfer lemma with a surviving required edge

Let $M$ be any original short matching of $Q_6$ with sixteen holes
$\{u\}\cup Z\cup W$, $u=0$ even/free, $|Z|=7$ even, $|W|=8$ odd,
and $Z\cup W$ independent. Let $v$ be its prescribed covered odd target.
Choose a coordinate $d$ with $v_d=1$, put $A=\{x:x_d=1\}$,
$B=\{x:x_d=0\}$, and suppose
$$|Z\cap A|=4,\qquad |W\cap A|=3.$$
The free root $u$ is in $B$. Choose two distinct sources
$S\subset Z\cap A$, and write $Y=\overline S$ for their short B mirrors.
Suppose the actual B marked input is a common cube-automorphic image of
the local theorem in Section1, and its actual required edge $e_B$ is an
original internally B-forced matching edge disjoint from $Y$.
Its transported pair $R_B$ has the same parity as $Y$ and excludes $u$.
Then every realizing original $M$ has a Hamilton $u$--$v$ extension
retaining $M$ and adding only short edges.

This is a new proof for this exact $s=2$ setting. The old generic
forced-cherry transfer stated $s\ge3$; that hypothesis is not silently
dropped in applying it. The path, compression and gap arguments are
proved here with the present root/source counts.

### 2.1 Legal A completion and arbitrary original matching

Write $M_A,M_B$ for the internal restrictions and $X_A,X_B$ for original
crossing ports. Shortness gives
$$|X_A\cap E|-|X_A\cap O|=3-4=-1.$$
Thus the crossing number $c$ is positive and odd, so there is no empty
crossing boundary to import. Choose any $r\in S$ as the free even A root.
The artificial-completion domain is
$$V_D=X_A\cup(S\setminus\{r\}),\qquad |V_D|=c+1.$$
Its vertices are free for $M_A$. Any perfect pairing $D$ of $V_D$ gives
$M_A+D$ with exactly three free holes of each parity. The accepted
all-balanced Q5 arbitrary-matching endpoint theorem supplies a Hamilton
$r$--$v$ path through $M_A+D$, adding short edges. Here $r$ is free and
$v$ is a legal covered odd target; if $v$ is an original crossing port,
$D$ covers it. Artificial $D$ pairs may be long or same-parity, as the
accepted theorem permits. This is an existence assertion for every actual
$M$, and does not choose an original matching favorably.

### 2.2 Transfer, tag and actual B compression

Delete $D$ from the A Hamilton path. Attach every actual original crossing,
the two short source bridges, and the tagged auxiliary edge $uv$. The
tag attaches the previously free B root as a leaf at the endpoint $v$.
The A root $r$ gains its missing degree by its source bridge; every other
deleted-gap endpoint gains its crossing or source attachment. If a
crossing target is isolated when its only A edge is deleted, its crossing
and the tag supply its two degrees. Hence all retained A vertices have
degree2 and the result is a path system with distinct B leaves, not an
internal A cycle. Its endpoint matching $T$ is on $X_B\cup Y\cup\{u\}$.

Each $y\in Y$ was originally internally B-covered: its A mirror was an
original hole, independence excludes a nonroot B hole there, and its odd
parity excludes the even root. Its short original B mate $h_y$ is distinct,
opposite-parity, and outside all attachments and $Y$. The only degree
conflicts in $T+M_B$ occur at $Y$, with pendant mates $h_y$.
Suppress those conflicts, preserving the full represented paths and the
tag. Even a Y--Y transfer edge only joins two distinct pendant mates;
it cannot create a cycle. The resulting actual perfect matching $F_B$
has holes
$$H_*=(Z\cap B)\cup(W\cap B)\cup Y,$$
with counts3 even,7 odd and omissions exactly $Y$ of size2. The consumed
root $u$ is now covered by its tagged path. The matching is on22 vertices
and may have arbitrary edges, as the local theorem permits.
Since $e_B\in M_B$ is disjoint from $Y$, neither of its original endpoints
is an attachment; its original edge survives unchanged in $F_B$.

### 2.3 Avoiding the actual same-parity pair

Write $R_B=\{p,q\}$. Both vertices were originally covered, because they
are outside the marked holes and the consumed root. Their common parity
is the parity of $Y$, so $pq\notin M_B$ by original shortness.
If either is not an original port, its short internal mate has parity
opposite $Y$ and is outside $Y$, so that original edge survives unchanged
and cannot be $pq$. Suppression can move a transfer end at $Y$ only to an
opposite-parity mate, never to $p$ or $q$. Therefore a compressed pair
$pq$ can arise only when both are original B ports and were directly
paired in $T$.

In that remaining case let $\alpha,\beta\in X_A$ be their actual original
crossing partners. Prescribe $\alpha\beta\in D$. This is legal: $r\in S$
is an original source hole, never an original port, so neither prescribed
endpoint is excluded from $V_D$. Pair its remaining even number of
vertices arbitrarily. Deleting $\alpha\beta$ from a simple A path
separates its endpoints; further deletions and distinct B leaf attachments
cannot reconnect them. Hence $p,q$ are not a T pair, and therefore not
an $F_B$ pair. Only path deletion is used here: the root is in B, so the
tag does not close an A cycle, and a second deletion is not needed.
The covered crossing-target boundary remains valid even if it is one of
$\alpha,\beta$: its isolated segment contains the distinct root, which
does not belong to $R_B$.

Thus $F_B$ contains $e_B$ and avoids $R_B$ simultaneously. Invoke the
new local theorem on its exact marked input. Expand its cycle through
the represented paths and pendant original edges to obtain one tagged
spanning64-cycle retaining every original edge. Delete the tag to obtain
the required Hamilton $u$--$v$ path. Every artificial D edge was deleted;
every compressed placeholder was expanded; all actual newly added edges
are short. This proves the transfer lemma.

## 3. Exact actual118 application and candidate complement

The source is the frozen15-byte Z7/W8 streams
`SIXTEEN_LOCAL_remaining_v{1,7,31}_covered.bin`, bound by the accepted
`SIXTEEN_LOCAL_REVIEW.json`. The producer searches every actual record,
every legal small-cut coordinate and every two-element source subset.
Each witness in `SIXTEEN_SMALLCUT_application.json` records its exact
source index and record, cut, sources, full common-map data, actual $e_B$,
actual $R_B$ and a degree-one leaf chain proving $e_B$ is forced in every
original matching. A leaf chain removes each forced edge's two endpoints
before taking the next leaf; it is a universal matching argument, not a
favorable perfect-matching sample. Both endpoints of $e_B$ are in B and
outside $Y$. All minority/majority/omission sets, the required edge and
forbidden pair use one common translation/permutation of the new local
statement. The producer checks that $R_B$ has Y parity and excludes root0.

The candidate positive counts are v1:0, v7:18, v31:100. Its exact complement
is v1:0, v7:0, v31:30. These are the four nonstar orbit sizes18,20,60,20;
no orbit classification is needed as a coverage premise because all148
actual records were scanned directly. The six saved positive/complement
streams partition the frozen source in source order. All30 retained
records are the distinct root-star orbit being treated separately.

The local certificate layout is256 forests of38 bytes,256 reduced
pairings of18 bytes,256 columns of18 bytes, and256 matrix rows of32 bytes
(little-bit-first). Producer sanity reconstructs the physical forests,
degrees, acyclicity, pairings, contractions, matrix and rank. It is not
fresh independent review. The reviewer must independently verify all
these conditions, the actual source/map/leaf witnesses and exact partition,
and the new $s=2$ transfer rather than importing the old $s\ge3$ statement.

Dependencies are acyclic: accepted balanced Q5 endpoint theorem and
matching-connectivity rank theorem -> new conditional local finite gate
-> new small-cut transfer -> actual118 sufficient records. The accepted
source's complete-sixteen-domain reduction separately depends on complete
fourteen holes, which remains OPEN. No result in this package is used to
justify its own inputs, and no full16,18 or $P_6$ closure follows yet.

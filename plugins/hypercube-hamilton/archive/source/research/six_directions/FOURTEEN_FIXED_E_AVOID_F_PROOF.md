# Fixed e, avoided mixed-parity f: producer proof package

Status: **PROVABLE AS STATED relative to the positive finite certificate and
accepted matching-connectivity rank theorem; fresh independent review required.**
Role: proof-writer/computational producer. No self-acceptance, ledger promotion,
or new fourteen-hole geometric subtraction is claimed. The accepted residual
stays $2527=240+702+1585$ covered geometries, with the inherited free branch
closed. Full fourteen-hole and full $P_6$ remain unproved.

## Exact local claim

In $Q_5$, put
$$H=\{0,3,5,6,9,10,12,15,17,18,20,27\},\qquad
U=\{0,5,6,9,10,12\},\qquad K=V(Q_5)\setminus H.$$
Let $e=\{19,23\}$ and $f=\{8,24\}$. For every perfect matching $F$ of
the complete graph on $K$, if $e\in F$ and $f\notin F$, there is a cycle on
exactly $V(Q_5)\setminus U$ retaining $F$ and adding only cube edges.
This is a sufficient statement. No converse, exhaustive complement-forest
classification, or implication from a deficient rank is asserted.

Dependencies: accepted complete matching-connectivity rank theorem on16
labels (rank $2^{16/2-1}=128$) -> explicit128-row reduced certificate -> local
claim. The primary-source import is the same generic theorem recorded in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. The old producer local index9
rank256 is not a completeness premise for this new theorem.

Each selected short forest $S_i$ has degree0 on $U$, degree2 on $H\setminus U$,
degree1 on $K$, and no cycles. Its path endpoint pairing is $P_i$ on20
labels. Since $P_i$ does not contain $e$, the union $P_i+e$ consists of paths:
the two endpoints of $e$ have degree2 and all other endpoints degree1.
Suppress19,23 to obtain a matching $Q_i$ on $K\setminus e$. Each selected
$Q_i$ contains $f$. Set $R_i=Q_i\setminus\{f\}$ on
$$V_{16}=K\setminus\{8,19,23,24\}.$$
These assertions are direct finite witness conditions, not consequences of
the source rank metadata. They must all be independently checked.

The supplied128 $R_i$ against128 supplied arbitrary perfect-matching columns
have a GF(2) connectivity matrix of rank128. The generic complete matrix on
$V_{16}$ has rank128, so these rows span its whole row space. Every full
column is nonzero: one can cyclically join the eight matching edges using
another perfect matching. Thus for any perfect matching $G$ on $V_{16}$,
some selected $R_i+G$ is connected.

For the arbitrary $F$ in the claim, delete $e$ to obtain $F_{18}$ on
$K\setminus e$. Because $f\notin F$, the mates
$a=F_{18}(8)$ and $b=F_{18}(24)$ are distinct and outside $f$. Delete
$\{8,a\},\{24,b\}$ and insert $\{a,b\}$, obtaining a perfect matching
$G$ on $V_{16}$. For each selected row, connectedness is preserved by
contracting first the $e$-joining path and then $a$--8--24--$b$:
$$P_i+F\text{ connected}\iff Q_i+F_{18}\text{ connected}
\iff R_i+G\text{ connected}.$$
Choose the row furnished by full reduced rank and expand its short forest.
The resulting degree2 graph is one cycle on $V(Q_5)\setminus U$.
A common physical required/forest edge would be a separate labelled
two-edge component, inconsistent with connectedness on26 vertices, so no
such duplication occurs. The local claim follows.

## General transfer lemma for an original absent pair

This lemma extends the completion argument without presuming that a forbidden
pair has the same parity as the source mirrors. Use the accepted uniform
transfer setting in `HIGHER_FORCED_CHERRY_TRANSFER.md`, with legal source
set $S$, $|S|=s\ge3$, $Y=\overline S$, and $c>0$ original crossings.
Let $f=\{p,q\}$ be two distinct final covered B vertices, neither equal to
the global free root $u$. Assume $f\notin M_B$ for the actual original short
matching $M$. Then one can choose the legal A root and completion matching
$D$ so that the actual compressed B matching avoids $f$.

To prove this, recall that suppression at $Y$ only extends transferred path
ends by the pendant original edges $y h_y$, where the $h_y$ are distinct
and outside all attachment vertices. Consider either endpoint $p$ of $f$.
If it is originally internally B matched and its original mate is not in
$Y$, its original edge remains unchanged. Since $f\notin M_B$, that edge
already precludes compressed $f$, regardless of $D$. The same holds for
$q$. It remains to consider the case when neither endpoint has such a
retained edge. Each endpoint is then either an original B crossing port,
or the mate $h_y$ of exactly one omitted mirror $y\in Y$. The only other
possible attachment is the consumed global root, excluded by hypothesis.

Assign its preimage B attachment to be the port itself in the first case
and $y$ in the second case. The two preimages are distinct, because all
ports, mirrors and pendant mates are disjoint and the mates are injective.
Let $\alpha,\beta$ be the corresponding A attachment vertices, either
original crossing partners or source holes. They are distinct and lie in
$X_A\cup S$. Choose the A root so that neither is excluded from the
completion domain: if $u\in A$, use $r=u$, an original hole outside both
sets; in even consumption with $u\in B$, choose $r\in S$ outside
$\{\alpha,\beta\}$, possible since $s\ge3$; in odd consumption with
$u\in B$, choose an even crossing port outside these two vertices, possible
since the even-port surplus is $s+1\ge4$. The remaining completion-domain
cardinality is even, so prescribe $\alpha\beta\in D$ and pair the rest
arbitrarily. The accepted A endpoint theorem permits arbitrary added pairs.

Delete $D$ from the resulting A Hamilton path. If $u\in B$, the deleted
edge $\alpha\beta$ separates its endpoints into different components. If
$u\in A$, work with the tagged A cycle: its direct $\alpha\beta$ arc is
cut, and at least one other D edge cuts the complementary arc, since
$|D|\ge2$. In both cases attaching distinct B leaves does not reconnect
the components. Therefore the two preimage attachments do not form one
transferred pair, and extending them by pendant edges cannot create $f$.
Covered target ports, including an isolated target after gap deletion, are
included by the tagged path/cycle argument. This proves the lemma. If
$c=0$, use the accepted five-direction endpoint import directly.

In the actual index9 application, the required original leaf-forced edge
$e$ lies internally in B and outside $Y$, so it survives the transfer for
every $D$. The local theorem and this lemma therefore suffice for the
matching-level branch where its actual short pair $f$ is absent in $M$.
This branch is conditional on the original matching, not a whole-geometry
closure. Original shortness alone cannot exclude $f$: unlike the old
same-parity cherries, this $f$ is itself a cube edge.

## Producer finite data and actual boundary

`FOURTEEN_FIXED_E_AVOID_F_produce.py` selects128 forests from the frozen
index9 pool, recomputes their physical degrees/path pairings as producer
sanity, and produces their twice-reduced pairings,128 columns and128x128
binary matrix. The217 nonzero source rows all have the stated intermediate
pair $f$; only the128 selected rows are needed for the positive theorem.
Rows of `_forests.bin` have32 bytes (16 physical edges), `_pairs16.bin`
and `_columns16.bin` have16 bytes (eight endpoint pairs), and `_matrix.bin`
has128 rows of16 bytes, little-bit-first. Row selection and exact sets are
recorded in `_local.json`. These are producer computations pending a fresh
checker; their successful assertions are not independent acceptance.

The actual source is the accepted maximal-A complement of size2527.
`FOURTEEN_FIXED_E_AVOID_F_scan.py` finds636 normalized fixed-e projections
on318 distinct geometries. Each geometry has only one distinct actual
forbidden pair $f$ under these projections. Its canonical global root is
4,1,2,11,7 or lies in A, and is never8 or24, so the lemma's root exclusion
holds in these explored projections. No unaffected internal-edge guard
excludes the pair universally. Fixing this short pair in the original
covered graph still permits a perfect matching in all318 cases (a search
diagnostic, not a claimed exhaustive matching certificate). Thus no
geometry is subtracted on the basis of this local certificate alone.

`FOURTEEN_FIXED_E_AVOID_F_badbranch.py` explores the original-$f$ branch
using all alternative new-type geometries and surviving known edges from
the forced leaf chain plus $f$. Its only task is index9 with fixed pairs
$\{8,24\},\{19,23\}$. The existing forest pool does not provide a positive
certificate for this task. This is a boundary of the current construction,
not a counterexample or a proof of nonextension. It leaves the actual
original-$f$ branch unresolved, and the accepted covered residual remains2527.

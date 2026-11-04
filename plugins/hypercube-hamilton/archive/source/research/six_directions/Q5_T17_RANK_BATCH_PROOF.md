# All seventeen actual T17 marked orbits: full and conditional rank inputs

2026-11-01. ARIS proof-writer producer package. Fresh independent review is
required; these are proposed local inputs and sufficient Q6 classes.

## Claim and status

For every row below, let the minority hole be $0$, let its seven majority
holes be $J$, and let $U$ be the specified omitted triple. Every required
matching is an arbitrary perfect matching on $K=Q_5\setminus(\{0\}\cup J)$.
All required edges may be long or same-parity.

For each unforced row, every such matching has a simple $29$-cycle on
$Q_5\setminus U$ containing it, with only short new edges. For each forced
row, such a cycle exists **if and only if** the required matching does not
contain the specified edge $pq$.

**PROVABLE AS STATED relative to the generic matching-connectivity rank
upper bound and independent verification of the supplied certificates.**
All producer-side forest/matrix/elimination checks passed. No full T17,
complete ten-hole P6, or full P6 claim is made. Earlier first-case files,
T26 source files and the main state were not changed.

## Exact marked cases

The IDs are fixed IDs of `Q5_T17_RANK_candidate_profile.json` on the
accepted $4096$-record T26-batch remainder, not mutable dynamic IDs.

| ID | $J$ | $U$ | Condition | Matrix endpoint count | Rank |
|---:|---|---|---|---:|---:|
|1|$1,2,7,11,13,21,31$|$1,2,13$|none|24|2048|
|2|$1,2,7,13,26,28,31$|$1,2,28$|none|24|2048|
|3|$1,2,7,25,26,28,31$|$1,2,28$|none|24|2048|
|4|$7,11,13,19,21,26,28$|$7,11,19$|none|24|2048|
|5|$1,2,4,7,11,28,31$|$1,2,4$|$pq=8,16$ absent|22|1024|
|6|$1,2,4,11,13,22,31$|$1,2,4$|$pq=8,16$ absent|22|1024|
|7|$1,2,13,14,21,25,28$|$1,2,14$|none|24|2048|
|8|$1,7,11,14,22,26,31$|$1,7,11$|none|24|2048|
|9|$1,2,4,7,11,21,31$|$1,2,4$|$pq=8,16$ absent|22|1024|
|10|$1,7,14,22,25,26,31$|$1,7,25$|none|24|2048|
|11|$1,2,4,11,19,25,26$|$1,2,4$|$pq=8,16$ absent|22|1024|
|12|$1,2,4,7,11,13,31$|$1,2,4$|$pq=8,16$ absent|22|1024|
|13|$1,2,4,11,13,14,31$|$1,2,4$|$pq=8,16$ absent|22|1024|
|14|$1,7,14,22,25,26,28$|$1,7,25$|none|24|2048|
|15|$1,7,11,14,21,26,28$|$1,11,21$|none|24|2048|
|16|$1,7,11,21,26,28,31$|$1,11,21$|none|24|2048|
|17|$1,2,4,7,11,13,14$|$1,2,4$|$pq=8,16$ absent|22|1024|

## Assumptions, notation and dependency map

Import only the generic binary matching-connectivity matrix bound
$\operatorname{rank}(\mathcal H_{2n})\le 2^{n-1}$ from the primary theorem
identified in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. At twenty-four
endpoints this gives $2048$, and at twenty-two it gives $1024$.
The local inputs use neither a Q6 theorem nor any other T17/T26 theorem.
The optional Q6 application separately imports the accepted uniform transfer
and the final accepted T26-batch residual. Thus the dependency DAG is acyclic.

The rank interface, labeled union convention, exact matching columns and
positive forest checks are the same as in `Q5_T17_RANK_FIRST_PROOF.md`,
but every case here has a new batch prefix and independently checked data.
An admissible forest has degree zero at $U$, one at all $24$ terminals in
$K$, and two at the five included holes. It has $17$ short edges and $12$
path components. Its endpoint pairing is denoted $P$.

## Proof

### 1. Full-rank unforced rows

Each selected forest is verified directly as a graph and compressed to its
actual terminal matching $P$. For each of the ten unforced rows the saved
$2048$ forest pairings and matching columns have connectivity rank $2048$
over $\mathbb F_2$. The imported upper bound makes those complete rows span
the whole matching-connectivity row space. Every column indexed by an
arbitrary original matching $F$ is nonzero: cyclically connect consecutive
required edges to construct another arbitrary matching whose union with
$F$ is one alternating cycle. Hence some selected forest pairing connects
with $F$. Expanding the forest paths yields the required simple $29$-cycle.
Only stored legal forests are needed, not exhaustive forest enumeration.

Every actual union retains the two matching labels. A common pair would
form an isolated two-edge component and cannot pass the single-cycle test.
Thus no physical short edge duplicates a required edge on expansion.

### 2. Forced cherry and exact conditional classification

For a forced row all three omissions are short neighbors of $0$. The two
remaining neighbors are precisely $p,q$, and both are covered vertices:
the four included majority holes are nonneighbors of $0$. Every admissible
forest must include $p-0-q$, so every $P$ contains $pq$.

If the required matching contains $pq$, its three edges with this forced
path make an isolated triangle. No spanning $29$-cycle can have such a
component. This proves necessity analytically, without a failed search.

Otherwise put $a=F(p)$ and $b=F(q)$. The four vertices are distinct.
Suppress $a-p-q-b$ in the labeled graph $F+P$: replace $pa,qb$ in $F$ by
$ab$ and remove $pq$ from $P$. The resulting perfect matchings $F',P'$
are on $K\setminus\{p,q\}$ and have a single alternating cycle exactly
when $F+P$ does. This is path suppression, valid even for long or
same-parity original edges.

For each of the seven forced rows, the saved $1024$ shortened forest
pairings $P'$ have rank $1024$ against supplied arbitrary matching columns
on those $22$ endpoints. The generic upper bound and the same nonzero-column
argument give some connecting $P'$ for every $F'$. Use its associated full
forest $S$ and expand the suppressed path to recover all original edges,
$p,q$ and the included minority hole $0$. The result is the required
$29$-cycle. Thus absence of $pq$ is sufficient as well as necessary.

### 3. Exact certificate formats and verification

Unforced prefixes are `Q5_T17_RANK_batch_XX`, forced prefixes are
`Q5_T17_RANK_forced_XX`. Every config contains the eight holes and three
omissions; forced configs additionally append $p,q$.

For an unforced prefix, `_forests.bin` has $2048$ records of $34$ bytes,
`_pairs.bin` and `_columns.bin` have $2048$ records of $24$ bytes, and the
matrix/pivot/combination files each have $2048$ rows of $256$ bytes.

For a forced prefix, `_forests.bin` has $1024$ records of $34$ bytes;
`_full_pairs.bin` has $1024$ records of $24$ bytes. Its corresponding
`_pairs.bin` deletes the forced pair and has $1024$ records of $22$ bytes;
`_columns.bin` also has $1024$ records of $22$ bytes. Its matrix/pivot/
combination files each have $1024$ rows of $128$ bytes. Bits in each row
are stored least-significant-bit first. Pairs use actual Q5 labels.

The new reduced search preserves the full twenty-four endpoint degree
constraints and full forest paths, checks that the compressed pairing
contains the forced pair, and only then removes it for the rank matrix.
It does not silently pretend $p,q$ are omitted vertices of the forest.

`Q5_T17_RANK_batch_author_check.py` verifies all $27648$ saved forests,
all full and shortened endpoint pairings, every matching column, all
$49283072$ connectivity matrix bits and every pivot XOR combination.
The highest set bit of pivot row $j$ is exactly $j$, proving the rank
lower bounds in exact binary arithmetic. All seventeen checks pass.
These checks are producer evidence and need fresh independent acceptance.

### 4. Unforced Q6 transfer union

For a covered-target Q6 input use the accepted uniform-transfer notation.
In row $(a,b)=(3,1)$ select the three even A holes. The B input has the
one remaining nonroot even hole as minority and four odd B holes plus the
three mirror holes as majority, omitting precisely the mirrors. In row
$(0,4)$ select three of the four odd A holes excluding the root mirror;
the minority is the sole odd B hole and the majority is the four even B
holes plus those three mirrors. Both A inputs require only the established
balanced-two-hole endpoint theorem. All crossing counts are covered by the
accepted uniform transfer, including the zero-crossing import.

The full-rank inputs allow every arbitrary compressed matching. No
same-parity-edge exclusion is added to the unforced Q6 application.

`Q5_T17_RANK_batch_coverage.py` starts from the **accepted independent**
T26-batch remainder files and checks equality with the candidate source
bytes. It enumerates every relevant actual cut and legal source triple,
normalizes the unique minority and all marked omissions under a common
coordinate permutation, and tests membership in the ten full-rank orbits.
Each input is counted once, retaining one concrete projection witness.
The exact disjoint union accounting is:

| $v$ | Accepted input | Unforced T17 union | Remaining | Remaining with a forced T17 choice |
|---:|---:|---:|---:|---:|
| $1$ | $910$ | $570$ | $340$ | $220$ |
| $7$ | $1476$ | $918$ | $558$ | $396$ |
| $31$ | $1710$ | $1110$ | $600$ | $420$ |
| Total | $4096$ | $2598$ | $1498$ | $1036$ |

The remaining $462$ inputs have no T17 projection of these rows. These
counts await fresh application review; no main-ledger decrement was made.
The retained JSON witnesses give original labels, selected sources,
actual local sets and a normalizing coordinate permutation. The raw
remaining files contain the exact unresolved records, without any
matching-feasibility exclusion.

### 5. Forced Q6 completion avoidance remains a separate obligation

For the $1036$ remaining records admitting forced projections, the witness
file gives every supported projection and its actual B obstruction pair.
The original internal short matching cannot contain that same-parity edge,
but the compressed matching can acquire it through transferred paths and
the global endpoint tag. Absence from the original B matching is therefore
insufficient to apply the local conditional classification.

The obstruction pair may even contain the global root $u=0$ when it lies
in B: tagged closure consumes that originally free vertex before local
classification, so it is legitimately a local covered endpoint. The
witnesses explicitly flag this boundary. No claim that both obstruction
endpoints were originally covered is made.

The companion `Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md` proves how to choose
$D$ whenever the global root is outside the obstruction pair, including
a target that is a crossing port. A concrete safe choice exists for all
$1036$ forced-only records and is retained in
`Q5_T17_RANK_forced_safe_witnesses.json`. That new universal lemma and
its finite application require fresh review together with these local
inputs. Root-in-obstruction templates are not used or declared positive.

## Corrections, scope and open risks

All seventeen local theorem statements retain arbitrary required edges.
Their classifications and positive certificates are proposed complete
local inputs, subject to independent review and the explicit primary
rank bound. The unforced union is a proposed sufficient global class.
Root-in-obstruction transfer templates, the $462$ records without any T17
projection, and full P6 are outside this package; the safe companion
transfer is a separate proposed proof submitted with it. Failed or capped searches are never used as
nonexistence claims. Previously frozen first-case files remain unchanged.

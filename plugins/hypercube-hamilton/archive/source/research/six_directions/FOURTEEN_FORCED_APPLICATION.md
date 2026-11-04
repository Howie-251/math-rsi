# Actual fourteen-hole application: strict root-safe cherries plus row54

## Claim and status

The exact accepted Hall residual has3923 covered-target geometries. The
eight conditional local statements and unconditional row54 in
`FOURTEEN_FORCED_PROOF.md`, once independently accepted, give sufficient
Hamilton endpoint constructions for1336 of these geometries and leave
exactly2587 records. Each sufficient claim holds for EVERY original short
matching realizing the indicated geometry, with the fixed root and target.

PROVABLE AS STATED relative to the accepted source/transfer imports and the
new local finite certificates, pending FRESH independent local and actual
application review. No self-review or ledger promotion is performed.

The source is now final PASS in `FOURTEEN_HALL_REVIEW.json`, SHA256
`ff01d0f0888da2bcbb826ad9e585e001ce6d78ce3f3317b3451188bf2b8f18bd`.
Its three nonempty outputs are `FOURTEEN_HALL_remaining_v{1,7,31}_covered.bin`,
containing840/1188/1895 records. Each thirteen-byte record has six nonroot
even holes $Z$, seven odd holes $W$, free even root $u=0$, covered odd
target $v$, and $Z\cup W$ independent. No new matching-realizability
exclusion is applied by this package.

## Exact actual source rows

For a coordinate face $A$ containing $v$, put
$a=|Z\cap A|$, $b=|W\cap A|$. In even consumption use
$s=a+1-b$ originally free even sources in $Z\cap A$; in odd consumption
use $s=b-a-1$ sources in $W\cap A$ excluding the root mirror. Because
$v$ is covered, it is not a source hole. All legal subsets are enumerated.

| Local shape | Even row $(a,b);s$ | Odd row $(a,b);s$ | Actual B holes | Omissions | A holes per parity |
|---|---|---|---|---:|---:|
|T39, unconditional54|(3,1);3|(0,4);3|3:9|3|1|
|T2_10, forced13/14/19/27/28|(4,1);4|(0,5);4|2:10|4|1|
|T1_11, forced20/29/30|(5,1);5|(0,6);5|1:11|5|1|

In an even row, the actual B minority is $Z\cap B$ and majority
$(W\cap B)\cup Y$. In an odd row, the minority is $W\cap B$ and majority
$(Z\cap B)\cup Y$. Here $Y$ consists exactly of source mirrors and exactly
$Y$ is omitted. The root is consumed separately when it lies in B and
is not counted as a nonroot minority hole. These formulas, rather than
unmarked type names, determine the local input.

Every source is originally free. A source mirror cannot be an original
crossing port because its actual short crossing partner would be that
free source. Independence and root-mirror exclusion exclude original holes
there, so each mirror is originally internally B-covered. Original short
mates are distinct opposite-parity pendant endpoints outside transferred
endpoints. Simultaneous suppression is therefore path compression even
when a transferred edge joins two mirrors. The actual compressed matching
may be long or same-parity, which every imported local statement permits.

Completed A has one free hole per parity in every row. The accepted
arbitrary-matching endpoint input, with free even root and prescribed
covered odd target, supplies its A path. Covered crossing-target and
temporarily isolated-target boundaries are included. Artificial completion
edges may be long or same-parity and are eventually deleted. With no
original crossings use the explicit accepted five-direction Q6 endpoint
import, not a theorem applied independently to disconnected faces.

## Single and double cherry: actual compressed acyclicity

Use the FINAL accepted generic theorem
`HIGHER_FORCED_CHERRY_TRANSFER.md` Sections5--6 and
`HIGHER_FORCED_CHERRY_REVIEW.json`. Its exact local hypothesis is

$$\text{local cycle through arbitrary }F\quad\Longleftrightarrow\quad
F+R\text{ has no labelled cycle}.$$

For each actual marked hit, transport ALL paired $R$ edges together with
minority,majority and omissions. Every obstruction endpoint is covered,
outside the holes, and has the parity of $Y$. Reject the witness if the
global root lies in ANY actual obstruction endpoint. In projected labels,
root0 lies in B exactly when the target cut bit is1, and then its projected
label is0. This is a strict root-not-obstruction application. No alternative
root-in-obstruction route or original-matching forced-edge shortcut is used.

For clarity, the accepted generic proof's simultaneous safety argument is
fully discharged here. For a realizing original matching let $c$ be the
actual crossing count, $D$ its A completion, and $d=|D|$. Let $J_B$ be
those edges of the ACTUAL $R$ whose TWO endpoints are original B ports,
$j=|J_B|$. These edges use distinct ports, so $j\le\lfloor c/2\rfloor$.
Their short original A crossing partners give disjoint prescribed pairs
$J_A\subset D$. These pairs are legal completion vertices: an even-source
root in B is a source, not a port; an odd-source root is an even A port,
whereas obstruction endpoints then have odd A crossing partners. Root in
A is originally free. Thus no prescribed pair consumes the local root.

Writing $\delta=1$ when $u\in A$, completion parity and sizes give

$$d=(c+s)/2\quad(\delta=1),\qquad
d=(c+s-1)/2\quad(\delta=0).$$

All our source counts satisfy $s\ge3$, hence
$d>\lfloor c/2\rfloor\ge j$. At least one completion edge remains outside
$J_A$. Choose these prescribed pairs and pair the other completion
vertices arbitrarily; the endpoint theorem permits the resulting matching.

Any cycle in the ACTUAL compressed matching $L$ plus $R$ would lie wholly
in the common parity class of the obstruction endpoints. Original internal
short edges and suppressed mirror-mate edges leave that class; an edge
to the root cannot be in the cycle because the root is excluded. Every
edge of that cycle belonging to $L$ must therefore be a direct transfer
pair between two original ports. Lift its transferred paths to A and
replace its $J_B$ edges by their prescribed $J_A$ pairs. This would make
a cycle in the tagged A cycle with $D\setminus J_A$ deleted when the root
is in A, or in a subgraph of the original A path when the root is in B.
The former is a forest because $d>j$; the latter is a forest as a subgraph
of a path. The lifted paths have disjoint interiors, so a cycle, not merely
a repeated-vertex closed walk, would result. Contradiction.

Thus the actual $L+R$ is acyclic SIMULTANEOUSLY. For rows13/14 this excludes
alternating4-cycles between the two cherries as well as shared pairs;
checking $L\cap R=\varnothing$ alone would be insufficient. The exact
new local classification now applies to every realizing compressed $L$.

Row54 uses the unconditional local theorem and needs no obstruction test.
In every route expand all recorded paths/conflicts and delete the unique
endpoint tag. Every original matching edge and all64 vertices are restored;
completion edges disappear, compressed edges expand, and every surviving
new physical edge is short. The endpoints are the original prescribed
$u,v$, not favorable substitutes. Completion choices may depend on M,
which respects the universal-M/existential-path quantifier order.

## Complete producer scan, witness format and exact union

`FOURTEEN_FORCED_profile.py` tries every target-facing cut, every legal
source subset and all nine precise marked local inputs. Minority-anchor
translation and coordinate permutations move the entire marked geometry
and PAIRED $R$ synchronously. A vertex mask alone is not enough for the
two-cherry condition. Hits are identified by target and original source
index; overlapping witnesses do not create extra coverage.

Each selected witness is40 bytes, little-endian `<BIHBQIIIB4B7x`:

- byte0 target; bytes1--4 original thirteen-byte source-file index;
- bytes5--6 original61 local index; byte7 actual outer cut;
- bytes8--15 original-label source mask;
- bytes16--27 actual projected minority,majority,omission masks, uint32;
- byte28 number of forced pairs,0/1/2;
- bytes29--32 endpoints of those pairs consecutively, padded255 after
  the last actual endpoint; final7 bytes are padding.

The source index always refers to the COMMON original3923 domain. Unhit
records are copied unchanged in source order to
`FOURTEEN_FORCED_remaining_v{1,7,31}_covered.bin`.

| Target | Accepted source | Sufficient union | Remaining |
|---:|---:|---:|---:|
|1|840|600|240|
|7|1188|486|702|
|31|1895|250|1645|
|Total|3923|1336|2587|

The eight forced classes cover1326; unconditional54 covers10, all at v31;
their exact record-index intersection is0. Of the chosen forced witnesses,
1206 use one cherry and120 use two cherries. Chosen local counts are
13:60,14:60,19:306,20:288,27:171,28:135,29:135,30:171,54:10.
These are producer set/count results, requiring independent reconstruction
and exact residual-byte comparison before acceptance.

The producer author checks recompute all2304 forests/columns and688128
matrix bits, obtain the declared reduced ranks, replay all1336 actual
witnesses with simultaneous paired transports, and verify all three exact
source-order complements. These checks are not independent review.

## Gates and limits

The acyclic DAG is accepted Hall source plus accepted endpoint/uniform
single/multi-cherry transfer, together with the new independently checked
local certificates, implying actual sufficient subsets and their exact
union. No desired full fourteen-hole theorem, unrestricted local theorem
or new root-exception rule is used. All remaining2587 geometries stay OPEN;
their matching realizability is not asserted and lookup/rank failure is
not a negative certificate. Fresh review of the local and actual finite
gates remains mandatory. Full fourteen-hole and full P6 remain unproved
by this package, and no ledger/state is changed.

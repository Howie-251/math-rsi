# Twelve-hole four-type positive registry: actual coverage and greedy certificate scope

2026-11-01. ARIS proof-writer producer application. Local rank inputs and
this application require their separate independent acceptance. The
148 nonfull searches remain OPEN; none is a negative certificate. No
original profile, summary, search source, old raw input or main ledger
was modified.

## Exact input and sufficient statement

The input consists of215243 covered-target twelve-hole marked geometries,
in the three frozen HIGHER_Q5_FULL_T37_FORCED_union_remaining_h12_v{1,7,31}
_covered.bin files. The root is0, the odd target v is covered, Z consists
of five other even holes, W of six odd holes, and Z union W is independent.
Each eleven-byte record lists sorted Z then sorted W in original labels.
The earlier reductions/censuses and accepted ten-hole predecessor are
separate source-bound gates; this scan does not itself accept those gates.

For every original short Q6 matching realizing a record, an actual cut
and legal source set is sufficient if its resulting marked B geometry
is a common cube-automorphic image of one of the selected FULL-RANK
candidate local inputs. Required B matching edges may be long or same-
parity; the local theorem must quantify over all such complete-graph
matchings and preserve its marked omissions. No favorable original
matching or unknown mate is selected by the hole-geometry witness.

## Exact four local types and actual Q6 rows

| Type | Minority/majority holes | Omitted majority | Covered endpoints | Rank needed | Short forest edges | Q6(a,b) rows |
|---|---|---:|---:|---:|---:|---|
|T28|2/8|3|22|1024|18|(3,1),(0,4)|
|T19|1/9|4|22|1024|17|(4,1),(0,5)|
|T84|0/8|4|24|2048|16|(5,2),(1,6)|
|T105|0/10|5|22|1024|16|(5,1),(0,6)|

The candidate universal local theorems are defined by explicit minority,
majority and omitted sets in TWELVE_NEW_TYPES_profile.json and the local
rank certificates. The generic matching-connectivity rank upper bound
on n covered endpoints is2^(n/2-1). Legal selected forests have omitted
degree0, included-hole degree2, covered degree1 and no cycles; expanding
a connecting endpoint matching gives the local single cycle. Full rank
on valid complete-graph columns makes their rows span the complete
connectivity row space, and every arbitrary matching column is nonzero
by cyclically linking its oriented edges. These are candidate LOCAL
proofs, not a conclusion from producer full_rank flags alone.

There are380 actual marked local orbits in the source domain. The final
producer summary has232 full-rank and148 nonfull rows. This application
uses only the232 full-rank rows to determine a complete positive union,
then reduces the needed proof registry to111 full-rank rows with the SAME
union. Nonfull and unselected positive rows are not premises of the
selected application theorem. No unrestricted theorem for any of these
four local types is asserted.

## Transfer proof and legality

For a target-oriented cut A let a=|Z intersect A|, b=|W intersect A|.
Even-consumption rows select s=a+1-b sources from Z intersect A; the table
has b=1 or2, s=3,4 or5. Odd-consumption rows select s=b-a-1 sources from
W intersect A excluding its possible mirror to root0; the table has
a=0 or1 and s=3,4 or5. Since v is covered it is not a source hole.
For odd rows b-s=a+1>=1, so at most one root-mirror exclusion leaves
enough sources. The code explicitly enumerates legal source subsets.

All rows fall within the accepted uniform transfer's ORIGINAL A endpoint
ranges: b<=3 in even consumption, a<=2 in odd consumption. Their completed
A matching has balanced b:b or(a+1):(a+1) holes; here only balanced2 or4
total holes arise. Choose the free even A root and completion matching
exactly as in that accepted proof, including the even-port surplus when
root0 is in B. Covered v remains a valid target even if it is a crossing
port. For zero original crossings use the accepted five-direction theorem.

Every bridge mirror is distinct and internally B-covered: its source is
an original free short mirror, independence excludes another original
hole, and source choice excludes root0. After deleting completion edges,
attaching actual crossings/bridges and adding the endpoint tag, the accepted
construction is a forest. Conflicts occur only at the same-parity mirrors;
their distinct original short mates are opposite-parity pendant endpoints
outside the transferred endpoint set, so suppression cannot create a
cycle. The final B matching has exactly the actual projected minority,
majority and marked mirror omissions encoded in the witness.

Its candidate local theorem supplies a cycle on B minus those mirrors.
Expand all conflict and A paths and delete the tag. Every original required
edge and all Q6 vertices are restored, with the prescribed root/target
endpoints. Artificial completions were deleted, compressed edges expanded,
and the tag removed. All surviving new physical edges are short. Thus
each marked positive-orbit witness is universally sufficient once its
local and application acceptance gates pass.

## Actual synchronous marked lookup and all positive hit sets

TWELVE_NEW_TYPES_coverage.py imports or executes no profile/search program.
It reads the frozen explicit380-row geometry registry and final summary,
requires completed=requested=380, and verifies the required rank for each
used full-rank row. It independently constructs synchronous marked images
using every coordinate permutation and an anchor translation: a minority
hole when present, otherwise a marked omitted hole. The runtime actual
geometry is normalized by the same rule. Minority,majority and omissions
are always transformed TOGETHER. Omitting the marked set from a lookup
would be invalid and is not done.

For every original record it examines all six actual target-oriented cuts
and every legal source subset for the four type shapes. It projects away
only that cut coordinate and forms the actual B minority, majority and
mirror-omission masks. For EACH positive local orbit hit it retains one
concrete cut/source witness; it does not stop at the first local orbit.
This yields541463 distinct original-record/positive-orbit hits. All232
per-orbit record counts agree exactly with the independently reconstructed
lookup/actual projection sets and the supplied profile counts.

The complete positive hits are stored as28-byte records in
TWELVE_NEW_TYPES_positive_hits.bin: v uint8, original file record index
uint32, local orbit uint16, outer cut uint8, original source-mask uint64,
then actual local minority,majority,omission masks as three uint32 values,
all little-endian. Each original record can have several orbit hits, but
each orbit appears at most once for that record. These full sets, not
producer coverage totals, define the positive union.

## Greedy sufficient registry and exact remaining domain

Greedy selection repeatedly chooses the positive orbit covering most
currently uncovered ORIGINAL RECORD IDs, breaking ties by smaller index.
It stops when its union equals that of ALL232 positive orbits. The result
contains111 rows, recorded with exact geometry/prefix/rank in
TWELVE_NEW_TYPES_greedy_registry.json. No minimum-cardinality claim is
made. The other121 full-rank rows are producer reserves, not needed by
this application's sufficient registry. Root can freeze and independently
audit only these111 selected local certificates.

One chosen-greedy actual witness per covered original record is saved
with the same28-byte format in TWELVE_NEW_TYPES_selected_witnesses.bin.
The output copies every uncovered original eleven-byte record unchanged
and in original order.

| Covered target | Input | Positive union | Still OPEN |
|---:|---:|---:|---:|
|1|59684|51652|8032|
|7|68385|56724|11661|
|31|87174|69462|17712|
|Total|215243|177838|37405|

The exact new raw names are TWELVE_NEW_TYPES_positive_remaining_v{1,7,31}.bin.
All inputs here are covered-target geometries; no free target is counted
or claimed by this application. Fresh review must replay complete marked
lookups, source legality, all record/orbit sets and greedy union equality,
and verify complete residual byte/set equality, not merely subtraction
of totals. The application manifest pins all these outputs and the local
selected registry boundary.

## Open scope and dependency boundary

The dependency DAG is accepted balanced2/4-hole endpoint and uniform
transfer + the selected111 candidate local universal rank theorems ->
actual cut/source sufficient witnesses -> positive union/residual.
No desired complete twelve-hole theorem is fed into a local proof.
Upstream accepted/reviewed input-domain gates remain separately bound.

The37405 residual records are OPEN obligations, not counterexamples;
some may be unrealizable short-matching hole sets. The148 nonfull local
rank cases likewise remain OPEN. No rank0 or search cap is used to infer
nonexistence. All new local certificates and application counts remain
producer evidence until fresh independent acceptance. Full twelve-hole,
14--18-hole layers and full P6 are not closed by this package, and no
main state was changed.

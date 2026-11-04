# Twelve-hole residual: conservative accepted-Q5 registry reuse

2026-11-01. ARIS proof-writer producer package. The theorem below is
relative to accepted local imports; the new lookup/census needs fresh
independent review. No frozen near-balanced proof, local theorem, T26/T63
input or accepted ledger was changed. Full twelve-hole and P6 remain OPEN.

## Exact general source-transfer theorem

Let M be a short Q6 matching with twelve holes, free even root u=0 and
any opposite-parity target v, free or covered. Its other even holes Z
have size5, its odd holes W size6, and Z union W is independent. Choose
a coordinate face A containing v, with a=|Z intersect A|, b=|W intersect A|.
Either construction suffices when the actual marked B geometry is an
accepted universal local matching input in the table below:

* Even consumption: b>=1 and s=a+1-b>=0. Choose s sources S from Z
  intersect A. B minority holes are Z intersect B, majority holes are
  (W intersect B) union Y, with Y the s short source mirrors; omit Y.
* Odd consumption: t=b-a-1>=1. Choose t sources S from W intersect A
  excluding v when free and excluding the root mirror. B minority holes
  are W intersect B, majority holes are (Z intersect B) union Y; omit Y.

The selected source set must exist. This is a statement for every original
matching realizing the geometry; it is not a favorable-matching search.

## Replay with full balanced Q5 endpoint inputs

For zero original crossings use the accepted five-direction theorem.
Otherwise let X_A,X_B be actual distinct ports and delta indicate u in A.
In even consumption, if delta=1 choose r=u and pair X_A union S into D.
If delta=0 and s>=1 choose r in S and pair X_A union (S minus {r}).
If delta=0 and s=0, shortness gives even-port surplus1; choose an even
port r and pair the rest. The completed A matching has exactly b holes
per parity with free r. Since b>=1, the accepted FULL balanced Q5 endpoint
theorem applies, with covered or free odd target v. Even sources cannot
consume v. The old b<=3 restriction served only the old endpoint import.

In odd consumption, choose r=u and pair X_A union S when delta=1.
When delta=0 the even-port surplus is t+1>0; choose an even port r and
pair (X_A minus {r}) union S. The completed A matching has exactly a+1
holes per parity with r free. The legal source exclusions retain v.
The full endpoint theorem applies for every a, extending its former
limited a<=2 input. Pairing-set parity is the original degree-counting
identity, and arbitrary long or same-parity completion edges are allowed.

Every mirror is distinct and internally B-covered: independence excludes
opposite-parity holes, a free original short mirror excludes a crossing
port, and source choice excludes u. Delete D from the A path and attach
all crossings/bridges. When u is in A the positive-crossing parity identities
make D nonempty; when u is in B it is initially unattached. The tagged uv
closure is a forest, including D-empty and target-port boundaries already
present in the accepted uniform proof. Compress the A paths.

The only B conflicts are the same-parity mirrors Y. Each has a distinct
original internally covered pendant mate of opposite parity, outside Y,
ports, root and original holes. Conflict components therefore are paths
and cannot close a cycle, even when a transferred edge joins two mirrors.
Suppress them, retaining all path data and the tag. The resulting arbitrary
B matching has holes exactly (H_B minus {u}) union Y and omissions Y.
Apply its actual accepted marked theorem. Expand all recorded paths and
delete the tag. All original edges and prescribed endpoints are restored;
D was deleted, compressed edges expanded, and the tag removed. Every
surviving new physical edge is short. This proves the theorem for free
and covered v without extrapolating the old numerical endpoint bounds.

## Accepted marked local inputs and their precise scope

| Family code | Actual B input |
|---:|---|
|1|Complete T44: four same-parity holes, any two prescribed omissions|
|2|T63 with actual marked2/4-hole,1/2-omission split|
|3|The exact55 T26 rank marked orbits, minority2/majority6, omit2 majority|
|4|Accepted old24 T15 cores/full split plus exact15 new T15 rank orbits|
|5|T15 short augmentation at an included majority hole to complete T44|
|6|Exact10 UNFORCED T17 rank marked inputs, minority1/majority7, omit3 majority|
|7|Exact7 additional same-parity T63 rank marked inputs and their common cube images|

All their required matchings may be arbitrary complete-graph matchings,
including the long and same-parity edges created by compression. Marked
omissions are transported together with the hole geometry. T26 lookup
normalizes either minority to0 and applies every coordinate permutation.
T15/T17 normalize their singleton minority to0. T63 rank lookup uses all
common translations and coordinate permutations, including parity reversal.
T63 split is tested in the actual five coordinates after the outer cut.

The old T15 lookup is the frozen independently generated table from
TEN_HOLE_COVERED_PARTIAL_REVIEW. No unrestricted same-face shortcut is
used. Family5 adds a short edge from the minority hole to a nonomitted
included majority hole, leaving four majority holes retaining both marked
omissions; T44 then applies. That added edge is short relative to F.

The seven CONDITIONAL forced-T17 inputs are excluded here. Original M_B
lacking their same-parity obstruction is not a proof that compressed L
lacks it. Their earlier root-not-obstruction Q6 application had a specific
ten-hole/covered-target scope, which is not silently extended by this filter.

## Complete producer scan and concrete witnesses

The source is the SIX frozen near-balanced eleven-byte-record residual
files, free/covered at v=1,7,31, totaling8008722 geometries. Their initial
independent-domain reduction uses accepted complete ten-hole Q6. That
does not itself accept the new near-balanced census or this lookup scan.

HIGHER_Q5_FULL_build_lookups.py reads final PASS reviews. The producer
filter tries every actual target-oriented cut, determines exact source
number and parity, rejects even b=0, and tries every legal source subset
whose local hole counts can use one of the table's families. It projects
only the outer coordinate and tests the ACTUAL minority/majority/omission
masks. Each success is sufficient for every realizing short matching.

Every success writes a26-byte witness: original input index uint32,
outer cut byte, family byte, original-label source mask uint64, then
three actual local minority/majority/omission masks uint32, little-endian.
The first success is retained. Each unhit eleven-byte record is copied
unchanged and in original order to its corresponding new remaining file.
No matching-feasibility or root-adjacency filter is added at this stage.

| Target/status | Input | Covered | Still OPEN |
|---|---:|---:|---:|
|v1 covered|2364029|2262675|101354|
|v7 covered|2632038|2520645|111393|
|v31 covered|2824049|2688560|135489|
|v1 free|0|0|0|
|v7 free|80622|80595|27|
|v31 free|107984|107964|20|
|Total|8008722|7660439|348283|

First successful family counts are code1:25788, code2:120791,
code3:3919665, code4:2856110, code5:0, code6:690981, code7:47104.
The residual has348236 covered-target and47 free-target geometries.
These are producer counts requiring independent lookup reconstruction,
all actual witness replay and exact complete residual byte/set equality.
No accepted coverage decrement follows from reported counts alone.

## Shared next inputs and scope limits

The new raw files are
HIGHER_Q5_FULL_reuse_remaining_h12_v{1,7,31}_{covered,free}.bin, with
matching reuse_witness binaries. They are a useful next-profile domain;
new T37 rank inputs and generalized forced-T17 applications are separate
obligations. These348283 are marked hole geometries, not matching counts
or counterexamples, and some may be unrealizable by a short matching.

The acyclic DAG is accepted local Q5 endpoint/marked theorem -> general
source transfer -> actual projection/witness census. Its independent-hole
preprocessing additionally imports complete ten-hole Q6. No desired
twelve-hole theorem is fed into any local premise. Full twelve-hole,
subsequent14--18-hole layers and full P6 remain OPEN. No previously frozen
source, accepted report, producer input or main state was modified.

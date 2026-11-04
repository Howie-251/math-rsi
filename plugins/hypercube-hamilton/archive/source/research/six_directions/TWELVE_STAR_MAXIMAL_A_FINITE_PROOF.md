# Root-star maximal A-matchings: finite positive mixed-opening certificate

2026-11-02. Producer finite package pending fresh independent domain and
certificate review. This proves a LOCAL finite completion assertion once
its checks pass. The separate maximal-extension reduction and final Q6
assembly are additional gates. Full root-star Q6, twelve-hole Q6 and P6
are NOT declared closed here. No existing proof/state file was changed.

## Exact finite local assertion

Use Q5 labels0,...,31 on A. Let E be its15 nonzero even vertices, O its11
odd vertices of weight at least3, and K0=E union O. Thus A's original
holes are0 and the five units1,2,4,8,16. Original A matching edges must
be SHORT edges of this26-vertex induced bipartite graph. Fix one T row:

| Index | Mandatory internally covered odd set T | Own producer count of maximal A-matchings | T-stabilizer order | Own orbit count |
|---:|---|---:|---:|---:|
|0|7,11,13,19,21|629747|4|157690|
|1|7,11,13,19,31|598097|2|299245|
|2|7,11,13,22,31|598067|2|299206|
|3|7,11,19,28,31|598037|12|49986|
|4|7,11,21,25,31|598067|8|74898|
|5|7,11,21,26,31|598037|2|299053|

Let M_A range over EVERY inclusion-maximal matching of that SHORT graph
which covers T. Maximal means that no short edge has both endpoints
unmatched; it does NOT mean maximum cardinality. Then a certificate exists
with q an unmatched even vertex, t in T minus {31}, and distinct unit
holes w,b, such that q--t is short and the following holds.

If31 is internally matched in M_A to h, replace31--h by w--h, giving
L_A. If31 is unmatched in M_A, put L_A=M_A. In either case L_A is a
bipartite matching, possibly with one long w--h edge. There is a supplied
legal short forest S on Q5 minus {0,31}, containing q--t, with degree2
at q,b and degree1 at every other retained vertex, such that the LABELLED
union S+L_A has no cycle. The exact (q,t,w,b) also has an accepted actual
marked B classification as specified below.

Consequently there is SOME bipartite artificial completion D on the
uncovered terminal set such that S+L_A+D is one simple30-cycle, containing
L_A+D and the optional opening edge q--t. The proof is existential in D
AFTER the original maximal M_A and its witness are known. It does not
assert the stronger statement for every arbitrary prescribed D.

## Complete domain boundary and independent cardinality requirement

Every short edge of K0 joins one of O's11 vertices to one of E's15.
Specifying each odd vertex's unique even partner or an unmatched sentinel
determines a matching uniquely. The mandatory odd vertices T may not
take the unmatched option. No even vertex may be used twice. After all
odd choices, maximality is exactly that every unmatched odd vertex has
all of its short even neighbors already used. These conditions define
the finite domain without any B-matching or global-realizability filter.

The producer enumerates this domain and separately counts it in another
own count program, with matching results. Both use the odd-partner
description; this is NOT an independent audit or an independent DP.
Fresh acceptance must either independently enumerate the entire domain
or compute its exact cardinality, and verify that each certificate input
is legal, mandatory-T-covering, maximal and unique. Equality of that
independently determined cardinality with the valid unique input set then
proves coverage. The producer counts above are proposed exact counts,
not an external accepted oracle.

There are3620052 records across the six domains. Matchings have9,10 or11
edges: the unmatched odd counts are2,1,0 and the unmatched even counts
are6,5,4, giving8,6,4 total ports. In general these counts are11-m and15-m,
and their difference is4. The group statistics use all coordinate
permutations fixing T, which automatically fix0,31 and the unit-hole set.
The orbit-size counts are supplemental and are not needed for positivity
or complete input coverage after the direct domain checks.

## Finite witness representation

Each TWELVE_STAR_MAXIMAL_A_full_i_certificates.bin has one32-byte record
per maximal matching, in deterministic producer enumeration order:

| Bytes, zero-based | Meaning |
|---|---|
|0..21|m sorted unordered original M_A edges, then255 padding to22bytes|
|22|edge count m, between9 and11|
|23,24,25,26|actual q,t,w,b labels|
|27|opening case ID, either0 or3|
|28..29|uint16 little-endian index of the selected positive S record|
|30|coordinate-permutation index,0..119, lexicographic permutations|
|31|1 iff31 originally internally matched;0 otherwise|

The six complete binaries total115841664bytes. Every original M_A is
stored explicitly; no reliance on the producer's leaf index is needed
to verify legality or uniqueness. No failed or unknown record is present.
Each full-run metadata says the complete domain was reached below its
1000000 limit, and the associated unhit file is empty. Those producer
fields do not substitute for independent domain coverage checks.

## Only positive opening forests are used, never their deficient rank

Two SOURCE forest files are used:

* TWELVE_ROOT_STAR_OPENING_case_00_forests.bin, canonical(q,b,t)=(3,4,7).
* TWELVE_ROOT_STAR_OPENING_case_03_forests.bin, canonical(q,b,t)=(15,1,7).

Each contains8031 records of32bytes:16 unordered short edges. Every S
must be independently checked for edge uniqueness/shortness, omission of
0,31, degree2 at canonical q,b, degree1 elsewhere, absence of cycles,
and presence of the canonical opening q--t. Such a forest has14 path
components. The actual witness transports all vertices by its declared
coordinate permutation, sending the canonical(q,b,t) to the actual
tuple and preserving0,31. Its actual q is unmatched in M_A and t belongs
to mandatory T minus {31}, so t is internally covered and cannot be a
selected source or crossing port.

The source files happened to be selected during rank probes with rank8031,
but THIS FINITE PROOF DOES NOT USE THAT RANK, its closeness to8192, a basis
claim, or exhaustion of legal S. It uses only each chosen S's positive
graph properties and its compatibility with THIS M_A. Unused source
forests, matrices and the forest generator's completeness are irrelevant.

## Direct compatibility and the bipartite completion lemma

Form L_A as stated. The original matching is short and bipartite. In
the internal-target case,31 is odd and h even; the replacement w odd--h
even is bipartite and legal because w was a hole. In the target-port case
there is no internal replacement. Vertex31 and0 are absent from both
S and L_A, and q,b are uncovered in L_A. Distinct matching edges give
degree at most2 in S+L_A. All graph edges retain LABELS: if an L_A edge
equals an S edge, they form a two-edge cycle and the witness is rejected,
rather than collapsed into one physical edge.

The producer tests cycles by first contracting S's14 paths, then adding
each L_A edge with a14-component DSU. Every union must join distinct
components. A fresh checker may instead insert all actual S and L_A
edges directly into a32-vertex DSU; the acyclicity statement is identical.
No assertion about arbitrary prescribed completed matching is inferred
from a rank probe.

Since acyclic, S+L_A consists of14-m paths, where m=|M_A|. Their endpoint
set is exactly K_open minus V(L_A), with
K_open=Q5 minus {0,q,31,b}. It has14-m even and14-m odd endpoints.
The balance follows because K_open has14 vertices of each parity and
L_A has m opposite-parity pairs. Here14-m is3,4 or5, so several components
remain. Endpoints are precisely the original completion domain: in the
internal case (X_A minus {q}) union the other three unit holes S_sources;
in the port case replace original31 port by virtual w first. This identity
does not assume the virtual crossing is short.

**Bipartite path-joining lemma.** For disjoint paths with equally many
even and odd endpoints, a bipartite matching of the endpoints can join
all paths into one cycle when the nondegenerate component count here is
at least3. The numbers of EE-ended and OO-ended paths are equal. If both
are zero, orient all EO paths from E to O and concatenate them cyclically
by O--E edges. Otherwise alternate the EE and OO paths in a cycle using
opposite-color connecting edges, then insert each EO path into a suitable
connector with its orientation chosen accordingly. Each endpoint gets
one connector; connectors join distinct path components. Thus no connector
duplicates a forest edge. Call their matching D.

D is disjoint from L_A's covered vertices and avoids q,b,0,31. It gives
exactly the bipartite completion required by the structured A matching.
The resulting simple30-cycle retains every L_A edge, every D edge, and
q--t. The opening edge lies in S and cannot be in D or L_A because q
is an unmatched port and t was mandatory internally covered. This proves
the existential completion statement from a verified finite witness.

## Exact accepted B geometry for each retained option

The geometric option file is drawn from cases0 or3 of
TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json. Each actual option determines
Y={1,2,4,8,16} minus {w,b}, actual B minority0, majority
(T minus {t}) union Y, omissions Y and forced pair {w,b}. All657 retained
geometric options across the six families have been mapped synchronously
to exact already accepted forced-T17 classes in the old7 registry, the
new15 extra-forced registry, or the new10 star-B registry. Their actual
majority/omission/pair maps are in TWELVE_STAR_MAXIMAL_A_B_gates.json;
they must be independently verified against the bound final PASS scopes.
Stale producer labels such as pending in the old exploratory options file
are not used as acceptance gates.

The B local theorem is CONDITIONAL iff its actual required matching lacks
the actual forced edge. The finite A witness by itself does not prove
this absence in a global transfer. That fact, the opening/deletion
expansion, restoration of a real or virtual auxiliary crossing, and the
maximal-extension reduction are explicitly separate obligations.

## Strict acceptance and scope boundary

The producer's own count agrees with its complete certificate record
counts; all3620052 records are positive and zero are unhit. Independent
acceptance still requires legal/unique/maximal/T-covered source inputs,
independent exact-domain cardinality, chosen forest validity and map,
acyclic labelled S+L_A and balanced actual D-domain, and exact accepted
B-class membership. The manifest pins all source/certificate bytes.

This package deliberately does NOT assume the candidate monotonic
extension lemma from a nonmaximal original M_A to M_Amax. It also does
not replace a complete Q6 construction/geometry transport/assembly audit.
Even final PASS here proves only the explicit local maximal-matching
completion assertion. Full235 star geometries, complete twelve-hole Q6
and full P6 must pass their separate mathematical gates before closure.
No unhit S family or deficient rank is ever a counterexample claim.

# T17 rank batch and root-not-obstruction transfer: fresh independent review

2026-11-01. Reviewer `/root/t17_safe_transfer_review`; user-selected
`gpt-6.1-sol`, reasoning `high`. ARIS proof-checker assurance:
**same-family / provisional**.

**PASS, modulo the explicitly imported matching-connectivity upper bound and
established local endpoint/uniform-transfer inputs.** All seventeen marked
local statements are proved in their stated arbitrary-matching scope. The new
root-not-obstruction transfer is valid for every realizing original short
matching and covered odd target, including targets that are crossing ports.
The actual accepted 4096-record domain has disjoint sufficient classes of
2598 unforced and 1036 additional safe forced records, leaving exactly 462.
No T15 result was used. Full T17, full ten-hole coverage and full P6 remain
OPEN within this audit's scope; no producer proof or production state changed.

## Frozen inputs and independence

Reviewed manifest SHA256:
`77122b232fd586043f6960ce466d465cbbd5ccce97aaac72dfecf8418bcdef6b`.
All 166 manifest-bound files were independently hashed against current bytes.
The complete theorem-bearing inputs are `Q5_T17_RANK_BATCH_PROOF.md` and
`Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md`; their hashes are in the JSON report.
The 17 explicit J/U rows were copied from the theorem statement and checked
against configs, so acceptance is tied to those rows rather than mutable IDs.

New independent checkers are `Q5_T17_RANK_BATCH_REVIEW_check.cpp` and
`Q5_T17_RANK_BATCH_REVIEW_check.py`. No producer verifier, search executable,
coverage script or producer self-check was executed. The C++ checker was
compiled with `D:/mingw64/bin/g++.exe -O3 -std=c++17` and run without NDEBUG;
the Python orchestration used `D:/anaconda/python.exe`.
The new checker recomputes matrix entries and performs its own increasing-
column Gaussian elimination. Saved producer pivots/combinations are separately
verified as certificates, rather than taken as the computed rank.

The uniform transfer and its accepted review were read. Its exact arbitrary-
matching balanced-two-hole endpoint input, zero-crossing five-direction import,
and graph expansion conventions are inherited explicitly. The mathematical
rank import is the full complete-graph matching-connectivity bound
rank_GF2(H_t) <= 2^(t/2-1), for all even t, identified in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. Its arbitrary-matching scope covers
both t=24 and t=22; no bipartite restriction is introduced here.

Dependency DAG: rank upper bound + independently checked short forests and
matrices -> 17 local classifications; local endpoint import -> A path ->
completion-avoidance -> conditional B input -> tagged expansion. Accepted T26
residual -> finite actual projection census -> sufficient Q6 class. There is
no backward dependency on a ten-hole theorem, P6, or T15.

## Local proof ledger

For every listed J/U and every perfect matching F on
K=Q5 minus ({0} union J), the local conclusion quantifies over arbitrary
complete-graph edges, including long and same-parity edges.

| Obligation | Independent discharge |
|---|---|
| L01 Legal selected forests | Each of 27648 records has 17 distinct short edges; DSU insertion detects every cycle; degrees are zero on U, two on five included holes, one on all 24 covered terminals. Thus all nontrivial components are terminal-to-terminal paths and no closed hole component is hidden. |
| L02 Actual endpoint pairing | Every full 24-label pairing is a perfect matching of exactly K, and its unordered pairs equal actual connected terminal pairs of that forest. |
| L03 Forced cherry | All seven forced rows have U={1,2,4}, p=8,q=16. Both edges 0--8 and 0--16 and the full pair {8,16} are present in every selected forest. Geometry forces this cherry in every admissible forest, because 0 has only these two neighbors in Q5 minus U. |
| L04 Reduced pairing | Each forced reduced pairing is exactly its verified full pairing with {8,16} removed; p,q remain present in the full forest. The domain is K minus {p,q}, with 22 labels. |
| L05 Columns | Every supplied column is an actual perfect matching on the exact 24- or 22-label domain, with no repeated or forbidden endpoint. No shortness or parity restriction is assumed. |
| L06 Connectivity bits | All 49283072 bits are recomputed from connectedness of the labeled union of the two matchings. These unions have degree two with matching labels retained. A common pair creates a separate two-edge component and fails the global connectedness test on these domains. |
| L07 Exact rank | Fresh elimination obtains rank2048 for each of ten unforced matrices and rank1024 for each of seven reduced matrices. Every supplied pivot equals the indicated XOR of original matrix rows, has its designated highest bit, and no higher bit. |
| L08 Full row-space span | Independence after restriction to supplied columns implies independence in the full H_t. The imported upper bound makes these N independent rows a basis of the full row space. No exhaustive enumeration of forests or arbitrary F is needed. |
| L09 Arbitrary F has a nonzero column | Order and orient the edges of F, and pair the end of each with the start of the next cyclically. Its union with F is one alternating cycle. Therefore some basis row connects every F. |
| L10 Expansion | Expanding disjoint short forest paths in that connected alternating cycle yields a simple cycle through the 24 terminals plus five included holes, of length29. A direct duplicated short required edge would have been an isolated common-pair component, already excluded. |
| L11 Forced negative direction | If F contains pq, the required pq edge and forced p--0--q path fill all three vertices' cycle degrees, producing an isolated triangle. A spanning29-cycle is impossible. This is an analytic impossibility, not a search inference. |
| L12 Forced positive direction | If pq is absent, a=F(p), b=F(q) are distinct and outside {p,q}; replacing pa,qb by ab gives a valid perfect matching F' on the 22-label domain. Since P contains pq, suppressing the labeled path a--p--q--b preserves components and the single-cycle property in F+P. The reduced full-rank basis connects F'; use the associated full forest and undo suppression. This recovers every required F edge and the vertex0. |

Ten matrices contribute 41943040 connectivity bits; seven contribute7340032;
total49283072. Forest counts are20480+7168=27648.
Ranks are derived by exact arithmetic, with no probabilistic acceptance.

## New universal completion-avoidance lemma

Canonical statement: for every original short matching M in Q6 with ten
holes {u} union Z union W, u even/free, covered odd target v, Z union W
independent, and any cut/source choice of row(3,1) or(0,4) whose actual B
geometry is one of the seven forced marked inputs, if its actual obstruction
pair excludes u, there exists a Hamilton u--v extension through M with only
short new edges. The choice of D may depend on M and this projection; a
single fixed D for all M is neither needed nor claimed.

| Obligation | Independent discharge |
|---|---|
| T01 Zero crossings | c=0 is the explicit established five-direction endpoint import. No artificial port argument is needed. |
| T02 Source legality | Row(3,1) uses the three even A holes. Row(0,4) uses any three of four odd A holes excluding the root mirror. Covered v excludes no hole source; at most one root mirror is excluded. |
| T03 Completion sizes | For delta=1, c is positive odd, |D|=(c+3)/2>=2. For delta=0 in row(3,1), c positive even and |D|=(c+2)/2>=2, with r in S. For delta=0 in row(0,4), even-port surplus4 implies c>=4 and |D|=(c+2)/2>=3, with r an even port. |
| T04 Endpoint import | These completions leave exactly one even and one odd hole; r is free/even and v covered/odd. Every D endpoint is free for M_A and distinct from the remaining root. Long/same-parity D is allowed by the local import. |
| T05 Bridge mates | Each y in Y has a free original mirror, is not a crossing port, and is not an original hole by independence and root-mirror exclusion. Its original internal mate h_y exists, is distinct for different y, has parity opposite Y, and is neither a port, root, nor member of Y. |
| T06 Actual obstruction endpoints | p,q have Y's parity, lie outside Y and final holes, and are originally covered because u is excluded. If not ports they have unchanged internal matching edges, whose opposite-parity mates cannot be in Y. |
| T07 Suppression classification | M_B does not contain same-parity pq. The only T/M_B overlaps are Y. Each conflict component consists of one T edge, with a pendant h_y attached at each Y endpoint that it has. Port--Y becomes port--h_y; Y--Y becomes h_y--h_z; edges incident to the root retain that root. None creates pq. Thus L contains pq only if both are ports and their direct T pairing is pq. This explicitly concerns the compressed L, not merely original M_B. |
| T08 Legal prescribed edge | When both are ports, their actual crossing partners p',q' are distinct completion vertices. In row(3,1), r is u or a source hole, hence not a port. In row(0,4),delta=0, p,q are even B vertices, so p',q' are odd and cannot equal the chosen even r. In delta=1, r=u is free. Therefore prescribe p'q' in D and pair the remaining even number of vertices arbitrarily. |
| T09 Delta1 separation | The Hamilton u--v A path plus tagged uv is a simple32-cycle; its endpoint edge cannot already be a path edge. Delete all D edges. The prescribed p'q' arc is removed and the other arc contains a second D edge by T03. Hence p',q' are in distinct A components. All crossings/bridges attach distinct B leaves, so cannot merge those components. |
| T10 Delta0 separation | Deleting the prescribed p'q' edge from the simple r--v A path separates its endpoints; more deletions cannot reconnect them. Root u is a new B leaf at v, and all crossing and source attachments have distinct B endpoints. If r lies in S, its bridge is still just a leaf attachment. |
| T11 Target-port degeneracy | When v is a port and incident with the prescribed D edge, it can become isolated after deletion. In delta1 its tagged-cycle degree remains accounted for. In delta0 the tag and crossing give u--v--bar(v), whose root endpoint is not p or q. The other prescribed endpoint remains in a different A component. Thus this boundary does not create the forbidden port--port transfer segment. No assertion that all A vertices remain nonisolated before attachments is used. |
| T12 Final B matching and expansion | T09/T10 give pq absent from T; T07 gives pq absent from actual compressed L. The forced local classification therefore applies. Its29-cycle expands through all bridge mates and the32 A vertices to a tagged64-cycle, retaining original M edges. D was deleted; compressed artificial edges are expanded. Deleting tagged uv produces the required Hamilton path with only short new edges. |

Counterexample-first checks: a single prescribed deletion from a cycle would
leave its endpoints connected, so a proof omitting |D|>=2 fails; the actual
parameter table rules out that case. If u belongs to the obstruction pair
and v is its other endpoint's crossing partner, the isolated-target segment
u--v--bar(v) forces exactly that forbidden T edge. This explains and respects
the explicit root exclusion. The original M_B merely lacking pq was not used
as a substitute for T07--T11. There are no remaining key-lemma gaps.

## Exhaustive finite geometry application

Input bytes are the three accepted independent
`Q5_T26_RANK_BATCH_REVIEW_remaining_v*.bin` files. Their4096 records are unique
within each v domain, have4 even nonroot and5 odd holes, exclude the covered
target, and satisfy the stated independent-hole assumption. Candidate-source
bytes were compared to these accepted bytes exactly, with no feasibility
filter on M.

For every record the checker considers all six actual cuts, both permissible
rows, and all legal three-source choices. It translates by the unique actual
B minority, deletes the cut coordinate, and tests the actual marked majority
and omitted sets under a common coordinate permutation. Its orbit dictionary
is generated from all120 permutations of each of the17 statement rows; it
does not trust producer canonicalization or marginal orbit totals. Actual
obstruction endpoints are lifted back to Q6 and tested against root0.

The independent census finds8859 supported unforced projections and6718
supported forced projections, with multiplicities across inputs/cuts/sources.
Every retained unforced witness is validated; all forced choices for every
forced-only record are reconstructed and compared as exact sets; each of the
1036 chosen safe witnesses is legal and has root outside its actual pair.
No root-in-obstruction projection is accepted.

| v | Accepted input | Unforced net | Additional safe forced | Exact remaining |
|---:|---:|---:|---:|---:|
|1|910|570|220|120|
|7|1476|918|396|162|
|31|1710|1110|420|180|
|Total|4096|2598|1036|462|

The exact unresolved records, preserving source order and bytes, are saved as
`Q5_T17_RANK_BATCH_REVIEW_remaining_v1.bin`,
`Q5_T17_RANK_BATCH_REVIEW_remaining_v7.bin`, and
`Q5_T17_RANK_BATCH_REVIEW_remaining_v31.bin`.
They equal producer `after_safe_forced` residual bytes exactly, and the
intermediate1498-record unforced remainder also agrees byte for byte.
SHA256 digests are fixed in the report JSON. These462 have no supported T17
projection of the specified rows, not merely no selected safe witness.

## Acceptance and remaining scope

All L01--L12 and T01--T12 obligations are discharged modulo the named imports;
all independent deterministic checks PASS. Issues: none. No unsupported
nonexistence claim follows from capped search; only the forced-triangle
negative statement is accepted. The audit accepts the local classifications,
the stated root-not-obstruction universal transfer, and its exact sufficient
3634-record application. Root-in-obstruction templates, unrestricted T17,
the remaining462 records and whole ten-hole/P6 closure are outside this
result. A later assembly may combine independent inputs, but was not used
to justify this proof. No production state was changed.

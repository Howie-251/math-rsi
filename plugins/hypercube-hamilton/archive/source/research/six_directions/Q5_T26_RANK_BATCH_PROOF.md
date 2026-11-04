# Actual Q5 T26 marked-orbit batch: 55 full-rank certificates

2026-11-01. ARIS proof-writer producer package. Complete candidate proof,
relative to the primary rank theorem and explicit finite certificates.
Fresh independent rank, forest and Q6-application review is required.
No accepted ledger or previously frozen first/T63 input is changed.

## Exact theorem and status

For each row of the exact marked-geometry registry below, let F be ANY
matching of K(Q5) with precisely the listed two minority and six majority
holes, and omit precisely its listed majority pair. Then F extends to
one simple 30-cycle on the other Q5 vertices with all new edges short.
Required edges may be long or join equal parities. Common cube
translations and coordinate permutations transport the entire marked
geometry and arbitrary matching, including the opposite parity case.
This theorem is only for these 55 marked orbits, not universal T26.

Status: PROVABLE AS STATED conditional on independent verification of the
finite full-rank certificates and explicit primary rank import. All 55
producer searches reached rank 2048 without any capped or deficient case.
The first frozen certificate is reused for index0; other prefixes are
Q5_T26_RANK_batch_01 through Q5_T26_RANK_batch_54.

## Forest and rank argument

For each registry row put H=minority union majority, U=the omission pair,
and K=Q5-H. Each selected short graph S on Q5-U has degree one at the 24
covered vertices K, degree two at the six included holes, and no cycle.
It therefore has twelve paths and eighteen edges. P(S) pairs its path
endpoints. If a required matching F and P(S) form one labelled alternating
24-cycle, expanding every P(S) path gives one simple 30-cycle containing
all F edges. A shared F/P pair would be an isolated labelled 2-cycle,
impossible in a connected 24-cycle; thus no length-one path duplicates
an original edge. All introduced edges are short.

The primary theorem of Cygan--Kratsch--Nederlof, Corollary3.5 of
*Fast Hamiltonicity checking via bases of perfect matchings*, gives
rank_GF(2)(H_24)<=2^(24/2-1)=2048 on ALL perfect matchings of the complete
graph on K. The generic theorem, primary version and domain alignment are
recorded in A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md. Its upper bound,
not the specific standard basis construction, is the external premise.

For every registry row the supplied 2048 forest endpoint matchings,
restricted to the supplied 2048 valid matching columns, form a full-rank
binary connectivity matrix. Their complete rows of H_24 therefore span
its entire row space. For any matching F its column is nonzero: write
F={(a_i,b_i)} for twelve disjoint pairs and match b_i to a_(i+1) cyclically.
This produces one alternating cycle. If every selected row were zero at
column F, so would their span and all rows of H_24, a contradiction.
Hence some selected forest connects to every F. Expanding it proves the
claimed universal matching theorem for that exact row. This proof does
not require enumerating every original F or every possible short forest.
A deficient or capped search would remain OPEN; none is used as evidence.

## Explicit finite certificate boundary

Each prefix has 2048 records of36bytes in _forests.bin (eighteen sorted
short edges), 2048 records of24bytes in _pairs.bin, 2048 valid24byte
matching columns in _columns.bin, and 2048 rows of256bytes in _matrix.bin.
The _pivots.bin and _combos.bin files have the same matrix dimensions:
pivot j has highest set bit j and equals the XOR of original matrix rows
specified by combos[j]. A checker may verify these combinations or
recompute rank from scratch over GF(2).

Required fresh checks per registry row are exact forest shortness,
uniqueness, degrees, omission, acyclicity and derived endpoint matching;
column matching validity; every one of the 4194304 connectivity bits;
and all rank evidence. The producer search enforces cycles through DSU
rather than an independent-cherry assumption. Generation completeness is
not a proof premise. The frozen first-author check already recomputes all
these checks for index0 in independent Python; batch success is still
producer evidence, not fresh acceptance.

## Exact marked registry

| Index | Minority | Majority | Omitted | Forests examined | GF2 rank |
|---:|---|---|---|---:|---:|
| 0 | 0,3 | 1,4,14,22,28,31 | 1,4 | 9605 | 2048 |
| 1 | 0,3 | 1,4,13,14,22,26 | 1,4 | 14934 | 2048 |
| 2 | 0,3 | 1,4,14,22,26,28 | 1,4 | 9853 | 2048 |
| 3 | 0,3 | 1,13,14,22,28,31 | 1,13 | 12863 | 2048 |
| 4 | 0,3 | 4,11,13,21,28,31 | 4,11 | 7002 | 2048 |
| 5 | 0,3 | 4,13,14,21,25,31 | 4,14 | 20518 | 2048 |
| 6 | 0,3 | 4,13,14,25,28,31 | 4,14 | 20113 | 2048 |
| 7 | 0,3 | 1,4,14,22,26,31 | 1,4 | 9858 | 2048 |
| 8 | 0,3 | 4,8,21,22,25,31 | 4,8 | 10877 | 2048 |
| 9 | 0,3 | 4,8,13,14,21,31 | 4,8 | 13260 | 2048 |
| 10 | 0,3 | 4,8,13,21,22,31 | 4,8 | 12380 | 2048 |
| 11 | 0,3 | 4,13,14,21,28,31 | 4,14 | 20527 | 2048 |
| 12 | 0,3 | 1,13,14,22,26,28 | 1,13 | 13233 | 2048 |
| 13 | 0,3 | 1,2,13,21,25,28 | 1,2 | 9829 | 2048 |
| 14 | 0,3 | 1,13,22,26,28,31 | 1,13 | 12319 | 2048 |
| 15 | 0,3 | 4,7,13,21,28,31 | 4,7 | 13116 | 2048 |
| 16 | 0,3 | 4,11,13,21,25,28 | 4,11 | 6742 | 2048 |
| 17 | 0,3 | 1,4,14,26,28,31 | 1,4 | 9216 | 2048 |
| 18 | 0,3 | 1,13,14,21,22,26 | 1,13 | 12855 | 2048 |
| 19 | 0,3 | 1,2,13,14,21,25 | 1,2 | 14934 | 2048 |
| 20 | 0,3 | 1,13,14,21,25,28 | 1,14 | 6192 | 2048 |
| 21 | 0,3 | 4,13,21,26,28,31 | 4,26 | 9036 | 2048 |
| 22 | 0,3 | 1,4,13,21,25,28 | 1,4 | 9829 | 2048 |
| 23 | 0,3 | 1,13,14,21,22,25 | 1,14 | 8096 | 2048 |
| 24 | 0,3 | 4,7,13,14,21,25 | 4,7 | 10786 | 2048 |
| 25 | 0,3 | 4,7,13,21,25,28 | 4,7 | 14020 | 2048 |
| 26 | 0,3 | 4,8,13,21,25,28 | 4,8 | 9049 | 2048 |
| 27 | 0,3 | 4,11,13,14,21,25 | 4,11 | 8464 | 2048 |
| 28 | 0,3 | 4,11,21,25,28,31 | 4,11 | 6987 | 2048 |
| 29 | 0,3 | 4,13,14,21,25,28 | 4,14 | 20632 | 2048 |
| 30 | 0,3 | 4,13,22,25,28,31 | 4,22 | 18844 | 2048 |
| 31 | 0,3 | 4,13,21,25,26,31 | 4,26 | 9152 | 2048 |
| 32 | 0,3 | 4,13,25,26,28,31 | 4,26 | 11427 | 2048 |
| 33 | 0,3 | 13,14,21,22,25,28 | 14,22 | 23920 | 2048 |
| 34 | 0,3 | 13,14,21,26,28,31 | 13,21 | 26120 | 2048 |
| 35 | 0,3 | 4,8,13,21,22,26 | 4,8 | 16837 | 2048 |
| 36 | 0,3 | 4,8,13,21,26,31 | 4,8 | 13547 | 2048 |
| 37 | 0,3 | 4,8,13,22,28,31 | 4,8 | 12834 | 2048 |
| 38 | 0,3 | 1,13,21,26,28,31 | 1,28 | 9358 | 2048 |
| 39 | 0,3 | 4,8,13,14,21,26 | 4,8 | 17645 | 2048 |
| 40 | 0,3 | 4,13,21,26,28,31 | 4,28 | 10015 | 2048 |
| 41 | 0,3 | 4,8,21,22,28,31 | 4,8 | 9821 | 2048 |
| 42 | 0,3 | 1,4,13,21,26,31 | 1,4 | 12340 | 2048 |
| 43 | 0,3 | 4,8,13,22,26,31 | 4,8 | 15320 | 2048 |
| 44 | 0,3 | 4,8,21,26,28,31 | 4,8 | 10163 | 2048 |
| 45 | 0,3 | 4,8,13,14,28,31 | 4,8 | 12480 | 2048 |
| 46 | 0,3 | 4,13,21,25,26,28 | 4,26 | 9210 | 2048 |
| 47 | 0,3 | 1,13,14,21,28,31 | 1,14 | 6167 | 2048 |
| 48 | 0,3 | 1,2,13,21,28,31 | 1,2 | 9605 | 2048 |
| 49 | 0,3 | 4,7,13,25,28,31 | 4,7 | 18384 | 2048 |
| 50 | 0,3 | 4,8,13,14,21,22 | 4,8 | 16337 | 2048 |
| 51 | 0,3 | 4,8,21,22,25,26 | 4,8 | 13728 | 2048 |
| 52 | 0,3 | 13,14,21,22,28,31 | 13,21 | 26223 | 2048 |
| 53 | 0,3 | 4,13,14,21,25,26 | 4,26 | 10074 | 2048 |
| 54 | 0,3 | 1,13,21,26,28,31 | 1,26 | 5988 | 2048 |

## Actual Q6 application and producer coverage

The accepted uniform transfer applies to covered odd target v, root0,
independent nonroot holes Z,W, and rows(a,b)=(2,1) or(0,3). Both A local
inputs have balanced two holes and already accepted arbitrary-matching
endpoint theorems. In row(2,1), use both Z holes in A as even bridge
sources: B minority is Z intersect B, majority is (W intersect B) plus
its two mirrors. In row(0,3), choose two W holes in A excluding any
source whose mirror is root0; three sources and at most one exclusion
suffice. B minority is W intersect B, majority is (Z intersect B) plus
the two mirrors. The mirrors are precisely the marked omissions.

The original short matching makes each legal mirror internally covered;
independence excludes another hole and a free mirror excludes crossing
ports. The accepted simultaneous conflict/tag/forest/suppression and
expansion proof remains valid. The arbitrary matching produced on B
may be long and same-parity, which each rank theorem explicitly permits.
The global root and covered target remain prescribed; no artificial
completion, compressed edge or tag survives expansion. The zero-original-
crossing boundary remains the accepted five-direction theorem.

Q5_T26_RANK_batch_coverage.py enumerates every such actual projection
and legal source pair in the ACCEPTED41236-input domain
`ten_covered_q5_and_t63_remaining_v{1,7,31}.bin`, bound through the PASS
TEN_COVERED_Q5_ENDPOINT_REVIEW. The projection-witness JSON records every
actual cut/source/marked local geometry and its canonical registry index.
This is a common transformation of minority,majority and omissions,
not unmarked hole classification. Every record is counted only once.
The producer predicts37140 newly covered and4096 remaining OPEN:

| Target | Accepted input | Newly covered | Still OPEN |
|---:|---:|---:|---:|
|1|12910|12000|910|
|7|12696|11220|1476|
|31|15630|13920|1710|
|Total|41236|37140|4096|

Exact remaining original bytes are saved in the three batch residual
files. The greedy list in the coverage JSON uses22 registry rows to
reach the same union; all55 certificate scopes remain separately valid
candidates. Fresh review must independently regenerate every actual
projection, replay source/marked-normalization witnesses, and verify
complete remaining byte/set equality before accepting this decrement.
The new profile begins after accepted A10/T63/endpoint coverage and
therefore makes no repeated decrement for those earlier classes.

## Scope and dependencies

The local DAG is only the generic primary rank bound plus the selected
finite forests/columns/matrices. Q6 coverage additionally imports the
accepted uniform transfer and accepted exact41236 residual. It does not
feed a ten-hole claim back into any local rank theorem. No complete
T26, ten-hole covered/free theorem, A12, remaining Q6 layer or full P6
is asserted. The4096 residual geometries remain obligations, not
counterexamples. All finite computations are producer-only pending
same-family/provisional independent review; no acceptance is inferred
from a successful executable alone.

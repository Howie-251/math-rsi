# Fifth A8 residual orbit: independent full-closure review

2026-11-01. Fresh reviewer `/root/a8_bridge_inputs_audit`, requested
GPT-6.1-sol/high. ARIS proof-checker method within the authorized scope.
`review_independence: same-family`; `acceptance_status: provisional`.

**PASS, relative to the explicitly declared Q4 imports and audited bridge
criteria.** The mathematical four-cut coverage argument, independently
reconstructed exact domain of 2732625 arbitrary matching inputs, all
2732625 positive 31-cycle witnesses, and the twenty-image coordinate orbit
have passed. All reviewed input and final certificate hashes remained
unchanged during verification. No new mathematical gap was found.

## Exact scope and dependency ledger

The candidate theorem is for holes `{0,2,4,8,15,23,27,29}`, omitted vertex
`0`, and arbitrary twelve-edge matchings of the other 24 Q5 vertices.
Long and same-parity required edges are included. The independently generated coordinate
orbit has exactly 20 marked geometries. Full A8, full P6, and the original full Q6
question remain OPEN in this audit, after this individual orbit's
gate has passed; a separate global assembly audit is required.

The theorem-bearing source is `A8_ORBIT5_FULL_CLOSURE.md`. The acyclic
dependency DAG is: GQ4-avoid + Q4 T15/T63 classifications -> audited
two-/three-bridge criteria -> four-cut sufficient constructions;
independently, allowed-edge graphs -> full finite matching domain ->
explicit positive 31-cycles. Their union establishes only the exact orbit
theorem. The diagnostic typed spectrum, producer search completeness,
search unknown counters, full A8, and higher-layer P6 are not premises.

The independent checker `A8_ORBIT5_FULL_REVIEW_check.py` does not import
the producer or the prepared existing verifier. It first reconstructs
the domain and template data; a separate `--certificates` phase checks
the full completed certificate file and pins its final hash. Only review
artifacts are written. This reviewer does not modify producer runs or
accept partial outputs; only the complete standard certificate file can
pass the final phase. The production proof and main state are not modified.

## Four actual marked Q4 inputs

Majority parity is even. The other four even holes are nonadjacent to all
three minority holes 2,4,8, so residual nonadjacency holds. With A the
zero face, every cut contains forbidden 0 in A. The exact templates are:

| Bit | Minority A sources | Covered B mirrors Y | Singleton/common B vertex | Remaining neighbor(s) | Fixed OB edge |
|---:|---|---|---:|---|---|
| 2 | 4,8 | 6,10 | 2 | 3,18 | 3--18 |
| 4 | 2,8 | 6,12 | 4 | 5,20 | 5--20 |
| 8 | 2,4 | 10,12 | 8 | 9,24 | 9--24 |
| 16 | 2,4,8 | 18,20,24 | 16 | 17 | 16--17 |

For bits 2,4,8 the original A holes have 2+2 parity counts. Removing
the two minority sources leaves two majority holes including 0, so
GQ4-avoid is applicable. Original B holes consist of one minority and
three majority holes; adding the two mirror holes gives exactly T15's
1+5 pattern with its specified omitted pair. The singleton's in-face
short neighbors are precisely the omitted pair and the displayed two
vertices, so the fixed obstruction edge is the actual marked T15 edge.

For bit 16, A has three minority and two majority holes, again leaving
two majority holes including 0 after the bridges. B has three majority
holes, and the three covered mirrors produce the exact T63 six-hole
pattern with specified omitted triple. Their unique common in-face short
neighbor is 16 and its remaining neighbor is 17. All mirrors and displayed
obstruction endpoints are outside H. These facts can be derived directly
from H without any normalization or unreviewed type table.

## Coverage necessity and strictness of the bridge criterion

Fix a row, put S=Y union {p,q}, and suppose pq is absent from F. A crossing
edge entering B outside S gives a covered nonmirror degree-one terminal
in G rooted at its A port. An internal mirror's mate outside S likewise
gives a covered nonmirror degree-one terminal rooted through its bridge.
Either violation therefore creates a rooted terminal outside {p,q}.
This is valid for arbitrary long original edges, including equal-parity
edges, and mirrors may themselves be crossing ports.

Let P pair the T-to-T components of G, and let e be the indicator that
both p and q are rooted terminals. The rooted-terminal count is
R=|T|-2|P|. It is even: the first three cuts have c even and |T|=c+2;
the last has c odd and |T|=c+3. If e=0, the additional terminal gives
R>=2>0. If e=1, both p,q plus the additional terminal give R>=4>2.
Thus d=|T|/2>|P|+e=|J|. The candidate root edge is disjoint from P,
the original obstruction edge is absent by premise, and every hypothesis
of the previously audited sufficient bridge criterion is satisfied.

In particular the artificial prescriptions are a proper subset of D;
they cannot close a component before compression, and cannot introduce
the OB edge in the final B matching. The audited expansion restores all
A-0 vertices, bridge mirrors, and arbitrary original required edges.
No claim about a producer's failure to find an A cycle is involved.

Taking the contrapositive, every input not already solved must, for each
row, either contain its fixed edge or obey both restricted conditions.
This is a necessary cover of the unconstructed inputs. A converse is not
needed: the finite graph family may also contain inputs already solved
by some construction. Certifying its entire domain is sufficient.

## Sixteen domains and independent reconstruction

The actual occurrences of the four fixed edges determine a unique mask.
Set-bit edges are required; unset-bit edges are explicitly absent and
their restricted conditions are imposed. In each applicable graph,
crossings can enter B only at S and an internal B edge meeting Y must
remain in S. All other original complete-graph edges are permitted.
The required edges are checked against every applicable restriction
before their endpoints are removed. Distinct masks cannot share a full
input matching.

The four fixed edges are pairwise disjoint, so no empty branch here can
be justified by an edge-overlap argument from a different orbit. The
independent reconstruction instead checks actual connected components
of every residual allowed graph. Any odd component with no outgoing
allowed edges prevents a perfect matching. Exact odd-component witnesses
are recorded in the domain evidence for the eleven empty masks.

For every domain without such an obstruction, the checker recursively
chooses the least remaining vertex and each allowed partner. This
enumerates each perfect matching exactly once. At every leaf its full
canonical 24-byte input must occur in the independently parsed input
set and is removed. The initial set is checked to contain distinct
matchings covering exactly Q5-H, and must be empty after enumeration.
No producer memoized count or producer code is imported.

The independently verified exact counts are:

| Mask | Original arbitrary matchings |
|---:|---:|
| 7 | 176400 |
| 11 | 176400 |
| 13 | 176400 |
| 14 | 176400 |
| 15 | 2027025 |
| Total | 2732625 |

Mask 15 leaves a complete graph on sixteen vertices and has the
independent analytic count 15!!=2027025. All counts passed the
exact input-set equality check. Input size is exactly 65583000 bytes.

## Full positive-certificate gate

The completed certificate file has exactly 2732625*55=150294375
bytes, and all 2732625 records passed the following direct checks. Each record must begin with the exact corresponding original
matching, followed by 31 distinct vertices exactly equal to {1,...,31}.
Every original edge must occur between cyclic neighbors. Every other
cyclic edge, including the closing edge, must have XOR in
{1,2,4,8,16}. This directly checks one connected simple extending cycle;
neither degrees alone nor a search-success total suffices.

The checker pins the completed file hash before verification, rehashes
it afterward, and verifies all previously pinned theorem, import and
domain sources are unchanged. It accepts only when every one of the
2732625 inputs has a valid positive record. A truncated file, missing
record, duplicate input, invalid cycle, changed source, or unknown
producer result leaves the orbit theorem unaccepted.

## Orbit transfer, adversarial checks, and current status

All 120 coordinate permutations fix 0 and preserve shortness and the
entire arbitrary matching domain. Generating their images gave
exactly twenty distinct hole sets. This transports the completed
representative theorem to its marked orbit, and proves no other orbit.

Structural edge cases examined include mirrors as ports, internal paired
mirrors, arbitrary long crossings and internal edges, distinct roots,
an endpoint not rooted at T, obstructions introduced by compression,
the e=0/e=1 parity distinction needed for strictness, actual unset-edge
absences, and a complete-graph final mask. No mathematical gap was found
in the coverage argument relative to the explicit imports.

The complete domain, all 2732625 positive certificates and the twenty-image
orbit checks passed. Semantic acceptance remains same-family/provisional
and relative to the declared Q4 imports; this review does not transitively
re-audit all their base files. Full A8, full P6 and full Q6 are not accepted
by this orbit-only review.

Final certificate SHA-256:
`4faabf92ae61845e9a12b36a754998b03f14bf143e263999a6c6e731ac397f22`.
The independently checked input SHA-256 and all theorem/import pins are
recorded under `audited_input_hashes` in `A8_ORBIT5_FULL_REVIEW.json`.
Reproduce the domain phase with `D:\anaconda\python.exe research\six_directions\A8_ORBIT5_FULL_REVIEW_check.py`,
then its full certificate phase with the additional `--certificates` flag.
Production sources and the main state were not modified by this review.

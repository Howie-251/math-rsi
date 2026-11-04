# Complete fourteen-hole Q6 prescribed-endpoint theorem

2026-11-02. ARIS proof-writer submission. Independent final assembly
acceptance is a separate gate. Any named finite or import gate that has
not yet passed remains an obligation; this document does not update the
acceptance ledger by itself.

## Exact theorem

Let M be any matching of25 edges of the six-dimensional cube Q6, and
let u be any vertex not covered by M. For every vertex v of parity
opposite to u, including v covered by M, there is a Hamilton u-v path
containing every edge of M.

All original edges of M are cube edges. Artificial complete-graph matching
edges occur only in explicitly imported intermediate constructions; they
are removed or restored as required when the physical Q6 path is assembled.
This is the entire fourteen-hole layer of P6, not full P6.

## Imports and dependency order

The complete twelve-hole predecessor is TWELVE_HOLE_FULL_REVIEW. It
covers arbitrary opposite-parity targets, not only free targets. The
accepted HIGHER_Q5_FULL_REVIEW reduction may therefore be applied to
fourteen holes without an unmet predecessor assumption. The Q5 balanced
endpoint/cycle and marked local inputs used by this reduction and the
subsequent applications have their exact import scopes and source hashes
recorded in the named reviews below. Their earlier conditional A8/A10
premises have been discharged by the already accepted full Q5 inputs.

The fourteen-hole applications are used in the following exact source
order. Each review must affirm every-realizing-original-matching scope and
bind its actual source and remaining streams, not only a numerical count.

| Gate | Remaining covered | Remaining free |
|---|---:|---:|
| HIGHER_Q5_FULL_REVIEW, h14 | 9252401 | 232042 |
| FOURTEEN_REUSE_REVIEW | 47893 | 318 |
| FOURTEEN_CACHED_REVIEW | 12528 | 18 |
| FOURTEEN_HALL_REVIEW | 3923 | 0 |
| FOURTEEN_FORCED_REVIEW | 2587 | 0 |
| FOURTEEN_MAXIMAL_A_REVIEW | 2527 | 0 |
| FOURTEEN_STAR_EXPANDED_REVIEW | 2407 | 0 |
| FOURTEEN_STAR_B_GLOBAL35_REVIEW | 2287 | 0 |
| FOURTEEN_MID_SELECTED_REVIEW | 25 | 0 |
| FOURTEEN_FINAL25_REVIEW | 0 | 0 |

The final review's hash must be bound by the final assembly checker once
the producer's final25 package has passed. A pending
producer package or positive rank flag cannot discharge that last row.

## Proof of the theorem

Translate the cube by u and permute coordinates. The root becomes0 and
the target becomes1,7 or31 according to its odd Hamming distance from the
root. This common automorphism preserves cube edges, matching membership,
holes, and prescribed endpoints. There are seven holes of each parity.

If v is free, FOURTEEN_HALL_REVIEW supplies the full free-target assembly:
the complete predecessor and the initial reduction cover every input
outside the exact232,042-record free residual, the reuse and cached
applications reduce this to18, and each of those18 admits an explicit
covered-neighborhood deficiency witness. Such a hole set cannot arise
from the actual short matching M. Hence the free-target case is proved.
The adjacent-hole augmentation argument includes the special edge uv;
its stronger endpoint condition was independently checked in that gate.

Suppose v is covered. If the fourteen-hole predecessor reduction supplies
a path, the claim is already proved. Otherwise the normalized actual hole
set is one of its9,252,401 exact covered-target records. At each subsequent
row of the table, the imported proof either supplies a Hamilton path for
every short matching realizing that record, or gives an explicit positive
Hall obstruction showing that no such original matching can exist, or
retains the record in the exact complementary stream. The last alternative
therefore passes the same actual normalized M to the next stage.

The ordinary marked-rank applications are universal over arbitrary
compressed required matchings; the forced applications verify their
obstruction-avoidance hypotheses for the actual matching using the stated
cut/source and root restrictions. The maximal-A applications enumerate
complete classes of local inclusion-maximal matchings and prove the
submatching lift back to arbitrary original M. In particular, added local
edges remain completion edges, extra original holes remain bridge sources,
and every omitted target edge is restored when the cycle is opened.
These are the exact quantified conclusions imported from their independent
reviews, rather than an assumption that one example matching represents
all matchings with the same holes.

After the selected three local inputs, only25 target31 records remain,
forming two disjoint target-stabilizer orbits of sizes20 and5. Their common
even-hole representative is Z={39,43,45,51,53,57}; the odd holes are
respectively {1,2,4,8,14,16,32} and {1,2,4,8,16,32,62}.
The final25 proof covers both complete local maximal-A domains, including
the target's internal/crossing cases because31 is not in the mandatory
odd set. In the second orbit, even30 is mandatory internally matched
because its mirror62 is an original B hole. Its separately audited B
inputs and exact actual transports supply the required path in both
orbits. Thus no covered-target record remains.

Apply the inverse initial cube automorphism to the constructed path. Its
endpoints are the original u,v and it contains the entire original M.
This completes the fourteen-hole theorem relative to the explicitly
accepted imports and exact finite certificates.

## Acceptance boundary

Final acceptance requires all table gates to be formal PASS, every
source/remaining interface to agree exactly, each finite premise to have
the stated complete-domain scope, and all live hash bindings to agree.
The final assembly must also confirm an acyclic dependency graph: no
fourteen-hole argument here assumes complete sixteen/eighteen holes or
full P6. Even after acceptance, full P6 additionally requires the complete
sixteen/eighteen-hole steps and the accepted rooted range reduction.
The audit regime is same-family/provisional, not Lean formal verification.

# Ten-hole covered targets: marked T63 split application review

2026-11-01. ARIS proof-checker; fresh reviewer `/root/t63_complete_split_review`.
Explicit user route: GPT-6.1-sol / high. Assurance is **same-family / provisional**.

**PASS**, relative to the accepted uniform transfer and the independently
checked marked Q5 T63 split theorem. Exactly **12916** additional geometries
are uniformly covered. Exactly **41306** remain **OPEN**. Complete ten-hole
covered targets and full P6 are not proved; residual records are not negative
instances. No producer, prior import, frozen input or main state was changed.

## Exact statement and hypotheses

The input domain is precisely the three frozen residual files accepted by
`Q5_A8_CONSEQUENCES_REVIEW.json`, totaling 54222 geometries. Each record has
four even holes Z and five odd holes W; the remaining even hole is u=0.
The target v is odd and covered. Z union W is independent. For every short
27-edge Q6 matching realizing a given geometry, a successful row below
produces a spanning u--v path containing every original matching edge.
Quantification is over all realizing matchings, not one sampled matching.

The imported Q5 statement applies to every arbitrary complete-graph matching
with six same-parity holes H and three marked omissions U, whenever an internal
coordinate has marked (2,1)/(4,2) counts. It includes zero original crossing
count and long required edges. `Q5_T63_COMPLETE_SPLIT_REVIEW.json` accepts
this precise statement at same-family/provisional assurance.

## Application obligation ledger

| ID | Obligation | Discharge |
|---|---|---|
| T1 | Accepted residual identity | All three byte hashes agree with the earlier accepted review; all records are unique with proper parity, sorted halves, valid labels, covered v, and independent Z union W. |
| T2 | Even-consumption row (4,2) | Select three actual free even sources S in Z intersect A. Uniform transfer has s=4+1-2=3 and balanced (2,2) A holes. Actual B holes are (W intersect B) union mirror(S), with omissions mirror(S), giving six odd holes. |
| T3 | Odd-consumption row (1,5) | Select three actual free odd sources in W intersect A excluding mirror(u). At least four remain. Transfer has t=5-1-1=3 and balanced (2,2) A holes. Actual B holes are (Z intersect B) union mirror(S), with omissions mirror(S), giving six even holes. |
| T4 | Simultaneous bridges legal | Sources are free, so a short original matching cannot have a crossing port at their mirrors. Independence excludes original holes there, and the selection excludes u. Distinct sources give distinct mirrors; mirrors are internally covered and their pendant partners cannot form conflicts with crossing or root endpoints. |
| T5 | Actual marked geometry | Build the actual B holes and omissions before projection; check all six outer cuts, every eligible source triple and all five internal coordinates. The relative marked geometry is independent of the arbitrary A completion matching. |
| T6 | Uniform transfer applies | For c>0, the accepted balanced-four-hole endpoint theorem and the tagged simultaneous-suppression transfer apply in each row. Suppression gives an arbitrary B matching, which the marked T63 theorem explicitly permits. Expansion restores every vertex and required edge; deleting the tag leaves the required Hamilton path and only short new edges. For c=0 use the accepted five-direction endpoint input directly. |
| T7 | Positive witness validity | For every newly covered input, its producer-declared actual cut, row, sources, projected holes, projected omissions and list of good internal cuts belong to the independently enumerated legal options. |
| T8 | Exhaustive partition and exact outputs | Every input without a legal marked split is retained, in its original order and bytes; both byte equality and exact set equality are checked against frozen producer residuals. No record is lost or duplicated. |

The transfer source and review hashes match the prior accepted bindings.
This review checks its hypotheses for the present rows and treats the
previous endpoint/transfer theorems as explicit accepted imports. The complete
Q5 proof was separately audited in the companion report. There is no dependency
from this ten-hole count back into the Q5 proof.

## Independent coverage calculation

`TEN_COVERED_T63_SPLIT_REVIEW_check.py` was newly written and run using
`D:\anaconda\python.exe`; it neither imports nor executes producer code.
It checks all candidates, rather than stopping at a producer's first success,
then verifies every declared witness by membership in that independently
computed set. Its JSON records hashes and the following totals.

| v | Accepted input | Newly covered | Remaining | Successful actual source selections checked |
|---:|---:|---:|---:|---:|
| 1 | 16920 | 4000 | 12920 | 21220 |
| 7 | 17022 | 4296 | 12726 | 22278 |
| 31 | 20280 | 4620 | 15660 | 15180 |
| Total | 54222 | 12916 | 41306 | 58678 |

The remaining files agree byte for byte and as sets. Their SHA-256 hashes are:

| v | Remaining file SHA-256 |
|---:|---|
| 1 | `d47ca251ac8fcad17aafc2d757dfdc78608a80aa7b6cc9293ad7cdab508c2f4d` |
| 7 | `01c2251b1549d2f134f6bd9f6704aff3bd7f0843402ab0a4c4c97fb463573404` |
| 31 | `041b1a6b5615cc7840cfb52810f91513104f0f48e2bf40e010881f0b14347c01` |

Fixed inputs were rehashed after all checks and remained unchanged.
Adversarial cases covered include the odd-consumption forbidden mirror of u,
outer face orientation, internal projection, simultaneous three-bridge
availability, arbitrary compressed matching edges, c=0, and duplicate/set
partition failures. No FATAL, CRITICAL, MAJOR or MINOR mathematical issue
remains in the audited scope. No inference of nonexistence is made from a
failed geometric test. Complete Q5 T63, full ten-hole covered targets,
remaining Q6 layers and full P6 remain **OPEN**.

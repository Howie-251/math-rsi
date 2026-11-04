# Independent ARIS review: twenty-seven single-cherry local classifications

**PASS**, modulo the explicit primary matching-connectivity rank theorem.
Each of the27 marked local statements is proved for EVERY arbitrary
complete-graph required matching F, with exact classification: a short-added
cycle on Q5 minus U exists if and only if the marked edge pq is absent from F.
This is local-only acceptance; no actual Q6 coverage count, full T28/T19,
complete twelve-hole Q6 or P6 conclusion is asserted.

Reviewer `/root/higher_q5_nearbalanced_review`, user-selected GPT-6.1-sol /
high, independently checks the root producer's package under ARIS
proof-checker. Review independence: same-family; acceptance: provisional.
No producer proof, certificate, summary or state was edited.

Frozen proof SHA256:
`8c45729c0d838eae4aeca4938027b9f9ac265dad75b71f3ea7c79c50059a7b00`.
Manifest SHA256:
`67b2c0b4918079c593c3af1d598abf670494145405127462434ca5aa90b1996f`.
All249 declared input hashes match and were rechecked after computation.

## Exact statement, imported bound and dependency graph

For each exact row of TWELVE_NEW_FORCED_summary.json, let H be its
minority/majority hole union, U its specified majority omissions, and
K=Q5 minus H. For EVERY perfect matching F of the complete graph on K,
there exists a simple cycle on precisely Q5 minus U containing F, with
every edge outside F short, if and only if pq is not an edge of F.
The conclusion transports under a common cube automorphism of H,U,h,p,q
and F. There is no shortness, bipartite or parity restriction on F.

The exact accepted indices are
6,31,51,52,79,86,123,178,206,207,214,215,234,237,272,273,277,278,279,
349,360,361,362,363,366,367,373. They comprise12 T28 inputs and15 T19
inputs. This does not assert that the list exhausts all geometries, or
require that its rows belong to disjoint symmetry orbits.

The primary [accepted manuscript of Cygan--Kratsch--Nederlof](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf)
was opened directly. Its abstract defines the connectivity matrix on all
complete-graph perfect matchings. Theorem3.4 and Corollary3.5, PDF page9,
give binary rank2^(t/2-1) for every even t>=2. Substitution t=20 gives512.
Thus the generic bound applies to K' below, including long/same-parity
matchings. The older source note's emphasized t=22 application does not
restrict the generic corollary.

The acyclic DAG is primary rank theorem plus checked finite reduced
forest/matrix certificates -> universal row-space spanning -> the27 exact
local classifications. The generic Q6 safe-transfer theorem is mentioned
only as a boundary for future applications; no Q6 theorem is needed to
prove these local statements. Producer extraction from an older512x1024
matrix, chosen-source-column metadata and original search ranks are not
premises of this audit.

## Mathematical obligation ledger

| ID | Obligation and discharge |
|---|---|
| L01 | Every H has10 distinct holes, so K has22 vertices. T28 has minority2/majority8, omissions3; T19 has minority1/majority9, omissions4. U is a subset of majority holes and h is included. All exact sets and p,q agree between summary, config and per-prefix metadata. |
| L02 | For every row, the available short neighbors of h in Q5 minus U are EXACTLY p and q, and both lie in K. Since no required edge is incident to the hole h, every admissible cycle must use p--h--q. |
| L03 | If F contains pq, that required edge together with p--h--q makes a closed triangle whose three vertices already have degree2. The cycle is required to contain29 vertices in T28 or28 in T19, both greater than3, so no such spanning cycle exists. This is a genuine necessary obstruction, not an inference from failed search. |
| L04 | Each supplied S uses distinct short edges, degree0 on U, degree1 on K, degree2 on H minus U, and is acyclic. Hence its support is exactly Q5 minus U and each nontrivial component is a path with two endpoints in K. There are11 paths and18 or17 edges respectively. All full path endpoint pairs are independently reconstructed. |
| L05 | In every S, the entire component through h is exactly p--h--q: the two physical edges occur, h has degree2, and p,q have degree1. Consequently its full pairing contains pq. Deleting that exact pair gives a perfect matching P' on K'=K minus {p,q}, with20 vertices. No arbitrary pair is removed. |
| L06 | For arbitrary F excluding pq, write F(p)=a,F(q)=b. Matching validity implies p,q,a,b are distinct. Removing pa and qb and adding ab produces a perfect matching F' on K'. A shared pair with another edge of F cannot arise because a,b had no other original mate. F' may be long or same-parity, which is permitted. |
| L07 | In the labelled degree2 union F+P(S), contract the path a--p--q--b to the labelled F' edge ab. This changes no other component, so connectivity holds exactly when F'+P'(S) is connected. Distinctness from L06 excludes loops/degenerate contractions. A common pair is retained as a labelled two-edge component in this reasoning; it is never collapsed to a simple edge. |
| L08 | Each supplied reduced column is a perfect matching on exactly K'. Every saved connectivity bit is independently recomputed from actual reduced P' and actual column matching. The new GF(2) elimination uses the recomputed matrix, not producer pivots/combos, and obtains rank512 for each row. |
| L09 | A rank512 restriction implies independence of the512 complete rows of H20. The primary upper bound512 forces them to span the full row space. For every arbitrary F', its column is nonzero: orient its ten pairs and cyclically connect the end of each to the start of the next to construct another complete matching giving one alternating20-cycle. If all512 chosen rows vanished on F', every row would vanish there, contradiction. Thus some chosen P' connects to EVERY F'. The512 finite columns witness rank; they do not restrict the universal original matching quantifier. |
| L10 | Undoing the contraction gives a connected labelled alternating union F+P(S). Expanding each path pair through S gives a single connected degree2 graph on exactly Q5 minus U. A shared physical required/forest edge would have both endpoints in K and be a length-one forest component; its common endpoint pair would give a separate labelled two-edge component, impossible on22 connected endpoints. Hence the expanded cycle is simple, retains all F and adds only short S edges. |
| L11 | L03 gives necessity and L04-L10 give sufficiency for the EXACT same F domain and marked geometry. Applying one common cube automorphism preserves required edges, short added edges, the forced cherry, omissions and forbidden pair. Neither a favorable required matching nor a different omitted set is selected. |

## Independent deterministic verification

TWELVE_NEW_FORCED_REVIEW_prepare.py checks the exact27 summary rows against
the manifest index list, all geometry populations/parities, the neighbor
identity N(h) minus U={p,q}, and equality with config and metadata. It
writes a new reviewer-only row file for the C++ checker. Its result has
the249 checked frozen hashes and the exact12/15 type split.

TWELVE_NEW_FORCED_REVIEW_check.cpp independently processes every certificate:

- Exact byte lengths:512 forest records of36 or34 bytes, full pair records22
  bytes, reduced pairs20 bytes, arbitrary matching columns20 bytes, and
  matrix512x64 bytes.
- Every physical forest edge, vertex label, duplicate edge, degree,
  omission, component and cycle condition; actual full endpoint pairings;
  the physical cherry and exact reduced-pair deletion.
- Every endpoint in every reduced column, without a parity restriction.
- Every connectivity bit, by contracting each reduced row to10 components
  and unioning actual column edges. Connected means9 successful unions;
  common row/column pairs remain loops on a contracted component and cannot
  falsely count as a connecting edge.
- Exact byte/bit comparison with the saved matrix, followed by new forward
  Gaussian elimination using increasing columns and64-bit rows.

| Check | Complete total |
|---|---:|
| Local marked classifications |27|
| Physical forests/full and reduced pairings |13824|
| Valid reduced matching columns |13824|
| Recomputed connectivity bits |7077888|
| Independent GF(2) eliminations |27|
| Rank of each recomputed512x512 matrix |512|

The verifier exits0 and its check JSON is PASS. Saved pivots and combos are
hash-bound but not used to establish rank. The source512x1024 matrices and
extraction-column selections are not read as evidence. Certificate legality
and independently recomputed reduced rank stand on their own.

The final checker rehashes all249 inputs after computation and exhaustively
tests the contraction equivalence on all1386 admissible small labelled
pairing pairs at endpoint counts6 and8, including common-pair/disconnected
degeneracies. These finite pressure tests supplement L06-L07 rather than
replace the general graph proof.

Reproduction: run TWELVE_NEW_FORCED_REVIEW_prepare.py with
D:/anaconda/python.exe; compile the reviewer C++ with
D:/mingw64/bin/g++.exe -std=c++17 -O3; execute it with this directory as
argument and save stdout to TWELVE_NEW_FORCED_REVIEW_check.json; run
TWELVE_NEW_FORCED_REVIEW_finish.py. All written files have reviewer names.

## Boundaries and decision

Counterexample pressure considered a required pq, an extra available
neighbor of h, a missing cherry edge, a forest all-hole cycle, an incorrect
full or reduced pair, a column omitting a terminal, a common row/column
pair misinterpreted as one edge, contraction with a=b, rank over the wrong
field or bipartite domain, and replacing universal F by the512 supplied
columns. The exact predicates and L01-L11 exclude each failure. There are
no analytic, limiting, asymptotic or probabilistic obligations.

The27 exact local classifications pass with zero open mathematical issues.
A later Q6 use must check its ACTUAL marked geometry, legal source set,
root outside the ACTUAL forbidden pair, and all hypotheses of the accepted
generic forced-cherry transfer. Original M_B lacking pq is insufficient by
itself. No actual Q6 application or residual decrement is accepted here;
full T28, full T19, complete twelve-hole Q6 and full P6 remain unproved
by this local package. Semantic assurance remains same-family/provisional
relative to the explicit primary rank theorem.

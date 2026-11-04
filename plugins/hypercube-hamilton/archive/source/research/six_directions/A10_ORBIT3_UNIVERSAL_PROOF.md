# Final A10 orbit: universal extension from 1024 short-forest rows

2026-11-01. ARIS proof-writer candidate. **PROVABLE AS STATED, conditional
on fresh independent verification of the frozen finite certificate and the
explicit matching-connectivity rank import.** Producer-side checks pass;
independent semantic acceptance is pending. No main ledger is changed.

## Exact theorem

Let V={0,...,31}, H={0,1,2,4,8,15,23,27,29,30}, and K=V minus H.
For every matching F of the complete graph on V whose uncovered set is
exactly H, there exists a simple cycle on exactly V minus {0} containing F,
with every edge outside F a Q5 short edge. Required edges may be arbitrary,
long, or have endpoints of equal parity. Coordinate permutations give the
same assertion on the marked orbit of five normalized geometries.

The proof uses neither previously closed A10 orbits, A8, nor any P6 result.
Its dependency DAG is only: imported rank upper bound + 1024 independently
checkable forest witnesses + finite full-rank matrix -> the stated theorem.
It proves this last A10 orbit only; broader consequences need separate
scope accounting. There are no asymptotic, analytic, or probability claims.

## 1. Short forests and endpoint matchings

Call S admissible if it is a simple graph of Q5 short edges on V minus {0},
with degree one at every vertex of K, degree two at every vertex of
H minus {0}, and with every connected component a path. Thus it contains
31 vertices, 20 edges, and eleven disjoint paths. Its 22 endpoints are
exactly K. Pairing the two endpoints of each path gives a perfect matching
P(S) of the complete graph on K. Paths may have length one.

For an original F, regard F and P(S) as separately labelled matchings even
if an endpoint pair occurs in both. If their union is one alternating
22-cycle, expand each P(S) edge into its stored S path. Interiors of the
paths are mutually disjoint and are precisely the nine included holes.
The expansion is one simple 31-cycle and retains every F edge.

There is no edge-duplication loophole: a common F/P pair would form an
isolated labelled two-edge component of F+P, impossible in a single
22-cycle. In particular a length-one S path cannot duplicate an F edge
in a successful pair. Consequently the expanded graph is simple, and
all introduced edges belong to S and are short. This proves the required
extension whenever F+P(S) is connected.

## 2. Imported finite-matrix theorem

Let M be the set of all perfect matchings on K. Define the binary matrix
H_22 indexed by M on both sides, with entry h(F,P)=1 exactly when the
labelled multigraph F+P is one alternating cycle. There are no restrictions
on matching edge length or parity.

The external theorem used is **rank_GF(2)(H_22)<=1024**. It is Corollary 3.5
of Cygan--Kratsch--Nederlof, *Fast Hamiltonicity checking via bases of
perfect matchings* (JACM 2018), derived from Theorem 3.4. The source defines
this matrix on all complete-graph perfect matchings, so the import matches
the present domain exactly. Version, pages, basis definition and primary
links are recorded in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`.

Only this upper bound is used. A certificate verifier may check any 1024
valid matching columns; it need not rely on the external basis construction
or assume our selected forest matchings have a prescribed form.

## 3. Universal finite-row criterion and proof

**Lemma.** Suppose S_1,...,S_1024 are admissible short forests, and
X_1,...,X_1024 are perfect matchings on K. If the matrix
A[i,j]=h(P(S_i),X_j) has GF(2) rank 1024, then every F in M admits at least
one i such that h(F,P(S_i))=1.

**Proof.** The complete rows of H_22 indexed by P(S_i) are linearly
independent, since their restriction to the chosen columns has full rank.
Their span has dimension 1024. The imported upper bound implies these
rows span the entire row space of H_22.

For every fixed F, its column in H_22 is nonzero. Explicitly order its
eleven edges as (a_1,b_1),...,(a_11,b_11) and take the perfect matching
R={(b_i,a_(i+1)):1<=i<=11}, with cyclic indices. All endpoints are distinct,
and F+R is the single alternating cycle
a_1,b_1,a_2,b_2,...,a_11,b_11,a_1. Thus h(R,F)=1. R is used only to prove
this algebraic nonzero-column fact and is not claimed to be a short forest.

If every selected row were zero at column F, every GF(2) linear combination
of them would also be zero there. Since they span every row, this would
make the entire column zero, contradicting h(R,F)=1. Hence at least one
selected row has entry one at F. Symmetry gives h(F,P(S_i))=1. Section 1
expands its forest to the desired simple cycle. This proves the lemma and
the universal claim without enumerating any original F. QED.

This criterion is sufficient, not asserted necessary. A deficient row rank
would not prove a counterexample or disprove the universal theorem. Here
the saved matrix has full rank, so no residual matching domain remains.

## 4. The explicit certificate

The covered vertices in fixed increasing order are
`[3,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,28,31]`.
The complete supplementary-spectrum producer supplied 17496 endpoint
matchings, but **its exhaustive coverage is not required for this proof**.
Only the selected 1024 legal forest witnesses are premises. Their matching
rows were selected by deterministic GF(2) elimination against 1024 matching
columns. All values are saved as raw unsigned bytes.

| Frozen artifact | Format and purpose |
|---|---|
| `A10_ORBIT3_UNIVERSAL_rank.json` | 1024 zero-based source-row indices; producer rank result |
| `A10_ORBIT3_UNIVERSAL_rank_selected_pairs.bin` | 1024 records of 22 bytes, eleven sorted unordered endpoint pairs |
| `A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin` | 1024 records of 40 bytes, twenty sorted unordered short edges, aligned with the selected pairs |
| `A10_ORBIT3_UNIVERSAL_rank_columns.bin` | 1024 records of 22 bytes, valid matching columns on K |
| `A10_ORBIT3_UNIVERSAL_rank_matrix.bin` | 1024 records of 128 bytes: row i, bit j is h(P_i,X_j), low bit first in each byte |
| `A10_ORBIT3_UNIVERSAL_rank_pivots.bin` | 1024 records of 128 bytes; pivot row j has highest set bit j |
| `A10_ORBIT3_UNIVERSAL_rank_combos.bin` | 1024 records of 128 bytes; row j selects original matrix rows whose XOR equals pivot row j |

The columns were generated by Definition 3.1 of the imported paper; the
C++ implementation also checks their entire 1024-square connectivity
submatrix equals the complementary-bitstring permutation matrix. This is
an additional check, not a replacement for recomputing the selected matrix.

To independently certify rank, recompute every matrix bit directly by
traversing the two labelled matchings. Check every saved row against the
recomputed row. Then for each j verify XOR of matrix rows selected by
combos[j] equals pivots[j], and that pivots[j] has bit j set and no bits
above j. These 1024 triangular pivot rows are independent, proving rank
1024. Alternatively ignore all saved elimination data and recompute GF(2)
rank from scratch. No floating-point arithmetic is involved.

To independently certify the forest-to-matching interface, check edge
uniqueness, shortness, omission of 0, exact degrees at all 31 vertices,
acyclicity and complete path decomposition, and compare each endpoint
pairing with its selected P record. This also checks the nine included
holes occur exactly once as internal vertices and all covered vertices
occur exactly once as endpoints. Check every column is a perfect matching
on K. These checks discharge all finite hypotheses of Section 3.

The accompanying manifest pins the selected artifacts, implementation,
source-reference text and this proof. Producer-side
`A10_ORBIT3_UNIVERSAL_author_check.py/.json` verifies every selected forest,
source alignment, and all saved elimination combinations. The C++ rank
search computes the matching-connectivity bits directly. These are
producer checks; fresh independent recomputation and semantic review are
still required before this candidate is accepted.

## 5. Coordinate orbit

Every coordinate permutation fixes 0 and preserves Q5 short adjacency,
arbitrary required edges, the matching condition, simplicity, and the
claimed vertex set. The marked geometry distinguishes the absent odd
unit hole 16, while the other four unit vertices are holes. Its stabilizer
permutes the four remaining coordinates and has size 24. Hence the
coordinate orbit has 120/24=5 geometries. Transport a matching to the
displayed geometry, apply the proved criterion, and transport its cycle
back. This preserves the exact original quantifiers and forbidden vertex.

## Open acceptance obligation

No mathematical hypothesis has been added to the original statement.
The candidate closes the final marked orbit relative to the primary rank
theorem and the supplied deterministic certificate. The remaining action
is fresh proof-checker acceptance of the import alignment, row-space
argument, all 1024 forest witnesses, and the full-rank matrix. Producer
success alone is not recorded as acceptance, and this file does not modify
the main A10/P6 ledger.

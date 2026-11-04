# Independent ARIS proof review: 55 marked T37 inputs

2026-11-01. Fresh reviewer: `/root/higher_forced_cherry_review`, GPT-6.1-sol/high under the explicit user route. Skill: ARIS proof-checker. The reviewer did not produce this package. Review independence: **same-family**. Acceptance: **provisional**.

**Verdict: PASS, modulo the explicit primary matching-connectivity rank import.** All finite witness obligations for the 55 positive marked local inputs pass independent deterministic checks. No mathematical issue remains open in these claimed local conclusions. This is not a proof of full T37, full twelve-hole Q6, any complete higher Q6 layer, or full P6. Indices 0,1,2,3,6,12,13,14,15 remain OPEN.

## Frozen scope and dependencies

Reviewed the full `Q5_T37_INDEPENDENT_PROOF.md`, the manifest, the summary's explicit geometry rows, and every finite witness for indices 4,5,7,8,9,10,11 and 16 through 63. Independently compared all 451 file hashes declared by `Q5_T37_INDEPENDENT_MANIFEST.json`; every one matches. The manifest's own SHA256 is recorded in the review JSON. Producer search implementations, ranks, selected-row metadata, matrices, and pivot data were not accepted as verification of their own semantic claims.

For each of those explicit marked pairs (H,U), with |H|=10 split 3:7 by parity, |U|=2 contained in the majority set, the conclusion is:

For every arbitrary perfect matching F of the complete graph on K=V(Q5) minus H, there exists a simple cycle on exactly V(Q5) minus U containing F, with every edge outside F a Q5 edge.

The matching F may contain long and same-parity edges. The claim also holds for the image of this same marked pair (H,U) under any cube automorphism. No enumeration of those automorphisms or proof of a 64-orbit classification is necessary for that implication. The supplementary exhaustive 64-orbit classification was **not audited** and is not an accepted dependency here. Likewise, the unsuccessful ranks of the nine other rows were not independently certified and are not negative classifications.

Dependency DAG: explicit geometry -> checked legal short forests -> independently derived endpoint matchings and validated arbitrary matching columns -> independently reconstructed connectivity submatrix -> independent GF(2) rank 1024 -> imported full-matrix rank upper bound -> universal row coverage -> expansion to the required local cycle. This graph is acyclic and has no Q6 theorem or predecessor induction as an input.

## Independent deterministic verification

The fresh checker is `Q5_T37_INDEPENDENT_REVIEW_check.cpp`, compiled with `g++ -std=c++17 -O3`. It reads only the explicit geometry table and frozen finite witnesses. It does not run or include the producer search code. Reproduction from this directory:

```
g++ -std=c++17 -O3 Q5_T37_INDEPENDENT_REVIEW_check.cpp -o Q5_T37_INDEPENDENT_REVIEW_check.exe
./Q5_T37_INDEPENDENT_REVIEW_check.exe
```

`Q5_T37_INDEPENDENT_REVIEW_geometries.txt` was separately derived from the summary. For all 55 claimed rows, an independent Python preparation checked distinct vertices in 0..31, parity of the 3-vertex and 7-vertex sets, opposite parity classes, disjointness, two distinct majority omissions, exact claimed index list and prefix, agreement with the full_rank flags, and exact agreement of each twelve-integer config with sorted H followed by U. The JSON records the explicit audited marked geometries, so the accepted domain does not depend on the unreviewed orbit enumeration.

The C++ checker then verifies the following, with explicit runtime failures rather than compiler-removable assertions:

1. Every file has precisely its documented byte length: 1024 forest records of 38 bytes; 1024 endpoint/column records of 22 bytes; and 1024 records of 128 bytes for each matrix, pivot and combination file. Labels are interpreted as unsigned bytes, and matrix bits as little-bit-first.
2. Each of the 56,320 forest records consists of nineteen distinct Q5 edges. All labels lie in 0..31, each endpoint XOR has one set bit, and an independent disjoint-set union (DSU) detects no cycle. Degrees are exactly one on K, two on H minus U, and zero on U. No loop, parallel forest edge, omitted vertex use, disconnected hole-only cycle, or missing retained vertex can survive these checks.
3. The forest's DSU components determine its endpoint pairing: each nontrivial path component has exactly two K endpoints, giving eleven disjoint pairs covering exactly K. These derived pairs, normalized independently of stored orientation/order, equal the supplied pairing record. Connectivity uses the **derived** pairs.
4. Each column is a valid perfect matching of exactly K. Every endpoint is checked once, with no self-pair. Columns are not required to be short or bipartite; a basis-generation prescription is unnecessary because any independently verified full-rank set of columns suffices.
5. For every row and column, initialize DSU with the derived row matching and add all eleven column pairs. As their labeled union is 2-regular, it is a single alternating cycle exactly when DSU has one connected component. This reconstructs all **57,671,680** matrix entries without the producer's alternating-traversal method. Every reconstructed bit agrees with its frozen matrix bit. Common matching edges remain labeled two-edge cycles and are correctly rejected on this 22-terminal domain: they leave other components.
6. Fresh ascending-pivot Gaussian elimination runs on the reconstructed rows, without supplied pivots or combinations. Every one of the 55 matrices has exact GF(2) rank **1024**. The use of ascending pivots differs from the supplied highest-pivot certificate layout.
7. As an additional certificate check, all **56,320** supplied pivots have their indicated highest set bit, and each is exactly the XOR of reconstructed matrix rows named by its supplied combination vector. All equations pass. These equations are supplementary: independent rank already establishes the needed lower bound.

The complete per-row deterministic result is `Q5_T37_INDEPENDENT_REVIEW_check.json`. All 55 entries report rank 1024, 1024 forests and 1,048,576 rebuilt connectivity bits. `Q5_T37_INDEPENDENT_REVIEW_hashcheck.json` records every manifest file comparison. These are exhaustive checks of the claimed frozen finite witnesses, not sampled search evidence.

## Primary import and hypothesis discharge

I reopened the primary [Cygan–Kratsch–Nederlof manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf). Its matching-connectivity matrix is indexed by all perfect matchings of a complete graph; Corollary 3.5 gives GF(2) rank 2^(t/2-1) for every even t>=2. The manuscript also explicitly distinguishes the labeled double-edge convention at t=2 from the impossibility of a shared edge in a Hamiltonian matching union for t>=4. Here t=22, so the rank is 1024. Only its upper bound is required after the independently checked lower bound.

The statement is neither a bipartite-matching bound nor a real-field rank bound. It applies after the arbitrary labeling bijection from the actual K vertices to 22 labels. Required matchings and certified columns both lie in its complete-graph domain. The local proof does not import any consequence of A10 or a higher Q6 layer: those package files are provenance only, while the actual semantic import is the generic rank theorem.

## Mathematical proof ledger

**MC1: Legal forest decomposition.** The checked degree sum is 22+2·8=38, hence nineteen edges. No retained vertex has degree zero. A finite acyclic graph with degrees at most two consists of paths; degree-one vertices are exactly K. Therefore there are eleven disjoint paths covering all thirty retained vertices, with interiors among the eight included holes. Omissions are unused. This discharges all hypotheses required to replace S by P(S).

**MC2: Connectivity meaning.** The union of any two perfect matchings on K is a labeled 2-regular multigraph, hence a union of alternating cycles. It is one alternating cycle iff connected. The DSU predicate therefore computes the intended matching-connectivity entry, including parallel two-edge components. It does not silently reduce the union to a simple unlabeled graph.

**MC3: Full-row independence.** For a fixed geometry, let A be its reconstructed 1024-by-1024 submatrix. If the 1024 corresponding complete connectivity rows were linearly dependent over GF(2), restricting to the certified columns would give the same dependence among rows of A. Independent rank 1024 forbids this. Thus those complete rows are independent.

**MC4: Row-space span.** The imported full matching-connectivity matrix has rank at most 1024. Its 1024 independent selected full rows therefore form a basis of the entire row space, not merely of the frozen column restriction. This step is what permits universal quantification over F outside the supplied 1024 columns.

**MC5: Every arbitrary F column is nonzero.** Write F={(a_i,b_i):1<=i<=11}. Choose the perfect matching joining b_i to a_(i+1) cyclically. Its union with F is one alternating 22-cycle. Hence this arbitrary F column has a nonzero entry in the complete matrix; no enumerative claim about all F matchings is required.

**MC6: Selected witness for every F.** If all selected full rows vanished at that F column, every row in their span would vanish there, contradicting MC5. Some certified forest pairing therefore connects with F. The quantifier order is correct: one fixed finite family per marked geometry works for every F, while the chosen forest may depend on F.

**MC7: Expansion gives a simple cycle.** Replace the eleven selected pairing edges by their actual disjoint forest paths. The connected alternating cycle on K becomes a connected 2-regular graph on precisely the thirty retained vertices. Forest interiors lie in H minus U and are mutually disjoint, so no interior repeats and F touches none of them. A physical edge common to F and S could only be a one-edge forest component whose endpoint pair is also in F; that would be a proper labeled two-edge component on K, contradicting MC2. Thus no physical edge is reused. The result is a simple thirty-vertex cycle, and every edge outside F is a checked short forest edge.

**MC8: Symmetry preserves the marked claim.** For any cube automorphism g, pull an arbitrary matching on V minus g(H) back by g^-1, apply the audited marked (H,U) theorem, and push forward. Distinctness, required matching edges, shortness, and exact omitted set are preserved. H and U must move **together**; a matching of unmarked hole sets alone does not authorize an application.

## Adversarial and boundary checks

- A repeated or same-parity required matching edge is not excluded from F merely for being nonshort. The full-matrix domain and nonzero-column construction handle arbitrary F.
- Degree constraints alone could permit an unwanted short cycle component. Independent forest DSU rejects such components before deriving endpoints; no assumption that degrees imply acyclicity is used.
- A wrong stored endpoint pairing cannot certify a different legal forest: each record was checked against DSU-derived endpoints, and only those independently derived pairs reconstruct matrix entries.
- A physically shared F/forest edge is explicitly excluded by the labeled proper two-edge component argument on 22 endpoints. The t=2 exceptional convention is irrelevant to this expansion.
- Full rank only on selected columns would be inadequate without the imported global rank upper bound. MC3–MC4 explicitly discharge that obligation over the same field GF(2).
- Producer deficient ranks do not prove nonexistence. The nine indices remain open, and neither the supplementary 64-orbit exhaustion nor full local T37 is inferred from 55 positive records.
- A local marked theorem by itself does not provide actual Q6 cuts, legal sources, geometry identification, transfer applicability, or coverage. No twelve-hole Q6 or P6 closure follows in this audit.

There are no asymptotic estimates, probability assertions, limit interchanges, or unstated uniformity limits. The numerical dimension and degree equalities, rank argument, field, matching domains, nonzero-column construction and simplicity/shortness conclusion all match the theorem statement. No proof repair or producer edit was needed.

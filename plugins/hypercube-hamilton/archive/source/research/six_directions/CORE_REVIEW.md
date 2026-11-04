# Core derivation bounded review

Date: 2026-10-31
Reviewer: delegated Codex agent /root/open_problems
review_independence: same-family
acceptance_status: provisional
Scope: CORE_DERIVATION.md D1–D7, derive_structural_cases.py, structural_case_summary.json and bridge_parity_example.json. Full P6 remains unproved.

## Findings

No actionable logical error found in the reviewed claims.

- D1–D2: the half-layer rigidity proof applies to cube-edge perfect matchings, as explicitly required. The perfect-completion branch and its two-direction exceptional branch invoke the stated established results, not the six-dimensional conjecture.
- D3: adding the artificial endpoint edge and later deleting it correctly removes the only possible noncube edge. The conclusion needs the stated perfect-completion hypothesis on the punctured cube.
- D4: the opposite artificial pairing argument is valid. Removing the two artificial edges from the single alternating Hamilton cycle leaves two paths, each starting and ending with N-edges, hence each has odd length. Consequently each pairs an even terminal with an odd terminal. Restoring the artificial pairing cannot close two separate paths into two separate cycles, because the original union was one cycle. With exactly two pairs, the only remaining pairing is the desired one. The assumption of four distinct vertices already implies n≥2; explicitly stating n≥2, as planned, clarifies applicability of the cited theorem. This reasoning would not force a unique pairing for three or more pairs, which the text correctly notes.
- D5: the parity condition guarantees the required endpoints have opposite local parity within each Q5 slice. The cross-matching endpoints are uncovered by the corresponding internal matchings. The condition also prevents degenerate equal endpoints. Both single-slice paths therefore follow from the known five-direction theorem and join correctly.
- D6: the signed degree sum is exact; cut edges along a fixed cube direction form a matching, so the crossing-degree indicator is correct. Five forced even-side crossings require at least six odd-side crossings, hence at least11 in total. This bounds actual path crossings, not just matching crossings.
- D7: given F is a subset of the fixed coordinate cut, the prescribed internal degrees plus connectivity yield exactly a spanning u–v path. The linear forests and F contain the corresponding matching edges, so inclusion is preserved. Necessity holds by restricting a Hamilton path. The statement is an exact reformulation and does not itself prove the required forests exist.

## Fresh independent checks

A separate Python check validated the ten-edge D6 matching: disjoint endpoints, cube adjacency, six distinct directions, and no edge at0. It checked the supplied64-vertex witness is a Hamilton0–32 path containing all ten edges. The signed cut identity was verified for each of the six coordinate cuts. The displayed witness uses31 crossings in the indicated cut, consistent with the lower bound11; the document does not claim tightness of11.

The classification script was inspected: perfect completion is checked by an exact maximum-cardinality matching on the residual induced graph, not a greedy heuristic. Its D5 test correctly requires opposite slices and an odd A-side endpoint when the root is0. The reported classification totals512+32+1+72+535=1152 and are expressly sample counts, not proof coverage percentages. The classification computation was not independently rerun in this review.

## Scope limitation

This is a same-family consistency review relying on the named published theorems. It does not independently certify their original proofs, resolve the remaining near-perfect class, or establish full P6/T6. No claim of mathematical novelty has been validated.

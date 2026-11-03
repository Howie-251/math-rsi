# Integration delta audit: three repeat-support components

Date: 2026-10-11. Reviewer: `/root/proof_review_n62_12_20_30`.

**Verdict: PASS for the reviewed integration delta — same-family, provisional.** No mathematical issue was found in the actual-graph coverage bridge, the transfer of the three quotient exclusions, the shorter 12-case dependency chain, or the conditional component-count consequence. This bounded review does not duplicate the separate widened finite-check review or reopen the stable individual proof reviews.

## Scope and evidence boundary

The complete new `proofs/dd82/n62/THREE_COMPONENT_EXCLUSION.md` was read, including its four sections and evidence boundary. The already-reviewed 12-case proof remains unchanged. The complete short 6-case and 8-case papers were read to verify their exact interfaces and the integration summaries. Relevant actual local-double theorem premises in `formal/DegreeDiameter/N62DoubleRoot.lean` and the general D1-existence argument in `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md` were inspected. Stable dependency claims checked in `PROOF_AUDIT.md` were reused.

The widened checker output `computations/dd82/n62/three_component_quotients_check.json` was present and read. It reports minimum component size two, 45 rows, 91,125 row triples, 9,108 trace-filtered matrices, 18 labelled survivors, and three canonical quotients; its listed quotients exactly match the new paper and the three individual exclusion statements. It reports no size-two survivor and comparison success against the original list.

The other reviewer is responsible for certifying that finite execution and checker completeness. No checker or enumeration was rerun here, and its independent receipt was not available to this reviewer at writing. Consequently this PASS concerns the mathematical bridge **conditional on that separately checked finite classification**. The JSON's numerical claims are recorded as external evidence, not recertified by this audit. There is no Lean or cross-family acceptance claim.

## Obligations checked

| ID | Integration location | Result |
|---|---|---|
| ID-01 | Section 1, actual quotient construction | The partition is into whole positive-support B-components. AB=BA and the B-eigenvalue-three component-indicator space give A-equitability. The quotient orientation agrees with all three source papers. Row sum eight, size balance, the quadratic identity, and trace seven are necessary for every actual three-component quotient. No preservation of individual components by A is assumed. |
| ID-02 | Section 1, widened finite domain | The component weight identity gives positive even sizes, hence a lower bound of two without B≤2. Every nonnegative integer row of sum eight belongs to the 45 weak compositions of eight into three parts. Therefore enumerating all ordered triples and then applying the exact necessary filters cannot lose an actual quotient. The row sum of Q=R²+R−10I is 64+8−10=62, so equality of its rows to n also imposes n₁+n₂+n₃=62. Simultaneously permuting n, rows, and columns is precisely relabelling components. |
| ID-03 | Sections 1 and 3, finite-output interfaces | The three output matrices and their ordered size vectors agree entry-for-entry with the 6-, 8-, and 12-case exclusion statements. All six simultaneous permutations are harmless relabellings; no graph automorphism is required. The classification is a necessary-model cover, so it need not establish realizability of surviving quotients. The actual computation of the 9,108/18/3 counts remains the other reviewer's scope. |
| ID-04 | Section 2, triple-entry replacement | If B_uv=3, nonnegative row sum three exhausts both endpoint rows. Symmetry, zero diagonal, and their positive mutual entry make {u,v} a whole connected support component of size two. None of the three surviving size vectors contains two, so B≤2 follows inside each case. This inference occurs after the widened classification and is not circular. |
| ID-05 | Section 2, double-root coverage | `n62_double_root_d1_or_closed_component` has only actual graph degree, diameter, order, and one entry B_rw=2 as hypotheses. It concludes a D1 parent template or a closed double four-component, with no global B≤2 premise. The integration correctly states this local fact. In any event the three cases already have B≤2 by ID-04 before the D1 incidence bounds are used. |
| ID-06 | Section 3, 6-case transfer | The source needs the six-component internal degree zero, its degree eight into the 24-component, and the latter's parent degree two and internal degree two. These entries match the first candidate. Its generated original triangle lies in the whole 24-component, whereas triangle pairing forces the containing support component to have six vertices. The integration does not assume all G is triangle-free in this case. |
| ID-07 | Section 3, 8-case transfer | No size-six component gives global triangle-freeness. No size-four component rules out D0. For a double in the eight-component, the generated component choices C,K,L contradict respectively the required bounds r_CC≥4 (actual value two), r_KC≥3 (actual value two), or r_CL≥4 (actual value zero). Together with ID-04 this gives simple B[C]. The source then applies with the stated two four-cycles, matching partners, and weighted row contradiction. No simplicity of B[K] is assumed. |
| ID-08 | Section 3, 12-case dependency replacement | For a double in C of size twelve, the generated component must be C,D,E because these are all support components. H=K=C would require r_CC≥4, contrary to 3. K=D would require r_CD≥4, contrary to 0. K=E would require r_EC≥3, contrary to 2. D0 is ruled out by the absence of size four, and triples by ID-04. Thus B_C is simple cubic connected, and G is triangle-free by absence of size six. These are exactly the initial properties required by the previously reviewed proof. The stronger heavy minimum-size chain is no longer needed for this theorem. |
| ID-09 | Section 3, 12-case spectral interface | P is still the actual cubic original induced adjacency, X has row sum five and column sum two, Z is the actual degree-two induced adjacency, and A[C,D]=0. Thus both block identities and all reviewed arguments about connected P, connected weighted F, the possible sign kernel, and the trace polynomial remain applicable. Connectedness of F is proved from its own equitable trace contradiction; it is not borrowed from G. |
| ID-10 | Section 4, general component-count consequence | The additional imports guarantee existence of a D1 pair and both associated component sizes at least fourteen. For H=K, its original internal degree is at least four, so tr R≥4 and c+2 tr R=17 give c≤9. For H≠K, B≤2 plus even positive component size gives a minimum of four for every other component: size two would force its only off-diagonal entry to be three. Hence 28+4(c−2)≤62, or c≤10.5, gives integer c≤10. The trace identity makes c odd, so c≤9 again. With c≥1 and the new exclusion c≠3, exactly {1,5,7,9} remains as a necessary list. |

All ten semantic bridge obligations are discharged. The independent finite-classification receipt is an explicitly separated imported evidence item, not an unproved algebraic step hidden inside this delta.

## Dependency and counterexample checks

The main three-component theorem uses the widened minimum-size-two quotient classification first, then local triangle/double consequences, and the three specific contradictions. It does not silently use the stronger general D1 minimum-size or existence theorem. Section 4 explicitly restores those additional imports and their general triple-repeat dependency for a stronger conditional conclusion.

The actual distinctions were checked against the following adversarial possibilities:

- A size-two component before quotient classification is retained in the search domain. It is excluded only by the finite classification; the original minimum-size-four diagnostic alone is not used for completeness.
- A repeat triple outside the chosen small component would still force a whole size-two component, so the local B≤2 deduction is global within each surviving quotient.
- A D1 generated component equal to its heavy component is retained as a separate case. The internal-degree bound, rather than a cross-component bound, handles it.
- The direction of D1 incidence matters: for the 12/20/30 case, E has r_EC=2, which violates the reverse lower bound three even though r_CE=5 satisfies the forward lower bound four.
- H and K are counted twice in the size estimate only in the H≠K branch. The H=K branch instead uses the trace bound.
- No original-graph connectedness argument is substituted for B-support connectedness or for the independently proved auxiliary-F connectedness. Each relevant use concerns the correct graph.
- The number c is positive and odd; the listed remaining values are necessary possibilities, not existence claims. The new theorem removes c=3 only, and no argument here removes c=1,5,7,9.

No counterexample satisfying the full reviewed hypotheses was found. No source change, additional arithmetic execution, proof repair, higher-order research, or order-63–65 work was performed.

## Disposition

The integration is mathematically sound on its stated imported basis. Record this receipt as a **same-family provisional PASS for the integration bridge and conditional component-count consequence**, and attach the separate widened finite-check receipt for the 9,108/18/3 classification. Whole-order62 nonexistence, the exact N8 value, Lean certification, and cross-family acceptance remain outside this receipt.

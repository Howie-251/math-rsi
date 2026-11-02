# Proof audit: connected residual matching cover

**Verdict: PASS for the bounded mathematical audit, sound modulo the explicit representation import.** No substantive or minor issue was found in one round. This fresh Codex review is `same-family` / `provisional`; no cross-family acceptance or Lean verification is asserted.

The checked claim concerns every 58-vertex simple graph of maximum degree eight and diameter at most two containing false twins. It proves residual E connectivity, the strict W-spectrum interval and gap, the conditional bipartite 3/4 neighbor distribution, and nonsingularity of H. It does not establish existence or nonexistence of this family.

## Actual read and checked scope

I read the project `AGENTS.md`, local proof-checker skill, all 209 lines of `FALSE_TWINS58_RESIDUAL_CONNECTED.md`, and all 268 lines of `FALSE_TWINS58_EIGHT_SIX_FIBERS.md`. The mathematical dependency checked in the latter is §§1–2 (lines 16–113), including the arbitrary-order-58 regularity reduction, defect budgets, fibre representation and exact cross-fibre coverage. Later symmetry specialization and numerical enumeration were not audited or used. No other reviewers' reports or opinions were read.

The representation is an explicit import boundary in this review, with its needed local derivation checked directly. No Lean theorem was imported as a certificate and no Lean was run. No source changes, external backend calls, new solver or graph enumeration were made. Only the four requested audit files were written. The root agent handles any external review and wiki adoption.

## Findings and hypothesis checks

- **Residual graph and commutation:** Off-diagonal coverage gives permutation blocks; same-fibre matching uniqueness gives diagonal H² blocks 7I. Consequently E is an undirected simple 7-regular matching cover. The identities HD=DH=J−D and HJ=JH are correctly normalized. H connectivity follows solely from exact cross-fibre coverage.
- **Component quotient:** A matching and its inverse stay within an E-component, proving uniform fibre intersections without a transitivity assumption. Preservation of the full 7-eigenspace gives an equitable partition of H and integer Q. Detailed balance is t_i q_ij=t_j q_ji; ordinary symmetry is used only for equal weights. The rank-one factor in Q²+Q=14I+7·1 t^T is correct.
- **Multiplicity and cases:** The rational characteristic polynomial has conjugate irrational roots α,β with equal algebraic multiplicities; weighted symmetry supplies diagonalizability. Connected H makes 7 simple. Thus c=1,3,5. The three partitions of six into three positive parts and the sole five-part partition are complete, up to permitted relabeling. Each row-bound, parity and matrix-entry contradiction was rederived; no endpoint or hidden positivity case is omitted.
- **Spectrum and invertibility:** The upper E endpoint is excluded on W by connectedness; the lower endpoint is retained until bipartiteness is handled. In the bipartite case connectedness supplies a one-dimensional −7-eigenspace, fibre balance places its sign vector in W, and odd H degree excludes Hz=0. Fibre-constant H eigenvalues 7 and −1 complete the nonsingularity argument.

The detailed micro-obligations, side conditions, symbol types and dependency chain are recorded in `PROOF_SKELETON.md`. All checked obligations close under the stated import. The claims have the same quantified scope as their conclusions; no automorphism, uniform matching permutation, or additional graph-family assumption enters.

## Counterexample-directed checks

| Attempt | Algebraic outcome |
| --- | --- |
| An E-component with unequal intersections with two fibres | Impossible: its inter-fibre matching restricts to a bijection, and the inverse also lies in the component. |
| A non-symmetric Q escaping the exclusions | Weighted symmetry is preserved. The nonuniform profiles (4,1,1), (3,2,1), (2,1,1,1,1) were explicitly checked; no use of unweighted symmetry outside equal-weight blocks occurs. |
| Boundary or missed component profile | Positivity and sum six, combined with odd c≤6, give exactly the enumerated profiles. Zero quotient entries and zero diagonal entries remain allowed throughout. In the five-component case A=2,4,6 exhaust the closed permitted range. |
| A conjugate eigenvalue of unequal multiplicity | Impossible for integer Q: x²+x−14 is irreducible over ℚ, so its two roots occur with equal multiplicity in the characteristic polynomial. |
| An H eigenvalue at either strict bound | It would give E eigenvalue 7 on W, contrary to the simple global constant eigenspace of connected E. |
| Bipartite E with unbalanced fibre parts or Hz=0 | Pairwise equations r_i+r_j=6 and a third fibre force r_i=3. Each coordinate of Hz is odd, so zero is impossible; all potential H zero modes then lie in a one-dimensional space where H acts as −1. |

These are exact counterexample attempts against the load-bearing steps, not a numerical search. No verified counterexample or unresolved candidate was found.

## Open items and disposition

There are zero open FATAL, CRITICAL, MAJOR or MINOR findings in this scope. No repair is required. The representation remains the named dependency; formal Lean verification and cross-family semantic acceptance are not provided by this review. General false-twin-family existence/nonexistence and the order-58 problem remain open as expressly stated in the proof. Limits/integrability/probability/asymptotic checks are not applicable to this finite algebraic argument.

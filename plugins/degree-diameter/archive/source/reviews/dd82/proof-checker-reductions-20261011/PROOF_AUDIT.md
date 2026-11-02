# Reduction proof audit — 2026-10-11

**Verdict: PASS for the stated paper-level results, same-family provisional.** No mathematical gap or counterexample was found in the five requested sources. This does not establish arbitrary n62 or n59 nonexistence, and it is not a compiled Lean result or cross-family acceptance.

The fresh reviewer read the complete primary sources, `FOUNDATIONS.md`, the n59 global trace proof, the actual archived triple-edge enumerator, root-template generator and canonical partition source. The short-cycle papers used by the n59 final corollary were also read. No prior reviewer verdicts were read. The requested `gpt-6-astra` / `ultra` configuration was accepted by the parent invocation; this report has no independent backend attestation.

| Requested source | Outcome | Decisive checks |
|---|---|---|
| `proofs/dd82/N65_MOD29_TRACE.md` | PASS, paper proof | Actual graph forces B=0. M²=4J, MJ=17J. The complete power coefficient is 17(4·65)^14, so traces are 17 and 7 modulo29. Prime-orbit trace Frobenius applies. |
| `proofs/dd82/N64_MOD11_TRACE.md` | PASS, paper proof | Integral row-one defect gives B²=I; triangle-freeness gives tr(AB)=0. D²=17I+16B+4J becomes E+4J. The recurrence holds even at k=0. At exponent11 the incompatible residues are 5 and 9. |
| `proofs/dd82/N64_MOD5_DETERMINANT.md` | PASS, paper proof | Pair sum/difference vectors form a basis in characteristic5. The blocks are 33I+8J and I. Full determinant residue is 3, with 17² included; 3 is not a square. The rank-one formula requires no invertibility of a. |
| `proofs/dd82/n62/RECOVERED_REDUCTION.md` | PASS, paper reduction with exact finite check | Five-cell derivation, matrix/lift/Gram constraints, source enumeration completeness, multiplicity premise, parity, seven templates and 80 symmetry cases checked. All candidates map into the finite objects; no converse realization is assumed. |
| `proofs/dd82/n59/h5_nonzero_trace_constraints_20261011.md` | PASS under its explicit N15 hypothesis | Trace localization, same quadratic form counted twice, fourth/fifth walk coefficients, four row candidates, private-neighborhood coupling and full support forms checked. The optional ≥10 cycle corollary uses the short-cycle proofs explicitly. |

The foundations' root-ball, rational quadratic and original-defect arguments were checked as dependencies. The global n59 trace proof gives exactly tr(A⁴)=126n+s−12T and tr(A⁵)=428n+w−2s+102T. The five-step walk coefficient is 210T: 30 internal triangle walks plus 18·10 walks using one external incident edge, per triangle. These counts continue to hold when distinct triangles share vertices or extra unused chords are present.

## Adversarial checks

- **Finite-field degeneracy:** Checked integer nonnegativity before scalar reduction, all denominators only where invertible, the k=0 recurrence, full determinant scaling, and prime cyclic orbits. No exceptional branch remains.
- **Triple-edge coverage:** Reconstructed U,V directly from graph neighborhoods. In particular, the exact E,U equation gives CDᵀ=J, and the six D rows of any U_s must partition V. Positivity of Gram pairs is only a necessary filter. The other two N-types have forced overlap of Q and L, so the checker legitimately starts its lift search at N=J−I.
- **Enumeration completeness:** Read the full branching and propagation code. No orbit pruning discards Q choices; all eight L representatives are run. Copy relabelings normalize three matchings in each separate K₂,₂ block. Final parity uses all six permutations exactly once; this premise follows from the support table and is not merely presumed by the archived parity routine.
- **Root symmetry:** Checked each singleton class size and actual template fields. The 80 cases use relabelings of arbitrary graphs preserving fixed root data, without assuming those relabelings are graph automorphisms. They are coverage representatives, not a literal partition of labeled graphs.
- **Single triangle:** Allowed the three row types to vary before coupling them. The surviving arithmetic possibilities are (22[4],22[4],1111[1]), (22[4],211[2],211[3]), (1111[0],1111[2],1111[2]), and (1111[1],1111[1],1111[2]). The first three force private-neighborhood edge counts to be negative, equivalently violate the a-vector triangle inequalities. The last yields exactly (m_uv,m_uw,m_vw)=(2,0,0). Remaining repeat sets in the 38-point remainder may overlap; no disjointness assumption was inserted.
- **Optional short-cycle dependency:** Checked C3/C6 forced edges, C4's 39-point charge against the four private triangle budgets, C5 light-pair contradiction, C7's 21 versus14 charge, C8's step-three-edge elimination and 8 versus6 count, and C9's chord/light-pair and external-neighborhood coverage arguments. None uses a blanket N15 condition on nonzero vertices.

All these attempts left the stated conclusions intact. No alleged counterexample was reported merely because it was a candidate.

## Bounded exact check

The archived triple-edge checker ran to completion, with the root-template and S_DISJOINT signature audit functions invoked without their file-writing mains. Process affinity was one CPU; CPU and wall limits were 60 seconds. Total measured duration was **4.4371 seconds**. No SAT solver or old queue was run, and primary/archive/formal sources were not modified.

The per-lift Q counts were **13,5,5,1,5,1,1,1** in lexicographic bit order; only 111 survived the Gram test. Its 24 row supports and all six copy-pattern tables matched the source; there were zero six-row resolutions. Arithmetic checks reproduced the finite-field residues and the four n59 candidates. See `bounded_check_receipt.txt` and `.json` for exact output.

## Gaps outside the proved scope

These are acknowledged unfinished objectives, not defects in the scoped claims:

1. n62 still needs contradictions for all five double-repeat and both simple-repeat templates, plus any chosen graph-to-CNF satisfiability bridge and checked certificates. Historical RAW_UNSAT answers supply none of these proof obligations.
2. The n59 statements assume N15 for zero vertices. Deriving that condition from H5 is not proved by these files or by this audit. The single-triangle necessary form is not excluded, nor is the general range containing triangles.
3. Formalization and final theorem assembly remain separate. This review certifies no Lean build.

No edits to mathematical or formal sources were necessary. No fatal, critical, major or minor issues were opened. The artifact format follows the user's concise Markdown/JSON override; no hashes, manifests, TeX, PDF or HTML were generated. Wiki claim creation is left to the coordinating agent.

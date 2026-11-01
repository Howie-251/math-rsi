# Twenty-one-point mathematics, T34 round 01

Updated 2026-10-13; exact arithmetic results and scope are recorded below. The entire **minimum-degree-six branch has a complete paper candidate**. It is not yet a Lean theorem. The entire minimum-degree-seven branch now also has complete paper candidates. The minimum-degree-eight branch now also has a complete paper candidate. The complete 21-point map is `COMPLETE_TWENTYONE.md`.

## Complete degree-six candidate map

| Actual input | Proof | Exact new witnesses |
|---|---|---|
| At least two degree-six points | `MULTIPLE_SIX.md` | `MULTIPLE_SIX_WITNESSES.json`, 323 strict rows |
| Unique six, no seven | `UNIQUE_SIX_NO_SEVEN.md` plus frozen equality-case reduction | `EQUALITY_QUAD.json`, 5 strict rows |
| Unique six, one or more sevens | `SIX_WITH_SEVENS.md` | `SIX_WITH_SEVENS_WITNESSES.json`, 404 strict rows; 5 shared-vector certificates |

`SIX_UNIT_SET_LEMMA.md` isolates the reusable actual-input structural lemma: at least seven degree-eight unit neighbors of a six-degree point force all their mutual codegrees to be two and every x-edge to contain at most two of them, unless an existing strict witness already finishes the proof.

## Verification entrances

- `verify_exact.py` independently checks labelled-injection A/B/C, the complete unordered-slot capacity domain, exact rational quota deductions, selected degrees and total edge count. Run it against each of the three files listed above; each saved `_VERIFIED.json` records the result.
- `verify_joint.py ONE_SEVEN_FIVE_DUAL_JOINT.json` independently checks all five mixed-layout certificates using saved actual profile counts, independent injection probabilities and exact rational repaired-dual arithmetic. Output `ONE_SEVEN_FIVE_DUAL_JOINT_VERIFIED.json` has five passes. These use the parent's common-bad-vector mixed-layout inequality, not independent layout worst cases.
- The only old numerical inputs are the frozen (6,8,8)/(6,8,8,8) reduction witnesses in `context/propertyb34-hour1-20261013/low-math/TWENTYONE_SIX_REDUCTION_VERIFIED.json` and their domain source `TWENTYONE_SIX_QUAD.json`. They are reused, not rewritten.

## Targeted review obligations

1. General unit-set lemma: the induced empty/P3 graph classification and the extension of every pair to a P3 when a unit edge exists.
2. Multiple-six coverage: minimum third degree≤8; complete 668 residual list; common-unit set≥7 when λxy=2; a real x-edge supplies the final triple incidence.
3. Unique-six/no-seven: the frozen equality reduction, external codegree sum nine, and the actual xb-edge supplying exactly one common-four trace.
4. Unique-six with sevens: 677 two residues; the r=2 sets U and S and their cardinalities; r=1 unit-set argument, equal y-codegrees and actual xuv selection.
5. Mixed-layout certificate: all layouts share one actual bad-pair count vector; quota lower bounds and capacity repair are valid before averaging. Arithmetic has been independently replayed, while the abstract probability/actual-input connection is a proof obligation.

Each branch document gives exact coverage, definitions and evidence. Cross-model responses are saved by the parent and are not claimed here. The T34 claim remains open until all point-count branches, actual-input connections, Lean, audits and final review are complete.

## Added degree-seven candidate branches

- `AT_LEAST_THREE_SEVENS.md`: complete r≥3 candidate. For r≥5, 762 single-layout and 71 mixed-layout witnesses were independently verified; for r=3,4 the additional combined exact replay and all 20 mixed-layout witnesses passed. See `verify_three_four.log` and the source-specific `_VERIFIED.json` files.
- `TWO_SEVENS.md`: complete r=2 candidate. It finishes by a parity-of-counting contradiction for two actual matchings on the common unit-neighbor set. All 594 new single-layout rows and 53 mixed-layout witnesses passed independent exact checks (`verify_two_sevens.log`).
- `UNIQUE_SEVEN.md`: complete r=1 candidate. Two actual disjoint U pairs in x-edges fix the six-lock input; 203 single-layout and six mixed-layout witnesses passed independent checks (`verify_unique_seven.log`).
- The new universal degree-seven unit-set lemma is Section 1 of `TWO_SEVENS.md`: at least three degree-eight unit neighbors force pair codegree two and at most two such points per center edge, unless a strict selected witness supplies a coloring.

## Added degree-eight candidate

`EIGHT.md` closes minimum degree eight. The proof excludes codegree three using the at-most-two high-degree vertices, then contradicts a triangle-free unit graph of minimum degree six using C4 common edges and a two-profile claw extension. All 400 single-layout and 28 mixed-layout witnesses passed independent checks (`verify_eight.log`).

## Active next work

The 21-point paper candidate is complete; hand it to root for review and formalization. Continue mathematical work on 23 points with minimum degree at least seven, using the existing hour-one evidence. Reuse the subset position DP for all labelled orders and positions, then exact avoided-lock or joint-layout certificates on concrete residues. Prefer actual incidence contradictions to expanding local tables without a coverage argument. No whole-H enumeration, no Lean processes from this agent, no navigation edits and no other project access.

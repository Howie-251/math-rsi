# Two large-partner exclusions: corrected-proof delta audit

**Primary mathematical check: PASS14, zero open mathematical issues in the corrected source. Workflow verdict: PASS after inspection of the completed fresh blind post-fix review.** The original first-case proof contained a reversed quotient entry; the author corrected it during this review. Both corrected exclusions now follow from the stated actual-graph hypotheses.

Reviewed the current122-line `proofs/dd82/n62/D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`. Reviewer: `/root/proof_review_n62_d1_reduction`; requested model/effort `gpt-6-astra` / `ultra`, actual backend unattested. This is same-family provisional review. The reviewer did not edit the author paper.

## Resolved issue LP-01

- **Original status/severity:** UNJUSTIFIED, GLOBAL, CRITICAL; category DIMENSION_TRACKING / LOGICAL_GAP.
- **Original location:** first-case conclusion, formerly lines54–56.
- **Original claim:** d_K equals three on H, so for v∈X the entire left side of (A d_K)(v)+d_K(v)=20 is a multiple of three.
- **Problem:** d_K on H is the outgoing quotient degree a=5, not the reverse entry b=3. The asserted coefficient was false under the case hypotheses and the displayed congruence did not follow.
- **Fix:** CORRECT_COEFFICIENT / ADD_DERIVATION. The author changed the conclusion to

      20 = 5 x_v + 3 |N(v)∩Y|.

  The already forced x_v is two or three. Hence 20−5x_v is ten or five, neither divisible by three. This gives the required contradiction without changing the theorem hypotheses or conclusion.
- **Downstream check:** the second case uses d_H on K=b=3, which is correct. Its parity argument is unaffected. The combined necessary-case list still has eight entries if the two exclusions are accepted.

## Primary obligation ledger

All14 mathematical obligations below are discharged in the corrected source.

| ID | Checked implication |
|---|---|
| L01 | The hypotheses concern actual distinct B-components with the listed integer sizes, original internal/cross degrees, and the accepted exact moment constraints. No D1-specific structure is additionally needed within either exclusion. |
| L02 | For any component C, B1_C=3·1_C; thus (A²+A)1_C=10·1_C+|C|·1. Outside C this gives (A d_C)+d_C=|C|, with no individual-component invariance of A assumed. |
| L03 | Equitability makes each exterior type a union of complete B-components. Even component size plus the explicit B≤2 condition gives minimum nonempty size4, also for type00. |
| L04 | For h12,k20,a5,b3,s1,t2, the exterior moments are Sx24,Fx36,Sy60,Fy120,Qxy0 on30 vertices. They agree with the accepted formulas. |
| L05 | Qxy=0 gives disjoint positive supports X,Y. Qy=180 and Cauchy give |Y|≥20, hence |X|≤10, allowing any zero type initially. |
| L06 | Domain5x+3y≤20 gives x≤4. A nonempty x4 type would contribute≥48 to Fx36, so x≤3. Writing u,v,w for x1,x2,x3 counts gives u=3w−12,v=18−3w,|X|=6+w, whence w=4,v=6,u=0. |
| L07 | X has ten vertices, forcing Y to have twenty and no remaining zero-type vertices. Equality in Cauchy yields y=3 on Y; equivalently Σ_Y(y−3)²=180−360+180=0. The exact exterior distribution is (2,0):6,(3,0):4,(0,3):20. |
| L08 | For v∈X, N(v) avoids K and d_K is5 on H,3 on Y,0 on X,2 on K. The corrected identity20=5x_v+3d_Y(v) contradicts x_v∈{2,3}. |
| L09 | For h12,k24,a6,b3,s0,t2, the moments are Sx24,Fx24,Sy72,Fy168,Qxy72 on26 vertices. The domain reduces to x+3y≤12,2x+y≤8,x+y≤8. |
| L10 | x4 would require factorial contribution≥48. If x3 occurs, minimum type size and Fx24 force exactly four such points, no x2, and twelve x1. Their respective y-bounds2 and3 give Qxy≤60, contradiction. Hence x≤2. |
| L11 | The x moments force twelve x2 and fourteen x0 vertices. Since Qxy72 and y≤3 on x2, all twelve have type(2,3). |
| L12 | On the other fourteen points, y moments give Σn_j14,Σj n_j36,Σj(j−1)n_j96. Thus2n4−n1−n2=12; evenness gives n4=6 or8. The first yields n3=n0=4; the second forces n1=4,n2=n3=0,n0=2 and is forbidden. The displayed four-type distribution is exact. |
| L13 | Type(0,3) has four vertices. For any one, d_H is0 on H,3 on K,2 on the twelve-point X and0 elsewhere. The component identity gives12=9+2|N(v)∩X|, impossible by parity. |
| L14 | Combining the corrected exclusions with the separately checked finite inequalities and pure12×12 exclusion removes precisely two more cases from ten, leaving the seven k16 cases and the single k20,s0,t2 case. This is a conditional remaining list, not graph realization or D1 exclusion. |

The exceptional cases checked include the initial possible00 type, multiple x3 types, the forbidden two-point00 residue, and the distinction between outgoing and reverse quotient entries. In the second case, multiple x3 types cannot occur because each would have at least4 points while their combined factorial budget permits only4 total. The coefficient orientation was rechecked separately for both final identities.

## Completed fresh blind post-fix review

The project [proof-checker skill](/inspire/hdd/project/project-public/mahaitong-240108120090/global_user/ar4math/.agents/skills/proof-checker/SKILL.md), Phase3.5, requires: “For any fix that resolved a FATAL or CRITICAL issue, submit the fixed section alone ... to a fresh Codex thread.” The initial spawn and follow-up attempts failed with **agent thread limit reached** and did not execute; those failures remain recorded in JSON as historical events.

The parent subsequently started `/root/proof_review_n62_two_partners_blind` with the current proofs and no previous critique. Its actual [Markdown audit](../proof-checker-n62-two-partners-blind-20261011/PROOF_AUDIT.md) and [JSON receipt](../proof-checker-n62-two-partners-blind-20261011/PROOF_AUDIT.json) were inspected during the size-sixteen delta review. The receipt explicitly records no prior target audits read and returns PASS for both exclusions. It independently checks the corrected coefficient d_K|H=5 and the congruence 20=5x_v+3d_Y(v), as well as the second case's parity contradiction. The required post-fix review is therefore complete. This remains same-family provisional acceptance; the original error, repair, and failed early attempts are not erased.

No solver, LP result, finite separator table, hashes, TeX/PDF/HTML, or order63–65 computation was used in the two pure exclusions. Their no-triple/component-size premise remains an explicit prior import. The whole D1 branch and arbitrary order62 remain open.

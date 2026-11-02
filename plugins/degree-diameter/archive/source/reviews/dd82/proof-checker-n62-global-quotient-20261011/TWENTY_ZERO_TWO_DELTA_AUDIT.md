# Twelve-by-twenty zero/two case: quotient-divisibility audit

**PASS10 — zero open issues.** The quotient-divisibility argument excludes the actual component parameters (h,k,a,b,s,t)=(12,20,5,3,0,2). Its proof does not depend on a finite table, LP status, or the exclusion of repeat entries three.

Reviewed all193 lines of `proofs/dd82/n62/D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`. Reviewer `/root/proof_review_n62_d1_reduction`, requested `gpt-6-astra` / `ultra`, actual backend unattested; same-family provisional acceptance. No source edits were made.

The component quotient from the accepted global note is the only essential import. It is a quotient of the actual original adjacency matrix on all positive-support B-components; it does not assert that A preserves each component separately. The pointwise estimate is derived directly in this note. The exterior moments at the end provide an equivalent interpretation, not an additional existence assumption.

| ID | Checked implication |
|---|---|
| Q01 | The assumed distinct components have sizes12,20, cross degrees5,3 and internal degrees0,2 with the stated orientation. The actual integer quotient satisfies row sums8, detailed balance, and R²+R=10I+1n^T. |
| Q02 | The H row has remaining weight8−0−5=3; hence each exterior p=r_HE is an integer in0,…,3. If x=r_EH>0, balance12p=|E|x and positive component size force p>0. |
| Q03 | Balance12p=ex and20q=ey implies12py=20qx, hence3py=5qx and5 divides py. All numbers are integers. |
| Q04 | If x,y>0, then p∈{1,2,3}, each coprime to5, so5 divides y. |
| Q05 | At v∈E, (A²+A)1_H=10·1_H+12·1 gives Σ_{u∈N(v)}d_H(u)+x=12. Its y neighbors in K each contribute r_KH=3, giving x+3y≤12. With x,y positive this forces1≤y≤3, contradicting Q04. |
| Q06 | Therefore every exterior component has xy=0. If x=0 then p=0 by balance, so py=0 as well; there is no unhandled zero-coordinate case. |
| Q07 | The HK quotient entry is0·5+5·2+Σ_E py+5=20, henceΣ_E py=5. This contradicts Q06 and closes the claimed component exclusion. |
| Q08 | The optional exterior interpretation has N30,Sx36,Fx48,Sy60,Fy120,Qxy60 and the stated pointwise domain. Summing exy=12py gives the same impossible positive mixed moment. These constants match the accepted exact formulas. |
| Q09 | A whole type T_xy is a union of B-components. Summing their integer quotient entries makes original neighbor counts into T constant on H and K. Double-counting gives12 divides |T|x and20 divides |T|y, including empty or zero-coordinate types. |
| Q10 | The exclusion is for arbitrary actual components with the specified parameters. The combined seven-case H12 list is conditional on the other reductions and their review status; it is not a graph-realizability or full D1 claim. |

The critical arithmetic step uses p≤3 before cancelling its factor modulo5. It would not remain valid for unrestricted p, but the required bound is explicitly proved from the H row. The pointwise bound uses the correct reverse entry d_H|K=3, and the off-diagonal quotient equation uses the correct outgoing entry r_HK=5. Every zero case is covered without division by p,x or y.

No nonempty-type minimum or evenness is used in the main contradiction. Exterior components of any positive size are permitted, so no global no-triple or finite-check dependency is introduced by this particular argument. The extra type divisibilities also do not require positive x or y.

No counterexample or source repair was needed. The parent has separately started a fresh blind reviewer for this note and the corrected two-partner note; that result was not needed for or represented as evidence in this primary audit. No solver, enumeration, hashes, TeX/PDF/HTML, or order63–65 work was performed.

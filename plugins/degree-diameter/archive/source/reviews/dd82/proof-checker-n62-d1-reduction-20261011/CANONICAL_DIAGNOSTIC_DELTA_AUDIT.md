# Canonical hard-D1 diagnostic delta audit

**PASS14 — zero open issues.** The two surviving representatives are exactly sufficient for coverage: **b=28 or b=41** after normalizing c=35 in C5. All recorded constraints are necessary conditions under the proved hard-D1 hypotheses. This same-family provisional review does not certify a solver, CNF translation, or D1 exclusion. Requested reviewer: `gpt-6-astra` / `ultra`; actual backend identity is unattested.

Reviewed the complete `proofs/dd82/n62/D1_MATCH_CANONICAL_DIAGNOSTIC_COVERAGE.md` and its JSON companion `d1_match_canonical_diagnostic_constraints_20261011.json`, reusing accepted hard-D1/C4 deductions. Compared literal class IDs with the archived `n62_root_templates.json` D1_MATCH entry and inspected `class_layout`, `parent_map`, and `ABEncoder.fixed_A`. No source edits or solver/encoder execution occurred in this review.

## Decisive new argument

For the actual pair (5,r), singleton parenthood gives A_5r=0 and the established row of r gives B_5r=0. Hence their common-neighbor count is one. Since N(5)={0}∪C5 and r is not adjacent to 0, r has exactly one neighbor in C5. Both b and c are distinct neighbors of r, so after c is placed in C5, b cannot be W5. This directly excludes b=34; it does not rely on a diagnostic result.

The relabeling is simultaneous and lossless: swap parent labels 2,3 if necessary; permute 5–8 to put c in C5; then permute the remaining 6–8 to put b's parent at 6 if it is neither 4 nor 5. Independent within-class permutations send the proved-distinct pairs (r,u2), (p,u3), (W4,q), and (Wi,Ui) to the displayed IDs. Thus no additional automorphism or matching choice is assumed.

## Checked obligations

| ID | Conclusion | Evidence |
|---|---|---|
| C01 | Archived IDs agree exactly. | The companion's eight classes equal the D1_MATCH `singleton_classes`; exceptional parents are 9→123 and 10→14. The archived encoder reads these maps directly. |
| C02 | r may be normalized into C2. | The 2↔3 permutation preserves the exceptional parent pattern; inherited hard-D1 proof gives r∈C2∪C3. |
| C03 | c may then be normalized into C5. | The full permutation group on labels 5–8 preserves that pattern and the already fixed labels 1–4. |
| C04 | b has representatives W4,W5,W6. | After fixing c's parent, the remaining 6–8 form one orbit; labels 4 and 5 form the other two. |
| C05 | All displayed within-class IDs can be fixed together. | Each class has at most two distinguished points, and every relevant pair is proved distinct. No s,t,f,g or matching mate is assigned inadvertently. |
| C06 | b=W5 is impossible. | The unique C5-neighbor argument above excludes two distinct neighbors b,c there. |
| C07 | The JSON row-16 class counts are correct. | B_Xr=0; for every i≠2 the sole common neighbor of i,r must lie in Ci, since r avoids 0,w,a. C2 is independent. Together with parent 2 this gives degree eight. |
| C08 | All eleven complete original rows are valid. | Rows 0–8 are the actual parent template; rows 9,10 are exactly the established W and U neighborhood profiles. Every row has eight distinct entries. |
| C09 | The four additional A literals are necessary. | r is adjacent to b,c; a,r are nonadjacent; b,c are nonadjacent because both are distinct neighbors of triangle-free r. |
| C10 | N(r)∩U={35}, N(r)∩W={b}. | The base proof gives CN(a,r)={c} and CN(w,r)={2,b}; U and W are the ordinary portions of those neighborhoods. |
| C11 | All six complete B rows are exact. | Direct substitution of canonical IDs into B0,Bw,Ba,B1,B2,B3; unlisted entries vanish because each established row is exhausted. |
| C12 | Partial row 4 has precisely the stated safe domains. | f∈U excludes u3,c, leaving {17,42,49,56}; g∈W excludes W4. The equivalence f=u2 iff b=W4 gives {17} for b=28 and {42,49,56} otherwise. |
| C13 | Partial row 16 and the optional b=28 refinement are valid. | Its distinct unit endpoints have domains {9},C3,C4∪…∪C8. At (4,r), B_C4,r=A_fr+A_gr=[g=b]=B4b. If b=W4, this is zero and t∉C4. The JSON deliberately retains the broader valid domain; it does not encode this optional strengthening. |
| C14 | Companion fields and branch statuses match the proof. | A direct JSON comparison checked every class, role, complete row, fixed A entry, intersection, partial-row group and status in all three cases. b=34 is expressly marked excluded; the two surviving cases are only necessary constraints. |

The mechanical comparison also checked symmetry wherever both complete rows are listed, row sums, and the actual common-neighbor formula on all pairs whose two A rows are complete. This is a transcription/algebra check, not a graph search.

No issue was found in the meaningful exceptional cases: s=p remains allowed; b=g remains allowed; b=W4 correctly forces f=u2; the optional restriction t∉C4 for b=28 is not silently required by the JSON. Its broader domain is a sound weakening. The excluded b=34 entry is suitable only as an explicitly contradictory specification, not a surviving representative.

The audited JSON supplies semantic matrix/graph constraints, not DIMACS literal numbers. Any encoder must still honor its complete-row zeros, unit-group semantics, and actual B definition. The archived class/parent mapping is aligned, but this review does not certify a complete CNF bridge or authorize combining unrelated historical symmetry breakers. No SAT, hashes, TeX/PDF/HTML, or order63–65 work was performed.


## Limited prepared-driver inspection

After the parent reported preparing inputs, inspected `computations/dd82/n62/d1_hard_diagnostic.py` without executing it. Its extra structural facts are necessary under the accepted papers:

- B support from H stays in C2∪C3∪C4, by the exhausted total weight 15 in the five H rows.
- B[C2]=0 and B(C3,C4)=0 are the exact proved blocks.
- Each original A[Ci] block is zero for i=1,2,3,4 because its parent label i is triangle-free. This does not assert that every vertex in those classes is triangle-free.
- The exact triangle-free set used by the driver is {0,1,2,3,4,w,a,r,p,q,b,c}. The base proof handles 0,1,2,3,4,w,a,r; positive repeats from a transfer its status to p,q, and positive repeats from 2,3 transfer their status to b,c.
- The driver transcribes complete-row zeros and row-16 class counts directly. For each partial B row it sets every allowed B2 selector false, forces exactly one B1 selector in each disjoint group, and zeros entries outside the fixed/group support. This matches the audited group semantics. The excluded b=34 case is skipped.

No additional symmetry breaker is introduced in those loops. This addendum checks the necessity of the added mathematical facts and the visible helper semantics; it does not certify the archived encoder as a whole or independently replay every numeric emitted clause.

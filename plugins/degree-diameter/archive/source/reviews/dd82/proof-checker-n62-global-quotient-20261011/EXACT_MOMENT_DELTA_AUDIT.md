# Exact exterior-moment separator delta audit

**PASS10 — zero open issues.** The standard-library checker was rerun successfully: **33 parameter cases, 21 exact integer separators, 334 pointwise evaluations, 12 remaining cases**. The original-graph implication and parameter coverage also check out. Semantic acceptance is same-family provisional; the integer arithmetic result is deterministic evidence.

Inputs reviewed: `proofs/dd82/n62/D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`, `computations/dd82/n62/check_component_exterior_separators.py`, and the complete case data in `computations/dd82/n62/component_exterior_moments.json`. Requested reviewer is `gpt-6-astra` / `ultra`; actual backend identity is unattested. No source was edited, and no LP or SAT solver was run in this audit.

## Mathematical and computational obligations

| ID | Checked obligation | Result |
|---|---|---|
| E01 | Actual H12 graph maps into the five (k,a,b) triples. | The accepted minimum paper gives the list. Independently enumerating integer a≥4,b≥3 with a(b−1)≤14, balance k=12a/b and even k≥12 returns exactly those five triples. |
| E02 | The internal-degree ranges are complete. | Nonnegative integer s,t satisfy s+a≤8 and t+b≤8. The checker's ranges include both endpoints and all such choices. |
| E03 | The exact vector M is the sum of the feature vectors. | First/cross moments are from the accepted actual-graph identities. Subtracting Sx from Qx gives 12(14−s²−a(b−1)); similarly for y. N=50−k. All six coordinates match the displayed order. |
| E04 | Filtering negative coordinates is valid and the case list is complete. | Every feature 1,x,y,x(x−1),y(y−1),xy is nonnegative at nonnegative integer counts. Negative M entries contradict an actual graph. The surviving elementary cases number 4,9,9,7,4 for k=12,16,20,24,28 respectively, totaling33. |
| E05 | Each reconstructed point domain covers every actual exterior vertex. | Integer x,y≥0, x+y≤8, (s+1)x+by≤12 and ax+(t+1)y≤k are exactly the proved pointwise restrictions. The loops exhaust this domain; further type parity/component restrictions are safely omitted. |
| E06 | All 21 coefficient vectors give nonnegative pointwise values. | Each has six genuine integer coefficients. The supplied checker verifies every point in every associated domain. An independent direct polynomial evaluation agrees. There are334 evaluations, counted with their case domains, not334 distinct plane points. |
| E07 | The targets are exact negative integers and the paper table matches. | All21 paper coefficient vectors and targets were parsed and compared to the data. Direct integer dot products agree with every listed negative target. |
| E08 | Pointwise inequalities exclude actual graphs in those cases. | Summing z·φ(x_v,y_v)≥0 over actual exterior vertices gives z·M≥0, contradicting the checked negative integer. No feasibility assumption is reversed. |
| E09 | The remaining list is exactly the complement of the exclusions. | All12 paper entries match the complement of the21 checked cases among33. In particular all four k28 elementary cases are excluded. Remaining entries are not certified realizable. |
| E10 | The proof does not depend on floating LP outputs. | The checker uses only pathlib, itertools, JSON parsing, and integer operations. LP status/weights are not numerical proof inputs; only the exact coefficient data are checked. “Remaining” means not excluded by these inequalities. |

For an independent cross-check, the review regenerated M through the general square-moment formulas Qx=12(22−s−s²)−kb² and Qy=k(k+10−t−t²)−12a², then subtracted the first moments. It used ranges s,t=0,…,8 with explicit degree filters and derived the size/incidence triples, rather than importing the checker's hard-coded list. This reproduced all33 cases. It also reconstructed each domain and evaluated the coefficients directly as a polynomial, checked the21 Markdown table rows against JSON, and compared the Markdown remaining list to the exact complement.

The supplied checker rejects duplicate keys, missing/extra parameter cases, differing moments or domains, malformed coefficient lengths, negative domain values, or nonnegative/mismatched targets. For the data reviewed, all33 entries are present and the status split is exactly21 checked separators and12 unexcluded entries.

## Boundary

This finite result is independent of the separate pure12×12 exclusion; its12-case list intentionally still includes the two opposite-diagonal k12 cases. Floating feasible weights are not graph witnesses or exact integral type assignments. The discovery driver's timing and floating optimization were not rerun or certified here. The moment derivation remains an explicit paper dependency, and the checker is not a Lean theorem or an order-62 exclusion.

No fixes were needed. No hashes, TeX/PDF/HTML, or order63–65 work was performed.

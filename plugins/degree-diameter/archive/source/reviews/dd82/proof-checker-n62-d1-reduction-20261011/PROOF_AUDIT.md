# D1_MATCH local reduction: fresh proof audit

**Verdict: PASS for the stated local reduction, 36 obligations discharged, zero open issues.** This is a same-family provisional semantic judgment. It does not exclude D1_MATCH or establish an order-62 upper bound.

Reviewed all 209 lines of `proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md`, including the completed final section (16). The author confirmed the file was stable. Review requested `gpt-6-astra` with reasoning `ultra`; the running backend/model is not independently attested. Fresh reviewer task: `/root/proof_review_n62_d1_reduction`. No author source was edited.

The accompanying `PROOF_SKELETON.md` supplies the assumptions, types, dependency DAG, and the 36 individual obligations. Review was based on the proof text and mathematical dependencies, not prior verdicts.

## Results that matter

The residual endpoints r,p,q really are three distinct ordinary vertices. Equation (1) has nonnegative summands and right-hand side at most one, so it simultaneously forbids a repeated endpoint between the rows of w and a and a doubled remaining entry in the row of a. Earlier row calculations exclude X, w, a, and C1 as appropriate; no endpoint is merely assumed ordinary.

The D0 reroot argument uses the original graph. Since w is triangle-free, the positive repeat B_wr=1 makes w,r nonadjacent and gives precisely two common neighbors. If r∈C4, those two parents are in W and disjoint from {1,2,3}. The heavy mate 0 and light mate r are nonadjacent in G. The complete B_w row ensures all other rerooted outside vertices have one parent. Thus every D0_MATCH hypothesis is satisfied. In the D0 theorem's four-cycle, the third mate of its heavy vertex 0 is the original a, giving exactly B_ar=2. This contradicts the already derived zero entry. No classification algorithm or triple-repeat elimination is needed here.

After r is normalized into C2, the commutation entries distinguish b and c: b is in W, while c is adjacent to a and outside W. The (2,r) entry forces r adjacent to b. The (w,c) entry forces r adjacent to c because its BA side is the single Boolean A_rc and its AB side already has the contribution B3c=1. Since a is triangle-free, a and r cannot also be adjacent. Their zero repeat entry then gives exactly one common neighbor, namely c. Thus rerooting at w has the actual parent pair {2,b}, intersecting the heavy parent triple {1,2,3} in precisely one point.

The three matchings in G and the three matchings in B are independently derived and remain separate. Their omitted points are respectively (u2,u3,W4) and (r,p,q). The proof establishes that corresponding omitted points differ. The weight 18−3=15 in the repeat calculation exhausts every H row; this legitimizes later removal of all classes C5,…,C8 from repeat sums. Formula (15) is an equality of multisets of H-mates, allowing both terms to choose the same mate. The case b=W4 remains permitted.

The final transport appendix is valid. At an ordinary target y, direct expansion gives

    (BA)_2y = 1_{y∈C1∪C3}+A_by,
    (AB)_2y = 1_{y=r}+B_C2,y,

and the analogous formula for row 3. The previously proved neighbor counts therefore give zero internal repeat degree throughout C2, and internal repeat degree one exactly at v1,v2 in C3. Symmetry and zero diagonal force the single unit edge v1v2. They also give one cross-repeat unit in every row on both sides of C2–C3. The original cross matching follows separately from common-neighbor counts. Nothing in these equations equates the two matchings or contradicts their coexistence.

## Dependency inspection and hypothesis discharge

`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, sections 1–4, gives a closed repeat prism for every original triangle. Its only local import is `S_TOUCH_SATURATED_ROW_EXCLUSION.md`. That derivation uses the saturated root/label rows, actual parent sets, triangle budget, nonnegative integrality and commutation; its steps do not require a global restriction B_xy≤1. The stronger universal use made by the pairing proof is therefore legitimate. Saturation of all six prism rows proves the triangle-status homogeneity used for a,4,r,c. Evenness of the total number of triangles alone would not suffice, and is not substituted for this fact.

`D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, section 1, was inspected directly. Its three distinct c_i are forced by the (c_i,w) row sum, and their common adjacency to the light mates gives B_ab≥2+A_ab. The remaining budget on a forces A_ab=0,B_ab=2; the four rows close. This local theorem is independent of that file's global parity/outlet argument, and applies to the reroot as detailed above.

Only the elementary actual-graph identities and displayed D1 template definitions from `RECOVERED_REDUCTION.md` are needed. Its triple-repeat finite checker was not rerun or used. The source's suggested future parity route is a remaining research obligation, not a theorem proved by this audit.

## Targeted counterexample and degeneracy pass

All attempts below were checked algebraically against the premises; none supplies a counterexample to a reviewed conclusion.

- Set r=a, or put r in C1: the (1,w) entry has fixed BA value two and would have an extra positive AB term.
- Identify r with p or q, or assign a double residual repeat from a: equation (1) would have left-hand side at least two and right-hand side at most one.
- Put r in C4: the actual reroot has the D0_MATCH premises and hence forces B_ar=2, contrary to (1).
- Identify b=c: the two commutation entries with w demand A_bw=1 and A_cw=0 simultaneously.
- Add edge ar: the already derived edges ac and rc form a triangle at the triangle-free vertex a.
- Put c at u2 or u3: the first creates an edge within the independent C2, and the second gives an adjacent positive repeat at triangle-free label 3.
- Identify p with u3 or q with W4: the first violates triangle-freeness of a; the second violates the nonnegative equality A_ar=A_pw+A_qw=0.
- Allow the two H-mates on either side of (15) to coincide: the equation retains multiplicity two and the text permits it. No unsupported distinct-mate inference occurs.
- Keep b=W4, or allow triangles elsewhere in C5,…,C8: neither option is falsely excluded. Every triangle-freeness application concerns a vertex whose status was actually proved.
- Add another internal C3 repeat, or double v1v2: the internal row sums from (16) forbid both. Collapse v1=v2: a common-neighbor set contains distinct vertices, and exactly two C3-neighbors were proved.
- Identify either v_i with u3 or the original C3-mate of r: this gives a triangle at c, whose triangle-free status follows from positive B3c and triangle-status homogeneity.

This pass checks the proof's possible endpoint collisions and uses of saturated weights. It is not a search over full order-62 graphs and provides no existence or nonexistence certificate beyond the deductions above.

## Acceptance and remaining work

All hypotheses used in the applications are discharged in the skeleton; the dependency DAG is acyclic. The single WLOG step is a permissible relabeling. No source fixes were needed. Review artifacts are Markdown and JSON only; no computation or output of digests, no TeX/PDF/HTML, no SAT, and no new formal assumptions were introduced.

The reduction is sound modulo its inspected paper imports. A cross-family overlay and any Lean connection remain separate work. D1 exclusion, an even-double-edge theorem for its repeat components, and exclusion of arbitrary order-62 graphs remain open.

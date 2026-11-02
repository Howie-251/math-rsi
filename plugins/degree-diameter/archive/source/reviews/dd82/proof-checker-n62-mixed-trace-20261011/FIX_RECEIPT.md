# Minimal type-one paragraph clarification

Date: 2026-10-11. Editor and fresh reviewer: `/root/proof_review_n62_mixed_trace`.
Authorization: root executor explicitly requested this reported minimal correction after receiving the review finding. Only the sentence cluster in §5 of `proofs/dd82/n62/CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md` was edited.

Before:

> The pair $a,c$ has common neighbors $h,b$. Neither can be a heavy endpoint, by the preceding isolation property, so $B_{ac}=1$. Thus $\{w,a,c\}$ is a unit repeat triangle.

After:

> The pair $a,c$ has common neighbors $h,b$. The repeat mates $a,c$ cannot be heavy endpoints, by the preceding isolation property. They are nonadjacent and have the two distinct common neighbors $h,b$, so $B_{ac}\ge1$; as neither endpoint is heavy, $B_{ac}\le1$. Thus $B_{ac}=1$, and $\{w,a,c\}$ is a unit repeat triangle.

Why the clarified argument holds: a,c both meet b in the positive mate graph, so neither can be a heavy mate, which would have to be isolated. Triangle-freeness excludes a~c. Also h∈N_G(w) while b is a repeat nonneighbor of w, so h≠b. The actual common-neighbor equation gives B_ac≥1; nonheavy endpoints exclude B_ac=2, and B≤2 is a stated input. The equalities B_wa=B_wc=1 and P_a∩P_c={h} then give a unit triangle with exactly one common original neighbor.

Classification: MINOR clarity issue, fixed by ADD_DERIVATION. No strengthened hypothesis, weakened conclusion, new lemma assumption, or claim of zero mixed trace. The final paragraph was reread and verified by the same fresh reviewer. There was no second independent reround. Cross-family overlay remains the root executor's task.

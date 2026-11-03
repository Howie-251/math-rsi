# Global double-triangle quotient: proof audit

**PASS36: all 36 obligations discharged; zero open issues.** This is same-family provisional semantic acceptance of the stated necessary restrictions, conditional on the explicit inspected/reused paper imports. It does not prove evenness of D1 double-edge counts or exclude an order-62 graph.

Reviewed `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, all 284 lines and all six sections. Requested model/effort: `gpt-6-astra` / `ultra`; actual backend metadata is unattested. The main reviewer is `/root/proof_review_n62_d1_reduction`. An independent bounded shard, `/root/proof_review_n62_d1_reduction/signed_spectral_delta`, checked sections 3 and 6 and reported no concrete error. The main reviewer checked those arguments as well and integrated the shard's obligations. No author source was edited.

The companion skeleton contains the quantified claim, dependency/import ledger, symbol scopes, and all individual obligations. No acceptance here is based on an unsuccessful graph search or an earlier verdict alone.

## Main findings

Generated triples are genuinely disjoint. D2 exclusion is the necessary imported ingredient that makes each generated pair's common-neighbor count exactly two. Without it, the intermediate equality would not follow from the row budget alone. With the imported root classification, only the heavy endpoint can have both parent labels: the light parent pair meets the triple in at most one point, and ordinary vertices have one parent. One shared generated vertex would require four unit repeats, while two shared vertices would acquire four distinct common neighbors. The double-edge endpoints themselves form a matching. Together with original triangle disjointness and triangle-free status of D and S, this proves 5d+3T≤62.

The D0 companion prism is independent in the original graph in both branches. BOUT follows directly from the c_i parent labels. In MATCH, the c_i have at most one original neighbor in the first generated triple. Equitability of the whole component partition forces a common internal degree zero or one. If it were one, writing

    A[K] = [[0,P],[P^T,0]],
    B[K] = [[J−I,I],[I,J−I]]

would give a zero-diagonal permutation P. Closure of B[K] gives (AB)[K,K]=A[K]B[K] and (BA)[K,K]=B[K]A[K], even if A has many edges leaving K. The upper-left blocks force P=P^T. Such a permutation would be a fixed-point-free involution on three points, impossible. Thus the companion has internal original degree zero. The argument never assumes A preserves K individually.

The quotient acts on the entire component-constant eigenspace. If L has the component indicators as columns, AL=LR, BL=3L, and JL=L1n^T. This gives R²+R=10I+1n^T. Detailed balance makes R similar to a symmetric matrix and gives n^TR=8n^T. Thus ker(n^T) is invariant, while span(1) supplies the single eigenvalue eight. The integer characteristic polynomial is

    (x−8)(x²+x−10)^m.

Consequently k=2m+1 and trace R=8−m, giving k+2Σr_ii=17. The coefficients in (6) are correct: a D0 component with its companion contributes 2 or 4, and an original paired-triangle prism contributes 5. The latter's internal original degree is two because the triangle-pairing theorem places the two triangles outside each other's original neighborhoods.

For D1, the exact rows place 1,2,3,4,b,c in K and the heavy endpoints with a,r in H. The actual neighbors give r_HK≥4,r_KH≥3 if the components differ, and r_HH≥4 otherwise. The “at most two” discussion is a degree restriction on the D1 incidence relation. It does not identify different heavy edges or force them into pairs. D0 components have their separate single-companion structure.

The port count also needs the fact that D1 light mates have fully unit repeat rows, in addition to the no-unit-triangle lemma. The former keeps them outside D; the latter keeps them outside S; triangle pairing keeps them outside original triangles. These facts are all present in the cited hard-D1/C4 imports. Summing the 2d1 unit ports into W against its total row capacity three proves 15d+9T+2d1≤186 without assuming distinct mates for different heavy edges.

## Signed-eigenspace and trace check

For each bipartite B-component C choose q_C equal to +1 and −1 on its two parts and zero elsewhere. Weighted regularity forces equal part sizes. Hence Jq_C=0, and the entire B=-3 eigenspace is spanned by these vectors. Commutation preserves this entire space, so A²+A=4I there.

A may mix these signed component directions. Writing Aq_j=Σ_i M_ij q_i, evaluation at a vertex of C_i+ gives

    M_ij = |N(x)∩C_j+| − |N(x)∩C_j−| ∈ Z.

The eigenspace condition guarantees the opposite value on C_i− and zero on nonbipartite components. Thus the restriction matrix is integral without any individual-component invariance assumption. Its characteristic polynomial is (x²+x−4)^(ell/2), giving ell even and trace M=−ell/2.

For x in C, the component-indicator equation makes s(x)+t(x) constant, and the signed diagonal equation makes s(x)−t(x)=M_CC constant, on both sides. This justifies s_C,t_C and their summed trace. The D0 cycle's bipartition is {0,b}|{w,a}. Its BOUT original edges 0b and wa stay within those sides, so its contribution is **+1**, while MATCH contributes zero. If any D0 exists, ell is positive and the total trace strictly negative. A non-D0 bipartite component must therefore have t_C>s_C. It cannot contain a generated triangle or an original triangle, since either supplies a triangle in B support.

## Counterexample/degeneracy pass

No counterexample to a reviewed conclusion was found. The following meaningful potential failures were checked:

- Overlapping generated triples: one shared vertex violates row sum three; two shared vertices violate the exact common-neighbor count. The distinctness of the four heavy endpoints is proved before that count is used.
- A D0_MATCH prism with a 3-cycle original cross matching: its cross permutation is not symmetric and violates the K,K commutator. A fixed point instead violates nonadjacency of its matched positive-repeat pair.
- Original edges leaving a B-component: permitted throughout. Equitability and both spectral restrictions concern full eigenspaces; the only block-local commutator uses B-closure.
- k=1: the quotient equation gives R=[8], m=0 and 1+16=17, so no missing nonprincipal-eigenvalue assumption is used.
- ell=0: the signed conclusions are vacuous. The additional-component conclusion explicitly starts from existence of a D0 component, which makes ell>0.
- Mixing signed indicators between different components: the displayed integer coefficient formula remains valid and preserves the trace proof.
- Reversing the BOUT sign: direct evaluation on {0,b}|{w,a} gives +1, not −1.
- Coincident D1 light mates from different heavy pairs: the port estimate allows up to three incoming units at each target and does not count targets as distinct.
- H=K in a D1 configuration: retained explicitly in (8); no proof step presumes heavy and generated motifs live in different components.
- T=0 or absence of D0 components: the removal and bookkeeping formulas remain valid, and no extra component is asserted without a D0 premise.

## Acceptance and limits

All assumptions at applications and all finite algebraic steps are discharged in the skeleton. No source repairs were needed. The bounded spectral shard agrees on its assigned eight obligations; it does not independently certify the whole paper or provide cross-family acceptance.

The source openly imports the recovered triple-repeat result and root-template coverage; their finite computation was not rerun. This audit creates only Markdown and JSON, introduces no formal axioms, and performs no SAT, TeX/PDF/HTML, digest generation, or order63–65 work. Lean connection and the separate cross-family review remain outside this audit. The claimed necessary restrictions pass; the order-62 exclusion remains open.

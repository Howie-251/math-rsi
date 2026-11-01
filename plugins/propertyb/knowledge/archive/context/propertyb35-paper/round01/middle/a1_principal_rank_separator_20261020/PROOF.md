# Principal incidence rank after deleting original-edge nodes

## 1. A hereditary component-rank inequality

Let E1,...,Em be distinct five-element subsets of an n-element ground set, where n<25. Let Gamma be the simple graph on these original set indices, adjacent exactly when |Ei intersect Ej| differs from one. Choose **any** set D of h graph vertices to delete. If the connected components of the induced graph Gamma−D have sizes s1,...,sc, then

    sum_i [1+ceil(log2 s_i)] <= n.                         (1)

No coloring, Property B assumption, point-pair coverage, original degree spectrum, maximum degree or requirement m>n is needed. D is any deletion set, not a set arising from a coloring or an induced critical core. Different deletions must each satisfy their own inequality; their ranks are not added across different D.

Proof. Let A be the real m-by-n incidence matrix and let J denote the appropriate all-ones matrix. Every row sum is five, so

    B=AA^T−J_m=A(I_n−J_n/25)A^T.

Q=I_n−J_n/25 is positive definite: its eigenvalues are1 and1−n/25>0. For any subset S of the original edge indices, the principal matrix B[S,S]=A_S Q A_S^T therefore has rank exactly rank(A_S), and at most n. The graph on S is precisely the corresponding induced Gamma, because removing other original edges does not change set intersections. Off-diagonal B entries between different induced components vanish. Thus B[S,S] is block diagonal and its rank is the sum of its block ranks.

In a block with s rows and row rank d, these distinct equal-positive-weight zero-one rows have affine dimension d−1. Indeed their affine hull lies in the hyperplane coordinate-sum=5, so the origin is not in that affine hull; its linear span, the row span, has dimension one greater. Choose d−1 coordinate functionals that are independent on the translation subspace of that affine hull. Their coordinate projection is injective on the affine hull, hence sends the s distinct binary rows to s distinct binary strings of length d−1. Therefore s<=2^(d−1), equivalently d>=1+ceil(log2 s).

Apply this bound in each block of B[S,S] for S=indices outside D, and sum the block ranks. This proves (1). Empty S gives the empty sum zero. The strict condition n<25 is used only for positive definiteness and the block row-rank equality. ∎

## 2. Two especially cheap structural tests

**Isolates after deletion.** If Gamma−D has I isolated vertices, then I<=n. In particular, for original35 sets on21 points, finding22 isolated vertices after deleting any chosen graph vertices is an immediate impossibility certificate. This is a necessary realization test, not a coloring algorithm. More generally one may add the nontrivial-component terms in (1); the sum cannot exceed21.

**Independent-set / separator test.** Any independent set S in Gamma has B[S,S]=4I, hence |S|<=n. Thus every vertex cover of Gamma has size at least m−n. For35 original edges on21 points this requires vertex-cover size at least14. Any three-node vertex cover is impossible, without any search over the underlying hypergraph.

This independent-set corollary even holds without n<25: on such an S, A_S A_S^T=4I+J is positive definite and has rank |S|<=n. The narrower n<25 hypothesis is retained in (1), where it is genuinely used. The test of22 isolated surviving vertices is just an easily recognized independent set, and does not assume those vertices were isolated before deletion.

A heuristic that first tries the three highest-degree Gamma nodes as D is safe only as a **rejection** test: if it exposes22 isolates, impossibility is proved. If it does not, no separator or rank conclusion in the opposite direction follows. No claim that top-three deletion suffices for all Gamma is made.

## 3. Both saved scalar graph optimizers fail the actual realization test

The old graph from a1_rank_component_wedge_budget_20261020/VERIFY.json has76 edges and Gamma-degree histogram34^2,11^1,3^9,2^23. The five-edge-transfer graph from a1_critical_core_singleton_degree_20261020/CHECK.json also has76 edges and histogram34,29,16,3^9,2^23. In each literal numbering the three highest-degree vertices are exactly

    D={0,1,25}.

CHECK.py independently reads all explicit graph edges and verifies that every edge meets D. The remaining32 original graph indices are therefore independent; after deleting D they are32 isolated singleton components. Their principal rank lower bound is32, contradicting the available ground-set dimension21 by11.

Consequently **neither saved graph can be the non-one-intersection graph of35 distinct five-sets on21 points.** In particular the new P13002 graph does not supply an original-H counterexample or a joint Gram realization. It remains a valid feasible witness for the earlier weaker graph/core relaxation, exactly as previously stated. Its rejection by an additional real Gram constraint does not falsify either the old no-gain theorem about that relaxed domain or the literal graph arithmetic.

The25 surviving aggregate profiles are not identified with these two graph examples. Excluding the examples therefore does not reject any particular aggregate profile unless a new common majorant or complete actual argument is supplied. There is no new whole A1 or original21-point branch closure here.

## 4. Evidence and current review boundary

CHECK.py/CHECK.json save both three-node covers, their degrees, all32 outside indices, the zero uncovered-edge lists and exact rank obstruction. Actual deterministic result PASS_LITERAL_SEPARATOR_ONLY, about0.000442 CPU seconds. This is a direct reading of two graphs, not a graph/hypergraph search, Gram fitting, lock table or new negative layout.

The proof above is a complete general necessary-realization lemma. Its new mathematical scope has not received designated cross-family review. Root's separate audit of the critical-core general proof, REPORT and CHECK source is complete and root actually reran that CHECK PASS, CPU0.000361. Root has fully reread the component-wedge REPORT and read its VERIFY source; that complete VERIFY is pending actual execution as of this report. This new separator proof and two-graph CHECK await root's own read/run. No pending check is described as executed.

Reproduction from the project root:

```sh
python3 -B context/propertyb35-paper/round01/middle/a1_principal_rank_separator_20261020/CHECK.py
```

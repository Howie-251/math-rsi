# Proof obligations and exact scope

Review date: 2026-10-11. This is the fresh reviewer `/root/proof_review_transport_a6_butterfly`'s ledger, not a claim of Lean verification.

## Common definitions and assumptions

For the three n59 papers, an original legal graph is a finite simple undirected graph on 59 vertices, of maximum degree at most eight, in which every distinct pair has a path of length one or two. A vertex of degree at most seven reaches at most `1 + 7 + 7·7 = 57` vertices, so this graph is eight-regular.

- `A`: the actual symmetric 0/1 adjacency matrix, with zero diagonal.
- `J`: the all-ones matrix; `B = A² + A − 7I − J`: the actual integer defect matrix. It is symmetric, nonnegative, has zero diagonal, commutes with `A`, and has row sum six.
- `t(v)`: the number of actual triangles containing `v`; `T`: the total number of actual triangles; `Z = {v : t(v)=0}` and `N = V \ Z`.
- N15: for every `z ∈ Z`, row `B_z` has precisely two entries two and two entries one; its induced positive-support graph consists precisely of the two equal-weight edges. This is a hypothesis here, not a conclusion for arbitrary legal graphs.
- `Q₂(r) = ½∑xy B_rx A_xy B_ry`, `s_r = ∑x B_rx²`, `s = tr(B²)`, and `e_r = Q₂(r) − s_r + 5` are actual-graph quantities.
- `C₄,C₅`: numbers of unoriented simple cycles, allowing chords.

For the Brown paper, the reference graph is exactly `computations/dd82/construction/brown57.edges`. The candidate graph has the same 57 labeled old vertices plus one new vertex, maximum degree eight, and diameter at most two; all old deletions/additions are allowed. The audited branch assumes exactly nine old deletions and exactly six distinct destroyed III triangles.

## Dependency DAG

```text
Original legal graph → regularity and actual defect identities
Original legal graph + zero-row N15 → zero-heavy endpoint lemma
Actual defect identities + zero-row N15 → transport theorem
Actual defect identities + closed-walk counts → four/five trace identities
Endpoint + transport + both traces + exact butterfly triangles → three necessary templates
Transport + N15 at six private zero neighbors + one triangle at root + row22 → local contradiction
Endpoint + transport + local contradiction + four trace + exact butterfly triangles → butterfly exclusion
Brown edge list → concrete degree/triangle facts + 14 disjoint-III families
Order58 root bounds + nine deletions + a=6 + Brown facts → nine disjoint deletion blocks
Disjoint blocks + regularity → no added old edge at S → constrained original-graph domination
Independent finite check → no such S → Brown r9/a6 exclusion
```

This DAG is acyclic. The new butterfly exclusion does not invoke the three-template reduction or the fifth trace.

## Canonical claims and discharged obligations

|ID|Hypotheses and conclusion|Discharge|
|---|---|---|
|T1|For every legal n59 graph with zero-row N15, every root has the stated zero-support matching, independent-neighbor transport, and exact remainder identity.|T1.1–T1.4 below.|
|T1.1|If `x ∈ Z` and `B_rx>0`, then `∑y A_xy B_ry = B_rx`.|N15 at `x` makes the same-weight partner the sole adjacent point in its support; symmetry and `AB=BA` transport the equality. No N15 at `r` is used.|
|T1.2|Adjacent zero support points have equal weights and no other support neighbors.|Apply T1.1 at both endpoints. Nonnegative summands force equality and vanishing of every other contribution. Weights are one or two by N15 and symmetry.|
|T1.3|An isolated zero support point has an independent nonzero-support neighborhood of total weight equal to its own.|T1.1 supplies the sum; a neighboring pair would form a triangle at the zero point.|
|T1.4|`e_r = 5 + Q_N(r) − s_N(r) − K_r`, and the stated fifth-trace consequences hold.|Partition weighted edges into nonzero/nonzero, isolated-zero/nonzero, and isolated zero pairs. Their square contributions cancel exactly. The trace input is checked below.|
|T2|Under the same assumptions and exactly two triangles sharing precisely one vertex, the displayed parameters belong, up to permitted butterfly relabeling, to Templates I–III.|T2.1–T2.4. This is necessary only; it does not assert realizability.|
|T2.1|The center has nonedge pattern11; cross-pair outer defects vanish.|All center nonneighbors are zero. The endpoint lemma forbids a heavy center repeat. Any additional cross-pair common neighbor is zero and forces a center defect at least two by T1.1, contradicting that lemma.|
|T2.2|The outer zero patterns are22 or1111, with the stated `a,c,s,e`; center has `α∈{0,2}`.|N15 bounds zero weights by two. Pattern211 would leave a heavy isolated point facing a weight-one edge. T1.2–T1.4 give all displayed parameters.|
|T2.3|Commutation gives the paired `m` equations; the traces give exactly the three tables.|Nonzero terms on both sides of each relevant `BA` equality are one. The four trace forces odd `k`; the fifth trace excludes `k=3` using `∑x=α≤2`. For `k=1`, `a_a=0` forces `x_a=m_ab=0`; the remaining integer cases give I–III.|
|T2.4|Private neighborhoods have sizes4,6,6,6,6; the specified nonempty blocks are matchings.|A zero cannot meet adjacent nonzero vertices, and the vanishing cross defects exclude meeting nonadjacent ones. For an adjacent nonzero pair the common-neighbor formula gives the relevant block degree as a defect entry. The table's nonempty blocks have both relevant rows1111 (the unique22 row has no such nonempty block).|
|T3|A root on one triangle with six private zero neighbors cannot have its entire nonedge row consisting of two weight-two zero points.|Transport forces the heavy pair adjacent and disjoint from the triangle endpoints. Their three-element parent sets partition the six private points. Their induced light-defect graph is `2K₃`, whereas N15 at any private point requires its two light endpoints adjacent in the original graph. The private neighborhood is independent.|
|T4|A legal n59 graph with zero-row N15 cannot have exactly two triangles whose intersection has exactly one vertex.|T2.1 and transport exclude211 at each outer vertex; all six private neighbors are zero, so T3 excludes22. All five nonzero rows have square sum6; all54 zero rows have square sum10. Hence `s=570`; the four trace demands `8C₄=900`, impossible.|
|B1|Nine old deletions destroying six III triangles force nine disjoint blocks.|Every internal point must lose an old triangle. `a+b≤9`, `3a+b≥21`, `a=6` imply `b=3` and exact single coverage. The independently checked fourteen six-triangle families each omit an III triangle `M`; its three external-neighbor sets are disjoint, giving the three five-point blocks.|
|B2|Every order58 extension in this branch gives a constrained dominating eight-set in the stated41-point set.|The nine deleted edges form a matching, avoid `C`, and give only unit deficits. Each new neighbor uses its sole deficit, preventing any added old edge at that neighbor. Diameter two from the new vertex implies domination after deletion, hence domination before deletion. A deletion block contributes at most its adjacent pair of endpoints.|
|B3|All fourteen constrained pre-deletion domination problems are infeasible.|Independent edge-list reconstruction and Python exact enumeration:14 families,343 external cases per family, zero solutions. Submitted C++ was separately rerun and reproduced its exact1189-node total.|
|B4|No order58 extension with exactly nine deletions destroys exactly six distinct III triangles.|B1–B3. No assumption that other old edges remain fixed; no conclusion for the other r9 branches.|

## Load-bearing imported derivations checked directly

The endpoint lemma was read in full. Its root with `t(v)=2` has exactly two edges in its eight-point neighborhood. Any independent three-parent set contains an isolated point of this two-edge graph. Commutation at that point's six ordinary children proves that the point itself is zero. N15 then demands an edge between its two light endpoints, contradicting the independent parent set. The `t(v)=3` case is already excluded by its zero nonedge repeat budget. Thus the endpoint lemma supplies exactly the hypothesis required at the butterfly center.

For the four trace, the actual defect expansion gives `tr(A⁴)=126n+s−12T`. The elementary eight-regular closed-walk count gives `tr(A⁴)=120n+8C₄`: single-edge walks contribute `8n`, and walks on a two-edge path contribute `4·n·binom(8,2)=112n`. Thus `8C₄=6n+s−12T`.

The fifth-trace algebra gives `tr(A⁵)=428n+w−2s+102T`, where `w=tr(AB²)`. Every non-simple closed five-walk uses exactly one triangle; a fixed triangle contributes30 walks wholly within it and180 walks using one external excursion. Hence `tr(A⁵)=10C₅+210T`. A zero row contributes `s_r=10`, `Q₂(r)=5`; substituting yields precisely `5C₅=209·59+∑_(r∈N)e_r−54T` and its modulus-five congruence. The coefficient and sign checks therefore do not rely on a previous audit verdict.

All statements are finite and exact. There are no limit interchanges, probabilities, asymptotic constants, or uniformity qualifications to discharge.

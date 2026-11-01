# Seven distinct four-sets on at most seventeen points

## Forest deduction lemma

Let A1,…,A7 be seven distinct four-element subsets of a set Ω with |Ω|≤17. In a uniformly chosen ten-element red subset of a seventeen-element ambient set containing Ω, let Ei be the event Ai⊆red. There exists a tree T on the seven indices for which

\[
\sum_{ij\in T}\#(E_i\cap E_j)\ge636,
\tag{1}
\]

where counts refer to the C(17,10)=19448 equally likely red sets. Consequently

\[
\#\bigcup_{i=1}^7 E_i\le7\binom{13}{6}-636.
\tag{2}
\]

The sets need not cover the ambient set. No bound on the number of other events, on the degrees of the points, or on any hypergraph realization is part of this lemma.

**Proof.** Form the overlap graph L on the seven set indices, with an edge when two four-sets meet. Its components have disjoint supports. A singleton component uses four points; a component containing at least two indices uses at least five points because its sets are distinct. Thus L has at most four components.

If |Ai∩Aj|=j, the joint numerator is exactly

\[
w_j=\binom{17-(8-j)}{10-(8-j)}=\binom{9+j}{2+j}.
\]

Distinctness gives0≤j≤3, and (w0,w1,w2,w3)=(36,120,330,792). In particular even a pair in different overlap components contributes36 in the event tree.

If L has at most two components, choose a spanning tree in each component and join the components if necessary. This is one tree on all seven indices with at least five overlap edges, so its total joint count is at least5·120+36=636. In the connected case it has six overlap edges and gives the stronger720; the common636 estimate is still valid.

If L has three components, some pair of four-sets must meet in at least two points. To prove this, assume every pair meets in at most one. For a component of s indices, the first two inclusion–exclusion terms give support size at least4s−C(s,2). The only decreasing partitions of seven into three positive parts are

\[
(5,1,1),\ (4,2,1),\ (3,3,1),\ (3,2,2).
\]

Their total support lower bounds are18,21,22,23, all exceeding17. This contradiction proves the claimed pair. Keep that overlap edge and extend it to a spanning tree in its component; choose arbitrary spanning trees of the other components. Together these give four overlap edges, one having joint count at least330. Joining the three components with two further index-pairs gives one full tree, of weight at least330+3·120+2·36=762. The favorable pair and all other deductions therefore belong to the same tree.

If L has four components, their sizes must be (4,1,1,1). Indeed any other partition into four components has at least two nonsingleton components and thus uses at least5+5+4+4=18 points. The large component's support is at most17−3·4=5 and at least5. Its four distinct four-sets therefore lie on exactly five points and each pair intersects in exactly three points. A spanning tree of that component has three weight792 edges. Joining the other three components supplies three weight36 edges, for total3·792+3·36=2484.

These cases prove (1). For any tree T and any outcome, let I be the indices of occurring events. If I is nonempty, the number |I|−e(T[I]) is the positive number of components of the induced forest T[I]; if I is empty it is zero. Thus pointwise

\[
1_{\cup E_i}\le\sum_i1_{E_i}-\sum_{ij\in T}1_{E_i\cap E_j}.
\]

Taking counts and using (1) proves (2). All deductions use this single event tree; no potentially incompatible pair deductions are added. ∎

## Actual22-point A/B repair

Let H be a simple five-uniform hypergraph on22 vertices with35 edges. Define Γ on the original edges by adjacency when the intersection size differs from one. Suppose an original F has Γ-degree exactly two. Its other32 original edges meet F in singletons, except for two exceptional neighbors G,H. Let ai count singleton edges attached at i∈F; then Σai=32.

The earlier complete single-sample analysis in [the22-point report](../twentytwo_two_nonunit_direct_repair_20261020/REPORT.md) leaves five necessary types A–E if none of its strict entries applies. In A the exceptional traces on F are empty and a triple, with attachment baseline (7,7,7,5,5) and exactly one extra attachment. In B they are empty and a four-set, with baseline (7,7,7,7,3) and exactly one extra attachment. These attachment counts, rather than a count of33, are the actual32 singleton edges of the same H.

Choose v in the nonempty trace with av=7. Such a point exists: the trace contains at least three points, whereas there is only one extra attachment. Color v red and all other points of F blue. The exceptional edge meeting F is immediately proper, and the other exceptional edge is disjoint from F. On the remaining17 points choose uniformly ten red and seven blue.

The seven red-attached original edges have seven distinct external four-sets: equality of two such four-sets would make the original edges, both attached at v, identical, contrary to simplicity. Apply the lemma to these actual seven sets. The25 blue-attached edges each have bad numerator C(13,10)=286. The disjoint exceptional edge has bad numerator C(12,5)+C(12,10)=858. The fixed edge F is already proper. Hence a common-sample upper bound for a bad original edge is

\[
\frac{7\cdot1716+25\cdot286+858-636}{19448}
=\frac{19384}{19448}=\frac{2423}{2431}<1.
\]

Thus every type-A or type-B actual H is properly two-colorable. This uses no bound on Δ or δ, no point-pair coverage, and no assumption that either exceptional neighbor is a leaf of Γ.

Combining with the earlier complete351-label/19-trace-type calculation, only C,D,E remain for this22-point qΓ(F)=2 analysis. Each requires a degree11 point in F. In particular every such H with maximum degree at most10 is two-colorable, with no minimum-degree or covering condition. The unrestricted C,D,E cases are not settled here and are not claimed to be actual counterexamples.

## Deterministic receipt

[CHECK.py](CHECK.py) independently generates all partitions of seven, checks the support bounds and same-tree scalar deductions, and verifies the exact hypergeometric event counts and all ten A/B surplus placements. [CHECK.json](CHECK.json) is PASS: the common strict numerator is19384 against19448, a margin of64 outcomes. It does not enumerate free four-set families or original hypergraphs. The positive proof is the analytic component argument above. This is same-family/provisional checking; cross-family review is separately controlled by the main project.

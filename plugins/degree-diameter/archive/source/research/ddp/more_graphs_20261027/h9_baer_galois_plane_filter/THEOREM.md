# All potentially foldable Baer planes: a Galois reduction

This is a new selection lemma for the existing Baer13 mechanism. It does not rerun old graph diameter validation. PAIRING.json directly checks that every actual two-point fiber of each saved partial-fold map is exactly {p,Frob3(p)}. Singleton fibers are allowed, so this lemma also respects the split sets. The two maps have28959 and25074 such fibers; no exception occurred.

Let tau=Frob3 on Q(6,9), and let W be a3-dimensional F9-vector subspace defining a totally singular projective plane. If a13-point Baer set B inside W has at most12 distinct pi-images, there are different p,q in B with pi(p)=pi(q), hence q=tau(p).

Both p and tau(p) are in W and in tau(W). They are projectively different, so their vector span is a2-space inside W intersection tau(W).

- If W=tau(W), its unique reduced row echelon basis is also fixed by tau. Its entries therefore lie in F3. These are exactly the1120 extended totally singular planes of Q(6,3), already enumerated in the flat/nonflat batches.
- Otherwise W intersection tau(W) has dimension exactly2. It is tau-stable and thus has an F3 row echelon basis. Call its projective line L. It is one of the3640 singular lines of Q(6,3).

For any fixed L, the quadratic quotient L-perp/L is a3-dimensional nondegenerate quadratic space. Its isotropic projective points parametrize the maximal totally singular planes through L. OverF9 there are10; exactly4 are defined overF3. The remaining6 are nonstable. A nonstable W cannot contain two different F3-lines: the two lines span W, which would make W stable. Consequently these remaining planes are counted without duplication, and their number is3640*6=21840.

Thus every Baer13 set which can fold to at most12 pins lies in one of1120+21840=22960 candidate planes. This is a complete reduction among the598600 totally singular generator planes of Q(6,9). It is not an assertion about arbitrary non-Baer neighbor sets. The older364 H9 flatplanes were only part of the1120 stable case; the additional756 stable nonflat planes have been checked separately.

A further source-specific degree pruning is sound. All folding collisions of a nonstable W lie on its unique line L. L has4 fixed points and3 nonfixed tau-pairs. A raw Baer set can be degree-legal only if every collision it uses maps to an old vertex with a free degree slot. Therefore N12 needs at leastone eligible unsplit pair on L, and N11 needs at leasttwo (13 raw points must become at most11). If those counts fail, all6 planes through L may be rejected before enumerating their Baer masks. This rejects the new plane domain mathematically; it does not require old-graph BFS.

Every retained candidate still needs its full actual neighbor-set R4 check, including extras, before adding a graph vertex. The Galois reduction only selects planes and degree-feasible folded neighbor sets. Future complete graphs, if any, must be recorded separately.

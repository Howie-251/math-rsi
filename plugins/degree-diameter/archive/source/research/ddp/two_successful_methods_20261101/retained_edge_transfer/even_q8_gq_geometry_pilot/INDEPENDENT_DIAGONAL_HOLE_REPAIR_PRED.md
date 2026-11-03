# Independent diagonal-hole prediction before the single b5 diagnostic

One new selected-subset test for each accepted q8 geometry, single worker<=15CPU. No repetition of the one-copy abstract-owner enumeration. No field/projection revalidation, large source/copy graph, BFS, Lean, solver or b6 run.

Select exactly the first five literal ovoid indices I=[0,1,2,3,4] in each geometry. Derive their actual spreadowner columns sigma(I); do not assume these are columns0..4. For every off-diagonal center outside I rows and sigma(I) columns, enumerate all old pair pins in each omitted N(D_h), and count genuine source routes of length<=2 using the accepted incidence table. Predict exactly one positive old pair pin per hole, hence five distinct such pins per target.

Use the already saved projection receipts to predict this pin: projection of o_i onto S_sigma(h) gives p*, connector of o_h to its projection on S_j gives L*. Pin is(p*,L*); middle source vertex is(the projection of o_h onto S_j, connector from o_i to p*). These inherited projection records are read, not recomputed as an oldGQ test.

Freed fill f_sigma(h) should have no route<=2 to outside targets because the spread columns differ. Old D has no short route, checked by the previously accepted selected-geometry matrices. Every freed old pair/fill has its unique adjacent center in the omitted diagonal set, so it has no remaining clone neighbor and cannot provide an overlooked two-step shortcut via an existing clone.

Paper prediction for arbitrary I, not just this selected subset: each outside target has at most b direct-owner old-pin roots, and t=b+1 helpers leave at least one deficient root-target pair. Each existing clone can be assigned to one helper and covers at most t+1 such pairs; total clone pins<=t*Delta. Thus (R-b)(R-b-1)<=t(t+1)Delta is necessary. Scalars for b1..5 only should contradict it for both q8 cases. No b6 experiment or extension is authorized.

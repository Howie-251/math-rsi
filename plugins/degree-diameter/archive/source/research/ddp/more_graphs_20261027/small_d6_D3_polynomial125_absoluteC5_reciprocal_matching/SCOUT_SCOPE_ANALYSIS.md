# AbsoluteC5 plus reciprocal matching: algebraic scope check

**The declared rule is valid and executable; no uniform obstruction was found here.** This is not a D3 existence claim. No graph, matching assignment, BFS or solver was run by this review.

The coordinate change y=b−a²/2, h=c−a³−4ay is bijective, with inverse b=y+a²/2, c=h+a³+4ay. Direct substitution of the old polynomial edge yields `(a,y,h)->(a+t,−y−t²/2,−h+4ty+t³)`. The only old selfloops have t0 andv=(y,h)=0. Thus the loop-deleted source has5degree4 absolute vertices and120degree5 vertices, totaling310edges.

For v=t rep_L nonzero, tau(v)=kappa_L/t has tau(−v)=−tau(v). Hence `(a,v)->(a+tau(v),−v)` is a fixedpoint-free involution on the120nonabsolute vertices. An old edge sendingv to−v would force t²/2=0 in its y-coordinate and therefore oldt0, while the new shifttau is nonzero. New matching edges are genuine nonedges. The absolute fibre has no old internal edges, so its addedC5 is also simple. These add60+5edges:125vertices/375edges, all degree6, with every old edge retained.

Translation of a by anyr inF5 preserves the transformed source rule, the absoluteC5 and all reciprocal matching edges. It acts freely with25orbits indexed byv. Therefore all25roots(a0,v) suffice for a globalD3 check of a fixed instance; a single root does not suffice without an additional symmetry proof. Neither Cayley nor full vertex transitivity is presumed.

With canonical reps(1,m),m0..4,and(0,1), the six nonzero kappas give4^6=4096 parameter settings. This is the complete stated reciprocal family, not all C5-equivariant matchings or all preserved-edge augmentations. The previous single-matching120 bound cannot transfer: on the5absolute vertices the augmentation has degree2 and two consecutive added steps need not cancel. Likewise the old involutive-automorphism fixedroot lemma does not describe this whole augmentation.

Actual simplicity, degree and complete25-representative coverage remain the producer's obligations. This algebraic review does not establishD3, select a best failed setting, or launch another field/source/solver.

# A critical non-Property-B core supplies every singleton attachment

## General statement

Let H be a finite simple k-uniform hypergraph, k>=2, and suppose H does not have Property B. Let b be an integer such that every simple k-uniform hypergraph with at most b edges has Property B. If H has M edges, its singleton-intersection graph has an induced subgraph on at least b+1 vertices with minimum degree at least k.

More precisely, there is an inclusion-minimal non-Property-B subfamily K of H, of size at least b+1, with the following property:

> For every e in K and every v in e, there is an f in K distinct from e such that f intersects e exactly in {v}.

Consequently each original e in K has at least k distinct singleton-intersection neighbors already inside K. At most M−b−1 vertices of the singleton-intersection graph of H can have degree less than k. The graph vertices here are original edge indices; the uniformity k refers to original hypergraph vertices.

## Proof

Since H is finite and is not two-colorable, choose an inclusion-minimal non-two-colorable edge subfamily K. The assumed b-edge theorem gives |K|>=b+1. It is not assumed that H itself is edge-critical.

Fix e in K and v in e. By minimality, K without e has a proper two-coloring chi of the original finite vertex set. The edge e must be monochromatic in chi, because otherwise the same coloring would be proper for K. Call its color red.

Change only v to blue. This makes e proper. If every edge of K remained proper, it would contradict the choice of K. Thus some original f in K without e becomes monochromatic. It must contain v, since no other vertex changed; it must become all blue, since its changed vertex became blue. Every other vertex of f was therefore blue before the change, while every vertex of e was red. Hence f intersects e exactly in {v}.

Repeat this existence argument for each v in e. The chosen proper colorings may differ with v; no common-source coloring is claimed. Nevertheless the conclusion concerns the same fixed original K. Witness edges for different v must be different, because their exact intersections with e are different singleton sets. Thus e has at least k neighbors inside the singleton-intersection graph induced by K.

The full singleton graph of H can only add neighbors to these original e, so every degree-below-k vertex lies outside K. There are at most M−|K|<=M−b−1 such vertices. This proves both statements. ∎

## Actual35-edge consequence using the already proved T33

For simple five-uniform H with35 edges, the accepted theorem that every at-most33-edge simple five-uniform hypergraph is two-colorable gives b=33. If H is non-B, its singleton graph has an induced at-least34-vertex subgraph with minimum degree at least5. In particular, at most one of its35 vertices has singleton degree below5.

If Gamma joins original edges whose intersection size differs from one, and q_e is its degree, then singleton degree is34−q_e. Therefore

    #{e:q_e>29}<=1.

No pair coverage, A1 degree spectrum, balanced coloring, restriction on the vertices outside K, or preservation of the original vertex degrees by K is used. The argument does not apply an A1 theorem to K and does not claim K inherits that spectrum. It only imports the already established T33 theorem. It does not prove that H itself is colorable.

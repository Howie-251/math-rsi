# Clone pinOwner: explicit reverse-type formula for the actual16389 graph

This is a paper proof for the fixed literal source15552 and the accepted837 ordered roles. It neither compiles Lean nor reads a graph edge table, reruns atomic ranks/field laws, solves an inverse, searches a packing or changes any existing proof module. The earlier paused derivation is continued, not restarted. The current source/clone pilot remains a pilot; this note does not assert a complete original-target kernel theorem.

## Fixed constants and exact labels

Work in F=F3, V=F^4, with coordinates indexed0,1,2,3. Use the five actual global types from `../NEW_ROUTE4_TYPES_AND_TRANSITIONS.json`, bound to the original recovered960 arcs in the existing pilot-preparation receipt. These types are permuted among a controller's five outgoing arcs; the global type index must match that transition table.

The inverse-type permutation is

    q(p) = [0,3,4,1,2][p].

Write v_p for direction p and κ_p for its first nonzero coordinate. All those first coordinates are1. The small constants are:

| p | q(p) | κ_p | κ_q | (v_q)_1 | ((v_q)_1)^(-1) |
|---:|---:|---:|---:|---:|---:|
|0|0|0|0|2|2|
|1|3|0|0|1|1|
|2|4|1|0|2|2|
|3|1|0|0|2|2|
|4|2|0|1|1|1|

All five actual c_p are0. The literal coefficient tables, copied without a new matrix computation, are:

p=0
```text
B = [[0, 0, 0, 0], [1, 0, 2, 1], [2, 0, 1, 0], [0, 1, 1, 0]]
v = [1, 2, 1, 0]
c = [0, 0, 0, 0]
```

p=1
```text
B = [[0, 0, 0, 0], [0, 2, 0, 1], [2, 1, 2, 1], [0, 2, 2, 2]]
v = [1, 2, 2, 0]
c = [0, 0, 0, 0]
```

p=2
```text
B = [[2, 1, 1, 2], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 2, 1]]
v = [0, 1, 0, 1]
c = [0, 0, 0, 0]
```

p=3
```text
B = [[0, 0, 0, 0], [2, 1, 1, 2], [1, 0, 1, 1], [0, 2, 1, 2]]
v = [1, 1, 1, 1]
c = [0, 0, 0, 0]
```

p=4
```text
B = [[0, 0, 0, 0], [2, 1, 0, 2], [0, 2, 2, 1], [1, 0, 2, 0]]
v = [1, 2, 1, 2]
c = [0, 0, 0, 0]
```

The selected31 layers I and their completed five-target sets T are fixed by `../CONTROL_PACKING_RESULT.json` and `PARAMETERS.json`. All155 target-controller labels are different across the pairs(i,p). Define a total `layerOwner : Fin192 → Option(Fin31 × Fin5)` by those155 entries and None on the other37. Its sole positive correctness equation is

    layerOwner(controller(I_i,p)) = Some(i,p).

This finite table preserves self-controller entries. It is not an ordinary independent-set table and must not remove targets merely because controller(I_i,p)=I_i.

For j=27i+r,0≤r<27, the source plane coordinate is

    w = (r mod3, 0, floor(r/3) mod3, floor(r/9) mod3),
    center(j) = 81 I_i + val(w0) + 9 val(w2) + 27 val(w3),
    newlabel(j) = 15552+j.

Conversely, the center index is j=27i+val(w0)+3val(w2)+9val(w3). The local graph label offset and the27-plane index use different radix weights; they must not be interchanged. Existing production and fresh label tables agree on all837 ordered labels, inherited from the small pilot-binding preparation; no837 neighborhoods are revalidated here.

## Five literal identities, with no rank or inverse premise

For each actual type p and q=q(p), direct expansion of the displayed coefficients in F3 gives

    B_q v_p = 0,
    B_q B_p = I − v_q e_(κ_q)^T.                         (1)

Here e_k^T x=x_k, so (1) means B_q(B_p x)=x−x_(κ_q) v_q for every x. To make the exact five finite obligations explicit, their product rows are as follows; these are paper coefficient identities, not a report of a newly executed checker:

| product | rows of I − v_q e_(κ_q)^T |
|---|---|
|B0 B0|[[0,0,0,0],[1,1,0,0],[2,0,1,0],[0,0,0,1]]|
|B3 B1|[[0,0,0,0],[2,1,0,0],[2,0,1,0],[2,0,0,1]]|
|B4 B2|[[0,0,0,0],[1,1,0,0],[2,0,1,0],[1,0,0,1]]|
|B1 B3|[[0,0,0,0],[1,1,0,0],[1,0,1,0],[0,0,0,1]]|
|B2 B4|[[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,2,0,1]]|

For example, B0^2 has rows0, (1,1,0,0), (2,0,1,0), (0,0,0,1), exactly the first product; multiplying B0 by v0 gives0. Each other row follows by the same finite row expansion. Replacing p by q also supplies B_p v_q=0 and B_p B_q=I−v_p e_(κ_p)^T. No assertion that B_p itself is invertible is made or needed. No stored inverse for [B_p e0,B_p e2,B_p e3,v_p] is used: existing route-noise inverses concern different matrices and cannot be substituted.

The normalized output pivot row of B_p is0 and (v_p)_(κ_p)=1, so completed output y=B_p w+t v_p has noise t=y_(κ_p). Equation(1) moreover implies ker B_p=span(v_q): v_q is killed, and B_p x=0 forces x=x_(κ_q) v_q. Since (v_q)_1 is always nonzero, W={w:w1=0} meets that kernel only at0. Thus even the required kernel/transversal fact follows from the same explicit identities, without adding a rank hypothesis or trusting an unproved numerical receipt as a theorem premise.

## Explicit local inverse, valid on every completed output

For any y∈V define

    z = B_q y,
    s = z1 / (v_q)_1,
    R_p(y) = z − s v_q,                                 (2)
    t_p(y) = y_(κ_p).

This is an explicit formula involving only the existing five B matrices, v vectors and the scalars1/2 in the table; it does not call a4×4 inverse. Its second coordinate is0. If w∈W and y=B_p w+t v_p, then (1) gives

    z = w − w_(κ_q) v_q,
    z1 = −w_(κ_q) (v_q)_1,
    R_p(y) = w.

Thus every completed pin recovers its exact original W center, independent of t. In fact this is a full inverse on W×F: since B_p v_q=0 and B_p B_q=I−v_p e_(κ_p)^T,

    B_p R_p(y) + t_p(y) v_p = y.

Therefore the inverse coordinates for the hypothetical4×4 matrix [B_p e0,B_p e2,B_p e3,v_p] would be (R_p(y)0,R_p(y)2,R_p(y)3,t_p(y)); no new inverse constants need to be generated.

## Total pinOwner and the actual-adjacency bridge

For any original label u<15552, decode a=controllerOf(u) and y=decodeVec(fiberOf(u)). If layerOwner(a)=Some(i,p), set w=R_p(y) and

    pinOwner(u) = 27i + val(w0) + 3 val(w2) + 9 val(w3) : Fin837.

If layerOwner(a)=None, set pinOwner(u)=0. This arbitrary default is harmless: no selected center's completed outgoing pin, hence no actual selected source-neighbor pin, lies in those37 controller layers. The finite bound is27·30+2+3·2+9·2=836<837.

For every actual source adjacency Adj(u,center(j)), one must first obtain a CENTER-ORIGINATING completed representation

    u = forward(center(j),p,t).                         (3)

For the physical graph, the exact old recovery bound all77760 completed rowsets to the author source, followed by deletion of only equal global labels; source undirectedness then gives (3). This mathematical premise is the accepted actual source identity, not a claim that arbitrary affine tables are reciprocal.

For the symmetrized Lean definition of Adj, do not omit its reverse-origin disjunct. A short symbolic bridge is available from the SAME identities. If y=B_p x+t v_p, then

    B_q y + x_(κ_q) v_q = x.                            (4)

Together with the existing literal controller reverse equation

    controller(controller(a,p),q(p))=a,

(4) shows forward(forward(u,p,t),q(p),x_(κ_q))=u. The reverse noise is the indicated input coordinate; it is not generally −t. Thus a reverse-origin adjacency is also a forward-origin completed step from center(j), proving (3). The distinct-endpoint condition remains supplied by actual Adj; completed stays need not become edges.

Now (3) puts controllerOf(u) at controller(I_i,p), so layerOwner returns the correct(i,p). Formula(2) recovers exactly the original plane coordinate w of j, and radix decoding recovers j. Consequently

    Adj(u,center(j))  ⇒  pinOwner(u)=j.                  (5)

If a pin is adjacent to two selected centers j,k, applying (5) gives j=pinOwner(u)=k. Hence every real pin load is at most1. This supplies the desired load bound with a total owner formula and positive controller-table equations, rather than15552×837 negative enumeration.

## Virtualself and degree14 are not exceptions to uniqueness

The old source N is SIMPLE open N: a completed output equal to the entire old center label is removed before that N is frozen. A same-controller output with different local coordinate remains a real edge. Formula(2) may recover an owner for a removed completed stay; that is allowed because (5) is needed only for real adjacency. It does NOT authorize reinserting the old center into its clone's neighborhood.

The completed31×27×5×3 slots number12555, while the actual837 simple Ns contain12519 pins:36 centers of degree14 and801 of degree15. Those36 missing virtualself outputs are omitted, so the12519 actual pins have load≤1. The proof never assumes every clone has15 neighbors, that all155 completed target fibers are completely covered by actual pins, or that selected centers are independent. Removing completed outputs preserves injectivity; it cannot create shared real pins.

## Minimal formal interface and present status

A self-contained no-user-certificate formal implementation needs only the fixed literal definitions and proofs of:

1. The155 positive `layerOwner(controller(I_i,p))=Some(i,p)` equations, including self-controller entries; and the literal ordered837 center labels/radix identities.
2. The five B_q v_p=0 equations and five B_q B_p=I−v_q e_(κ_q)^T identities, extended from basis vectors to all x by linearity. Also the five pivot normalization equations and second-coordinate units from the displayed table. They are concrete finite identities, not imported receipt assumptions.
3. The already literal controller reverse identity, then the symbolic forward reversal(4) to discharge both branches of the actual Adj definition.
4. Field-linear simplification of R_p(B_p w+t v_p)=w for w1=0, and the base3 recovery of j. From(5), the generic FullNeighborhoodClones.load≤1 argument is immediate.

No separate kernel-rank theorem, numeric4×4 inverse, noise enumeration, complete-edge parse, all-old-root BFS, source-diameter theorem, independent-centers assumption or full source/clone FinalClaim is required for this LOAD proof. Source D4, degree and exact diameter are separate final-target obligations; the full target is not marked closed by this note. It also does not enlarge the fixed31-layer/W pool or exclude other point-level/load2 constructions.

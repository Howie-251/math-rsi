# Diamond shared endpoints sharpen the mixed trace

## Claim and assumptions

Work in the actual connected-repeat order-62 setting of
CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md. Keep its notation
D,S,W,ell,L3,C1,U1,t1,tau. Let H be the set of shared-edge endpoints
of all nongenerated unit diamonds. Distinct diamonds are disjoint.
Then

    tau + 4t1 + 2|U1\C1| + 2|H\C1|
        <= 248 - 24d + 2L3.                       (1)

In particular, if d=9 and v_extra=10, at least one of the four
nongenerated unit triangles has type zero. This does not force
v_extra=10 or a type-zero triangle for arbitrary d=9.

## 1. The exact local contribution at a shared endpoint

Take a unit diamond with shared-edge endpoints x,y and tips z,w.
The exact repeat row at x is B_x=e_y+e_z+e_w. The original graph
is triangle-free, so every positive-repeat pair is an original
nonedge: if it were an edge, B would count its common neighbors
and be zero. Thus among the three repeat neighbors y,z,w, only
the tip pair z,w can be an original edge. In the mixed-trace
notation,

    m(x)=m(y)=A_zw.                               (2)

Consequently m<=1 on H. If either diamond triangle has type one,
CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md Section6 shows that
z,w cannot be originally adjacent. In that case m(x)=m(y)=0.

Every vertex of H has ell=0 because it lies on a unit triangle.

## 2. Summation without double counting centers

The existing bound starts from

    m(w) <= 2-ell(w)+1_(ell(w)=3),    w in W.

Centers in C1 have ell=m=0, gaining two relative to this bound.
Vertices in U1\C1 have ell=0,m<=1, gaining one. These are disjoint
contributions and give the previously proved inequality

    tau + 4t1 + 2|U1\C1| <= 248 - 24d + 2L3.

For each vertex in H\C1 there is one further unit of improvement.
If it belongs to U1, its diamond has a type-one triangle, and (2)
improves its previous bound m<=1 to m=0. If it does not belong to
U1, neither diamond triangle is type one, and (2) improves its
previous bound m<=2 to m<=1. Centers have been removed, so none
is charged twice. Since tau=2 sum_(w in W) m(w), this proves (1).

## 3. The d=9, v_extra=10 boundary

By CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md, c_out=0 and the
nongenerated clusters comprise two isolated triangles and one
diamond. There are four nongenerated unit triangles on ten vertices.

Suppose all four triangles have type one. Their center graph Gamma
has four vertices and no isolated vertex, since c_out=0. Its permitted
components are K1,K2,P3,P4 after the center-cycle exclusion. Thus Gamma
is either two copies of K2 or one P4. A P4 requires two different
diamonds, by the center-graph overlap theorem, whereas only one is
present. Therefore Gamma is two copies of K2.

There are four distinct centers. All lie in the nongenerated union:
c_out=0 puts them on unit triangles, and
CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md Section3 proves that
type-one centers lie outside all generated triangles.
Hence |U1\C1|=10-4=6.

No center can be a shared-edge endpoint of the sole diamond: such a
center lies on both of its type-one triangles and would give its own
triangle degree two in Gamma. All Gamma degrees here are one.
Thus |H\C1|=2.

The strict heavy-port bound gives L3<=5 at d=9. Applying (1) yields

    tau + 16 + 12 + 4 <= 248-216+10 = 42,
    tau <= 10.                                    (3)

On the other hand, the total number of unit repeat triangles is
u=d+4=13. The sixth-cycle identity gives u congruent C5 modulo2.
The existing five-cycle range at d=9 is 2498<=C5<=2501, so its odd
values are 2499 and 2501. The actual mixed trace is
tau=10C5-24976, giving respectively 14 and 34. Both contradict (3).

Thus at least one nongenerated triangle has type zero at this
boundary.

## Scope

All component, triangle, type, and trace claims concern the actual
original graph and its derived repeat matrix. The needed connected
and D1 reductions, center-component classification, strict capacity,
and sixth-cycle identity remain paper imports. No graph realization,
d exclusion, full order62 contradiction, or Lean theorem is asserted.
New proof awaiting independent review.

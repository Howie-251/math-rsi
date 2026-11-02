# General port-line quotient: conditional interface, not a construction

This note gives sufficient coverage tests and the precise scope of a necessary
Hall obstruction. It does not instantiate360 matrices, test D0/D2 coverage,
construct a fiber graph, run a solver/BFS/Lean, or certify numerical feasibility.
The separate executed quotient-screen results are in
[general_quotient_relaxation/RESULT.json](general_quotient_relaxation/RESULT.json)
and the two sources' MINIMAL_HALL_CERTIFICATE.json files. Their numeric data
were produced by the other task; this note supplies the mathematical implication
and does not report an independent recomputation of those data.

Use K,F_s,L_p,N and the simple5-port controller from MECHANISM_PROOF.md. For
Sections1–4 retain the internal N,wN C4 edges and homogeneous semilinear darts.
Allow T_e to be an arbitrary invertible F_s-semilinear map satisfying only
T_e(L_p)=β_e L_r, β_e≠0, with the reverse dart its TRUE inverse. It need not
preserve the conic set or the nucleus line. Those omitted properties cannot be
reused from the original conic theorem.

## 1. Quotient domain and matrix lifts

Choose H_p with H_p L_p=e0=(1,0,0). A useful selected family of lifts is

    T = H_r^(-1) diag(1,Q) F_s H_p,   Q∈GL2(4), s∈{0,1}.

Then T L_p=L_r exactly. Since |GL2(4)|=180, there are360 such selected lifts for
fixed p,r. The inverse has the same form with the ports reversed and
Q_reverse=F_s(Q^(-1)); using an unrelated reverse lift is invalid.

These360 are SPLIT lifts, not all invertible port-line maps. After exact vector
normalization, the full linear part can have adapted block form

    [[1, ell], [0,Q]],       ell∈K^(1×2),

followed by F_s between H_p and H_r; there are16 shear choices, so5760 exact
vector-normalized semilinear lifts. Allowing a nonzero first diagonal entry
also allows arbitrary port scaling β. Shears and these scalars do not create
additional projective quotient permutations. This distinction matters: failure
of just the360 split lifts would not by itself exclude every general lift.

Every such map induces an invertible F_s-semilinear map
K³/K L_p → K³/K L_r. On the quotient's PG1(4), there are5 points. The four
other conic directions project to four different points: equality of two such
projections would put three conic points in one plane. The fifth point is the
projection of N, since N is in no conic secant plane. The5-point action of
PΓL2(4) is all S5, hence exactly120 quotient permutations; each has3 scalar
GL2 lifts and then the shear freedoms above. Thus testing all120 quotient
permutations is an exhaustive NECESSARY screen for every general lift, even
though no3×3 matrix has been enumerated.

Actual PG labels depend on H_p. The producer records them in
[QUOTIENT_BINDING.json](general_quotient_relaxation/QUOTIENT_BINDING.json).
The missing target PG point is the target's nucleus joker, not automatically
the same numeric column at every port. A quotient image in that joker direction
is rank-good for every possible outgoing conic port other than r.

## 2. D1 remains automatic; D0 has a real extra condition

D1: a direct dart to port r plus a target backtrack at any q≠r still gives the
four affine secant planes through L_r. The inverse cancellation is exact and
does not require T to preserve the whole conic. Direct plus≤2 target internal
steps gives the tangent span(L_r,N). Their common basepoint is T_e x, so all64
target vectors are covered in≤3. This part remains automatic.

D0: before using any neighbor internal move, all these offsets from x are
available within≤3:

    B49 = K N ∪ ⋃_p ⋃_(c∈{0,1,w}) (cN+K L_p).

For a fixed c, the five shifted conic lines meet just at cN and have16 points;
the three c-sectors are disjoint. K N contributes only the additional point
w²N, giving |B49|=49. Its exact missing set is

    M15 = {w²N+tL_p : p one of5ports, t∈K*}.

The15 vectors are distinct. They are the remaining non-nucleus offsets in the
five tangent planes through N.

For each outgoing dart e at p, putting an internal move at the neighbor and
returning adds one of the affine line sets

    T_e^(-1)(N)+K L_p,     T_e^(-1)(wN)+K L_p.

Consequently a sufficient self-layer test is that their union covers M15.
That condition is NOT automatic for a general T and is not replaced by a rank
or linear-span test. Additional closed controller words might provide more
routes; this displayed cover is only a sufficient test in the general case.

## 3. D2: actual four cosets, not just a spanning quotient vector

Fix one controller-distance2 path with darts T1,T2. Let r1 be the first incoming
port at the middle vertex, p2 the second outgoing port there, and r2 the final
reverse port. Since r1≠p2 and T2 maps K L_p2 to K L_r2,

    H=span(T2 L_r1,L_r2)

has dimension2. A two-cross route has affine base b=T2T1 x and noise plane H.
The permitted insertion of one internal step at source, middle or target gives
exactly the following sufficient shift set (repetitions are allowed):

    Z={0,N,wN,T2N,T2(wN),T2T1N,T2T1(wN)}.

The corresponding endpoints include b+H+Z. Therefore the sufficient test is

    {z+H:z∈Z} = K³/H,          four ACTUAL cosets.

This is an equality of residue sets, not a projective-direction test and not
merely the assertion that their K-linear span is the quotient. In a1-dimensional
quotient any nonzero vector spans, but the actual coefficients0,1,w may still
miss w². Frobenius factors in T2(wN) and T2T1(wN) must be retained.

This argument uses one fixed controller word, whose base b is identical for
all insertion positions. Combining masks from different words without their
different bases T_word x would not establish coverage for every source x.
No numeric D2 residue test has been executed by this note.

## 4. D3 rank sufficiency and its quotient description

For a nonbacktracking three-cross word the endpoint formula, including suffix
Frobenius reparameterization, is the same as in the conic proof. Rank is full
exactly when

    det(T2 L_r1, L_r2, L_p3) ≠0.

Equivalently, the induced quotient image of L_r1 mod L_p2 is DIFFERENT from
the quotient point L_p3 mod L_r2. This comparison is between PG1 points, so
shears along L_r2 and nonzero scalars do not alter the rank verdict.
The target nucleus joker is different from every outgoing conic port's
quotient point, hence universally rank-good for those four outgoing choices.
A single full-rank word suffices for every source x and target fiber coordinate.

The conic proof's stronger necessity “every bad word misses nonzero N” does
NOT apply: the images need not be conic secants, and a bad plane can contain N.
No assertion about a union of multiple bad words is made here.

With controller diameter≤3, the D0 cover in Section2 at every controller vertex,
the D2 residue test for at least one fixed word per distance2 pair, and a full-
rank word per distance3 pair are sufficient for graph diameter≤3. These are
conditional interfaces, not checked properties of any current72-controller.

## 5. Unique distance3 words: affine offsets and arbitrary internal edges cannot help

Here is a separate NECESSARY statement, stronger in scope than the sufficient
interface. Keep the same controller arcs and one full K-line of cross noise
per dart in K³, with invertible affine-semilinear darts

    F_e(x)=T_e x+b_e,

whose linear parts obey the port-line compatibility. Allow arbitrary additional
within-fiber edges; do not assume they contain the C4, preserve any direction,
or have a particular degree. Reverse edge relations are assumed compatible
with the undirected graph (true affine inverses are sufficient).

Suppose controller vertices u,z have distance3 and EXACTLY ONE length-three
controller path e1,e2,e3. Any graph walk of length≤3 from fiber u to fiber z
must spend all3 steps crossing controller edges, so cannot use even one
within-fiber edge. The projected three-cross word must be that unique path.
For a fixed source x all its possible endpoints are

    F3 F2 F1(x) + span(T3T2 L_r1, T3 L_r2, L_r3),

with the same independent Frobenius reparameterizations as before. Affine
offsets change only the displayed basepoint. If its noise rank is≤2, this
affine set contains at most16 of the64 target coordinates. Thus a unique
controller-distance3 path MUST have full noise rank in any diameter≤3 graph.
Arbitrarily many/internal types of within-fiber edges and arbitrary affine
offsets cannot repair this failure within the3-edge budget.

For a fixed middle controller edge, every such unique-path demand forbids one
mapping “incoming quotient point → outgoing quotient point.” The four incoming
conic quotient points must be sent injectively into the five target PG points.
They may use the one nucleus joker, but only ONE input can use it. If three
inputs have at most two allowed target points in their union, no injective
quotient map exists (Hall's necessary condition), hence no compatible general
matrix lift exists for that edge. This conclusion covers all shears, all port
scalings, both Frobenius choices, affine offsets, and arbitrary within-fiber
connections. It does not require the homogeneous all-bad-conic argument.

This is the mathematical scope of the producer's reported surviving Hall
obstructions on the two fixed Exoo72/Michel72 objects. Its actual data witnesses
are [Exoo72/MINIMAL_HALL_CERTIFICATE.json](general_quotient_relaxation/Exoo72/MINIMAL_HALL_CERTIFICATE.json)
and [Michel72/MINIMAL_HALL_CERTIFICATE.json](general_quotient_relaxation/Michel72/MINIMAL_HALL_CERTIFICATE.json).
The executed producer RESULT reports24 and36 empty middle-edge quotient domains
respectively; this note has not recomputed controller paths or those numeric
certificates. Conditional on those actual unique-path/forbidden-entry witnesses,
Section5 excludes the stated5-arc/full-F4-line/3D affine-semilinear rules on
those specific controllers. It does not exclude other controllers, changes to
the controller/cross-noise model, nonlinear fiber maps, or general degree22
D3 graphs. No graph construction or numeric feasibility result follows from
the conditional interfaces in Sections1–4.

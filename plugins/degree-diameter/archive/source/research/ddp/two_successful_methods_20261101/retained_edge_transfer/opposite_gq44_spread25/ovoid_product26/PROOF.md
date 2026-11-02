# Fixed ovoid-by-spread full-neighborhood packing

The initial geometry/packing result below concerns the frozen 7242-point graph in the parent directory. Following root release, the one 7531-point candidate was actually constructed; the final section records its immutable-pin binding, routes and finite checks. All field arithmetic, point/line IDs, spread order and the old labels 85*p+l are inherited unchanged from ../PARAMETERS.json and ../FIELD_TABLES.json. The literal source input is ../graph_d25_D3_n7242.edges.

## The explicit ovoid

Write the coordinates as (u0,u1,v0,v1) and use

    Q = u0^2 + u0*v1 + w*v1^2 + u1*(v0+v1),  w=GF4 code 2.

Direct expansion in characteristic 2 gives the polar form

    Q(X+Y)+Q(X)+Q(Y)
      = u0*v1' + u0'*v1 + u1*v0' + u1'*v0
        + u1*v1' + u1'*v1
      = Trace_GF16/GF4(u*v' + v*u') = B(X,Y).

The actual finite check tested Q(aX)=a^2 Q(X) for all 4 scalars and all 256 vectors, and polar equality for all 65536 ordered pairs of vectors.

For a direct count, put x=u0, y=v1, r=u1, s=v0+v1. Then Q=A(x,y)+r*s, where A=x^2+x*y+w*y^2. The binary form A is anisotropic: if y=0 its only zero is x=0; if y is nonzero, a zero would give (x/y)^2+(x/y)+w=0, whereas this polynomial has no GF4 root. If (x,y)=(0,0), the equation r*s=0 has six nonzero vectors (r,s). For the other 15 choices of (x,y), A is nonzero and r*s=A has three solutions. Thus Q has 6+15*3=51 nonzero zero vectors, giving 51/3=17 projective points.

No two distinct Q-zero projective points are B-collinear. Otherwise their two-dimensional GF4 span W would be totally Q-singular. The linear coordinate r on W has a nonzero kernel vector z. For this vector r=0 and Q=A(x,y)=0 force x=y=0, so z is a nonzero s-axis vector. Polar orthogonality to z forces r=0 on all of W; Q=0 then forces x=y=0 throughout W. Hence W lies in a one-dimensional s-axis, a contradiction.

Each of the 85 isotropic lines contains at most one Q-zero point. The 17 zero points each lie on five lines, giving 85 distinct incidences, so each of the 85 lines contains exactly one of them. Therefore this 17-point set O is an ovoid of the literal GQ(4,4).

The actual zero point IDs are

    1,5,8,18,19,39,41,48,50,54,56,65,67,75,76,77,78.

The finite precheck found exactly these 17 points, checked all 136 distinct pairs have B nonzero, and verified every literal line contains exactly one of them. OVOID_GEOMETRY_CHECK.json saves the point coordinates and the unique ovoid point of every line. No alternate Q, ovoid or spread was tested.

## The 289 product centers and raw partition

Let S be the fixed 17-line spread. For each (p,l) in O times S, choose the old source center c=(p,l), labeled 85*p+l. The center order is ascending ovoid point ID outer, then the unchanged spread index 0..16 inner. ORDERED_CENTERS.json lists all 289 centers in this order.

Its raw cross-incidence neighborhood before deleting a self-loop is

    R_(p,l) = {(q,m): q is on l and p is on m}.

It has 5*5=25 elements. The raw neighborhoods partition all 7225 old vertices. Indeed an arbitrary old vertex (q,m) belongs to exactly one of them: choose the unique spread line l through q and the unique ovoid point p on m. Equivalently, two distinct product centers have disjoint raw neighborhoods: different spread lines have no common point, and different ovoid points have no common incident line.

## The seventeen self/bonus substitutions

Exactly 17 chosen product centers are incident flags, one for each p and one for each spread owner. At such a center c=(p,l), its raw neighborhood contains c. In the accepted loopless 7242-point source, its actual full neighborhood is

    N(c) = (R_c minus {c}) union {7225+owner(p)}.

For every other product center the actual full neighborhood remains R_c. Since the ovoid meets each spread line once, the 17 bonus owners are all different and cover indices 0..16. Thus the actual 289 full neighborhoods remain pairwise disjoint, each still has size 25, and their union is

    (all7225oldvertices minus the17chosenflagcenters)
      union (all17bonusvertices).

The union has 7225 vertices. The 17 missing source vertices are exactly

    85,446,716,1606,1692,3382,3534,4120,4304,4633,4842,
    5571,5766,6432,6486,6609,6661.

The literal source-edge readback verified every center has the predicted full neighborhood and all substitutions agree with the actual bonus owner. It computed all 7242 vertex multiplicities: 7225 have multiplicity 1 and 17 have multiplicity 0, with maximum load 1. NEIGHBOR_MULTIPLICITY.json stores that entire array; FLAG_EXCEPTIONS.json records all 17 raw-self deletions and bonus substitutions. No source BFS or distance check was performed.

## Capacity and the conditional clone interface

With a 25-regular source and cap 26, each original source vertex can support at most one additional edge. If T clones each use a full original 25-neighborhood as their pins, then 25*T <=7242, so T<=floor(7242/25)=289. The actual packing attains this bound. It is an optimum only for this fixed-source/full-original-neighborhood extension class with source vertex load at most 1; it gives no bound on N(26,3).

If root later releases the fixed construction, attach one new clone to each actual full neighborhood above and preserve every existing edge. The source vertices covered by the packing become degree 26; the 17 missing centers remain degree 25; all 289 clones have degree 25. The predicted graph therefore has 7531 vertices, 90525+289*25=97750 edges, and degree histogram 25:306,26:7225.

The source diameter-3 property supplies the coverage interface, but no radius-3 computation was made here. For any original center c and source target t, a source walk from c to t of length at most 3 starts in N(c), so N(c) reaches t within 2 steps; the case t=c uses any neighbor. For two different centers c,d, a source walk of length at most 3 gives a route of length at most 3 between their proposed clones, after replacing its endpoints by the clones; at center-distance 1 one can instead use clone(c),d,c,clone(d). Consequently any earlier clone is also at distance at most 2 from the next pin set. The later construction must still actually check complete-current-radius-2 coverage at every step, including every earlier clone, and the degree loads.

## Initial precheck scope and cost (historical stage 1)

The one fixed precheck used 0.161736872 CPU seconds and one worker within a 20-CPU-second cap. It read the frozen geometry and full 7242 source edge table, and produced only geometry/packing data. It generated no 26-degree candidate, performed zero R3 checks, zero source BFS, zero solver calls and zero Lean calls. At this initial stage public comparison and root release were pending, and 7531 was only a conditional prediction. The later actual construction is recorded below; the initial precheck artifacts remain unchanged.


## Actual 7531 construction from immutable original source pins

After the public gate and root release, generate_once.py serialized the exact 289 original 25-neighborhoods from ORDERED_CENTERS.json into IMMUTABLE_SOURCE_PINS.json before constructing the current adjacency. It then read only this snapshot as immutable tuple pin lists. At index i, the new clone has label 7242+i and its neighbors are exactly rows[i].original_source_pins. Every pin is an original source label below 7242. No pin list was taken from a center's evolving current neighborhood. PARAMETERS.json records these label and binding rules.

This distinction matters because the centers are not independent. Index the ovoid point on spread line L_i as p_i and write c_(i,j)=(p_i,L_j). The only center-induced nontrivial edges pair c_(i,j) with c_(j,i) for i !=j; each diagonal center c_(i,i) is isolated among the centers. Thus the induced graph consists of 136 disjoint edges and 17 isolates. The one literal source-induced check confirmed exactly this structure and saved all 136 edges and 17 isolates in CENTERS_INDUCED_CHECK.json. Adjacency of centers is allowed; it does not authorize extra edges between new clones.

Each original source vertex lies in at most one immutable pin set. The source was 25 regular, so each of the 7225 covered source vertices becomes degree 26 and the 17 missing source vertices remain degree 25. All 289 new clones have degree 25. The final degree histogram is therefore 25:306, 26:7225. The final graph has 7242+289=7531 vertices and 90525+25*289=97750 edges. Every source edge is retained; all new edges join one clone to an original source vertex, and there are zero new-new edges.

For completeness the diameter routes use the actual accepted source diameter 3 and the fixed original pin lists. Old-old distances remain at most 3. Given source center c and source target t distinct from c, choose a shortest source path c,a,...,t of length at most 3. Its first vertex a belongs to the fixed pins N(c), so the clone of c reaches t within 3. If t=c, the clone reaches c in 2 through any neighbor of c. For two distinct centers c,d at source distance 2 or 3, replace the path endpoints by their clones to obtain a walk of the same length. At source distance 1, use clone(c),d,c,clone(d), of length 3. These cases cover every new-new pair, including the 136 adjacent center pairs. Hence the final diameter is at most 3. Since 7531 exceeds the cap-26 diameter-2 Moore bound 1+26+26*25=677, it is exactly 3.

The production run additionally checked before every insertion that all 25 immutable pins had degree 25 (<26) and their radius-2 union in the complete current graph covered every current vertex, including all earlier clones. All 289 checks passed for current orders 7242 through 7530, with zero uncovered vertices. EXTENSION_STEPS.json stores every exact pin list, per-step degree counts, complete-current distance histogram and earlier-clone histogram. The final step covered all 7530 current vertices and all 288 earlier clones were at pin-distance 2.

The producer verified the one final graph is simple and reciprocal, has the exact degree histogram and 97750 edges, retains all 90525 source edges, and has zero new-new edges. One ordinary final root-0 connectivity BFS reached all 7531 vertices. It ran no source BFS, no candidate all-roots BFS, no solver and no alternative field/ovoid/spread/completion variant. Production cost was 0.787637899 CPU seconds, one worker, within the 30 CPU budget. The unique complete edge table is graph_d26_D3_n7531.edges, with header 7531 97750 and lexicographically sorted unordered pairs a<b.

The [limited public comparison](../../../public_baseline_audit/DEGREE26_EXTENSION_20261101.md) gives 7514 from a published general Delorme theorem applied to the classical 7225 source and an ovoid/spread product. This is a public mathematical guarantee, not a located 7514 edge table. The 7531 candidate exceeds that guarantee by 17 vertices. Fresh independent literal acceptance and concrete Lean remain separate tasks; global-record status and priority are not certified.

# The internal C3 repeat edge has triangle-free endpoints

Assume the actual hard D1 branch and notation from `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. Let v1v2 be the unique internal unit edge of B[C3]. Then both v1 and v2 are triangle-free in the original graph.

This is a further local deduction, not an exclusion of the hard D1 branch.

The complete rows established there are

    B_vi = e_vj + e_yi + e_zi,    {i,j}={1,2},

where y1,y2 are distinct points of C2. If vi=p, its endpoint zi is a; otherwise zi is its unique B-mate in H=C1. When neither vi equals p, z1,z2 are distinct points of H. Also B[H]=0 and B[C2]=0. Every C2 point has at most one unit of B weight toward H, by the deficient H-to-C2 matching.

If some vi equals p, then B_pa=1 and a is triangle-free. The triangle-pairing theorem says that positive B entries preserve triangle status, so p and its B-neighbor vj are both triangle-free.

Now suppose neither vi is p. Assume for contradiction that v1 lies in an original triangle. Vertex v2 then lies in a triangle as well, since B_v1,v2=1. Their original edge is absent because C3 is independent. In the paired-triangle structure of the triangle-pairing theorem, v1 and v2 must therefore be each other's external mates. Their original triangle partners are exactly y1,z1 and y2,z2, respectively, since those are the two remaining entries in their complete B rows.

The mate bijection between the two triangles must match {y1,z1} with {y2,z2}. The option y1↔y2 and z1↔z2 is impossible, since B[C2]=B[H]=0. Hence it must match y1↔z2 and z1↔y2.

But y1 then has a unit B entry to z1 along its own triangle edge and a second unit B entry to its external mate z2. The two points z1,z2 are distinct members of H. This contradicts the at-most-one unit of B weight from y1 into H. The contradiction proves that v1 is triangle-free, and B_v1,v2>0 gives the same conclusion for v2.

The argument uses the actual triangle-pairing theorem and the exact established matchings. It does not infer triangle-freeness merely from a zero parent, nor assume that all points of C3 are triangle-free. No conclusion about the parity of heavy edges in the whole B component follows here.

## Corollary: the internal C4 repeat edge also has triangle-free endpoints

Let x1x2 be the unique internal unit edge of B[C4]. If an endpoint is q, it is triangle-free because B_qa=1 and a is triangle-free; the other endpoint then has the same status.

Otherwise each x_i has its unique H-repeat h_i. These h_i are distinct by the H-to-C4 matching. The internal edge and this H-repeat use two units, so there is exactly one remaining distinct unit endpoint k_i, and

    B_xi = e_xj + e_hi + e_ki.

The points x1,x2 are nonadjacent in the original graph because C4 is independent. If they were triangle-bearing, they would be paired-triangle mates, with original triangle partners {h1,k1} and {h2,k2}. A matching between h1 and h2 is impossible because B[H]=0, so the pairing must match k1 to h2 and h1 to k2. Then k1 has both the original-triangle repeat h1 and the external-mate repeat h2, two distinct positive B neighbors in H.

This is impossible globally: the entire B support from H is the union of its three deficient matchings into C2,C3,C4. Every vertex, whether inside or outside those classes, consequently has at most one positive B neighbor in H. This proves both internal-edge endpoints are triangle-free.

This corollary requires no claim that all of C4 is triangle-free, only that C4 is an independent original set because its parent 4 is triangle-free. The C4 edge's existence and unit weight were proved in `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`.

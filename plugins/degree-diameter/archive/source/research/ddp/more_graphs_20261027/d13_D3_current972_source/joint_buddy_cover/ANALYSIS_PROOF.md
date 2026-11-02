# Exact adjacent-buddy append criterion

Let H be the accepted972-vertex source with maximum degree13 and diameter at most3. Keep its induced graph unchanged. Add distinct vertices a,b, their edge a-b, and spokes from a to A subset V(H) and from b to B subset V(H), with no other new edges. Distances below are in the unchanged old graph H.

For every old target t,

    d_new(a,t)=min(1+d_H(A,t),2+d_H(B,t)),
    d_new(b,t)=min(1+d_H(B,t),2+d_H(A,t)).

Each right-hand route is available. Conversely, a shortest path can be chosen simple. If an a-to-t path visits b after first leaving a through an old vertex, replace its entire prefix from a to b by the edge a-b, which shortens it. Hence a shortest route either enters H through A and stays in H, or starts a-b and then enters H through B. It cannot later revisit a or b. These are exactly the two displayed terms. The proof for b is symmetric.

Using closed old balls, the complete new-old distance requirement for diameter at most3 is therefore exactly

    R2_H(A) union R1_H(B)=V(H),
    R2_H(B) union R1_H(A)=V(H).

Old-old distances stay at most3 because every source edge is retained; the new-new distance is1. Thus these two coverage equations, together with the degree conditions below, are sufficient for a valid974-vertex graph. No old-source all-root BFS is needed to infer its old-old distances. The old diameter premise is inherited source evidence and is not reproved here.

The source has108 degree12 free vertices and all other vertices have degree13. Each old pin can receive at most one added edge. Consequently the exact degree conditions are A and B subsets of the free set, A intersect B empty, and |A|,|B| at most12: the buddy edge consumes one of each new root's13 slots. The result is simple when the literal pin lists are distinct sets and a,b are fresh labels972,973. Its edge count is6264+1+|A|+|B|.

Equivalently, binary variables x_p,y_p obey x_p+y_p<=1 and each sum<=12. For each target t, its R2 coverers contribute to x and its R1 coverers to y, with total at least1, and the reversed constraint is also required. These are1944 exact coverage clauses over216 variables. They describe this fixed spoke-and-buddy model completely, rather than a relaxation of its distance requirement.

A bound using total row weight W and individual-ball capacities C2,C1 can only give a necessary inequality W<=12(C2+C1). Satisfying such a scalar capacity bound does not imply either coverage equation or predict a successful graph. The earlier single-point15-pin certificate cannot by itself exclude this buddy model, which has genuinely different R2/R1 routes.

This file proves the conditional model equivalence only. No source BFS, parameter search, candidate graph or numerical diameter result was produced for it. A positive producer output still requires literal degree, retained-edge and two-new-root verification as assigned by the parent.

Producer disposition: the authorized finite solver run ended UNKNOWN at its original time limit, with no incumbent. Its LP total22.26556668 is below the24-pin combined budget and does not prove integer feasibility. No candidate or new-root BFS followed; this exact buddy family remains open. The theorem above is a model-equivalence result, not an exclusion.

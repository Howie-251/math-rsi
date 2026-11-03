# Conditional twin/line replacement theorem and actual empty scope

The actual structural selector found zero qualifying ordered twins among the164 current twin vertices. STRUCTURAL_BINDING.json is the inherited evidence: CPU0.016929184, no BFS and no cutgraph cache. PREDICTION.json was frozen by the producer before this scan. No deleted-vertex instance or pin allocation was created here. The201 inserted vertices and all earlier absorption/switch scopes were not scanned or reopened.

The following is a conditional theorem, not a claim that the current graph has such a square. Let v=T0,T1,L0,L1 be distinct; require T0T1 and L0L1 edges, and exact equalities

    N(T0)\{T1}=N(L0)\{L1}=P0,
    N(T1)\{T0}=N(L1)\{L0}=P1.

Then deleting T0 preserves the distance of every remaining pair whose endpoints are both different from T1. For any shortest path through T0 with both adjacent vertices in P0, replace p-T0-q by p-L0-q. If the path uses T0T1, T1 is internal because it is not an endpoint. Its other neighbor lies in P1, so replace p-T0-T1-q by p-L0-L1-q. Both substitutions have the same length and avoid T0. Repeated vertices in the substituted walk only allow shortening. Thus a diameter4 source retains diameter4 for all old pairs except possibly those with endpoint T1. In a proposed final split graph, one T1-root coverage check would complete this old-old obligation; T1 need not already cover the deletion graph before the new vertices are added.

For a valid instance let H=G-v, new a,b adjacent, old-neighbor sets A,B. The exact new-root conditions are R3_H(A) union R2_H(B)=V(H) and the reverse. A shortest a-to-old path that uses b can use a-b immediately, so no later new-root excursion is omitted by these formulas.

If the full eligible pin pool P has18 vertices, each with exactly one available slot, a feasible solution may be extended monotonically to A disjoint-union B=P. The maxdegree11 bound gives |A|,|B|<=10 and hence8<=|A|<=10. For each old target t define U_t=R2_H(t) intersect P and T_t=R3_H(t) intersect P. If U_t is nonempty, the pin it contains is assigned to one root and automatically reaches both roots within4. If U_t is empty, each root needs its own color in T_t, because the buddy route through a distance3 pin has length5. Hence the exact two-root condition becomes a balanced nonmonochromatic coloring of those T_t. A singleton is impossible, and size-two clauses impose opposite colors, so an odd cycle of such clauses is an obstruction. A pin with two available slots can instead be used by both roots; the cap1 reduction must not be applied to it.

These facts give a specific, potentially cheap route certificate, but their intended current full-square class is empty. No support matrix, coloring search, candidate graph, BFS or new diameter result was produced. This does not exclude other delete-v/add-adjacent-two cooperative constructions.

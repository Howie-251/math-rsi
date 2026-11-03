> Actual terminal: `OLD_RESULT.json` reports max-hit bounds11/7/12 against32/21/32 obligations; no OR or representative-pair check was needed. See `FINAL_PROOF.md` for the complete NO and the paper-only extension to arbitrary at-most-three cuts/pin subsets. The prepared twelve-representative gate below remains the historical general proof.

# Exact two-edge gate for the old critical-pair obligations

This is a paper review of one necessary-condition gate in the fixed331387-source three-cut/six-star problem. It evaluates no vertex mask, source edge, edge class, critical pair or candidate. It performs no field/DP/BFS, solver, graph or Lean run. The actual RIGHT Cayley source, three positive generator representatives and critical-pair count certificate are inherited from the source/profile interfaces.

## Obligations for a fixed first edge

Fix one canonical source cut e0={e,s}, where s is one of the three positive generators. Let K_s be the saved set of certified critical pairs(u,v): d(u,e)=4, d(s,v)=4, d(u,v)=9 and the exact shortest-count factorization says every source9-geodesic uses e0. The earlier paper proves that, after deleting e0 and two other disjoint edges and adding a six-star, this pair is within9 exactly when at least one of the other four pins lies in

B3_G(u) union B3_G(v).

The baseline pins e,s supply distance4 to both ends, and the remaining pin must improve one side to≤3. Deleted internal-pin edges do not change distance from the full pin set. Thus the criterion is exact for each certified pair. The obligation list need only consist of true critical pairs for a negative gate to be valid; it is not assumed to enumerate every old source-distance-nine bottleneck.

For each old vertex x, define its K_s-bit mask V_s(x) by setting a pair's bit exactly when x is in that pair's displayed radius-three union. For another old edge f={a,b}, put M_s(f)=V_s(a) OR V_s(b). Then two other cuts f,g jointly repair all K_s obligations exactly when

M_s(f) OR M_s(g)=ALL_s.

The two edges must also be mutually vertex-disjoint and avoid both endpoints of e0. This is a mask condition for an old-route obligation, not a full diameter test.

## Correct candidate pool and grouping order

First form E_s: all actual old edges having neither endpoint in e0. **Filter these first-edge conflicts before computing class counts or truncating representatives.** For each bitmask m, let E_s(m) be the edges of E_s with that exact mask. Count all members and keep the first min(12,count) distinct undirected edge representatives. A class of size≤11 is fully retained; size≥12 is marked large.

If the full source were grouped first and only the stored representatives were later filtered against e0, twelve would not give the proof below: the representatives could be consumed by conflicts with the first edge before avoiding the second edge. The grouping after the fixed-edge filter is part of the exact domain, not an optional implementation optimization.

Retain mask zero. An edge with full obligation mask may need a disjoint zero-mask edge to provide the other two required pins; discarding zero could produce a false NO. Allow a class to pair with itself. Two different edges of the same mask may jointly cover ALL and be disjoint. Identical edges are not a valid pair and are automatically rejected by the endpoint-disjointness test.

## Why twelve representatives suffice

The old graph is simple and maximum degree6. For any fixed eligible edge f={a,b}, the number of old edges sharing an endpoint with f is at most

deg(a)+deg(b)-1≤11.

The subtraction counts f itself only once. The same bound holds in the filtered pool, since deleting pool edges cannot increase degree. Therefore, from any class with twelve distinct eligible edge representatives, at least one is vertex-disjoint from any fixed eligible edge f.

For every unordered pair of nonempty mask classes m,n with m OR n=ALL, decide as follows:

- Both classes small: all of their edges are stored; checking every representative pair for disjointness is exactly the full question. For m=n check distinct representatives, with the same endpoint test.
- One class large: choose any stored edge from the other class. Among the large class's twelve stored edges there is a disjoint one by the11-conflict bound. This gives an actual witness, not merely a counting possibility.
- Both classes large: the same argument applies. It also applies if m=n: select one stored edge f, and the twelve representatives of that very class contain an edge disjoint from f; f itself is among the at most eleven forbidden edges.

Consequently the counted classes plus these bounded representative sets decide **exactly** whether two eligible, mutually disjoint old edges cover all obligations. Equivalently, checking all stored representative pairs for every covering mask pair is complete: small classes are exhaustive and any pair involving a large class has a representative witness. Counts are required to distinguish genuinely small classes from truncated large ones. Representatives must be distinct undirected old edges; repeated orientations do not count as twelve.

## Complete source-edge and first-type domain

The actual six generators form three distinct inverse pairs, with no involution among them. Scanning(h,h*s) for every source vertex h and each of the three chosen positive representatives therefore covers every undirected source edge exactly once. If an edge is initially written using s^(-1), reorient it from h*s^(-1) to h to obtain a positive representative. This is the actual source recipe, not a replacement field or abstract edge-class guess.

For any first cut{h,h*s}, left multiplication by h^(-1) maps it to{e,s}. Left multiplication is an automorphism of the working RIGHT Cayley graph. It maps all other cuts, the six pins, source critical-pair obligations and the star modification consistently; the new star vertex is fixed as the added role. It preserves disjointness, masks interpreted geometrically and candidate distances.

Suppose all three canonical first-type gates return NO. Any hypothetical successful three-cut/six-star candidate has some first cut. Reorient and left-translate it to one canonical type. Its two remaining cuts are edges in E_s and are mutually disjoint. Every K_s critical pair must be repaired by their four endpoints, so their masks must OR to ALL_s. The complete two-edge gate says that no such pair exists, a contradiction.

Thus complete NO for the three canonical gates strictly excludes **all three-disjoint-cut/six-star modifications of this fixed source**, without needing a newroot test or a full seam verifier. It does not exclude other old-edge edits, another source or general(6,9). A NO for only some first types excludes triples containing those types; it is not the complete family conclusion.

## Positive-gate and representative boundaries

A covering edge pair is only a necessary old-route witness. It does not prove that the new star reaches every old vertex within9, that the obligations of the other two cuts are repaired, or that every remaining old source-distance-nine pair is safe. A separately authorized first-triple check may evaluate those conditions and ultimately use the complete seam interface.

The twelve-representative reduction is exact only for the mask-cover-plus-disjointness question above. It is **not** a representative theorem for newroot missing-set intersection, other-cut obligations or full candidate diameter. Distinct edges in the same mask class can have different translated missing sets and different effects on other old routes. In particular, failures of those twelve stored realizations must not be used to exclude every real realization of that mask pair. The case must retain this distinction if a necessary gate passes.

No numeric result is asserted by this note. The finite owner must report the complete mask-class gate scope, keep the zero class, filter first-cut incidence before truncating, include same-class pairs, and state whether all three first types were actually exhausted. This paper changes no graph/parameter/Lean or method count.

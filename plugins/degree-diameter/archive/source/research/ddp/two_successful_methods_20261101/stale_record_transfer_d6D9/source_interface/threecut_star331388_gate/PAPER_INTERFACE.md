# Three old cuts and one six-star: exact missing-set and geodesic interfaces

This is a paper review of the actual Rodriguez–Canale source. It runs no source/field validation, distance or count DP, BFS, endpoint-pair enumeration, shift search, graph generation, solver or Lean. The required full missing sets and shortest-count arrays are not presently cached. `HISTORY_SOURCE_GATE.json` gives the actual read-only source/provenance and the precise old-scope boundaries.

## Actual source and multiplication convention

The inherited source has331387 vertices,994161 edges, is6-regular and has diameter9. The primary entry credits Alexis Rodriguez and Eduardo Canale, communication2012-08-20, at `desc_g9.html#69`. The cached author C is `research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c`. No full raw adjacency is locally required by this interface.

Work in the already adopted RIGHT Cayley model on C49 semidirect F6763, with

(j,n)*(a,c) = (j+a mod49, n*41^a+c mod6763),
label(j,n)=6763*j+n,
(j,n)^(-1)=(-j mod49,-n*41^(-j) mod6763).

An edge is h—h*s. The inherited six inverse-closed generators are

```text
(25,1254), (24,2125),
(18, 541), (31,3289),
(47,4642), ( 2,1300).
```

Use the first member of each listed pair as a positive edge representative. The original author C uses left-Cayley edges; the existing interface relates it to this right model by inversion. That is an inherited isomorphism, not permission to interchange left and right products in a new endpoint formula.

Left multiplication L_h:g↦h*g is an automorphism of this right Cayley graph. Explicitly, for h=(k,t), L_h(j,n)=(k+j,t*41^j+n) in the indicated modular coordinates. This is different from right multiplication g*h. No arbitrary right translation is assumed to preserve the generator set.

## Intended edit and degree account

Delete three pairwise vertex-disjoint actual old edges e_i={h_i,h_i*s_i}, and let P be their six endpoints. Add a new vertex z adjacent once to each pin in P. All six old endpoints lose and regain one edge; all other old degrees stay6 and z has degree6. The intended candidate would have331388 vertices and994161-3+6=994164 edges. This paper produces no such candidate and claims no new result.

Put F={e_1,e_2,e_3} and H=G−F. These symbols denote this deleted-edge host, not the group.

## Deleted internal pin edges do not affect distance from the pin set

For every old v,

d_H(P,v)=d_G(P,v).

Removal can only increase distance. Conversely choose a shortest G-path from the entire source set P to v. If it traversed any deleted edge, the endpoint immediately after that edge would again belong to P, and its suffix to v would be a strictly shorter path starting in P. That contradicts nearest-source minimality. Thus a shortest P-to-v route avoids all F and exists in H. The argument uses every deleted edge having both endpoints in P; it is not true for arbitrary unrelated deleted edges and an arbitrary chosen source set.

Any shortest z-to-old route uses z only at its start, so

d_new(z,v)=1+d_H(P,v)=1+d_G(P,v).

For each positive representative s define the endpoint-pair radius-eight missing set

M_s={v : d_G({e,s},v)>8}.

It is the same set if the representative edge{e,s} is removed first, by the same two-pin lemma. For a translated cut{h,h*s}, its missing set is exactly L_h(M_s). A negative-generator edge may be reoriented from its other endpoint to use the corresponding positive representative. Therefore

newroot z has radius≤9  iff  intersection_i L_{h_i}(M_{s_i}) is empty.

This is **necessary and sufficient**, not merely a necessary gate weakened by deleting the other two cut edges. The six-pin distance lemma removes that supposed extra deletion concern. Missing counts, histograms or first missing labels do not determine the intersection; actual full sets are required. The previous single-subdivision runs saved only counts14088/13875/14028 and first labels20/6/20, not the required full sets. They do not settle this three-cut rule.

## Exact old-pair distance formula

For any old u,v,

d_new(u,v)=min(d_H(u,v), d_H(u,P)+2+d_H(v,P))
             =min(d_H(u,v), d_G(u,P)+2+d_G(v,P)).

A shortest route either avoids z and lies in H, or visits z once and uses two star edges. Conversely nearest-pin routes and those two edges give a walk of the displayed length; if that walk repeats a vertex, removing the repetition only improves the upper bound. The matching-cut distance lemma justifies the second equality.

Thus a successful newroot gate does not automatically preserve diameter9 for old pairs. Source diameter9 does give every candidate diameter≤10. For an old shortest path using one cut, replace that edge by its two star edges, increasing length by1. If it uses two or more cuts, replace the whole subpath from the first cut's entering pin to the last cut's exiting pin by two star edges. Disjoint cuts make that old segment at least three edges long, so the replacement shortens it. New-to-old distances are≤10 from the source diameter bound.

In particular every old pair with source distance≤8 is safe within9. A source-distance9 pair is also safe if any one of its geodesics avoids F or uses at least two cut edges. Remaining potential old damage concerns source-distance9 geodesics cut in a more concentrated fashion. The single-edge critical test below supplies exact obligations for a useful subset; it does not classify all possible distributed multi-edge geodesic bottlenecks.

## Exact oriented critical-edge count from one identity table

Define d(g)=d_G(e,g) and let c(g) be the integer number of shortest right-generator words from e to g. The word count must be for the actual F6763 endpoint, not the old49-phase nonbacktracking-prefix count and not an image table for F6959. Left translation gives

d_G(u,v)=d(u^(-1)*v),
number of geodesics u→v = c(u^(-1)*v).

Fix a positive source edge e—s. Consider old endpoints satisfying

d_G(u,e)=4,  d_G(s,v)=4,  d_G(u,v)=9.

Equivalently these are d(u^(-1))=4, d(s^(-1)*v)=4 and d(u^(-1)*v)=9. The equality d(u^(-1))=d(u) may be used because the graph is undirected, but retaining the oriented product avoids convention errors.

The triangle inequality forces

d_G(u,s)=5,  d_G(e,v)=5:

both are at most5 through the displayed edge, and any smaller value would give a u→v route of length≤8. Consequently no9-geodesic can traverse the cut in the reverse direction s→e, since doing so would require at least5+1+5=11 steps.

Every shortest u→e prefix and shortest s→v suffix concatenated with e→s gives a length9 walk. Because d_G(u,v)=9, it is a geodesic; an overlapping/backtracking concatenation would otherwise shorten it, contradicting that distance. Conversely every geodesic through e→s splits uniquely into such a prefix and suffix. Hence the exact number of source9-geodesics using the undirected cut is

c(u^(-1)) * c(s^(-1)*v).

There is no missing reverse-orientation term under these4+1+4 hypotheses. Thus

c(u^(-1)*v)=c(u^(-1))*c(s^(-1)*v)

holds **if and only if all** source9-geodesics between this u,v use the cut e—s. The product is a count of actual shortest paths, not a product of unconditioned/nonbacktracking word totals. Prefix/suffix factors and total must all be computed exactly in the same source convention.

For a translated cut h—h*s the corresponding formula is

c(u^(-1)*v)=c(u^(-1)*h)*c((h*s)^(-1)*v),

with d_G(u,h)=d_G(h*s,v)=4 and d_G(u,v)=9. Note (h*s)^(-1)=s^(-1)*h^(-1); replacing these left-translation products by v*s^(-1) or v*u^(-1) is not justified.

## Turning a critical pair into a four-pin obligation

If the count equality certifies a4+1+4 pair for one selected cut, deleting that edge already destroys every old route of length≤9 between u,v; deleting two more edges cannot restore one. Therefore in the intended edited graph this pair is within9 exactly when the star route satisfies

d_G(u,P)+d_G(v,P)≤7.

The first cut's two pins supply minimum distance4 to each endpoint: the other cross distances are5. Let P' be the four endpoints of the other two cuts. Then the displayed condition is equivalent to

P' intersects (B3_G(u) union B3_G(v)).

Indeed without such an intersection both nearest-pin distances are4 and their sum8 fails; if a remaining pin is within3 of either endpoint, that side has distance≤3 and the other still has its original pin at distance4, giving sum≤7. This is an exact repair criterion **for this certified pair**, and consequently a necessary condition for any full diameter-nine construction. It provides a route obligation for choosing the two other old edges, rather than a scalar score to optimize blindly.

Passing all obligations obtained from this4+1+4 single-cut certificate is not asserted sufficient for all old pairs. Source9-pair geodesics may distribute across multiple cuts without one edge common to all of them. Those cases need their own treatment or final actual validation. The newroot missing-set complement and old critical-pair repair conditions must be satisfied simultaneously; neither replaces the other.

## Current boundary and stop

No full source identity distance/count table or full representative M_s sets were located in the inherited materials. This paper does not create them. The only current result is the exact interface and its multiplication/orientation proof. A later separately authorized data task can export the needed missing sets and exact shortest counts once for this new mechanism; it must not label old49-phase raw counts as source geodesics or silently repeat old source-validity work.

Old single-edge-subdivision NO and the different F6959 generator-family NO remain inherited without replay and do not exclude this fixed-F6763 three-cut/six-star rule. No candidate, graph/parameter/Lean increment, field ladder, new source or automatic triple search follows from this note.


## Later exact-verifier interface

The original absence-of-data paragraph above describes the initial read gate. `PROFILE_DATA_SCHEMA.json` now records separately produced support/count inputs for this new mechanism. `PAPER_SEAM_VERIFIER.md` extends the4+1+4 necessary subset to a complete old-pair seam criterion for one fixed candidate, with both cut orientations and an explicit exact-D9 witness requirement. This paper task does not read the binary arrays or run that criterion.

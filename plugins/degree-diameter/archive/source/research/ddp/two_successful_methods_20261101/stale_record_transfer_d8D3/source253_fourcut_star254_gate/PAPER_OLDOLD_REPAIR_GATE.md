> Actual final closure: `COUPLED_RESULT.json` exhausts all repair/half choices and bounds base by12 in each first type; adding the two full-cut bounds gives24<27. See `FINAL_PROOF.md` for the complete repair-rule NO and the paper-only at-most-five pure-deletion/star corollary. The independent35-capacity OPEN checkpoint and conditional prototype discussion below are retained as history.

# Five matching cuts, one old–old repair and an eight-star: necessary capacity gate

This paper uses the inherited CM253 source and the actual cached-witness four-cut gate. It does not repeat source/field/unique3 validation, parse the full source, compute a distance, enumerate cuts or repairs, generate a graph, run BFS or invoke a solver. The new repair-capacity numeric result is read as a separate bounded upper-bound gate, not as a candidate graph or family exclusion.

## Degree account and the genuine new rule

Start with the8-regular253/1012 source. Delete five vertex-disjoint source edges, releasing one slot at each of ten old endpoints. Add one genuinely new old–old nonedge R={a,b}, and a new vertex z of degree8. At maximum degree8, a and b must be released endpoints and cannot also be star pins; every untouched source vertex is still saturated. The eight other endpoints form P, the star neighborhood. Every released slot is used once, giving254vertices/1016edges, all8-regular:1012−5+1+8=1016.

If a and b were the endpoints of one deleted edge, adding R would merely restore it; the remaining four matching cuts and the eight-star are exactly the already excluded four-cut graph. Thus a genuinely new repair joins endpoints of two different cut edges. Those two cuts are half-cuts: each has one repair endpoint and one star pin. The other three cuts are full-cuts with both endpoints in P.

Choose any full-cut as canonical first edge e–s. Such a cut always exists. Left translation and positive inverse-class orientation use the same actual RIGHT recipe and four classes as in `PAPER_WITNESS_GATE.md`. Of the six other star pins, four come from the two remaining full-cut edges and two are the isolated star endpoints of the half-cuts.

A source edge already retained in G−F cannot be newly added as an old–old repair in a simple graph. Treating that retained edge as an extra addition would leave a,b at degree7 and would not produce the claimed all8-regular edge count. It is not literally the same as restoring one deleted edge. Only the restoration case above reduces exactly to four cuts. The numerical repair domain correctly restricts R to original-source nonedges.

## No short old-pair path can mix the two new mechanisms

Consider a simple path of length≤3 between two old vertices. If it visits z, it uses two consecutive star edges p–z–q. To also use R within at most three total edges, the sole remaining edge would be R immediately before or after that segment, making one endpoint of R equal to p or q. This contradicts {a,b} disjoint from P. R cannot be the middle edge at z because both its endpoints are old vertices.

Therefore an old–old route of length≤3 either uses the star or uses R, never both. If it uses neither, it is a route in G−F. Each cached unique3 witness for the first cut has no such route, because its unique old≤3 path used e–s and that edge is deleted. Hence every witness must be repaired by **star OR repair-only**. No third mixed short-path family is omitted. This conclusion depends materially on the repair endpoints not being star pins; a model with overlapping roles would require a different route classification.

## Star masks are safe upper bounds, not the old exact distance identity

There is a new subtlety: the two half-cuts have one endpoint outside P. Thus the old identity d_(G−F)(P,v)=d_G(P,v), used for a full-endpoint pure star, is not available in general here. A half-cut may break the one old leg from a witness endpoint to a star pin. This must not be inherited as an equality in a positive verifier.

Nevertheless every actual star route is also a source-old-leg star route if future cuts are ignored. The previous positional hit masks therefore remain **necessary upper bounds**:

- a middle witness u–e–s–v can be star-repaired only if u or v is another star pin;
- a first witness e–s–x–v can be star-repaired only if another star pin belongs to the closed source ball B1(v);
- a last witness is dual.

The first pins e,s hit no witness bits. Let mEdge be the inherited maximum hit by an eligible other source edge and mVertex the maximum hit by one allowed old vertex, or a larger superset domain. Two other full cuts and two half-cut single pins can cover at most

2*mEdge + 2*mVertex

obligation bits. Overlap can only reduce the actual union. The bound deliberately ignores whether maximizing vertices can be the half-cut endpoints simultaneously, whether repair endpoints are excluded, and whether the full cuts are mutually disjoint. These relaxations are valid for a negative upper-bound gate.

## Repair-only mask

Put G0=G−{e–s}, ignoring the other four future cuts. For each candidate original-source nonedge R={a,b} disjoint from e,s, define its repair mask by all source-old-leg routes

u —(G0, at most i steps)— a —R— b —(G0, at most j steps)— v,

and the reversed orientation, with i,j≥0 and i+j≤2. These are exactly the length≤3 routes using R in this relaxed graph, after deleting redundant loops if necessary. In the actual graph, a simple repair-only route uses R once and both remaining legs lie in G−F⊆G0. Thus the relaxed mask contains every actual repair-only witness.

This does not assert that a maximal relaxed path survives the other four cuts or that a,b can be freed by compatible half-cut edges. The domain is an upper bound. Both orientations and all0/1/2 old-leg splits must be included. No source distance/field recomputation is needed to justify this classification.

For a fixed R, every necessary cached obligation lies in its relaxed repair mask or in the star mask. A sufficient capacity-only NO would be

2*mEdge+2*mVertex+max_R(popcount(repairmask(R))) < number_of_obligations

for every canonical first type. Maximizing the terms separately only weakens this obstruction and can never turn a true possibility into a false negative. If the inequality fails, even by a large margin, it is not a positive graph or a proof that compatible cuts/pins exist.

## Actual bounded gate outcome

The numeric owner's `REPAIR_RESULT.json` reports for each of the four classes27 inherited obligations, mEdge=6 and mVertex=6. The star bound is24. It evaluates the original-source nonedges avoiding the two first pins and finds maximal relaxed repair hit11; the recorded positional split is3 first,5 middle and3 last. The resulting capacity bound is35, which is not less than27.

Accordingly the proposed capacity-alone exclusion is **not supported**, and the genuine five-cut/one-nonedge-repair/eight-star family remains open. The stored repair-only paths demonstrate that old–old repair can bypass some unique source paths that a pure star could not repair; they do not demonstrate one compatible five-cut candidate. No five-cut enumeration, candidate graph, BFS or solver was performed. The actual cumulative terminal is1.868182278/10CPU seconds, preserving the earlier four-cut gate. This paper does not re-evaluate any of those masks.

## Paper-only corollary: every pure star with at most four deletions is excluded

The earlier actual four-cut witness gate has27 obligations per canonical first class and maximum6 over every source edge disjoint from its two endpoints. All mixed-position witness masks have V(e)=V(s)=0. For any source vertex x outside that first pair,8-regular simplicity gives at least six incident edges{x,y} with y also outside the pair. Each is eligible and has mask V(x) OR V(y) containing V(x). Hence V(x) has at most6 hits. The same is trivial for the zero-mask first pins.

An excluded source edge touching one first pin has mask V(x), or is the zero-mask first edge itself. Thus the maximum over **all** source edges is also at most6, without another scan. This is a dominance consequence of the actual eligible bound, not a newly measured maximum.

Now delete any nonempty set F of at most four distinct source edges, allowing shared endpoints, and let Q be all their endpoints. The full star on Q is degree-legal: |Q|≤8, every old endpoint has degree8−deg_F+1≤8, and all others remain8. Choose a first edge and translate to its canonical class. The other at most three edges hit at most18 of its27 witness obligations, leaving a witness unhit by all Q. Since all deleted edges are internal to Q, the nearest-source distance identity does apply to this pure-star graph. The original unique3 path is destroyed, while the star cannot repair its unhit pair within3. Hence the full-star graph is not diameter≤3.

Any smaller new neighborhood N⊆Q is a subgraph of that degree-legal full star and cannot shorten the failed distance. With only old-edge deletions, a new neighbor must be an endpoint of a deleted edge anyway because every untouched source vertex remains saturated at8. The no-deletion case cannot connect the new point. Thus no one-point pure-deletion/star augmentation with at most four deleted old edges works, even allowing shared cut endpoints and a nonregular final degree distribution.

This corollary contains no added old–old repair edges. If R simply restores one deleted cut, the effective four-cut pure-star case is covered. If R is already a retained source edge, it creates no new repair-only route for a unique witness in G0; such a redundant-edge operation cannot be credited as a new repair. In the intended five-matching-cut role split, its star capacity is at most24<27 as above, so treating the duplicate as an actual simple addition does not create a counterexample either.

## Scope and stop

The proved pure-star NO and the open five-cut genuine-repair domain must stay separate. The former does not exclude new old–old edges. The latter permits a mechanism absent from the original source and has only passed a relaxed capacity obstruction; no candidate is known from this gate. Allowing nonmatching cuts with repair/star roles overlapping, more repairs, other sources or general one-point rewiring is not classified here. No such alternative is automatically launched. This is the same CM253 problem and changes no graph/parameter/Lean or independent-method count.


## Subsequent coupled-halfcut gate and one fixed-repair prototype

The next separately authorized task couples R with its half-cut star endpoints; this paper still runs no values or candidates. Write R={a,b}, a source nonedge disjoint from the canonical first full-cut endpoints e,s. Choose a' in N_G(a) and b' in N_G(b). The six vertices{e,s,a,b,a',b'} must all be distinct. The first cut e–s and half-cuts a–a',b–b' are then vertex-disjoint. Two remaining full-cut edges must avoid all six occupied vertices and each other. The final pin set is{e,s,a',b'} plus their four endpoints, with exactly eight distinct pins and neither repair endpoint. This creates precisely three full cuts and two half-cuts, not an additional uncounted cut or an overlapping-role graph.

For each legal half choice, define base=relaxedRepairMask(R) OR V(a') OR V(b'). The remaining two full cuts each have at most the inherited6 hits, since their domain is a subset of the old997 edges already disjoint from the first cut. Hence their union can add at most12 bits. A strict maxBase+12<27 for **all** original nonedge repairs, all legal half choices and all four canonical first types would be a complete necessary-condition NO for this rule. No disjointness or role-compatibility constraint may be silently dropped when reporting that full domain. Using larger relaxed masks only weakens a negative bound, so remains safe.

If that global bound does not exclude the family, freezing one globally best repair tuple(firsttype,a,b), with the stipulated deterministic tie-break, is a prototype selection, not a complete repair search. For that fixed R there are at most8*8 half choices before the six-vertex distinctness filter. It is legitimate to inspect those choices without reselecting R, but their outcome must remain scoped to the frozen repair.

For a fixed half choice the exact **cached-obligation** completion condition is

base OR M(f) OR M(g)=ALL27,

where f,g are actual source edges disjoint from the six occupied vertices and mutually disjoint. A membership/superset join can decide this condition exactly. The old997-edge pool is only an initial superset: it must additionally exclude edges touching a,b,a',b'. If a mask query returns several edges and the first intersects f, the others cannot be discarded without checking or an exact incompatibility filter. Self-pairing the same edge is also disallowed by endpoint disjointness.

The number12 in the capacity bound is **coverage6+6**, not a transferable representative-count theorem. If one elected to truncate edge classes instead of keeping the complete997 pool, the earlier degree-six12-representative argument would not apply: here an eligible fixed edge can intersect up to15 old edges in a simple degree-eight graph. Sixteen distinct representatives after filtering all six occupied vertices would suffice for that disjointness lemma. No truncation is needed for an exact join of the actual small edge pool.

Passing this cached mask join is still not a diameter certificate. The witness list is incomplete, the star masks ignore potentially deleted half-cut legs, and the repair mask ignores all four future cuts. The pure-star704-seam verifier also cannot be applied unchanged: the new rule has extra R-routes and its deleted-edge endpoints are not all star pins. Construct the actual254/1016 simple graph and test its new root, then old roots as authorized. A newroot pass does not settle old–old damage. No universal diameter-four upper bound for this new repair graph is assumed by this paper.

If at most1000 actual candidates for the one repair are tested and all fail before the compatible domain is exhausted, the result is a bounded prototype UNKNOWN, not a fixed-repair or global NO. If an exact cached-obligation join exhausts all half choices with no pair, it excludes only that frozen repair; a complete actual-candidate exhaustion would similarly remain fixed-repair scope. A first full positive needs the actual edge table, all-root acceptance and the root's separate decision before any new graph is counted. Neither the scalar capacity gate nor the cached join substitutes for that acceptance.

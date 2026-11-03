# Higher-degree core obstruction closes the same fixed-host family

This supplements the earlier minimum-degree-three checkpoint; it does not replace its historical prediction or claim that the parameter (11,3) itself is impossible.

**Scope.** Start from the actual accepted715-vertex host. Preserve every old edge. Add a nonempty finite set H of new vertices, with arbitrary new–new edges, arbitrary new–old spokes, and arbitrary additional old–old edges. Require a simple graph, maximum degree at most11 and diameter at most3. The520 old core vertices already have degree11. Consequently every new old–old edge lies among the195 eligible vertices, and no helper can have a core neighbor. Thus every added old–old edge, including any within an original P3 class, may be treated as the same E-edge type in the earlier paper.

The old core design and moment inputs are inherited, not checked again. The earlier route/degree tradeoff excludes minimum helper degrees0,1,2 and4 or more, and forces any hypothetical augmentation to have minimum helper degree exactly3. For each degree-three helper h it further forces eight leaf pins in eight distinct classes and

(b,c,s)=(20,8,0) or (21,7,1),

where b is the total old spokes at its three helper neighbors, c is the number of new old–old edge incidences at its own pins, and s counts additional helper incidences at its own pins. Its three neighbors' helper degrees must sum to13 or12 respectively. To see that last necessity precisely, let L be that degree sum. Their total old spokes satisfy b≤33-L. The two-helper-step term is at most8(L-3). The earlier upper bound replaced this by8(30-b); if L<33-b it loses at least8, whereas the full eligible-target bound has only one unit (or zero units) to spare before falling below195. Hence L=33-b.

## New nonminimum-helper argument

Take any helper v, now not necessarily of minimum degree, and let d be its degree in H. Suppose4≤d≤7. Let p be its number of old spokes and q the number of distinct classes containing its own pins. Then q≤p≤11-d≤7.

For any outside owner class j, each of these q old classes hits at most one of its eight core points within two steps in the original host. Thus at least one of those eight core points is missed by all original two-step suffixes from the own pins, and there are at least65-q such bad owner classes.

Every route of length at most3 from v to such a missed core point must repair its owner class through one of exactly two channels:

1. v–helper-neighbor–oldpin–core: at most b owner classes, where b counts all old spokes at the d helper neighbors, with multiplicity;
2. v–ownpin–E-endpoint–core: at most c owner classes, where c counts E-edge incidences at the own pins, with multiplicity.

Original old–old edges on the last two steps were already included in the inherited two-step suffix. A route v–ownpin–another-helper–core cannot occur because the core is saturated. A route with two helper edges also cannot end at a core in the remaining one edge. These statements cover shared old pins and helper reentry; they do not assume a single helper owner for any pin. Counting multiplicities only makes the upper bound larger.

Since every helper has H-degree at least3, every neighboring helper has at most8 old spokes, so b≤8d. Every own pin is either an old center with no slot left after its spoke to v, or an old leaf with at most one slot left. Therefore c≤p≤11-d, even when other helpers share that pin. In particular a new E-edge between two own pins is charged twice, which is harmless for an upper bound.

The necessary core inequality is therefore

54+d ≤ 65-q ≤ b+c ≤ 8d+(11-d)=7d+11.

It would require43≤6d, which is false for d=4,5,6,7. The corresponding deficits are19,13,7,1. No use was made of v being a minimum-degree vertex.

It follows that every helper degree belongs to{3,8,9,10,11}. There is a degree-three helper because the global minimum is3. Its three neighbors have degree sum9 if they are all degree3, and degree sum at least14 if any has degree at least8. The sum cannot equal12 or13, contradicting the earlier necessary local tradeoff.

## Conclusion

There is **no diameter-at-most-three, maximum-degree-at-most-eleven augmentation by a nonempty finite helper set that retains all old edges of this fixed715 host**, even allowing arbitrary new eligible-old/old edges and all helper spokes and helper–helper edges. Arbitrary original-P3 triangle completions are included: the new leaf–leaf edge is just an E-edge, consumes the same residual slots, and does not change any inherited original-host suffix used in the count.

This is a same-node paper closure, not a search over H, not an impossibility result for general N(11,3), not a new graph or Lean instance, and not a priority claim. Deleting/replacing old edges, changing the host, or allowing a larger degree remains outside the closed scope. The previous minimum-degree-three-open state remains recorded as the historical intermediate checkpoint. No source, field, design, core support, graph/BFS, helper sample, solver or Lean computation was repeated. The only new numerical operation was the four integer inequalities and possible three-neighbor degree sums.

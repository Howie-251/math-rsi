# Four-cut spread pins: paper check and falsifiable prediction

2026-11-01. Paper-only complement; no numerical sample, source-profile/BFS or route calculation is run here. The sole numerical driver remains f9's bounded run in the original cumulative20CPU case budget.

**Why this is a real rule change.** In the previous3matching-cut operation, four of the six cut endpoints become new-helper pins. Four pins distributed among only three disjoint cut pairs force at least one pair to have both endpoints selected. Those pins were adjacent in the original source; their cut edge itself is absent in the modified host. This is a forced original local correlation, not a proof that every such configuration fails.

Four disjoint cuts have eight distinct endpoints. Choosing exactly one endpoint from each cut for the four pins removes that specific pigeonhole constraint. It does not imply the four selected pins are pairwise independent in the original graph: another retained edge may join pins from different cut pairs. It also does not imply the two helper-radius balls are less overlapping or better covering; that is the new experiment's falsifiable claim.

**Degrees and edges.** Pair the four nonpin endpoints into two old-old repair edges, rejecting any repair already present in the deleted host. They form a matching on those four endpoints. Because each cut has one pin and one nonpin, such repairs cannot simply restore a selected cut edge. Split the four pins2+2 between adjacent new vertices600/601. Every one of the eight old endpoints loses its one cut edge and gains either one repair or one helper edge. All other old degrees stay3; each helper has two old pins and one peer. The result is simple cubic with602 vertices and

    900−4+2+4+1=903 edges.

The old route criterion from the parentPAPER_NOTE remains exact. For the modified old hostK (now four cuts and two repairs), helperx reaches an old targett at distance min(1+d_K(A,t),2+d_K(B,t)); both helpers cover all old vertices within9 iff R7_K(A)∪R7_K(B)∪[R8_K(A)∩R8_K(B)]=V(K). No original-source or old-only cover assumption is substituted.

**Predeclared prediction.** The new≤10000-distinct-configuration sample will contain at least one configuration in which both helpers reach all600 old vertices within9, i.e. the observed joint-helper cover rate will exceed0/10000. This is deliberately narrower than predicting a diameter9 graph. Such a helper-cover hit still needs actual old-old checking: cutting a fourth edge can damage more old routes despite better helper placement.

The preceding3cut sample had9999 first-helper failures and one first-helper pass followed by a second-helper failure, so it did not observe any old-old failure. Its terminal is boundedUNKNOWN, not an exact source/rule NO. If this new sample still has zero joint-helper pass, the new coverage prediction is refuted, but the whole4cut family remainsUNKNOWN. No fifth cut, additional seed or unbounded score search follows. This source/D9 sample remains separate from the exhaustive AFY70/D5 two-rule exclusions.

# Natural364 →365: paper scope and route review

2026-11-01. Paper-only complement: no source adjacency/profile, PORT_BALLS, geometry, D5BFS or secondsample was computed. Read the inherited natural-host report and `MULTI_VERTEX_PORT_BARRIER.md`, and this case's actualINPUT/RESULT/TERMINAL.

**Correct host and degree account.** This is the natural364/714 graph with28 degree3 ports and336 degree4 core vertices, not the published364/728 regular file. A perfectmatching on the ports adds14 old-old edges; their old distance5 makes these legitimate nonedges by inherited evidence. This intermediate graph G_M is4regular and retains D≤5 because no old edges were deleted. Delete two vertex-disjoint *original core-core* edges, then join all four freed endpoints to newz=364. Eachport gains1; eachcutendpoint loses1 and gains1; every othercore stays4; z hasdegree4. Thus n365,m714+14−2+4=730 and all degrees4 by construction.

**Outside the old NO.** The previous singlepoint and≤13helper exclusions retained every oldhost edge, added no old-old edges, and could attach only to the28 spareports. This new rule violates both restrictions and creates corepins by deletion. The portmatching also destroys the oldport-distance5 premise. Neither oldportR4 masks nor the minimum14helper conclusion is a NO filter for this operation. The old results remain valid in their original scopes.

**Exact newroot test; old-old still separate.** LetH=G_M minus the two cuts, and S their four endpoints. The only newvertex isz, so every shortestz-to-old path entersH once and remains there:

    d_J(z,t)=1+d_H(S,t).

Therefore newrootR5 is exactly R4_H(S)=V(H), with the newmatching and both cuts included. Bare-source R4 coverage is not interchangeable with this test. For oldverticesu,v,

    d_J(u,v)=min(d_H(u,v), d_H(u,S)+2+d_H(S,v)).

Newrootpass alone only gives each distance-toS≤4; it does not force this old-old minimum≤5. A surviving candidate must therefore receive the actual complete finalgraph BFS check already required by the numerical owner.

**Useful paper upper bound, not a family obstruction.** Every configuredgraph has D≤6 under the inherited sourceD5. For old-old pairs, use an originalD≤5 path. No cut leaves it intact; onecut can be replaced by endpoint–z–endpoint, costing one extra step. If the path uses both cuts, replace the entire segment spanning them by two edges viaz; its oldlength was at least3, so this shortens it. For z-to-oldt, choose an original-source closest endpoint s∈S. A shortest s-to-t path cannot traverse anycut: an endpoint encountered afters would be a closer member ofS. Thus this≤5 oldpath avoidsbothcuts, remains inH, and gives z-to-t≤6. Addedmatching edges can only shorten these walks.

Consequently an actualnewroot distance6 witness certifies D6 for that candidate using a paper upper bound, without pretending an old-old BFS was run. This does **not** force D6 for every possiblematching/cut choice; a D5 hit remains logically possible. No simpler source-facts-only obstruction closing this entire rule was found.

**Actual bounded outcome.** The sole10000-distinct sample ended `UNKNOWN_10000_SAMPLE_NO_HIT`: all10000 failed newrootR5, zero reached the old-old stage. The prediction of a newrootcover hit was refuted only in this sample. Firstcuts are(43,58),(151,314); the saved shortestnewroot path is

    364–43–54–56–360–345–0

oflength6. Equivalently, the fourpins are not anR4 cover in that actualmodifiedH. This shows the observedbottleneck is newrootcoverage, not testedold-olddamage. The fullmatching and exact witness remain inRESULT. Canonical cost1.537876879/20CPU, allterminal; no continuation, extra cuts, seed or H14 task is authorized. The whole matching/two-cut family is not exhaustively excluded.0newacceptedgraphs/parameters/Lean.

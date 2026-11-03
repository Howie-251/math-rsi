# Current(11,4)3645 source recovered: W(9) insertion layer, not81-fibers

The current literal source was obtained from [Nishant Bhakar's author repository](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg11/dia4). It has3645vertices,20044edges and maximumdegree11, with7vertices of degree10 and3638of degree11. The author's saved independent verifier reports diameter4 and0bad/unreachable pairs. No all-source BFS was repeated. The subsequent exact free-port coverage test below was executed once.

A fresh [Comellas main table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) reading confirms(11,4)=3645, not bold. Its [D4 description](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html) still describes the older3444 graph and has no3645entry. This lag is explicit; the current author repository supplies the actual3645data. The unique exact3645 lookup in the current Wiki/method ledger found no prior experiment on this literal.

Downloaded original files are source3645.edges, README.author.md, construction.author.json, insertions.author.txt and verification.author.txt. The author edge file has edge-type comment headings and no numericn/m header; source3645.header.edges is a format-only copy with the3645/20044header for downstream tools. The construction JSON specifies an explicit edge list, not a45-controller/F3^4recipe. No old972Zenodo403 interface was retried, and no external verifier/search program was executed.

## Bound actual structure

The author's construction starts with Dharunish Yugeswardeenoo's3444-vertex double of the generalized quadrangleW(9). It has820points and820lines, doubled to1640pointcopies and1640linecopies, plus164twins on a spread of82lines. Incidences match the two sheets; line copies and twin pairs have switch edges. The original base is11regular.

The current graph adds201vertices through absorbed-deletion insertions. Each insertion reconnects the two copies of a point and their detached hosts, while additional layer edges and chosen deletions preserveD4. The labels are concrete:

- 0..1639: pointcopies;
- 1640..3279: linecopies;
- 3280..3443: spreadtwins;
- 3444..3644: insertedlayer.

All original-type vertices have full degree11. Among the201layer vertices,194have degree11 and7have degree10. The current induced graph on the first3444vertices has18485edges, compared with18942in the original regular base; its457missing base edges cannot be ignored by claiming an unchanged oldcore.

The45×81factorization was only an initial question and is not the source architecture. The naive contiguous81-label partition is not equitable: in its firstblock, vertex0 has ten neighbors in block20 andone in block40, whereas vertex6 has three in block20,seven in block21 andone in block40. SOURCE_PROFILE.json records this diagnostic for all45blocks. No alternative81partition was searched.

## Prototype and degree-slack profile

The only free vertices are

    [3456,3489,3564,3571,3583,3603,3643],

each of degree10. There are exactly7free slots. Every prototype has at least9saturated neighbors; the minimum is attained only at3570. The full saturated-neighbor histogram is{9:1,10:75,11:3569}. Thus no complete sparestar exists, and the successful degree13single-fault star rule has no one-saturated-neighbor prototype on this source.

This is a local degree/structure profile, not a failed arbitrary-anchor search. CPU for the literal profile was0.04171s. No source diameter sweep, clone deletion,81chart test, voltage assignment or oldC25/Loz/441/1152restart was performed.

## Exact free-port coverage prediction refuted

COVER_PREDICTION.json froze the test that all7freevertices jointlyR3coverthe3645sourcevertices. The one exact multisource radius-3 computation covers2902vertices and misses743, all within the original3444labels; it covers all201inserted vertices. The first witness is vertex6, at distance4 from each of the7freeports. The prediction is false. COVER_RESULT.json contains the full missing list and the targeted witness distances; total CPU was0.01014s.

This also excludes any extension retaining every source edge, with any positive number of new vertices and even added old–old edges, under maximumdegree11 and diameter4. Along a short new-to-old route, take its last edge outside the original source. Its old endpoint must be one of the original free ports, and at most3original source steps remain. Such a route cannot reach vertex6. This statement does not exclude deleting source edges or absorbing insertion.

## Original-host two-edge absorption: prepared for the separate producer

The original3444base was reconstructed in memory by restoring the author's logged base-edge deletions. It has18942edges and is11regular. Each of164spreadtwins has the same ten original point-copy neighbors as a unique spread-linecopy. These exact signatures bind the two alternative original hosts without rebuilding geometry.

For every pointp=0..819, each of its two copies independently selects its original spreadtwin or matching spread-linecopy. The3280raw host choices reduce to2673whose two cut edges are both still present in currentG: TT698, TL632, LT630, LL713. All points are included;197valid candidates involve a point already used by the author's chain and2476an unused point. The201author steps use199distinctp, with repetitionsp493at3600/3633 andp665at3504/3505. This metadata does not restrict candidates.

Each candidate deletes those two edges and joins a new vertex to their four endpoints plus the seven free vertices: n3646,m20053,maxdegree11. Its new-root coverage is exactly the current-source R3union of these11neighbors. The existing seven-port union is reused, so the four endpoints need only cover its743missing vertices. The complete verification lemma in absorbed_pair_probe/PROOF.md proves that modified-graph BFS from closedN of the four endpoints plus the new vertex checks every potentially damaged pair. The old root set has37..44vertices on the frozen list, not3645.

The frozen literal list, original host bindings and reformatted seven-port cache are in absorbed_pair_probe/{frozen.json,HOST_BINDING.json,FREE_R3_CACHE.json}; prepare.py reproduces them in approximately0.083CPU seconds with no BFS. No candidate was evaluated by this preparation. A separate producer owns the finite actual scan and any complete3646graph; preparation alone is not a new lower bound. No global Wiki, HTML or delivery artifact was changed.

Evidence: BASELINE.json; PREDICTION.json; SOURCE_PROFILE.json; RESULT.json; COVER_PREDICTION.json; profile.py; the original author files. Original credits are preserved: Nishant Bhakar's201insertions over Dharunish Yugeswardeenoo'sW(9)double; the classical generalized-quadrangle basis is not claimed as new.

# Near-neighborhood proxy transfer: completefixedrule, no projectable stars

The rule learned from the successfuldegree13 construction was transferred once to the two different sources: degree14/94186 anddegree15/100132. This was not a D13recheck, a newgreedyseed or a resumedMIP. The positiveprediction of a complete projectedcover is refuted for the fixedrule.

## Frozen rule and exacttest

For everyfullvertex u withdegreeDelta, consider everyactualfree w withdegree<Delta satisfying

    |N(u) minus N(w)| <= 3,
    |N(w) minus N(u)| <= 1.

Commonneighbors were counted from allfreew by neighbor-of-neighbor wedges. For eachfullu choose oneproxy by maximumcommon, thenminimumdegree(w), thenminimumlabel(w). For eacholdprototypev inascendinglabel order, retainitsfreeneighbors and replaceeveryfullneighbor byitsfixedproxy. A prototype is rejected if any fullneighbor has noqualifyingproxy. Successfulprojectedpinsets would be deduplicated and checked with the complete existingallfreeR4cache; onlyfullcoverage and actualdegree legality would generate n+1.

Alloriginalfreecolumns and the complete source/degree/cache bindings were used. No rawcoremap or unprovedproxy-distance guarantee replaces the finalcompletecoverage criterion.

## Actual complete results

| source | freew | wedges | qualifying(u,w) | fullu withproxy | prototypesvisited | minimumunmapped fullpins | completeprojections | cachedR4checks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Delta14,n94186,m657452 | 3685 | 669198 | 1088 | 1088 | 94186 | 8 | 0 | 0 |
| Delta15,n100132,m749732 | 2498 | 523529 | 207 | 205 | 100132 | 9 | 0 | 0 |

Both proxysearches and both fullprototype passes completed. The failure is a structuraleligibility obstruction before radius4: everyoldstar has severalfullneighbors for which noactualfreevertex satisfies the fixednear-neighbor bounds. The existence of isolatedlocalproxies therefore did not supply a globalprojection of evenonefullneighborhood.

Because the rejectedfullneighbors have noeligibleproxy at all, changing the tiechoice amongeligibleproxies cannot repair this obstruction under the samebounds. This conclusion does not extend to broaderthresholds, severalproxies perfullpin, changedoldedges, nonstar neighborhoods or other sources. No such variants are started here.

## Costs and artifacts

Source14 CPU0.240984seconds; source15 CPU0.250909seconds. CompileCPU1.795135015; totalparent+allchildren CPU2.300918744, below the12total and5persource ceilings. No BFS, ballrecomputation, source download, solver, greedy, independentreview, Lean or newgraph occurred. Failed-star counts are not graphdiameters or badvertexpair counts.

PREDICTION.json freezes the rule andsourcebindings. Each d14/d15 subdirectory contains SOURCE_BINDING.json, the complete proxy_map.json, native.log, NATIVE_RESULT.json, RESULT.json andterminal.json. It gives eachchosenfullu/freew andcommon/difference counts. Root RESULT/terminal records the two variants under one transferablemechanism. Allrunning/pending flags are terminal; no sharedfamily,Wiki or HTML was changed.

Stop on the completezero-candidate result. The preexisting D14arbitrary14pin-cover question remainsUNKNOWN from its separateinterruptedMIP, and this proxytest does not upgrade it to an exclusion.

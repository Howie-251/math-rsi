# Degree13/D5: firstcomplete51418 star-repair extension

The firstcomplete candidate has51418 vertices and324461 edges, retaining everyedge of the published51417source and adding one vertex of degree10. Production actualdegree and complete selected-neighbor radius4 checks pass. Root independent acceptance passed: freshnewroot from the completeedgefile, exactcomparison retaining allofficial51417sourceedges, simple/connected/max13/ecc5. The latest publictable remains51417. This proves a new mathematical(13,5) lowerbound51418; no oldallsourceBFS was repeated.

## The exact finite rule

The prior fullstar scan found91prototypes whose currentfullneighborhood N(v) contains exactlyone degree13neighbor u; everyotherneighbor has a free slot. Freeze these91 by ascending(deg(v),v), delete thatuniqueu, and seek atmost min(13-|N(v)minus{u}|,2) actualfreeguards. Alloldedges remain. This uses neither rawH9orientation nor geometriccore coverage afterdeletion: every missing corepoint and extra is included in the actualwholegraph R4 criterion.

The frozen91 prototypes have degrees10/11/12/13 with counts38/36/14/3. Their mandatorysizes are9/10/11/12, leaving fullguardbudgets4/3/2/1. Only atmost2guards are tested; failure wherecap>2 cannot exclude repairs using the largerbudget.

Nativeproduction directly reuses h9_redei15/production/cover.cpp with the exactdegreeassert changed once to assert(DEG==13). It does not inherit a rawmap or a corecoverage shortcut. No sourceoldBFS was run.

## Successful literal

Prototype51013, degree10, has fullN(v)=[2813,9214,11352,15101,25662,33884,38121,38574,42842,48533]. Its unique saturatedneighbor is11352. Delete thatpin and retain9mandatorypins:

    [2813,9214,15101,25662,33884,38121,38574,42842,48533]

The oneguard50577 completes coverage. The newvertex51417 has the complete10-neighbor list

    [2813,9214,15101,25662,33884,38121,38574,42842,48533,50577].

Their olddegrees in the same order are[11,12,11,12,12,12,12,12,11,11], all strictlybelow13. The source's oldmaximum13 is unchanged or respected after one degreeincrement at eachpin; the newvertexdegree is10.

The9mandatorypins alone missed3614oldvertices, including3535core and79extras. A native exactguardmask search found50577; a fresh native selected-neighbor R4 check covered51417/51417 with0missing. This is the required complete-current-oldgraph certificate, not merely a smallmissingcount or a core-only geometricguarantee.

Given the inheritedvalid D5source, old-olddistances cannot increase and newroot-to-old distance is atmost1+4=5, so the expansion has D<=5 mathematically. Edgefile, literalparameters and exactcurrentcoverage are provided for root's one independent check.

## Profile and actual termination

The firstprototype4580 after deleting45089 had2752missing (2724core+28extras) and no atmost2guardrepair. Its nativecost was0.195981CPU seconds; firstprofile projected19.656583seconds for all91includingcompile. The successfulitem later had more mandatoryholes but a singleguard with the needed completecoverage, so holecount was not used as the searchobjective or successcriterion.

The batch stopped immediately on ordinal37:38itemsvisited,37exactfailures in the atmost2guard scope,1fullcandidate,53unattempted. CompileCPU1.822312189;39nativecalls; totalparent+allchildren CPU9.644256492, under30. There was no same-sourceBFS, wholeoldgraphBFS, solver, paidreview, hash, additionalfaultbranch or continuedcandidatequeue.

Artifacts: PREDICTION.json, frozen91.json, freeze_summary.json, cover.cpp, run.py, FIRST_PROFILE.json, first_hit.json, literal_params.json, generate.py, graph_d13_D5_n51418.edges, peritem nativeevidence underitems/, RESULT.json and terminal.json. SharedWiki, familydelivery and HTML were not modified by this producer.

Independent receipt: independent_newroot51418.json, CPU0.922seconds as reported byroot. The producer cost remains9.644256492CPU; it is not relabelled as a laterallsource check. The53unattempteditems are continued only by a separately frozen finitecurrent-base batch.

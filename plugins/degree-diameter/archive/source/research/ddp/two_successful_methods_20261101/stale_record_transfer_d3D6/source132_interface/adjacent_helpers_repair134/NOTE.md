# Exoo132 adjacent-helper repair sample

Actual status: UNKNOWN_10000_SAMPLE_NO_HIT. Tested 10000 distinct configurations to a terminal decision. Both helper roots passed radius6 in 0; 0 of those then failed an old-old pair. Stage counts and first actual counterexamples are in RESULT.json; ATTEMPTS.csv records every sampled configuration. The published sourceD6 fact is inherited; no source-wide D6 validation was run in this case.

The prediction that some candidate preserves new-old coverage was not supported in this sample. Old-old testing is only reported for candidates that passed both helper roots. A sample with no hit is UNKNOWN about the full rule. No claim of an exhaustive negative result or a new graph is made without a saved full candidate and root acceptance.

The operation keeps every source vertex cubic: six cut endpoints each lose exactly one edge and gain exactly one via repair or helper. Each helper has two old pins plus the peer edge. Repair endpoints must be anoriginalsource nonedge,so restoring a cutedge is excluded fromthisnumericdomain. The only allowed old modifications are the three cuts and single original nonedge repair. A hit has134 vertices and201 edges. This uses a different source and diameter from the old AFY70/D5 and Exoo600/D9 experiments; their negatives do not exclude this Exoo132/D6 rule.

Exact cooperative helper routes and old-old route cases are in ../PAPER_SCOPE_REVIEW.md. Ordinary BFS was performed only on modified134-vertex candidates, with both helpers first; old-labelled BFS rows are final-candidate checks. Onlyone firstfailedoldpair may have anoriginalsource shortestpathdiagnostic,recordedseparately. No source-wide original D6 BFS, symmetry search, solver, Lean, web or review was run.

Budget inherits priorcase0.179405319,includes conservative newpreparation0.2CPU,actualcompiler1.406538000 and run child0.045318000, plus driver CPU. Total1.872229226/20CPU, one worker. All processes terminal; fixed seed202611010306, no automatic retry or extension. Root owns acceptance, counts and global documents.

Actual stage comparison:9997 first-helper failures and3 second-helper failures;zero configurations passedboth. Therefore old-labelled finaltargetBFS andtheoptional originalsingle-pair diagnostic wereboth0,not old-old successes orfailures. The predictedcooperativecoverage wasrefuted inthissample only. One structuralinputcheck didbind132labels,198simpleedges andcubicdegrees;sourceD6/allrootBFS remained0. Canonicalfinal cumulativeCPU is1.872316415/20. Allworkstops without anotherseed,cutpattern orsample.

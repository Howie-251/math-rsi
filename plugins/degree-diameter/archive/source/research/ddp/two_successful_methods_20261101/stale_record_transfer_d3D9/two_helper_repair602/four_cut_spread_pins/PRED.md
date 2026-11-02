# Four-cut, one-pin-per-cut feedback experiment

Prediction before execution: at least one of the next10000 distinct sampled configurations has both adjacent helpers at distance≤9 from every600 old vertex, improving on the prior0/10000. Old-old preservation remains a separate check; a hit is not predicted or presumed.

The prior three-cut rule selected four pins from three disjoint cut pairs, forcing at least one entire oldcut pair into the pin set by pigeonhole. The new rule removes this specific compulsory adjacency: take four disjoint oldedge cuts; select exactly one endpoint from each as a pin; pair the other four endpoints into two original nonedges for old-old repairs. Partition pins2+2 between two adjacent helpers. Accidental other old adjacencies between pins are allowed; no extra spacing claim is made. Everyold endpoint loses1 and gains1, eachhelper has3 neighbors, so n602,m900−4+2+4+1=903, allcubic.

Use the same fixed seed202611010309 once, with canonical cut/pinmask/repairmatching/helperpartition keys rejecting duplicates. At most10000 distinct configurations, no five-cut or additionalseed branch. First two ordinary helper BFS tests on each final602 target; only both-pass configurations receive all600 old-labelled target BFS rows. First full hit saves edges and stops. No original600 validity/BFS is rerun.

This is one changed generator under the same20CPU total, inheriting prior terminal1.414890833; include all new preparation/compile/run. Any no-hit result remains UNKNOWN for the full rule. Stop both rules at this batch end; root alone accepts/counts graphs. No solver/Lean/remote/install/hash.

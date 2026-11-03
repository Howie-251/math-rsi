# GQ80 girth>=5 CNF: one window UNKNOWN

**UNKNOWN, no candidate.** Actual counts matched the frozen model:1080allowed noncollinear matching variables (540per side),80degree rows with27choices,1080cover clauses of29literals (17own+12relay), and6480unique mixed-rectangle forbiddances. Total80ALO+28080AMO+1080cover+6480rectangle=35720clauses. VARIABLE_MAP.json explicitly binds new DIMACS IDs to the old1560-variable model. Saved geometry/old model were reused without rebuilding either.

The restrictions are exactly girth>=5 for incidence plus two matchings: no collinear matching edge means no triangle, and every possible4cycle is a forbidden P–incidence–Q–incidence rectangle. Hence each5regular root would have26 distinct vertices within two steps; D3 still needs the exact original covering conditions. This is a restricted subfamily, not an exclusion of general GQ80 graphs.

One CaDiCaL-t30 returned exit0/UNKNOWN. Preparation measured0.056438234CPU/0.057925399wall; solver30.002933CPU/30.007696368wall. Total parent+children CPU was30.108124976, parent wall30.150679789, below35CPU/45wall guards. Internal SAT counters958516conflicts/1306031decisions/13644restarts are not graph bad-pair counts. No SAT witness, raw UNSAT, candidate, BFS, or new lower bound occurred.

The existence prediction remains UNKNOWN_NOT_REFUTED. Stop this batch without another seed, solver, timer or new cut. wiki_rows.json updates the same`ddp-wave11-gq80-paired-matchings`ID with a girth5 variant; INHERITED_THREE_WINDOWS_ROW.json and nested metrics preserve all three prior UNKNOWN windows. Code, actual counts, explicit map, CNF and terminal receipts are saved for recovery.

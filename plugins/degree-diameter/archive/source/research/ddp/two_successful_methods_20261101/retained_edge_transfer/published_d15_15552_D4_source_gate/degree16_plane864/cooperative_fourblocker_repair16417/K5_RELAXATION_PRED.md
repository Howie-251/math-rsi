# Saved helper-ball K5 relaxation prediction

Read only existing342 interfaces/schema/helperB0..B3 rows. No source, ball computation, H search, BFS or solver. Relax allfive helpers tocompleteK5, ignoringdegree. For helperh its strongestbasecover is B3(P_h) union allother B2(P_g), and helperpairs cost1.

**Concrete falsifiable prediction:** firstcasev15 stillmisses target1 fromhelper15560 underK5, because the testedH255 already joined thathelper toallfourothers and the successful oldleg options still require3oldsteps, giving1+1+3=5. Counts acrossall342 are unknown beforepostprocess.

Classifyeverycase as EVEN_K5_BASE_FAIL (firsthelper/firsttarget and eacholdleg budget) or K5_BASE_PASS_BUT_ALL_DEGREE_LEGAL_H_FAIL. Thelatter separatesroutepossibilityfromH/degreecompatibility; theformer cannotberepaired byaddingmorehelperedgeswithunchangedP.

Saveallcasecategories/fullactualsampledecompositions. CompleteK5 isnotasserteddegreelegal andnotanewcandidategraph. Samecase cumulative120: prior37.767076346+newprep.10+actualpostprocess, itself≤1CPU. CompleteSTOP, no sourceguided/split/S5 or new solver.

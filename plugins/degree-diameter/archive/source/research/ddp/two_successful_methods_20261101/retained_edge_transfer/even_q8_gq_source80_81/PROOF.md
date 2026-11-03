# Two fixed q8 filled-source candidates: production receipt and prefix proof

The producer wrote both classical unfilled sources and both filled candidates from the fresh small incidence/spread data. Classical unfilled files are reproductions of known sources,not new results. The separate fresh validation has since passed,as recorded below;this producer assigns no ledger count,and there is no concrete q8 source Lean yet.

## Actual identifiers and output

Derived uses the fresh restricted point labels0..511 and derived line labels0..639 from DERIVED_INCIDENCE.tsv. Its spread binding uses DERIVED_SPREAD64.tsv's `derived_line` column. Old vertex label is p*640+l,not an original585-point label. Balanced uses original point/line labels0..584 and SPREAD65.tsv's `original_line`,with old label p*585+l. No field operation or new geometry construction was performed.

| case | unfilled file n/m | filled file n/m | actual filled degrees |
| --- | --- | --- | --- |
| derived GQ(7,9) | 327680/13104640 | 327744/13109760 | 80:327744 |
| balanced GQ(8,8) | 342225/13857480 | 342290/13862745 | 81:342290 |

Files are under `derived/` and `balanced/`: `classical_unfilled_d80_n327680.edges`,`graph_d80_D3_n327744.edges`,`classical_unfilled_d81_n342225.edges`,`graph_d81_D3_n342290.edges`. All have n m headers and strict u<v lexicographic bodies.

Every old neighborhood is the Cartesian product linePoints[l]×pointLines[p],labeled q*nl+M,excluding the old vertex itself. The same sorted higher-neighbor stream is emitted to the unfilled and filled files. Thus every classical old edge is retained literally. A flag(p,l) receives only the unique fill indexed spreadOwner[p]. No fill-fill edge is emitted.

Derived has5120flags: their old degree79 becomes80; all322560other old vertices already have degree80. Its64fills each have80pins. Balanced has5265flags: their old degree80 becomes81; the336960other old vertices already have degree81. Its65fills each have81pins. Actual emitted edge and degree counters match all stated headers. `FILL_PINS.tsv` explicitly binds each helper label to its oldflag labels.

## Every prefix uses only available capacity and old interiors

For spread line S_j, pins are all flags(p,l) with p on S_j and l through p. Each oldflag has a point p and therefore exactly one spread owner. Consequently all helper pin sets are disjoint,each consumes precisely one old degree slot,and no step needs a later helper. After r helpers,remaining oldflags have degree delta-1;all other current vertices have degree delta. `PREFIX_DEGREES.csv` records this actual pin-count arithmetic after every prefix,including zero.

The existing generic source interface is `OppositeIncidenceSpread` in `OppositeIncidenceSpreadFamily.lean`,whose graph uses the actual incidence lists and explicit old-label equivalence. Its WalkD3 theorem requires an inhabited chosen line and,for each point p and line l,a witness q,m with Inc(q,l),Inc(p,m),Inc(q,m). These are supplied mathematically by the already checked fresh GQ projections;the current producer does not rerun those checks.

Its D3 proof also works when the helper index is restricted to a prefix,including the empty prefix:the diameter theorem has no full-spread owner hypothesis. All helper-to-old and helper-to-helper routes in that construction use oldsource interiors. For example,two helper lines choose points q,r joined by a connector m;the oldflags(q,m),(r,m) provide their three-step route,with coincident cases shortening it. The general generic Walk proof handles the coincidences. Degree control for every prefix follows directly from disjoint flag pins and the oldflag slack above.

With maximum degrees80/81,the radius2 endpoint capacities are6481/6643,far below every source order here. Thus a D3 graph cannot also have diameter at most2. Connecting the fresh finite data to the conditional generic Lean theorem is still a new formal obligation;the old generic theorem alone is not a completed concrete q8 Lean proof.

## Prediction and actual stopping status

The pre-production prediction was64copies of(1,80,5544,322119) and65copies of(1,81,5760,336448). The R2 count is(s+1)*s*t*(t+2). The independent agent has actually checked all64and65helper roots,and every histogram matches. The producer itself ran no BFS.

Compile CPU0.941706seconds,derived production0.822488,balanced production0.861531,and input/wrapper approximately0.019431,total **2.645157007CPU seconds** under30seconds,one worker. First compilation and both writers passed. No field/GQ/projection validation,BFS,Lean,solver,otherq or automatic next family was run by the producer. Its RESULT and TERMINAL preserve the original producer-only pending-acceptance receipt and no active process.

Fresh validation used10.520798412CPU seconds,reading each of the four complete files once. It checked oldbody edge-exact retention,the actual incidence formula,all degrees,all newflagpinsets,and all129helper-root ordinary BFS;oldroot BFS count0. Explicit nonD2 witnesses are derived[0,713] and balanced[42705,43363],with no edge/common neighbor. Independent prefix-pin records check spare degree and no previous use at every helper step. See `independent_acceptance/` for actual proofs,receipts and ordered helper-pin bindings. These small binding files can support a future formal bridge without another biggraph/BFS run.

The actual public gate locates327680/342225 and candidate gains64/65,only against checked source guarantees. Exact fill priority remains UNKNOWN because the JGT1985 fulltext gap persists. These new candidates are excluded from the separate P33 fifteen-target snapshot and ZIP scope.

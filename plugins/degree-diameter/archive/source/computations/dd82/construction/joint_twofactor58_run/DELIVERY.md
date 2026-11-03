# Joint free twofactor58 — final mathematical and experimental delivery

Final update 2026-10-18 09:23:05 UTC. Bounded mechanism CLOSED4/4, overall58–61 goal ACTIVE.

## Results and precise scope

1. Self-contained paper parity argument: any58 target has a triangle or a nonneighbor pair with at least3 common neighbors; internal4/cross4 balanced partition impossible. A nontrivial two-cell equitable partition must29+29/internal2/cross6. Accepted round1.
2. New self-contained component rigidity: H0C+CH1+C=J+P for two29-point twofactors forces BOTH H0,H1 to be singleC29. Fix a right cycleT lengthb; integersx_i toT satisfy xprev+3x_i+xnext=b+p_i. Extremes force range≤1; two values would alternate on all left edges, impossible on odd29; constantp forcesb29, transpose finishes. Accepted round3.
3. With the prior separately checked2C29 CNF and full graph bridge, no58 target has a nontrivial two-cell equitable partition. This final exclusion is computer-assisted, not entirely paper-only.
4. Stronger all-target constraint: every induced2-regular subgraph has at most28 vertices. Ifs≥29, its complement has internal minimum degree≥2 by actual route capacity (degree0 allows24 endpoints, degree1 at most28); cross-edge handshake forces s29 and complement2regular, invoking item3. Accepted round4. Applies to induced cycles and induced disjoint unions, not chorded cycles or arbitrary2-factors.

Full papers: proofs/dd82/construction/EQUITABLE_TWO_BLOCK58_REDUCTION.md; JOINT_TWOFACTOR58_COMPONENT_CONSTRAINTS.md; INDUCED_TWOFACTOR58_SIZE_BOUND.md. Old computed import: FREE_CROSS58_HAMILTON_BRIDGE.md. All relative proof names in this paragraph are under proofs/dd82/construction/.

## Actual single experiment — unchanged UNKNOWN

The model chooses ALL H0/H1/C jointly, with both internal2regular graphs free and crossdegree6. The legal right relabeling normalizesP=I without fixing cycle types. Every original same-side/cross-side pair is covered by actual edges/paths. No extraCdiagonal, triangle, Hamilton or hidden symmetry clauses.

Savedinput206103variables/674424clauses, including1653actualedgevariables. Oneprepare exit0 used2.352518CPU/2.369912wall seconds. Fresh CODE_REVIEW.md checked actual artifacts plus semantic completeness; 8AND valuations,7complete smallassignments passed, saved normalization2CNFcases. Independent separate24rightrelabel checks included14noninvolutoryP. These are semantics checks, not impossibility evidence.

One no-proof CaDiCaL -t58 discovery call, hard60CPU/90wall, CPU1,4GiBAS,256MiBfile. Exit0 UNKNOWN after57.906149CPU/58.206894wall seconds at internal softlimit. No model, decode/BFS or contradiction certificate. Originalresult.json unchanged. No solver/checker rerun, circle enumeration or increasedbudget afternewpaperproof.

## Review receipts and continuation

Actual existingAntigravity thread a3882b8c-59be-47b9-9626-73ccad9c417a; requested/returnedCLI metadata gemini-3.8-flash-high/high, SUCCESS. These are CLI-reported metadata, not independent backendattestation.
- Round1: reviews/dd82/20261018_joint_twofactor58_direction.json, paper/direction.
- Round2: reviews/dd82/20261018_joint_twofactor58_final_review.json, implementation/UNKNOWN snapshot accepted; mathematical family then stillopen.
- Round3: reviews/dd82/20261018_joint_twofactor58_component_review.json, newcomponentproof+equitable exclusion.
- Round4: reviews/dd82/20261018_joint_twofactor58_induced_bound_review.json, newlarger induced-subgraph scope.

Later paper results supersede the earlier mathematicalOPEN snapshot, not the actualUNKNOWN experimental record. No new fulljointCNF certificate and no complete58 exclusion. No graph above57;57≤N(8,2)≤61 unchanged; Leanpostponed.

User-requested old/new61 boundedalignment also COMPLETE: research-wiki/DD82_OLD_NEW61_ALIGNMENT_20261018.md. Exact[3,3]↔shared-endpointdouble correspondence; old4RAWrecords inherited forwork avoidance, no checkedDmatching theorem; I12H/globalnoO fine structures remainconditional. No oldSAT/Lean/all-history audit. Do not repeat alignment or coveredlongDpaths.

Hourly means HTMLreporting only, not newtheorem/hypothesisquota. Continue constructions and globalproofs with the new58 induced-subgraph obstruction; no need to enumerate the nowexcludedtwofactorfamily. Mathematicaldirection follows evidence and humanfeedback.

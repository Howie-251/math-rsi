# C9 external core and offset4 secant chords: uniform T-to-E obstruction

The result is for the declared PREDICTION.json rule, with inherited actual A/S/T geometry from the13-point base. No new geometry INPUT, CNF, decoder, chosen graph, voltage assignment, solver or BFS was generated. Root and the independent source-scout/expert paper reasoning confirm the following route classification.

## Three positive predictions remain valid

The9 external vertices are E_i in C9. Pair i of secants has T-adjacent endpoint s_i and its mate s'_i, joined by a retained identity S-S edge. Their external edges are E_i-s_i and s'_i-E_(i+4). Only both external edges of pair0 are deleted. Helpers form a-b-c, with a attached to E0,E4 and one A, b attached to two A, and c attached to the full3-point T fibre. Each freed S attaches to one eligible A; remaining A ports pair as declared.

Every pair of external vertices is within3: cyclic offsets1,2,3 use C9, and cyclic offset4 uses its secant-pair path of length3, except the removed pair0 whose E0-E4 route is replaced by E0-a-E4 of length2. This proves E_E.

The complete T fibre lets c reach every T-adjacent secant in2 and every secant mate in3. The inherited A-S incidence also lets it reach every other A lift in3. Each E_i has its T-neighbor branch via s_i, except E0; c-b-a-E0 restores that target. The helper targets are already within2. This proves c_all, as an R3 statement only.

Finally, the C9 closed radius2 sets of E0 and E4 cover all9 external vertices, so a reaches every E in3. This proves a_E. None of these statements certifies the remaining old-root routes.

## A full-T root must still miss an external target

Because the A-S edges are perfect matchings for every allowed trit, exactly one vertex t in the full T fibre is adjacent to s0. Its four neighbors are its three old secant neighbors and c; its port is already occupied by c, so it has no other new edge. The other two secant neighbors are T-adjacent endpoints s_i,s_j of pairs different from0.

The s0 branch gives no external endpoint within3 steps from t. Both external edges of pair0 are deleted. After t-s0, at most two steps remain: s0 can next reach its old A neighbor, its S mate s'_0, or its newly paired A. The two A vertices have no E neighbor; s'_0 has lost its E edge and also has no E neighbor. Thus this branch contributes zero.

The c branch also contributes zero. No external vertex lies within2 of c: c has only T-fibre neighbors and b, and neither an A vertex nor b has an external neighbor. The valid uniform R3(c) certificate therefore begins too late to help t within3.

For either remaining secant branch s_k, an external endpoint within3 of t can only be its direct external neighbor E_k, the two cycle neighbors E_(k-1),E_(k+1), or the external endpoint E_(k+4) reached through its S mate. Its other A neighbors have no E neighbor. New helper a may be reached after stepping through E, but that uses the third step and ends at a; another step would be needed to produce a new E endpoint. Each branch therefore supplies at most the four-element set

    {E_(k-1), E_k, E_(k+1), E_(k+4)}.

Consequently t has at most8 of the9 external vertices in its closed radius3. The two sets may overlap, so8 is an upper bound, not an exact measured count. At least one external target is too far for every trit and every legal port completion. The witness root t and target can depend on those choices; this is a uniform existence proof, not a fixed expanded-graph BFS result.

## Scope and termination

The joint existence prediction is strictly refuted for this C9/offset4/pair0-deletion/fullT-c/P3 rule. The three stated positive route-class predictions are independently supported; they do not contradict the old T-root failure. This does not exclude arbitrary42-vertex graphs, every altered E-core or other helper/attachment rules.

Compilation was stopped before any new INPUT, variable map, CNF or decoder was generated. Only the parent-frozen prediction, paper reasoning and label-coordination discussion occurred. The two earlier no-cut and single-ES-cut histories remain unchanged. No solver budget was consumed, and no next-template or free-spoke adjustment is started by this result.

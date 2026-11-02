# Hoffman–Singleton augmentation: exact construction model and experiments

## Target

Construct a full58–61 vertex graph of maximum degree8 and diameter2 by augmenting the explicit50-vertex Hoffman–Singleton graph Q. This is a restricted construction mechanism, with no assumed coverage of arbitrary target graphs.

## Status

COHERENT AS STATED as an exact formulation. No valid target found. The induced-Q formulation is mathematically impossible at all four orders. Deletion repairs are the next mechanism; two fixed58 star-deletion geometries are also checked UNSAT.

## Invariant object and assumptions

The invariant is actual one/two-step coverage in a single expanded simple graph. Its block adjacency is [[A',B],[Bᵀ,H]], where A' is the retained old adjacency, B is binary old–new incidence, and H is the new simple graph. Every target at order>57 is8-regular by the elementary radius-two bound. All identities below are exact; no probabilistic or matrix-relaxation conclusion is substituted for a graph.

## Notation and derivation strategy

The explicit Q has P(i,j)=5i+j and Q(i,j)=25+5i+j, indices modulo5. Its edges are P(i,j)P(i,j+1), Q(i,j)Q(i,j+2), and P(i,j)Q(k,ik+j). The generator checks175 edges, degree7, and common-neighbor count0/1 for adjacent/nonadjacent old pairs. The official [NetworkX HS documentation](https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.hoffman_singleton_graph.html) supplies an independently identifiable construction source.

Write k=n−50. First retain A'=A_Q. Each old vertex then has exactly one new neighbor, giving attachment map f and fiber sizes s_a=8−d_H(a). Thus2e(H)=8k−50. Old pairs are already covered. New pairs must be covered inside H. The remaining exact obligation is N_Q(x)∩f⁻¹(a) nonempty whenever a is outside the closed H-neighborhood of f(x).

## Derivation map and main conclusions

1. Degree rigidity gives a fiber partition and the exact auxiliary edge count.
2. Unique common old neighbors give the collision identity and inequality in [the companion proof](CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md). These imply no induced-Q target at58–61, independent of SAT or symmetry normalization.
3. Allow old-edge deletions. For t deletions, row B_v has size1+r_v, total old–new incidences50+2t, and e(H)=4k−25−t.
4. The simultaneous coverage obligations are A'+A'²+BBᵀ>0 off diagonal, B+A'B+BH>0 entrywise, and H+H²+BᵀB>0 off diagonal. Alongside both degree equations, these are sufficient and necessary for the expanded graph.
5. At58 the new-pair count forces0≤t≤7 and excludes1≤t≤5. At t=6 the deleted edges form a star and force the recorded repair geometry. At t=7 only a seven-star, six-star plus disjoint edge, or broom survives. The companion proof contains the exact inequalities and topology proof.

## Actual complete candidates and bounded experiments

All complete seeds are8-regular, have4n edges, and have diameter3. The independent BFS checker reads only the saved expanded edge list; it saves every bad pair and common-neighbor list. None is a valid lower bound.

| Model | n | Bad seed pairs | Solver wall seconds | Result |
|---|---:|---:|---:|---|
| Retained Q plus star controller |58|105|0.189|LRAT checked UNSAT|
| Retained Q plus Petersen controller |60|160|30.292|LRAT checked UNSAT|
| Six-star deletion, forced repair ports |58|97|0.132|LRAT checked UNSAT|
| Seven-star deletion, free two-ports on leaves |58|66|0.589|LRAT checked UNSAT|
| Broom deletion, one explicit embedding |58|109|0.132|LRAT checked UNSAT|
| Six-star plus edge incident with retained neighbor |58|114|0.069|LRAT checked UNSAT|
| Six-star plus independent edge near retained neighbor |58|108|0.067|LRAT checked UNSAT|
| Six-star plus independent edge farther from retained neighbor |58|113|0.067|LRAT checked UNSAT|

Source: [hs_augmentation.py](../../../computations/dd82/construction/hs_augmentation.py), [hs_delete_star58.py](../../../computations/dd82/construction/hs_delete_star58.py), [independent checker](../../../computations/dd82/construction/verify_hs_candidate.py). All inputs, maps, proofs, results and expanded seeds are under [hs_augmentation/](../../../computations/dd82/construction/hs_augmentation/). First two initial RAW solver records are followed by certificate_check.json; the deletion records include captured checker logs. Every check uses official lrat-trim0.2.0 --no-trim and ends exit20/s VERIFIED. Each solver had a60-second cap and one pinned CPU; no unchanged run was repeated.

The SAT formulas enforce exact row/column degrees, and all uncovered old pairs through a shared new neighbor; old–new clauses list every possible intermediate vertex. New–new coverage for the two star models follows directly from fixed ports and is asserted before generation. The additional four models in [hs_delete_remaining58.py](../../../computations/dd82/construction/hs_delete_remaining58.py) encode every new–new pair explicitly; their additional forced ports are proved in the companion note. They use30-second caps and captured LRAT checker logs. Cardinality uses only the existing generic exact-counter primitive, without any n62 graph constraints.

## Remarks and interpretation

The failure identifies a structural choice to change: repartitioning an intact HS graph cannot help. The deletion model is a different simultaneous design problem, not a new random seed of the excluded partition search. In the seven-star case the center attaches to all8 new points, each former leaf chooses2 new points, and its6 old neighbors must bijectively use the complementary6 colors. The chosen first leaf can be assigned colors0,1 by renaming new vertices; all other leaf choices remain free.

## Boundaries and non-claims

The analytic induced-HS theorem covers all auxiliary graphs. Each computational deletion exclusion is conservatively scoped to the saved old labeling and fixed deletion pattern; global HS automorphism coverage has not been used as a hidden premise. No arbitrary58–61 order is excluded. n62 evidence has a separate completed review. These results are not Lean theorems.

## Open risks and next action

No unresolved modeling approximation exists: a SAT assignment expands into a full graph and would be independently checked. All selected deletion shapes and embeddings failed; move to a materially different construction such as order59 with variable auxiliary graph, or another base/representation. Full58 deletion-family coverage would require all embeddings or a proved automorphism reduction; it is not inferred from these six deletion certificates. Do not restart identical inputs.

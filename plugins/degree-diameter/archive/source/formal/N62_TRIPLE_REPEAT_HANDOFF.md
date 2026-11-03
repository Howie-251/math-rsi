# Actual order-62 triple-repeat local geometry

Task source: `proofs/dd82/n62/RECOVERED_REDUCTION.md`, Steps 1–2. Target: original finite simple graph `G`, degree at most 8, diameter at most 2, order 62, and an actual entry `defectMatrix G u v = 3`.

New module: `DegreeDiameter/N62TripleRepeat.lean`. No root template, supplied defect row, component certificate, or global defect bound is a hypothesis. `commonNeighborVertices G u v` is the actual filtered original-neighbor set, with cardinality definitionally equal to `commonNeighborCount G u v`.

Implemented interfaces:

- `n62_triple_repeat_rows`: both complete actual rows are concentrated with weight 3 at the opposite endpoint.
- `n62_triple_repeat_nonadj`: endpoints are distinct and nonadjacent in the original graph.
- `n62_triple_endpoint_zero_triangle`: an endpoint has an independent original neighborhood; applying symmetry gives both endpoints.
- `n62_triple_common_card`: the actual common-neighbor set has exactly four vertices.
- `n62_triple_common_nonadj`: this four-set is independent in the original graph.
- `n62_triple_common_rows`: for each member, its complete actual defect row is exactly the unit indicator of the other three members. Thus the actual repeat block is `J₄-I₄` and every entry leaving it is zero.
- `n62_triple_common_pair_neighbors`: any two distinct members have common-neighbor set exactly `{u,v}`.
- `n62_triple_outside_common_neighbors_unique`: a vertex outside `{u,v}` has at most one original neighbor in the four-set.
- `n62_triple_pair_component`: the actual repeat-support component of `u` is exactly `{u,v}`.
- `n62_triple_common_component`: the actual support component of every member of the four-set is exactly that four-set.
- `n62_triple_component_sizes`: constructs the actual size-2 and size-4 support components.

Proof connections: actual row sum 3 plus nonnegativity saturates the triple rows. The existing actual original-edge defect bound excludes endpoint adjacency. The triangle incidence lower bound then gives triangle-free endpoints. The off-diagonal defect identity gives four common neighbors. Each distinct pair in the four-set has the two actual endpoints as common neighbors and is nonadjacent, hence has defect at least 1. Three such lower bounds saturate each row, proving the entire unit row and its closure. Actual support walks stay in either closed set, while actual positive entries connect all its vertices; this identifies the actual connected components.

Dedicated audit: `ReviewN62TripleRepeat.lean`, including original-input examples for both triangle-free endpoints, the actual four common neighbors, the full four-set defect rows, and the actual component sizes.

Reproduction:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62TripleRepeat
lake env lean ReviewN62TripleRepeat.lean
```

Targeted build exit 0: `logs/n62-triple-repeat-second.log` (new module 16s, no new-module warning; the log replays existing warnings from dependencies). Dedicated audit exit 0: `logs/n62-triple-repeat-type-axiom-audit.log`. All 12 public theorems, including the membership API, use only `[propext, Classical.choice, Quot.sound]`. All three original-input example callers compile. The first build log preserves repaired identifier/symmetry-interface errors and is not a success record.

Remaining boundary: this module does not build the five-cell quotient, the `E+`/`E-` matching, the later finite matrix objects, or any exhaustive coverage/enumeration/parity contradiction. Full triple elimination and the unconditional actual `B ≤ 2` theorem remain outstanding. The local conclusions here do not assert nonexistence of order 62.

Existing modules, shared entrypoints/STATUS, and order-63–65 sources are unchanged. Parent owns integration and cross-family source review.

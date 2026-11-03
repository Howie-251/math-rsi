# Five-helper candidate checker — prepared, not run

The sole numerical owner searches the342 four-blocker choices and helper
graphs. This folder reads none of its search inputs or masks. No candidate
or data suite is assumed during preparation. ROOT must first see an actual
complete candidate and assign a fresh independent budget.

Future entry:

```
python verify_cooperative_candidate.py \
  --source /absolute/repo/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/graph_d16_D4_n16416.edges \
  --candidate /absolute/new-case/graph_d16_D4_n16417.edges \
  --params /absolute/new-case/actual_params.json \
  --out /absolute/new-case/independent_acceptance \
  --cpu-budget ROOT_ASSIGNED_SECONDS
```

Params have actual labels, not helper indices:

```
{"new_center": ORIGINAL_SOURCE_LABEL,
 "donors": [ACTUAL_CLONE_LABEL_0, ACTUAL_CLONE_LABEL_1,
            ACTUAL_CLONE_LABEL_2, ACTUAL_CLONE_LABEL_3],
 "H_edges": [[ACTUAL_HELPER_LABEL, ACTUAL_HELPER_LABEL], ...]}
```

Old donors lie in15552..16415; newZ=16416; every H endpoint is one of these
five labels. All16416 old labels stay unchanged in the final16417 graph.
The proof's base16412 is only a conceptual induced subgraph.

The checker parses accepted C and the complete candidate once each. It
uses the already accepted864 role table only for donor-to-original-center
labels, not neighborhood masks. From actual C adjacency it derives N_v,
the saturated original pin set, all four forced owners and every required
donor-edge deletion. It checks frozen donor N against the original induced
center N directly. Expected delta is exactly old C minus those edges,
plusZ-N_v plusH; all other860 clones and original G edges remain intact.
All H degrees and complete final degree<=16 are checked, retaining legal
degree14 shared pins.

Planned BFS is only on the ACTUAL NEW candidate: four donors, Z, then fixed
old0, at most6 roots. Stable base D4 follows from the source retraction,
five helper rows cover all other pairs, and old0 supplies a genuine4-walk.
No old all-root/sourceD4/field/Lean/ARIS run, no producer coverage import,
and no sequential helper-prefix assertion occurs.

The code has not been executed or runtime-tested during preparation.
No RESULT/TERMINAL PASS is created unless ROOT authorizes an actual run.
If the search has no candidate, this folder remains unused.

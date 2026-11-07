# What the construction figures show

The figures explain four construction ideas using an exact small example and schematics of the larger constructions. ARIS renders the English and Chinese manuscripts with its academic template; the pages embed their figures and interaction for offline reading.

## A. Preserved-edge filling: an exact small example

Start with the cube on vertices 0–7. Two vertices are adjacent when their three-bit labels differ in one bit. The source has maximum degree 3 and diameter 3. The demonstration imposes limits **Δ ≤ 4, D ≤ 3**.

| Display step | Added neighbors | Current vertices covered by the latest pins' radius-two balls | Final maximum degree | Final diameter |
| --- | --- | ---: | ---: | ---: |
| One pin | x → {0} | 7/8 | 4 | 4 |
| Complementary pins | x → {0,7} | 8/8 | 4 | 3 |
| Reuse exhausted pins | x → {0,7}, y → {0,7} | 9/9 | 5 | 3 |
| Reallocate the choice | x → {0,7}, y → {1,6} | 9/9 | 4 | 3 |

The [figure generator](../tools/plot_constructions.py) computes these small graphs' degrees and distances exactly, and writes the [demonstration data](../data/construction_demo.json). No large graph is regenerated to animate the page. The four controls switch between the rendered examples.

The general extension argument is: if the old graph has diameter at most D, all old edges remain, the new vertex has at most Δ neighbors, every selected neighbor has spare degree, and their radius-(D−1) balls cover **every current vertex**, then the new graph still satisfies both limits. The last example deliberately includes the earlier new vertex x among the vertices to cover. This is the condition used in the recorded D5 sequences; the cube is an explanatory example of that condition, not a reconstruction of a record-size graph.

## B. Controller and finite-field fibers: the 3,840-vertex source

The saved [literal parameters](../reproduce/late_graphs/materials/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PARAMETERS.json) and [generator](../reproduce/late_graphs/materials/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/generate.py) use 60 controller states and F₄³ at each state. Thus there are **60 × 64 = 3,840** vertices. Five ports each contribute four affine neighbors, giving degree **20**.

For a given control edge, the relation is y = Aₑx + λbₑ, with λ ∈ F₄. Along a three-step control route, full rank of the three propagated direction vectors makes the 4³ parameter choices cover the target fiber. This explains one coverage mechanism; adjacent-layer cases additionally require complementary plane covers. Shared-edge compatibility is part of the full construction. The picture shows a local controller neighborhood and two schematic 64-point coordinate layers, not the full C60 embedding or its literal affine matrices.

## C. Connection reallocation: 7,531 → 7,532

The accepted 7,531-vertex graph starts from a filled 7,242-vertex source and 289 clones. Among the clones, 17 correspond to incident flags and have a connection to their associated filler. The new rule removes those **17 clone–filler edges** and inserts **17 hub–filler edges**, introducing one hub. Thus the graph has **7,532 vertices and the same 97,750 edges**.

Each removed connection c–f has a two-step replacement c–a–f with a suitable old flag a. This explains why it is possible to free that connection. The complete argument separately covers all original-vertex, clone, filler and hub pair types; replacing one edge by two steps alone would not establish the global diameter bound.

The figure draws three of the 17 role groups. The source H is retained; the changed edges belonged to the clone extension of H. Relevant material:

- [Preserved construction/proof draft](records/d26_D3_n7532_PROOF_DRAFT.md), copied from the actual research directory. Its historical final paragraph describes the producer-stage status, before the later release.
- [Frozen numerical parameters](../reproduce/late_graphs/materials/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/PARAMETERS.json).
- [Final release record](records/d26_D3_n7532_ROOT_GRAPH_RELEASE.json), including the subsequent verification and concrete Lean status.

## D. Extend a full-degree source: 2,566 → 2,567

The [new figure](../assets/construction_d10_d4.png) shows the final step of the (10,4) construction. The source is already 10-regular, so each attachment point first needs a free degree slot. Delete these five disjoint source edges:

```text
(193,2362), (192,2363), (417,2555), (2508,2565), (2511,2528)
```

Add vertex **2566** and join it to all ten endpoints. Every endpoint loses one edge and gains one; the new vertex has ten neighbors. The graph therefore remains 10-regular, with **2,567 vertices and 12,830 − 5 + 10 = 12,835 edges**. No further 2-switch is needed at this final step; earlier stages of the source chain used switches.

This adapts route-preserving extension to a source with every degree slot already occupied. Degree bookkeeping alone does not establish the diameter: removing edges can change old-to-old routes, while the new vertex must also reach the entire graph within four steps. Independent all-root BFS on the final graph confirmed diameter exactly 4, and the complete original-statement Lean proof passed. The [portable construction package](../reproduce/d10_d4/) provides the actual edge cuts, deterministic replay and preserved verification records. The diagram is a schematic of those changes, not a drawing of all 2,567 vertices.

## Display reproduction

From this case directory, with the existing Python/Matplotlib environment:

```bash
python3 tools/plot_results.py
python3 tools/plot_constructions.py
python3 tools/render_index.py
```

The last command uses only the Python standard library. Edit `README.md` for the English case and `README.zh-CN.md` for its Chinese translation. The adapter in `tools/render_index.py` uses the repository's ARIS Markdown parser and academic template, adds the interactive illustrations, and embeds their assets. The resulting `index.html` and `index.zh-CN.html` can each be opened by themselves. Download links point to the accompanying case files.

The original ARIS renderer, academic template and license are also included under `tools/aris-render-html/`, allowing the same command to work after extracting this case on its own. The footer records the manuscript path and actual generation time. Source fingerprints are omitted in accordance with the project owner's preference.

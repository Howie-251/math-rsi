# Why attachment-only repair cannot complete the new 26-bad-pair graph

Date: 2026-10-11. This is a concrete failure analysis of the new order-59
candidate, not an exclusion of arbitrary HS rewiring or arbitrary graphs.
All labels here use the original order-60 graph, with vertex41 deleted.

Take the original HS50 core on vertices0..39 and50..59. The remaining nine
vertices are40,42..49. Relative to this HS core, the new26-bad-pair graph
has exactly these old–old edits:

- delete edge50–55;
- add edges9–14 and38–55.

Its old induced graph has176edges. Vertices9,14,38 have old degree8 and
therefore **no ports for new neighbors** in any eight-regular completion
that keeps this old induced graph. Vertex50 has two ports; the other46old
vertices have one. The auxiliary graph has12edges, with three vertices of
degree2 and six ofdegree3; it is the retained Petersen graph minus vertex41.
The total available old-to-new incidences is48 on both sides.

In the actual old induced graph, the pairs9–55 and14–55 are nonadjacent and
have no common old neighbor. They cannot acquire a new common neighbor
either: vertices9and14 already use all eight degree slots on old vertices.
Consequently **every completion retaining this old induced graph has at
least these two uncovered pairs**, regardless of the new–new graph or
the choice of old-to-new attachments.

This also follows directly from the HS structure. Vertices9,14,38,55 were
four distinct neighbors of50. The added9–14edge consumes both endpoint
ports. Deleting50–55 removes the unique old two-step paths55–50–9 and
55–50–14. The new edge38–55 cannot restore either path, because distinct
HS neighbors of50 are nonadjacent;9–14 also does not restore them.

Thus a solver that only releases attachments or the nine-point auxiliary
graph would be solving an already obstructed input. Further constructive
work on this seed must change its old induced graph as well. The completed
24-state26-energy two-switch component proves that a nonworsening
two-switch path alone cannot lower its bad-pair count and therefore cannot
reach a diameter-two graph from this seed. Neither observation rules out other edits or other initial cores.

The exact old/new partition, edits, port degrees, auxiliary graph and
uncovered pairs were recomputed directly from the saved expanded edges:
`computations/dd82/construction/twin59_neutral_component_run/component.path2.old_core_obstruction.json`.
This short argument needs no additional SAT, enumeration or Lean work.

# Conditional SingleExtension proof for16417

This text is an unexecuted preparation template. It applies only after the
fresh literal checker binds an actual16417-vertex, {{M}}-edge graph to the
accepted16416 source and the selected {{K}} pins. No candidate is assumed
to exist when this template is written.

The accepted source is the complete graph_d16_D4_n16416.edges. Its closed
concrete target is
DegreeDiameter.Portfolio.F3Graph15552.Clone16416.d16_16416 in
formal/DegreeDiameter/Portfolio/F3Graph15552Clone16416Exact.lean, with its
standalone Audit and external label binding already accepted. It supplies
genuine Walk diameter at most4. No oldBFS, field or Lean module is rerun.

The new literal checker binds all129240 old edges exactly and permits only
the new label16416 to have new edges, precisely to S. Thus it is
DegreeDiameter.Portfolio.singleVertexExtension H S under the label mapping
some v -> v and none ->16416. Every old degree is d_H(v)+1[v inS], and the
new degree is |S|<=16. The actual checker verifies all degrees<=16 and that
every selected old pin had one free slot.

The checker performs one ordinary BFS from newZ on the actual final file.
A shortest predecessor path cannot revisit newZ. Dropping its first edge
therefore gives an old-source Walk from a selected pin to every old target
of length at most3. OLD_R3_PARENT_DEPTH.tsv gives this finite certificate:
depth(v)=distance_from_Z(v)-1, depth-zero vertices belong to S, and each
positive-depth old vertex has a source-adjacent old parent of depth one
less. The finite labels, actual source edges and candidate binding make
this a genuine PinsCoverRadius H S 3 certificate; it is not an assumption
that maximum-graph paths survive arbitrary vertex deletion.

Apply DegreeDiameter.Portfolio.singleVertexExtension_diameter
(module SingleExtension.lean), with
D=4 and r=3: all old-old pairs retain a source Walk<=4; new-old pairs use
Z-pin followed by an old Walk<=3; reversed walks cover old-new; the new
vertex to itself has the empty walk. This proves all-pairs diameter<=4
without all-root BFS. There are no future helper vertices in the proof.

The old false-twin collapse argument MUST NOT be reused: S is arbitrary,
so this extension may shorten some old distances, including old witnesses.
Instead one preselected old root0 is measured on the NEW final graph and
an actual shortest4-walk is saved. This directly proves non-D3. The newZ
BFS also saves a4-walk. Equivalently the Moore radius3 bound at maximum
degree16 is1+16+240+3600=3857<16417, so the proven upper4 cannot be3.

Exactly two candidate-graph BFS roots are planned: newZ and old0; no
source-only root or all-root suite is performed. New concrete Lean,
priority, reviews, counts and ROOT release are separate subsequent tasks.

# Can complete source proofs share controller rows?

This is a new finite structural question on the already recovered192x5
controller transition table. It does not generate another controller,
field or graph, and does not repeat a distance/rank computation.

The source is not transitive under port-preserving controller permutations:
type0 fixes controller0 but does not fix controller1. Thus one row cannot
automatically supply every row. The falsifiable useful prediction is weaker:
there is a nonidentity permutation h satisfying, for every a,p,

    h(controller(a,p)) = controller(h(a),p).

Such h lifts to a source automorphism (a,x)->(h(a),x), because all five
affine maps and constants depend only on p. Equal global labels and the
simple-graph deletion convention are preserved. One proved controller row
therefore supplies every row in its orbit, for arbitrary targetcontroller
and coordinate. This could reduce the remaining exact kernel workload.

For each of the192 possible images h(0), propagate the forced images along
the five transitions. Reject on the first consistency or injectivity
conflict. A complete bijective mapping is saved with its960 exact
commutation equations; report its point orbits. If the controller component
is all192, this enumerates the complete centralizer: any such permutation
is determined by h(0). A trivial outcome pauses this compression idea only;
it does not exclude automorphisms that also alter ports or fiber coordinates.

Budget: one process <=5CPU seconds; existing960 arcs only. No graph-body
reads, BFS, matrix/field/rank/solver/Lean, queries, seeds or retries. Return
actual accepted permutations, exact forced conflicts for rejected images,
orbit representatives, and the resulting concrete proof-work decision.

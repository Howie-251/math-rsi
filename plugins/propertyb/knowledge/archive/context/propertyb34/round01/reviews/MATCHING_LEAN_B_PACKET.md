# Scoped B review: actual eight-lock selection at 24 vertices

Target of this review is the actual input bridge, not the full T34 theorem.
Read and independently translate these declarations and their assumptions:

1. `formal/Aris4Math/ThirtyFour/WeightedThreePartition.lean`.
2. `formal/Aris4Math/ThirtyFour/TwentyFourMatchingSelection.lean`, especially
   `exists_eight_matching_locks` and `exists_eight_matching_vertices`.
3. `formal/Aris4Math/ThirtyFour/LockRelabel.lean`.

For the selected vertices, inspect whether all required degree and pair
codegree properties are proved from the same original simple five-uniform
hypergraph with 34 edges. Check all inequalities used to count the available
color classes, inclusion of lower-degree vertices, distinctness, and the
claim about endpoints of nonunit pairs. Try to falsify a claim before
accepting it. Consult defining dependencies as needed.

For relabeling, independently determine the direction of the permutation
and image of a type. Check the proof preserves all actual edge
multiplicities of H. The selected-lock position layout will be supplied by
its separate probability caller; this lemma itself only transports counts.

Existing build evidence:
`context/propertyb34/round01/twentyone-lean/build-queue-TwentyFourMatchingSelection-r10.log`
and `build-queue-LockRelabel-r8.log` in the same directory. Read these as
existing logs, not as your own executions. Selection is compiled; complete
24-point local classification and coloring assembly remain open.

Apply HERO: report genuine correctness/interface issues with concrete
locations and reasons. Do not invent a generic checklist or demand unrelated
infrastructure. State files actually read, whether any commands ran, actual
remaining mathematical obligation, and a scoped verdict. Read only.

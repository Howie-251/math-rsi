# Actual7242 statement alignment — new parameter scope

Original: ../PARAMETERS.json, ../PROOF.md and ../EXTENSION_STEPS.json. This is
the fixed W(3,4) GQ(4,4) opposite graph with all17 original Desarguesian spread
vertices. No claim about global novelty, arbitrary fields or existence of a
geometry for every a,b is made.

Read actual definitions:
- formal/DegreeDiameter/Portfolio/OppositeIncidenceSpreadSlots.lean: Inc,graph,
  forward; Family.lean: order_degree_and_exact_D3 is an explicitly CONDITIONAL
  reusable interface, not a concrete7242 proof.
- formal/DegreeDiameter/Portfolio/OppositeGQ44SpreadDefinitions.lean: typed
  linePoint85×5,pointLine85×5,spread17,spreadOwner85,Inc,oldEquiv,old,graph,label,
  old_label,label_old,label_new and FinalClaim. This module actually PASSed.
- Existing OppositeGQ35SpreadGeneric.graph's four cases are unchanged and reused.

Point IDs are PARAMETERS'85 lexicographic normalized GF4 four-tuples: multiply
by the inverse of the first nonzero coordinate to make it1. Lines are the85
lexicographically ordered ascending five-point-ID tuples. The formal incidence
relation is literal membership in those exact five entries. The graph does not
reinterpret GF4 as ZMod4; it uses these fixed literal incidences directly.
Spread order is exactly [21,26,31,36,57,54,67,64,77,82,71,76,49,46,43,40,0].
It must not be sorted to line order: new j is labeled7225+j, corresponding to
that original ordered spread entry. Owner is the original85-element index list.

Actual carrier is Fin7225⊕Fin17. `oldEquiv` is the explicit correspondence to
Fin85×Fin85 with old label85*p+l. `label` is the explicit equivalence to
Fin7242; label_old is identity and label_new=7225+j, all proved rfl.
Expanded graph:
- old u,old v iff distinct and Inc(point u,line v) and Inc(point v,line u);
- old u,new j (and reverse) iff Inc(point u,line u) and Inc(point u,spread j);
- new,new False.

FinalClaim is the closed proposition:
card Vertex=7242 ∧ (∀v,graph.degree v≤25) ∧ DiameterAtMost graph3 ∧ ¬D2.
This is presently a target definition, NOT a proved concrete theorem.
DiameterAtMost is the existing true SimpleGraph.Walk length bound.
The final actual theorem must discharge every conditional family hypothesis.

INPUT_BINDING_CHECK.json is actual readback:850 typed incidence entries,
17 ordered spread IDs,85 owner indices,425 ordered pin labels at the same
EXTENSION_STEPS indices; old85*p+l/new7225+j. Direct formula enumeration equals
all90525 literal edges with zero distance traversals. This is an external input
binding, not an ASCII-parser theorem or another independent acceptance.

Highest open interfaces:
1. actual pointLine coverage and soundness, actual unique spread owner;
2. all7225 point-line projections via per-row threeFin5 indices: q in target
   line, m among pointLine(p), q in m. First two incidences use definitions and
   shared pointLine_sound; one actual point equality per pair remains;
3. generic family caller witha=b=5 and the closed cardinal threshold, then
   final concrete theorem + executed independent import/type/axiom audit.
Rows00/84 will be measured first; remaining batch is not started yet.
New total budget1000CPU including already-PASS6.322335CPU generic work,
permodule115CPU initially singleworker. No old source/cache rebuild, BFS,
solver, installation, hashes,native_decide or unproved axioms.
A new-scope external alignment is pending root coordination; local proof work
continues independently of any model verdict.

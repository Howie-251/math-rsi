# GQ160050 final checkpoint C: actual closed theorem and import audit

Read actual definition bodies and the exported type before this summary. This
is the fixed GQ(7,7) instance; prior7242/6160 review verdicts do not cover it.

Final entrypoint:
`formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadExact.lean`.
Actual declaration:
```
DegreeDiameter.Portfolio.OppositeGQ77Spread.concrete_order_degree_and_exact_D3 :
  Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```
No input, geometry, projection, capacity or success hypothesis remains on it.
`final_claim : FinalClaim` is the same proposition. DiameterAtMost is the
project's actual Walk-length definition, not a numerical success predicate.

Actual definitions:
- `OppositeGQ77SpreadDefinitions.lean`: carrier Fin160000⊕Fin50, typed Inc
  membership, graph body, oldEquiv and label equivalence to Fin160050.
- `OppositeIncidenceSpreadSlots.lean`: generic Inc and graph wrapper.
- `OppositeGQ35SpreadGeneric.lean`: actual graph cases (cross-incidence between
  distinct old pairs; flag+spread incidence for old-new; no new-new edges).
All these Portfolio paths begin `formal/DegreeDiameter/Portfolio/`.
Old(p,l) has label400*p+l; newj has160000+j. The theorem is on the Sum carrier
with an explicit Fin label equivalence, not a separately transported Fin graph.
The field explanation is external; Lean uses the actual literal incidence graph,
without a ZMod49 substitution or a field-existence premise.

Concrete caller closure:
- IncidenceData/Chunk0..7/Incidence kernel-check all6400 positive inverse-position
  equalities, cover all Fin400 labels via the actual8×50 index equivalence, and
  check all50×8 owner entries. The two initial elaboration failures were fixed;
  their archived logs are historical, not accepted theorem dependencies.
- InputInterface proves the projection-to-Inc bridge. Every InputRow000..399
  actually compiles its400 finite equalities. Inputs closes the universal
  quantifier over all400 original point labels. No representative-row assumption
  is used by the final caller.
- Exact applies the unchanged arbitrary-a,b Family theorem at8,8 and supplies
  every actual hypothesis. Shared Slots proves degree≤64; shared Walks supplies
  D3; shared LowerGeneric proves non-D2 from the finite-neighbor bound4161<160050.

Actual execution evidence, in this formalization directory:
- FINAL_COMPILE_RESULT.json: all415 current modules exit0.
- OppositeGQ77SpreadInputs.log and its RESULT: universal finite assembly.
- OppositeGQ77SpreadExact.log and its RESULT: actual unconditional theorem.
- OppositeGQ77SpreadAudit.log and its RESULT: a separate process imports Exact,
  prints the actual graph/type/body and transitive axioms.
The final theorem and final_claim depend only on
`[propext, Classical.choice, Quot.sound]`; no sorryAx/native_decide/new axiom.
All Lean attempts, including the2 historical failed elaborations, measured
6240.278580CPU of15000. Old graph/generic sources and cache were not changed or
rebuilt. No old/full-source BFS, solver, install or hash was run.

INPUT_BINDING.md and INPUT_BINDING_CHECK.json give exact readback of6400
incidence entries,50 original spread labels,400 owners,160000 ordered triples,
all50×64 ordered pins, and every5121600 literal formula edge. Blocking is20×20
row-major lookup of the same Fin400 label, with no permutation. The owner lookup
also equals actual spread membership at each point. This is explicit external
correspondence, not an ASCII-parser theorem or independent graph acceptance.

The observed Python status-file publication race and its recovery are separately
retained in batch_history/; it caused no Lean row failure or recompilation of
the217 already PASS rows. Metadata publication became atomic and only183
unfinished rows were resumed under the same CPU limit.

Root owns A/B/C raw records and dispositions. B198 actually PASSed the finite
connection at its stated scope; it is not final C. This file is the new final-C
packet after actual kernel and import completion. Global record/priority remains
uncertified; Lean validity does not establish novelty.

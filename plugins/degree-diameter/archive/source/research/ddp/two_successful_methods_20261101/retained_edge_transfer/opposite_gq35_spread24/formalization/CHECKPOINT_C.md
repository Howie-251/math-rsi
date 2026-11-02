# Actual final6160 theorem — fresh final scope

Kernel completion is now actual. This is a final-source review, not a plan or
continuation of the architecture-only B verdict. Original target is unchanged
from A: the literal fixed Payne-GQ GF4 opposite graph plus the16 original
vertical-spread vertices; actual labels old96*p+l,new6144+j.

Read original ../PARAMETERS.json, ../PROOF.md and INPUT_BINDING_CHECK.json.
Do not print large numeric tables or rerun any solver/BFS. Read actual sources:
- formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadGeneric.lean: graph's4cases;
- OppositeGQ35SpreadDefinitions.lean: actual original line/pointLine arrays,
  Inc,spread,spreadOwner,oldEquiv,old,graph,label,all3 label theorems,FinalClaim;
- OppositeGQ35SpreadFastTables.lean: all384linePoint+384pointLine values are
  kernel-equal to evaluation tables. Original graph definitions were not changed;
- OppositeGQ35SpreadIncidence.lean: all384 positive-incidence coverage checks,
  all64 spread-owner checks, symbolic return to original Inc;
- OppositeGQ35SpreadInputData.lean,InputChecks.lean: chosen6144 point-line
  projection witnesses; each row's3 explicitFin4 indices imply actual Inc;
- OppositeGQ35SpreadInputRow00.lean through InputRow63.lean and Inputs.lean:
  all64 current row modules have exit0, then inputRows exhausts Fin64 and
  projection supplies the original ∀p l,∃q m,Inc q l∧Inc p m∧Inc q m premise.
  No witness/certificate premise is exported to the user. Read representative
  bodies and actual receipts; no need to transcribe6144 numeric entries;
- OppositeGQ35SpreadWalks.lean: weak-edge equality compression→true Walk≤3;
- OppositeGQ35SpreadSlots.lean: old self slot becomes unique new owner, other
  slots give raw old opposite-incidence output; all neighbors are covered by
  4×6 positions. Coverage suffices, distinctness/adjacency of every output is
  not assumed or claimed;
- OppositeGQ35SpreadLowerGeneric.lean: actual Walk≤2 classification + finite
  endpoint surjection gives card≤1+k+k²;
- OppositeGQ35SpreadDegree.lean: actual forward Fin24,forward_covers and degree;
- OppositeGQ35SpreadDiameter.lean: actual projection caller gives D3;
- OppositeGQ35SpreadLower.lean: actual forward caller gives6160≤601 contradiction;
- OppositeGQ35SpreadExact.lean: final unconditional assembly;
- formal/OppositeGQ35SpreadAudit.lean and its actual log: independent import,
  original definition bodies, label types, actual final type/body and axioms.

Final entry declaration, now compiled:
DegreeDiameter.Portfolio.OppositeGQ35Spread.concrete_order_degree_and_exact_D3 :
 Fintype.card Vertex=6160 ∧ (∀v,graph.degree v≤24) ∧
 DiameterAtMost graph3 ∧ ¬DiameterAtMost graph2.
`final_claim : FinalClaim` is also proved. DiameterAtMost is the existing
SingleExtension definition in terms of genuine SimpleGraph.Walk and length.
Carrier is Fin6144⊕Fin16; label is its explicit equivalence to Fin6160, with
proved old identity and new6144+j. A transported SimpleGraph(Fin6160) is not
separately claimed. Exact degree24/edge count are external producer/independent
results; Lean proves the requested upper degree bound.

Actual final logs/receipts in this directory:
- OppositeGQ35SpreadInputs/Degree/Diameter/Lower/Exact/Audit.log and _RESULT.json:
  all exit0; final ExactCPU1.965, separate AuditCPU1.963;
- INPUT_BATCH_RESULT.json: all60 remaining rows complete, plus already-PASS
  00/01/62/63; every actual point-line pair is kernel checked;
- FINAL_COMPILE_RESULT.json:79 current-module receipts, exact final type and
  axioms exactly propext,Classical.choice,Quot.sound; no sorryAx/extra axiom;
- finite all attempts678.621700CPU<750; other proof/definition work including
  conservative old timing overcount63.413667<450; total742.035367<1200.
No old F4 module changed/rebuilt. No BFS/solver/install/hash/native_decide.

INPUT_BINDING_CHECK is actual external readback of all768 original entries,
all16 ordered spread steps and all384 ordered pin labels, new6144+j at the same
index. Direct formula neighbors equal the73920-edge literal graph;0 distance
traversals. This is not an ASCII-parser theorem or an independent acceptance.
The separate independent literal checker has actually PASSed all6160 roots.
A was SUCCESS/PASS; B was SOUND ARCHITECTURE with finite discharge then pending.
Neither previous verdict is silently upgraded to this completed new final scope.
Global novelty remains UNCONFIRMED regardless of Lean/legal graph completion.

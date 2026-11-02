# 6160 key proof connections — compiled scope

Read original PROOF.md, CHECKPOINT_A.md, actual Generic/Definitions, and:
- OppositeGQ35SpreadWalks.lean: diameter_three, compiled PASS; projection
  supplies actual old-old, old-new and new-new3-step chains. Consecutive equal
  vertices are suppressed using real0/1-length Walks then append. No dummy
  adjacency self-loops or path certificates are assumed in the upper-bound proof.
- OppositeGQ35SpreadSlots.lean: slot,slot_covers,degree_le_of_cover, PASS.
  Old slots(q on old l,m through old p) normally give old(q,m); exactly when
  that equals the source old vertex, the slot instead points to owner(p)'s new
  spread vertex. No exact-degree arithmetic is assumed. Coverage is enough.
- OppositeGQ35SpreadLowerGeneric.lean: diameter_two_card_le, helper actual PASS
  in lower_helper/. Genuine Walk≤2 is split into0/1/2 edges. A finite endpoint
  map from((Unit⊕Fin k)⊕(Fin k×Fin k)) is surjective, giving1+k+k².
- OppositeGQ35SpreadFastTables.lean:768 original lookup entries equal alternative
  evaluation tables, both universal equalities PASS42.008CPU. Graph bodies and
  original literal arrays remain unchanged.
- OppositeGQ35SpreadIncidence.lean: pointLine_inverse checks just384 positive
  line incidences, spread_owner_on_rows checks64 spread entries. These give
  universal pointLine_covers_literal and spread_unique_literal, actual PASS.
- OppositeGQ35SpreadInputChecks.lean: each projection needs three explicitFin4
  indices, checked as equalities, and inputRow_of_checks returns actual InputRow.
- OppositeGQ35SpreadInputRow00.lean: actual row0 PASS6.160CPU in the current
  representation; exactly96 point-line projections. The other rows are an
  ongoing bounded batch, not a completed universal6144-pair result yet.

INPUT_BINDING_CHECK.json is actual readback:384 line-point and384 point-line
entries equal PARAMETERS in order; all16*24 ordered pins equal every produced
EXTENSION_STEPS entry at its original index; old96*p+l and new6144+i labels.
A direct formula-neighbor enumeration equals all73920 literal edges. This is
input binding with zero distance traversal, not another independent validation.
Independent literal6160-root acceptance has separately PASSed; do not conflate
it with the Lean finite row proofs or call this binding an ASCII-parser theorem.

Highest remaining connection: all64 current row proofs assembled to `projection`
and actual slot coverage caller, then unconditional Exact and separate Audit.
The current Exact source is the intended assembly but has not yet compiled.
A and this B are new6160 scopes; prior F4/clone reviews do not cover them.

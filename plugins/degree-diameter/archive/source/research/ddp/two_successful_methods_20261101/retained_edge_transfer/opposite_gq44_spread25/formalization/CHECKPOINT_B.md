#7242 actual key connections and initial row checks

Scope: new generic wrapper/family + actual W(3,4) typed literals and the
three-index projection bridge. Original6160 Generic/Walks/Slots/LowerGeneric
are unchanged and imported from their already-PASS caches. No old rebuild.

Actual compiled sources:
- OppositeIncidenceSpreadSlots.lean: Inc equals linePoint membership; graph
  retains old labels through e:V≃P×L. Generic Fin(a*b) forward and neighbor
  coverage→degree≤a*b apply the original self-slot/bonus argument. The output
  need only cover actual neighbors; distinctness/adjacency of all outputs is
  not assumed or claimed.
- OppositeIncidenceSpreadFamily.lean: conditional cardP*cardL+cardJ, degree,
  trueWalkD3 and nonD2 interface. Explicit hypotheses: pointLine covers every
  Inc; actual spread incidence j forces j=owner(p); positive a; every point-line
  pair has(q,m) with q∈l,p∈m,q∈m; order>1+ab+(ab)^2. Nonempty of the graph
  needed by the generic lower lemma is derived from that cardinal inequality.
  This does not assert existence of geometries for arbitrary a,b or fields.
- OppositeIncidenceSpreadAudit.lean: actual separate import/type/axiom audit;
  all3 modules PASS6.322335CPU, standard3 axioms.
- OppositeGQ44SpreadDefinitions.lean: actual typed original850 incidence
  entries,17 spread IDs and85 owner indices, Sum Fin7225 Fin17, label Fin7242,
  old85*p+l/new7225+j. Actual PASS2.867420CPU. FinalClaim is only a target here.
- OppositeGQ44SpreadIncidence.lean: actual pointLine_inverse and pointLine_sound
  each425 positive checks; spread_owner_on_rows85 positive checks. Symbolic
  return yields original Inc coverage/soundness and unique owner. PASS27.950719CPU.
- OppositeGQ44SpreadInputInterface.lean: threeFin5 indices mean q's position on
  target l, common line m's position in pointLine(p), q's position on m. One
  equality checks q on m; q∈l is definitional and p∈m follows from the compiled
  pointLine_sound. projection_row_of_check returns actual original Inc facts.
  This module PASS1.894060CPU.
- OppositeGQ44SpreadInputRow00/84.lean: actual first/last rows PASS3.849872 and
  6.374317CPU. No universal7225-pair certificate is claimed until all rows
  and actual Inputs compile. The bounded83 remaining rows are running.

Projection indices derive exactly from ../PROJECTION_WITNESSES.json's6800
nonincident(q,m) pairs;425 incident cases use q=p,m=l. Kernel checks every
actual supplied equality and closes Inc; producer witness validity is not a
final exported hypothesis.
INPUT_BINDING_CHECK is actual source readback of all850+17+85 values, all within
Fin bounds;425 ordered pin labels equal each original extension step at the
same index. Direct formula neighbors equal all90525 edges, zero distance BFS.
This external readback is not an ASCII-parser theorem or independent acceptance.

Remaining: all85 row proofs→Inputs.projection→actual Family caller in Exact,
then independent Audit and fresh final scope review. Only the concrete final
assembly can establish the unconditional7242 claim. Global novelty unconfirmed.

import Aris4Math.ThirtyThree.TraceProfileBridge
import Aris4Math.ThirtyThree.EightClassification
import Aris4Math.ProfileApplication

/-! The fourteen eight-lock tables at 25 vertices and 33 edges.  Closed
arithmetic is checked by the kernel; every real input count is supplied by
TraceRecovery through TraceProfileBridge. -/

namespace Aris4Math.ThirtyThree.EightProfiles

open Aris4Math.TraceRecovery Aris4Math.ThirtyThree.TraceProfileBridge
open Aris4Math.TraceProfiles (tableCount)
open Aris4Math.ThirtyThree.EightClassification

/-- Eight central one-based positions 9 through 16. -/
def positions : Fin 8 ↪ Fin 25 where
  toFun i := ⟨i.val + 8, by omega⟩
  inj' := by
    intro i j h
    apply Fin.ext
    have := congrArg Fin.val h
    simp only at this
    omega

/-- Explicit positive rows, in the same label order as representative8. -/
def profile (k : Fin 14) : Numeric.Profile :=
  match k.val with
  | 0 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 8⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 14], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 15], 1⟩, ⟨[11, 16], 1⟩, ⟨[12, 13, 15], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 14, 16], 1⟩], none, []⟩
  | 1 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 8⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[15], 1⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 16], 1⟩, ⟨[10, 15], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 13, 16], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
  | 2 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 7⟩, ⟨[11], 1⟩, ⟨[12], 2⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 14], 1⟩, ⟨[10, 13], 1⟩, ⟨[10, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 14, 16], 1⟩, ⟨[12, 13, 16], 1⟩, ⟨[13, 14, 15], 1⟩], none, []⟩
  | 3 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 8⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 1⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 13], 1⟩, ⟨[11, 14, 15], 1⟩, ⟨[11, 16], 1⟩, ⟨[12, 14, 16], 1⟩, ⟨[12, 15], 1⟩, ⟨[13, 15], 1⟩, ⟨[13, 16], 1⟩], none, []⟩
  | 4 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 7⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11, 14], 1⟩, ⟨[10, 12], 1⟩, ⟨[10, 13, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 16], 1⟩, ⟨[11, 13], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 13], 1⟩, ⟨[12, 14, 15], 1⟩, ⟨[13, 14, 16], 1⟩], none, []⟩
  | 5 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 8⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 1⟩, ⟨[15], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 14], 1⟩, ⟨[11, 13, 15], 1⟩, ⟨[11, 16], 1⟩, ⟨[12, 15], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 16], 1⟩, ⟨[14, 16], 1⟩], none, []⟩
  | 6 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 7⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 2⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 13, 14], 1⟩, ⟨[11, 16], 1⟩, ⟨[12, 14, 16], 1⟩, ⟨[13, 15], 1⟩, ⟨[13, 16], 1⟩], none, []⟩
  | 7 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 8⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 1⟩, ⟨[14], 1⟩, ⟨[15], 1⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 14], 1⟩, ⟨[11, 13, 16], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 15], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 16], 1⟩], none, []⟩
  | 8 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 6⟩, ⟨[10], 2⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 1⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13], 1⟩, ⟨[9, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11, 13], 1⟩, ⟨[10, 12, 15], 1⟩, ⟨[10, 14, 16], 1⟩, ⟨[11, 12, 16], 1⟩, ⟨[11, 14, 15], 1⟩, ⟨[12, 13, 14], 1⟩, ⟨[13, 15], 1⟩, ⟨[13, 16], 1⟩], none, []⟩
  | 9 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 7⟩, ⟨[9], 1⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 2⟩, ⟨[14], 2⟩, ⟨[15], 1⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 14], 1⟩, ⟨[11, 13, 16], 1⟩, ⟨[11, 15], 1⟩, ⟨[12, 15], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 16], 1⟩], none, []⟩
  | 10 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 7⟩, ⟨[9], 1⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 1⟩, ⟨[13], 2⟩, ⟨[14], 1⟩, ⟨[15], 2⟩, ⟨[16], 1⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 13, 16], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 14], 1⟩, ⟨[12, 16], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 16], 1⟩], none, []⟩
  | 11 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 6⟩, ⟨[9], 1⟩, ⟨[10], 1⟩, ⟨[11], 1⟩, ⟨[12], 2⟩, ⟨[13], 2⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11], 1⟩, ⟨[10, 12, 13], 1⟩, ⟨[10, 14, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 13, 16], 1⟩, ⟨[11, 14], 1⟩, ⟨[12, 14, 16], 1⟩, ⟨[13, 15], 1⟩], none, []⟩
  | 12 => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 6⟩, ⟨[9], 1⟩, ⟨[10], 1⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 2⟩, ⟨[14], 2⟩, ⟨[15], 1⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11], 1⟩, ⟨[9, 12], 1⟩, ⟨[9, 13, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11, 13], 1⟩, ⟨[10, 12, 14], 1⟩, ⟨[10, 15], 1⟩, ⟨[10, 16], 1⟩, ⟨[11, 12, 15], 1⟩, ⟨[11, 14, 16], 1⟩, ⟨[12, 13, 16], 1⟩, ⟨[13, 15], 1⟩, ⟨[14, 15], 1⟩], none, []⟩
  | _ => ⟨25, [9,10,11,12,13,14,15,16], [⟨[], 5⟩, ⟨[9], 2⟩, ⟨[10], 2⟩, ⟨[11], 2⟩, ⟨[12], 2⟩, ⟨[13], 2⟩, ⟨[14], 2⟩, ⟨[15], 2⟩, ⟨[16], 2⟩, ⟨[9, 10], 1⟩, ⟨[9, 11, 12], 1⟩, ⟨[9, 13, 14], 1⟩, ⟨[9, 15, 16], 1⟩, ⟨[10, 11, 13], 1⟩, ⟨[10, 12, 15], 1⟩, ⟨[10, 14, 16], 1⟩, ⟨[11, 14, 15], 1⟩, ⟨[11, 16], 1⟩, ⟨[12, 13, 16], 1⟩, ⟨[12, 14], 1⟩, ⟨[13, 15], 1⟩], none, []⟩

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem numeric_counts : ∀ k : Fin 14, ∀ T : Finset (Fin 8),
    recoveredCount 33 6 (K6Classification.pairCompletion (representative8 k)) T =
      tableCount (profile k) (encode positions T) := by
  intro k
  fin_cases k <;> decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem table_certificates : ∀ k : Fin 14,
    Numeric.validProfile (profile k) 33 ∧ RowCertificate positions (profile k) ∧
    (profile k).v = 25 ∧
    (profile k).positions.toFinset = Finset.univ.image (fun i => (positions i).val+1) ∧
    (profile k).emptyPairCap = none ∧ (profile k).correctionCenters = [] := by
  unfold Numeric.validProfile
  intro k
  fin_cases k <;> decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem strict : ∀ k : Fin 14, Numeric.totalBound (profile k) < 1 := by
  intro k
  fin_cases k <;> decide +kernel

/-- A representative classification of the actual eight-point trace family
provides every needed probability input, with 33 total edges. -/
theorem propertyB_of_eight_family (H : Simple5Hypergraph (Fin 25))
    (S : Finset (Fin 25)) (label : ↥S ≃ Fin 8)
    (unit : H.UnitCodegrees S) (degrees : ∀ x ∈ S, H.degree x = 6)
    (edges33 : H.edges.card = 33) (k : Fin 14)
    (family : (H.multiTraces S).image (labelBlock S label) =
      K6Classification.pairCompletion (representative8 k)) : PropertyB H := by
  obtain ⟨valid,rows,vEq,posEq,noCap,noCorrection⟩ := table_certificates k
  have real := realizes_of_recovered_counts H S label unit degrees edges33
    (K6Classification.pairCompletion (representative8 k)) family positions
    (profile k) valid vEq posEq (rowData_of_certificate _ _ rows) (numeric_counts k)
  exact ProfileApplication.propertyB_of_uncorrected_profile H (lockVertices S label)
    positions (profile k) real noCap noCorrection (strict k)

end Aris4Math.ThirtyThree.EightProfiles

#print axioms Aris4Math.ThirtyThree.EightProfiles.numeric_counts
#print axioms Aris4Math.ThirtyThree.EightProfiles.strict
#print axioms Aris4Math.ThirtyThree.EightProfiles.propertyB_of_eight_family

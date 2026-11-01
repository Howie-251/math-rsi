import Aris4Math.ThirtyThree.TraceProfileBridge
import Aris4Math.ProfileApplication

/-! The three six-lock representatives containing a block of size at least four,
with their actual 33-edge multiplicities and strict probability bounds. -/

namespace Aris4Math.ThirtyThree.SixLargeProfiles

open Aris4Math.TraceRecovery Aris4Math.ThirtyThree.TraceProfileBridge
open Aris4Math.TraceProfiles (tableCount positions25)
open Aris4Math.K6Classification

/-- Indices 6,7,8 in the analytic six-point classification. -/
def index (k : Fin 3) : Fin 9 := ⟨k.val+6,by omega⟩

/-- Increasing the edge total affects only the empty trace. -/
def profile (k : Fin 3) : Numeric.Profile :=
  let p := TraceProfiles.profile25 (index k)
  {p with types := p.types.map fun t =>
    if t.locks = [] then {t with count := t.count+1} else t}

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem numeric_counts : ∀ k : Fin 3, ∀ T : Finset (Fin 6),
    recoveredCount 33 6 (fullRepresentative (index k)) T =
      tableCount (profile k) (encode positions25 T) := by
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem table_certificates : ∀ k : Fin 3,
    Numeric.validProfile (profile k) 33 ∧ RowCertificate positions25 (profile k) ∧
    (profile k).v = 25 ∧
    (profile k).positions.toFinset = Finset.univ.image (fun i => (positions25 i).val+1) ∧
    (profile k).emptyPairCap = none ∧ (profile k).correctionCenters = [] := by
  unfold Numeric.validProfile
  decide +kernel

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem strict : ∀ k : Fin 3, Numeric.totalBound (profile k) < 1 := by
  decide +kernel

theorem propertyB_of_six_family (H : Simple5Hypergraph (Fin 25))
    (S : Finset (Fin 25)) (label : ↥S ≃ Fin 6)
    (unit : H.UnitCodegrees S) (degrees : ∀ x ∈ S, H.degree x = 6)
    (edges33 : H.edges.card = 33) (k : Fin 3)
    (family : (H.multiTraces S).image (labelBlock S label) =
      fullRepresentative (index k)) : PropertyB H := by
  obtain ⟨valid,rows,vEq,posEq,noCap,noCorrection⟩ := table_certificates k
  have real := realizes_of_recovered_counts H S label unit degrees edges33
    (fullRepresentative (index k)) family positions25
    (profile k) valid vEq posEq (rowData_of_certificate _ _ rows) (numeric_counts k)
  exact ProfileApplication.propertyB_of_uncorrected_profile H (lockVertices S label)
    positions25 (profile k) real noCap noCorrection (strict k)

/-- Only the last three analytic representatives can contain a four-point block. -/
theorem index_large : ∀ k : Fin 9, (∃ B ∈ representative k, 4 ≤ B.card) → 6 ≤ k.val := by
  decide +kernel

theorem propertyB_of_large_trace (H : Simple5Hypergraph (Fin 25))
    (S : Finset (Fin 25)) (six : S.card = 6)
    (unit : H.UnitCodegrees S) (degrees : ∀ x ∈ S, H.degree x = 6)
    (edges33 : H.edges.card = 33)
    (large : ∃ B ∈ H.multiTraces S, 4 ≤ B.card) : PropertyB H := by
  obtain ⟨B,hB,four⟩ := large
  have good : ¬ Avoidance.TwoTripleShape (H.multiTraces S) := by
    intro bad
    have small := bad.1 B hB
    omega
  obtain ⟨k,_,_,label,largeFamily⟩ := K6Traces.classify_on_set S (H.multiTraces S) six
    (fun _ h => H.multiTraces_subset S h) (fun _ h => H.multiTraces_card_le_five S h)
    (fun _ hB _ hC ne => H.multiTraces_inter_card_le_one S unit hB hC ne) good
  have hl : labelBlock S label B ∈ representative k := by
    rw [← largeFamily]
    exact Finset.mem_image.mpr ⟨B,Finset.mem_filter.mpr ⟨hB,by omega⟩,rfl⟩
  have kge := index_large k ⟨labelBlock S label B,hl,
    by rw [labelBlock_card S label B (H.multiTraces_subset S hB)]; exact four⟩
  let j : Fin 3 := ⟨k.val-6,by omega⟩
  have jeq : index j = k := by apply Fin.ext; simp [index,j]; omega
  apply propertyB_of_six_family H S label unit degrees edges33 j
  rw [labeled_traces_recovered H S unit label]
  change pairCompletion ((largeBlocks (H.multiTraces S)).image (labelBlock S label)) = _
  rw [show (largeBlocks (H.multiTraces S)).image (labelBlock S label) = representative k
    from largeFamily,jeq]
  rfl

end Aris4Math.ThirtyThree.SixLargeProfiles

#print axioms Aris4Math.ThirtyThree.SixLargeProfiles.propertyB_of_large_trace

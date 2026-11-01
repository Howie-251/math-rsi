import Aris4Math.ThirtyThree.TwentyFourFiveMatchingData
import Aris4Math.ThirtyThree.TwentyFourSelection
import Aris4Math.ProfileApplication

/-! Probability caller and actual labeling for the five-low matching branch. -/
namespace Aris4Math.ThirtyThree.TwentyFourFiveMatching
open TwentyFourFiveMatchingData

/-- All genuine type multiplicities suffice; the finite numeric bound is
supplied by the module and cannot be an extra user premise. -/
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (k : Fin 18)
    (actual : ∀ T, MultiLockRecovery.count H vertices T = counts k T) : PropertyB H := by
  obtain ⟨valid,strict,noCap,noCorrection⟩ := certificates k
  have real := FiveProfiles.realizes_profile H vertices (positions k) (counts k) actual []
    (by simpa only [← p_eq] using valid)
  rw [← p_eq] at real
  exact ProfileApplication.propertyB_of_uncorrected_profile H vertices (positions k)
    (p k) real noCap noCorrection strict

def pairDegree (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} ∨ ({i,j} : Finset (Fin 5)) = {2,3} then 2 else 1

def lowData (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then 6 else
  if T = {0,1} ∨ T = {2,3} then 2 else 1

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovery_formula : ∀ k T,
    MultiLockRecovery.recovered lowData (counts k) T = counts k T := by decide +kernel

/-- It is enough for the structural classification to provide large traces;
the actual ordinary degrees and codegrees recover every smaller type. -/
theorem propertyB_of_large (H : Simple5Hypergraph (Fin 24))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 24)
    (degrees : ∀ i, H.degree (vertices i) = 6)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (k : Fin 18) (large : ∀ T, 3 ≤ T.card → MultiLockRecovery.count H vertices T = counts k T) :
    PropertyB H := by
  have hlow : ∀ T, T.card ≤ 2 → MultiLockRecovery.upperCount H vertices T = lowData T := by
    apply MultiLockRecovery.upper_eq_of_low_data H vertices lowData
    · simp [lowData,edges33]
    · intro i
      simp [lowData,degrees]
    · intro i j ij
      rw [pairs i j ij]
      simp [lowData,pairDegree,ij]
  apply propertyB_of_counts H vertices k
  intro T
  exact (MultiLockRecovery.actual_recovered H vertices lowData (counts k) hlow large T).trans
    (recovery_formula k T)

set_option maxHeartbeats 1000000 in
/-- The structurally selected five distinct vertices acquire the fixed
matching labels `(0,1)` and `(2,3)`, with no additional ordering assumption. -/
theorem exists_labeled (H : Simple5Hypergraph (Fin 24))
    (selected : TwentyFourSelection.FiveMatchingLocks H) :
    ∃ vertices : Fin 5 ↪ Fin 24,
      (∀ i, H.degree (vertices i) = 6) ∧
      (∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j) := by
  obtain ⟨a,b,c,d,e,ab,ac,ad,ae,bc,bd,be,cd,ce,de,degrees,
    cab,ccd,cac,cad,cae,cbc,cbd,cbe,cce,cde⟩ := selected
  let f : Fin 5 → Fin 24 := ![a,b,c,d,e]
  have inj : Function.Injective f := by
    intro i j eq
    fin_cases i <;> fin_cases j <;> simp_all [f,Ne.symm]
  let vertices : Fin 5 ↪ Fin 24 := ⟨f,inj⟩
  refine ⟨vertices,?_,?_⟩
  · intro i
    apply degrees
    fin_cases i <;> simp [vertices,f]
  · intro i j ij
    have cba := (H.codegree_comm b a).trans cab
    have cca := (H.codegree_comm c a).trans cac
    have cda := (H.codegree_comm d a).trans cad
    have cea := (H.codegree_comm e a).trans cae
    have ccb := (H.codegree_comm c b).trans cbc
    have cdb := (H.codegree_comm d b).trans cbd
    have ceb := (H.codegree_comm e b).trans cbe
    have cdc := (H.codegree_comm d c).trans ccd
    have cec := (H.codegree_comm e c).trans cce
    have ced := (H.codegree_comm e d).trans cde
    fin_cases i <;> fin_cases j <;>
      simp_all [vertices,f,pairDegree] <;> decide

end Aris4Math.ThirtyThree.TwentyFourFiveMatching
#print axioms Aris4Math.ThirtyThree.TwentyFourFiveMatching.exists_labeled
#print axioms Aris4Math.ThirtyThree.TwentyFourFiveMatching.propertyB_of_counts

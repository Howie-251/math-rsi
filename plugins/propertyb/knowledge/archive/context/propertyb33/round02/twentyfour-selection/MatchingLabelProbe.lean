import Aris4Math.ThirtyThree.FiveProfiles
import Aris4Math.ThirtyThree.TwentyFourSelection
namespace Aris4Math.ThirtyThree.TwentyFourFiveMatching
def pairDegree (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} ∨ ({i,j} : Finset (Fin 5)) = {2,3} then 2 else 1

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

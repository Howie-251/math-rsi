import Aris4Math.ThirtyThree.TwentyThreeThreeLowData
import Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog
namespace Aris4Math.ThirtyThree.ThreeLowRecoveryProbe
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeThreeLowData TwentyThreeThreeLowHighCatalog

def degreeData (i : Fin 5) : ℕ := if i.val < 3 then 6 else 7

def low (c : Case) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then (if 0 ∈ T ∨ 1 ∈ T ∨ 2 ∈ T then 6 else 7) else
  if T = {0,1} then lowExcess c 0+1 else
  if T = {0,2} then lowExcess c 1+1 else
  if T = {1,2} then lowExcess c 2+1 else
  if T = {3,4} then highCodegree c else 1

variable
 (recovery_formula : ∀ c T, recovered (low c) (counts c) T = counts c T)
 (pbCounts : ∀ (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) (c : Case),
  (∀ T, count H vertices T = counts c T) → PropertyB H)
include recovery_formula pbCounts

theorem propertyB_of_large (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 23) (c : Case)
    (degrees : ∀ i, H.degree (vertices i) = degreeData i)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) =
      pairDegree (lowExcess c) (highCodegree c) i j)
    (large : ∀ T, 3 ≤ T.card → count H vertices T = counts c T) : PropertyB H := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low c T := by
    apply upper_eq_of_low_data
    · simp [low,edges33]
    · intro i
      rw [degrees]
      fin_cases i <;> simp [low,degreeData]
    · intro i j ij
      rw [pairs i j ij]
      simp [low,pairDegree,ij]
  apply pbCounts H vertices c
  intro T
  exact (actual_recovered H vertices (low c) (counts c) hlow large T).trans
    (recovery_formula c T)

end Aris4Math.ThirtyThree.ThreeLowRecoveryProbe

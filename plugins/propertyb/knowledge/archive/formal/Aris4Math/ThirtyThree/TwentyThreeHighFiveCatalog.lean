import Aris4Math.ThirtyThree.TwentyThreeHighFiveData
import Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog

/-! Complete zero/one matching pair catalog, reusing the shared 55-trace domain. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighFiveCatalog
open scoped BigOperators
open TwentyThreeHighFiveData (extra catalog counts)
def largeTypes : Fin 16 → Finset (Fin 5) := ![{0,1,2},{0,1,3},{0,2,3},{1,2,3},{0,1,2,3},{0,1,4},{0,2,4},{1,2,4},{0,1,2,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem largeTypes_injective : Function.Injective largeTypes := by decide +kernel
theorem largeTypes_card : ∀ a, 3 ≤ (largeTypes a).card := by decide +kernel
theorem largeTypes_complete : ∀ T : Finset (Fin 5), 3 ≤ T.card → ∃ a, largeTypes a = T := by decide +kernel
def pairDegree (e : Fin 2) (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} then e.val+1 else 1
def lowData (e : Fin 2) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then 7 else
  if T = {0,1} then e.val+1 else 1
def highValue (h : Fin 16 → Bool) (T : Finset (Fin 5)) : ℕ :=
  if ∃ a : Fin 16, largeTypes a = T ∧ h a = true then 1 else 0
def pairSum (h : Fin 16 → Bool) (i j : Fin 5) : ℕ :=
  ∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then
    if h a then 1 else 0 else 0
def Admissible (e : Fin 2) (h : Fin 16 → Bool) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree e i j

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem catalog_reduce : ∀ e : Fin 2, ∀ r : Fin 55,
    Admissible e (TwentyThreeTwoLowHighCatalog.catalog r) →
    ∃ s : Fin 73, extra s = e ∧
      ∀ a, TwentyThreeTwoLowHighCatalog.catalog r a = catalog s a := by
  intro e r
  fin_cases e <;> fin_cases r <;> unfold Admissible <;> decide +kernel

theorem covers (e : Fin 2) (h : Fin 16 → Bool) (admissible : Admissible e h) :
    ∃ s : Fin 73, extra s = e ∧ ∀ a, h a = catalog s a := by
  have shared : TwentyThreeTwoLowHighCatalog.Admissible (e.val+1) 1 h := by
    intro i j ij
    have hb := admissible i j ij
    change pairSum h i j ≤ _
    apply hb.trans_eq
    unfold pairDegree TwentyThreeTwoLowHighCatalog.pairDegree
    split_ifs <;> rfl
  obtain ⟨r,hr⟩ := TwentyThreeTwoLowHighCatalog.covers (e.val+1) 1 h (by omega) (by omega) shared
  have eq := funext hr
  rw [eq] at admissible ⊢
  exact catalog_reduce e r admissible

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem catalog_counts : ∀ s T, 3 ≤ T.card → highValue (catalog s) T = counts s T := by
  intro s
  fin_cases s <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovery_formula : ∀ s T,
    MultiLockRecovery.recovered (lowData (extra s)) (counts s) T = counts s T := by
  intro s
  fin_cases s <;> decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeHighFiveCatalog

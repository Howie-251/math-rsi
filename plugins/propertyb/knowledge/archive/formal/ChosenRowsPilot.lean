import Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot

/-! A fixed certificate selects one valid A/B/C upper bound per position.
Only the selected expression has to be evaluated in each finite strict check. -/
namespace Aris4Math.ThirtyFour.CachedChosenRows
open CachedRows
open scoped BigOperators

def selected (a b c : ℚ) (choice : Fin 3) : ℚ :=
  if choice=0 then a else if choice=1 then b else c

theorem min_le_selected (a b c : ℚ) (choice : Fin 3) :
    min a (min b c) ≤ selected a b c choice := by
  fin_cases choice
  · exact min_le_left _ _
  · exact (min_le_right _ _).trans (min_le_left _ _)
  · exact (min_le_right _ _).trans (min_le_right _ _)

def bound {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3) : ℚ :=
  ∑ k,selected (cachedA p (k.val+1) true) (cachedA p (k.val+1) false)
    (cachedC p (k.val+1)) (choices k)

theorem strict {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3)
    (less : bound p choices<1) :
    (∑ k : Fin v,min (cachedA p (k.val+1) true)
      (min (cachedA p (k.val+1) false) (cachedC p (k.val+1))))<1 := by
  apply lt_of_le_of_lt _ less
  exact Finset.sum_le_sum (fun k _ => min_le_selected _ _ _ _)
end Aris4Math.ThirtyFour.CachedChosenRows

namespace Aris4Math.ThirtyFour.ChosenRowsPilot
open CachedRows CachedChosenRows TwentyFiveCoefficientPilot
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def choices : Fin 25 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,1,1,1,1,1,1,1,1]
set_option profiler true in
theorem chosen_value : bound computed choices=(12869/12870 : ℚ) := by decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (vertices : Fin 9↪Fin 25)
    (counts : ∀ T,count H vertices T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H vertices positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,p_eq_computed]
    apply CachedChosenRows.strict computed choices
    rw [chosen_value]
    norm_num
#print axioms propertyB_of_counts
end Aris4Math.ThirtyFour.ChosenRowsPilot

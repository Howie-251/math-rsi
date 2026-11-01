import Aris4Math.ThirtyFour.CachedSparseApplication

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

def profileRow (p : Numeric.Profile) (k : ℕ) (choice : Fin 3) : ℚ :=
  if choice=0 then cachedA p k true
  else if choice=1 then cachedA p k false
  else cachedC p k

theorem profileRow_eq (p : Numeric.Profile) (k : ℕ) (choice : Fin 3) :
    profileRow p k choice=selected (cachedA p k true) (cachedA p k false) (cachedC p k) choice := by rfl

def bound {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3) : ℚ :=
  ∑ k,profileRow p (k.val+1) (choices k)

theorem strict {v : ℕ} (p : Numeric.Profile) (choices : Fin v → Fin 3)
    (less : bound p choices<1) :
    (∑ k : Fin v,min (cachedA p (k.val+1) true)
      (min (cachedA p (k.val+1) false) (cachedC p (k.val+1))))<1 := by
  apply lt_of_le_of_lt _ less
  apply Finset.sum_le_sum
  intro k _
  rw [profileRow_eq]
  exact min_le_selected _ _ _ _
end Aris4Math.ThirtyFour.CachedChosenRows

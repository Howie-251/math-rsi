import Aris4Math.ThirtyFour.TwentyFiveUnitCounts

/-! Sparse recovery certificates. The only potentially nonzero recovered
types are empty, singleton, or actual multipoint blocks. Checking these types
proves equality on every subset, without enumerating a whole powerset. -/
namespace Aris4Math.ThirtyFour.TwentyFiveInventorySupport

open TwentyFiveUnitCounts

variable {n : ℕ}

def labels (listed : List (Finset (Fin n))) : List (Finset (Fin n)) :=
  ∅ :: ((List.ofFn fun i : Fin n => ({i} : Finset (Fin n))) ++ listed)

theorem empty_mem (listed : List (Finset (Fin n))) : ∅∈labels listed := by simp [labels]

theorem singleton_mem (listed : List (Finset (Fin n))) (i : Fin n) : {i}∈labels listed := by
  simp only [labels,List.mem_cons,List.mem_append,List.mem_ofFn]
  exact Or.inr (Or.inl ⟨i,rfl⟩)

theorem block_mem (listed : List (Finset (Fin n))) (T : Finset (Fin n)) (mem : T∈listed) :
    T∈labels listed := by simp only [labels,List.mem_cons,List.mem_append]; tauto

theorem inventory_zero (m : ℕ) (degree : Fin n → ℕ)
    (listed : List (Finset (Fin n))) (T : Finset (Fin n)) (absent : T∉labels listed) :
    inventory m degree listed.toFinset T=0 := by
  have empty : T≠∅ := fun eq => absent (eq ▸ empty_mem listed)
  have singleton : T.card≠1 := by
    intro card
    obtain ⟨i,rfl⟩ := Finset.card_eq_one.mp card
    exact absent (singleton_mem listed i)
  have block : T∉listed.toFinset := fun mem => absent (block_mem listed T (List.mem_toFinset.mp mem))
  simp only [inventory,if_neg empty,if_neg singleton,if_neg block]

theorem eq_of_support (m : ℕ) (degree : Fin n → ℕ)
    (listed : List (Finset (Fin n))) (μ : Finset (Fin n) → ℕ)
    (support : ∀ T,μ T≠0→T∈labels listed)
    (checked : (labels listed).all (fun T => decide (inventory m degree listed.toFinset T=μ T))=true) :
    ∀ T, inventory m degree listed.toFinset T=μ T := by
  intro T
  by_cases mem : T∈labels listed
  · exact of_decide_eq_true (List.all_eq_true.mp checked T mem)
  · rw [inventory_zero m degree listed T mem]
    exact (by_contra fun h => mem (support T (Ne.symm h)))

end Aris4Math.ThirtyFour.TwentyFiveInventorySupport

#print axioms Aris4Math.ThirtyFour.TwentyFiveInventorySupport.eq_of_support

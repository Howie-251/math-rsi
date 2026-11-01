import Aris4Math.ThirtyFour.TwentyLowComplete
namespace T34TwentyLowAudit
 theorem original_coloring
    (E : Finset (Finset (Fin 20)))
    (uniform : ∀ e ∈ E, e.card = 5)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (edge_count : E.card = 34)
    (low_degree : ∃ x : Fin 20, (E.filter fun e => x ∈ e).card ≤ 6) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x = true).card ∧
      (e.filter fun x => c x = true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.TwentyLow.propertyB_of_low_degree ⟨E,uniform⟩ cover edge_count low_degree
end T34TwentyLowAudit
#check @Aris4Math.ThirtyFour.TwentyLow.propertyB_of_low_degree
#print axioms Aris4Math.ThirtyFour.TwentyLow.propertyB_of_low_degree
#print axioms T34TwentyLowAudit.original_coloring

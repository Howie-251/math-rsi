import Aris4Math.ThirtyFour.TwentySevenMany
namespace T34TwentySevenAudit
 theorem original_coloring
    (E : Finset (Finset (Fin 20)))
    (uniform : ∀ e ∈ E, e.card = 5)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (edge_count : E.card = 34)
    (minimum : ∀ x : Fin 20, 7 ≤ (E.filter fun e => x ∈ e).card)
    (three_sevens : 3 ≤ (Finset.univ.filter fun x : Fin 20 =>
       (E.filter fun e => x ∈ e).card = 7).card) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x = true).card ∧
      (e.filter fun x => c x = true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_many_sevens
    ⟨E,uniform⟩ cover edge_count minimum three_sevens
end T34TwentySevenAudit
#check @Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_four_sevens
#check @Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_many_sevens
#print axioms Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_four_sevens
#print axioms Aris4Math.ThirtyFour.TwentySevenMany.propertyB_of_many_sevens
#print axioms T34TwentySevenAudit.original_coloring

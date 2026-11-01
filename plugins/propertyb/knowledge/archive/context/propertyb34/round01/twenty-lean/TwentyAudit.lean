import Aris4Math.ThirtyFour.Twenty
namespace T34TwentyAudit

theorem original_coloring (E : Finset (Finset (Fin 20)))
    (uniform : ∀ e ∈ E, e.card=5)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (size : E.card=34) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.twenty_propertyB ⟨E,uniform⟩ cover size

theorem original_two_colors (E : Finset (Finset (Fin 20)))
    (uniform : ∀ e ∈ E, e.card=5)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (size : E.card=34) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ E,
      (∃ x ∈ e, c x=true) ∧ (∃ y ∈ e, c y=false) := by
  obtain ⟨c,hc⟩ := original_coloring E uniform cover size
  refine ⟨c,?_⟩
  intro e he
  obtain ⟨lower,upper⟩ := hc e he
  constructor
  · obtain ⟨x,hx⟩ := Finset.one_le_card.mp lower
    exact ⟨x,(Finset.mem_filter.mp hx).1,(Finset.mem_filter.mp hx).2⟩
  · by_contra hn
    have all : ∀ x ∈ e, c x=true := by
      intro x hx
      cases eq : c x
      · exact False.elim (hn ⟨x,hx,eq⟩)
      · rfl
    have eq : e.filter (fun x => c x=true)=e := Finset.filter_eq_self.mpr all
    rw [eq,uniform e he] at upper
    omega
end T34TwentyAudit
#check @Aris4Math.ThirtyFour.twenty_propertyB
#print axioms Aris4Math.ThirtyFour.TwentyEight.propertyB_of_minimum_eight
#print axioms Aris4Math.ThirtyFour.twenty_propertyB
#print axioms T34TwentyAudit.original_coloring
#print axioms T34TwentyAudit.original_two_colors

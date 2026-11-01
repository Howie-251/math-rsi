import Aris4Math.ThirtyFour.Nineteen
namespace T34NineteenAudit
 theorem original_coloring
    (E : Finset (Finset (Fin 19)))
    (uniform : ∀ e ∈ E, e.card = 5)
    (cover : ∀ x y : Fin 19, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (bound : E.card ≤ 34) :
    ∃ c : Fin 19 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x = true).card ∧
      (e.filter fun x => c x = true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.nineteen_propertyB ⟨E,uniform⟩ cover bound
end T34NineteenAudit
#print Aris4Math.PropertyB
#check @Aris4Math.ThirtyFour.NineteenSelection.exists_selected
#check @Aris4Math.ThirtyFour.nineteen_propertyB
#print axioms Aris4Math.ThirtyFour.nineteen_propertyB
#print axioms T34NineteenAudit.original_coloring

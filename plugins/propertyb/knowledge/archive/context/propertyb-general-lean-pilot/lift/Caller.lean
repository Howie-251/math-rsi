import Aris4Math.General.RS.Lift

namespace Aris4Math.General.RS

universe u

/-- Independent bare original-form caller for the finite-type transfer. The supplied
`Fin n` theorem is the only premise, to be filled by the assembled RS proof. -/
theorem bare_finite_pilot_caller
    (hfin : ∀ (n : ℕ) (F : Finset (Finset (Fin n))),
      Uniform F 17 → F.card ≤ 2 ^ 17 → PropertyB F) :
    ∀ (V : Type u) [Finite V] (E : Finset (Finset V)),
      (∀ e ∈ E, e.card = 17) → E.card ≤ 2 ^ 17 →
      ∃ c : V → Bool, ∀ e ∈ E,
        (∃ x ∈ e, c x = true) ∧ (∃ y ∈ e, c y = false) := by
  exact pilotTarget_of_fin hfin

/-- The criterion transfer uses the actual cardinality and actual gamma from E. -/
theorem bare_finite_criterion_caller (k : ℕ) (C : ℕ → ℕ → Prop)
    (hfin : ∀ (n : ℕ) (F : Finset (Finset (Fin n))),
      Uniform F k → C F.card (gamma F) → PropertyB F)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (hU : ∀ e ∈ E, e.card = k) (hC : C E.card (gamma E)) :
    ∃ c : V → Bool, ∀ e ∈ E,
      (∃ x ∈ e, c x = true) ∧ (∃ y ∈ e, c y = false) := by
  exact propertyB_of_fin_criterion k C hfin E hU hC

end Aris4Math.General.RS

#check Aris4Math.General.RS.pilotTarget_of_fin
#check Aris4Math.General.RS.propertyB_of_fin_criterion
#print axioms Aris4Math.General.RS.bare_finite_pilot_caller
#print axioms Aris4Math.General.RS.bare_finite_criterion_caller

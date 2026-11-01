import Aris4Math.ThirtyThree.Assembly
open Aris4Math

/-- Independently spell out the actual24-point coloring conclusion. -/
theorem audit_twenty_four (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) :
    ∃ c : Fin 24 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  ThirtyThree.twenty_four_propertyB H cover edges33

/-- The only remaining premise is the original23-point coloring assertion.
This is an equivalence, not a proof of either side. -/
theorem audit_remaining : Target33 ↔
    (∀ H : Simple5Hypergraph (Fin 23), H.edges.card = 33 → H.PairCovering →
      ∃ c : Fin 23 → Bool, ∀ e ∈ H.edges,
        1 ≤ (e.filter (fun x => c x = true)).card ∧
        (e.filter (fun x => c x = true)).card ≤ 4) :=
  ThirtyThree.target_iff_remaining_goal

#print ThirtyThree.twenty_four_propertyB
#print ThirtyThree.RemainingGoal
#print Target33
#print axioms audit_twenty_four
#print axioms audit_remaining
#print axioms ThirtyThree.target_iff_remaining_goal

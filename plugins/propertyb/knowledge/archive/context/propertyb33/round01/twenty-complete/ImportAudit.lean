import Aris4Math.ThirtyThree.Assembly

open Aris4Math Aris4Math.ThirtyThree

#check twenty_propertyB
#check TwentyEight.propertyB_of_eight_eight
#print RemainingGoal
#check target_iff_remaining_goal
#print axioms CustomDeletion.propertyB_of_custom_deletion
#print axioms TwentyEight.propertyB_of_eight_eight
#print axioms twenty_propertyB
#print axioms target_iff_remaining_goal

/-- Independent restatement of the complete actual twenty-vertex branch. -/
example (H : Simple5Hypergraph (Fin 20)) (edges : H.edges.card = 33)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  twenty_propertyB H cover edges

universe u

/-- The new original-target caller still requires the five unsolved cases. -/
example
    (remaining : ∀ v : ℕ, 21 ≤ v → v ≤ 25 →
      ∀ H : Simple5Hypergraph (Fin v),
        H.edges.card = 33 → H.PairCovering → PropertyB H) : Target33.{u} :=
  target_of_remaining_goal remaining

import Aris4Math.ThirtyThree.Assembly
import Aris4Math.ThirtyThree.TwentyThreeComplete

/-! End-to-end proof of the universe-polymorphic 33-edge Property B target. -/
namespace Aris4Math
universe u

namespace ThirtyThree

/-- The final finite branch, established from its actual input. -/
theorem remaining_goal : RemainingGoal := by
  intro H edges33 cover
  exact twenty_three_propertyB H cover edges33

/-- All seven possible vertex counts in the finite reduction. -/
theorem finite_goal : FiniteGoal := finite_goal_of_remaining remaining_goal

end ThirtyThree

/-- Every finite simple five-uniform hypergraph with at most 33 edges
has a coloring in which every edge contains both colors. -/
theorem propertyB_of_at_most_thirty_three : Target33.{u} :=
  ThirtyThree.target_of_remaining_goal ThirtyThree.remaining_goal

/-- The original coloring statement with all definitions exposed. -/
theorem two_colorable_of_at_most_thirty_three
    (V : Type u) [Fintype V] (H : Simple5Hypergraph V) (edges : H.edges.card ≤ 33) :
    ∃ c : V → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  propertyB_of_at_most_thirty_three V H edges

/-- Equivalently, every non-two-colorable simple five-uniform hypergraph
has at least 34 edges. -/
theorem non_propertyB_edges_ge_thirty_four
    (V : Type u) [Fintype V] (H : Simple5Hypergraph V) (hnot : ¬ PropertyB H) :
    34 ≤ H.edges.card := by
  by_contra hsmall
  exact hnot (propertyB_of_at_most_thirty_three V H (by omega))

end Aris4Math

#print axioms Aris4Math.ThirtyThree.twenty_three_propertyB
#print axioms Aris4Math.ThirtyThree.remaining_goal
#print axioms Aris4Math.ThirtyThree.finite_goal
#print axioms Aris4Math.propertyB_of_at_most_thirty_three
#print axioms Aris4Math.two_colorable_of_at_most_thirty_three
#print axioms Aris4Math.non_propertyB_edges_ge_thirty_four

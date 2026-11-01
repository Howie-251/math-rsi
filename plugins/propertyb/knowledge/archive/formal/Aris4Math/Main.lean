import Aris4Math.SmallVertices
import Aris4Math.NoLocks
import Aris4Math.GlobalPairs
import Aris4Math.TwentyOne
import Aris4Math.TwentyTwo
import Aris4Math.TwentyThree
import Aris4Math.LargeVertices

/-! Assembly of the original, universe-polymorphic Property B target.
Each finite branch below is a theorem about the actual hypergraph. -/

namespace Aris4Math

universe u

theorem finite_goal : SmallVertices.FiniteGoal := by
  intro v lower upper H edges32 cover
  interval_cases v
  · exact NoLocks.nineteen_propertyB H (by omega)
  · exact TwentyVertices.twenty_propertyB H (by omega)
  · exact TwentyOne.twenty_one_propertyB H cover edges32
  · exact TwentyTwo.twenty_two_propertyB H cover edges32
  · exact TwentyThree.twenty_three_propertyB H cover edges32
  · exact LargeVertices.twenty_four_propertyB H cover edges32
  · exact LargeVertices.twenty_five_propertyB H cover edges32

/-- Every finite simple five-uniform hypergraph with at most thirty-two edges
has a two-coloring in which every edge contains both colors. -/
theorem propertyB_of_at_most_thirty_two : Target.{u} :=
  SmallVertices.target_of_finite_goal finite_goal

/-- Expanded original statement, for direct semantic inspection. -/
theorem two_colorable_of_at_most_thirty_two
    (V : Type u) [Fintype V] (H : Simple5Hypergraph V) (edges : H.edges.card ≤ 32) :
    ∃ c : V → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 :=
  propertyB_of_at_most_thirty_two V H edges

/-- Direct lower-bound formulation: every non-two-colorable simple
five-uniform hypergraph has at least thirty-three edges. -/
theorem non_propertyB_edges_ge_thirty_three
    (V : Type u) [Fintype V] (H : Simple5Hypergraph V) (hnot : ¬ PropertyB H) :
    33 ≤ H.edges.card := by
  by_contra hsmall
  exact hnot (propertyB_of_at_most_thirty_two V H (by omega))

end Aris4Math

#print axioms Aris4Math.finite_goal
#print axioms Aris4Math.propertyB_of_at_most_thirty_two
#print axioms Aris4Math.two_colorable_of_at_most_thirty_two
#print axioms Aris4Math.non_propertyB_edges_ge_thirty_three

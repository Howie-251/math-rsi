import Aris4Math.ThirtyThree.Reduction
import Aris4Math.ThirtyThree.Nineteen
import Aris4Math.ThirtyThree.Twenty
import Aris4Math.ThirtyThree.TwentyOne
import Aris4Math.ThirtyThree.TwentyTwoComplete
import Aris4Math.ThirtyThree.TwentyFourComplete
import Aris4Math.ThirtyThree.TwentyFive

/-!
# T33 after the completed 19-, 20-, 21-, 22-, 24-, and 25-vertex branches

The remaining 23-vertex case is an explicit proposition and an explicit premise.
This module does not assert that T33 or that case has been proved.
-/

namespace Aris4Math.ThirtyThree

universe u

/-- The actual remaining 23-vertex case after the other six branches. -/
def RemainingGoal : Prop :=
  ∀ H : Simple5Hypergraph (Fin 23),
    H.edges.card = 33 → H.PairCovering → PropertyB H

/-- Connect the six completed branches to the original finite reduction,
retaining the 23-vertex case as a visible premise. -/
theorem finite_goal_of_remaining (remaining : RemainingGoal) : FiniteGoal := by
  intro v lower upper H edges33 cover
  by_cases h19 : v = 19
  · subst v
    exact Nineteen.nineteen_propertyB H (by omega)
  · by_cases h20 : v = 20
    · subst v
      exact twenty_propertyB H cover edges33
    · by_cases h21 : v = 21
      · subst v
        exact twenty_one_propertyB H cover edges33
      · by_cases h22 : v = 22
        · subst v
          exact twenty_two_propertyB H cover edges33
        · by_cases h25 : v = 25
          · subst v
            exact twenty_five_propertyB H cover edges33
          · by_cases h24 : v = 24
            · subst v
              exact twenty_four_propertyB H cover edges33
            · have h23 : v = 23 := by omega
              subst v
              exact remaining H edges33 cover

/-- The remaining case suffices for the original arbitrary-vertex target. -/
theorem target_of_remaining_goal (remaining : RemainingGoal) : Target33.{u} :=
  target_of_finite_goal (finite_goal_of_remaining remaining)

/-- Exact identification of what remains after the six completed cases. -/
theorem target_iff_remaining_goal : Target33.{u} ↔ RemainingGoal := by
  constructor
  · intro target H edges33 cover
    exact (target_iff_finite_goal.mp target) 23 (by omega) (by omega) H edges33 cover
  · exact target_of_remaining_goal

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.finite_goal_of_remaining
#print axioms Aris4Math.ThirtyThree.target_of_remaining_goal
#print axioms Aris4Math.ThirtyThree.target_iff_remaining_goal

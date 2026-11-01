import Aris4Math.Main
import Aris4Math.ThirtyThree.TwentyTwo
import Aris4Math.ThirtyThree.DoubleLockAt
import Aris4Math.ThirtyThree.TwentyStandard

#check Aris4Math.ThirtyThree.DoubleLockAt.realizes_profile_at
#check Aris4Math.ThirtyThree.TwentyTwo.six_six_propertyB
#check Aris4Math.ThirtyThree.TwentyTwo.six_seven_propertyB
#check Aris4Math.ThirtyThree.TwentyStandard.propertyB_of_standard_pair
#print Aris4Math.ThirtyThree.TwentyStandard.standardDegrees
#print axioms Aris4Math.ThirtyThree.DoubleLockAt.realizes_profile_at
#print axioms Aris4Math.ThirtyThree.TwentyTwo.six_six_propertyB
#print axioms Aris4Math.ThirtyThree.TwentyTwo.six_seven_propertyB
#print axioms Aris4Math.ThirtyThree.TwentyStandard.propertyB_of_standard_pair
#print axioms Aris4Math.propertyB_of_at_most_thirty_two

/-- The original result is still available at its unchanged Target. -/
example : Aris4Math.Target := Aris4Math.propertyB_of_at_most_thirty_two

/-- Expanded conclusion of the actual new (6,6) branch. -/
example (H : Aris4Math.Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 6) :
    ∃ c : Fin 22 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter (fun z => c z = true)).card ∧
      (e.filter (fun z => c z = true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.TwentyTwo.six_six_propertyB H cover edges33 x y hne codegree1 dx dy

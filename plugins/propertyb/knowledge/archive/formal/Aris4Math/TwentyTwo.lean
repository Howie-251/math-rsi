import Aris4Math.DoubleTripleLockProfiles
import Aris4Math.ProfileApplication

/-! Complete 22-vertex finite-goal branch, including the actual link
deductions for degree 6,7 and degree 7,7 pairs. -/

namespace Aris4Math.TwentyTwo

open DoubleLockProfiles TypeCounting LinkDeletion LinkWeightCertificates

theorem six_six_propertyB (H : Simple5Hypergraph (Fin 22)) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 6) : PropertyB H := by
  have real := realizes_v22_66 H edges32 x y hne codegree1 dx dy
  exact ProfileApplication.propertyB_of_uncorrected_profile H
    (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_66
    real rfl rfl Numeric.v22_66_lt_one

theorem six_seven_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 6) (dy : H.degree y = 7) : PropertyB H := by
  have real := realizes_v22_67 H edges32 x y hne codegree1 dx dy
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_67
    real rfl _ Numeric.v22_67_lt_one
  intro j hj
  fin_cases j
  · norm_num [twoPositions, Numeric.v22_67] at hj
  · exact v22_67_deduction_12 H cover (twoVertices x y hne)
      (twoPositions 22 (by decide)) real 1 rfl dy

theorem seven_seven_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x y : Fin 22) (hne : x ≠ y) (codegree1 : H.codegree x y = 1)
    (dx : H.degree x = 7) (dy : H.degree y = 7) : PropertyB H := by
  have real := realizes_v22_77 H edges32 x y hne codegree1 dx dy
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (twoPositions 22 (by decide)) Numeric.v22_77
    real rfl _ Numeric.v22_77_lt_one
  intro j _
  fin_cases j
  · exact v22_77_deduction_11 H cover (twoVertices x y hne)
      (twoPositions 22 (by decide)) real 0 rfl dx
  · exact v22_77_deduction_12 H cover (twoVertices x y hne)
      (twoPositions 22 (by decide)) real 1 rfl dy

/-- Every point-pair-covering 32-edge simple 5-uniform hypergraph on 22
vertices has Property B. The actual structural selection, type table,
permutation formulas and link correction have all been discharged. -/
theorem twenty_two_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) : PropertyB H := by
  obtain ⟨x, y, hne, hc, hdegrees⟩ := H.exists_two_locks_of_twenty_two cover edges32 (by simp)
  rcases hdegrees with ⟨dx,dy⟩ | ⟨dx,dy⟩ | ⟨dx,dy⟩
  · exact six_six_propertyB H edges32 x y hne hc dx dy
  · exact six_seven_propertyB H cover edges32 x y hne hc dx dy
  · exact seven_seven_propertyB H cover edges32 x y hne hc dx dy

end Aris4Math.TwentyTwo

#print axioms Aris4Math.TwentyTwo.six_six_propertyB
#print axioms Aris4Math.TwentyTwo.six_seven_propertyB
#print axioms Aris4Math.TwentyTwo.seven_seven_propertyB
#print axioms Aris4Math.TwentyTwo.twenty_two_propertyB

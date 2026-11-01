import Aris4Math.DoubleTripleLockProfiles
import Aris4Math.TripleLockProfiles
import Aris4Math.ProfileApplication

/-! Complete 23-vertex branch, including both actual lock alternatives and
the exceptional zero-weight link pair in the three-lock profile. -/

namespace Aris4Math.TwentyThree

open TypeCounting DoubleLockProfiles TripleLockProfiles LinkWeightCertificates

theorem two_six_propertyB (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x y : Fin 23) (hne : x ≠ y)
    (dx : H.degree x = 6) (dy : H.degree y = 6) (codegree1 : H.codegree x y = 1) :
    PropertyB H := by
  have real := realizes_v23_66 H edges32 x y hne codegree1 dx dy
  apply ProfileApplication.propertyB_of_corrected_profile H (twoVertices x y hne)
    (twoPositions 23 (by decide)) Numeric.v23_66 real rfl _ Numeric.v23_66_lt_one
  intro j _
  fin_cases j
  · exact v23_66_deduction_11 H cover _ _ real 0 rfl dx
  · exact v23_66_deduction_12 H cover _ _ real 1 rfl dy

theorem six_seven_seven_propertyB (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x y z : Fin 23) (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (cxy : H.codegree x y = 1) (cxz : H.codegree x z = 1) (cyz : H.codegree y z = 1)
    (noTriple : ∀ e ∈ H.edges, ¬ (x ∈ e ∧ y ∈ e ∧ z ∈ e)) : PropertyB H := by
  have real := realizes_677_of_vertices H edges32 x y z hxy hxz hyz dx dy dz cxy cxz cyz noTriple
  apply ProfileApplication.propertyB_of_corrected_profile H
    (threeVertices x y z hxy hxz hyz) threePositions Numeric.v23_677 real rfl _
    Numeric.v23_677_lt_one
  intro j hj
  fin_cases j
  · norm_num [threePositions, Numeric.v23_677] at hj
  · exact v23_677_deduction_12 H cover _ _ real 1 rfl dy
  · exact v23_677_deduction_13 H cover _ _ real 2 rfl dz

/-- Actual structure exhausts both alternatives, each yielding the original
PropertyB predicate without numerical or profile hypotheses. -/
theorem twenty_three_propertyB (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) : PropertyB H := by
  rcases H.exists_locks_of_twenty_three cover edges32 (by simp) with two | three
  · obtain ⟨x,y,hne,dx,dy,hcodeg⟩ := two
    exact two_six_propertyB H cover edges32 x y hne dx dy hcodeg
  · obtain ⟨x,y,z,hxy,hxz,hyz,dx,dy,dz,cxy,cxz,cyz,noTriple⟩ := three
    exact six_seven_seven_propertyB H cover edges32 x y z hxy hxz hyz
      dx dy dz cxy cxz cyz noTriple

end Aris4Math.TwentyThree

#print axioms Aris4Math.TwentyThree.two_six_propertyB
#print axioms Aris4Math.TwentyThree.six_seven_seven_propertyB
#print axioms Aris4Math.TwentyThree.twenty_three_propertyB

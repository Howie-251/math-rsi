import Aris4Math.ThirtyThree.TwentyThreeHighPath
import Aris4Math.ThirtyThree.TwentyThreeClusterSelection

/-! After the actual high-pair and induced-path probability branches, the
remaining r=0 configurations are precisely the selected five/six cluster cases. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighReduction

open TwentyThreeClusterSelection

theorem cluster_cases_of_not_propertyB (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) (count : H.sixVertices.card = 0)
    (notB : ¬PropertyB H) : FiveCase H ∨ SixCase H := by
  have budget := TwentyThreeSelection.six_seven_budget H cover edges33 (by decide)
  have many : 19 ≤ (TwentyThreeSelection.sevenVertices H).card := by omega
  have upper (x : Fin 23) (dx : H.degree x = 7) (y : Fin 23) (dy : H.degree y = 7)
      (xy : x ≠ y) : H.codegree x y ≤ 2 := by
    by_contra hn
    exact notB (TwentyThreeHighQuad.propertyB_of_pair_at_least_three H cover edges33 many
      x y dx dy xy (by omega))
  apply cluster_selection_of_no_sixes H cover (by decide) edges33 count upper
  intro x dx y dy z dz xy xz yz cxy cxz cyz
  exact notB (TwentyThreeHighPath.propertyB_of_path H cover edges33 many upper
    y x z dy dx dz xy.symm yz xz ((H.codegree_comm y x).trans cxy) cyz cxz)

theorem propertyB_or_cluster_cases (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) (count : H.sixVertices.card = 0) :
    PropertyB H ∨ FiveCase H ∨ SixCase H := by
  classical
  by_cases h : PropertyB H
  · exact Or.inl h
  · exact Or.inr (cluster_cases_of_not_propertyB H cover edges33 count h)

end Aris4Math.ThirtyThree.TwentyThreeHighReduction

import Aris4Math.ThirtyThree.TwentyThreeHighComplete

open Aris4Math
open Aris4Math.ThirtyThree

/-- Independent caller states the actual coloring requirement in full. -/
theorem high_branch_original_coloring
    (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (noSix : H.sixVertices.card = 0) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun x => coloring x = true).card ∧
      (e.filter fun x => coloring x = true).card ≤ 4 :=
  TwentyThreeHighComplete.propertyB_of_no_sixes H cover edges33 noSix

#print axioms ThirtyThree.TwentyThreeHighPath.propertyB_of_path
#print axioms ThirtyThree.TwentyThreeHighReduction.cluster_cases_of_not_propertyB
#print axioms ThirtyThree.TwentyThreeHighFive.propertyB_of_five_case
#print axioms ThirtyThree.TwentyThreeHighSixCatalog.covers
#print axioms ThirtyThree.TwentyThreeHighSix.propertyB_of_six_case
#print axioms ThirtyThree.TwentyThreeHighComplete.propertyB_of_no_sixes
#print axioms high_branch_original_coloring
#print ThirtyThree.TwentyThreeHighComplete.propertyB_of_no_sixes

import Aris4Math.ThirtyThree.TwentyThreeHighFive
import Aris4Math.ThirtyThree.TwentyThreeHighSix
open Aris4Math Aris4Math.ThirtyThree

theorem cluster_five_original_coloring (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (selected : TwentyThreeClusterSelection.FiveCase H) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun x => coloring x = true).card ∧
      (e.filter fun x => coloring x = true).card ≤ 4 :=
  TwentyThreeHighFive.propertyB_of_five_case H cover edges33 selected

theorem cluster_six_original_coloring (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (selected : TwentyThreeClusterSelection.SixCase H) :
    ∃ coloring : Fin 23 → Bool, ∀ e ∈ H.edges,
      1 ≤ (e.filter fun x => coloring x = true).card ∧
      (e.filter fun x => coloring x = true).card ≤ 4 :=
  TwentyThreeHighSix.propertyB_of_six_case H edges33 selected

#print axioms TwentyThreeHighFiveCatalog.covers
#print axioms TwentyThreeHighFive.propertyB_of_five_case
#print axioms TwentyThreeHighSixCatalog.pivot_covers
#print axioms TwentyThreeHighSixCatalog.covers
#print axioms TwentyThreeHighSix.propertyB_of_six_case
#print axioms cluster_five_original_coloring
#print axioms cluster_six_original_coloring

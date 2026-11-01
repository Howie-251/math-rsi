import Aris4Math.ThirtyThree.TwentyThreeFourLowStructure
open Aris4Math Aris4Math.ThirtyThree

example (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (degree : ∀ i, H.degree (f i) = 6) :
    (∀ i : Fin 4, MultiLockRecovery.count H f (QuadProfiles.highLabels i.castSucc) < 3) ∧
      MultiLockRecovery.count H f (QuadProfiles.highLabels 4) < 2 :=
  TwentyThreeFourLowStructure.actual_high_bounds H cover f degree

#print axioms TwentyThreeFourLowStructure.actual_high_bounds

import Aris4Math.ThirtyThree.TwentyFourUniqueBadPair
import Aris4Math.ThirtyThree.MultiLockRecovery
import Aris4Math.ThirtyThree.ActualBadSlot

#check Aris4Math.ThirtyThree.TwentyFourUniqueBadPair.exists_unique_bad_pair_arms
#check Aris4Math.ThirtyThree.MultiLockRecovery.actual_recovered
#check Aris4Math.ThirtyThree.MultiLockRecovery.realizes_recovered
#check Aris4Math.ThirtyThree.ActualBadSlot.exists_actual_slot
#check Aris4Math.ThirtyThree.ActualBadSlot.slot_weight_lower

#print axioms Aris4Math.ThirtyThree.TwentyFourUniqueBadPair.exists_unique_bad_pair_arms
#print axioms Aris4Math.ThirtyThree.MultiLockRecovery.realizes_recovered
#print axioms Aris4Math.ThirtyThree.ActualBadSlot.slot_weight_lower

/-- Independently restate the actual 24-vertex degree-six local conclusion. -/
example (H : Aris4Math.Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (x : Fin 24) (six : H.degree x = 6) :
    ∃ z E F A B, z ≠ x ∧ H.codegree x z = 2 ∧ E ∈ H.edges ∧ F ∈ H.edges ∧
      E ≠ F ∧ E ∩ F = {x,z} ∧ H.badLinkPairs x = {{E,F}} ∧
      A = E \ {x,z} ∧ B = F \ {x,z} ∧ A.card = 3 ∧ B.card = 3 ∧
      Disjoint A B ∧ E = {x,z} ∪ A ∧ F = {x,z} ∪ B :=
  Aris4Math.ThirtyThree.TwentyFourUniqueBadPair.exists_unique_bad_pair_arms
    H cover (by decide) six

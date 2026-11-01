import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionData
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def testRows : List (List ℕ × (Fin 5 × NewCase × NewPerm)) := [([2,2,0,1,1,0,0],(2,0,0)),([2,2,0,0,0,1,0],(0,0,0)),([2,1,0,2,1,0,0],(0,0,0)),([2,1,0,1,2,0,0],(0,0,0)),([2,1,0,1,1,0,0],(2,0,0))]
def testCovered (row : List ℕ × (Fin 5 × NewCase × NewPerm)) : Prop :=
  TwentyThreeLowPromotionBase.Feasible (newCounts 7 row.1) →
  OldResidual (projected row.2.1 (newCounts 7 row.1)) →
  ∀ T, newCounts 7 row.1 (T.map (newPerm row.2.2.2).toEmbedding)=μ row.2.2.1 T
noncomputable instance (r) : Decidable (testCovered r) := by unfold testCovered;infer_instance
example : testRows.all (fun row => decide (testCovered row))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion

import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
import Aris4Math.ThirtyFour.TwentyThreeSixLowStrictJoint0
import Aris4Math.ThirtyFour.TwentyThreeSixLowStrictJoint1
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open TwentyThreeSixLowPromotion (NewCase μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Residue := Fin 1
def residualSource : Residue → NewCase := ![2]
def residualCounts (r : Residue) := μ (residualSource r)
theorem joint_binding0 : ∀ T, μ 0 T=TwentyThreeSixLowStrictJoint0Data.μ T := by decide +kernel
theorem joint_binding1 : ∀ T, μ 1 T=TwentyThreeSixLowStrictJoint1Data.μ T := by decide +kernel
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23)) (f : Fin 6 ↪ Fin 23)
    (q : NewCase) (notB : ¬ PropertyB H) (actual : ∀ T, count H f T=μ q T) :
    ∃ r : Residue, ∀ T, count H f T=residualCounts r T := by
  fin_cases q
  · exact (notB (TwentyThreeSixLowStrictJoint0.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding0 T)))).elim
  · exact (notB (TwentyThreeSixLowStrictJoint1.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding1 T)))).elim
  · exact ⟨0,actual⟩
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 6 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ r : Residue, ∃ σ : Equiv.Perm (Fin 6),
      ∀ T, count H (σ.toEmbedding.trans f) T=residualCounts r T := by
  obtain ⟨q,σ,actual⟩ := TwentyThreeSixLowPromotion.actual H cover edges f degrees notB
  obtain ⟨r,hr⟩ := residual_of_noB H (σ.toEmbedding.trans f) q notB actual
  exact ⟨r,σ,hr⟩
end Aris4Math.ThirtyFour.TwentyThreeSixLowClassified
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowClassified.actual_residual

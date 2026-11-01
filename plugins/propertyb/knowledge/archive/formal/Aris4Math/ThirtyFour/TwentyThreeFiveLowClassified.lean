import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrict
import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open TwentyThreeFiveLowPromotion (NewCase μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Residue := Fin 2
def residualSource : Residue → NewCase := ![0,2]
def residualCounts (r : Residue) := μ (residualSource r)
def pureSource : TwentyThreeFiveLowStrictData.Case → NewCase := ![1,4,5,6,7,8,9,10,11]
theorem pure_binding : ∀ i T, μ (pureSource i) T=TwentyThreeFiveLowStrictData.μ i T := by decide +kernel
theorem joint_binding3 : ∀ T, μ 3 T=TwentyThreeFiveLowStrictJoint3Data.μ T := by decide +kernel
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23)) (f : Fin 5 ↪ Fin 23)
    (q : NewCase) (notB : ¬ PropertyB H) (actual : ∀ T, count H f T=μ q T) :
    ∃ r : Residue, ∀ T, count H f T=residualCounts r T := by
  fin_cases q
  · exact ⟨0,actual⟩
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 0
      (fun T => (actual T).trans (pure_binding 0 T)))).elim
  · exact ⟨1,actual⟩
  · exact (notB (TwentyThreeFiveLowStrictJoint3.propertyB_of_counts H f
      (fun T => (actual T).trans (joint_binding3 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 1
      (fun T => (actual T).trans (pure_binding 1 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 2
      (fun T => (actual T).trans (pure_binding 2 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 3
      (fun T => (actual T).trans (pure_binding 3 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 4
      (fun T => (actual T).trans (pure_binding 4 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 5
      (fun T => (actual T).trans (pure_binding 5 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 6
      (fun T => (actual T).trans (pure_binding 6 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 7
      (fun T => (actual T).trans (pure_binding 7 T)))).elim
  · exact (notB (TwentyThreeFiveLowStrict.propertyB_of_counts H f 8
      (fun T => (actual T).trans (pure_binding 8 T)))).elim
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (f : Fin 5 ↪ Fin 23)
    (degrees : ∀ i, H.degree (f i)=6) (notB : ¬ PropertyB H) :
    ∃ r : Residue, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=residualCounts r T := by
  obtain ⟨q,σ,actual⟩ := TwentyThreeFiveLowPromotion.actual H cover edges f degrees notB
  obtain ⟨r,hr⟩ := residual_of_noB H (σ.toEmbedding.trans f) q notB actual
  exact ⟨r,σ,hr⟩
end Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified.actual_residual

import Aris4Math.ThirtyFour.TwentyThreeFewLowFourCoverage
import Aris4Math.ThirtyFour.TwentyThreeOneLowFour
import Aris4Math.ThirtyFour.TwentyThreeTwoLowFour
import Aris4Math.ThirtyFour.TwentyThreeOneLowFourJoint17
import Aris4Math.ThirtyFour.TwentyThreeOneLowFourJoint22
import Aris4Math.ThirtyFour.TwentyThreeOneLowFourJoint53
import Aris4Math.ThirtyFour.TwentyThreeOneLowFourJoint57
import Aris4Math.ThirtyFour.TwentyThreeTwoLowFourJoint39
namespace Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
namespace OneLow
open TwentyThreeFewLowFourCoverage.OneLow (NewCase μ)
def residual : Finset NewCase := {0,2,3,4,7,9,10,15,16,18,19,20,23,27,28,33,37,41,44,46,48,51}
def pureIndex : TwentyThreeOneLowFourData.Case → NewCase := ![1,5,6,8,11,12,13,14,21,24,25,26,29,30,31,32,34,35,36,38,39,40,42,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72]
theorem pureMatch : ∀ c T, μ (pureIndex c) T=TwentyThreeOneLowFourData.μ c T := by decide +kernel
theorem jointMatch17 : ∀ T, μ 17 T=TwentyThreeOneLowFourJoint17Data.μ T := by decide +kernel
theorem jointMatch22 : ∀ T, μ 22 T=TwentyThreeOneLowFourJoint22Data.μ T := by decide +kernel
theorem jointMatch53 : ∀ T, μ 53 T=TwentyThreeOneLowFourJoint53Data.μ T := by decide +kernel
theorem jointMatch57 : ∀ T, μ 57 T=TwentyThreeOneLowFourJoint57Data.μ T := by decide +kernel
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23))
    (f : Fin 4 ↪ Fin 23) (c : NewCase)
    (counts : ∀ T, count H f T=μ c T) (noB : ¬PropertyB H) : c∈residual := by
  by_contra absent
  fin_cases c
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 0
    intro T
    exact (counts T).trans (pureMatch 0 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 1
    intro T
    exact (counts T).trans (pureMatch 1 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 2
    intro T
    exact (counts T).trans (pureMatch 2 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 3
    intro T
    exact (counts T).trans (pureMatch 3 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 4
    intro T
    exact (counts T).trans (pureMatch 4 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 5
    intro T
    exact (counts T).trans (pureMatch 5 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 6
    intro T
    exact (counts T).trans (pureMatch 6 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 7
    intro T
    exact (counts T).trans (pureMatch 7 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFourJoint17.propertyB_of_counts H f
    intro T
    exact (counts T).trans (jointMatch17 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 8
    intro T
    exact (counts T).trans (pureMatch 8 T)
  · apply noB
    apply TwentyThreeOneLowFourJoint22.propertyB_of_counts H f
    intro T
    exact (counts T).trans (jointMatch22 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 9
    intro T
    exact (counts T).trans (pureMatch 9 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 10
    intro T
    exact (counts T).trans (pureMatch 10 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 11
    intro T
    exact (counts T).trans (pureMatch 11 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 12
    intro T
    exact (counts T).trans (pureMatch 12 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 13
    intro T
    exact (counts T).trans (pureMatch 13 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 14
    intro T
    exact (counts T).trans (pureMatch 14 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 15
    intro T
    exact (counts T).trans (pureMatch 15 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 16
    intro T
    exact (counts T).trans (pureMatch 16 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 17
    intro T
    exact (counts T).trans (pureMatch 17 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 18
    intro T
    exact (counts T).trans (pureMatch 18 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 19
    intro T
    exact (counts T).trans (pureMatch 19 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 20
    intro T
    exact (counts T).trans (pureMatch 20 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 21
    intro T
    exact (counts T).trans (pureMatch 21 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 22
    intro T
    exact (counts T).trans (pureMatch 22 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 23
    intro T
    exact (counts T).trans (pureMatch 23 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 24
    intro T
    exact (counts T).trans (pureMatch 24 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 25
    intro T
    exact (counts T).trans (pureMatch 25 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 26
    intro T
    exact (counts T).trans (pureMatch 26 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 27
    intro T
    exact (counts T).trans (pureMatch 27 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 28
    intro T
    exact (counts T).trans (pureMatch 28 T)
  · apply noB
    apply TwentyThreeOneLowFourJoint53.propertyB_of_counts H f
    intro T
    exact (counts T).trans (jointMatch53 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 29
    intro T
    exact (counts T).trans (pureMatch 29 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 30
    intro T
    exact (counts T).trans (pureMatch 30 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 31
    intro T
    exact (counts T).trans (pureMatch 31 T)
  · apply noB
    apply TwentyThreeOneLowFourJoint57.propertyB_of_counts H f
    intro T
    exact (counts T).trans (jointMatch57 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 32
    intro T
    exact (counts T).trans (pureMatch 32 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 33
    intro T
    exact (counts T).trans (pureMatch 33 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 34
    intro T
    exact (counts T).trans (pureMatch 34 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 35
    intro T
    exact (counts T).trans (pureMatch 35 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 36
    intro T
    exact (counts T).trans (pureMatch 36 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 37
    intro T
    exact (counts T).trans (pureMatch 37 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 38
    intro T
    exact (counts T).trans (pureMatch 38 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 39
    intro T
    exact (counts T).trans (pureMatch 39 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 40
    intro T
    exact (counts T).trans (pureMatch 40 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 41
    intro T
    exact (counts T).trans (pureMatch 41 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 42
    intro T
    exact (counts T).trans (pureMatch 42 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 43
    intro T
    exact (counts T).trans (pureMatch 43 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 44
    intro T
    exact (counts T).trans (pureMatch 44 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 45
    intro T
    exact (counts T).trans (pureMatch 45 T)
  · apply noB
    apply TwentyThreeOneLowFour.propertyB_of_counts H f 46
    intro T
    exact (counts T).trans (pureMatch 46 T)
/-- Actual old/new lock classification followed by all proved strict exclusions. -/
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (c : TwentyThreeFewLowBase.Case)
    (old : ∀ T, count H (LockExtension.restrict f) T=TwentyThreeFewLowBase.oneLow c T)
    (degree : H.degree (f 3)=7)
    (pairs : ∀ i : Fin 3,
      H.codegree (f i.castSucc) (f 3)≤TwentyThreeFewLowFourCoverage.OneLow.cap (some i))
    (noB : ¬PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<1 ↔ i.val<1) ∧ q∈residual ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨q,σ,roles,counts⟩ :=
    TwentyThreeFewLowFourCoverage.OneLow.actual H cover f c old degree pairs
  exact ⟨q,σ,roles,residual_of_noB H (σ.toEmbedding.trans f) q counts noB,counts⟩
end OneLow
namespace TwoLow
open TwentyThreeFewLowFourCoverage.TwoLow (NewCase μ)
def residual : Finset NewCase := {0,2,3,5,6,8,9,11,14,16,17,19,20,22,23,26,28,29,40}
def pureIndex : TwentyThreeTwoLowFourData.Case → NewCase := ![1,4,7,10,12,13,15,18,21,24,25,27,30,31,32,33,34,35,36,37,38,41,42,43,44,45,46,47]
theorem pureMatch : ∀ c T, μ (pureIndex c) T=TwentyThreeTwoLowFourData.μ c T := by decide +kernel
theorem jointMatch39 : ∀ T, μ 39 T=TwentyThreeTwoLowFourJoint39Data.μ T := by decide +kernel
theorem residual_of_noB (H : Simple5Hypergraph (Fin 23))
    (f : Fin 4 ↪ Fin 23) (c : NewCase)
    (counts : ∀ T, count H f T=μ c T) (noB : ¬PropertyB H) : c∈residual := by
  by_contra absent
  fin_cases c
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 0
    intro T
    exact (counts T).trans (pureMatch 0 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 1
    intro T
    exact (counts T).trans (pureMatch 1 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 2
    intro T
    exact (counts T).trans (pureMatch 2 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 3
    intro T
    exact (counts T).trans (pureMatch 3 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 4
    intro T
    exact (counts T).trans (pureMatch 4 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 5
    intro T
    exact (counts T).trans (pureMatch 5 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 6
    intro T
    exact (counts T).trans (pureMatch 6 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 7
    intro T
    exact (counts T).trans (pureMatch 7 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 8
    intro T
    exact (counts T).trans (pureMatch 8 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 9
    intro T
    exact (counts T).trans (pureMatch 9 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 10
    intro T
    exact (counts T).trans (pureMatch 10 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 11
    intro T
    exact (counts T).trans (pureMatch 11 T)
  · exact absent (by decide)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 12
    intro T
    exact (counts T).trans (pureMatch 12 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 13
    intro T
    exact (counts T).trans (pureMatch 13 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 14
    intro T
    exact (counts T).trans (pureMatch 14 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 15
    intro T
    exact (counts T).trans (pureMatch 15 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 16
    intro T
    exact (counts T).trans (pureMatch 16 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 17
    intro T
    exact (counts T).trans (pureMatch 17 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 18
    intro T
    exact (counts T).trans (pureMatch 18 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 19
    intro T
    exact (counts T).trans (pureMatch 19 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 20
    intro T
    exact (counts T).trans (pureMatch 20 T)
  · apply noB
    apply TwentyThreeTwoLowFourJoint39.propertyB_of_counts H f
    intro T
    exact (counts T).trans (jointMatch39 T)
  · exact absent (by decide)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 21
    intro T
    exact (counts T).trans (pureMatch 21 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 22
    intro T
    exact (counts T).trans (pureMatch 22 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 23
    intro T
    exact (counts T).trans (pureMatch 23 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 24
    intro T
    exact (counts T).trans (pureMatch 24 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 25
    intro T
    exact (counts T).trans (pureMatch 25 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 26
    intro T
    exact (counts T).trans (pureMatch 26 T)
  · apply noB
    apply TwentyThreeTwoLowFour.propertyB_of_counts H f 27
    intro T
    exact (counts T).trans (pureMatch 27 T)
/-- Actual old/new lock classification followed by all proved strict exclusions. -/
theorem actual_residual (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (f : Fin 4 ↪ Fin 23) (c : TwentyThreeFewLowBase.Case)
    (old : ∀ T, count H (LockExtension.restrict f) T=TwentyThreeFewLowBase.twoLow c T)
    (degree : H.degree (f 3)=7)
    (pairs : ∀ i : Fin 3,
      H.codegree (f i.castSucc) (f 3)≤TwentyThreeFewLowFourCoverage.TwoLow.cap (some i))
    (noB : ¬PropertyB H) :
    ∃ q : NewCase, ∃ σ : Equiv.Perm (Fin 4),
      (∀ i, (σ i).val<2 ↔ i.val<2) ∧ q∈residual ∧
      ∀ T, count H (σ.toEmbedding.trans f) T=μ q T := by
  obtain ⟨q,σ,roles,counts⟩ :=
    TwentyThreeFewLowFourCoverage.TwoLow.actual H cover f c old degree pairs
  exact ⟨q,σ,roles,residual_of_noB H (σ.toEmbedding.trans f) q counts noB,counts⟩
end TwoLow
end Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.OneLow.residual_of_noB
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.TwoLow.residual_of_noB
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.OneLow.actual_residual
#print axioms Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified.TwoLow.actual_residual

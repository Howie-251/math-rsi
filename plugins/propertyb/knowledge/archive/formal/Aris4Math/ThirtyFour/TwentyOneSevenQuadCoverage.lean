import Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverageKernel
namespace Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem residue_readback (c : Case) (h : 61≤c.val) (T : Finset (Fin 4)) :
    μ c T=residueμ ⟨c.val-61,by omega⟩ T := by
  have low : ¬ c.val<52 := by omega
  simp only [μ,dif_neg low]
  split_ifs <;> omega

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 4↪Fin 21)
    (c : Case) (strict : c.val<61)
    (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H f T=μ c T) : PropertyB H := by
  by_cases small:c.val<52
  · apply TwentyOneSevenQuad7777.propertyB_of_counts H f ⟨c.val,small⟩
    simpa only [μ,dif_pos small] using counts
  · have lower : 52≤c.val := by omega
    have bound : c.val<70:=c.isLt
    interval_cases v:c.val
    · apply TwentyOneSevenJointQuad0.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad1.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad3.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad4.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad18.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad19.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad20.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad21.propertyB_of_counts H f
      simpa [μ,v] using counts
    · apply TwentyOneSevenJointQuad32.propertyB_of_counts H f
      simpa [μ,v] using counts
end Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage

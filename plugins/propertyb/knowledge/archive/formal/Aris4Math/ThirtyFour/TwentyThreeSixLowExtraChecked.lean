import Aris4Math.ThirtyFour.TwentyThreeSixLowExtraCatalogue
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16
import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra8

namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraChecked
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
open TwentyThreeSixLowExtraCatalogue (Degree NewCase μ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000

def pureSeven : NewCase → TwentyThreeSixLowExtra7Data.Case :=
  ![0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,16]

theorem seven_binding : ∀ q : NewCase, q≠16 → ∀ T,
    μ 0 q T=TwentyThreeSixLowExtra7Data.μ (pureSeven q) T := by decide +kernel

theorem joint_binding : ∀ T, μ 0 16 T=TwentyThreeSixLowExtra7Joint16Data.μ T :=
  by decide +kernel

theorem eight_binding : ∀ q : NewCase, ∀ T,
    μ 1 q T=TwentyThreeSixLowExtra8Data.μ q T := by decide +kernel

/-- Every one of the actual seven-lock representatives gives a coloring. -/
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23)) (f : Fin 7↪Fin 23)
    (d : Degree) (q : NewCase) (actual : ∀ T, count H f T=μ d q T) :
    PropertyB H := by
  fin_cases d
  · by_cases special : q=16
    · subst q
      exact TwentyThreeSixLowExtra7Joint16.propertyB_of_counts H f
        (fun T => (actual T).trans (joint_binding T))
    · exact TwentyThreeSixLowExtra7.propertyB_of_counts H f (pureSeven q)
        (fun T => (actual T).trans (seven_binding q special T))
  · exact TwentyThreeSixLowExtra8.propertyB_of_counts H f q
      (fun T => (actual T).trans (eight_binding q T))

end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraChecked
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowExtraChecked.propertyB_of_counts

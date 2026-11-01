import Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math Aris4Math.ThirtyThree.TwentyFourMixedData
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
example : ∀ k : Fin 24,
    Numeric.boundA (p 0) (k.val+1) = (abc 0 k).1 ∧
    Numeric.boundB (p 0) (k.val+1) = (abc 0 k).2.1 ∧
    Numeric.boundC (p 0) (k.val+1) = (abc 0 k).2.2 := by decide +kernel

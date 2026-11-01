import Aris4Math.General.RS.PilotEstimates

open Aris4Math.General.RS
#check pilot_ak_gt_half
#check pilot_jk_le
#check pilot_estimate_sq
#check pilot_estimate
#check pilot_estimate_actual
#print axioms pilot_estimate_actual
#print axioms pilot_estimate

example {V : Type*} (E : Finset (Finset V)) (hm : E.card ≤ 2^17) :
    1 - (ak 17 (1/17))^((E.card : ℝ)/(2:ℝ)^16) +
      (gamma E : ℝ)/((2:ℝ)^16)^2 * jk 17 (1/17) < 1 :=
  pilot_estimate_actual E hm

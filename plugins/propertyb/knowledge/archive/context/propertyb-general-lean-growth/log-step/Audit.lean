import Aris4Math.General.Growth.LogStep
open Aris4Math.General.RS

example (M s r d a J L : ℝ) (hM : 2 ≤ M) (hs0 : 0 < s) (hr : 1 < r)
    (hd : 0 < d) (ha : 0 < a) (hJ : 0 ≤ J)
    (hlog : -2 * L < (M / d) * Real.log a)
    (hs : (2 + 2 * L) * s + 2 < M / r)
    (hacc : M * (M - 1) / d ^ 2 * J < a ^ (M / d)) :
    ((M + s) ^ 2 * (1 - 1 / r)) / d ^ 2 * J < a ^ ((M + s) / d) :=
  rs_increment_of_log_slack M s r d a J L hM hs0 hr hd ha hJ hlog hs hacc

#print Aris4Math.General.RS.rs_increment_of_log_slack
#print axioms Aris4Math.General.RS.rs_increment_of_log_slack

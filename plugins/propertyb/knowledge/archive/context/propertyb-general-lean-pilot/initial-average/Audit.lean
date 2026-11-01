import Aris4Math.General.RS.InitialAverage
import Aris4Math.General.RS.Algorithm

open Aris4Math.General.RS

#check initial_monoCount_average
#check initial_power_average
#check initial_residual_conditional
#check initial_residual_average
#print monoCount
#print axioms initial_monoCount_average
#print axioms initial_power_average
#print axioms initial_residual_conditional
#print axioms initial_residual_average

/-- Independent actual algorithm-event caller, with only original uniformity
and the RS parameter domain. -/
example {n : ℕ} (E : Finset (Finset (Fin n))) (k : ℕ) (hk : 2 ≤ k)
    (hE : Uniform E k) {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    bernoulliExpect (1/2) (fun c => bernoulliProb p (ResidualEvent E c)) ≤
      1 - (ak k p)^((E.card : ℝ)/(2:ℝ)^(k-1)) := by
  simpa only [ResidualEvent] using initial_residual_average E k (by omega) hE hp hp1

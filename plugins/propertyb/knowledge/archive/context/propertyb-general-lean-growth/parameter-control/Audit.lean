import Aris4Math.General.Growth.ParameterControl

open Aris4Math.General.RS

#check acceptedAt_parameter_control
#print axioms ak_le_mul
#print axioms rs_integrand_ge_half
#print axioms jk_lower_small
#print axioms jk_mono_unit
#print axioms acceptedAt_parameter_control

example {k M : ℕ} {p : ℝ} (hk : 17 ≤ k) (hM : 2^k ≤ M)
    (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (hAcc : (M : ℝ) * ((M : ℝ)-1) / ((2 : ℝ)^(k-1))^2 * jk k p <
      (1-(1-p)^k) ^ ((M : ℝ)/(2 : ℝ)^(k-1))) :
    1/(k : ℝ)^2 < p ∧ 1/(2*(k : ℝ)^2) ≤ jk k p ∧
    (M : ℝ)/(2 : ℝ)^(k-1) < 2*(k : ℝ) ∧
    -2*Real.log (k : ℝ) < ((M : ℝ)/(2 : ℝ)^(k-1))*Real.log (1-(1-p)^k) := by
  exact acceptedAt_parameter_control hk hM ⟨hp, hp1, hAcc⟩

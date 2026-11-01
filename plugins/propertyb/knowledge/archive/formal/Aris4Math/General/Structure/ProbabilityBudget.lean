import Aris4Math.General.RS.ProbabilityBound

/-! Monotone budget substitution in the proved actual-object RS criterion. -/
namespace Aris4Math.General.RS

universe u
noncomputable section

theorem propertyB_of_rs_budget {V : Type u} [Finite V]
    (E : Finset (Finset V)) (k N : ℕ) (hk : 2 ≤ k) (hu : Uniform E k)
    {p G : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) (hm : E.card ≤ N)
    (hgamma : (gamma E : ℝ) ≤ G)
    (hbound : G / ((2 : ℝ) ^ (k - 1)) ^ 2 * jk k p <
      (ak k p) ^ ((N : ℝ) / (2 : ℝ) ^ (k - 1))) : PropertyB E := by
  have ha0 := ak_pos (by omega : 0 < k) hp hp1
  have ha1 := ak_le_one k hp1
  have h_exp : (E.card : ℝ) / (2 : ℝ) ^ (k - 1) ≤
      (N : ℝ) / (2 : ℝ) ^ (k - 1) :=
    div_le_div_of_nonneg_right (by exact_mod_cast hm) (by positivity)
  have h_power := Real.rpow_le_rpow_of_exponent_ge ha0 ha1 h_exp
  have h_coefficient : (gamma E : ℝ) / ((2 : ℝ) ^ (k - 1)) ^ 2 ≤
      G / ((2 : ℝ) ^ (k - 1)) ^ 2 :=
    div_le_div_of_nonneg_right hgamma (by positivity)
  have h_term := mul_le_mul_of_nonneg_right h_coefficient (jk_nonneg k hp.le hp1)
  apply propertyB_of_rs_bound E k hk hu hp hp1
  linarith

end
end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.propertyB_of_rs_budget

import Aris4Math.General.RS.Definitions
import Aris4Math.General.RS.Integral
import Mathlib.Analysis.SpecialFunctions.Pow.Real

noncomputable section
namespace Aris4Math.General.RS

lemma pilot_ak_gt_half : (1/2 : ℝ) < ak 17 (1/17) := by
  norm_num [ak]

lemma pilot_jk_le : jk 17 (1/17) ≤ (1/17 : ℝ) :=
  jk_le 17 (by norm_num) (by norm_num)

/-- The numerical RS pilot has slack even with the crude directed-pair bound m². -/
lemma pilot_estimate_sq (m γ : ℕ) (hm : m ≤ 2^17) (hγ : γ ≤ m^2) :
    1 - (ak 17 (1/17))^((m : ℝ)/(2:ℝ)^16) +
      (γ : ℝ)/((2:ℝ)^16)^2 * jk 17 (1/17) < 1 := by
  have ha := pilot_ak_gt_half
  have ha0 : 0 < ak 17 (1/17) := lt_trans (by norm_num : (0:ℝ)<1/2) ha
  have ha1 : ak 17 (1/17) ≤ 1 := ak_le_one 17 (by norm_num)
  have hm0 : (0:ℝ) ≤ m := by positivity
  have hmr : (m : ℝ) ≤ 131072 := by exact_mod_cast hm
  have hγr : (γ : ℝ) ≤ (m : ℝ)^2 := by exact_mod_cast hγ
  have hexp : (m : ℝ)/(2:ℝ)^16 ≤ (2:ℝ) := by norm_num; linarith
  have hpower : (1/4 : ℝ) < (ak 17 (1/17))^((m : ℝ)/(2:ℝ)^16) := by
    have hs : (1/4 : ℝ) < (ak 17 (1/17))^2 := by nlinarith
    have hr := Real.rpow_le_rpow_of_exponent_ge ha0 ha1 hexp
    have hr' : (ak 17 (1/17))^2 ≤ (ak 17 (1/17))^((m : ℝ)/(2:ℝ)^16) := by
      simpa only [Real.rpow_two] using hr
    exact hs.trans_le hr'
  have hcoef : (γ : ℝ)/((2:ℝ)^16)^2 ≤ 4 := by
    norm_num
    have hprod := mul_nonneg hm0 (show 0 ≤ 131072-(m:ℝ) by linarith)
    nlinarith
  have hcoef0 : 0 ≤ (γ : ℝ)/((2:ℝ)^16)^2 := by positivity
  have hj := mul_le_mul_of_nonneg_left pilot_jk_le hcoef0
  have hc := mul_le_mul_of_nonneg_right hcoef (by norm_num : (0:ℝ) ≤ 1/17)
  nlinarith

/-- The standard directed-pair bound supplies the numerical RS pilot. -/
lemma pilot_estimate (m γ : ℕ) (hm : m ≤ 2^17) (hγ : γ ≤ m*(m-1)) :
    1 - (ak 17 (1/17))^((m : ℝ)/(2:ℝ)^16) +
      (γ : ℝ)/((2:ℝ)^16)^2 * jk 17 (1/17) < 1 := by
  apply pilot_estimate_sq m γ hm
  exact hγ.trans (by nlinarith [Nat.sub_le m 1])

/-- Every directed single-intersection pair is an actual pair of original edges. -/
lemma gamma_le_edges_sq {V : Type*} (E : Finset (Finset V)) : gamma E ≤ E.card^2 := by
  classical
  unfold gamma singlePairs
  exact (Finset.card_filter_le _ _).trans_eq (by simp [pow_two])

/-- Actual-edge-family numerical caller, including the empty family. -/
lemma pilot_estimate_actual {V : Type*} (E : Finset (Finset V)) (hm : E.card ≤ 2^17) :
    1 - (ak 17 (1/17))^((E.card : ℝ)/(2:ℝ)^16) +
      (gamma E : ℝ)/((2:ℝ)^16)^2 * jk 17 (1/17) < 1 :=
  pilot_estimate_sq E.card (gamma E) hm (gamma_le_edges_sq E)

end Aris4Math.General.RS

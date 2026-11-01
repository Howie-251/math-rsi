import Aris4Math.General.Growth.Definitions
import Mathlib.Algebra.Order.Ring.Pow

namespace Aris4Math.General.RS
noncomputable section
open MeasureTheory Set

lemma ak_le_mul (k : ℕ) {p : ℝ} (_hp : 0 ≤ p) (hp1 : p ≤ 1) :
    ak k p ≤ (k : ℝ) * p := by
  have hb := one_add_mul_sub_le_pow (a := (1 - p)) (by linarith) k
  dsimp [ak]
  nlinarith

lemma rs_integrand_ge_half {k : ℕ} (hk : 2 ≤ k) {y : ℝ}
    (hy : 0 ≤ y) (hyk : y ≤ 1 / (k : ℝ)^2) :
    (1 : ℝ) / 2 ≤ (1 - y^2)^(k-1) := by
  have hkR : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hkpos : (0 : ℝ) < k := by linarith
  have hyk' : y * (k : ℝ)^2 ≤ 1 := (le_div_iff₀ (sq_pos_of_pos hkpos)).mp hyk
  have hy1 : y ≤ 1 := by nlinarith
  have hy2 : y^2 ≤ y := by nlinarith
  have hcoeff : (k - 1 : ℕ) ≤ k := Nat.sub_le _ _
  have hcoeffR : ((k - 1 : ℕ) : ℝ) ≤ k := by exact_mod_cast hcoeff
  have hb := one_add_mul_sub_le_pow (a := (1-y^2)) (by nlinarith) (k-1)
  have hky : 2 * (k : ℝ) * y ≤ 1 := by nlinarith [mul_nonneg hy (by nlinarith : (0:ℝ) ≤ (k:ℝ)^2 - 2*k)]
  have hprod : ((k-1:ℕ):ℝ) * y^2 ≤ (k:ℝ)*y :=
    mul_le_mul hcoeffR hy2 (sq_nonneg y) (by positivity)
  nlinarith

lemma jk_lower_small {k : ℕ} (hk : 2 ≤ k) {p : ℝ}
    (hp : 0 ≤ p) (hpk : p ≤ 1 / (k : ℝ)^2) : p / 2 ≤ jk k p := by
  have h := intervalIntegral.integral_mono_on hp
    (show IntervalIntegrable (fun _ : ℝ => (1 : ℝ)/2) volume 0 p from intervalIntegrable_const)
    (show IntervalIntegrable (fun y : ℝ => (1-y^2)^(k-1)) volume 0 p from
      (by fun_prop : Continuous (fun y : ℝ => (1-y^2)^(k-1))).intervalIntegrable 0 p)
    (fun y hy => rs_integrand_ge_half hk hy.1 (hy.2.trans hpk))
  simpa [jk] using h

lemma jk_mono_unit (k : ℕ) {p q : ℝ} (hq : 0 ≤ q) (hqp : q ≤ p) (hp1 : p ≤ 1) :
    jk k q ≤ jk k p := by
  have hi : ∀ a b : ℝ, IntervalIntegrable (fun y : ℝ => (1-y^2)^(k-1)) volume a b :=
    fun a b => (by fun_prop : Continuous (fun y : ℝ => (1-y^2)^(k-1))).intervalIntegrable a b
  have hadd := intervalIntegral.integral_add_adjacent_intervals (hi 0 q) (hi q p)
  have hnon : 0 ≤ ∫ y in q..p, (1-y^2)^(k-1) := by
    apply intervalIntegral.integral_nonneg hqp
    intro y hy
    apply pow_nonneg
    nlinarith [mul_nonneg (show 0 ≤ y by linarith [hy.1]) (show 0 ≤ 1-y by linarith [hy.2])]
  dsimp [jk]
  linarith

/-- The accepted-parameter control of Lemma B.1, for the same precise RS
acceptance inequality and its actual parameter witness. -/
theorem acceptedAt_parameter_control {k M : ℕ} {p : ℝ}
    (hk : 17 ≤ k) (hM : 2^k ≤ M) (hAcc : AcceptedAt k M p) :
    1 / (k : ℝ)^2 < p ∧
    1 / (2 * (k : ℝ)^2) ≤ jk k p ∧
    (M : ℝ) / (2 : ℝ)^(k-1) < 2 * (k : ℝ) ∧
    -2 * Real.log (k : ℝ) <
      ((M : ℝ) / (2 : ℝ)^(k-1)) * Real.log (ak k p) := by
  obtain ⟨hp, hp1, hacc⟩ := hAcc
  have hk2 : 2 ≤ k := by omega
  have hkR : (2 : ℝ) ≤ k := by exact_mod_cast hk2
  have hkpos : (0 : ℝ) < k := by linarith
  let d : ℝ := (2 : ℝ)^(k-1)
  let t : ℝ := (M : ℝ) / d
  let C : ℝ := (M : ℝ) * ((M : ℝ)-1) / d^2
  have hdpos : 0 < d := by dsimp [d]; positivity
  have hd1 : 1 ≤ d := by dsimp [d]; exact one_le_pow₀ (by norm_num)
  have hpow : (2 : ℝ)^k = 2*d := by
    dsimp [d]
    conv_lhs => rw [← Nat.sub_add_cancel (show 1 ≤ k by omega), pow_succ]
    ring
  have hMr : (2 : ℝ)^k ≤ M := by exact_mod_cast hM
  have hMd : 2*d ≤ M := by rwa [hpow] at hMr
  have hMr2 : (2 : ℝ) ≤ M := by linarith
  have ht2 : 2 ≤ t := (le_div_iff₀ hdpos).mpr hMd
  have hC : t^2/2 ≤ C := by
    have hm : (M : ℝ)^2/2 ≤ (M : ℝ)*((M : ℝ)-1) := by nlinarith
    calc
      t^2/2 = (M : ℝ)^2/2/d^2 := by dsimp [t]; rw [div_pow]; ring
      _ ≤ C := div_le_div_of_nonneg_right hm (sq_nonneg d)
  have hJ := jk_nonneg k hp hp1
  have hmain : t^2/2 * jk k p < (ak k p)^t :=
    (mul_le_mul_of_nonneg_right hC hJ).trans_lt hacc
  have ha0 := ak_nonneg k hp hp1
  have ha1 := ak_le_one k hp1
  have hab := ak_le_mul k hp hp1
  have hsmall : 1 / (k : ℝ)^2 < p := by
    by_contra hnot
    have hpk : p ≤ 1/(k : ℝ)^2 := le_of_not_gt hnot
    have hJp := jk_lower_small hk2 hp hpk
    have hpkk : p * (k : ℝ)^2 ≤ 1 := (le_div_iff₀ (sq_pos_of_pos hkpos)).mp hpk
    have hpowle : (ak k p)^t ≤ (ak k p)^2 := by
      simpa only [Real.rpow_two] using
        (Real.rpow_le_rpow_of_exponent_ge' ha0 ha1 (by norm_num : (0:ℝ) ≤ 2) ht2)
    have hakp2 : (ak k p)^2 ≤ ((k : ℝ)*p)^2 := by nlinarith
    have hkp2 : ((k : ℝ)*p)^2 ≤ p := by
      nlinarith [mul_nonneg hp (show 0 ≤ 1-p*(k:ℝ)^2 by linarith)]
    have ht2sq : 2 ≤ t^2/2 := by nlinarith
    have hleft : p ≤ t^2/2 * jk k p := by
      have hh := mul_le_mul_of_nonneg_right ht2sq hJ
      linarith
    exact (not_lt_of_ge (hpowle.trans (hakp2.trans hkp2))) (hleft.trans_lt hmain)
  have hq0 : (0:ℝ) ≤ 1/(k:ℝ)^2 := by positivity
  have hJq := jk_lower_small hk2 hq0 (le_refl (1/(k:ℝ)^2))
  have hJmono := jk_mono_unit k hq0 hsmall.le hp1
  have hJbound : 1/(2*(k:ℝ)^2) ≤ jk k p := by
    have heq : (1/(k:ℝ)^2)/2 = 1/(2*(k:ℝ)^2) := by ring
    rw [heq] at hJq
    exact hJq.trans hJmono
  have hpow1 : (ak k p)^t ≤ 1 := Real.rpow_le_one ha0 ha1 (by linarith)
  have hstrict : t^2/(4*(k:ℝ)^2) < (ak k p)^t := by
    have hh := mul_le_mul_of_nonneg_left hJbound (show 0 ≤ t^2/2 by positivity)
    have heq : t^2/2*(1/(2*(k:ℝ)^2)) = t^2/(4*(k:ℝ)^2) := by ring
    rw [heq] at hh
    exact hh.trans_lt hmain
  have htupper : t < 2*(k:ℝ) := by
    have hh1 : t^2/(4*(k:ℝ)^2) < 1 := hstrict.trans_le hpow1
    have hh : t^2 < 1 * (4*(k:ℝ)^2) :=
      (div_lt_iff₀ (by positivity : (0:ℝ) < 4*(k:ℝ)^2)).mp hh1
    nlinarith
  have hbase : 1/(k:ℝ)^2 < (ak k p)^t := by
    have htsq : 4 ≤ t^2 := by nlinarith only [ht2]
    have haux : 1/(k:ℝ)^2 ≤ t^2/(4*(k:ℝ)^2) := calc
      _ = 4/(4*(k:ℝ)^2) := by ring
      _ ≤ _ := div_le_div_of_nonneg_right htsq (by positivity)
    exact haux.trans_lt hstrict
  have hapos : 0 < ak k p := ak_pos (by omega) (lt_of_lt_of_le (by positivity : (0:ℝ) < 1/(k:ℝ)^2) hsmall.le) hp1
  have hlog := Real.log_lt_log (by positivity : (0:ℝ) < 1/(k:ℝ)^2) hbase
  rw [Real.log_rpow hapos] at hlog
  have hlogeq : Real.log (1/(k:ℝ)^2) = -2 * Real.log (k:ℝ) := by
    rw [one_div, Real.log_inv, Real.log_pow]
    norm_num
  rw [hlogeq] at hlog
  exact ⟨hsmall, hJbound, htupper, hlog⟩

end
end Aris4Math.General.RS

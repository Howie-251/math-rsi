import Aris4Math.General.Growth.Main
import Mathlib.Tactic.IntervalCases
import Mathlib.Analysis.Complex.ExponentialBounds

/-! Extension of the same maximal RS budget and integer gain to all k ≥ 12.
The five new natural parameters use elementary exact inequalities; no hypergraph
or coloring enumeration is involved. -/
namespace Aris4Math.General.RS
universe u
noncomputable section

theorem seed_ak_three_fifths {k : ℕ} (hk : 12 ≤ k) (hk16 : k ≤ 16) :
    (3 / 5 : ℝ) ≤ ak k (1 / (k : ℝ)) := by
  interval_cases k <;> norm_num [ak]


theorem seed_acceptedAt_twelve {k : ℕ} (hk : 12 ≤ k) :
    AcceptedAt k (2 ^ k) (1 / (k : ℝ)) := by
  by_cases h17 : 17 ≤ k
  · exact seed_acceptedAt h17
  have hk16 : k ≤ 16 := by omega
  have hkR : (12 : ℝ) ≤ k := by exact_mod_cast hk
  have hk0 : (0 : ℝ) < k := by linarith
  have hp0 : (0 : ℝ) ≤ 1 / (k : ℝ) := by positivity
  have hp1 : (1 : ℝ) / (k : ℝ) ≤ 1 :=
    (div_le_one hk0).mpr (by linarith)
  have hd : (0 : ℝ) < (2 : ℝ) ^ (k - 1) := by positivity
  have hM : ((2 ^ k : ℕ) : ℝ) = 2 * (2 : ℝ) ^ (k - 1) := by
    rw [Nat.cast_pow, Nat.cast_ofNat]
    conv_lhs => rw [show k = (k - 1) + 1 by omega]
    rw [pow_succ]
    ring
  have hexp : ((2 ^ k : ℕ) : ℝ) / (2 : ℝ) ^ (k - 1) = 2 := by
    rw [hM]
    field_simp
  have hMr : (1 : ℝ) ≤ ((2 ^ k : ℕ) : ℝ) := by
    norm_cast
    exact Nat.one_le_pow k 2 (by decide)
  have hcoef0 : 0 ≤ ((2 ^ k : ℕ) : ℝ) * (((2 ^ k : ℕ) : ℝ) - 1) /
      ((2 : ℝ) ^ (k - 1)) ^ 2 := by
    exact div_nonneg (mul_nonneg (by positivity) (sub_nonneg.mpr hMr)) (sq_nonneg _)
  have hcoef : ((2 ^ k : ℕ) : ℝ) * (((2 ^ k : ℕ) : ℝ) - 1) /
      ((2 : ℝ) ^ (k - 1)) ^ 2 ≤ 4 := by
    apply (div_le_iff₀ (sq_pos_of_pos hd)).mpr
    rw [hM]
    nlinarith
  have hj := mul_le_mul_of_nonneg_left (jk_le k hp0 hp1) hcoef0
  have hc := mul_le_mul_of_nonneg_right hcoef hp0
  have hstrict : (4 : ℝ) * (1 / (k : ℝ)) < 9 / 25 := by
    rw [mul_one_div, div_lt_iff₀ hk0]
    linarith
  have ha := seed_ak_three_fifths hk hk16
  have ha0 := ak_nonneg k hp0 hp1
  have hsq : (9 / 25 : ℝ) ≤ (ak k (1 / (k : ℝ))) ^ 2 := by nlinarith
  refine ⟨hp0, hp1, ?_⟩
  rw [hexp, Real.rpow_two]
  exact (hj.trans hc).trans_lt (hstrict.trans_le hsq)

theorem seed_rsAccepts_twelve {k : ℕ} (hk : 12 ≤ k) : RSAccepts k (2 ^ k) := by
  refine ⟨?_, 1 / (k : ℝ), seed_acceptedAt_twelve hk⟩
  exact Nat.one_le_pow k 2 (by decide)



theorem acceptedAt_parameter_control_two {k M : ℕ} {p : ℝ}
    (hk : 2 ≤ k) (hM : 2^k ≤ M) (hAcc : AcceptedAt k M p) :
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


theorem rsaAccepts_lt_twelve {k M : ℕ} (hk : 12 ≤ k) (hA : RSAccepts k M) :
    M < k * 2^k := by
  by_cases hM : M < 2^k
  · have hcut : 2^k ≤ k*2^k := by
      calc
        2^k = 1 * 2^k := by simp
        _ ≤ k*2^k := Nat.mul_le_mul_right _ (by omega)
    exact hM.trans_le hcut
  · have hMb : 2^k ≤ M := Nat.le_of_not_gt hM
    obtain ⟨hMpos, p, hp⟩ := hA
    have hu := (acceptedAt_parameter_control_two (by omega) hMb hp).2.2.1
    have hd : (0:ℝ) < (2:ℝ)^(k-1) := by positivity
    have hmul : (M:ℝ) < 2*(k:ℝ)*(2:ℝ)^(k-1) := (div_lt_iff₀ hd).mp hu
    have hpow : (2:ℝ)^k = 2*(2:ℝ)^(k-1) := by
      conv_lhs => rw [← Nat.sub_add_cancel (show 1 ≤ k by omega), pow_succ]
      ring
    have hcast : (M:ℝ) < ((k*2^k:ℕ):ℝ) := by
      rw [Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat, hpow]
      nlinarith only [hmul]
    exact_mod_cast hcast

/-- Every accepted budget is at most the actual maximum. -/
theorem le_rsBudget_of_accepts_twelve {k M : ℕ} (hk : 12 ≤ k) (hA : RSAccepts k M) :
    M ≤ rsBudget k := by
  classical
  unfold rsBudget
  exact Finset.le_sup (f := id) (Finset.mem_filter.mpr
    ⟨Finset.mem_range.mpr (rsaAccepts_lt_twelve hk hA), hA⟩)

/-- The seed guarantees the finite accepted set is nonempty. -/
theorem seed_le_rsBudget_twelve {k : ℕ} (hk : 12 ≤ k) : 2^k ≤ rsBudget k :=
  le_rsBudget_of_accepts_twelve hk (seed_rsAccepts_twelve hk)

/-- The maximum is itself accepted, so an actual parameter witness exists. -/
theorem rsBudget_accepts_twelve {k : ℕ} (hk : 12 ≤ k) : RSAccepts k (rsBudget k) := by
  classical
  let S := (Finset.range (k*2^k)).filter (RSAccepts k)
  have hseed : 2^k ∈ S := Finset.mem_filter.mpr
    ⟨Finset.mem_range.mpr (rsaAccepts_lt_twelve hk (seed_rsAccepts_twelve hk)), seed_rsAccepts_twelve hk⟩
  obtain ⟨M, hM, heq⟩ := Finset.exists_mem_eq_sup S ⟨2^k, hseed⟩ id
  have hacc : RSAccepts k M := (Finset.mem_filter.mp hM).2
  change RSAccepts k (S.sup id)
  rw [heq]
  exact hacc

/-- The maximum retains the strict uniform upper bound. -/
theorem rsBudget_lt_twelve {k : ℕ} (hk : 12 ≤ k) : rsBudget k < k*2^k :=
  rsaAccepts_lt_twelve hk (rsBudget_accepts_twelve hk)

/-- Exact mathematical characterization of the maximum accepted integer. -/
theorem rsBudget_characterization_twelve {k : ℕ} (hk : 12 ≤ k) :
    RSAccepts k (rsBudget k) ∧ ∀ M : ℕ, RSAccepts k M → M ≤ rsBudget k :=
  ⟨rsBudget_accepts_twelve hk, fun _ hM => le_rsBudget_of_accepts_twelve hk hM⟩

/-- The maximum comes with an actual positive accepted parameter. -/
theorem rsBudget_parameter_twelve {k : ℕ} (hk : 12 ≤ k) :
    ∃ p : ℝ, 0 < p ∧ p ≤ 1 ∧ AcceptedAt k (rsBudget k) p := by
  obtain ⟨hBpos, p, hp⟩ := rsBudget_accepts_twelve hk
  exact ⟨p, acceptedAt_p_pos hBpos hp, hp.2.1, hp⟩


theorem sqrt_ge_sixtyfour {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    (64 : ℝ) ≤ Real.sqrt (M : ℝ) := by
  apply Real.le_sqrt_of_sq_le
  have hpow : 2 ^ 12 ≤ 2 ^ k := Nat.pow_le_pow_right (by omega) hk
  have h : 4096 ≤ M := by norm_num at hpow; omega
  exact_mod_cast h

theorem pow_four_le_nine_pow_two {k : ℕ} (hk : 12 ≤ k) : k ^ 4 ≤ 9 * 2 ^ k := by
  induction k, hk using Nat.le_induction with
  | base => norm_num
  | succ k hk ih =>
    have hstep : (k + 1) ^ 4 ≤ 2 * k ^ 4 := by
      obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hk
      nlinarith [Nat.zero_le (t ^ 4), Nat.zero_le (t ^ 3), Nat.zero_le (t ^ 2)]
    calc
      (k + 1) ^ 4 ≤ 2 * k ^ 4 := hstep
      _ ≤ 2 * (9 * 2 ^ k) := Nat.mul_le_mul_left 2 ih
      _ = 9 * 2 ^ (k + 1) := by rw [pow_succ]; ac_rfl

theorem square_le_three_sqrt {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    (k : ℝ) ^ 2 ≤ 3 * Real.sqrt (M : ℝ) := by
  have hNat := (pow_four_le_nine_pow_two hk).trans (Nat.mul_le_mul_left 9 hM)
  have h : (k : ℝ) ^ 4 ≤ 9 * (M : ℝ) := by exact_mod_cast hNat
  have hs := Real.sq_sqrt (show 0 ≤ (M : ℝ) by positivity)
  nlinarith [Real.sqrt_nonneg (M : ℝ)]

theorem gain_denominator_pos_twelve {k : ℕ} (hk : 12 ≤ k) :
    0 < 8 * (1 + Real.log (k : ℝ)) := by
  have hkreal : (1 : ℝ) ≤ k := by exact_mod_cast (show 1 ≤ k by omega)
  have hl := Real.log_nonneg hkreal
  linarith

theorem gain_denominator_le_sqrt_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    8 * (1 + Real.log (k : ℝ)) ≤ Real.sqrt (M : ℝ) := by
  by_cases h17 : 17 ≤ k
  · exact gain_denominator_le_sqrt h17 hM
  have hk16 : k ≤ 16 := by omega
  have hkR : (0 : ℝ) < k := by exact_mod_cast (show 0 < k by omega)
  have hl : Real.log (k : ℝ) ≤ 4 := by
    have hmono := Real.log_le_log hkR (show (k : ℝ) ≤ 16 by exact_mod_cast hk16)
    have hlog2 := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2)
    have heq : Real.log (16 : ℝ) = 4 * Real.log 2 := by
      rw [show (16 : ℝ) = 2 ^ 4 by norm_num, Real.log_pow]
      norm_num
    rw [heq] at hmono
    linarith
  have hs := sqrt_ge_sixtyfour hk hM
  linarith

/-- The gain is at least two throughout the enlarged range. -/
theorem integerGain_two_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    2 ≤ integerGain k M := by
  unfold integerGain
  apply (Nat.le_floor_iff' (by norm_num : (2 : ℕ) ≠ 0)).2
  norm_num only [Nat.cast_ofNat]
  apply (le_div_iff₀ (gain_denominator_pos_twelve hk)).2
  by_cases h17 : 17 ≤ k
  · have hkR : (17 : ℝ) ≤ k := by exact_mod_cast h17
    have hl := Real.log_le_sub_one_of_pos (by linarith : (0 : ℝ) < k)
    have hs := sqrt_ge_square h17 hM
    nlinarith
  · have hk16 : k ≤ 16 := by omega
    have hkR : (0 : ℝ) < k := by exact_mod_cast (show 0 < k by omega)
    have hl : Real.log (k : ℝ) ≤ 3 := by
      have hmono := Real.log_le_log hkR (show (k : ℝ) ≤ 16 by exact_mod_cast hk16)
      have heq : Real.log (16 : ℝ) = 4 * Real.log 2 := by
        rw [show (16 : ℝ) = 2 ^ 4 by norm_num, Real.log_pow]
        norm_num
      rw [heq] at hmono
      linarith [Real.log_two_lt_d9]
    have hs := sqrt_ge_sixtyfour hk hM
    linarith

theorem integerGain_pos_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    1 ≤ integerGain k M := by
  unfold integerGain
  apply (Nat.one_le_floor_iff _).2
  exact (le_div_iff₀ (gain_denominator_pos_twelve hk)).2 (by
    simpa using gain_denominator_le_sqrt_twelve hk hM)

theorem integerGain_le_quotient_twelve {k M : ℕ} (hk : 12 ≤ k) :
    (integerGain k M : ℝ) ≤ Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) := by
  apply Nat.floor_le
  exact div_nonneg (Real.sqrt_nonneg _) (gain_denominator_pos_twelve hk).le

theorem integerGain_le_budget_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    integerGain k M ≤ M := by
  have hs := integerGain_le_quotient_twelve (M := M) hk
  have hd := gain_denominator_pos_twelve hk
  have hl : 1 ≤ 8 * (1 + Real.log (k : ℝ)) := by
    have hlog := Real.log_nonneg (show (1 : ℝ) ≤ k by exact_mod_cast (show 1 ≤ k by omega))
    linarith
  have hq : Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) ≤ Real.sqrt (M : ℝ) :=
    div_le_self (Real.sqrt_nonneg _) hl
  have hroot : Real.sqrt (M : ℝ) ≤ M := by
    apply Real.sqrt_le_iff.2
    have hMr : (1 : ℝ) ≤ M := by
      exact_mod_cast (show 1 ≤ M from (one_le_pow₀ (by omega : 1 ≤ (2 : ℕ))).trans hM)
    constructor
    · positivity
    · nlinarith
  exact_mod_cast hs.trans (hq.trans hroot)

theorem budget_add_integerGain_le_twice_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    M + integerGain k M ≤ 2 * M := by
  have h := integerGain_le_budget_twelve hk hM
  omega

/-- Unified elementary inputs for the main growing-budget theorem. -/
theorem integerGain_bounds_twelve {k M : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M) :
    1 ≤ integerGain k M ∧
    (integerGain k M : ℝ) ≤ Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ))) ∧
    integerGain k M ≤ M ∧ M + integerGain k M ≤ 2 * M :=
  ⟨integerGain_pos_twelve hk hM, integerGain_le_quotient_twelve hk,
    integerGain_le_budget_twelve hk hM, budget_add_integerGain_le_twice_twelve hk hM⟩



theorem cliqueBudget_le_three_sqrt {k M N n : ℕ} (hk : 12 ≤ k)
    (hM : 2 ^ k ≤ M) (hN : N ≤ 2 * M)
    (hn : n * (n - 1) ≤ k * (k - 1) * N) :
    (cliqueBudget k n : ℝ) ≤ 3 * Real.sqrt (M : ℝ) := by
  have hs := square_le_three_sqrt hk hM
  have hs0 := Real.sqrt_nonneg (M : ℝ)
  have hfirstNat : k * k - k + 1 ≤ k ^ 2 := by
    have hkk : k ≤ k * k := by nlinarith
    simp only [pow_two]
    omega
  have hfirst : ((k * k - k + 1 : ℕ) : ℝ) ≤ 3 * Real.sqrt (M : ℝ) := by
    have ht : ((k * k - k + 1 : ℕ) : ℝ) ≤ (k : ℝ) ^ 2 := by exact_mod_cast hfirstNat
    linarith
  have hsqNat : (n - 1) ^ 2 ≤ k * (k - 1) * (2 * M) := by
    calc
      (n - 1) ^ 2 = (n - 1) * (n - 1) := pow_two _
      _ ≤ n * (n - 1) := Nat.mul_le_mul_right _ (Nat.sub_le n 1)
      _ ≤ k * (k - 1) * N := hn
      _ ≤ k * (k - 1) * (2 * M) := Nat.mul_le_mul_left _ hN
  have hsq : ((n - 1 : ℕ) : ℝ) ^ 2 ≤
      (k : ℝ) * ((k - 1 : ℕ) : ℝ) * (2 * (M : ℝ)) := by exact_mod_cast hsqNat
  have hkd : (k : ℝ) ≤ 2 * ((k - 1 : ℕ) : ℝ) := by
    exact_mod_cast (show k ≤ 2 * (k - 1) by omega)
  have hmul := mul_le_mul_of_nonneg_right hkd
    (show 0 ≤ 2 * ((k - 1 : ℕ) : ℝ) * (M : ℝ) by positivity)
  have hsquare := Real.sq_sqrt (show 0 ≤ (M : ℝ) by positivity)
  have htsq : ((n - 1 : ℕ) : ℝ) ^ 2 ≤
      (2 * ((k - 1 : ℕ) : ℝ) * Real.sqrt (M : ℝ)) ^ 2 := by
    simp only [mul_pow, hsquare]
    nlinarith only [hsq, hmul]
  have ht : ((n - 1 : ℕ) : ℝ) ≤ 2 * ((k - 1 : ℕ) : ℝ) * Real.sqrt (M : ℝ) :=
    (sq_le_sq₀ (by positivity) (by positivity)).1 htsq
  have hd : (0 : ℝ) < ((k - 1 : ℕ) : ℝ) := by exact_mod_cast (show 0 < k - 1 by omega)
  have hsecond : (((n - 1) / (k - 1) : ℕ) : ℝ) ≤ 2 * Real.sqrt (M : ℝ) := by
    calc
      (((n - 1) / (k - 1) : ℕ) : ℝ) ≤ ((n - 1 : ℕ) : ℝ) / ((k - 1 : ℕ) : ℝ) :=
        Nat.cast_div_le
      _ ≤ 2 * Real.sqrt (M : ℝ) := (div_le_iff₀ hd).2 (by nlinarith only [ht])
  simpa only [cliqueBudget, Nat.cast_max] using max_le hfirst (hsecond.trans (by nlinarith only [hs0]))


theorem cliqueBudget_gt_one_twelve {k : ℕ} (hk : 12 ≤ k) (n : ℕ) :
    (1 : ℝ) < (cliqueBudget k n : ℝ) := by
  have hkk : k + k ≤ k * k := by nlinarith
  have htwo : 1 < k * k - k + 1 := by omega
  have hmax : k * k - k + 1 ≤ cliqueBudget k n := le_max_left _ _
  exact_mod_cast htwo.trans_le hmax

/-- The actual integer gain has the strict logarithmic slack needed for the
RS perturbation, with all structural budget premises discharged internally. -/
theorem integerGain_log_slack_twelve {k M n : ℕ} (hk : 12 ≤ k) (hM : 2 ^ k ≤ M)
    (hn : n * (n - 1) ≤ k * (k - 1) * (M + integerGain k M)) :
    (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) + 2 <
      (M : ℝ) / (cliqueBudget k n : ℝ) := by
  have hd := gain_denominator_pos_twelve hk
  have hgain := integerGain_le_quotient_twelve (M := M) hk
  have hmul : 8 * (1 + Real.log (k : ℝ)) * (integerGain k M : ℝ) ≤
      Real.sqrt (M : ℝ) := by
    have h := (le_div_iff₀ hd).1 hgain
    nlinarith only [h]
  have hleft : (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) ≤
      Real.sqrt (M : ℝ) / 4 := by nlinarith only [hmul]
  have hs8 := sqrt_ge_sixtyfour hk hM
  have hstrict : (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) + 2 <
      Real.sqrt (M : ℝ) / 3 := by linarith
  have hrbound := cliqueBudget_le_three_sqrt hk hM
    (budget_add_integerGain_le_twice_twelve hk hM) hn
  have hrpos : (0 : ℝ) < (cliqueBudget k n : ℝ) :=
    lt_trans zero_lt_one (cliqueBudget_gt_one_twelve hk n)
  have hs0 := Real.sqrt_nonneg (M : ℝ)
  have hsq := Real.sq_sqrt (show 0 ≤ (M : ℝ) by positivity)
  have hprod := mul_le_mul_of_nonneg_left hrbound hs0
  have hright : Real.sqrt (M : ℝ) / 3 ≤ (M : ℝ) / (cliqueBudget k n : ℝ) := by
    apply (le_div_iff₀ hrpos).2
    nlinarith only [hprod, hsq]
  exact hstrict.trans_le hright


theorem propertyB_of_accepted_gain_twelve {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k M : ℕ} (hk : 12 ≤ k)
    (hu : Uniform E k) (hM : 2 ^ k ≤ M) {p : ℝ} (hA : AcceptedAt k M p)
    (hE : E.card ≤ M + integerGain k M) : PropertyB E := by
  have hM1 : 1 ≤ M := (Nat.one_le_pow k 2 (by decide)).trans hM
  have hp := acceptedAt_p_pos hM1 hA
  obtain ⟨_, _, _, hlog⟩ := acceptedAt_parameter_control_two (by omega) hM hA
  apply propertyB_of_structural_rs_bound E k (M + integerGain k M)
    (by omega) hu hE hp hA.2.1
  intro n _ hcount
  have hd : (0 : ℝ) < (2 : ℝ) ^ (k - 1) := by positivity
  have hMd : (2 : ℝ) * (2 : ℝ) ^ (k - 1) ≤ (M : ℝ) := by
    have hpow : (2 : ℝ) ^ k = 2 * (2 : ℝ) ^ (k - 1) := by
      conv_lhs => rw [show k = (k - 1) + 1 by omega]
      rw [pow_succ]
      ring
    rw [← hpow]
    exact_mod_cast hM
  have hM2 : (2 : ℝ) ≤ M := by
    have : (1 : ℝ) ≤ (2 : ℝ) ^ (k - 1) := one_le_pow₀ (by norm_num)
    linarith
  have hs : (0 : ℝ) < (integerGain k M : ℝ) := by
    exact_mod_cast integerGain_pos_twelve hk hM
  have h := rs_increment_of_log_slack (M : ℝ) (integerGain k M : ℝ)
    (cliqueBudget k n : ℝ) ((2 : ℝ) ^ (k - 1)) (ak k p) (jk k p)
    (Real.log (k : ℝ)) hM2 hs (cliqueBudget_gt_one_twelve hk n) hd
    (ak_pos (by omega) hp hA.2.1) (jk_nonneg k hp.le hA.2.1)
    hlog (integerGain_log_slack_twelve hk hM hcount) hA.2.2
  simpa only [Nat.cast_add, mul_comm] using h

/-- The full original coloring statement. The maximal budget and its accepted
parameter, minimum-counterexample structure and all probability estimates are
constructed internally; only uniformity and the stated edge budget remain. -/
theorem propertyB_of_general_growth_twelve {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k : ℕ} (hk : 12 ≤ k) (hu : Uniform E k)
    (hE : E.card ≤ rsBudget k + integerGain k (rsBudget k)) : PropertyB E := by
  obtain ⟨_, p, hp⟩ := rsBudget_accepts_twelve hk
  exact propertyB_of_accepted_gain_twelve E hk hu (seed_le_rsBudget_twelve hk) hp hE

/-- The equivalent lower bound on the edge count of every non-Property-B
hypergraph, expressed without introducing a separate minimization over graphs. -/
theorem non_propertyB_edges_ge_general_growth_twelve {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k : ℕ} (hk : 12 ≤ k) (hu : Uniform E k)
    (hnot : ¬ PropertyB E) :
    rsBudget k + integerGain k (rsBudget k) + 1 ≤ E.card := by
  by_contra h
  exact hnot (propertyB_of_general_growth_twelve E hk hu (by omega))


end
end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.rsBudget_characterization_twelve
#print axioms Aris4Math.General.RS.rsBudget_parameter_twelve
#print axioms Aris4Math.General.RS.integerGain_two_twelve
#print axioms Aris4Math.General.RS.propertyB_of_accepted_gain_twelve
#print axioms Aris4Math.General.RS.propertyB_of_general_growth_twelve
#print axioms Aris4Math.General.RS.non_propertyB_edges_ge_general_growth_twelve

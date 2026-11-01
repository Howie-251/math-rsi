import Aris4Math.General.Growth.Seed
import Aris4Math.General.Growth.ParameterControl
import Mathlib.Data.Finset.Lattice.Fold

namespace Aris4Math.General.RS
noncomputable section

/-- Every accepted integer budget lies below the uniform finite cutoff. -/
theorem rsaAccepts_lt {k M : ℕ} (hk : 17 ≤ k) (hA : RSAccepts k M) :
    M < k * 2^k := by
  by_cases hM : M < 2^k
  · have hcut : 2^k ≤ k*2^k := by
      calc
        2^k = 1 * 2^k := by simp
        _ ≤ k*2^k := Nat.mul_le_mul_right _ (by omega)
    exact hM.trans_le hcut
  · have hMb : 2^k ≤ M := Nat.le_of_not_gt hM
    obtain ⟨hMpos, p, hp⟩ := hA
    have hu := (acceptedAt_parameter_control hk hMb hp).2.2.1
    have hd : (0:ℝ) < (2:ℝ)^(k-1) := by positivity
    have hmul : (M:ℝ) < 2*(k:ℝ)*(2:ℝ)^(k-1) := (div_lt_iff₀ hd).mp hu
    have hpow : (2:ℝ)^k = 2*(2:ℝ)^(k-1) := by
      conv_lhs => rw [← Nat.sub_add_cancel (show 1 ≤ k by omega), pow_succ]
      ring
    have hcast : (M:ℝ) < ((k*2^k:ℕ):ℝ) := by
      rw [Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat, hpow]
      nlinarith only [hmul]
    exact_mod_cast hcast

/-- The maximum integer accepted by the precise RS criterion; the finite cutoff
is justified for `k≥17` by `rsaAccepts_lt`, rather than assumed. -/
def rsBudget (k : ℕ) : ℕ := by
  classical
  exact ((Finset.range (k*2^k)).filter (RSAccepts k)).sup id

/-- Every accepted budget is at most the actual maximum. -/
theorem le_rsBudget_of_accepts {k M : ℕ} (hk : 17 ≤ k) (hA : RSAccepts k M) :
    M ≤ rsBudget k := by
  classical
  unfold rsBudget
  exact Finset.le_sup (f := id) (Finset.mem_filter.mpr
    ⟨Finset.mem_range.mpr (rsaAccepts_lt hk hA), hA⟩)

/-- The seed guarantees the finite accepted set is nonempty. -/
theorem seed_le_rsBudget {k : ℕ} (hk : 17 ≤ k) : 2^k ≤ rsBudget k :=
  le_rsBudget_of_accepts hk (seed_rsAccepts hk)

/-- The maximum is itself accepted, so an actual parameter witness exists. -/
theorem rsBudget_accepts {k : ℕ} (hk : 17 ≤ k) : RSAccepts k (rsBudget k) := by
  classical
  let S := (Finset.range (k*2^k)).filter (RSAccepts k)
  have hseed : 2^k ∈ S := Finset.mem_filter.mpr
    ⟨Finset.mem_range.mpr (rsaAccepts_lt hk (seed_rsAccepts hk)), seed_rsAccepts hk⟩
  obtain ⟨M, hM, heq⟩ := Finset.exists_mem_eq_sup S ⟨2^k, hseed⟩ id
  have hacc : RSAccepts k M := (Finset.mem_filter.mp hM).2
  change RSAccepts k (S.sup id)
  rw [heq]
  exact hacc

/-- The maximum retains the strict uniform upper bound. -/
theorem rsBudget_lt {k : ℕ} (hk : 17 ≤ k) : rsBudget k < k*2^k :=
  rsaAccepts_lt hk (rsBudget_accepts hk)

/-- Exact mathematical characterization of the maximum accepted integer. -/
theorem rsBudget_characterization {k : ℕ} (hk : 17 ≤ k) :
    RSAccepts k (rsBudget k) ∧ ∀ M : ℕ, RSAccepts k M → M ≤ rsBudget k :=
  ⟨rsBudget_accepts hk, fun _ hM => le_rsBudget_of_accepts hk hM⟩

/-- The maximum comes with an actual positive accepted parameter. -/
theorem rsBudget_parameter {k : ℕ} (hk : 17 ≤ k) :
    ∃ p : ℝ, 0 < p ∧ p ≤ 1 ∧ AcceptedAt k (rsBudget k) p := by
  obtain ⟨hBpos, p, hp⟩ := rsBudget_accepts hk
  exact ⟨p, acceptedAt_p_pos hBpos hp, hp.2.1, hp⟩

end
end Aris4Math.General.RS

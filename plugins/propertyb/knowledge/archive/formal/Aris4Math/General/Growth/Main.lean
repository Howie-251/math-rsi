import Aris4Math.General.Structure.Main
import Aris4Math.General.Growth.Budget
import Aris4Math.General.Growth.Slack
import Aris4Math.General.Growth.LogStep

/-! The growing integer improvement over the maximal precise RS budget,
for every k ≥ 17 and every finite simple k-uniform hypergraph. -/
namespace Aris4Math.General.RS
universe u
noncomputable section

/-- Transfer the very same accepted parameter to the enlarged budget. -/
theorem propertyB_of_accepted_gain {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k M : ℕ} (hk : 17 ≤ k)
    (hu : Uniform E k) (hM : 2 ^ k ≤ M) {p : ℝ} (hA : AcceptedAt k M p)
    (hE : E.card ≤ M + integerGain k M) : PropertyB E := by
  have hM1 : 1 ≤ M := (Nat.one_le_pow k 2 (by decide)).trans hM
  have hp := acceptedAt_p_pos hM1 hA
  obtain ⟨_, _, _, hlog⟩ := acceptedAt_parameter_control hk hM hA
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
    exact_mod_cast integerGain_pos hk hM
  have h := rs_increment_of_log_slack (M : ℝ) (integerGain k M : ℝ)
    (cliqueBudget k n : ℝ) ((2 : ℝ) ^ (k - 1)) (ak k p) (jk k p)
    (Real.log (k : ℝ)) hM2 hs (cliqueBudget_gt_one hk n) hd
    (ak_pos (by omega) hp hA.2.1) (jk_nonneg k hp.le hA.2.1)
    hlog (integerGain_log_slack hk hM hcount) hA.2.2
  simpa only [Nat.cast_add, mul_comm] using h

/-- The full original coloring statement. The maximal budget and its accepted
parameter, minimum-counterexample structure and all probability estimates are
constructed internally; only uniformity and the stated edge budget remain. -/
theorem propertyB_of_general_growth {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k : ℕ} (hk : 17 ≤ k) (hu : Uniform E k)
    (hE : E.card ≤ rsBudget k + integerGain k (rsBudget k)) : PropertyB E := by
  obtain ⟨_, p, hp⟩ := rsBudget_accepts hk
  exact propertyB_of_accepted_gain E hk hu (seed_le_rsBudget hk) hp hE

/-- The equivalent lower bound on the edge count of every non-Property-B
hypergraph, expressed without introducing a separate minimization over graphs. -/
theorem non_propertyB_edges_ge_general_growth {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k : ℕ} (hk : 17 ≤ k) (hu : Uniform E k)
    (hnot : ¬ PropertyB E) :
    rsBudget k + integerGain k (rsBudget k) + 1 ≤ E.card := by
  by_contra h
  exact hnot (propertyB_of_general_growth E hk hu (by omega))

end
end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.propertyB_of_accepted_gain
#print axioms Aris4Math.General.RS.propertyB_of_general_growth
#print axioms Aris4Math.General.RS.non_propertyB_edges_ge_general_growth

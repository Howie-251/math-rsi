import Aris4Math.General.Structure.Reduction
import Aris4Math.General.Structure.Clique
import Aris4Math.General.Structure.Turan
import Aris4Math.General.Structure.ProbabilityBudget

/-! The whole structural spine: arbitrary original input, minimal counterexample,
actual single-intersection graph, Turán, and the proved RS coloring criterion. -/
namespace Aris4Math.General.RS

universe u
noncomputable section

theorem cliqueBudget_pos (k n : ℕ) : 0 < cliqueBudget k n := by
  unfold cliqueBudget
  omega

/-- Every auxiliary object is constructed from the original counterexample.
The only remaining premise is an explicit scalar condition over the possible
vertex counts, not an assumed structural or probabilistic certificate. -/
theorem propertyB_of_structural_rs_bound {V : Type u} [Finite V]
    (E : Finset (Finset V)) (k N : ℕ) (hk : 2 ≤ k)
    (hu : Uniform E k) (hm : E.card ≤ N)
    {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1)
    (hbound : ∀ n : ℕ, k ≤ n → n * (n - 1) ≤ k * (k - 1) * N →
      ((1 - 1 / (cliqueBudget k n : ℝ)) * (N : ℝ) ^ 2) /
        ((2 : ℝ) ^ (k - 1)) ^ 2 * jk k p <
        (ak k p) ^ ((N : ℝ) / (2 : ℝ) ^ (k - 1))) : PropertyB E := by
  classical
  by_contra hnB
  obtain ⟨n, K, hU, hM, hB, hP⟩ := exists_pair_covering_counterexample E hu hm hnB
  obtain ⟨_, hkn, hcount⟩ := pairCovering_vertex_bound K hU hM hB hP
  apply hB
  apply propertyB_of_rs_budget K k N hk hU hp hp1 hM
    (G := (1 - 1 / (cliqueBudget k n : ℝ)) * (N : ℝ) ^ 2)
  · have hg := gamma_le_cliqueBudget K hU hk
    simp only [Fintype.card_fin] at hg
    apply hg.trans
    have hr : (1 : ℝ) ≤ (cliqueBudget k n : ℝ) := by
      exact_mod_cast cliqueBudget_pos k n
    have hcoef : 0 ≤ 1 - 1 / (cliqueBudget k n : ℝ) := by
      have hrpos : (0 : ℝ) < (cliqueBudget k n : ℝ) := lt_of_lt_of_le zero_lt_one hr
      have : (1 : ℝ) / (cliqueBudget k n : ℝ) ≤ 1 := (div_le_one hrpos).mpr hr
      linarith
    apply mul_le_mul_of_nonneg_left _ hcoef
    have hmreal : (K.card : ℝ) ≤ (N : ℝ) := by exact_mod_cast hM
    have hprod := mul_nonneg (sub_nonneg.mpr hmreal)
      (show (0 : ℝ) ≤ (N : ℝ) + (K.card : ℝ) by positivity)
    nlinarith
  · exact hbound n hkn hcount

end
end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.gamma_le_cliqueBudget
#print axioms Aris4Math.General.RS.propertyB_of_structural_rs_bound

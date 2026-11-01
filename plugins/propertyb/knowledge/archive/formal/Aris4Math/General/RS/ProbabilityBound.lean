import Aris4Math.General.RS.UnionBound
import Aris4Math.General.RS.PairProbability
import Aris4Math.General.RS.Lift

/-! The actual RS failure bound, assembled from algorithmic coverage, positive
association, and the exact actual single-intersection pair probability. -/
namespace Aris4Math.General.RS

open scoped BigOperators
noncomputable section
attribute [local instance] Classical.propDecidable

universe u

/-- Sum over the actual directed single-intersection pairs and the two final colors.
The factor of two changes the one-color denominator into `d²`, with `d=2^(k-1)`. -/
theorem pair_probability_sum {n : ℕ} (E : Finset (Finset (Fin n))) (k : ℕ)
    (hk : 1 ≤ k) (hu : Uniform E k) (p : ℝ) :
    (∑ ef ∈ singlePairs E, ∑ q : Bool,
      sampleProb p (fun c b σ => PairEvent ef.1 ef.2 c b σ q)) =
      (gamma E : ℝ) / ((2 : ℝ)^(k-1))^2 * jk k p := by
  have hpairs (ef : Finset (Fin n) × Finset (Fin n)) (he : ef ∈ singlePairs E) :
      (∑ q : Bool, sampleProb p (fun c b σ => PairEvent ef.1 ef.2 c b σ q)) =
        2 * (jk k p / (2 : ℝ)^(2*k-1)) := by
    have he' := he
    simp only [singlePairs, Finset.mem_filter, Finset.mem_product] at he'
    have hcard : (ef.1 ∩ ef.2).card = 1 := by
      obtain ⟨x, hx⟩ := Finset.card_eq_one.mp he'.2.2
      apply Finset.card_eq_one.mpr
      refine ⟨x, ?_⟩
      ext z
      simpa only [Finset.mem_inter, Finset.mem_singleton] using Finset.ext_iff.mp hx z
    simp_rw [sampleProb_pairEvent ef.1 ef.2 hcard
      (hu _ he'.1.1) (hu _ he'.1.2) hk]
    simp
  rw [Finset.sum_congr rfl hpairs]
  simp only [Finset.sum_const, nsmul_eq_mul]
  change (gamma E : ℝ) * (2 * (jk k p / (2 : ℝ)^(2*k-1))) = _
  have hpow : (2 : ℝ)^(2*k-1) = 2 * ((2 : ℝ)^(k-1))^2 := by
    rw [show 2*k-1 = (k-1)+(k-1)+1 by omega, pow_add, pow_add]
    ring
  rw [hpow]
  field_simp

/-- The complete bound on the actual finite-index RS algorithm. -/
theorem rs_recoloring_failure_le_fin {n : ℕ} (E : Finset (Finset (Fin n)))
    (k : ℕ) (hk : 2 ≤ k) (hu : Uniform E k)
    {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    failureProb E p ≤
      1 - (ak k p)^((E.card : ℝ)/(2 : ℝ)^(k-1)) +
        (gamma E : ℝ) / ((2 : ℝ)^(k-1))^2 * jk k p := by
  have h := rs_union_bound E k hk hu hp hp1
  rw [pair_probability_sum E k (by omega) hu p] at h
  exact h

/-- Actual finite RS failure probability for arbitrary finite vertices.
Vertices are bijectively indexed by `Fin n`; the same original edge family is relabeled. -/
def rsFailureProbability {V : Type u} [Finite V] (E : Finset (Finset V)) (p : ℝ) : ℝ :=
  letI := Fintype.ofFinite V
  failureProb (relabel (Fintype.equivFin V) E) p

/-- The general original-object RS probability bound. Its edge count and gamma
are those of the original actual edge family, preserved by the indexing equivalence. -/
theorem rs_recoloring_failure_le {V : Type u} [Finite V]
    (E : Finset (Finset V)) (k : ℕ) (hk : 2 ≤ k) (hu : Uniform E k)
    {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    rsFailureProbability E p ≤
      1 - (ak k p)^((E.card : ℝ)/(2 : ℝ)^(k-1)) +
        (gamma E : ℝ) / ((2 : ℝ)^(k-1))^2 * jk k p := by
  letI := Fintype.ofFinite V
  let f := Fintype.equivFin V
  have h := rs_recoloring_failure_le_fin (relabel f E) k hk
    ((uniform_relabel_iff f E k).mpr hu) hp hp1
  simpa only [rsFailureProbability, f, relabel_card, gamma_relabel] using h

/-- Strictly subunit failure probability gives an actual two-coloring of the
original vertex type, by pulling the successful algorithm output back. -/
theorem propertyB_of_rsFailureProbability_lt_one {V : Type u} [Finite V]
    (E : Finset (Finset V)) (p : ℝ) (h : rsFailureProbability E p < 1) : PropertyB E := by
  letI := Fintype.ofFinite V
  let f := Fintype.equivFin V
  apply (propertyB_relabel_iff f E).mp
  apply propertyB_of_failureProb_lt_one (relabel f E) p
  exact h

/-- The RS sufficient criterion with no additional probability, coverage, or
certificate premise. Every event estimate is proved above for the actual algorithm. -/
theorem propertyB_of_rs_bound {V : Type u} [Finite V]
    (E : Finset (Finset V)) (k : ℕ) (hk : 2 ≤ k) (hu : Uniform E k)
    {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1)
    (hbound : 1 - (ak k p)^((E.card : ℝ)/(2 : ℝ)^(k-1)) +
      (gamma E : ℝ) / ((2 : ℝ)^(k-1))^2 * jk k p < 1) : PropertyB E := by
  apply propertyB_of_rsFailureProbability_lt_one E p
  exact (rs_recoloring_failure_le E k hk hu hp hp1).trans_lt hbound

end
end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.rs_recoloring_failure_le
#print axioms Aris4Math.General.RS.propertyB_of_rs_bound

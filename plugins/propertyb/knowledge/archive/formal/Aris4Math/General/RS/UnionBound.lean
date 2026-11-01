import Aris4Math.General.RS.Sample
import Aris4Math.General.RS.InitialAverage

namespace Aris4Math.General.RS

open scoped BigOperators
noncomputable section
attribute [local instance] Classical.propDecidable
variable {n : ℕ}

theorem failure_covered_singlePairs (E : Finset (Finset (Fin n))) (k : ℕ)
    (hk : 2 ≤ k) (hu : Uniform E k) (c b : Fin n → Bool)
    (σ : Equiv.Perm (Fin n)) (hfail : Failure E c b σ) :
    ResidualEvent E c b ∨
      ∃ ef ∈ singlePairs E, ∃ q : Bool, PairEvent ef.1 ef.2 c b σ q := by
  rcases failure_covered E k hk hu c b σ hfail with h | ⟨f, hf, g, hg, hfg, q, hq⟩
  · exact Or.inl h
  · refine Or.inr ⟨(f,g), ?_, q, hq⟩
    obtain ⟨x, hx, _⟩ := hq
    simp only [singlePairs, Finset.mem_filter, Finset.mem_product]
    refine ⟨⟨hf, hg⟩, hfg, Finset.card_eq_one.mpr ⟨x, ?_⟩⟩
    ext z
    simpa only [Finset.mem_inter, Finset.mem_singleton] using Finset.ext_iff.mp hx z

theorem residual_probability_le (E : Finset (Finset (Fin n))) (k : ℕ)
    (hk : 1 ≤ k) (hu : Uniform E k) {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    sampleProb p (fun c b _ => ResidualEvent E c b) ≤
      1 - (ak k p)^((E.card : ℝ)/(2:ℝ)^(k-1)) := by
  rw [sampleProb_no_order]
  exact initial_residual_average E k hk hu hp hp1

/-- Every actual algorithm failure is charged to the residual event or to an
ordered single-intersection pair of original edges and one of the two colors. -/
theorem rs_union_bound (E : Finset (Finset (Fin n))) (k : ℕ)
    (hk : 2 ≤ k) (hu : Uniform E k) {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    failureProb E p ≤ 1 - (ak k p)^((E.card : ℝ)/(2:ℝ)^(k-1)) +
      ∑ ef ∈ singlePairs E, ∑ q : Bool,
        sampleProb p (fun c b σ => PairEvent ef.1 ef.2 c b σ q) := by
  let P := fun (ef : Finset (Fin n) × Finset (Fin n)) c b σ =>
    ∃ q : Bool, PairEvent ef.1 ef.2 c b σ q
  have hcover := sampleProb_mono hp.le hp1 (fun c b σ h =>
    failure_covered_singlePairs E k hk hu c b σ h)
  have hpair : sampleProb p (fun c b σ => ∃ ef ∈ singlePairs E, P ef c b σ) ≤
      ∑ ef ∈ singlePairs E, ∑ q : Bool,
        sampleProb p (fun c b σ => PairEvent ef.1 ef.2 c b σ q) := by
    refine (sampleProb_finset_union_le hp.le hp1 (singlePairs E) P).trans ?_
    apply Finset.sum_le_sum
    intro ef _
    simpa only [Finset.mem_univ, true_and, P] using
      sampleProb_finset_union_le hp.le hp1 (Finset.univ : Finset Bool)
        (fun q c b σ => PairEvent ef.1 ef.2 c b σ q)
  exact hcover.trans ((sampleProb_union_le hp.le hp1
    (fun c b _ => ResidualEvent E c b)
    (fun c b σ => ∃ ef ∈ singlePairs E, P ef c b σ)).trans
      (add_le_add (residual_probability_le E k (by omega) hu hp hp1) hpair))

end
end Aris4Math.General.RS

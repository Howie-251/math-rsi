import Aris4Math.General.RS.Definitions
import Aris4Math.General.RS.Bernoulli
import Aris4Math.General.RS.Integral
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Analysis.Convex.SpecificFunctions.Basic

noncomputable section
open scoped BigOperators
namespace Aris4Math.General.RS
attribute [local instance] Classical.propDecidable

/-- Number of monochromatic actual edges in the initial coloring. -/
def monoCount {V : Type*} (E : Finset (Finset V)) (c : V → Bool) : ℕ :=
  (E.filter (fun e => ∃ q : Bool, Mono e c q)).card

lemma monoCount_cast {V : Type*} (E : Finset (Finset V)) (c : V → Bool) :
    (monoCount E c : ℝ) = ∑ e ∈ E, if ∃ q : Bool, Mono e c q then (1 : ℝ) else 0 := by
  classical
  unfold monoCount
  rw [Finset.card_eq_sum_ones, Nat.cast_sum, Finset.sum_filter]
  simp only [Nat.cast_one]

/-- Exact probability for either fixed initial color on an actual edge. -/
lemma bernoulliProb_mono_color {V : Type*} [Fintype V] (e : Finset V) (q : Bool) :
    bernoulliProb (1/2) (fun c => Mono e c q) = (1/2 : ℝ)^e.card := by
  classical
  unfold bernoulliProb
  trans bernoulliExpect (1/2) (fun c => ∏ v, if v ∈ e → c v = q then (1 : ℝ) else 0)
  · congr 1
    funext c
    rw [Fintype.prod_boole]
    simp only [Mono]
    split_ifs <;> rfl
  rw [bernoulliExpect_coordinate_prod (1/2)
    (fun v a => if v ∈ e → a = q then (1 : ℝ) else 0)]
  trans ∏ v : V, if v ∈ e then (1/2 : ℝ) else 1
  · apply Finset.prod_congr rfl
    intro v _
    by_cases hv : v ∈ e <;> cases q <;> norm_num [hv]
  · simp

/-- A nonempty actual edge is monochromatic with probability exactly 2^(1-|e|). -/
lemma initial_mono_probability {V : Type*} [Fintype V] (e : Finset V) (he : e.Nonempty) :
    bernoulliProb (1/2) (fun c => ∃ q : Bool, Mono e c q) = 2 * (1/2 : ℝ)^e.card := by
  have hd (c : V → Bool) : ¬ (Mono e c false ∧ Mono e c true) := by
    rintro ⟨hf, ht⟩
    obtain ⟨v, hv⟩ := he
    exact Bool.false_ne_true ((hf v hv).symm.trans (ht v hv))
  have hi (c : V → Bool) :
      (if ∃ q : Bool, Mono e c q then (1:ℝ) else 0) =
      (if Mono e c false then (1:ℝ) else 0) +
        (if Mono e c true then 1 else 0) := by
    by_cases hf : Mono e c false <;> by_cases ht : Mono e c true
    · exact (hd c ⟨hf, ht⟩).elim
    · simp [Bool.exists_bool, hf, ht]
    · simp [Bool.exists_bool, hf, ht]
    · simp [Bool.exists_bool, hf, ht]
  unfold bernoulliProb
  trans bernoulliExpect (1/2) (fun c =>
    (if Mono e c false then (1:ℝ) else 0) + (if Mono e c true then 1 else 0))
  · congr 1
    funext c
    convert hi c using 1
    split_ifs <;> rfl
  rw [bernoulliExpect_add]

  change bernoulliProb (1/2) (fun c => Mono e c false) +
    bernoulliProb (1/2) (fun c => Mono e c true) = _
  rw [bernoulliProb_mono_color, bernoulliProb_mono_color]
  ring

/-- Exact average of the number of monochromatic actual edges, with no vertex
or overlap restrictions on the uniform hypergraph. -/
lemma initial_monoCount_average {V : Type*} [Fintype V] (E : Finset (Finset V))
    (k : ℕ) (hk : 1 ≤ k) (hE : Uniform E k) :
    bernoulliExpect (1/2) (fun c => (monoCount E c : ℝ)) =
      (E.card : ℝ) / (2 : ℝ)^(k-1) := by
  classical
  have hl : bernoulliExpect (1/2) (fun c => (monoCount E c : ℝ)) =
      ∑ e ∈ E, bernoulliProb (1/2) (fun c => ∃ q : Bool, Mono e c q) := by
    simp_rw [monoCount_cast]
    simp only [bernoulliProb, bernoulliExpect]
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro e he
    apply Finset.sum_congr rfl
    intro c hc
    congr 1
    split_ifs <;> rfl
  rw [hl]
  have hprob (e : Finset V) (he : e ∈ E) :
      bernoulliProb (1/2) (fun c => ∃ q : Bool, Mono e c q) = 2*(1/2 : ℝ)^k := by
    have hne : e.Nonempty := Finset.card_pos.mp (by rw [hE e he]; omega)
    rw [initial_mono_probability e hne, hE e he]
  simp_rw [Finset.sum_congr rfl (fun e he => hprob e he)]
  simp only [Finset.sum_const, nsmul_eq_mul]
  rw [div_pow]
  simp only [one_pow]
  rw [show k = (k-1)+1 by omega, pow_succ]
  simp only [Nat.add_sub_cancel]
  field_simp

/-- Finite weighted Jensen for the exponential form a^x. -/
lemma bernoulliExpect_rpow_ge {V : Type*} [Fintype V] {p a : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (ha : 0 < a) (f : (V → Bool) → ℝ) :
    a ^ (bernoulliExpect p f) ≤ bernoulliExpect p (fun c => a ^ (f c)) := by
  have h := convexOn_exp.map_sum_le
    (t := Finset.univ) (w := bernoulliWeight (V := V) p)
    (p := fun c => f c * Real.log a)
    (fun c _ => bernoulliWeight_nonneg hp hp1 c) (sum_bernoulliWeight p)
    (fun c _ => Set.mem_univ _)
  simp only [smul_eq_mul] at h
  have hs : (∑ c : V → Bool, bernoulliWeight p c * (f c * Real.log a)) =
      bernoulliExpect p f * Real.log a := by
    simp [bernoulliExpect, Finset.sum_mul, mul_assoc]
  rw [hs] at h
  simpa only [Real.rpow_def_of_pos ha, mul_comm, bernoulliExpect] using h

/-- Actual initial-color caller of Jensen, using the exact edge-count average. -/
lemma initial_power_average {V : Type*} [Fintype V] (E : Finset (Finset V))
    (k : ℕ) (hk : 1 ≤ k) (hE : Uniform E k) {a : ℝ} (ha : 0 < a) :
    a ^ ((E.card : ℝ)/(2:ℝ)^(k-1)) ≤
      bernoulliExpect (1/2) (fun c => a ^ (monoCount E c : ℝ)) := by
  have h := bernoulliExpect_rpow_ge (V := V) (by norm_num : (0:ℝ) ≤ 1/2)
    (by norm_num : (1/2:ℝ) ≤ 1) ha (fun c => (monoCount E c : ℝ))
  rw [initial_monoCount_average E k hk hE] at h
  exact h

/-- Conditional residual bound: overlapping initial monochromatic edges are
handled by positive association, not by an independence assumption. -/
lemma initial_residual_conditional {V : Type*} [Fintype V] (E : Finset (Finset V))
    (k : ℕ) (hE : Uniform E k) {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1) (c : V → Bool) :
    bernoulliProb p (fun b => ∃ e ∈ E, (∃ q : Bool, Mono e c q) ∧
      ∀ x ∈ e, b x = false) ≤ 1 - (ak k p)^(monoCount E c) := by
  classical
  let F := E.filter (fun e => ∃ q : Bool, Mono e c q)
  have hh := bernoulliProb_all_edges_hit hp hp1 F
  have hprod : (∏ e ∈ F, (1-(1-p)^e.card)) = (ak k p)^(monoCount E c) := by
    trans ∏ e ∈ F, ak k p
    · apply Finset.prod_congr rfl
      intro e he
      rw [hE e (Finset.mem_filter.mp he).1]
      rfl
    · simp [monoCount, F]
  rw [hprod] at hh
  have heq : (fun b : V → Bool => ∃ e ∈ E, (∃ q : Bool, Mono e c q) ∧
      ∀ x ∈ e, b x = false) =
      (fun b => ¬ ∀ e ∈ F, ∃ x ∈ e, b x = true) := by
    funext b
    apply propext
    constructor
    · rintro ⟨e, he, hmono, hb⟩ hall
      obtain ⟨x, hx, hbx⟩ := hall e (Finset.mem_filter.mpr ⟨he,hmono⟩)
      exact Bool.false_ne_true ((hb x hx).symm.trans hbx)
    · intro hn
      simp only [not_forall, exists_prop] at hn
      obtain ⟨e, he, hnot⟩ := hn
      obtain ⟨heE, hmono⟩ := Finset.mem_filter.mp he
      refine ⟨e, heE, hmono, ?_⟩
      intro x hx
      cases hbx : b x
      · rfl
      · exact (hnot ⟨x,hx,hbx⟩).elim
  rw [heq, bernoulliProb_compl]
  linarith

/-- Actual two-stage initial-color/eligibility average for the residual event. -/
lemma initial_residual_average {V : Type*} [Fintype V] (E : Finset (Finset V))
    (k : ℕ) (hk : 1 ≤ k) (hE : Uniform E k) {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    bernoulliExpect (1/2) (fun c => bernoulliProb p (fun b =>
      ∃ e ∈ E, (∃ q : Bool, Mono e c q) ∧ ∀ x ∈ e, b x = false)) ≤
      1 - (ak k p)^((E.card : ℝ)/(2:ℝ)^(k-1)) := by
  have hc := bernoulliExpect_mono (V := V) (by norm_num : (0:ℝ) ≤ 1/2)
    (by norm_num : (1/2:ℝ) ≤ 1)
    (fun c => initial_residual_conditional E k hE hp.le hp1 c)
  have he : bernoulliExpect (1/2) (fun c : V → Bool => 1 - (ak k p)^(monoCount E c)) =
      1 - bernoulliExpect (1/2) (fun c => (ak k p)^(monoCount E c)) := by
    unfold bernoulliExpect
    simp_rw [mul_sub, mul_one, Finset.sum_sub_distrib]
    rw [sum_bernoulliWeight]
  rw [he] at hc
  have hj := initial_power_average E k hk hE (ak_pos (by omega : 0 < k) hp hp1)
  simp only [Real.rpow_natCast] at hj
  linarith

end Aris4Math.General.RS

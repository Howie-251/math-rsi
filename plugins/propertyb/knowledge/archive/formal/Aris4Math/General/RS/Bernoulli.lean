import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.GroupWithZero.Finset
import Mathlib.Data.Fintype.Option
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Tactic.Linarith

/-! Finite product Bernoulli weights and Harris positive association. -/
namespace Aris4Math.General.RS
open scoped BigOperators

noncomputable section
attribute [local instance] Classical.propDecidable

/-- Weight of one eligibility bit. -/
def bitWeight (p : ℝ) (b : Bool) : ℝ := if b then p else 1 - p

/-- Product Bernoulli weight on the actual finite vertex set. -/
def bernoulliWeight {V : Type*} [Fintype V] (p : ℝ) (b : V → Bool) : ℝ :=
  ∏ v, bitWeight p (b v)

/-- Finite weighted expectation. -/
def bernoulliExpect {V : Type*} [Fintype V] (p : ℝ) (f : (V → Bool) → ℝ) : ℝ :=
  ∑ b, bernoulliWeight p b * f b

@[simp] theorem bitWeight_false (p : ℝ) : bitWeight p false = 1 - p := rfl
@[simp] theorem bitWeight_true (p : ℝ) : bitWeight p true = p := rfl

 theorem bitWeight_nonneg {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1) (b : Bool) :
    0 ≤ bitWeight p b := by cases b <;> simp [hp, sub_nonneg.mpr hp1]

 theorem bernoulliWeight_nonneg {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (b : V → Bool) : 0 ≤ bernoulliWeight p b :=
by
  classical
  unfold bernoulliWeight
  have h (s : Finset V) : 0 ≤ ∏ v ∈ s, bitWeight p (b v) := by
    induction s using Finset.induction with
    | empty => simp
    | @insert v s hv ih =>
      rw [Finset.prod_insert hv]
      exact mul_nonneg (bitWeight_nonneg hp hp1 _) ih
  exact h Finset.univ

@[simp] theorem sum_bernoulliWeight {V : Type*} [Fintype V] (p : ℝ) :
    ∑ b : V → Bool, bernoulliWeight p b = 1 := by
  classical
  unfold bernoulliWeight
  rw [← Fintype.prod_sum]
  simp

@[simp] theorem bernoulliExpect_const {V : Type*} [Fintype V] (p c : ℝ) :
    bernoulliExpect (V := V) p (fun _ => c) = c := by
  simp [bernoulliExpect, ← Finset.sum_mul]

 theorem bernoulliExpect_add {V : Type*} [Fintype V] (p : ℝ)
    (f g : (V → Bool) → ℝ) :
    bernoulliExpect p (fun b => f b + g b) = bernoulliExpect p f + bernoulliExpect p g := by
  simp [bernoulliExpect, mul_add, Finset.sum_add_distrib]

 theorem bernoulliExpect_mul_const {V : Type*} [Fintype V] (p c : ℝ)
    (f : (V → Bool) → ℝ) :
    bernoulliExpect p (fun b => f b * c) = bernoulliExpect p f * c := by
  simp [bernoulliExpect, mul_assoc, Finset.sum_mul]

 theorem bernoulliExpect_const_mul {V : Type*} [Fintype V] (p c : ℝ)
    (f : (V → Bool) → ℝ) :
    bernoulliExpect p (fun b => c * f b) = c * bernoulliExpect p f := by
  simpa [mul_comm] using bernoulliExpect_mul_const p c f

 theorem bernoulliExpect_mono {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) {f g : (V → Bool) → ℝ} (h : ∀ b, f b ≤ g b) :
    bernoulliExpect p f ≤ bernoulliExpect p g := by
  exact Finset.sum_le_sum fun b _ => mul_le_mul_of_nonneg_left (h b)
    (bernoulliWeight_nonneg hp hp1 b)

 theorem bernoulliExpect_nonneg {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) {f : (V → Bool) → ℝ} (h : ∀ b, 0 ≤ f b) :
    0 ≤ bernoulliExpect p f := by
  simpa using bernoulliExpect_mono hp hp1 h

/-- The reindexing equivalence used for coordinate induction. -/
def cubeEquiv {V W : Type*} (e : V ≃ W) : (V → Bool) ≃ (W → Bool) where
  toFun b := b ∘ e.symm
  invFun b := b ∘ e
  left_inv b := by funext v; simp
  right_inv b := by funext w; simp

 theorem bernoulliWeight_equiv {V W : Type*} [Fintype V] [Fintype W]
    (e : V ≃ W) (p : ℝ) (b : W → Bool) :
    bernoulliWeight p (b ∘ e) = bernoulliWeight p b := by
  classical
  exact Fintype.prod_equiv e _ _ fun _ => rfl

 theorem bernoulliExpect_equiv {V W : Type*} [Fintype V] [Fintype W]
    (e : V ≃ W) (p : ℝ) (f : (W → Bool) → ℝ) :
    bernoulliExpect p (fun b => f (cubeEquiv e b)) = bernoulliExpect p f := by
  classical
  unfold bernoulliExpect
  apply Fintype.sum_equiv (cubeEquiv e)
  intro b
  have hw := bernoulliWeight_equiv e p (cubeEquiv e b)
  simpa [cubeEquiv, Function.comp_def] using congrArg (fun w => w * f (cubeEquiv e b)) hw

/-- Fix the new coordinate and keep all old coordinates. -/
def cubeCons {V : Type*} (a : Bool) (b : V → Bool) : Option V → Bool :=
  fun v => Option.casesOn v a b

@[simp] theorem cubeCons_none {V : Type*} (a : Bool) (b : V → Bool) :
    cubeCons a b none = a := rfl
@[simp] theorem cubeCons_some {V : Type*} (a : Bool) (b : V → Bool) (v : V) :
    cubeCons a b (some v) = b v := rfl

 theorem cubeCons_mono {V : Type*} {a a' : Bool} {b b' : V → Bool}
    (ha : a ≤ a') (hb : b ≤ b') : cubeCons a b ≤ cubeCons a' b' := by
  intro v; cases v with
  | none => exact ha
  | some v => exact hb v

@[simp] theorem bernoulliWeight_cons {V : Type*} [Fintype V] (p : ℝ)
    (a : Bool) (b : V → Bool) :
    bernoulliWeight p (cubeCons a b) = bitWeight p a * bernoulliWeight p b := by
  simp [bernoulliWeight, Fintype.prod_option, cubeCons]

 theorem bernoulliExpect_option {V : Type*} [Fintype V] (p : ℝ)
    (f : (Option V → Bool) → ℝ) :
    bernoulliExpect p f = (1-p) * bernoulliExpect p (fun b => f (cubeCons false b)) +
      p * bernoulliExpect p (fun b => f (cubeCons true b)) := by
  classical
  letI : DecidableEq (Option V) := Classical.decEq _
  unfold bernoulliExpect
  rw [Fintype.sum_equiv Equiv.piOptionEquivProd _
    (fun ab : Bool × (V → Bool) =>
      bitWeight p ab.1 * bernoulliWeight p ab.2 * f (cubeCons ab.1 ab.2))]
  · simp [Fintype.sum_prod_type, ← Finset.mul_sum, mul_assoc, add_comm]
  · intro b
    have hc : cubeCons (b none) (fun v => b (some v)) = b := by
      funext v; cases v <;> rfl
    simpa only [Equiv.piOptionEquivProd_apply, hc] using
      congrArg (fun w => w * f b) (bernoulliWeight_cons p (b none) (fun v => b (some v)))

/-- Harris inequality for arbitrary real-valued increasing functions and every
Bernoulli parameter in `[0,1]`; no independence between the two functions is assumed. -/
theorem bernoulli_harris {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (f g : (V → Bool) → ℝ)
    (hf : Monotone f) (hg : Monotone g) :
    bernoulliExpect p f * bernoulliExpect p g ≤
      bernoulliExpect p (fun b => f b * g b) := by
  classical
  revert f g
  refine Fintype.induction_empty_option (P := fun V _ =>
    ∀ (f g : (V → Bool) → ℝ), Monotone f → Monotone g →
    bernoulliExpect p f * bernoulliExpect p g ≤ bernoulliExpect p (fun b => f b * g b))
    ?_ ?_ ?_ V
  · intro V W _ e ih f g hf hg
    letI : Fintype V := Fintype.ofEquiv W e.symm
    have hm : Monotone (cubeEquiv e) := by
      intro b c h w
      exact h (e.symm w)
    have h := ih (fun b => f (cubeEquiv e b)) (fun b => g (cubeEquiv e b))
      (hf.comp hm) (hg.comp hm)
    rw [bernoulliExpect_equiv, bernoulliExpect_equiv] at h
    change bernoulliExpect p f * bernoulliExpect p g ≤
      bernoulliExpect p (fun b => (fun c => f c * g c) (cubeEquiv e b)) at h
    rw [bernoulliExpect_equiv e p (fun c => f c * g c)] at h
    exact h
  · intro f g hf hg
    simp [bernoulliExpect, bernoulliWeight]
  · intro V _ ih f g hf hg
    have hm (a : Bool) : Monotone (cubeCons (V := V) a) :=
      fun _ _ h => cubeCons_mono le_rfl h
    have ih0 := ih (fun b => f (cubeCons false b)) (fun b => g (cubeCons false b))
      (hf.comp (hm false)) (hg.comp (hm false))
    have ih1 := ih (fun b => f (cubeCons true b)) (fun b => g (cubeCons true b))
      (hf.comp (hm true)) (hg.comp (hm true))
    have hF : bernoulliExpect p (fun b => f (cubeCons false b)) ≤
        bernoulliExpect p (fun b => f (cubeCons true b)) :=
      bernoulliExpect_mono hp hp1 fun b => hf (cubeCons_mono (by decide) le_rfl)
    have hG : bernoulliExpect p (fun b => g (cubeCons false b)) ≤
        bernoulliExpect p (fun b => g (cubeCons true b)) :=
      bernoulliExpect_mono hp hp1 fun b => hg (cubeCons_mono (by decide) le_rfl)
    have h0 := mul_le_mul_of_nonneg_left ih0 (sub_nonneg.mpr hp1)
    have h1 := mul_le_mul_of_nonneg_left ih1 hp
    have hcov := mul_nonneg (mul_nonneg (mul_nonneg hp (sub_nonneg.mpr hp1))
      (sub_nonneg.mpr hF)) (sub_nonneg.mpr hG)
    rw [bernoulliExpect_option p f, bernoulliExpect_option p g,
      bernoulliExpect_option p (fun b => f b * g b)]
    nlinarith

/-- Probability of an event under the finite Bernoulli product law. -/
def bernoulliProb {V : Type*} [Fintype V] (p : ℝ) (P : (V → Bool) → Prop) : ℝ :=
  bernoulliExpect p (fun b => if P b then 1 else 0)

 theorem bernoulliProb_nonneg {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (P : (V → Bool) → Prop) :
    0 ≤ bernoulliProb p P :=
  bernoulliExpect_nonneg hp hp1 fun b => by split_ifs <;> norm_num

@[simp] theorem bernoulliProb_true {V : Type*} [Fintype V] (p : ℝ) :
    bernoulliProb (V := V) p (fun _ => True) = 1 := by simp [bernoulliProb]

@[simp] theorem bernoulliProb_false {V : Type*} [Fintype V] (p : ℝ) :
    bernoulliProb (V := V) p (fun _ => False) = 0 := by simp [bernoulliProb]

 theorem bernoulliProb_mono {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) {P Q : (V → Bool) → Prop}
    (h : ∀ b, P b → Q b) : bernoulliProb p P ≤ bernoulliProb p Q := by
  apply bernoulliExpect_mono hp hp1
  intro b
  by_cases hP : P b
  · simp [hP, h b hP]
  · simp [hP]; split_ifs <;> norm_num

 theorem bernoulliProb_le_one {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (P : (V → Bool) → Prop) :
    bernoulliProb p P ≤ 1 := by
  simpa using bernoulliProb_mono hp hp1 (P := P) (Q := fun _ => True) (fun _ _ => trivial)

/-- Event form of weighted Harris association. -/
theorem bernoulli_harris_event {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (P Q : (V → Bool) → Prop)
    (hP : ∀ b c, b ≤ c → P b → P c) (hQ : ∀ b c, b ≤ c → Q b → Q c) :
    bernoulliProb p P * bernoulliProb p Q ≤ bernoulliProb p (fun b => P b ∧ Q b) := by
  have hm (R : (V → Bool) → Prop) (hR : ∀ b c, b ≤ c → R b → R c) :
      Monotone (fun b => if R b then (1 : ℝ) else 0) := by
    intro b c hbc
    by_cases hb : R b
    · simp [hb, hR b c hbc hb]
    · simp [hb]; split_ifs <;> norm_num
  have h := bernoulli_harris hp hp1 _ _ (hm P hP) (hm Q hQ)
  have heq : (fun b => (if P b then (1 : ℝ) else 0) * (if Q b then 1 else 0)) =
      (fun b => if P b ∧ Q b then 1 else 0) := by
    funext b; by_cases hPb : P b <;> by_cases hQb : Q b <;> simp [hPb, hQb]
  change bernoulliProb p P * bernoulliProb p Q ≤ _ at h
  refine h.trans_eq ?_
  unfold bernoulliProb
  congr 1
  funext b
  by_cases hPb : P b <;> by_cases hQb : Q b <;> simp [hPb, hQb]

/-- Factorization applies to functions of distinct coordinates only. -/
theorem bernoulliExpect_coordinate_prod {V : Type*} [Fintype V] (p : ℝ)
    (q : V → Bool → ℝ) :
    bernoulliExpect p (fun b => ∏ v, q v (b v)) =
      ∏ v, ((1-p) * q v false + p * q v true) := by
  classical
  unfold bernoulliExpect bernoulliWeight
  simp_rw [← Finset.prod_mul_distrib]
  calc
    _ = ∏ v, ∑ a : Bool, bitWeight p a * q v a :=
      (Fintype.prod_sum (fun v a => bitWeight p a * q v a)).symm
    _ = _ := by simp [add_comm]

 theorem bernoulliProb_compl {V : Type*} [Fintype V] (p : ℝ)
    (P : (V → Bool) → Prop) :
    bernoulliProb p (fun b => ¬ P b) = 1 - bernoulliProb p P := by
  have h := bernoulliExpect_add p (fun b => if ¬P b then (1 : ℝ) else 0)
    (fun b => if P b then (1 : ℝ) else 0)
  have he : (fun b => (if ¬P b then (1 : ℝ) else 0) + (if P b then 1 else 0)) =
      (fun _ => 1) := by
    funext b; by_cases hb : P b <;> simp [hb]
  rw [he, bernoulliExpect_const] at h
  have hn : bernoulliProb p (fun b => ¬ P b) =
      bernoulliExpect p (fun b => if ¬P b then (1 : ℝ) else 0) := by
    unfold bernoulliProb
    congr 1
    funext b
    by_cases hb : P b <;> simp [hb]
  rw [hn]
  unfold bernoulliProb
  linarith

 theorem bernoulliProb_union_le {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (P Q : (V → Bool) → Prop) :
    bernoulliProb p (fun b => P b ∨ Q b) ≤ bernoulliProb p P + bernoulliProb p Q := by
  unfold bernoulliProb
  rw [← bernoulliExpect_add]
  apply bernoulliExpect_mono hp hp1
  intro b
  by_cases hP : P b <;> by_cases hQ : Q b <;> simp [hP, hQ]

/-- The probability being below one supplies an actual successful bit assignment. -/
theorem exists_not_of_bernoulliProb_lt_one {V : Type*} [Fintype V] {p : ℝ}
    (P : (V → Bool) → Prop) (h : bernoulliProb p P < 1) : ∃ b, ¬ P b := by
  by_contra hn
  have hall : ∀ b, P b := by simpa using hn
  have heq : P = (fun _ => True) := by funext b; exact propext ⟨fun _ => trivial, fun _ => hall b⟩
  rw [heq, bernoulliProb_true] at h
  exact lt_irrefl _ h

/-- Positive association for any finite family of increasing events. -/
theorem bernoulli_harris_events {V I : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (s : Finset I) (P : I → (V → Bool) → Prop)
    (hP : ∀ i ∈ s, ∀ b c, b ≤ c → P i b → P i c) :
    (∏ i ∈ s, bernoulliProb p (P i)) ≤ bernoulliProb p (fun b => ∀ i ∈ s, P i b) := by
  classical
  induction s using Finset.induction with
  | empty => simp
  | @insert i s hi ih =>
    rw [Finset.prod_insert hi]
    have hh := bernoulli_harris_event hp hp1 (P i) (fun b => ∀ j ∈ s, P j b)
      (hP i (Finset.mem_insert_self i s))
      (fun b c hbc hb j hj => hP j (Finset.mem_insert_of_mem hj) b c hbc (hb j hj))
    have hm := mul_le_mul_of_nonneg_left (ih (fun j hj => hP j (Finset.mem_insert_of_mem hj)))
      (bernoulliProb_nonneg hp hp1 (P i))
    refine hm.trans (hh.trans_eq ?_)
    congr 1
    funext b
    exact propext (by simp)

/-- Exact no-hit probability for a specified actual set of vertices. -/
theorem bernoulliProb_all_false {V : Type*} [Fintype V] (p : ℝ) (s : Finset V) :
    bernoulliProb p (fun b => ∀ v ∈ s, b v = false) = (1-p) ^ s.card := by
  classical
  unfold bernoulliProb
  trans bernoulliExpect p (fun b => ∏ v, if v ∈ s → b v = false then (1 : ℝ) else 0)
  · congr 1
    funext b
    rw [Fintype.prod_boole]
    by_cases hb : ∀ v ∈ s, b v = false <;> simp [hb]
  rw [bernoulliExpect_coordinate_prod p (fun v a => if v ∈ s → a = false then (1 : ℝ) else 0)]
  trans ∏ v : V, if v ∈ s then 1-p else 1
  · apply Finset.prod_congr rfl
    intro v _
    by_cases hv : v ∈ s <;> simp [hv]
  · simp

/-- Eligibility hits a specified edge with probability `1-(1-p)^|e|`. -/
theorem bernoulliProb_hits {V : Type*} [Fintype V] (p : ℝ) (s : Finset V) :
    bernoulliProb p (fun b => ∃ v ∈ s, b v = true) = 1 - (1-p) ^ s.card := by
  have heq : (fun b : V → Bool => ∃ v ∈ s, b v = true) =
      (fun b => ¬ (∀ v ∈ s, b v = false)) := by
    funext b
    apply propext
    simp only [not_forall, exists_prop]
    constructor
    · rintro ⟨v, hv, hb⟩; exact ⟨v, hv, by simp [hb]⟩
    · rintro ⟨v, hv, hb⟩
      exact ⟨v, hv, by cases h : b v <;> simp_all⟩
  rw [heq, bernoulliProb_compl, bernoulliProb_all_false]

/-- Actual edge-family caller: simultaneous eligibility hits are positively
associated even when the edges overlap. -/
theorem bernoulliProb_all_edges_hit {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (edges : Finset (Finset V)) :
    (∏ e ∈ edges, (1 - (1-p) ^ e.card)) ≤
      bernoulliProb p (fun b => ∀ e ∈ edges, ∃ v ∈ e, b v = true) := by
  have hm (e : Finset V) (b c : V → Bool) (hbc : b ≤ c)
      (hb : ∃ v ∈ e, b v = true) : ∃ v ∈ e, c v = true := by
    obtain ⟨v, hv, hb⟩ := hb
    refine ⟨v, hv, ?_⟩
    have hvle := hbc v
    cases hc : c v with
    | false =>
      have hbad : ¬ ((true : Bool) ≤ false) := by decide
      exact (hbad (by simpa only [hb, hc] using hvle)).elim
    | true => rfl
  have h := bernoulli_harris_events hp hp1 edges
    (fun e b => ∃ v ∈ e, b v = true) (fun e _ => hm e)
  simpa only [bernoulliProb_hits] using h

/-- Finite Jensen with the same actual product weights used in Harris. -/
theorem bernoulli_jensen {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (f : (V → Bool) → ℝ) (φ : ℝ → ℝ)
    (hφ : ConvexOn ℝ Set.univ φ) :
    φ (bernoulliExpect p f) ≤ bernoulliExpect p (fun b => φ (f b)) := by
  have h := hφ.map_sum_le (t := Finset.univ) (w := bernoulliWeight (V := V) p)
    (p := f) (fun b _ => bernoulliWeight_nonneg hp hp1 b) (sum_bernoulliWeight p)
    (fun _ _ => Set.mem_univ _)
  simpa only [smul_eq_mul, bernoulliExpect] using h

theorem bernoulli_exp_jensen {V : Type*} [Fintype V] {p : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (f : (V → Bool) → ℝ) :
    Real.exp (bernoulliExpect p f) ≤ bernoulliExpect p (fun b => Real.exp (f b)) :=
  bernoulli_jensen hp hp1 f Real.exp convexOn_exp

/-- The RS averaging step: a positive base raised to the mean count is at
most the mean of the base raised to the actual count. -/
theorem bernoulli_rpow_jensen {V : Type*} [Fintype V] {p a : ℝ}
    (hp : 0 ≤ p) (hp1 : p ≤ 1) (ha : 0 < a) (f : (V → Bool) → ℝ) :
    a ^ (bernoulliExpect p f) ≤ bernoulliExpect p (fun b => a ^ (f b)) := by
  have h := bernoulli_exp_jensen hp hp1 (fun b => Real.log a * f b)
  simpa only [bernoulliExpect_const_mul, Real.rpow_def_of_pos ha] using h

end
end Aris4Math.General.RS

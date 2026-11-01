import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

noncomputable section
open scoped BigOperators
open MeasureTheory Set

namespace Aris4Math.General.RS

/-- Exact RS single-intersection integral. -/
def jk (k : ℕ) (p : ℝ) : ℝ := ∫ y in (0 : ℝ)..p, (1 - y ^ 2) ^ (k - 1)

/-- Probability that a k-edge has an eligible vertex. -/
def ak (k : ℕ) (p : ℝ) : ℝ := 1 - (1 - p) ^ k

lemma ak_nonneg (k : ℕ) {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1) : 0 ≤ ak k p := by
  exact sub_nonneg.mpr (pow_le_one₀ (by linarith : 0 ≤ 1-p) (by linarith : 1-p ≤ 1))

lemma ak_le_one (k : ℕ) {p : ℝ} (hp1 : p ≤ 1) : ak k p ≤ 1 := by
  exact sub_le_self 1 (pow_nonneg (by linarith : 0 ≤ 1-p) k)

lemma ak_pos {k : ℕ} (hk : 0 < k) {p : ℝ} (hp : 0 < p) (hp1 : p ≤ 1) :
    0 < ak k p := by
  exact sub_pos.mpr (pow_lt_one₀ (by linarith : 0 ≤ 1-p) (by linarith : 1-p < 1) (by omega))

lemma jk_rescale (k : ℕ) (p : ℝ) :
    p * (∫ t in (0 : ℝ)..1, (1 - p * t) ^ (k - 1) * (1 + p * t) ^ (k - 1)) =
      jk k p := by
  have h : (fun t : ℝ => (1 - p * t) ^ (k - 1) * (1 + p * t) ^ (k - 1)) =
      (fun t : ℝ => (1 - (p * t) ^ 2) ^ (k - 1)) := by
    funext t
    rw [← mul_pow]
    congr 1
    ring_nf
  rw [h]
  simpa [jk] using
    (intervalIntegral.mul_integral_comp_mul_left (a := 0) (b := 1)
      (f := fun y : ℝ => (1 - y ^ 2) ^ (k - 1)) p)

lemma jk_nonneg (k : ℕ) {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1) : 0 ≤ jk k p := by
  apply intervalIntegral.integral_nonneg hp
  intro y hy
  apply pow_nonneg
  have hyy := mul_nonneg hy.1 (show 0 ≤ 1-y by linarith [hy.2])
  nlinarith

lemma jk_le (k : ℕ) {p : ℝ} (hp : 0 ≤ p) (hp1 : p ≤ 1) : jk k p ≤ p := by
  have h := intervalIntegral.integral_mono_on hp
    (show IntervalIntegrable (fun y : ℝ => (1-y^2)^(k-1)) volume 0 p from
      (by fun_prop : Continuous (fun y : ℝ => (1-y^2)^(k-1))).intervalIntegrable 0 p)
    (show IntervalIntegrable (fun _ : ℝ => (1 : ℝ)) volume 0 p from intervalIntegrable_const)
    (fun y hy => pow_le_one₀ (by
        have hyy := mul_nonneg hy.1 (show 0 ≤ 1-y by linarith [hy.2])
        nlinarith : 0 ≤ 1-y^2)
      (by nlinarith [sq_nonneg y] : 1-y^2 ≤ 1))
  simpa [jk] using h

/-- The elementary integer-parameter beta integral used for relative permutation order. -/
lemma beta_nat (a b : ℕ) :
    (∫ t in (0 : ℝ)..1, t^a * (1-t)^b) =
      (a.factorial : ℝ) * b.factorial / (a+b+1).factorial := by
  induction b generalizing a with
  | zero =>
    simp only [pow_zero, mul_one, integral_pow, one_pow, zero_pow (Nat.succ_ne_zero _), sub_zero,
      Nat.factorial_zero, Nat.cast_one, mul_one, Nat.add_zero, Nat.factorial_succ, Nat.cast_mul,
      Nat.cast_add, Nat.cast_one]
    field_simp
  | succ b ih =>
    have der (t : ℝ) : HasDerivAt (fun t : ℝ => t^(a+1)*(1-t)^(b+1))
        (((a+1 : ℕ) : ℝ) * t^a * (1-t)^(b+1) -
          ((b+1 : ℕ) : ℝ) * t^(a+1) * (1-t)^b) t := by
      convert ((hasDerivAt_id t).pow (a+1)).mul
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id t)).pow (b+1)) using 1
      simp
      ring_nf
    have hi : (∫ t in (0 : ℝ)..1,
        ((a+1 : ℕ) : ℝ) * t^a * (1-t)^(b+1) -
          ((b+1 : ℕ) : ℝ) * t^(a+1) * (1-t)^b) = 0 := by
      convert intervalIntegral.integral_eq_sub_of_hasDerivAt (fun t _ => der t)
        (by exact (by fun_prop : Continuous (fun t : ℝ =>
          ((a+1 : ℕ) : ℝ) * t^a * (1-t)^(b+1) -
          ((b+1 : ℕ) : ℝ) * t^(a+1) * (1-t)^b)).intervalIntegrable 0 1) using 1
      simp
    rw [intervalIntegral.integral_sub
      ((by fun_prop : Continuous (fun t : ℝ => ((a+1 : ℕ) : ℝ) * t^a * (1-t)^(b+1))).intervalIntegrable 0 1)
      ((by fun_prop : Continuous (fun t : ℝ => ((b+1 : ℕ) : ℝ) * t^(a+1) * (1-t)^b)).intervalIntegrable 0 1)] at hi
    simp_rw [mul_assoc, intervalIntegral.integral_const_mul] at hi
    rw [ih (a+1)] at hi
    have ha : ((a+1 : ℕ) : ℝ) ≠ 0 := by positivity
    apply mul_left_cancel₀ ha
    rw [sub_eq_zero] at hi
    rw [hi]
    rw [show a+1+b+1 = a+b+1+1 by omega]
    rw [Nat.factorial_succ a, Nat.factorial_succ b]
    push_cast
    ring_nf



/-- Bernoulli eligibility and relative-order finite sum, before the distinguished flip. -/
def orderSum (n : ℕ) (p : ℝ) : ℝ :=
  ∑ a ∈ Finset.range (n+1), ∑ b ∈ Finset.range (n+1),
    (n.choose a : ℝ) * (n.choose b : ℝ) * p^(a+b) * (1-p)^(n-b) *
      ((a.factorial : ℝ) * b.factorial / (a+b+1).factorial)

lemma binomial_order_integrand (n : ℕ) (p t : ℝ) :
    (∑ a ∈ Finset.range (n+1), ∑ b ∈ Finset.range (n+1),
      (n.choose a : ℝ) * (n.choose b : ℝ) * p^(a+b) * (1-p)^(n-b) *
        (t^a * (1-t)^b)) = (1-p*t)^n * (1+p*t)^n := by
  have h1 := add_pow (p*t) (1:ℝ) n
  have h2 := add_pow (p*(1-t)) (1-p) n
  simp only [one_pow, mul_one] at h1
  calc
    _ = (∑ a ∈ Finset.range (n+1), (p*t)^a * (n.choose a : ℝ)) *
        (∑ b ∈ Finset.range (n+1),
          (p*(1-t))^b * (1-p)^(n-b) * (n.choose b : ℝ)) := by
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro a ha
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro b hb
      rw [pow_add, mul_pow, mul_pow]
      ring_nf
    _ = (p*t+1)^n * (p*(1-t)+(1-p))^n := by rw [← h1, ← h2]
    _ = (1-p*t)^n * (1+p*t)^n := by
      rw [show p*t+1 = 1+p*t by ring,
        show p*(1-t)+(1-p) = 1-p*t by ring]
      ring_nf

lemma orderSum_integral (n : ℕ) (p : ℝ) :
    orderSum n p = ∫ t in (0:ℝ)..1, (1-p*t)^n * (1+p*t)^n := by
  have hfun : (fun t : ℝ => (1-p*t)^n * (1+p*t)^n) =
      (fun t : ℝ => ∑ a ∈ Finset.range (n+1), ∑ b ∈ Finset.range (n+1),
        (n.choose a : ℝ) * (n.choose b : ℝ) * p^(a+b) * (1-p)^(n-b) *
          (t^a * (1-t)^b)) := by
    funext t
    exact (binomial_order_integrand n p t).symm
  rw [hfun, intervalIntegral.integral_finset_sum]
  · apply Finset.sum_congr rfl
    intro a ha
    rw [intervalIntegral.integral_finset_sum]
    · apply Finset.sum_congr rfl
      intro b hb
      rw [intervalIntegral.integral_const_mul, beta_nat]
    · intro b hb
      exact (by fun_prop : Continuous (fun t : ℝ =>
        (n.choose a : ℝ) * (n.choose b : ℝ) * p^(a+b) * (1-p)^(n-b) *
          (t^a * (1-t)^b))).intervalIntegrable 0 1
  · intro a ha
    exact (by fun_prop : Continuous (fun t : ℝ => ∑ b ∈ Finset.range (n+1),
      (n.choose a : ℝ) * (n.choose b : ℝ) * p^(a+b) * (1-p)^(n-b) *
        (t^a * (1-t)^b))).intervalIntegrable 0 1

/-- Exact connection from finite Bernoulli/order counting to the RS integral. -/
lemma orderSum_eq_jk (k : ℕ) (p : ℝ) :
    p * orderSum (k-1) p = jk k p := by
  rw [orderSum_integral]
  exact jk_rescale k p

/-- Equivalent explicit edge-size-indexed sum; `k ≥ 1` identifies its range with `k`. -/
lemma finite_order_sum_eq_jk (k : ℕ) (hk : 1 ≤ k) (p : ℝ) :
    p * (∑ a ∈ Finset.range k, ∑ b ∈ Finset.range k,
      ((k-1).choose a : ℝ) * ((k-1).choose b : ℝ) * p^(a+b) * (1-p)^(k-1-b) *
        ((a.factorial : ℝ) * b.factorial / (a+b+1).factorial)) = jk k p := by
  simpa [orderSum, Nat.sub_add_cancel hk] using orderSum_eq_jk k p

end Aris4Math.General.RS

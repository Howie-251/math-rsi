import Aris4Math.ThirtyThree.RefinedDeletion

/-! Finite weak duality for several layouts sharing the same underlying
bad-pair quantities. Only algebraic inequalities are used, not LP strong duality. -/
set_option autoImplicit false
namespace Aris4Math.ThirtyFour.MixedLayoutDual
open scoped BigOperators
variable {L C S Q : Type*} [Fintype L] [Fintype C] [Fintype S] [Fintype Q]

/-- A convex split of the two upper bounds for one center. -/
theorem min_split (g b a c d : ℚ) (hb : 0 ≤ b) (hbg : b ≤ g) :
    g * min a (c-d) ≤ (g-b)*a+b*c-b*d := by
  have ha := mul_le_mul_of_nonneg_left (min_le_left a (c-d)) (sub_nonneg.mpr hbg)
  have hc := mul_le_mul_of_nonneg_left (min_le_right a (c-d)) hb
  nlinarith

/-- All quota constraints act on one fixed vector z. Capacity repair charges
only the positive part of demand minus the available combined weight. -/
theorem quota_repair (z cap weight : S → ℚ) (coeff : Q → S → ℚ)
    (delta quota : Q → ℚ)
    (znonneg : ∀ s, 0 ≤ z s) (zcap : ∀ s, z s ≤ cap s)
    (dnonneg : ∀ q, 0 ≤ delta q)
    (valid : ∀ q, quota q ≤ ∑ s, coeff q s*z s) :
    (∑ q, delta q*quota q) -
      (∑ s, max 0 ((∑ q, delta q*coeff q s)-weight s)*cap s) ≤
      ∑ s, weight s*z s := by
  have hq : (∑ q, delta q*quota q) ≤ ∑ s, (∑ q, delta q*coeff q s)*z s := by
    calc
      _ ≤ ∑ q, delta q*(∑ s, coeff q s*z s) :=
        Finset.sum_le_sum (fun q _ => mul_le_mul_of_nonneg_left (valid q) (dnonneg q))
      _ = _ := by simp_rw [Finset.mul_sum,Finset.sum_mul,mul_assoc]; rw [Finset.sum_comm]
  have hs : (∑ s, (∑ q, delta q*coeff q s)*z s) ≤
      (∑ s, weight s*z s) + (∑ s, max 0 ((∑ q, delta q*coeff q s)-weight s)*cap s) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro s _
    have hp := le_max_right (0 : ℚ) ((∑ q, delta q*coeff q s)-weight s)
    have hmul := mul_le_mul_of_nonneg_right hp (znonneg s)
    have hcap := mul_le_mul_of_nonneg_left (zcap s)
      (le_max_left (0 : ℚ) ((∑ q, delta q*coeff q s)-weight s))
    linarith
  linarith

/-- A strict convex average forces at least one strictly successful layout. -/
theorem exists_strict_of_average (gamma U : L → ℚ)
    (nonneg : ∀ l, 0 ≤ gamma l) (mass : ∑ l, gamma l=1)
    (strict : (∑ l, gamma l*U l)<1) : ∃ l, U l<1 := by
  classical
  by_contra hn
  have lower : ∀ l, 1 ≤ U l := by intro l; by_contra h; exact hn ⟨l,by linarith⟩
  have h := Finset.sum_le_sum (s := Finset.univ) (fun l _ =>
    mul_le_mul_of_nonneg_left (lower l) (nonneg l))
  simp only [mul_one,mass] at h
  linarith

/-- Core layout bound. The weighted actual deductions may already have been
proved directly from bad pairs, without exposing a formal LP object. -/
theorem average_le (gamma : L → ℚ) (beta a c D : L → C → ℚ)
    (free : L → ℚ) (lower : C → ℚ)
    (beta_nonneg : ∀ l i, 0 ≤ beta l i)
    (beta_le : ∀ l i, beta l i ≤ gamma l)
    (deduction : ∀ i, lower i ≤ ∑ l, beta l i*D l i) :
    (∑ l, gamma l*(free l+∑ i, min (a l i) (c l i-D l i))) ≤
      (∑ l, gamma l*free l) +
      (∑ l, ∑ i, ((gamma l-beta l i)*a l i+beta l i*c l i)) - ∑ i, lower i := by
  have first : (∑ l, gamma l*(free l+∑ i, min (a l i) (c l i-D l i))) ≤
      ∑ l, (gamma l*free l + ∑ i, ((gamma l-beta l i)*a l i+beta l i*c l i-beta l i*D l i)) := by
    apply Finset.sum_le_sum
    intro l _
    rw [mul_add,Finset.mul_sum]
    exact add_le_add_left (Finset.sum_le_sum (fun i _ =>
      min_split _ _ _ _ _ (beta_nonneg l i) (beta_le l i))) _
  have ds := Finset.sum_le_sum (s := Finset.univ) (fun i _ => deduction i)
  have deq : (∑ i, ∑ l, beta l i*D l i) = ∑ l, ∑ i, beta l i*D l i := Finset.sum_comm
  rw [deq] at ds
  simp only [Finset.sum_add_distrib,Finset.sum_sub_distrib] at first ⊢
  linarith
end Aris4Math.ThirtyFour.MixedLayoutDual
#print axioms Aris4Math.ThirtyFour.MixedLayoutDual.average_le
#print axioms Aris4Math.ThirtyFour.MixedLayoutDual.quota_repair

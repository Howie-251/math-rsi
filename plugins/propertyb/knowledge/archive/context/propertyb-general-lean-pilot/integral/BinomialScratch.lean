import Mathlib.Data.Rat.Lemmas
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Tactic.Ring
open scoped BigOperators
lemma binomial_order_integrand (n : ℕ) (p t : ℚ) :
    (∑ a ∈ Finset.range (n+1), ∑ b ∈ Finset.range (n+1),
      (n.choose a : ℚ) * (n.choose b : ℚ) * p^(a+b) * (1-p)^(n-b) *
        (t^a * (1-t)^b)) = (1-p*t)^n * (1+p*t)^n := by
  have h1 := add_pow (p*t) (1:ℚ) n
  have h2 := add_pow (p*(1-t)) (1-p) n
  simp only [one_pow, mul_one] at h1
  calc
    _ = (∑ a ∈ Finset.range (n+1), (p*t)^a * (n.choose a : ℚ)) *
        (∑ b ∈ Finset.range (n+1),
          (p*(1-t))^b * (1-p)^(n-b) * (n.choose b : ℚ)) := by
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro a ha
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro b hb
      rw [pow_add, mul_pow, mul_pow]
      ring
    _ = (p*t+1)^n * (p*(1-t)+(1-p))^n := by rw [← h1, ← h2]
    _ = (1-p*t)^n * (1+p*t)^n := by
      rw [show p*t+1 = 1+p*t by ring,
        show p*(1-t)+(1-p) = 1-p*t by ring]
      ring

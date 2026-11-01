import Mathlib.Data.Rat.Lemmas
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

example (a : ℕ) : (1:ℚ)/(a+1) = (a.factorial : ℚ) * Nat.factorial 0 / (a+0+1).factorial := by
  simp only [Nat.factorial_zero, Nat.cast_one, mul_one, Nat.add_zero, Nat.factorial_succ,
    Nat.cast_mul, Nat.cast_add, Nat.cast_one]
  field_simp

example (a b : ℕ) (I : ℚ)
    (hi : ((a+1 : ℕ) : ℚ) * I = ((b+1 : ℕ) : ℚ) *
      ((a+1).factorial : ℚ) * b.factorial / (a+1+b+1).factorial) :
    I = (a.factorial : ℚ) * (b+1).factorial / (a+(b+1)+1).factorial := by
  have ha : ((a+1 : ℕ) : ℚ) ≠ 0 := by positivity
  apply mul_left_cancel₀ ha
  rw [hi]
  rw [show a+1+b+1 = a+b+1+1 by omega]
  rw [Nat.factorial_succ a, Nat.factorial_succ b]
  push_cast
  ring

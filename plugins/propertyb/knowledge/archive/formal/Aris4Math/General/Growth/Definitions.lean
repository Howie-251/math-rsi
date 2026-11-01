import Aris4Math.General.RS.Integral
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Sqrt
import Mathlib.Algebra.Order.Floor.Ring

namespace Aris4Math.General.RS

noncomputable section

/-- A particular parameter accepted by the precise RS comparison criterion. -/
def AcceptedAt (k M : ℕ) (p : ℝ) : Prop :=
  0 ≤ p ∧ p ≤ 1 ∧
  (M : ℝ) * ((M : ℝ) - 1) / ((2 : ℝ) ^ (k - 1)) ^ 2 * jk k p <
    (ak k p) ^ ((M : ℝ) / (2 : ℝ) ^ (k - 1))

def RSAccepts (k M : ℕ) : Prop := 1 ≤ M ∧ ∃ p : ℝ, AcceptedAt k M p

/-- The integer gain in the paper's main theorem. -/
def integerGain (k M : ℕ) : ℕ :=
  ⌊Real.sqrt (M : ℝ) / (8 * (1 + Real.log (k : ℝ)))⌋₊

end
end Aris4Math.General.RS

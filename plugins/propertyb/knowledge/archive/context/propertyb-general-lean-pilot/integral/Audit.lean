import Aris4Math.General.RS.Integral

#check Aris4Math.General.RS.orderSum_eq_jk
#check Aris4Math.General.RS.finite_order_sum_eq_jk
#print axioms Aris4Math.General.RS.finite_order_sum_eq_jk
#print Aris4Math.General.RS.orderSum
#print Aris4Math.General.RS.jk
#print Aris4Math.General.RS.ak
#print axioms Aris4Math.General.RS.orderSum_eq_jk
#print axioms Aris4Math.General.RS.beta_nat
#print axioms Aris4Math.General.RS.jk_nonneg
#print axioms Aris4Math.General.RS.jk_le
#print axioms Aris4Math.General.RS.ak_pos

open scoped BigOperators
open Aris4Math.General.RS
example (k : ℕ) (hk : 1 ≤ k) (p : ℝ) :
    p * (∑ a ∈ Finset.range k, ∑ b ∈ Finset.range k,
      ((k-1).choose a : ℝ) * ((k-1).choose b : ℝ) * p^(a+b) * (1-p)^(k-1-b) *
        ((a.factorial : ℝ) * b.factorial / (a+b+1).factorial)) = jk k p := by
  simpa [orderSum, Nat.sub_add_cancel hk] using orderSum_eq_jk k p

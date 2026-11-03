import DegreeDiameter.N62RepeatQuotientTrace

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual repeat components have total weight seventeen, where weight is one plus twice the
internal original degree. No upper bound on actual defect entries is assumed. -/
theorem n62_repeat_component_weight_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    ∑ C : (repeatSupport G).ConnectedComponent, (1 + 2 * repeatQuotientMatrix G C C) = 17 := by
  have ht := n62_repeat_quotient_trace_identity G hdeg hdiam hcard
  simpa [Finset.sum_add_distrib, ← Finset.mul_sum, Matrix.trace, Matrix.diag_apply] using ht

/-- Every selected finite set of actual repeat components fits inside the exact weight budget. -/
theorem n62_repeat_component_subset_budget (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (S : Finset (repeatSupport G).ConnectedComponent) :
    (S.card : ℤ) + 2 * ∑ C ∈ S, repeatQuotientMatrix G C C ≤ 17 := by
  have hpos (C : (repeatSupport G).ConnectedComponent) :
      0 ≤ 1 + 2 * repeatQuotientMatrix G C C := by
    have := repeat_quotient_nonnegative G C C
    omega
  have hs := Finset.sum_le_univ_sum_of_nonneg (s := S) hpos
  rw [n62_repeat_component_weight_sum G hdeg hdiam hcard] at hs
  simpa [Finset.sum_add_distrib, ← Finset.mul_sum] using hs

/-- Six actual components and three actual internal degrees at least two contradict the trace.
This is the numerical tail of the analytic triple-repeat exclusion, not its component construction. -/
theorem n62_no_six_components_three_internal_two (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hcount : 6 ≤ Fintype.card (repeatSupport G).ConnectedComponent)
    (S : Finset (repeatSupport G).ConnectedComponent) (hsize : S.card = 3)
    (hinternal : ∀ C ∈ S, 2 ≤ repeatQuotientMatrix G C C) : False := by
  have hl : (6 : ℤ) ≤ ∑ C ∈ S, repeatQuotientMatrix G C C := by
    calc
      _ = ∑ _C ∈ S, (2 : ℤ) := by simp [hsize]
      _ ≤ _ := Finset.sum_le_sum hinternal
  have hu : (∑ C ∈ S, repeatQuotientMatrix G C C) ≤ trace (repeatQuotientMatrix G) :=
    Finset.sum_le_univ_sum_of_nonneg (fun C => repeat_quotient_nonnegative G C C)
  have hc : (6 : ℤ) ≤ (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) := by
    exact_mod_cast hcount
  have ht := n62_repeat_quotient_trace_identity G hdeg hdiam hcard
  omega

end
end DegreeDiameter


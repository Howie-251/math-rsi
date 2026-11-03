import DegreeDiameter.N62RepeatQuotient
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.CharP.Two

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual defect row restricted to its support component still has sum three. -/
theorem n62_repeat_component_defect_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent)
    {x : V} (hx : x ∈ C.supp) :
    ∑ y ∈ repeatComponentVertices G C, defectMatrix G x y = 3 := by
  have hh := n62_repeat_component_indicator_harmonic G hdeg hdiam hcard C x
  simpa [repeatComponentVertices,repeatComponentIndicator,hx,mul_ite,Finset.sum_filter] using hh

/-- Symmetric integer weights with zero diagonal have an even total on any finite square. -/
private theorem symmetric_zero_diagonal_sum_even (B : Matrix V V ℤ)
    (hsym : ∀ x y, B y x = B x y) (hdiag : ∀ x, B x x = 0) (S : Finset V) :
    Even (∑ x ∈ S, ∑ y ∈ S, B x y) := by
  have hz : ∑ p ∈ S ×ˢ S, (B p.1 p.2 : ZMod 2) = 0 := by
    refine Finset.sum_involution (fun p _ => p.swap) ?_ ?_ ?_ ?_
    · intro p _
      dsimp only [Prod.swap]
      rw [hsym]
      exact CharTwo.add_self_eq_zero _
    · intro p _ hn he
      have heq : p.2 = p.1 := congrArg Prod.fst he
      exact hn (by simp [heq,hdiag])
    · intro p hp
      exact Finset.mem_product.mpr ⟨(Finset.mem_product.mp hp).2,(Finset.mem_product.mp hp).1⟩
    · intro p _
      exact Prod.swap_swap p
  apply ZMod.intCast_eq_zero_iff_even.mp
  simpa [Finset.sum_product] using hz

/-- Every actual repeat-support component in an original legal order-62 graph has even size. -/
theorem n62_repeat_component_size_even (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    Even (repeatComponentSize G C) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hs := symmetric_zero_diagonal_sum_even (defectMatrix G)
    (fun x y => (defect_symmetric G).apply x y) (defect_diagonal G hreg)
    (repeatComponentVertices G C)
  have he : (∑ x ∈ repeatComponentVertices G C, ∑ y ∈ repeatComponentVertices G C,
      defectMatrix G x y) = 3 * (repeatComponentSize G C : ℤ) := by
    calc
      _ = ∑ _x ∈ repeatComponentVertices G C, (3 : ℤ) := by
        apply Finset.sum_congr rfl
        intro x hx
        exact n62_repeat_component_defect_row G hdeg hdiam hcard C
          ((mem_repeatComponentVertices G C x).mp hx)
      _ = _ := by simp [repeatComponentSize]; ring
  rw [he] at hs
  have hz := ZMod.intCast_eq_zero_iff_even.mpr hs
  apply ZMod.natCast_eq_zero_iff_even.mp
  simpa only [Int.cast_mul,Int.cast_ofNat,Int.cast_natCast,
    show (3 : ZMod 2) = 1 from rfl,one_mul] using hz

/-- If actual defect entries are at most two, every actual repeat component has at least four vertices. -/
theorem n62_repeat_component_size_ge_four (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hbound : ∀ x y, defectMatrix G x y ≤ 2)
    (C : (repeatSupport G).ConnectedComponent) :
    4 ≤ repeatComponentSize G C := by
  have he := n62_repeat_component_size_even G hdeg hdiam hcard C
  have hp := repeat_component_size_pos G C
  by_contra hsmall
  have htwo : (repeatComponentVertices G C).card = 2 := by
    rcases he with ⟨k,hk⟩
    change 0 < (repeatComponentVertices G C).card at hp
    change (repeatComponentVertices G C).card = k + k at hk
    change ¬ 4 ≤ (repeatComponentVertices G C).card at hsmall
    omega
  obtain ⟨x,y,hxy,hS⟩ := Finset.card_eq_two.mp htwo
  have hx : x ∈ C.supp := (mem_repeatComponentVertices G C x).mp (by simp [hS])
  have hr := n62_repeat_component_defect_row G hdeg hdiam hcard C hx
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  simp [hS,hxy,defect_diagonal G hreg] at hr
  have hb := hbound x y
  omega

/-- Positive quotient entries have positive reverse entries, as follows from actual edge balance. -/
theorem n62_repeat_quotient_reverse_positive (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C D : (repeatSupport G).ConnectedComponent)
    (hpos : 0 < repeatQuotientMatrix G C D) :
    0 < repeatQuotientMatrix G D C := by
  have hc : (0 : ℤ) < repeatComponentSize G C := by
    exact_mod_cast repeat_component_size_pos G C
  have hb := n62_repeat_quotient_balance G hdeg hdiam hcard C D
  have hm := mul_pos hc hpos
  rw [hb] at hm
  have hn := repeat_quotient_nonnegative G D C
  by_contra hh
  have hz : repeatQuotientMatrix G D C = 0 := by omega
  simp [hz] at hm

/-- Every summand in the actual quotient budget is nonnegative. -/
theorem n62_repeat_quotient_budget_term_nonnegative (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C D : (repeatSupport G).ConnectedComponent) :
    0 ≤ repeatQuotientMatrix G C D * (repeatQuotientMatrix G D C - 1) := by
  have hn := repeat_quotient_nonnegative G C D
  by_cases hz : repeatQuotientMatrix G C D = 0
  · simp [hz]
  have hp : 0 < repeatQuotientMatrix G C D := by omega
  have hr := n62_repeat_quotient_reverse_positive G hdeg hdiam hcard C D hp
  exact mul_nonneg hn (by omega)

/-- The actual quotient diagonal identity minus row sum eight gives its exact nonnegative budget. -/
theorem n62_repeat_quotient_budget (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    ∑ D, repeatQuotientMatrix G C D * (repeatQuotientMatrix G D C - 1) =
      (repeatComponentSize G C : ℤ) + 2 - repeatQuotientMatrix G C C := by
  have hq := congrArg (fun M => M C C) (n62_repeat_quotient_quadratic G hdeg hdiam hcard)
  dsimp only at hq
  simp only [Matrix.add_apply,Matrix.smul_apply,smul_eq_mul,Matrix.one_apply,ite_true,
    mul_one,repeatSizeMatrix,Matrix.mul_apply] at hq
  simp only [mul_sub,mul_one,Finset.sum_sub_distrib]
  rw [n62_repeat_quotient_row_sum G hdeg hdiam hcard C]
  omega

/-- The diagonal term of the actual nonnegative budget bounds internal original degree by component size. -/
theorem n62_repeat_component_size_ge_internal_square_sub_two (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    repeatQuotientMatrix G C C ^ 2 - 2 ≤ (repeatComponentSize G C : ℤ) := by
  have hle := Finset.single_le_sum
    (fun D (_ : D ∈ (Finset.univ : Finset (repeatSupport G).ConnectedComponent)) =>
      n62_repeat_quotient_budget_term_nonnegative G hdeg hdiam hcard C D)
    (Finset.mem_univ C)
  rw [n62_repeat_quotient_budget G hdeg hdiam hcard C] at hle
  have he : repeatQuotientMatrix G C C * (repeatQuotientMatrix G C C - 1) =
      repeatQuotientMatrix G C C ^ 2 - repeatQuotientMatrix G C C := by ring
  rw [he] at hle
  omega

end
end DegreeDiameter

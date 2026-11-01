import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Powerset
import Aris4Math.ThirtyFour.TwentyOneSevenSelection

/-! Weighted pigeonhole bounds for three actual seven-degree vertices.
The finite constants 12 and 9 count the eight subsets of Fin 3 only. -/
namespace Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights
open scoped BigOperators
variable {α β : Type*} [DecidableEq α] [DecidableEq β] [Fintype β]

theorem weighted_bound (S : Finset α) (pattern : α → β) (weight : β → ℕ)
    (unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y → weight (pattern x)=0) :
    (∑ x∈S,weight (pattern x))≤∑ b : β,weight b := by
  have image : (∑ b∈S.image pattern,weight b)=∑ x∈S,weight (pattern x) :=
    Finset.sum_image_of_pairwise_eq_zero unique
  rw [← image]
  exact Finset.sum_le_sum_of_subset (Finset.subset_univ _)

theorem repeated_of_weight (S : Finset α) (pattern : α → β) (weight : β → ℕ)
    (large : (∑ b : β,weight b)<∑ x∈S,weight (pattern x)) :
    ∃ x∈S,∃ y∈S,x≠y ∧ pattern x=pattern y ∧ 0<weight (pattern x) := by
  by_contra no
  have unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y → weight (pattern x)=0 := by
    intro x hx y hy ne same
    by_contra positive
    exact no ⟨x,hx,y,hy,ne,same,Nat.pos_of_ne_zero positive⟩
  exact (not_lt_of_ge (weighted_bound S pattern weight unique)) large

theorem subsets_weight : (∑ P : Finset (Fin 3),P.card)=12 := by decide +kernel

theorem repeated_nonempty (S : Finset α) (pattern : α → Finset (Fin 3))
    (large : 12<∑ x∈S,(pattern x).card) :
    ∃ x∈S,∃ y∈S,x≠y ∧ pattern x=pattern y ∧ (pattern x).Nonempty := by
  rw [← subsets_weight] at large
  obtain ⟨x,hx,y,hy,ne,same,pos⟩ := repeated_of_weight S pattern Finset.card large
  exact ⟨x,hx,y,hy,ne,same,Finset.card_pos.mp pos⟩

def properWeight (P : Finset (Fin 3)) : ℕ := if P=Finset.univ then 0 else P.card

theorem proper_weight : (∑ P : Finset (Fin 3),properWeight P)=9 := by decide +kernel

theorem full_pattern_bound (S : Finset α) (pattern : α → Finset (Fin 3))
    (unique : ∀ x∈S,∀ y∈S,x≠y → pattern x=pattern y →
      (pattern x).Nonempty → pattern x=Finset.univ) :
    (∑ x∈S,(pattern x).card)≤9+3*(S.filter fun x => pattern x=Finset.univ).card := by
  have proper : (∑ x∈S,properWeight (pattern x))≤9 := by
    rw [← proper_weight]
    apply weighted_bound S pattern properWeight
    intro x hx y hy ne same
    by_cases empty : pattern x=∅
    · simp [properWeight,empty]
    · have full := unique x hx y hy ne same (Finset.nonempty_iff_ne_empty.mpr empty)
      simp [properWeight,full]
  have each (x : α) : (pattern x).card=properWeight (pattern x)+
      if pattern x=Finset.univ then 3 else 0 := by
    by_cases full : pattern x=Finset.univ
    · simp [properWeight,full]
    · simp [properWeight,full]
  have totals : (∑ x∈S,(pattern x).card)=(∑ x∈S,properWeight (pattern x))+
      3*(S.filter fun x => pattern x=Finset.univ).card := by
    simp_rw [each,Finset.sum_add_distrib]
    rw [←Finset.sum_filter]
    simp [Nat.mul_comm]
  omega

end Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights.repeated_nonempty
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenThreeSelectionWeights.full_pattern_bound

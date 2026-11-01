import Aris4Math.ThirtyFour.WeightedSubsetSelection

/-! Select one actual outside vertex for all seven-lock projections at once. -/
namespace Aris4Math.ThirtyFour.WeightedSubsetSelection

open scoped BigOperators
variable {V : Type*} [DecidableEq V]

/-- The low-weight branches use this same actual y in every deletion
projection. Integer cut budgets give the bounds four and three. -/
theorem exists_seventh (w : V → V → ℕ) (symm : ∀ x y, w x y=w y x)
    (zero : ∀ x, w x x=0) (L S : Finset V) (minimal : IsMinimum w L S)
    (card : S.card=6) (large : 14 ≤ L.card)
    (maximum : ∀ x ∈ L, degree w L x ≤ 6) (lower : 4 ≤ energy w S) :
    ∃ y ∈ L \ S, degree w S y ≤ 4 ∧
      (6 ≤ energy w S → degree w S y ≤ 3) ∧
      ∀ x ∈ S, degree w S x + w x y ≤ degree w S y := by
  classical
  let B := L \ S
  have cards : B.card+S.card=L.card := Finset.card_sdiff_add_card_eq_card minimal.1
  have many : 8 ≤ B.card := by omega
  obtain ⟨y,hy,best⟩ := Finset.exists_min_image B (degree w S)
    (Finset.card_pos.mp (by omega))
  let cut := ∑ x ∈ S, degree w B x
  have transpose : (∑ z ∈ B, degree w S z)=cut := by
    dsimp [degree,cut]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro x hx
    exact Finset.sum_congr rfl (fun z _ => symm z x)
  have cutLower : B.card*degree w S y ≤ cut := by
    have summed := Finset.sum_le_sum best
    rw [transpose] at summed
    simpa using summed
  have split : energy w S + cut = ∑ x ∈ S, degree w L x := by
    rw [energy,← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun x _ => degree_split w L S minimal.1 x)
  have cutUpper : energy w S + cut ≤ 36 := by
    rw [split]
    have summed := Finset.sum_le_sum (s := S) (fun x hx => maximum x (minimal.1 hx))
    simpa [card] using summed
  have eight := Nat.mul_le_mul_right (degree w S y) many
  refine ⟨y,hy,?_,?_,?_⟩
  · nlinarith
  · intro six
    nlinarith
  · intro x hx
    exact swap_inequality w symm zero L S minimal x y hx hy

end Aris4Math.ThirtyFour.WeightedSubsetSelection

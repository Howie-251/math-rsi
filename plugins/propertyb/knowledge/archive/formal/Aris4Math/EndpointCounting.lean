import Aris4Math.JointCounting
import Mathlib.Data.Fintype.Option
import Mathlib.Tactic.FieldSimp

/-! Additional point locks and their exact normalization factor. -/

namespace Aris4Math.EndpointCounting

open Equiv
open Aris4Math.Counting Aris4Math.JointCounting

variable {α ι : Type*} [Fintype α] [DecidableEq α] [Fintype ι]

abbrev Locked (vertices positions : ι ↪ α) :=
  {σ : Perm α // ∀ i, σ (vertices i) = positions i}

/-- Exact probability of an event in the uniform locked sample space. -/
noncomputable def lockedRatio (vertices positions : ι ↪ α) (event : Perm α → Prop) : ℚ := by
  classical
  exact (Fintype.card {σ : Locked vertices positions // event σ.1} : ℚ) /
    (Fintype.card (Locked vertices positions) : ℚ)

theorem lockedRatio_congr (vertices positions : ι ↪ α) (P Q : Perm α → Prop)
    (h : ∀ σ, P σ ↔ Q σ) : lockedRatio vertices positions P = lockedRatio vertices positions Q := by
  have heq : P = Q := funext (fun σ => propext (h σ))
  rw [heq]

theorem lockedRatio_congr_on (vertices positions : ι ↪ α) (P Q : Perm α → Prop)
    (h : ∀ σ : Locked vertices positions, P σ.1 ↔ Q σ.1) :
    lockedRatio vertices positions P = lockedRatio vertices positions Q := by
  classical
  unfold lockedRatio
  rw [Fintype.card_congr (Equiv.subtypeEquivRight h)]

theorem lockedRatio_zero (vertices positions : ι ↪ α) (P : Perm α → Prop)
    (h : ∀ σ : Locked vertices positions, ¬ P σ.1) : lockedRatio vertices positions P = 0 := by
  classical
  have hempty : IsEmpty {σ : Locked vertices positions // P σ.1} := ⟨fun σ => h σ.1 σ.2⟩
  simp only [lockedRatio, Fintype.card_eq_zero_iff.mpr hempty, Nat.cast_zero, zero_div]

/-- Extend an injective lock list by one genuinely free point. -/
def addLock (a : ι ↪ α) (x : α) (hx : x ∉ Set.range a) : Option ι ↪ α where
  toFun := Option.elim' x a
  inj' := by
    intro i j hij
    cases i with
    | none =>
      cases j with
      | none => rfl
      | some j => exact False.elim (hx ⟨j, hij.symm⟩)
    | some i =>
      cases j with
      | none => exact False.elim (hx ⟨i, hij⟩)
      | some j => exact congrArg some (a.injective hij)

omit [Fintype α] [DecidableEq α] [Fintype ι] in
@[simp] theorem addLock_none (a : ι ↪ α) (x : α) (hx : x ∉ Set.range a) :
    addLock a x hx none = x := rfl

omit [Fintype α] [DecidableEq α] [Fintype ι] in
@[simp] theorem addLock_some (a : ι ↪ α) (x : α) (hx : x ∉ Set.range a) (i : ι) :
    addLock a x hx (some i) = a i := rfl

omit [Fintype α] [DecidableEq α] [Fintype ι] in
theorem mem_range_addLock_iff (a : ι ↪ α) (x : α) (hx : x ∉ Set.range a) (y : α) :
    y ∈ Set.range (addLock a x hx) ↔ y = x ∨ y ∈ Set.range a := by
  constructor
  · rintro ⟨i, hi⟩
    cases i with
    | none => exact Or.inl hi.symm
    | some i => exact Or.inr ⟨i, hi⟩
  · rintro (rfl | ⟨i, rfl⟩)
    · exact ⟨none, rfl⟩
    · exact ⟨some i, rfl⟩

/-- Conditioning on one more actual point image is exactly the extended
lock sample space. The underlying permutation is unchanged. -/
def extraLockEquiv (vertices positions : ι ↪ α) (x k : α)
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions) :
    {σ : Locked vertices positions // σ.1 x = k} ≃
      Locked (addLock vertices x hx) (addLock positions k hk) where
  toFun σ := ⟨σ.1.1, by
    intro i
    cases i with
    | none => exact σ.2
    | some i => exact σ.1.2 i⟩
  invFun σ := ⟨⟨σ.1, fun i => σ.2 (some i)⟩, σ.2 none⟩
  left_inv _ := rfl
  right_inv _ := rfl

theorem free_count_pos (vertices : ι ↪ α) (x : α) (hx : x ∉ Set.range vertices) :
    0 < Fintype.card α - Fintype.card ι := by
  have hne : Nonempty ↥((Set.range vertices)ᶜ) := ⟨⟨x, hx⟩⟩
  have hpos := Fintype.card_pos_iff.mpr hne
  rwa [card_free_vertices] at hpos

/-- An extra free point lock has probability exactly `1/N` in the original
conditional sample space. Both the numerator and denominator are real sample
cardinalities, not assumed factorial formulas. -/
theorem extra_lock_ratio (vertices positions : ι ↪ α) (x k : α)
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions) :
    (Fintype.card {σ : Locked vertices positions // σ.1 x = k} : ℚ) /
        (Fintype.card (Locked vertices positions) : ℚ) =
      1 / (Fintype.card α - Fintype.card ι : ℕ) := by
  rw [Fintype.card_congr (extraLockEquiv vertices positions x k hx hk),
    card_prescribed_images, card_prescribed_images, Fintype.card_option]
  have hN : Fintype.card α - Fintype.card ι ≠ 0 :=
    Nat.ne_of_gt (free_count_pos vertices x hx)
  rw [← Nat.sub_sub, ← Nat.mul_factorial_pred hN]
  simp only [Nat.cast_mul]
  simpa using mul_div_mul_right (1 : ℚ)
    (Fintype.card α - Fintype.card ι : ℕ)
    (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero (Fintype.card α - Fintype.card ι - 1)))

/-- An event forcing the additional center lock has the same actual outcomes
when expressed in the old sample or the extended-lock sample. -/
def extraLockEventEquiv (vertices positions : ι ↪ α) (x k : α)
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions)
    (event : Perm α → Prop) (hforces : ∀ σ, event σ → σ x = k) :
    {σ : Locked vertices positions // event σ.1} ≃
      {σ : Locked (addLock vertices x hx) (addLock positions k hk) // event σ.1} where
  toFun σ := ⟨(extraLockEquiv vertices positions x k hx hk) ⟨σ.1, hforces _ σ.2⟩, σ.2⟩
  invFun σ := ⟨((extraLockEquiv vertices positions x k hx hk).symm σ.1).1, σ.2⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- Exact conditioning identity for any actual event that forces the center.
The factor is `1/N`, irrespective of how many vertices the edges contain. -/
theorem extra_lock_event_ratio (vertices positions : ι ↪ α) (x k : α)
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions)
    (event : Perm α → Prop) [DecidablePred event]
    (hforces : ∀ σ, event σ → σ x = k) :
    (Fintype.card {σ : Locked vertices positions // event σ.1} : ℚ) /
        (Fintype.card (Locked vertices positions) : ℚ) =
      ((Fintype.card {σ : Locked (addLock vertices x hx) (addLock positions k hk) //
          event σ.1} : ℚ) /
        (Fintype.card (Locked (addLock vertices x hx) (addLock positions k hk)) : ℚ)) *
          (1 / (Fintype.card α - Fintype.card ι : ℕ)) := by
  classical
  have hratio := extra_lock_ratio vertices positions x k hx hk
  rw [Fintype.card_congr (extraLockEquiv vertices positions x k hx hk)] at hratio
  rw [Fintype.card_congr (extraLockEventEquiv vertices positions x k hx hk event hforces),
    ← hratio]
  have hnz : (Fintype.card
      (Locked (addLock vertices x hx) (addLock positions k hk)) : ℚ) ≠ 0 := by
    rw [card_prescribed_images]
    exact Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)
  field_simp

end Aris4Math.EndpointCounting

#print axioms Aris4Math.EndpointCounting.extra_lock_ratio
#print axioms Aris4Math.EndpointCounting.extra_lock_event_ratio

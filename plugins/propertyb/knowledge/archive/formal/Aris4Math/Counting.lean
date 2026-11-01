import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fintype.Sigma
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Logic.Equiv.Fintype

/-!
# Exact counts of permutations under locks

These results count arbitrary finite permutations with specified images. They
do not enumerate permutations and do not assume the factorial formula being
proved. The count is reduced to Mathlib's general theorem for permutations
supported on a finite set.
-/

namespace Aris4Math.Counting

open Equiv

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- Fixing each point of `s` leaves exactly the permutations of its complement. -/
def fixingEquivSupported (s : Finset α) :
    {σ : Perm α // ∀ x ∈ s, σ x = x} ≃ ↥(permsOfFinset sᶜ) where
  toFun σ := ⟨σ.1, mem_perms_of_finset_iff.mpr (by
    intro x hx
    exact Finset.mem_compl.mpr (fun hs => hx (σ.2 x hs)))⟩
  invFun σ := ⟨σ.1, by
    intro x hx
    by_contra hne
    exact (Finset.mem_compl.mp (mem_perms_of_finset_iff.mp σ.2 hne)) hx⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- A general formula, including the empty and fully locked cases. -/
theorem card_fixing (s : Finset α) :
    Fintype.card {σ : Perm α // ∀ x ∈ s, σ x = x} =
      (Fintype.card α - s.card).factorial := by
  rw [Fintype.card_congr (fixingEquivSupported s), Fintype.card_coe,
    card_perms_of_finset, Finset.card_compl]

/-- Composing by the inverse reference permutation turns image constraints
into pointwise fixing constraints. -/
def agreeingEquivFixing (s : Finset α) (reference : Perm α) :
    {σ : Perm α // ∀ x ∈ s, σ x = reference x} ≃
      {σ : Perm α // ∀ x ∈ s, σ x = x} where
  toFun σ := ⟨σ.1.trans reference.symm, by
    intro x hx
    simp only [Equiv.trans_apply, σ.2 x hx, Equiv.symm_apply_apply]⟩
  invFun σ := ⟨σ.1.trans reference, by
    intro x hx
    simp only [Equiv.trans_apply, σ.2 x hx]⟩
  left_inv σ := by
    apply Subtype.ext
    ext x
    simp
  right_inv σ := by
    apply Subtype.ext
    ext x
    simp

/-- Every admissible assignment on `s` has the same number of extensions.
The next theorem removes the reference-permutation parameter. -/
theorem card_agreeing (s : Finset α) (reference : Perm α) :
    Fintype.card {σ : Perm α // ∀ x ∈ s, σ x = reference x} =
      (Fintype.card α - s.card).factorial := by
  rw [Fintype.card_congr (agreeingEquivFixing s reference), card_fixing]

/-- For any two injective lists of locked vertices and their specified
positions, the number of extending permutations is `(N-r)!`.
Injectivity expresses both distinctness conditions; no extension of the locks
is assumed. Mathlib's finite-subtype extension constructs one inside the proof. -/
theorem card_prescribed_images {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α) :
    Fintype.card {σ : Perm α // ∀ i, σ (vertices i) = positions i} =
      (Fintype.card α - Fintype.card ι).factorial := by
  classical
  let s : Finset α := Finset.univ.map vertices
  let e : Set.range vertices ≃ Set.range positions :=
    vertices.toEquivRange.symm.trans positions.toEquivRange
  let reference : Perm α := e.extendSubtype
  have href (i : ι) : reference (vertices i) = positions i := by
    dsimp only [reference]
    rw [Equiv.extendSubtype_apply_of_mem e (vertices i) (Set.mem_range_self i)]
    simp [e]
  have hpred (σ : Perm α) :
      (∀ i, σ (vertices i) = positions i) ↔
        ∀ x ∈ s, σ x = reference x := by
    constructor
    · intro h x hx
      obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hx
      exact (h i).trans (href i).symm
    · intro h i
      exact (h (vertices i) (Finset.mem_map.mpr ⟨i, Finset.mem_univ i, rfl⟩)).trans
        (href i)
  rw [Fintype.card_congr (Equiv.subtypeEquivRight hpred), card_agreeing]
  simp [s]

/-- A permutation preserving a predicate is precisely an independent
permutation of the predicate and of its complement. -/
def preservingEquiv (p : α → Prop) [DecidablePred p] :
    {σ : Perm α // ∀ x, p (σ x) ↔ p x} ≃
      Perm {x // p x} × Perm {x // ¬ p x} where
  toFun σ := ⟨σ.1.subtypePerm σ.2,
    σ.1.subtypePerm (fun x => not_congr (σ.2 x))⟩
  invFun τ := ⟨τ.1.subtypeCongr τ.2, by
    intro x
    by_cases hx : p x
    · rw [Equiv.Perm.subtypeCongr.left_apply _ _ hx]
      exact iff_of_true (τ.1 ⟨x, hx⟩).2 hx
    · rw [Equiv.Perm.subtypeCongr.right_apply _ _ hx]
      exact iff_of_false (τ.2 ⟨x, hx⟩).2 hx⟩
  left_inv σ := by
    apply Subtype.ext
    ext x
    by_cases hx : p x
    · simp [Equiv.Perm.subtypeCongr.left_apply, hx]
    · simp [Equiv.Perm.subtypeCongr.right_apply, hx]
  right_inv τ := by
    apply Prod.ext
    · ext x
      simp
    · ext x
      simp

/-- There are `r! (N-r)!` permutations preserving an r-element set. -/
theorem card_preserving (s : Finset α) :
    Fintype.card {σ : Perm α // ∀ x, σ x ∈ s ↔ x ∈ s} =
      s.card.factorial * (Fintype.card α - s.card).factorial := by
  rw [Fintype.card_congr (preservingEquiv (fun x => x ∈ s)),
    Fintype.card_prod, Fintype.card_perm, Fintype.card_perm,
    Fintype.card_subtype_compl, Fintype.card_coe]

/-- Transporting the target subset back along a reference permutation
identifies its mapping fibre with the setwise stabilizer of the source. -/
def mappingEquivPreserving (s t : Finset α) (reference : Perm α)
    (href : ∀ x, reference x ∈ t ↔ x ∈ s) :
    {σ : Perm α // ∀ x, σ x ∈ t ↔ x ∈ s} ≃
      {σ : Perm α // ∀ x, σ x ∈ s ↔ x ∈ s} where
  toFun σ := ⟨σ.1.trans reference.symm, by
    intro x
    dsimp only [Equiv.trans_apply]
    rw [← href, Equiv.apply_symm_apply]
    exact σ.2 x⟩
  invFun σ := ⟨σ.1.trans reference, by
    intro x
    dsimp only [Equiv.trans_apply]
    exact (href (σ.1 x)).trans (σ.2 x)⟩
  left_inv σ := by
    apply Subtype.ext
    ext x
    simp
  right_inv σ := by
    apply Subtype.ext
    ext x
    simp

/-- Two subsets of equal size have a mapping fibre of size `r! (N-r)!`.
In particular the count is independent of the particular target subset. -/
theorem card_mapping (s t : Finset α) (heq : s.card = t.card) :
    Fintype.card {σ : Perm α // ∀ x, σ x ∈ t ↔ x ∈ s} =
      s.card.factorial * (Fintype.card α - s.card).factorial := by
  classical
  let e : {x // x ∈ s} ≃ {x // x ∈ t} :=
    Fintype.equivOfCardEq (by simpa using heq)
  let reference : Perm α := e.extendSubtype
  have href (x : α) : reference x ∈ t ↔ x ∈ s := by
    by_cases hx : x ∈ s
    · exact iff_of_true (e.extendSubtype_mem x hx) hx
    · exact iff_of_false (e.extendSubtype_not_mem x hx) hx
  rw [Fintype.card_congr (mappingEquivPreserving s t reference href), card_preserving]

/-- Literal set-image form of the uniform fibre theorem. A fixed set of
`r` labelled vertices occupies any prescribed `r` positions in exactly
`r! (N-r)!` permutations. -/
theorem card_image_eq (s t : Finset α) (heq : s.card = t.card) :
    Fintype.card {σ : Perm α // s.map σ.toEmbedding = t} =
      s.card.factorial * (Fintype.card α - s.card).factorial := by
  classical
  have hpred (σ : Perm α) :
      s.map σ.toEmbedding = t ↔ ∀ x, σ x ∈ t ↔ x ∈ s := by
    constructor
    · intro h x
      rw [← h]
      simp
    · intro h
      apply Finset.ext
      intro y
      obtain ⟨x, rfl⟩ := σ.surjective y
      simp [h]
  rw [Fintype.card_congr (Equiv.subtypeEquivRight hpred)]
  exact card_mapping s t heq

/-- Decompose the event that all vertices of `s` land in `allowed` by the
exact occupied position set. These fibres are disjoint by construction. -/
def imageSubsetEquiv (s allowed : Finset α) :
    {σ : Perm α // s.map σ.toEmbedding ⊆ allowed} ≃
      (t : ↥(allowed.powersetCard s.card)) ×
        {σ : Perm α // s.map σ.toEmbedding = t.1} where
  toFun σ := ⟨⟨s.map σ.1.toEmbedding,
    Finset.mem_powersetCard.mpr ⟨σ.2, Finset.card_map _⟩⟩, ⟨σ.1, rfl⟩⟩
  invFun τ := ⟨τ.2.1, by
    rw [τ.2.2]
    exact (Finset.mem_powersetCard.mp τ.1.2).1⟩
  left_inv _ := rfl
  right_inv τ := by
    rcases τ with ⟨⟨t, ht⟩, σ, hσ⟩
    cases hσ
    rfl

/-- General one-sided location count, including impossible capacity cases.
For `r=|s|`, `a=|allowed|`, `N=|α|`, the count is
`choose a r * r! * (N-r)!`. This is the integer-count core of P2b. -/
theorem card_image_subset (s allowed : Finset α) :
    Fintype.card {σ : Perm α // s.map σ.toEmbedding ⊆ allowed} =
      allowed.card.choose s.card *
        (s.card.factorial * (Fintype.card α - s.card).factorial) := by
  classical
  rw [Fintype.card_congr (imageSubsetEquiv s allowed), Fintype.card_sigma]
  have hfiber (t : ↥(allowed.powersetCard s.card)) :
      Fintype.card {σ : Perm α // s.map σ.toEmbedding = t.1} =
        s.card.factorial * (Fintype.card α - s.card).factorial :=
    card_image_eq s t.1 (Finset.mem_powersetCard.mp t.2).2.symm
  simp_rw [hfiber]
  simp [Finset.card_powersetCard]

/-- Normalize the preceding integer count by the size of the uniform
permutation sample space. This gives the binomial-ratio identity used in P2b,
for arbitrary finite free vertex sets (including the empty set). -/
theorem image_subset_ratio (s allowed : Finset α) :
    (Fintype.card {σ : Perm α // s.map σ.toEmbedding ⊆ allowed} : ℚ) /
        (Fintype.card (Perm α) : ℚ) =
      (allowed.card.choose s.card : ℚ) /
        ((Fintype.card α).choose s.card : ℚ) := by
  rw [card_image_subset, Fintype.card_perm,
    ← Nat.choose_mul_factorial_mul_factorial (Finset.card_le_univ s), Nat.mul_assoc]
  simp only [Nat.cast_mul]
  apply mul_div_mul_right
  exact mul_ne_zero (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _))
    (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _))

end Aris4Math.Counting

#print axioms Aris4Math.Counting.card_fixing
#print axioms Aris4Math.Counting.card_agreeing
#print axioms Aris4Math.Counting.card_prescribed_images
#print axioms Aris4Math.Counting.card_preserving
#print axioms Aris4Math.Counting.card_mapping
#print axioms Aris4Math.Counting.card_image_eq
#print axioms Aris4Math.Counting.card_image_subset
#print axioms Aris4Math.Counting.image_subset_ratio

import Aris4Math.Counting
import Mathlib.Data.Fintype.Sum

/-! General exact counts for two disjoint groups of labelled points. -/

namespace Aris4Math.JointCounting

open Equiv
open Aris4Math.Counting

variable {α : Type*} [Fintype α] [DecidableEq α]

private theorem sigmaPairSubtype_ext {β γ δ : Type*} {p : β → γ → δ → Prop}
    (a b : (x : β) × (y : γ) × {z : δ // p x y z})
    (hx : a.1 = b.1) (hy : a.2.1 = b.2.1) (hz : a.2.2.1 = b.2.2.1) : a = b := by
  rcases a with ⟨x, y, z, h⟩
  rcases b with ⟨x', y', z', h'⟩
  dsimp only at hx hy hz
  cases hx
  cases hy
  cases hz
  rfl

/-- Label the disjoint union of two vertex sets by a sum type. -/
def disjointEmbedding (A B : Finset α) (hAB : Disjoint A B) : (↥A ⊕ ↥B) ↪ α where
  toFun := Sum.elim Subtype.val Subtype.val
  inj' := by
    intro x y h
    cases x with
    | inl x =>
      cases y with
      | inl y => exact congrArg Sum.inl (Subtype.ext h)
      | inr y =>
        change (x : α) = y at h
        exact False.elim ((Finset.disjoint_left.mp hAB x.2) (h.symm ▸ y.2))
    | inr x =>
      cases y with
      | inl y =>
        change (x : α) = y at h
        exact False.elim ((Finset.disjoint_left.mp hAB y.2) (h ▸ x.2))
      | inr y => exact congrArg Sum.inr (Subtype.ext h)

/-- Restrict a permutation carrying one finite set exactly onto another. -/
def restrictImage (A T : Finset α) (σ : Perm α) (h : A.map σ.toEmbedding = T) :
    ↥A ≃ ↥T :=
  σ.subtypeEquiv (fun x => by rw [← h]; simp)

omit [Fintype α] [DecidableEq α] in
@[simp] theorem restrictImage_apply (A T : Finset α) (σ : Perm α)
    (h : A.map σ.toEmbedding = T) (x : ↥A) :
    (restrictImage A T σ h x : α) = σ x := rfl

/-- Combine two independent bijections between the two prescribed image sets. -/
def jointPositions (A B T U : Finset α) (hTU : Disjoint T U)
    (f : ↥A ≃ ↥T) (g : ↥B ≃ ↥U) : (↥A ⊕ ↥B) ↪ α :=
  (Equiv.sumCongr f g).toEmbedding.trans (disjointEmbedding T U hTU)

omit [Fintype α] [DecidableEq α] in
theorem image_eq_of_prescribed_left (A B T U : Finset α)
    (hAB : Disjoint A B) (hTU : Disjoint T U)
    (f : ↥A ≃ ↥T) (g : ↥B ≃ ↥U) (σ : Perm α)
    (h : ∀ i, σ (disjointEmbedding A B hAB i) = jointPositions A B T U hTU f g i) :
    A.map σ.toEmbedding = T := by
  apply Finset.ext
  intro y
  constructor
  · intro hy
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hy
    have hi := h (Sum.inl ⟨x, hx⟩)
    change σ x = (f ⟨x, hx⟩ : α) at hi
    exact hi ▸ (f ⟨x, hx⟩).2
  · intro hy
    obtain ⟨x, hx⟩ := f.surjective ⟨y, hy⟩
    refine Finset.mem_map.mpr ⟨x.1, x.2, ?_⟩
    have hi := h (Sum.inl x)
    change σ x = (f x : α) at hi
    exact hi.trans (congrArg Subtype.val hx)

omit [Fintype α] [DecidableEq α] in
theorem image_eq_of_prescribed_right (A B T U : Finset α)
    (hAB : Disjoint A B) (hTU : Disjoint T U)
    (f : ↥A ≃ ↥T) (g : ↥B ≃ ↥U) (σ : Perm α)
    (h : ∀ i, σ (disjointEmbedding A B hAB i) = jointPositions A B T U hTU f g i) :
    B.map σ.toEmbedding = U := by
  apply Finset.ext
  intro y
  constructor
  · intro hy
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hy
    have hi := h (Sum.inr ⟨x, hx⟩)
    change σ x = (g ⟨x, hx⟩ : α) at hi
    exact hi ▸ (g ⟨x, hx⟩).2
  · intro hy
    obtain ⟨x, hx⟩ := g.surjective ⟨y, hy⟩
    refine Finset.mem_map.mpr ⟨x.1, x.2, ?_⟩
    have hi := h (Sum.inr x)
    change σ x = (g x : α) at hi
    exact hi.trans (congrArg Subtype.val hx)

/-- Partition an exact two-set image event by the two bijections induced on
the labelled vertices. Each remaining fibre is a point-locking problem. -/
def jointImageEquiv (A B T U : Finset α)
    (hAB : Disjoint A B) (hTU : Disjoint T U) :
    {σ : Perm α // A.map σ.toEmbedding = T ∧ B.map σ.toEmbedding = U} ≃
      (f : ↥A ≃ ↥T) × (g : ↥B ≃ ↥U) ×
        {σ : Perm α // ∀ i, σ (disjointEmbedding A B hAB i) =
          jointPositions A B T U hTU f g i} where
  toFun σ := ⟨restrictImage A T σ.1 σ.2.1, restrictImage B U σ.1 σ.2.2,
    ⟨σ.1, by intro i; cases i <;> rfl⟩⟩
  invFun τ := ⟨τ.2.2.1,
    image_eq_of_prescribed_left A B T U hAB hTU τ.1 τ.2.1 τ.2.2.1 τ.2.2.2,
    image_eq_of_prescribed_right A B T U hAB hTU τ.1 τ.2.1 τ.2.2.1 τ.2.2.2⟩
  left_inv _ := rfl
  right_inv τ := by
    rcases τ with ⟨f, g, σ, h⟩
    have hf : restrictImage A T σ
        (image_eq_of_prescribed_left A B T U hAB hTU f g σ h) = f := by
      ext x
      exact h (Sum.inl x)
    have hg : restrictImage B U σ
        (image_eq_of_prescribed_right A B T U hAB hTU f g σ h) = g := by
      ext x
      exact h (Sum.inr x)
    exact sigmaPairSubtype_ext _ _ hf hg rfl

/-- Count the fibre in which two disjoint vertex sets occupy two specified
disjoint position sets of the respective sizes. -/
theorem card_joint_image_eq (A B T U : Finset α)
    (hAB : Disjoint A B) (hTU : Disjoint T U)
    (hAT : A.card = T.card) (hBU : B.card = U.card) :
    Fintype.card {σ : Perm α // A.map σ.toEmbedding = T ∧ B.map σ.toEmbedding = U} =
      A.card.factorial * (B.card.factorial *
        (Fintype.card α - A.card - B.card).factorial) := by
  classical
  let f : ↥A ≃ ↥T := Fintype.equivOfCardEq (by simpa using hAT)
  let g : ↥B ≃ ↥U := Fintype.equivOfCardEq (by simpa using hBU)
  have hcA : Fintype.card (↥A ≃ ↥T) = A.card.factorial := by
    rw [Fintype.card_equiv f, Fintype.card_coe]
  have hcB : Fintype.card (↥B ≃ ↥U) = B.card.factorial := by
    rw [Fintype.card_equiv g, Fintype.card_coe]
  rw [Fintype.card_congr (jointImageEquiv A B T U hAB hTU), Fintype.card_sigma]
  simp_rw [Fintype.card_sigma, card_prescribed_images,
    Fintype.card_sum, Fintype.card_coe]
  simp [hcA, hcB, Nat.sub_add_eq]

/-- Partition a joint allowed-position event by the exact two image sets. -/
def jointImageSubsetEquiv (A B L R : Finset α) :
    {σ : Perm α // A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} ≃
      (T : ↥(L.powersetCard A.card)) × (U : ↥(R.powersetCard B.card)) ×
        {σ : Perm α // A.map σ.toEmbedding = T.1 ∧ B.map σ.toEmbedding = U.1} where
  toFun σ := ⟨⟨A.map σ.1.toEmbedding,
      Finset.mem_powersetCard.mpr ⟨σ.2.1, Finset.card_map _⟩⟩,
    ⟨B.map σ.1.toEmbedding, Finset.mem_powersetCard.mpr ⟨σ.2.2, Finset.card_map _⟩⟩,
    ⟨σ.1, rfl, rfl⟩⟩
  invFun τ := ⟨τ.2.2.1, by
    constructor
    · rw [τ.2.2.2.1]
      exact (Finset.mem_powersetCard.mp τ.1.2).1
    · rw [τ.2.2.2.2]
      exact (Finset.mem_powersetCard.mp τ.2.1.2).1⟩
  left_inv _ := rfl
  right_inv τ := by
    rcases τ with ⟨⟨T, hT⟩, ⟨U, hU⟩, σ, hA, hB⟩
    cases hA
    cases hB
    rfl

/-- Exact joint counting formula. Source groups and allowed position groups
must each be disjoint; neither allowed group is required to be nonempty or
large enough. Impossible capacity cases are included as zero binomial counts. -/
theorem card_joint_image_subset (A B L R : Finset α)
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    Fintype.card {σ : Perm α // A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} =
      L.card.choose A.card * R.card.choose B.card * A.card.factorial *
        B.card.factorial * (Fintype.card α - A.card - B.card).factorial := by
  classical
  rw [Fintype.card_congr (jointImageSubsetEquiv A B L R), Fintype.card_sigma]
  have hfiber (T : ↥(L.powersetCard A.card)) (U : ↥(R.powersetCard B.card)) :
      Fintype.card {σ : Perm α // A.map σ.toEmbedding = T.1 ∧ B.map σ.toEmbedding = U.1} =
        A.card.factorial * (B.card.factorial *
          (Fintype.card α - A.card - B.card).factorial) := by
    have hT := Finset.mem_powersetCard.mp T.2
    have hU := Finset.mem_powersetCard.mp U.2
    exact card_joint_image_eq A B T.1 U.1 hAB (hLR.mono hT.1 hU.1) hT.2.symm hU.2.symm
  simp_rw [Fintype.card_sigma, hfiber]
  simp [Finset.card_powersetCard, Nat.mul_assoc]

/-- Normalize the joint count. This is the general two-sided binomial-ratio
formula in P4, before identifying its sets with hypergraph edge traces. -/
theorem joint_image_subset_ratio (A B L R : Finset α)
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    (Fintype.card {σ : Perm α //
        A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} : ℚ) /
        (Fintype.card (Perm α) : ℚ) =
      ((L.card.choose A.card : ℚ) * (R.card.choose B.card : ℚ)) /
        (((Fintype.card α).choose A.card : ℚ) *
          ((Fintype.card α - A.card).choose B.card : ℚ)) := by
  have hsum : A.card + B.card ≤ Fintype.card α := by
    rw [← Finset.card_union_of_disjoint hAB]
    exact Finset.card_le_univ _
  have hB : B.card ≤ Fintype.card α - A.card :=
    Nat.le_sub_of_add_le (by simpa [Nat.add_comm] using hsum)
  have hfac : (Fintype.card α).factorial =
      ((Fintype.card α).choose A.card * (Fintype.card α - A.card).choose B.card) *
        (A.card.factorial * B.card.factorial *
          (Fintype.card α - A.card - B.card).factorial) := by
    calc
      _ = (Fintype.card α).choose A.card * A.card.factorial *
          (Fintype.card α - A.card).factorial :=
        (Nat.choose_mul_factorial_mul_factorial (Finset.card_le_univ A)).symm
      _ = (Fintype.card α).choose A.card * A.card.factorial *
          ((Fintype.card α - A.card).choose B.card * B.card.factorial *
            (Fintype.card α - A.card - B.card).factorial) := by
        rw [Nat.choose_mul_factorial_mul_factorial hB]
      _ = _ := by ac_rfl
  rw [card_joint_image_subset A B L R hAB hLR, Fintype.card_perm, hfac]
  have hne : (A.card.factorial : ℚ) * B.card.factorial *
      (Fintype.card α - A.card - B.card).factorial ≠ 0 :=
    mul_ne_zero
      (mul_ne_zero (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _))
        (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)))
      (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _))
  simpa only [Nat.cast_mul, mul_assoc] using
    (mul_div_mul_right ((L.card.choose A.card : ℚ) * R.card.choose B.card)
      (((Fintype.card α).choose A.card : ℚ) *
        (Fintype.card α - A.card).choose B.card) hne)

section DifferentTypes

variable {β : Type*} [Fintype β] [DecidableEq β]

omit [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] in
private theorem transported_subset_iff (reference σ : α ≃ β)
    (A : Finset α) (L : Finset β) :
    A.map (σ.trans reference.symm).toEmbedding ⊆ L.map reference.symm.toEmbedding ↔
      A.map σ.toEmbedding ⊆ L := by
  change A.map (σ.toEmbedding.trans reference.symm.toEmbedding) ⊆ _ ↔ _
  rw [← Finset.map_map, Finset.map_subset_map]

/-- Use an explicit reference bijection only as coordinates; the count below
is independent of it. Vertices and positions may be different finite types. -/
def jointBijectionEquiv (reference : α ≃ β) (A B : Finset α) (L R : Finset β) :
    {σ : α ≃ β // A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} ≃
      {τ : Perm α // A.map τ.toEmbedding ⊆ L.map reference.symm.toEmbedding ∧
        B.map τ.toEmbedding ⊆ R.map reference.symm.toEmbedding} :=
  (Equiv.equivCongr (Equiv.refl α) reference.symm).subtypeEquiv (by
    intro σ
    exact (transported_subset_iff reference σ A L).symm.and
      (transported_subset_iff reference σ B R).symm)

/-- Joint counting for bijections between distinct finite types. -/
theorem card_joint_bijection_subset (reference : α ≃ β)
    (A B : Finset α) (L R : Finset β)
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    Fintype.card {σ : α ≃ β // A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} =
      L.card.choose A.card * R.card.choose B.card * A.card.factorial *
        B.card.factorial * (Fintype.card α - A.card - B.card).factorial := by
  rw [Fintype.card_congr (jointBijectionEquiv reference A B L R),
    card_joint_image_subset _ _ _ _ hAB ((Finset.disjoint_map _).mpr hLR)]
  simp only [Finset.card_map]

/-- The same normalized formula holds for distinct vertex and position types. -/
theorem joint_bijection_subset_ratio (reference : α ≃ β)
    (A B : Finset α) (L R : Finset β)
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    (Fintype.card {σ : α ≃ β //
        A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R} : ℚ) /
        (Fintype.card (α ≃ β) : ℚ) =
      ((L.card.choose A.card : ℚ) * (R.card.choose B.card : ℚ)) /
        (((Fintype.card α).choose A.card : ℚ) *
          ((Fintype.card α - A.card).choose B.card : ℚ)) := by
  rw [Fintype.card_congr (jointBijectionEquiv reference A B L R),
    Fintype.card_equiv reference, ← Fintype.card_perm (α := α)]
  simpa only [Finset.card_map] using
    joint_image_subset_ratio A B (L.map reference.symm.toEmbedding)
      (R.map reference.symm.toEmbedding) hAB ((Finset.disjoint_map _).mpr hLR)

end DifferentTypes

/-- The actual locked sample space is equivalent to all bijections from
the free vertices to the free positions. The two complement types are kept
distinct; no identification of them is silently assumed. -/
noncomputable def lockedEquivFree {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α) :
    {σ : Perm α // ∀ i, σ (vertices i) = positions i} ≃
      (↥((Set.range vertices)ᶜ) ≃ ↥((Set.range positions)ᶜ)) := by
  classical
  let e : Set.range vertices ≃ Set.range positions :=
    vertices.toEquivRange.symm.trans positions.toEquivRange
  have hpred (σ : Perm α) :
      (∀ i, σ (vertices i) = positions i) ↔
        ∀ x : Set.range vertices, σ x = e x := by
    constructor
    · intro h x
      rcases x with ⟨x, i, rfl⟩
      simpa [e] using h i
    · intro h i
      simpa [e] using h ⟨vertices i, Set.mem_range_self i⟩
  exact (Equiv.subtypeEquivRight hpred).trans (Equiv.Set.compl e)

omit [Fintype α] in
/-- Restricting a locked permutation preserves its actual action on every
free vertex. This is the event-transport interface, not just equality of counts. -/
theorem lockedEquivFree_apply {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α)
    (σ : {σ : Perm α // ∀ i, σ (vertices i) = positions i})
    (x : ↥((Set.range vertices)ᶜ)) :
    (lockedEquivFree vertices positions σ x : α) = σ.1 x := by
  classical
  rfl

/-- The number of genuinely free vertices after an injective set of locks. -/
theorem card_free_vertices {ι : Type*} [Fintype ι] (vertices : ι ↪ α) :
    Fintype.card ↥((Set.range vertices)ᶜ) = Fintype.card α - Fintype.card ι := by
  classical
  rw [Fintype.card_compl_set, ← Fintype.card_congr vertices.toEquivRange]

/-- An explicitly constructed coordinate bijection between the two free
types. It is used only to invoke the invariant bijection-counting theorem. -/
noncomputable def freeReference {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α) :
    ↥((Set.range vertices)ᶜ) ≃ ↥((Set.range positions)ᶜ) :=
  (vertices.toEquivRange.symm.trans positions.toEquivRange).toCompl

/-- Exact joint event count in the original locked-permutation sample space.
The domain of the outer subtype is precisely all permutations respecting the
given point locks, and each event is expressed using their genuine restriction
to free vertices (`lockedEquivFree_apply`). -/
theorem card_locked_joint_subset {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α)
    (A B : Finset ↥((Set.range vertices)ᶜ))
    (L R : Finset ↥((Set.range positions)ᶜ))
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    Fintype.card {σ : {σ : Perm α // ∀ i, σ (vertices i) = positions i} //
      A.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ L ∧
      B.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ R} =
        L.card.choose A.card * R.card.choose B.card * A.card.factorial *
          B.card.factorial *
            (Fintype.card α - Fintype.card ι - A.card - B.card).factorial := by
  classical
  let e := (lockedEquivFree vertices positions).subtypeEquiv
    (p := fun σ => A.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ L ∧
      B.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ R)
    (q := fun σ => A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R)
    (fun _ => Iff.rfl)
  rw [Fintype.card_congr e,
    card_joint_bijection_subset (freeReference vertices positions) A B L R hAB hLR,
    card_free_vertices]

/-- Conditional probability as an exact ratio of counts in the locked sample
space. No probabilistic independence assertion is assumed. -/
theorem locked_joint_subset_ratio {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α)
    (A B : Finset ↥((Set.range vertices)ᶜ))
    (L R : Finset ↥((Set.range positions)ᶜ))
    (hAB : Disjoint A B) (hLR : Disjoint L R) :
    (Fintype.card {σ : {σ : Perm α // ∀ i, σ (vertices i) = positions i} //
      A.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ L ∧
      B.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ R} : ℚ) /
        (Fintype.card {σ : Perm α // ∀ i, σ (vertices i) = positions i} : ℚ) =
      ((L.card.choose A.card : ℚ) * (R.card.choose B.card : ℚ)) /
        (((Fintype.card α - Fintype.card ι).choose A.card : ℚ) *
          ((Fintype.card α - Fintype.card ι - A.card).choose B.card : ℚ)) := by
  classical
  let e := (lockedEquivFree vertices positions).subtypeEquiv
    (p := fun σ => A.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ L ∧
      B.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ R)
    (q := fun σ => A.map σ.toEmbedding ⊆ L ∧ B.map σ.toEmbedding ⊆ R)
    (fun _ => Iff.rfl)
  rw [Fintype.card_congr e, Fintype.card_congr (lockedEquivFree vertices positions),
    joint_bijection_subset_ratio (freeReference vertices positions) A B L R hAB hLR,
    card_free_vertices]

/-- The one-sided location probability in the same real locked sample space;
this specializes the joint theorem with an empty second source/target group. -/
theorem locked_image_subset_ratio {ι : Type*} [Fintype ι]
    (vertices positions : ι ↪ α)
    (A : Finset ↥((Set.range vertices)ᶜ))
    (L : Finset ↥((Set.range positions)ᶜ)) :
    (Fintype.card {σ : {σ : Perm α // ∀ i, σ (vertices i) = positions i} //
      A.map (lockedEquivFree vertices positions σ).toEmbedding ⊆ L} : ℚ) /
        (Fintype.card {σ : Perm α // ∀ i, σ (vertices i) = positions i} : ℚ) =
      (L.card.choose A.card : ℚ) /
        ((Fintype.card α - Fintype.card ι).choose A.card : ℚ) := by
  simpa using locked_joint_subset_ratio vertices positions A ∅ L ∅
    (Finset.disjoint_empty_right _) (Finset.disjoint_empty_right _)

end Aris4Math.JointCounting

#print axioms Aris4Math.JointCounting.card_joint_image_eq
#print axioms Aris4Math.JointCounting.card_joint_image_subset
#print axioms Aris4Math.JointCounting.joint_image_subset_ratio
#print axioms Aris4Math.JointCounting.card_joint_bijection_subset
#print axioms Aris4Math.JointCounting.joint_bijection_subset_ratio
#print axioms Aris4Math.JointCounting.lockedEquivFree
#print axioms Aris4Math.JointCounting.lockedEquivFree_apply
#print axioms Aris4Math.JointCounting.card_free_vertices
#print axioms Aris4Math.JointCounting.card_locked_joint_subset
#print axioms Aris4Math.JointCounting.locked_joint_subset_ratio
#print axioms Aris4Math.JointCounting.locked_image_subset_ratio

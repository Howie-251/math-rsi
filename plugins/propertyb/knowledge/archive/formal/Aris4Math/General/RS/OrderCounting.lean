import Aris4Math.Counting
import Mathlib.Data.Finset.Sort
import Mathlib.Order.Interval.Finset.Fin
import Mathlib.Data.Real.Basic

/-! Relative orders of a fixed set of vertices in a uniform permutation. -/
namespace Aris4Math.General.RS

open Equiv


/-- `vertices` lists the active vertices. `τ` gives their ranks (vertex index to rank).
The global permutation likewise maps vertices to processing positions. -/
def HasOrderPattern {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (τ : Perm (Fin r)) (σ : Perm (Fin n)) : Prop :=
  StrictMono (fun i => σ (vertices (τ.symm i)))

noncomputable instance {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (τ : Perm (Fin r)) : DecidablePred (HasOrderPattern vertices τ) :=
  fun _ => Classical.propDecidable _

noncomputable def orderedPositions {n r : ℕ}
    (t : ↥((Finset.univ : Finset (Fin n)).powersetCard r)) : Fin r ↪o Fin n :=
  t.1.orderEmbOfFin (Finset.mem_powersetCard.mp t.2).2

/-- Fixing an order pattern and the occupied position set is equivalent to
fixing all active vertex images. -/
theorem orderPattern_iff_images {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (τ : Perm (Fin r)) (σ : Perm (Fin n))
    (t : ↥((Finset.univ : Finset (Fin n)).powersetCard r))
    (himage : (Finset.univ.map vertices).map σ.toEmbedding = t.1) :
    HasOrderPattern vertices τ σ ↔
      ∀ i, σ (vertices i) = orderedPositions t (τ i) := by
  constructor
  · intro h
    have heq : (fun i => σ (vertices (τ.symm i))) = orderedPositions t := by
      apply Finset.orderEmbOfFin_unique
      · intro i
        rw [← himage]
        simp only [Finset.mem_map, Finset.mem_univ, true_and]
        exact ⟨vertices (τ.symm i), ⟨τ.symm i, rfl⟩, rfl⟩
      · exact h
    intro i
    simpa using congrFun heq (τ i)
  · intro h i j hij
    simpa only [h, apply_symm_apply] using (orderedPositions t).strictMono hij

noncomputable def orderPatternEquiv {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (τ : Perm (Fin r)) :
    {σ : Perm (Fin n) // HasOrderPattern vertices τ σ} ≃
      (t : ↥((Finset.univ : Finset (Fin n)).powersetCard r)) ×
        {σ : Perm (Fin n) // ∀ i, σ (vertices i) = orderedPositions t (τ i)} where
  toFun σ := by
    let t : ↥((Finset.univ : Finset (Fin n)).powersetCard r) :=
      ⟨(Finset.univ.map vertices).map σ.1.toEmbedding,
        Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, by simp⟩⟩
    exact ⟨t, σ.1, (orderPattern_iff_images vertices τ σ.1 t rfl).mp σ.2⟩
  invFun q := by
    have himage : (Finset.univ.map vertices).map q.2.1.toEmbedding = q.1.1 := by
      ext x
      constructor
      · intro hx
        obtain ⟨v, hv, rfl⟩ := Finset.mem_map.mp hx
        obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hv
        change q.2.1 (vertices i) ∈ q.1.1
        rw [q.2.2 i]
        exact Finset.orderEmbOfFin_mem _ _ _
      · intro hx
        have hrange := Finset.range_orderEmbOfFin q.1.1
          (Finset.mem_powersetCard.mp q.1.2).2
        obtain ⟨j, hj⟩ := (Set.ext_iff.mp hrange x).mpr hx
        apply Finset.mem_map.mpr
        refine ⟨vertices (τ.symm j), Finset.mem_map.mpr ⟨τ.symm j, by simp, rfl⟩, ?_⟩
        change q.2.1 (vertices (τ.symm j)) = x
        rw [q.2.2, apply_symm_apply]
        exact hj
    exact ⟨q.2.1, (orderPattern_iff_images vertices τ q.2.1 q.1 himage).mpr q.2.2⟩
  left_inv σ := rfl
  right_inv q := by
    rcases q with ⟨⟨t, ht⟩, σ, hσ⟩
    have himage : (Finset.univ.map vertices).map σ.toEmbedding = t := by
      ext x
      constructor
      · intro hx
        obtain ⟨v, hv, rfl⟩ := Finset.mem_map.mp hx
        obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hv
        change σ (vertices i) ∈ t
        rw [hσ i]
        exact Finset.orderEmbOfFin_mem _ _ _
      · intro hx
        have hrange := Finset.range_orderEmbOfFin t (Finset.mem_powersetCard.mp ht).2
        obtain ⟨j, hj⟩ := (Set.ext_iff.mp hrange x).mpr hx
        apply Finset.mem_map.mpr
        refine ⟨vertices (τ.symm j), Finset.mem_map.mpr ⟨τ.symm j, by simp, rfl⟩, ?_⟩
        change σ (vertices (τ.symm j)) = x
        rw [hσ, apply_symm_apply]
        exact hj
    have hh : (⟨(Finset.univ.map vertices).map σ.toEmbedding,
        Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, by simp⟩⟩ :
        ↥((Finset.univ : Finset (Fin n)).powersetCard r)) = ⟨t, ht⟩ :=
      Subtype.ext himage
    refine Sigma.ext hh ?_
    exact (Subtype.heq_iff_coe_eq (fun s => by dsimp only; rw [hh])).mpr rfl

attribute [-instance] Nat.decidableForallFin in
/-- Every relative order of `r` active vertices occurs equally often. -/
theorem card_orderPattern {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (τ : Perm (Fin r)) :
    Fintype.card {σ : Perm (Fin n) // HasOrderPattern vertices τ σ} =
      n.choose r * (n-r).factorial := by
  classical
  rw [Fintype.card_congr (orderPatternEquiv vertices τ), Fintype.card_sigma]
  have hfiber (t : ↥((Finset.univ : Finset (Fin n)).powersetCard r)) :
      Fintype.card {σ : Perm (Fin n) //
        ∀ i, σ (vertices i) = orderedPositions t (τ i)} = (n-r).factorial := by
    simpa using Aris4Math.Counting.card_prescribed_images vertices
      (τ.toEmbedding.trans (orderedPositions t).toEmbedding)
  simp_rw [hfiber]
  simp [Finset.card_powersetCard]

/-- The actual relative rank permutation obtained by sorting the occupied positions. -/
noncomputable def relativeRank {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (σ : Perm (Fin n)) : Perm (Fin r) := by
  let t := (Finset.univ.map vertices).map σ.toEmbedding
  have ht : t.card = r := by simp [t]
  let e : Fin r ≃ ↥t := Equiv.ofBijective
    (fun i => ⟨σ (vertices i), by simp [t]⟩) (by
      constructor
      · intro i j h
        exact vertices.injective (σ.injective (congrArg Subtype.val h))
      · intro y
        obtain ⟨v, hv, heq⟩ := Finset.mem_map.mp y.2
        obtain ⟨i, _, rfl⟩ := Finset.mem_map.mp hv
        exact ⟨i, Subtype.ext heq⟩)
  exact e.trans (t.orderIsoOfFin ht).symm.toEquiv

theorem hasOrderPattern_relativeRank {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (σ : Perm (Fin n)) : HasOrderPattern vertices (relativeRank vertices σ) σ := by
  let t := (Finset.univ.map vertices).map σ.toEmbedding
  have ht : t.card = r := by simp [t]
  have h (i : Fin r) : σ (vertices ((relativeRank vertices σ).symm i)) =
      t.orderEmbOfFin ht i := by
    have h := (relativeRank vertices σ).apply_symm_apply i
    change (t.orderIsoOfFin ht).symm _ = i at h
    have h' := congrArg (fun j => ((t.orderIsoOfFin ht) j : Fin n)) h
    simpa using h'
  intro i j hij
  change σ (vertices ((relativeRank vertices σ).symm i)) <
    σ (vertices ((relativeRank vertices σ).symm j))
  rw [h i, h j]
  exact (t.orderEmbOfFin ht).strictMono hij

theorem orderPattern_unique {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (σ : Perm (Fin n)) (τ ρ : Perm (Fin r))
    (hτ : HasOrderPattern vertices τ σ) (hρ : HasOrderPattern vertices ρ σ) : τ = ρ := by
  let t : ↥((Finset.univ : Finset (Fin n)).powersetCard r) :=
    ⟨(Finset.univ.map vertices).map σ.toEmbedding,
      Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, by simp⟩⟩
  have hτ' := (orderPattern_iff_images vertices τ σ t rfl).mp hτ
  have hρ' := (orderPattern_iff_images vertices ρ σ t rfl).mp hρ
  apply Equiv.ext
  intro i
  apply (orderedPositions t).injective
  exact (hτ' i).symm.trans (hρ' i)

/-- The relative rank is exactly the unique pattern realized by the global order. -/
theorem relativeRank_eq_iff {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (σ : Perm (Fin n)) (τ : Perm (Fin r)) :
    relativeRank vertices σ = τ ↔ HasOrderPattern vertices τ σ := by
  constructor
  · intro h
    rw [← h]
    exact hasOrderPattern_relativeRank vertices σ
  · intro h
    exact orderPattern_unique vertices σ _ τ (hasOrderPattern_relativeRank vertices σ) h

noncomputable def relativeEventEquiv {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (P : Perm (Fin r) → Prop) :
    {σ : Perm (Fin n) // P (relativeRank vertices σ)} ≃
      (τ : {τ : Perm (Fin r) // P τ}) ×
        {σ : Perm (Fin n) // HasOrderPattern vertices τ.1 σ} where
  toFun σ := ⟨⟨relativeRank vertices σ.1, σ.2⟩,
    σ.1, hasOrderPattern_relativeRank vertices σ.1⟩
  invFun q := ⟨q.2.1, by
    rw [(relativeRank_eq_iff vertices q.2.1 q.1.1).mpr q.2.2]
    exact q.1.2⟩
  left_inv _ := rfl
  right_inv q := by
    refine Sigma.ext (Subtype.ext ?_) ?_
    · exact (relativeRank_eq_iff vertices q.2.1 q.1.1).mpr q.2.2
    · exact (Subtype.heq_iff_coe_eq (fun _ => by
        dsimp only
        rw [(relativeRank_eq_iff vertices q.2.1 q.1.1).mpr q.2.2])).mpr rfl

/-- An arbitrary event on the actual active relative order has uniform fibres. -/
theorem card_relativeEvent {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (P : Perm (Fin r) → Prop) [DecidablePred P] :
    Fintype.card {σ : Perm (Fin n) // P (relativeRank vertices σ)} =
      Fintype.card {τ : Perm (Fin r) // P τ} *
        (n.choose r * (n-r).factorial) := by
  classical
  rw [Fintype.card_congr (relativeEventEquiv vertices P), Fintype.card_sigma]
  simp_rw [card_orderPattern]
  simp

/-- Uniform relative order, normalized over the actual global permutation space. -/
theorem relativeEvent_ratio {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (P : Perm (Fin r) → Prop) [DecidablePred P] :
    (Fintype.card {σ : Perm (Fin n) // P (relativeRank vertices σ)} : ℝ) /
        Fintype.card (Perm (Fin n)) =
      (Fintype.card {τ : Perm (Fin r) // P τ} : ℝ) / r.factorial := by
  have hr : r ≤ n := by
    simpa using Fintype.card_le_of_injective vertices vertices.injective
  have hc : ((n.choose r : ℝ) * ((n-r).factorial : ℝ)) ≠ 0 := by
    apply mul_ne_zero
    · exact_mod_cast (Nat.choose_pos hr).ne'
    · exact_mod_cast Nat.factorial_ne_zero (n-r)
  rw [card_relativeEvent, Fintype.card_perm, Fintype.card_fin,
    ← Nat.choose_mul_factorial_mul_factorial hr]
  simp only [Nat.cast_mul]
  simpa only [mul_assoc, mul_left_comm, mul_comm] using
    (mul_div_mul_right (Fintype.card {τ : Perm (Fin r) // P τ} : ℝ)
      (r.factorial : ℝ) hc)

/-- The before/pivot/after relative-order event. -/
def BeforeAfter {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (σ : Perm (Fin n)) : Prop :=
  (∀ i ∈ A, σ i < σ x) ∧ (∀ i ∈ B, σ x < σ i)

noncomputable instance {n : ℕ} (A B : Finset (Fin n)) (x : Fin n) :
    DecidablePred (BeforeAfter A B x) := fun _ => Classical.propDecidable _

/-- For a full active domain, the before/after condition is precisely preservation
of the lower block together with fixing its endpoint. -/
theorem beforeAfter_intervals_iff {r : ℕ} (x : Fin r) (σ : Perm (Fin r)) :
    BeforeAfter (Finset.Iio x) (Finset.Ioi x) x σ ↔
      (∀ i, σ i ∈ Finset.Iio x ↔ i ∈ Finset.Iio x) ∧ σ x = x := by
  constructor
  · intro h
    have hiff (i : Fin r) : σ i < σ x ↔ i < x := by
      constructor
      · intro hi
        rcases lt_trichotomy i x with hix | hix | hix
        · exact hix
        · subst i; exact (lt_irrefl _ hi).elim
        · exact (lt_asymm hi (h.2 i (Finset.mem_Ioi.mpr hix))).elim
      · intro hi
        exact h.1 i (Finset.mem_Iio.mpr hi)
    have himage : (Finset.Iio x).map σ.toEmbedding = Finset.Iio (σ x) := by
      ext y
      obtain ⟨i, rfl⟩ := σ.surjective y
      simp [hiff]
    have hcard := congrArg Finset.card himage
    simp only [Finset.card_map, Fin.card_Iio] at hcard
    have hfix : σ x = x := Fin.ext hcard.symm
    exact ⟨by intro i; simpa only [Finset.mem_Iio, hfix] using hiff i, hfix⟩
  · rintro ⟨hp, hx⟩
    constructor
    · intro i hi
      simpa only [hx] using Finset.mem_Iio.mp ((hp i).mpr hi)
    · intro i hi
      have hni : ¬ σ i < x := by
        intro hh
        exact (not_lt_of_gt (Finset.mem_Ioi.mp hi))
          (Finset.mem_Iio.mp ((hp i).mp (Finset.mem_Iio.mpr hh)))
      have hne : σ i ≠ x := by
        intro heq
        have : i = x := σ.injective (heq.trans hx.symm)
        subst i
        exact (lt_irrefl _ (Finset.mem_Ioi.mp hi))
      rw [hx]
      exact lt_of_le_of_ne (le_of_not_gt hni) (Ne.symm hne)

/-- Independent permutations of a preserved block and of its complement,
with one distinguished complementary point fixed. -/
noncomputable def preservingFixingEquiv {α : Type*} [Fintype α] [DecidableEq α]
    (s : Finset α) (x : α) (hx : x ∉ s) :
    {σ : Perm α // (∀ i, σ i ∈ s ↔ i ∈ s) ∧ σ x = x} ≃
      Perm ↥s × {τ : Perm {i // i ∉ s} // τ ⟨x, hx⟩ = ⟨x, hx⟩} where
  toFun σ :=
    let q := Aris4Math.Counting.preservingEquiv (fun i => i ∈ s) ⟨σ.1, σ.2.1⟩
    ⟨q.1, q.2, by apply Subtype.ext; exact σ.2.2⟩
  invFun q := ⟨q.1.subtypeCongr q.2.1, by
    constructor
    · intro i
      by_cases hi : i ∈ s
      · rw [Perm.subtypeCongr.left_apply _ _ hi]
        exact iff_of_true (q.1 ⟨i, hi⟩).2 hi
      · rw [Perm.subtypeCongr.right_apply _ _ hi]
        exact iff_of_false (q.2.1 ⟨i, hi⟩).2 hi
    · rw [Perm.subtypeCongr.right_apply _ _ hx]
      exact congrArg Subtype.val q.2.2⟩
  left_inv σ := by
    apply Subtype.ext
    ext i
    by_cases hi : i ∈ s <;> simp [Perm.subtypeCongr.left_apply,
      Perm.subtypeCongr.right_apply, hi, Aris4Math.Counting.preservingEquiv]
  right_inv q := by
    apply Prod.ext
    · ext i
      simp [Aris4Math.Counting.preservingEquiv]
    · apply Subtype.ext
      ext i
      simp [Aris4Math.Counting.preservingEquiv]

theorem card_preserving_fixing {α : Type*} [Fintype α] [DecidableEq α]
    (s : Finset α) (x : α) (hx : x ∉ s) :
    Fintype.card {σ : Perm α // (∀ i, σ i ∈ s ↔ i ∈ s) ∧ σ x = x} =
      s.card.factorial * (Fintype.card α - s.card - 1).factorial := by
  classical
  rw [Fintype.card_congr (preservingFixingEquiv s x hx), Fintype.card_prod,
    Fintype.card_perm, Fintype.card_coe]
  have hf : Fintype.card {τ : Perm {i // i ∉ s} // τ ⟨x, hx⟩ = ⟨x, hx⟩} =
      (Fintype.card α - s.card - 1).factorial := by
    simpa [Fintype.card_subtype_compl] using
      Aris4Math.Counting.card_fixing ({⟨x, hx⟩} : Finset {i // i ∉ s})
  rw [hf]

/-- There are exactly `a! b!` relative orders with `a` specified vertices before
and `b` specified vertices after their common pivot. -/
theorem card_beforeAfter_intervals {r : ℕ} (x : Fin r) :
    Fintype.card {σ : Perm (Fin r) //
      BeforeAfter (Finset.Iio x) (Finset.Ioi x) x σ} =
      x.val.factorial * (r-x.val-1).factorial := by
  classical
  rw [Fintype.card_congr (Equiv.subtypeEquivRight (beforeAfter_intervals_iff x))]
  simpa using card_preserving_fixing (Finset.Iio x) x (by simp)

/-- Comparing actual positions is the same as comparing the induced active ranks. -/
theorem relativeRank_lt_iff {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (σ : Perm (Fin n)) (i j : Fin r) :
    relativeRank vertices σ i < relativeRank vertices σ j ↔
      σ (vertices i) < σ (vertices j) := by
  let t : ↥((Finset.univ : Finset (Fin n)).powersetCard r) :=
    ⟨(Finset.univ.map vertices).map σ.toEmbedding,
      Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, by simp⟩⟩
  have h := (orderPattern_iff_images vertices (relativeRank vertices σ) σ t rfl).mp
    (hasOrderPattern_relativeRank vertices σ)
  rw [h i, h j]
  exact (orderedPositions t).lt_iff_lt.symm

theorem beforeAfter_embedded_iff {n r : ℕ} (vertices : Fin r ↪ Fin n)
    (x : Fin r) (σ : Perm (Fin n)) :
    BeforeAfter ((Finset.Iio x).map vertices) ((Finset.Ioi x).map vertices)
        (vertices x) σ ↔
      BeforeAfter (Finset.Iio x) (Finset.Ioi x) x (relativeRank vertices σ) := by
  constructor
  · rintro ⟨hA, hB⟩
    exact ⟨fun i hi => (relativeRank_lt_iff vertices σ i x).mpr
      (hA _ (Finset.mem_map.mpr ⟨i, hi, rfl⟩)),
      fun i hi => (relativeRank_lt_iff vertices σ x i).mpr
      (hB _ (Finset.mem_map.mpr ⟨i, hi, rfl⟩))⟩
  · rintro ⟨hA, hB⟩
    constructor
    · intro i hi
      obtain ⟨j, hj, rfl⟩ := Finset.mem_map.mp hi
      exact (relativeRank_lt_iff vertices σ j x).mp (hA j hj)
    · intro i hi
      obtain ⟨j, hj, rfl⟩ := Finset.mem_map.mp hi
      exact (relativeRank_lt_iff vertices σ x j).mp (hB j hj)

/-- The factorial ratio for actual global processing permutations, for an arbitrary
embedded before/pivot/after active block. -/
theorem beforeAfter_embedded_ratio {n r : ℕ} (vertices : Fin r ↪ Fin n) (x : Fin r) :
    (Fintype.card {σ : Perm (Fin n) //
      BeforeAfter ((Finset.Iio x).map vertices) ((Finset.Ioi x).map vertices)
        (vertices x) σ} : ℝ) / Fintype.card (Perm (Fin n)) =
      ((x.val.factorial : ℝ) * (r-x.val-1).factorial) / r.factorial := by
  classical
  rw [Fintype.card_congr (Equiv.subtypeEquivRight (beforeAfter_embedded_iff vertices x))]
  rw [relativeEvent_ratio, card_beforeAfter_intervals, Nat.cast_mul]

/-- Number the active vertices with `A` first, then `x`, then `B`. This is only
an internal parametrization; the input sets need not respect their original labels. -/
noncomputable def blockEmbedding {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    Fin (A.card+B.card+1) ↪ Fin n := by
  let eA := (Fintype.equivFin ↥A).symm
  let eB := (Fintype.equivFin ↥B).symm
  let f : Fin (A.card+B.card+1) → Fin n := fun i =>
    if hi : i.val < A.card then eA ⟨i.val, by simpa using hi⟩
    else if hix : i.val = A.card then x
    else eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩
  refine ⟨f, ?_⟩
  intro i j hij
  have hdis : ∀ y, y ∈ A → y ∈ B → False := Finset.disjoint_left.mp hAB
  by_cases hi : i.val < A.card
  · by_cases hj : j.val < A.card
    · have hh : eA ⟨i.val, by simpa using hi⟩ = eA ⟨j.val, by simpa using hj⟩ := by
        apply Subtype.ext
        simpa [f, hi, hj] using hij
      have hh' := congrArg Fin.val (eA.injective hh)
      exact Fin.ext hh'
    · by_cases hjx : j.val = A.card
      · have hh : (eA ⟨i.val, by simpa using hi⟩ : Fin n) = x := by
          simpa [f, hi, hj, hjx] using hij
        exact (hxA (hh ▸ (eA ⟨i.val, by simpa using hi⟩).2)).elim
      · have hh : (eA ⟨i.val, by simpa using hi⟩ : Fin n) =
            eB ⟨j.val-A.card-1, by have := j.isLt; simp only [Fintype.card_coe]; omega⟩ := by
          simpa [f, hi, hj, hjx] using hij
        exact (hdis _ (eA ⟨i.val, by simpa using hi⟩).2
          (hh ▸ (eB ⟨j.val-A.card-1, by have := j.isLt; simp only [Fintype.card_coe]; omega⟩).2)).elim
  · by_cases hj : j.val < A.card
    · by_cases hix : i.val = A.card
      · have hh : x = (eA ⟨j.val, by simpa using hj⟩ : Fin n) := by
          simpa [f, hi, hj, hix] using hij
        exact (hxA (hh ▸ (eA ⟨j.val, by simpa using hj⟩).2)).elim
      · have hh : (eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩ : Fin n) =
            eA ⟨j.val, by simpa using hj⟩ := by
          simpa [f, hi, hj, hix] using hij
        exact (hdis _ (eA ⟨j.val, by simpa using hj⟩).2
          (hh ▸ (eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩).2)).elim
    · by_cases hix : i.val = A.card
      · by_cases hjx : j.val = A.card
        · exact Fin.ext (hix.trans hjx.symm)
        · have hh : x = (eB ⟨j.val-A.card-1, by have := j.isLt; simp only [Fintype.card_coe]; omega⟩ : Fin n) := by
            simpa [f, hi, hj, hix, hjx] using hij
          exact (hxB (hh ▸ (eB ⟨j.val-A.card-1, by have := j.isLt; simp only [Fintype.card_coe]; omega⟩).2)).elim
      · by_cases hjx : j.val = A.card
        · have hh : (eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩ : Fin n) = x := by
            simpa [f, hi, hj, hix, hjx] using hij
          exact (hxB (hh ▸ (eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩).2)).elim
        · have hh : eB ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩ =
              eB ⟨j.val-A.card-1, by have := j.isLt; simp only [Fintype.card_coe]; omega⟩ := by
            apply Subtype.ext
            simpa [f, hi, hj, hix, hjx] using hij
          have hh' := congrArg Fin.val (eB.injective hh)
          change i.val-A.card-1 = j.val-A.card-1 at hh'
          apply Fin.ext
          omega

theorem blockEmbedding_pivot {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    blockEmbedding A B x hAB hxA hxB ⟨A.card, by omega⟩ = x := by
  simp [blockEmbedding]

theorem blockEmbedding_before {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    (Finset.Iio (⟨A.card, by omega⟩ : Fin (A.card+B.card+1))).map
      (blockEmbedding A B x hAB hxA hxB) = A := by
  apply Finset.eq_of_subset_of_card_le
  · intro y hy
    obtain ⟨i, hi, rfl⟩ := Finset.mem_map.mp hy
    have hi' := Finset.mem_Iio.mp hi
    change i.val < A.card at hi'
    dsimp only [blockEmbedding, Function.Embedding.coeFn_mk]
    rw [dif_pos hi']
    exact ((Fintype.equivFin ↥A).symm ⟨i.val, by simpa using hi'⟩).2
  · simp only [Finset.card_map, Fin.card_Iio]
    exact le_refl _

theorem blockEmbedding_after {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    (Finset.Ioi (⟨A.card, by omega⟩ : Fin (A.card+B.card+1))).map
      (blockEmbedding A B x hAB hxA hxB) = B := by
  apply Finset.eq_of_subset_of_card_le
  · intro y hy
    obtain ⟨i, hi, rfl⟩ := Finset.mem_map.mp hy
    have hi' := Finset.mem_Ioi.mp hi
    change A.card < i.val at hi'
    have hia : ¬ i.val < A.card := by omega
    have hix : ¬ i.val = A.card := by omega
    dsimp only [blockEmbedding, Function.Embedding.coeFn_mk]
    rw [dif_neg hia, dif_neg hix]
    exact ((Fintype.equivFin ↥B).symm
      ⟨i.val-A.card-1, by have := i.isLt; simp only [Fintype.card_coe]; omega⟩).2
  · simp only [Finset.card_map, Fin.card_Ioi]
    omega

/-- Exact integer count, before normalization. Inactive vertices contribute the
same `choose n r * (n-r)!` extension factor for every active relative order. -/
theorem card_beforeAfter {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    Fintype.card {σ : Perm (Fin n) // BeforeAfter A B x σ} =
      (A.card.factorial * B.card.factorial) *
        (n.choose (A.card+B.card+1) * (n-(A.card+B.card+1)).factorial) := by
  classical
  let vertices := blockEmbedding A B x hAB hxA hxB
  let pivot : Fin (A.card+B.card+1) := ⟨A.card, by omega⟩
  have hA : (Finset.Iio pivot).map vertices = A := blockEmbedding_before A B x hAB hxA hxB
  have hB : (Finset.Ioi pivot).map vertices = B := blockEmbedding_after A B x hAB hxA hxB
  have hx : vertices pivot = x := blockEmbedding_pivot A B x hAB hxA hxB
  have hevent := beforeAfter_embedded_iff vertices pivot
  rw [hA, hB, hx] at hevent
  rw [Fintype.card_congr (Equiv.subtypeEquivRight hevent),
    card_relativeEvent, card_beforeAfter_intervals]
  dsimp only [pivot]
  have heq : A.card+B.card+1-A.card-1 = B.card := by omega
  rw [heq]

/-- Exact relative-order probability for arbitrary disjoint finite vertex sets,
with no restriction on the number of inactive vertices. `σ` maps vertices to positions. -/
theorem beforeAfter_ratio {n : ℕ} (A B : Finset (Fin n)) (x : Fin n)
    (hAB : Disjoint A B) (hxA : x ∉ A) (hxB : x ∉ B) :
    (Fintype.card {σ : Perm (Fin n) // BeforeAfter A B x σ} : ℝ) /
        Fintype.card (Perm (Fin n)) =
      ((A.card.factorial : ℝ) * B.card.factorial) /
        (A.card+B.card+1).factorial := by
  have h := beforeAfter_embedded_ratio (blockEmbedding A B x hAB hxA hxB)
    (⟨A.card, by omega⟩ : Fin (A.card+B.card+1))
  rw [blockEmbedding_before, blockEmbedding_after, blockEmbedding_pivot] at h
  have heq : A.card+B.card+1-A.card-1 = B.card := by omega
  simpa only [heq] using h

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.card_orderPattern
#print axioms Aris4Math.General.RS.relativeEvent_ratio
#print axioms Aris4Math.General.RS.card_beforeAfter
#print axioms Aris4Math.General.RS.beforeAfter_ratio

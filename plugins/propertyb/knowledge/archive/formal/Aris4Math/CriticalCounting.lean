import Aris4Math.EndpointCounting
import Aris4Math.Greedy
import Mathlib.Algebra.BigOperators.Field

/-! Identify actual ordered edge endpoints with the counted position events. -/

namespace Aris4Math.CriticalCounting

open Equiv
open Aris4Math.Counting Aris4Math.JointCounting Aris4Math.EndpointCounting

variable {v : ℕ} {ι : Type*} [Fintype ι]

abbrev Free (vertices : ι ↪ Fin v) := ↥((Set.range vertices)ᶜ)

def freePart (vertices : ι ↪ Fin v) (A : Finset (Fin v)) : Finset (Free vertices) :=
  A.subtype (fun x => x ∉ Set.range vertices)

def beforeSlots (positions : ι ↪ Fin v) (k : Fin v) : Finset (Free positions) :=
  Finset.univ.filter (fun x => x.1 < k)

def afterSlots (positions : ι ↪ Fin v) (k : Fin v) : Finset (Free positions) :=
  Finset.univ.filter (fun x => k < x.1)

def LocksBefore (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (k : Fin v) : Prop :=
  ∀ i, vertices i ∈ A → positions i < k

def LocksAfter (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (k : Fin v) : Prop :=
  ∀ i, vertices i ∈ A → k < positions i

/-- An actual maximum/minimum coincidence with a specified common vertex. -/
def SeparatedAt (A B : Finset (Fin v)) (x : Fin v) (σ : Perm (Fin v)) (k : Fin v) : Prop :=
  σ x = k ∧ (∀ y ∈ A.erase x, σ y < k) ∧ (∀ y ∈ B.erase x, k < σ y)

theorem freePart_disjoint (vertices : ι ↪ Fin v) (A B : Finset (Fin v))
    (hAB : Disjoint A B) : Disjoint (freePart vertices A) (freePart vertices B) := by
  apply Finset.disjoint_left.mpr
  intro x hxA hxB
  exact Finset.disjoint_left.mp hAB (Finset.mem_subtype.mp hxA) (Finset.mem_subtype.mp hxB)

theorem slots_disjoint (positions : ι ↪ Fin v) (k : Fin v) :
    Disjoint (beforeSlots positions k) (afterSlots positions k) := by
  apply Finset.disjoint_left.mpr
  intro x hxL hxR
  exact (not_lt_of_gt (Finset.mem_filter.mp hxL).2) (Finset.mem_filter.mp hxR).2

theorem all_before_iff (vertices positions : ι ↪ Fin v)
    (σ : Locked vertices positions) (A : Finset (Fin v)) (k : Fin v) :
    (∀ y ∈ A, σ.1 y < k) ↔
      LocksBefore vertices positions A k ∧
        (freePart vertices A).map (lockedEquivFree vertices positions σ).toEmbedding ⊆
          beforeSlots positions k := by
  constructor
  · intro h
    constructor
    · intro i hi
      simpa only [σ.2 i] using h (vertices i) hi
    · intro y hy
      obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hy
      apply Finset.mem_filter.mpr
      refine ⟨Finset.mem_univ _, ?_⟩
      change (lockedEquivFree vertices positions σ x : Fin v) < k
      rw [lockedEquivFree_apply]
      exact h x (Finset.mem_subtype.mp hx)
  · rintro ⟨hlocks, hfree⟩ y hy
    by_cases hyr : y ∈ Set.range vertices
    · obtain ⟨i, rfl⟩ := hyr
      rw [σ.2 i]
      exact hlocks i hy
    · let x : Free vertices := ⟨y, hyr⟩
      have hx : x ∈ freePart vertices A := Finset.mem_subtype.mpr hy
      have him := hfree (Finset.mem_map.mpr ⟨x, hx, rfl⟩)
      have hlt := (Finset.mem_filter.mp him).2
      simpa only [lockedEquivFree_apply] using hlt

theorem all_after_iff (vertices positions : ι ↪ Fin v)
    (σ : Locked vertices positions) (A : Finset (Fin v)) (k : Fin v) :
    (∀ y ∈ A, k < σ.1 y) ↔
      LocksAfter vertices positions A k ∧
        (freePart vertices A).map (lockedEquivFree vertices positions σ).toEmbedding ⊆
          afterSlots positions k := by
  constructor
  · intro h
    constructor
    · intro i hi
      simpa only [σ.2 i] using h (vertices i) hi
    · intro y hy
      obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hy
      apply Finset.mem_filter.mpr
      refine ⟨Finset.mem_univ _, ?_⟩
      change k < (lockedEquivFree vertices positions σ x : Fin v)
      rw [lockedEquivFree_apply]
      exact h x (Finset.mem_subtype.mp hx)
  · rintro ⟨hlocks, hfree⟩ y hy
    by_cases hyr : y ∈ Set.range vertices
    · obtain ⟨i, rfl⟩ := hyr
      rw [σ.2 i]
      exact hlocks i hy
    · let x : Free vertices := ⟨y, hyr⟩
      have hx : x ∈ freePart vertices A := Finset.mem_subtype.mpr hy
      have him := hfree (Finset.mem_map.mpr ⟨x, hx, rfl⟩)
      have hlt := (Finset.mem_filter.mp him).2
      simpa only [lockedEquivFree_apply] using hlt

theorem erases_disjoint (A B : Finset (Fin v)) (x : Fin v)
    (hinter : A ∩ B = {x}) : Disjoint (A.erase x) (B.erase x) := by
  apply Finset.disjoint_left.mpr
  intro y hyA hyB
  have hy : y ∈ A ∩ B := Finset.mem_inter.mpr
    ⟨(Finset.mem_erase.mp hyA).2, (Finset.mem_erase.mp hyB).2⟩
  rw [hinter, Finset.mem_singleton] at hy
  exact (Finset.mem_erase.mp hyA).1 hy

/-- The separated position event is exactly Greedy's actual critical-pair
predicate for a fixed distinct pair with singleton intersection. -/
theorem separated_iff_critical (A B : Finset (Fin v)) (x k : Fin v)
    (hneq : A ≠ B) (hinter : A ∩ B = {x}) (σ : Perm (Fin v)) :
    SeparatedAt A B x σ k ↔
      Aris4Math.Greedy.CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k := by
  have hx : x ∈ A ∩ B := by rw [hinter]; simp
  have hxA := (Finset.mem_inter.mp hx).1
  have hxB := (Finset.mem_inter.mp hx).2
  constructor
  · rintro ⟨hcenter, hleft, hright⟩
    refine ⟨?_, Finset.mem_map.mpr ⟨x, hxA, hcenter⟩,
      Finset.mem_map.mpr ⟨x, hxB, hcenter⟩, ?_, ?_, ?_⟩
    · exact fun heq => hneq ((Finset.map_injective _ ) heq)
    · intro y hy
      obtain ⟨z, hz, rfl⟩ := Finset.mem_map.mp hy
      by_cases hzx : z = x
      · simp [hzx, hcenter]
      · exact (hleft z (Finset.mem_erase.mpr ⟨hzx, hz⟩)).le
    · intro y hy
      obtain ⟨z, hz, rfl⟩ := Finset.mem_map.mp hy
      by_cases hzx : z = x
      · simp [hzx, hcenter]
      · exact (hright z (Finset.mem_erase.mpr ⟨hzx, hz⟩)).le
    · rw [← Finset.map_inter, hinter, Finset.map_singleton]
      simp only [Equiv.coe_toEmbedding, hcenter]
  · intro hcrit
    have hcenter : σ x = k := by
      have hm : σ x ∈ A.map σ.toEmbedding ∩ B.map σ.toEmbedding :=
        Finset.mem_inter.mpr ⟨Finset.mem_map.mpr ⟨x, hxA, rfl⟩,
          Finset.mem_map.mpr ⟨x, hxB, rfl⟩⟩
      rwa [hcrit.singleton_intersection, Finset.mem_singleton] at hm
    refine ⟨hcenter, ?_, ?_⟩
    · intro y hy
      have hle := hcrit.last_left (σ y)
        (Finset.mem_map.mpr ⟨y, (Finset.mem_erase.mp hy).2, rfl⟩)
      apply lt_of_le_of_ne hle
      intro heq
      exact (Finset.mem_erase.mp hy).1 (σ.injective (heq.trans hcenter.symm))
    · intro y hy
      have hle := hcrit.first_right (σ y)
        (Finset.mem_map.mpr ⟨y, (Finset.mem_erase.mp hy).2, rfl⟩)
      apply lt_of_le_of_ne hle
      intro heq
      exact (Finset.mem_erase.mp hy).1 (σ.injective (heq.symm.trans hcenter.symm))

def Compatible (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v) : Prop :=
  LocksBefore vertices positions (A.erase x) k ∧
    LocksAfter vertices positions (B.erase x) k

instance compatibleDecidable (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v) :
    Decidable (Compatible vertices positions A B x k) := by
  unfold Compatible LocksBefore LocksAfter
  infer_instance

/-- The joint weight is stated in actual set cardinalities, not in a profile
whose relation to a hypergraph would need to be assumed. -/
def locationWeight (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v) : ℚ :=
  let r := (freePart vertices (A.erase x)).card
  let q := (freePart vertices (B.erase x)).card
  let N := v - Fintype.card ι
  (((beforeSlots positions k).card.choose r : ℚ) *
    ((afterSlots positions k).card.choose q : ℚ)) /
    ((N.choose r : ℚ) * ((N - r).choose q : ℚ))

theorem locked_separated_iff (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (j : ι) (σ : Locked vertices positions) :
    SeparatedAt A B (vertices j) σ.1 (positions j) ↔
      Compatible vertices positions A B (vertices j) (positions j) ∧
        ((freePart vertices (A.erase (vertices j))).map
            (lockedEquivFree vertices positions σ).toEmbedding ⊆ beforeSlots positions (positions j) ∧
        (freePart vertices (B.erase (vertices j))).map
            (lockedEquivFree vertices positions σ).toEmbedding ⊆ afterSlots positions (positions j)) := by
  rw [SeparatedAt, σ.2 j, and_iff_right rfl,
    all_before_iff vertices positions σ, all_after_iff vertices positions σ]
  exact ⟨fun ⟨⟨hl, hf⟩, hr, hg⟩ => ⟨⟨hl, hr⟩, hf, hg⟩,
    fun ⟨⟨hl, hr⟩, hf, hg⟩ => ⟨⟨hl, hf⟩, hr, hg⟩⟩

/-- The locked-center location formula, including exact zero for incompatible
locked positions. Its event is the actual separated endpoint event. -/
theorem locked_separated_ratio (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (j : ι)
    (hAB : Disjoint (A.erase (vertices j)) (B.erase (vertices j))) :
    lockedRatio vertices positions (fun σ => SeparatedAt A B (vertices j) σ (positions j)) =
      if Compatible vertices positions A B (vertices j) (positions j) then
        locationWeight vertices positions A B (vertices j) (positions j) else 0 := by
  classical
  unfold lockedRatio
  by_cases hc : Compatible vertices positions A B (vertices j) (positions j)
  · rw [if_pos hc]
    have he (σ : Locked vertices positions) :=
      (locked_separated_iff vertices positions A B j σ).trans (and_iff_right hc)
    rw [Fintype.card_congr (Equiv.subtypeEquivRight he)]
    simpa only [locationWeight, Fintype.card_fin] using
      locked_joint_subset_ratio vertices positions
        (freePart vertices (A.erase (vertices j))) (freePart vertices (B.erase (vertices j)))
        (beforeSlots positions (positions j)) (afterSlots positions (positions j))
        (freePart_disjoint vertices _ _ hAB) (slots_disjoint positions (positions j))
  · rw [if_neg hc]
    have hempty : IsEmpty {σ : Locked vertices positions //
        SeparatedAt A B (vertices j) σ.1 (positions j)} :=
      ⟨fun σ => hc ((locked_separated_iff vertices positions A B j σ.1).mp σ.2).1⟩
    simp only [Fintype.card_eq_zero_iff.mpr hempty, Nat.cast_zero, zero_div]

/-- P4 for an actual fixed ordered edge pair, in exactly the critical-pair
predicate used by the proved greedy obstruction theorem. -/
theorem locked_critical_ratio (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (j : ι) (hneq : A ≠ B)
    (hinter : A ∩ B = {vertices j}) :
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) (positions j)) =
      if Compatible vertices positions A B (vertices j) (positions j) then
        locationWeight vertices positions A B (vertices j) (positions j) else 0 := by
  rw [lockedRatio_congr vertices positions _ _ (fun σ =>
    (separated_iff_critical A B (vertices j) (positions j) hneq hinter σ).symm)]
  exact locked_separated_ratio vertices positions A B j (erases_disjoint A B _ hinter)

theorem freePart_addLock_card (vertices : ι ↪ Fin v) (x : Fin v)
    (hx : x ∉ Set.range vertices) (A : Finset (Fin v)) (hxA : x ∉ A) :
    (freePart (addLock vertices x hx) A).card = (freePart vertices A).card := by
  rw [freePart, Finset.card_subtype, freePart, Finset.card_subtype]
  apply congrArg Finset.card
  apply Finset.filter_congr
  intro y hy
  have hyx : y ≠ x := fun h => hxA (h ▸ hy)
  simp only [mem_range_addLock_iff, hyx, false_or]

theorem beforeSlots_eq_freePart (positions : ι ↪ Fin v) (k : Fin v) :
    beforeSlots positions k = freePart positions (Finset.univ.filter (fun y => y < k)) := by
  ext x
  simp [beforeSlots, freePart]

theorem afterSlots_eq_freePart (positions : ι ↪ Fin v) (k : Fin v) :
    afterSlots positions k = freePart positions (Finset.univ.filter (fun y => k < y)) := by
  ext x
  simp [afterSlots, freePart]

theorem beforeSlots_addLock_card (positions : ι ↪ Fin v) (k : Fin v)
    (hk : k ∉ Set.range positions) :
    (beforeSlots (addLock positions k hk) k).card = (beforeSlots positions k).card := by
  rw [beforeSlots_eq_freePart, beforeSlots_eq_freePart]
  exact freePart_addLock_card positions k hk _ (by simp)

theorem afterSlots_addLock_card (positions : ι ↪ Fin v) (k : Fin v)
    (hk : k ∉ Set.range positions) :
    (afterSlots (addLock positions k hk) k).card = (afterSlots positions k).card := by
  rw [afterSlots_eq_freePart, afterSlots_eq_freePart]
  exact freePart_addLock_card positions k hk _ (by simp)

omit [Fintype ι] in
theorem compatible_addLock_iff (vertices positions : ι ↪ Fin v) (x k : Fin v)
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions)
    (A B : Finset (Fin v)) :
    Compatible (addLock vertices x hx) (addLock positions k hk) A B x k ↔
      Compatible vertices positions A B x k := by
  constructor
  · rintro ⟨hl, hr⟩
    exact ⟨fun i hi => hl (some i) hi, fun i hi => hr (some i) hi⟩
  · rintro ⟨hl, hr⟩
    constructor
    · intro i hi
      cases i with
      | none => exact False.elim (Finset.notMem_erase x A hi)
      | some i => exact hl i hi
    · intro i hi
      cases i with
      | none => exact False.elim (Finset.notMem_erase x B hi)
      | some i => exact hr i hi

/-- Fixed common-point weight for a free center. Here r and q count the
free points other than the uniquely specified common point. There is no
choice of common point and hence no extra edge-size multiplicity. -/
def freeLocationWeight (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v) : ℚ :=
  let r := (freePart vertices (A.erase x)).card
  let q := (freePart vertices (B.erase x)).card
  let N := v - Fintype.card ι
  (((beforeSlots positions k).card.choose r : ℚ) *
    ((afterSlots positions k).card.choose q : ℚ)) /
    ((N : ℚ) * ((N - 1).choose r : ℚ) * ((N - 1 - r).choose q : ℚ))

/-- P3 for an actual fixed ordered critical pair, with all incompatible lock
conditions giving zero. It is derived from the actual additional center lock
and P4, not from an assumed independence or multiplicity factor. -/
theorem free_critical_ratio (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v) (hneq : A ≠ B)
    (hinter : A ∩ B = {x})
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions) :
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) =
      if Compatible vertices positions A B x k then
        freeLocationWeight vertices positions A B x k else 0 := by
  classical
  let P := fun σ : Perm (Fin v) => Aris4Math.Greedy.CriticalPair
    (A.map σ.toEmbedding) (B.map σ.toEmbedding) k
  have hforces : ∀ σ, P σ → σ x = k := fun σ h =>
    ((separated_iff_critical A B x k hneq hinter σ).mpr h).1
  have hcond := extra_lock_event_ratio vertices positions x k hx hk P hforces
  change lockedRatio vertices positions P =
    lockedRatio (addLock vertices x hx) (addLock positions k hk) P *
      (1 / (Fintype.card (Fin v) - Fintype.card ι : ℕ)) at hcond
  change lockedRatio vertices positions P = _
  rw [hcond]
  have hlocked := locked_critical_ratio (addLock vertices x hx) (addLock positions k hk)
    A B none hneq hinter
  change lockedRatio (addLock vertices x hx) (addLock positions k hk) P = _ at hlocked
  rw [hlocked]
  simp only [addLock_none, compatible_addLock_iff, Fintype.card_fin]
  by_cases hc : Compatible vertices positions A B x k
  · rw [if_pos hc, if_pos hc]
    simp only [locationWeight, freeLocationWeight,
      freePart_addLock_card vertices x hx _ (Finset.notMem_erase x A),
      freePart_addLock_card vertices x hx _ (Finset.notMem_erase x B),
      beforeSlots_addLock_card, afterSlots_addLock_card, Fintype.card_option, Nat.sub_add_eq]
    simp only [div_mul_div_comm, mul_one]
    congr 1
    ac_rfl
  · simp only [if_neg hc, zero_mul]

/-- The same free-center calculation for the raw endpoint separation event;
this includes a singleton on one side, as needed for single-edge endpoints. -/
theorem free_separated_ratio (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x k : Fin v)
    (hAB : Disjoint (A.erase x) (B.erase x))
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions) :
    lockedRatio vertices positions (fun σ => SeparatedAt A B x σ k) =
      if Compatible vertices positions A B x k then
        freeLocationWeight vertices positions A B x k else 0 := by
  classical
  let P := fun σ : Perm (Fin v) => SeparatedAt A B x σ k
  have hcond := extra_lock_event_ratio vertices positions x k hx hk P (fun _ h => h.1)
  change lockedRatio vertices positions P =
    lockedRatio (addLock vertices x hx) (addLock positions k hk) P *
      (1 / (Fintype.card (Fin v) - Fintype.card ι : ℕ)) at hcond
  change lockedRatio vertices positions P = _
  rw [hcond]
  have hlocked := locked_separated_ratio (addLock vertices x hx) (addLock positions k hk)
    A B none hAB
  change lockedRatio (addLock vertices x hx) (addLock positions k hk) P = _ at hlocked
  rw [hlocked]
  simp only [addLock_none, compatible_addLock_iff, Fintype.card_fin]
  by_cases hc : Compatible vertices positions A B x k
  · rw [if_pos hc, if_pos hc]
    simp only [locationWeight, freeLocationWeight,
      freePart_addLock_card vertices x hx _ (Finset.notMem_erase x A),
      freePart_addLock_card vertices x hx _ (Finset.notMem_erase x B),
      beforeSlots_addLock_card, afterSlots_addLock_card, Fintype.card_option, Nat.sub_add_eq]
    simp only [div_mul_div_comm, mul_one]
    congr 1
    ac_rfl
  · simp only [if_neg hc, zero_mul]

/-- `last=true` is the maximum; `last=false` is the minimum. -/
def FixedEndpoint (A : Finset (Fin v)) (x : Fin v) (σ : Perm (Fin v))
    (k : Fin v) (last : Bool) : Prop :=
  σ x = k ∧ ∀ y ∈ A.erase x, if last then σ y < k else k < σ y

/-- Actual endpoint event, naming its unique vertex by the inverse permutation. -/
def EndpointAt (A : Finset (Fin v)) (σ : Perm (Fin v)) (k : Fin v) (last : Bool) : Prop :=
  σ.symm k ∈ A ∧ FixedEndpoint A (σ.symm k) σ k last

def EndpointCompatible (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (k : Fin v) (last : Bool) : Prop :=
  if last then LocksBefore vertices positions A k else LocksAfter vertices positions A k

instance endpointCompatibleDecidable (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (k : Fin v) (last : Bool) :
    Decidable (EndpointCompatible vertices positions A k last) := by
  unfold EndpointCompatible LocksBefore LocksAfter
  infer_instance

def endpointSlots (positions : ι ↪ Fin v) (k : Fin v) (last : Bool) : Finset (Free positions) :=
  if last then beforeSlots positions k else afterSlots positions k

omit [Fintype ι] in
theorem endpointCompatible_erase_free (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (x k : Fin v) (last : Bool) (hx : x ∉ Set.range vertices) :
    EndpointCompatible vertices positions (A.erase x) k last ↔
      EndpointCompatible vertices positions A k last := by
  have hm (i : ι) : vertices i ∈ A.erase x ↔ vertices i ∈ A := by
    simp only [Finset.mem_erase]
    exact and_iff_right (fun h => hx ⟨i, h⟩)
  cases last <;> simp only [EndpointCompatible, Bool.false_eq_true, ↓reduceIte,
    LocksBefore, LocksAfter, hm]

theorem freePart_erase_card (vertices : ι ↪ Fin v) (A : Finset (Fin v))
    (x : Free vertices) (hxA : (x : Fin v) ∈ A) :
    (freePart vertices (A.erase x)).card = (freePart vertices A).card - 1 := by
  have hset : freePart vertices (A.erase x) = (freePart vertices A).erase x := by
    ext y
    simp [freePart, Subtype.ext_iff]
  have hmem : x ∈ freePart vertices A := Finset.mem_subtype.mpr hxA
  rw [hset, Finset.card_erase_of_mem hmem]

@[simp] theorem freePart_empty (vertices : ι ↪ Fin v) : freePart vertices ∅ = ∅ := by
  ext x
  simp [freePart]

/-- Probability for one specified free endpoint. Multiplicity is not included
here; it appears only when the disjoint endpoint fibres are summed. -/
theorem fixed_free_endpoint_ratio (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (x : Free vertices) (hxA : (x : Fin v) ∈ A)
    (k : Fin v) (hk : k ∉ Set.range positions) (last : Bool) :
    lockedRatio vertices positions (fun σ => FixedEndpoint A x σ k last) =
      if EndpointCompatible vertices positions A k last then
        ((endpointSlots positions k last).card.choose ((freePart vertices A).card - 1) : ℚ) /
          ((v - Fintype.card ι : ℕ) *
            ((v - Fintype.card ι - 1).choose ((freePart vertices A).card - 1) : ℚ))
      else 0 := by
  classical
  cases last with
  | true =>
    have he (σ : Perm (Fin v)) : FixedEndpoint A x σ k true ↔
        SeparatedAt A {(x : Fin v)} x σ k := by
      simp [FixedEndpoint, SeparatedAt]
    rw [lockedRatio_congr vertices positions _ _ he,
      free_separated_ratio vertices positions A {(x : Fin v)} x k (by simp) x.2 hk]
    have hc := endpointCompatible_erase_free vertices positions A x k true x.2
    simp only [EndpointCompatible, ↓reduceIte] at hc
    simp [Compatible, LocksAfter, freeLocationWeight, endpointSlots, EndpointCompatible,
      hc, freePart_erase_card vertices A x hxA]
  | false =>
    have he (σ : Perm (Fin v)) : FixedEndpoint A x σ k false ↔
        SeparatedAt {(x : Fin v)} A x σ k := by
      simp [FixedEndpoint, SeparatedAt]
    rw [lockedRatio_congr vertices positions _ _ he,
      free_separated_ratio vertices positions {(x : Fin v)} A x k (by simp) x.2 hk]
    have hc := endpointCompatible_erase_free vertices positions A x k false x.2
    simp only [EndpointCompatible, Bool.false_eq_true, ↓reduceIte] at hc
    simp [Compatible, LocksBefore, freeLocationWeight, endpointSlots, EndpointCompatible,
      hc, freePart_erase_card vertices A x hxA]

private theorem sigmaSubtype_ext {β δ : Type*} {p : β → δ → Prop}
    (a b : (x : β) × {z : δ // p x z})
    (hx : a.1 = b.1) (hz : a.2.1 = b.2.1) : a = b := by
  rcases a with ⟨x, z, h⟩
  rcases b with ⟨x', z', h'⟩
  dsimp only at hx hz
  cases hx
  cases hz
  rfl

def freePreimage (vertices positions : ι ↪ Fin v) (σ : Locked vertices positions)
    (k : Fin v) (hk : k ∉ Set.range positions) : Free vertices :=
  ⟨σ.1.symm k, by
    rintro ⟨i, hi⟩
    apply hk
    refine ⟨i, ?_⟩
    rw [← σ.2 i, hi, Equiv.apply_symm_apply]⟩

/-- Partition the free-position endpoint event by its unique original vertex.
The index set is the actual free part of the edge, so its size is exactly r. -/
def endpointFibersEquiv (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (k : Fin v) (hk : k ∉ Set.range positions) (last : Bool) :
    {σ : Locked vertices positions // EndpointAt A σ.1 k last} ≃
      (x : ↥(freePart vertices A)) ×
        {σ : Locked vertices positions // FixedEndpoint A x.1 σ.1 k last} where
  toFun σ := ⟨⟨freePreimage vertices positions σ.1 k hk,
    Finset.mem_subtype.mpr σ.2.1⟩, ⟨σ.1, σ.2.2⟩⟩
  invFun τ := ⟨τ.2.1, by
    have he : τ.2.1.1.symm k = τ.1.1 :=
      τ.2.1.1.symm_apply_eq.mpr τ.2.2.1.symm
    constructor
    · rw [he]
      exact Finset.mem_subtype.mp τ.1.2
    · simpa only [he] using τ.2.2⟩
  left_inv _ := rfl
  right_inv τ := by
    refine sigmaSubtype_ext
      (p := fun (x : ↥(freePart vertices A)) (σ : Locked vertices positions) =>
        FixedEndpoint A x.1 σ.1 k last) _ τ ?_ rfl
    apply Subtype.ext
    apply Subtype.ext
    exact τ.2.1.1.symm_apply_eq.mpr τ.2.2.1.symm

/-- P2a: the endpoint multiplicity r is justified by an exact disjoint fibre
partition. It does not enter the fixed ordered-pair formulas. -/
theorem free_endpoint_ratio (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (k : Fin v) (hk : k ∉ Set.range positions) (last : Bool) :
    lockedRatio vertices positions (fun σ => EndpointAt A σ k last) =
      if EndpointCompatible vertices positions A k last then
        ((freePart vertices A).card : ℚ) *
          ((endpointSlots positions k last).card.choose ((freePart vertices A).card - 1) : ℚ) /
          ((v - Fintype.card ι : ℕ) *
            ((v - Fintype.card ι - 1).choose ((freePart vertices A).card - 1) : ℚ))
      else 0 := by
  classical
  unfold lockedRatio
  rw [Fintype.card_congr (endpointFibersEquiv vertices positions A k hk last),
    Fintype.card_sigma, Nat.cast_sum, Finset.sum_div]
  have hr (x : ↥(freePart vertices A)) :=
    fixed_free_endpoint_ratio vertices positions A x.1 (Finset.mem_subtype.mp x.2) k hk last
  simp only [lockedRatio] at hr
  simp_rw [hr]
  by_cases hc : EndpointCompatible vertices positions A k last <;>
    simp [hc, mul_div_assoc]

theorem freePart_erase_locked (vertices : ι ↪ Fin v) (A : Finset (Fin v)) (j : ι) :
    freePart vertices (A.erase (vertices j)) = freePart vertices A := by
  ext x
  have hne : (x : Fin v) ≠ vertices j := fun h => x.2 ⟨j, h.symm⟩
  simp [freePart, hne]

theorem fixed_locked_endpoint_ratio (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (j : ι) (last : Bool) :
    lockedRatio vertices positions (fun σ => FixedEndpoint A (vertices j) σ (positions j) last) =
      if EndpointCompatible vertices positions (A.erase (vertices j)) (positions j) last then
        ((endpointSlots positions (positions j) last).card.choose (freePart vertices A).card : ℚ) /
          ((v - Fintype.card ι).choose (freePart vertices A).card : ℚ)
      else 0 := by
  classical
  cases last with
  | true =>
    have he (σ : Perm (Fin v)) : FixedEndpoint A (vertices j) σ (positions j) true ↔
        SeparatedAt A {vertices j} (vertices j) σ (positions j) := by
      simp [FixedEndpoint, SeparatedAt]
    rw [lockedRatio_congr vertices positions _ _ he,
      locked_separated_ratio vertices positions A {vertices j} j (by simp)]
    simp [Compatible, LocksAfter, locationWeight, endpointSlots, EndpointCompatible,
      freePart_erase_locked]
  | false =>
    have he (σ : Perm (Fin v)) : FixedEndpoint A (vertices j) σ (positions j) false ↔
        SeparatedAt {vertices j} A (vertices j) σ (positions j) := by
      simp [FixedEndpoint, SeparatedAt]
    rw [lockedRatio_congr vertices positions _ _ he,
      locked_separated_ratio vertices positions {vertices j} A j (by simp)]
    simp [Compatible, LocksBefore, locationWeight, endpointSlots, EndpointCompatible,
      freePart_erase_locked]

/-- P2b for the actual single-edge endpoint. Membership of the locked center
and all other locked-point order constraints are checked before the formula. -/
theorem locked_endpoint_ratio (vertices positions : ι ↪ Fin v)
    (A : Finset (Fin v)) (j : ι) (last : Bool) :
    lockedRatio vertices positions (fun σ => EndpointAt A σ (positions j) last) =
      if vertices j ∈ A ∧
          EndpointCompatible vertices positions (A.erase (vertices j)) (positions j) last then
        ((endpointSlots positions (positions j) last).card.choose (freePart vertices A).card : ℚ) /
          ((v - Fintype.card ι).choose (freePart vertices A).card : ℚ)
      else 0 := by
  classical
  by_cases hm : vertices j ∈ A
  · have he (σ : Locked vertices positions) : EndpointAt A σ.1 (positions j) last ↔
        FixedEndpoint A (vertices j) σ.1 (positions j) last := by
      have hpre : σ.1.symm (positions j) = vertices j := σ.1.symm_apply_eq.mpr (σ.2 j).symm
      simp only [EndpointAt, hpre, hm, true_and]
    rw [lockedRatio_congr_on vertices positions _
      (fun σ => FixedEndpoint A (vertices j) σ (positions j) last) he,
      fixed_locked_endpoint_ratio]
    simp only [hm, true_and]
  · rw [if_neg (fun h => hm h.1)]
    apply lockedRatio_zero
    intro σ h
    have hpre : σ.1.symm (positions j) = vertices j := σ.1.symm_apply_eq.mpr (σ.2 j).symm
    exact hm (hpre ▸ h.1)

/-- The endpoint event used in the counts is exactly the usual maximum event. -/
theorem endpointAt_true_iff (A : Finset (Fin v)) (σ : Perm (Fin v)) (k : Fin v) :
    EndpointAt A σ k true ↔ k ∈ A.map σ.toEmbedding ∧ ∀ y ∈ A, σ y ≤ k := by
  constructor
  · rintro ⟨hm, _, hstrict⟩
    refine ⟨Finset.mem_map.mpr ⟨σ.symm k, hm, σ.apply_symm_apply k⟩, ?_⟩
    intro y hy
    by_cases he : y = σ.symm k
    · simp [he]
    · exact (hstrict y (Finset.mem_erase.mpr ⟨he, hy⟩)).le
  · rintro ⟨hm, hle⟩
    obtain ⟨x, hx, hxk⟩ := Finset.mem_map.mp hm
    have hpre : σ.symm k = x := σ.symm_apply_eq.mpr hxk.symm
    refine ⟨hpre ▸ hx, σ.apply_symm_apply k, ?_⟩
    intro y hy
    apply lt_of_le_of_ne (hle y (Finset.mem_erase.mp hy).2)
    intro he
    exact (Finset.mem_erase.mp hy).1 (σ.injective (he.trans (σ.apply_symm_apply k).symm))

/-- The endpoint event used in the counts is exactly the usual minimum event. -/
theorem endpointAt_false_iff (A : Finset (Fin v)) (σ : Perm (Fin v)) (k : Fin v) :
    EndpointAt A σ k false ↔ k ∈ A.map σ.toEmbedding ∧ ∀ y ∈ A, k ≤ σ y := by
  constructor
  · rintro ⟨hm, _, hstrict⟩
    refine ⟨Finset.mem_map.mpr ⟨σ.symm k, hm, σ.apply_symm_apply k⟩, ?_⟩
    intro y hy
    by_cases he : y = σ.symm k
    · simp [he]
    · exact (hstrict y (Finset.mem_erase.mpr ⟨he, hy⟩)).le
  · rintro ⟨hm, hle⟩
    obtain ⟨x, hx, hxk⟩ := Finset.mem_map.mp hm
    have hpre : σ.symm k = x := σ.symm_apply_eq.mpr hxk.symm
    refine ⟨hpre ▸ hx, σ.apply_symm_apply k, ?_⟩
    intro y hy
    apply lt_of_le_of_ne (hle y (Finset.mem_erase.mp hy).2)
    intro he
    exact (Finset.mem_erase.mp hy).1 (σ.injective (he.symm.trans (σ.apply_symm_apply k).symm))

/-- A real critical pair forces both of the single-edge endpoint events. -/
theorem critical_implies_endpoints (A B : Finset (Fin v)) (σ : Perm (Fin v)) (k : Fin v)
    (h : Aris4Math.Greedy.CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) :
    EndpointAt A σ k true ∧ EndpointAt B σ k false := by
  constructor
  · apply (endpointAt_true_iff A σ k).mpr
    exact ⟨h.mem_left, fun y hy => h.last_left (σ y) (Finset.mem_map.mpr ⟨y, hy, rfl⟩)⟩
  · apply (endpointAt_false_iff B σ k).mpr
    exact ⟨h.mem_right, fun y hy => h.first_right (σ y) (Finset.mem_map.mpr ⟨y, hy, rfl⟩)⟩

/-- Non-singleton intersections have no actual critical-pair outcomes. -/
theorem critical_intersection_card (A B : Finset (Fin v)) (σ : Perm (Fin v)) (k : Fin v)
    (h : Aris4Math.Greedy.CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) :
    (A ∩ B).card = 1 := by
  have hc := congrArg Finset.card h.singleton_intersection
  simpa only [← Finset.map_inter, Finset.card_map, Finset.card_singleton] using hc

theorem critical_ratio_zero_of_intersection (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (k : Fin v) (hcard : (A ∩ B).card ≠ 1) :
    lockedRatio vertices positions (fun σ => Aris4Math.Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) = 0 := by
  apply lockedRatio_zero
  intro σ h
  exact hcard (critical_intersection_card A B σ.1 k h)

end Aris4Math.CriticalCounting

#print axioms Aris4Math.CriticalCounting.separated_iff_critical
#print axioms Aris4Math.CriticalCounting.locked_separated_ratio
#print axioms Aris4Math.CriticalCounting.locked_critical_ratio
#print axioms Aris4Math.CriticalCounting.free_critical_ratio
#print axioms Aris4Math.CriticalCounting.fixed_free_endpoint_ratio
#print axioms Aris4Math.CriticalCounting.free_endpoint_ratio
#print axioms Aris4Math.CriticalCounting.fixed_locked_endpoint_ratio
#print axioms Aris4Math.CriticalCounting.locked_endpoint_ratio
#print axioms Aris4Math.CriticalCounting.endpointAt_true_iff
#print axioms Aris4Math.CriticalCounting.endpointAt_false_iff
#print axioms Aris4Math.CriticalCounting.critical_implies_endpoints
#print axioms Aris4Math.CriticalCounting.critical_ratio_zero_of_intersection

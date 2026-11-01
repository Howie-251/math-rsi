import Aris4Math.TypeCounting
import Aris4Math.CriticalCounting
import Mathlib.Order.Interval.Finset.Fin

/-! Semantic identification of the Numeric formulas with the actual locked
permutation experiment. The profile table is used only through its geometry;
single-edge formulas do not assume any probability identity. -/

namespace Aris4Math.ProfileProbability

open Aris4Math.TypeCounting Aris4Math.EndpointCounting Aris4Math.CriticalCounting

variable {v edgeCount : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

omit [Fintype ι] [DecidableEq ι] in
theorem position_injective (positions : ι ↪ Fin v) :
    Function.Injective (fun i => (positions i).val + 1) := by
  intro i j hij
  exact positions.injective (Fin.ext (Nat.add_right_cancel hij))

theorem mem_positionType (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (n : ℕ) :
    n ∈ positionType vertices positions A ↔
      ∃ i, vertices i ∈ A ∧ (positions i).val + 1 = n := by
  simp [positionType, positionSignature]

theorem position_mem_type (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (j : ι) :
    (positions j).val + 1 ∈ positionType vertices positions A ↔ vertices j ∈ A := by
  rw [mem_positionType]
  constructor
  · rintro ⟨i, hi, heq⟩
    exact (position_injective positions heq) ▸ hi
  · intro hj
    exact ⟨j, hj, rfl⟩

theorem positionType_length (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) :
    (positionType vertices positions A).length = (lockSignature vertices A).card := by
  rw [positionType, Finset.length_sort, positionSignature,
    Finset.card_image_of_injective _ (position_injective positions)]

theorem freePart_card (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) :
    (freePart vertices A).card = A.card - (positionType vertices positions A).length := by
  rw [positionType_length, freePart, Finset.card_subtype]
  have himage : (lockSignature vertices A).image vertices = A.filter (· ∈ Set.range vertices) := by
    ext x
    simp only [Finset.mem_image, mem_lockSignature, Finset.mem_filter, Set.mem_range]
    constructor
    · rintro ⟨i, hi, rfl⟩
      exact ⟨hi, i, rfl⟩
    · rintro ⟨hx, i, rfl⟩
      exact ⟨i, hx, rfl⟩
  have hcard : (A.filter (· ∈ Set.range vertices)).card = (lockSignature vertices A).card := by
    rw [← himage, Finset.card_image_of_injective _ vertices.injective]
  have hsum := Finset.filter_card_add_filter_neg_card_eq_card (s := A)
    (fun x => x ∈ Set.range vertices)
  rw [hcard] at hsum
  omega

theorem positions_length (H : Simple5Hypergraph (Fin v)) (vertices positions : ι ↪ Fin v)
    (p : Numeric.Profile) (hp : RealizesProfile H vertices positions p edgeCount) :
    p.positions.length = Fintype.card ι := by
  have heq := congrArg Finset.card hp.positions_eq
  rw [List.toFinset_card_of_nodup hp.valid.1,
    Finset.card_image_of_injective _ (position_injective positions), Finset.card_univ] at heq
  exact heq

theorem mem_positions (H : Simple5Hypergraph (Fin v)) (vertices positions : ι ↪ Fin v)
    (p : Numeric.Profile) (hp : RealizesProfile H vertices positions p edgeCount) (k : Fin v) :
    k.val + 1 ∈ p.positions ↔ k ∈ Set.range positions := by
  rw [← List.mem_toFinset, hp.positions_eq]
  simp only [Finset.mem_image, Finset.mem_univ, true_and, Set.mem_range]
  constructor <;> rintro ⟨i, hi⟩
  · exact ⟨i, Fin.ext (by omega)⟩
  · exact ⟨i, congrArg (fun x : Fin v => x.val + 1) hi⟩

theorem positions_filter_length (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount) (f : ℕ → Bool) :
    (p.positions.filter f).length =
      (Finset.univ.filter (fun i => f ((positions i).val + 1))).card := by
  rw [← List.toFinset_card_of_nodup (hp.valid.1.filter f), List.toFinset_filter,
    hp.positions_eq, Finset.filter_image,
    Finset.card_image_of_injective _ (position_injective positions)]

theorem beforeSlots_card (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount) (k : Fin v) :
    (beforeSlots positions k).card = Numeric.leftCount p (k.val + 1) := by
  rw [beforeSlots_eq_freePart, freePart_card positions positions, positionType_length]
  have hc : (Finset.univ.filter (fun y : Fin v => y < k)).card = k.val := by
    have heq : Finset.univ.filter (fun y : Fin v => y < k) = Finset.Iio k := by ext y; simp
    rw [heq, Fin.card_Iio]
  rw [hc]
  unfold Numeric.leftCount
  rw [positions_filter_length H vertices positions p hp]
  simp [lockSignature]

theorem afterSlots_card (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount) (k : Fin v) :
    (afterSlots positions k).card = Numeric.rightCount p (k.val + 1) := by
  rw [afterSlots_eq_freePart, freePart_card positions positions, positionType_length]
  have hc : (Finset.univ.filter (fun y : Fin v => k < y)).card = v - 1 - k.val := by
    have heq : Finset.univ.filter (fun y : Fin v => k < y) = Finset.Ioi k := by ext y; simp
    rw [heq, Fin.card_Ioi]
  rw [hc]
  unfold Numeric.rightCount
  rw [positions_filter_length H vertices positions p hp, hp.vertex_count]
  have hsub : v - 1 - k.val = v - (k.val + 1) := by omega
  simp [lockSignature, hsub]

theorem free_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount) :
    v - Fintype.card ι = Numeric.freeCount p := by
  simp [Numeric.freeCount, hp.vertex_count, positions_length H vertices positions p hp]

theorem all_before (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (k : Fin v) :
    ((positionType vertices positions A).all (fun n => n < k.val + 1)) ↔
      LocksBefore vertices positions A k := by
  rw [List.all_eq_true]
  constructor
  · intro h i hi
    have hh := h ((positions i).val + 1) ((position_mem_type _ _ _ _).mpr hi)
    simpa using hh
  · intro h n hn
    obtain ⟨i, hi, rfl⟩ := (mem_positionType _ _ _ _).mp hn
    simpa using h i hi

theorem all_after (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (k : Fin v) :
    ((positionType vertices positions A).all (fun n => k.val + 1 < n)) ↔
      LocksAfter vertices positions A k := by
  rw [List.all_eq_true]
  constructor
  · intro h i hi
    have hh := h ((positions i).val + 1) ((position_mem_type _ _ _ _).mpr hi)
    simpa using hh
  · intro h n hn
    obtain ⟨i, hi, rfl⟩ := (mem_positionType _ _ _ _).mp hn
    simpa using h i hi

theorem all_before_erase (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (j : ι) :
    (((positionType vertices positions A).filter (· != (positions j).val + 1)).all
      (fun n => n < (positions j).val + 1)) ↔
      LocksBefore vertices positions (A.erase (vertices j)) (positions j) := by
  simp only [List.all_eq_true, List.mem_filter, bne_iff_ne, decide_eq_true_eq]
  constructor
  · intro h i hi
    have hine : i ≠ j := fun he => (Finset.mem_erase.mp hi).1 (congrArg vertices he)
    have hh := h ((positions i).val + 1)
      ⟨(position_mem_type _ _ _ _).mpr (Finset.mem_erase.mp hi).2,
        fun he => hine (position_injective positions he)⟩
    simpa using hh
  · intro h n hn
    obtain ⟨i, hi, rfl⟩ := (mem_positionType _ _ _ _).mp hn.1
    have hne : vertices i ≠ vertices j := fun he => hn.2
      (congrArg (fun a => (positions a).val + 1) (vertices.injective he))
    simpa using h i (Finset.mem_erase.mpr ⟨hne, hi⟩)

theorem all_after_erase (vertices positions : ι ↪ Fin v) (A : Finset (Fin v)) (j : ι) :
    (((positionType vertices positions A).filter (· != (positions j).val + 1)).all
      (fun n => (positions j).val + 1 < n)) ↔
      LocksAfter vertices positions (A.erase (vertices j)) (positions j) := by
  simp only [List.all_eq_true, List.mem_filter, bne_iff_ne, decide_eq_true_eq]
  constructor
  · intro h i hi
    have hine : i ≠ j := fun he => (Finset.mem_erase.mp hi).1 (congrArg vertices he)
    have hh := h ((positions i).val + 1)
      ⟨(position_mem_type _ _ _ _).mpr (Finset.mem_erase.mp hi).2,
        fun he => hine (position_injective positions he)⟩
    simpa using hh
  · intro h n hn
    obtain ⟨i, hi, rfl⟩ := (mem_positionType _ _ _ _).mp hn.1
    have hne : vertices i ≠ vertices j := fun he => hn.2
      (congrArg (fun a => (positions a).val + 1) (vertices.injective he))
    simpa using h i (Finset.mem_erase.mpr ⟨hne, hi⟩)

/-- The actual first/last event equals P2 of the realized profile. The type's
count is irrelevant; in particular this accepts the aggregation layer's count 0. -/
theorem endpoint_ratio_numeric (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount) (A : Finset (Fin v)) (hA : A ∈ H.edges)
    (t : Numeric.EdgeType) (ht : t.locks = positionType vertices positions A)
    (k : Fin v) (last : Bool) :
    lockedRatio vertices positions (fun σ => EndpointAt A σ k last) =
      Numeric.edgeWeight p t (k.val + 1) last := by
  classical
  have hr : (freePart vertices A).card = 5 - t.locks.length := by
    rw [freePart_card vertices positions, H.five_uniform A hA, ← ht]
  have hN := free_count H vertices positions p hp
  have hL := beforeSlots_card H vertices positions p hp k
  have hR := afterSlots_card H vertices positions p hp k
  by_cases hk : k ∈ Set.range positions
  · obtain ⟨j, rfl⟩ := hk
    have hmem : (positions j).val + 1 ∈ p.positions :=
      (mem_positions H vertices positions p hp _).mpr ⟨j, rfl⟩
    rw [locked_endpoint_ratio]
    cases last <;>
      simp only [Numeric.edgeWeight, hmem, hr, hN, endpointSlots,
        hL, hR, Numeric.binom_eq_choose, ht, EndpointCompatible,
        Bool.false_eq_true, ↓reduceIte] <;>
      simp only [position_mem_type, all_before_erase, all_after_erase]
  · have hmem : k.val + 1 ∉ p.positions :=
      fun h => hk ((mem_positions H vertices positions p hp k).mp h)
    rw [free_endpoint_ratio _ _ _ _ hk]
    by_cases hz : 5 - t.locks.length = 0
    · cases last <;>
        simp [Numeric.edgeWeight, hmem, hr, hz]
    · have hpos : 1 ≤ 5 - t.locks.length := by omega
      rw [ht] at hpos
      cases last <;>
        simp only [Numeric.edgeWeight, hmem, hr, hN, endpointSlots,
          hL, hR, Nat.cast_mul, Numeric.binom_eq_choose, ht, EndpointCompatible,
          Bool.false_eq_true, ↓reduceIte] <;>
        simp only [all_before, all_after, hpos, true_and]

theorem numeric_pairWeight_nonneg (p : Numeric.Profile) (t u : Numeric.EdgeType) (k : ℕ) :
    0 ≤ Numeric.pairWeight p t u k := by
  unfold Numeric.pairWeight
  dsimp only
  split_ifs <;> first
  | exact div_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _)
  | exact le_refl 0

theorem type_common_mem (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x : Fin v) (hx : A ∩ B = {x}) (n : ℕ)
    (hnA : n ∈ positionType vertices positions A) (hnB : n ∈ positionType vertices positions B) :
    ∃ i, vertices i = x ∧ (positions i).val + 1 = n := by
  obtain ⟨i, hi, hip⟩ := (mem_positionType _ _ _ _).mp hnA
  obtain ⟨j, hj, hjp⟩ := (mem_positionType _ _ _ _).mp hnB
  have heq : i = j := position_injective positions (hip.trans hjp.symm)
  subst j
  have hxmem : vertices i ∈ A ∩ B := Finset.mem_inter.mpr ⟨hi, hj⟩
  rw [hx, Finset.mem_singleton] at hxmem
  exact ⟨i, hxmem, hip⟩

theorem free_types_disjoint (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (x : Fin v) (hx : A ∩ B = {x}) (hfree : x ∉ Set.range vertices) :
    (positionType vertices positions A).all (· ∉ positionType vertices positions B) := by
  rw [List.all_eq_true]
  intro n hn
  simp only [decide_eq_true_eq]
  intro hnb
  obtain ⟨i, hi, _⟩ := type_common_mem vertices positions A B x hx n hn hnb
  exact hfree ⟨i, hi⟩

omit [DecidableEq ι] in
theorem free_union_bound (vertices : ι ↪ Fin v) (A B : Finset (Fin v))
    (x : Fin v) (hx : A ∩ B = {x}) (hfree : x ∉ Set.range vertices) :
    (freePart vertices A).card + (freePart vertices B).card - 1 ≤ v - Fintype.card ι := by
  classical
  have hint : freePart vertices A ∩ freePart vertices B = {⟨x, hfree⟩} := by
    ext y
    simp only [Finset.mem_inter, freePart, Finset.mem_subtype, Finset.mem_singleton,
      Subtype.ext_iff]
    simpa only [Finset.mem_inter, Finset.mem_singleton] using (Finset.ext_iff.mp hx y.1)
  have hc := Finset.card_union_add_card_inter (freePart vertices A) (freePart vertices B)
  have hbound := Finset.card_le_univ (freePart vertices A ∪ freePart vertices B)
  rw [Aris4Math.JointCounting.card_free_vertices, Fintype.card_fin] at hbound
  rw [hint, Finset.card_singleton] at hc
  omega

omit [DecidableEq ι] in
theorem locked_free_disjoint (vertices : ι ↪ Fin v) (A B : Finset (Fin v))
    (j : ι) (hx : A ∩ B = {vertices j}) :
    Disjoint (freePart vertices A) (freePart vertices B) := by
  apply Finset.disjoint_left.mpr
  intro x hxA hxB
  have hm : x.1 ∈ A ∩ B :=
    Finset.mem_inter.mpr ⟨Finset.mem_subtype.mp hxA, Finset.mem_subtype.mp hxB⟩
  rw [hx, Finset.mem_singleton] at hm
  exact x.2 ⟨j, hm.symm⟩

omit [DecidableEq ι] in
theorem locked_union_bound (vertices : ι ↪ Fin v) (A B : Finset (Fin v))
    (j : ι) (hx : A ∩ B = {vertices j}) :
    (freePart vertices A).card + (freePart vertices B).card ≤ v - Fintype.card ι := by
  rw [← Finset.card_union_of_disjoint (locked_free_disjoint vertices A B j hx)]
  simpa only [Aris4Math.JointCounting.card_free_vertices, Fintype.card_fin] using
    Finset.card_le_univ (freePart vertices A ∪ freePart vertices B)

theorem locked_types_common (vertices positions : ι ↪ Fin v)
    (A B : Finset (Fin v)) (j : ι) (hx : A ∩ B = {vertices j}) :
    (positionType vertices positions A).filter (· ∈ positionType vertices positions B) =
      [(positions j).val + 1] := by
  have hnodup : (positionType vertices positions A).Nodup := by simp [positionType]
  apply List.Perm.eq_singleton
  apply List.perm_of_nodup_nodup_toFinset_eq (hnodup.filter _) (by simp)
  ext n
  simp only [List.mem_toFinset, List.mem_filter, decide_eq_true_eq, List.mem_singleton]
  constructor
  · rintro ⟨hna, hnb⟩
    obtain ⟨i, hi, hn⟩ := type_common_mem vertices positions A B (vertices j) hx n hna hnb
    have heq : i = j := vertices.injective hi
    simpa [heq] using hn.symm
  · rintro rfl
    have hmem : vertices j ∈ A ∩ B := hx.symm ▸ Finset.mem_singleton_self _
    exact ⟨(position_mem_type _ _ _ _).mpr (Finset.mem_inter.mp hmem).1,
      (position_mem_type _ _ _ _).mpr (Finset.mem_inter.mp hmem).2⟩

/-- P3 identification for an actual singleton-intersection pair whose center
and target position are both free. -/
theorem free_critical_ratio_numeric (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount)
    (A B : Finset (Fin v)) (hA : A ∈ H.edges) (hB : B ∈ H.edges) (hne : A ≠ B)
    (t u : Numeric.EdgeType) (ht : t.locks = positionType vertices positions A)
    (hu : u.locks = positionType vertices positions B)
    (x k : Fin v) (hinter : A ∩ B = {x})
    (hx : x ∉ Set.range vertices) (hk : k ∉ Set.range positions) :
    lockedRatio vertices positions (fun σ => Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) =
      Numeric.pairWeight p t u (k.val + 1) := by
  classical
  have hxAB : x ∈ A ∩ B := hinter.symm ▸ Finset.mem_singleton_self _
  have hxA := (Finset.mem_inter.mp hxAB).1
  have hxB := (Finset.mem_inter.mp hxAB).2
  have hr : (freePart vertices A).card = 5 - t.locks.length := by
    rw [freePart_card vertices positions, H.five_uniform A hA, ← ht]
  have hq : (freePart vertices B).card = 5 - u.locks.length := by
    rw [freePart_card vertices positions, H.five_uniform B hB, ← hu]
  have hrpos : 1 ≤ 5 - t.locks.length := by
    rw [← hr]
    exact Finset.one_le_card.mpr ⟨⟨x, hx⟩, Finset.mem_subtype.mpr hxA⟩
  have hqpos : 1 ≤ 5 - u.locks.length := by
    rw [← hq]
    exact Finset.one_le_card.mpr ⟨⟨x, hx⟩, Finset.mem_subtype.mpr hxB⟩
  have hN := free_count H vertices positions p hp
  have hL := beforeSlots_card H vertices positions p hp k
  have hR := afterSlots_card H vertices positions p hp k
  have hcap : 5 - t.locks.length + (5 - u.locks.length) - 1 ≤ Numeric.freeCount p := by
    rw [← hr, ← hq, ← hN]
    exact free_union_bound vertices A B x hinter hx
  have hdis : t.locks.all (· ∉ u.locks) := by
    rw [ht, hu]
    exact free_types_disjoint vertices positions A B x hinter hx
  have hmem : k.val + 1 ∉ p.positions := fun h =>
    hk ((mem_positions H vertices positions p hp k).mp h)
  have hbefore := all_before vertices positions A k
  have hafter := all_after vertices positions B k
  rw [← ht] at hbefore
  rw [← hu] at hafter
  have heraseA : LocksBefore vertices positions (A.erase x) k ↔ LocksBefore vertices positions A k := by
    simpa [EndpointCompatible] using endpointCompatible_erase_free vertices positions A x k true hx
  have heraseB : LocksAfter vertices positions (B.erase x) k ↔ LocksAfter vertices positions B k := by
    simpa [EndpointCompatible] using endpointCompatible_erase_free vertices positions B x k false hx
  have hden : Numeric.freeCount p - 1 - (5 - t.locks.length - 1) =
      Numeric.freeCount p - (5 - t.locks.length) := by omega
  rw [free_critical_ratio _ _ A B x k hne hinter hx hk]
  simp only [Numeric.pairWeight, hmem, ↓reduceIte, hrpos, hqpos, hdis, hcap,
    true_and, and_true, hbefore, hafter, Compatible, heraseA, heraseB,
    freeLocationWeight, freePart_erase_card vertices A ⟨x, hx⟩ hxA,
    freePart_erase_card vertices B ⟨x, hx⟩ hxB, hr, hq, hN, hL, hR, hden,
    Numeric.binom_eq_choose, Nat.cast_mul]

/-- P4 identification when the singleton intersection is the locked center. -/
theorem locked_critical_ratio_numeric (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount)
    (A B : Finset (Fin v)) (hA : A ∈ H.edges) (hB : B ∈ H.edges) (hne : A ≠ B)
    (t u : Numeric.EdgeType) (ht : t.locks = positionType vertices positions A)
    (hu : u.locks = positionType vertices positions B)
    (j : ι) (hinter : A ∩ B = {vertices j}) :
    lockedRatio vertices positions (fun σ => Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) (positions j)) =
      Numeric.pairWeight p t u ((positions j).val + 1) := by
  have hr : (freePart vertices A).card = 5 - t.locks.length := by
    rw [freePart_card vertices positions, H.five_uniform A hA, ← ht]
  have hq : (freePart vertices B).card = 5 - u.locks.length := by
    rw [freePart_card vertices positions, H.five_uniform B hB, ← hu]
  have hN := free_count H vertices positions p hp
  have hL := beforeSlots_card H vertices positions p hp (positions j)
  have hR := afterSlots_card H vertices positions p hp (positions j)
  have hcap : 5 - t.locks.length + (5 - u.locks.length) ≤ Numeric.freeCount p := by
    rw [← hr, ← hq, ← hN]
    exact locked_union_bound vertices A B j hinter
  have hcommon : t.locks.filter (· ∈ u.locks) = [(positions j).val + 1] := by
    rw [ht, hu]
    exact locked_types_common vertices positions A B j hinter
  have hmem : (positions j).val + 1 ∈ p.positions :=
    (mem_positions H vertices positions p hp _).mpr ⟨j, rfl⟩
  have hbefore := all_before_erase vertices positions A j
  have hafter := all_after_erase vertices positions B j
  rw [← ht] at hbefore
  rw [← hu] at hafter
  rw [locked_critical_ratio _ _ A B j hne hinter]
  simp only [Numeric.pairWeight, hmem, ↓reduceIte, hcommon, hcap,
    true_and, and_true, hbefore, hafter, Compatible,
    locationWeight, freePart_erase_locked, hr, hq, hN, hL, hR,
    Numeric.binom_eq_choose, Nat.cast_mul]
  rw [hcommon]
  by_cases hc : LocksBefore vertices positions (A.erase (vertices j)) (positions j) ∧
      LocksAfter vertices positions (B.erase (vertices j)) (positions j)
  · rw [if_pos hc, if_pos ⟨rfl, hbefore.mpr hc.1, hafter.mpr hc.2, hcap⟩]
  · rw [if_neg hc]
    rw [if_neg (fun h => hc ⟨hbefore.mp h.2.1, hafter.mp h.2.2.1⟩)]

/-- Actual ordered edge-pair probability is always bounded by its Numeric
type weight. This includes nonsingle intersections and mismatched locked
centers, whose actual critical event is empty. -/
theorem critical_ratio_le_numeric (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p edgeCount)
    (A B : Finset (Fin v)) (hA : A ∈ H.edges) (hB : B ∈ H.edges) (hne : A ≠ B)
    (t u : Numeric.EdgeType) (ht : t.locks = positionType vertices positions A)
    (hu : u.locks = positionType vertices positions B) (k : Fin v) :
    lockedRatio vertices positions (fun σ => Greedy.CriticalPair
      (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) ≤
      Numeric.pairWeight p t u (k.val + 1) := by
  classical
  by_cases hi : (A ∩ B).card = 1
  · obtain ⟨x, hx⟩ := Finset.card_eq_one.mp hi
    by_cases hl : x ∈ Set.range vertices
    · obtain ⟨j, rfl⟩ := hl
      by_cases hk : k = positions j
      · subst k
        exact (locked_critical_ratio_numeric H vertices positions p hp A B hA hB hne t u ht hu j hx).le
      · have hz : lockedRatio vertices positions (fun σ => Greedy.CriticalPair
            (A.map σ.toEmbedding) (B.map σ.toEmbedding) k) = 0 := by
          apply lockedRatio_zero
          intro σ hevent
          have hs := ((separated_iff_critical A B (vertices j) k hne hx σ.1).mpr hevent).1
          exact hk (hs.symm.trans (σ.2 j))
        rw [hz]
        exact numeric_pairWeight_nonneg p t u _
    · by_cases hk : k ∈ Set.range positions
      · obtain ⟨j, rfl⟩ := hk
        have hz : lockedRatio vertices positions (fun σ => Greedy.CriticalPair
            (A.map σ.toEmbedding) (B.map σ.toEmbedding) (positions j)) = 0 := by
          apply lockedRatio_zero
          intro σ hevent
          have hs := ((separated_iff_critical A B x (positions j) hne hx σ.1).mpr hevent).1
          have heq : x = vertices j := σ.1.injective (hs.trans (σ.2 j).symm)
          exact hl ⟨j, heq.symm⟩
        rw [hz]
        exact numeric_pairWeight_nonneg p t u _
      · exact (free_critical_ratio_numeric H vertices positions p hp A B hA hB hne
          t u ht hu x k hx hl hk).le
  · rw [critical_ratio_zero_of_intersection _ _ A B k hi]
    exact numeric_pairWeight_nonneg p t u _

end Aris4Math.ProfileProbability

#print axioms Aris4Math.ProfileProbability.endpoint_ratio_numeric
#print axioms Aris4Math.ProfileProbability.free_critical_ratio_numeric
#print axioms Aris4Math.ProfileProbability.locked_critical_ratio_numeric
#print axioms Aris4Math.ProfileProbability.critical_ratio_le_numeric

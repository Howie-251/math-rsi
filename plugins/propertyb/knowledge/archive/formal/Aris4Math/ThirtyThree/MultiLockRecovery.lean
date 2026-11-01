import Aris4Math.ThirtyThree.QuadProfiles

/-! Recover actual lock-type multiplicities from exact large traces and the
ordinary total, degree and pair-codegree data. Large traces retain multiplicity;
the construction is valid for both unit and nonunit pair codegrees. -/

open scoped BigOperators

namespace Aris4Math.ThirtyThree.MultiLockRecovery

open Aris4Math.TypeCounting

variable {n v : ℕ}

def count (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (T : Finset (Fin n)) : ℕ := multiplicity H.edges (lockSignature vertices) T

def upperCount (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (T : Finset (Fin n)) : ℕ :=
  (H.edges.filter fun e => T ⊆ lockSignature vertices e).card

def supers (T : Finset (Fin n)) (k : ℕ) : Finset (Finset (Fin n)) :=
  Finset.univ.filter fun U => T ⊆ U ∧ k ≤ U.card

theorem sum_counts (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (types : Finset (Finset (Fin n))) :
    (∑ T ∈ types, count H vertices T) =
      (H.edges.filter fun e => lockSignature vertices e ∈ types).card :=
  Finset.sum_card_fiberwise_eq_card_filter H.edges types (lockSignature vertices)

theorem sum_supers (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (T : Finset (Fin n)) :
    (∑ U ∈ Finset.univ.filter (fun U => T ⊆ U), count H vertices U) =
      upperCount H vertices T := by
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, upperCount] using
    sum_counts H vertices (Finset.univ.filter fun U => T ⊆ U)

theorem count_add_larger (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (T : Finset (Fin n)) :
    count H vertices T + (∑ U ∈ supers T (T.card+1), count H vertices U) =
      upperCount H vertices T := by
  have family : Finset.univ.filter (fun U => T ⊆ U) = insert T (supers T (T.card+1)) := by
    ext U
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert,
      supers]
    constructor
    · intro hsub
      by_cases h : U = T
      · exact Or.inl h
      · right
        have lt : T.card < U.card := by
          by_contra hle
          exact h (Finset.eq_of_subset_of_card_le hsub (by omega)).symm
        exact ⟨hsub, by omega⟩
    · rintro (rfl | h)
      · exact Finset.Subset.refl _
      · exact h.1
  have notSelf : T ∉ supers T (T.card+1) := by simp [supers]
  rw [← sum_supers H vertices T, family, Finset.sum_insert notSelf]

theorem upper_empty (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v) :
    upperCount H vertices ∅ = H.edges.card := by simp [upperCount]

theorem upper_singleton (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (i : Fin n) :
    upperCount H vertices {i} = H.degree (vertices i) := by
  simp [upperCount, Simple5Hypergraph.degree]

theorem upper_pair (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (i j : Fin n) :
    upperCount H vertices {i,j} = H.codegree (vertices i) (vertices j) := by
  simp [upperCount, Simple5Hypergraph.codegree, Finset.insert_subset_iff]

/-- Only totals, singleton degrees, and distinct-pair codegrees have to be
matched; values of `low` on larger sets never enter the recovery. -/
theorem upper_eq_of_low_data (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (low : Finset (Fin n) → ℕ)
    (empty : low ∅ = H.edges.card)
    (singles : ∀ i, low {i} = H.degree (vertices i))
    (pairs : ∀ i j, i ≠ j → low {i,j} = H.codegree (vertices i) (vertices j)) :
    ∀ T, T.card ≤ 2 → upperCount H vertices T = low T := by
  intro T small
  have cases : T.card = 0 ∨ T.card = 1 ∨ T.card = 2 := by omega
  rcases cases with h | h | h
  · have h := Finset.card_eq_zero.mp h
    subst T
    exact (upper_empty H vertices).trans empty.symm
  · obtain ⟨i,rfl⟩ := Finset.card_eq_one.mp h
    exact (upper_singleton H vertices i).trans (singles i).symm
  · obtain ⟨i,j,ij,rfl⟩ := Finset.card_eq_two.mp h
    exact (upper_pair H vertices i j).trans (pairs i j ij).symm

theorem count_le_codegree (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (T : Finset (Fin n)) (i j : Fin n)
    (hi : i ∈ T) (hj : j ∈ T) :
    count H vertices T ≤ H.codegree (vertices i) (vertices j) := by
  apply Finset.card_le_card
  intro e he
  obtain ⟨he,heq⟩ := Finset.mem_filter.mp he
  exact Finset.mem_filter.mpr ⟨he,
    (mem_lockSignature vertices e i).mp (heq ▸ hi),
    (mem_lockSignature vertices e j).mp (heq ▸ hj)⟩

theorem high_pair_budget (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (i j : Fin n) (ij : i ≠ j) :
    (∑ U ∈ supers {i,j} 3, count H vertices U) ≤
      H.codegree (vertices i) (vertices j) := by
  have h := count_add_larger H vertices {i,j}
  have hc : ({i,j} : Finset (Fin n)).card = 2 := by simp [ij]
  rw [hc, upper_pair] at h
  change count H vertices {i,j} + (∑ U ∈ supers {i,j} 3, count H vertices U) =
    H.codegree (vertices i) (vertices j) at h
  omega

theorem count_eq_zero_of_large (H : Simple5Hypergraph (Fin v))
    (vertices : Fin n ↪ Fin v) (T : Finset (Fin n)) (large : 5 < T.card) :
    count H vertices T = 0 := by
  by_contra h
  have positive : 0 < count H vertices T := by omega
  obtain ⟨e,he⟩ := Finset.card_pos.mp positive
  obtain ⟨he,hsig⟩ := Finset.mem_filter.mp he
  have sub : T.image vertices ⊆ e := by
    intro x hx
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hx
    exact (mem_lockSignature vertices e i).mp (hsig ▸ hi)
  have hcard := Finset.card_le_card sub
  rw [Finset.card_image_of_injective _ vertices.injective, H.five_uniform e he] at hcard
  omega

def recoveredPair (low high : Finset (Fin n) → ℕ) (T : Finset (Fin n)) : ℕ :=
  low T - ∑ U ∈ supers T 3, high U

def recoveredNonempty (low high : Finset (Fin n) → ℕ) (T : Finset (Fin n)) : ℕ :=
  if 3 ≤ T.card then high T else
  if T.card = 2 then recoveredPair low high T else
  low T - ∑ U ∈ supers T 2,
    if 3 ≤ U.card then high U else recoveredPair low high U

def recovered (low high : Finset (Fin n) → ℕ) (T : Finset (Fin n)) : ℕ :=
  if T = ∅ then low T - ∑ U ∈ supers T 1, recoveredNonempty low high U
  else recoveredNonempty low high T

theorem actual_pair (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (low high : Finset (Fin n) → ℕ)
    (hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T)
    (hhigh : ∀ T, 3 ≤ T.card → count H vertices T = high T)
    (T : Finset (Fin n)) (two : T.card = 2) :
    count H vertices T = recoveredPair low high T := by
  have h := count_add_larger H vertices T
  rw [two, hlow T (by omega)] at h
  have eq : (∑ U ∈ supers T 3, count H vertices U) = ∑ U ∈ supers T 3, high U := by
    apply Finset.sum_congr rfl
    intro U hU
    exact hhigh U (Finset.mem_filter.mp hU).2.2
  change count H vertices T + (∑ U ∈ supers T 3, count H vertices U) = low T at h
  rw [eq] at h
  unfold recoveredPair
  omega

theorem actual_nonempty (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (low high : Finset (Fin n) → ℕ)
    (hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T)
    (hhigh : ∀ T, 3 ≤ T.card → count H vertices T = high T)
    (T : Finset (Fin n)) (nonempty : T.Nonempty) :
    count H vertices T = recoveredNonempty low high T := by
  by_cases large : 3 ≤ T.card
  · simp only [recoveredNonempty, if_pos large]
    exact hhigh T large
  by_cases two : T.card = 2
  · simp only [recoveredNonempty, if_neg large, if_pos two]
    exact actual_pair H vertices low high hlow hhigh T two
  have one : T.card = 1 := by have h := Finset.card_pos.mpr nonempty; omega
  have h := count_add_larger H vertices T
  rw [one, hlow T (by omega)] at h
  have eq : (∑ U ∈ supers T 2, count H vertices U) =
      ∑ U ∈ supers T 2, if 3 ≤ U.card then high U else recoveredPair low high U := by
    apply Finset.sum_congr rfl
    intro U hU
    have lower := (Finset.mem_filter.mp hU).2.2
    split_ifs with hu
    · exact hhigh U hu
    · exact actual_pair H vertices low high hlow hhigh U (by omega)
  change count H vertices T + (∑ U ∈ supers T 2, count H vertices U) = low T at h
  rw [eq] at h
  simp only [recoveredNonempty, if_neg large, if_neg two]
  omega

theorem actual_recovered (H : Simple5Hypergraph (Fin v)) (vertices : Fin n ↪ Fin v)
    (low high : Finset (Fin n) → ℕ)
    (hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T)
    (hhigh : ∀ T, 3 ≤ T.card → count H vertices T = high T)
    (T : Finset (Fin n)) : count H vertices T = recovered low high T := by
  by_cases empty : T = ∅
  · subst T
    have h := count_add_larger H vertices (∅ : Finset (Fin n))
    rw [Finset.card_empty, hlow ∅ (by simp)] at h
    have eq : (∑ U ∈ supers (∅ : Finset (Fin n)) 1, count H vertices U) =
        ∑ U ∈ supers (∅ : Finset (Fin n)) 1, recoveredNonempty low high U := by
      apply Finset.sum_congr rfl
      intro U hU
      exact actual_nonempty H vertices low high hlow hhigh U
        (Finset.card_pos.mp (Finset.mem_filter.mp hU).2.2)
    change count H vertices ∅ + (∑ U ∈ supers (∅ : Finset (Fin n)) 1,
      count H vertices U) = low ∅ at h
    rw [eq] at h
    change count H vertices ∅ = low ∅ - ∑ U ∈ supers (∅ : Finset (Fin n)) 1,
      recoveredNonempty low high U
    omega
  · simp only [recovered, if_neg empty]
    exact actual_nonempty H vertices low high hlow hhigh T (Finset.nonempty_iff_ne_empty.mpr empty)

/-- Canonical one-based lock positions for a recovered label subset. -/
def canonicalType (positions : Fin n ↪ Fin v) (T : Finset (Fin n)) : List ℕ :=
  (T.image fun i => (positions i).val + 1).sort (· ≤ ·)

theorem canonicalType_injective (positions : Fin n ↪ Fin v) :
    Function.Injective (canonicalType positions) := by
  intro A B h
  have hs := congrArg List.toFinset h
  simp only [canonicalType, Finset.sort_toFinset] at hs
  exact Finset.image_injective (fun i j hij =>
    positions.injective (Fin.ext (Nat.add_right_cancel hij))) hs

theorem position_fiber_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin n ↪ Fin v) (T : Finset (Fin n)) :
    multiplicity H.edges (positionType vertices positions) (canonicalType positions T) =
      count H vertices T := by
  unfold multiplicity fiber count
  congr 1
  apply Finset.filter_congr
  intro e _
  change (canonicalType positions (lockSignature vertices e) = canonicalType positions T) ↔ _
  exact (canonicalType_injective positions).eq_iff

def rawProfile (labels : List (Finset (Fin n))) (positions : Fin n ↪ Fin v)
    (μ : Finset (Fin n) → ℕ) (centers : List ℕ) : Numeric.Profile where
  v := v
  positions := canonicalType positions Finset.univ
  types := labels.map fun T => ⟨canonicalType positions T, μ T⟩
  correctionCenters := centers

def profile (labels : List (Finset (Fin n))) (positions : Fin n ↪ Fin v)
    (μ : Finset (Fin n) → ℕ) (centers : List ℕ) : Numeric.Profile :=
  TripleProfiles.pruneZero (rawProfile labels positions μ centers)

theorem raw_table (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup) (all : ∀ T, T ∈ labels)
    (μ : Finset (Fin n) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ) :
    TableRealization H.edges (positionType vertices positions)
      (rawProfile labels positions μ centers) := by
  constructor
  · change ((labels.map (fun T => (⟨canonicalType positions T, μ T⟩ : Numeric.EdgeType))).map
      Numeric.EdgeType.locks).Nodup
    simpa only [List.map_map, Function.comp_def] using
      nodup.map (canonicalType_injective positions)
  · intro e _
    apply List.mem_map.mpr
    refine ⟨⟨canonicalType positions (lockSignature vertices e), μ (lockSignature vertices e)⟩, ?_, rfl⟩
    exact List.mem_map.mpr ⟨lockSignature vertices e,all _,rfl⟩
  · intro t ht
    obtain ⟨T,_,rfl⟩ := List.mem_map.mp ht
    exact (position_fiber_count H vertices positions T).trans (hμ T)

/-- Instantiate the old probability interface with all actual multiplicities.
The remaining premises concern only explicit finite data and its validity. -/
theorem realizes_recovered (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup) (all : ∀ T, T ∈ labels)
    (low high : Finset (Fin n) → ℕ)
    (hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T)
    (hhigh : ∀ T, 3 ≤ T.card → count H vertices T = high T)
    (centers : List ℕ)
    (valid : Numeric.validProfile (profile labels positions (recovered low high) centers) 33) :
    RealizesProfile H vertices positions
      (profile labels positions (recovered low high) centers) 33 := by
  refine ⟨rfl,valid,?_,TripleProfiles.table_pruneZero _ _ _
    (raw_table H vertices positions labels nodup all (recovered low high)
      (actual_recovered H vertices low high hlow hhigh) centers)⟩
  simp [profile, TripleProfiles.pruneZero, rawProfile, canonicalType]

end Aris4Math.ThirtyThree.MultiLockRecovery

#print axioms Aris4Math.ThirtyThree.MultiLockRecovery.actual_recovered
#print axioms Aris4Math.ThirtyThree.MultiLockRecovery.realizes_recovered

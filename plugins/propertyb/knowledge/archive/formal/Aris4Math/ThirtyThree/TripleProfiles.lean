import Aris4Math.ThirtyThree.DoubleLockAt
import Aris4Math.TripleLockProfiles

/-! Actual three-lock multiplicities for arbitrary degrees, pair codegrees and
triple codegree. Zero-count rows are pruned without changing the actual table. -/

open scoped BigOperators

namespace Aris4Math.ThirtyThree.TripleProfiles

open Aris4Math.TypeCounting

/-- Keep exactly the positive rows of a finite profile table. -/
def pruneZero (p : Numeric.Profile) : Numeric.Profile :=
  {p with types := p.types.filter fun t => 0 < t.count}

theorem table_pruneZero {α : Type*} [DecidableEq α] (E : Finset α)
    (classify : α → List ℕ) (p : Numeric.Profile)
    (h : TableRealization E classify p) : TableRealization E classify (pruneZero p) := by
  constructor
  · exact (List.filter_sublist.map Numeric.EdgeType.locks).nodup h.unique
  · intro e he
    obtain ⟨t,ht,heq⟩ := List.mem_map.mp (h.covers e he)
    have hm : e ∈ fiber E classify t.locks := Finset.mem_filter.mpr ⟨he,heq.symm⟩
    have hpos : 0 < t.count := by
      rw [← h.counts t ht]
      exact Finset.card_pos.mpr ⟨e,hm⟩
    exact List.mem_map.mpr ⟨t,List.mem_filter.mpr ⟨ht,by simpa using hpos⟩,heq⟩
  · intro t ht
    exact h.counts t (List.mem_filter.mp ht).1

def labels : List (Finset (Fin 3)) :=
  [∅,{0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}]

theorem labels_nodup : labels.Nodup := by decide +kernel

theorem mem_labels (T : Finset (Fin 3)) : T ∈ labels := by
  have h := Finset.mem_univ T
  rw [Aris4Math.TripleLockProfiles.label_univ] at h
  simpa [labels] using h

variable {v : ℕ}

def tripleCodegree (H : Simple5Hypergraph (Fin v)) (x y z : Fin v) : ℕ :=
  (H.edges.filter fun e => x ∈ e ∧ y ∈ e ∧ z ∈ e).card

def threeVertices (x y z : Fin v) (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z) :
    Fin 3 ↪ Fin v :=
  ⟨![x,y,z], by
    intro i j h
    fin_cases i <;> fin_cases j <;> simp_all⟩

def count (H : Simple5Hypergraph (Fin v)) (vertices : Fin 3 ↪ Fin v)
    (T : Finset (Fin 3)) : ℕ := multiplicity H.edges (lockSignature vertices) T

theorem triple_count_eq (H : Simple5Hypergraph (Fin v)) (vertices : Fin 3 ↪ Fin v) :
    count H vertices {0,1,2} = tripleCodegree H (vertices 0) (vertices 1) (vertices 2) := by
  unfold count multiplicity fiber tripleCodegree
  congr 1
  apply Finset.filter_congr
  intro e _
  constructor
  · intro hs
    have h0 : 0 ∈ lockSignature vertices e := by rw [hs]; decide
    have h1 : 1 ∈ lockSignature vertices e := by rw [hs]; decide
    have h2 : 2 ∈ lockSignature vertices e := by rw [hs]; decide
    exact ⟨(mem_lockSignature _ _ _).mp h0, (mem_lockSignature _ _ _).mp h1,
      (mem_lockSignature _ _ _).mp h2⟩
  · rintro ⟨h0,h1,h2⟩
    ext i
    fin_cases i <;> simp [mem_lockSignature,h0,h1,h2]

theorem sum_counts (H : Simple5Hypergraph (Fin v)) (vertices : Fin 3 ↪ Fin v)
    (types : Finset (Finset (Fin 3))) :
    (∑ T ∈ types, count H vertices T) =
      (H.edges.filter fun e => lockSignature vertices e ∈ types).card := by
  exact Finset.sum_card_fiberwise_eq_card_filter H.edges types (lockSignature vertices)

theorem sum_all_counts (H : Simple5Hypergraph (Fin v)) (vertices : Fin 3 ↪ Fin v) :
    (∑ T : Finset (Fin 3), count H vertices T) = H.edges.card := by
  simpa only [Finset.mem_univ, Finset.filter_true] using sum_counts H vertices Finset.univ

theorem sum_degree_counts (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 3 ↪ Fin v) (i : Fin 3) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T), count H vertices T) =
      H.degree (vertices i) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

theorem sum_codegree_counts (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 3 ↪ Fin v) (i j : Fin 3) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T), count H vertices T) =
      H.codegree (vertices i) (vertices j) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

/-- Inclusion-exclusion on eight actual signature classes. -/
def recovered (m d0 d1 d2 c01 c02 c12 t : ℕ) (T : Finset (Fin 3)) : ℕ :=
  if T = ∅ then m+c01+c02+c12-d0-d1-d2-t else
  if T = {0} then d0+t-c01-c02 else
  if T = {1} then d1+t-c01-c12 else
  if T = {2} then d2+t-c02-c12 else
  if T = {0,1} then c01-t else
  if T = {0,2} then c02-t else
  if T = {1,2} then c12-t else t

set_option maxHeartbeats 2000000 in
theorem actual_recovered (H : Simple5Hypergraph (Fin v)) (vertices : Fin 3 ↪ Fin v)
    (T : Finset (Fin 3)) :
    count H vertices T = recovered H.edges.card
      (H.degree (vertices 0)) (H.degree (vertices 1)) (H.degree (vertices 2))
      (H.codegree (vertices 0) (vertices 1)) (H.codegree (vertices 0) (vertices 2))
      (H.codegree (vertices 1) (vertices 2)) (count H vertices {0,1,2}) T := by
  have hall := sum_all_counts H vertices
  have hd0 := sum_degree_counts H vertices 0
  have hd1 := sum_degree_counts H vertices 1
  have hd2 := sum_degree_counts H vertices 2
  have hc01 := sum_codegree_counts H vertices 0 1
  have hc02 := sum_codegree_counts H vertices 0 2
  have hc12 := sum_codegree_counts H vertices 1 2
  rw [Aris4Math.TripleLockProfiles.label_univ] at hall hd0 hd1 hd2 hc01 hc02 hc12
  simp +decide only [Finset.filter_insert, Finset.filter_singleton, Finset.sum_insert,
    Finset.sum_singleton, Finset.mem_insert, Finset.mem_singleton,
    if_true, if_false] at hall hd0 hd1 hd2 hc01 hc02 hc12
  have ht := mem_labels T
  simp only [labels, List.mem_cons, List.not_mem_nil, or_false] at ht
  rcases ht with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp +decide only [recovered, if_true, if_false] <;> omega

/-- Canonical increasing one-based position signature of an abstract label. -/
def canonicalType (positions : Fin 3 ↪ Fin v) (T : Finset (Fin 3)) : List ℕ :=
  (T.image fun i => (positions i).val + 1).sort (· ≤ ·)

/-- An executable representative of the canonical type; unlike the quotient
sort implementation this finite insertion sort reduces in the kernel. -/
def executableType (positions : Fin 3 ↪ Fin v) (T : Finset (Fin 3)) : List ℕ :=
  (((List.finRange 3).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (positions : Fin 3 ↪ Fin v) (T : Finset (Fin 3)) :
    executableType positions T = canonicalType positions T := by
  have hn : (((List.finRange 3).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange 3).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [executableType,canonicalType,List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

theorem canonicalType_injective (positions : Fin 3 ↪ Fin v) :
    Function.Injective (canonicalType positions) := by
  intro A B h
  have hs := congrArg List.toFinset h
  simp only [canonicalType, Finset.sort_toFinset] at hs
  exact Finset.image_injective (fun i j hij =>
    positions.injective (Fin.ext (Nat.add_right_cancel hij))) hs

theorem position_fiber_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin 3 ↪ Fin v) (T : Finset (Fin 3)) :
    multiplicity H.edges (positionType vertices positions) (canonicalType positions T) =
      count H vertices T := by
  unfold multiplicity fiber count
  congr 1
  apply Finset.filter_congr
  intro e _
  change (canonicalType positions (lockSignature vertices e) = canonicalType positions T) ↔ _
  exact (canonicalType_injective positions).eq_iff

def rawProfile (positions : Fin 3 ↪ Fin v) (μ : Finset (Fin 3) → ℕ)
    (centers : List ℕ) : Numeric.Profile where
  v := v
  positions := canonicalType positions Finset.univ
  types := labels.map fun T => ⟨canonicalType positions T, μ T⟩
  correctionCenters := centers

def profile (positions : Fin 3 ↪ Fin v) (μ : Finset (Fin 3) → ℕ)
    (centers : List ℕ) : Numeric.Profile := pruneZero (rawProfile positions μ centers)

theorem raw_table (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 3 ↪ Fin v)
    (μ : Finset (Fin 3) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ) :
    TableRealization H.edges (positionType vertices positions) (rawProfile positions μ centers) := by
  constructor
  · change ((labels.map (fun T => (⟨canonicalType positions T, μ T⟩ : Numeric.EdgeType))).map
      Numeric.EdgeType.locks).Nodup
    simpa only [List.map_map, Function.comp_def] using
      labels_nodup.map (canonicalType_injective positions)
  · intro e _
    apply List.mem_map.mpr
    refine ⟨⟨canonicalType positions (lockSignature vertices e), μ (lockSignature vertices e)⟩, ?_, rfl⟩
    exact List.mem_map.mpr ⟨lockSignature vertices e,mem_labels _,rfl⟩
  · intro t ht
    obtain ⟨T,_,rfl⟩ := List.mem_map.mp ht
    exact (position_fiber_count H vertices positions T).trans (hμ T)

/-- The actual-H table is built here; finite validity is checked by each caller. -/
theorem realizes_profile (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 3 ↪ Fin v)
    (μ : Finset (Fin 3) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ)
    (valid : Numeric.validProfile (profile positions μ centers) 33) :
    RealizesProfile H vertices positions (profile positions μ centers) 33 := by
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices positions μ hμ centers)⟩
  simp [profile, pruneZero, rawProfile, canonicalType]

end Aris4Math.ThirtyThree.TripleProfiles

#print axioms Aris4Math.ThirtyThree.TripleProfiles.actual_recovered
#print axioms Aris4Math.ThirtyThree.TripleProfiles.realizes_profile

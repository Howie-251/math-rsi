import Aris4Math.ThirtyThree.TripleProfiles

/-! Four-lock actual multiplicities recovered from degrees, six pair codegrees,
four exact triple traces and the exact quadruple trace. -/
open scoped BigOperators
namespace Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero table_pruneZero)

def labels : List (Finset (Fin 4)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3}]

theorem labels_nodup : labels.Nodup := by decide +kernel

theorem label_univ : (Finset.univ : Finset (Finset (Fin 4))) = labels.toFinset := by decide +kernel

theorem mem_labels (T : Finset (Fin 4)) : T ∈ labels := by
  have h := Finset.mem_univ T
  rw [label_univ] at h
  exact List.mem_toFinset.mp h

variable {v : ℕ}

def count (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (T : Finset (Fin 4)) : ℕ := multiplicity H.edges (lockSignature vertices) T

theorem sum_counts (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (types : Finset (Finset (Fin 4))) :
    (∑ T ∈ types, count H vertices T) =
      (H.edges.filter fun e => lockSignature vertices e ∈ types).card := by
  exact Finset.sum_card_fiberwise_eq_card_filter H.edges types (lockSignature vertices)

theorem sum_all_counts (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v) :
    (∑ T : Finset (Fin 4), count H vertices T) = H.edges.card := by
  simpa only [Finset.mem_univ, Finset.filter_true] using sum_counts H vertices Finset.univ

theorem sum_degree_counts (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 4 ↪ Fin v) (i : Fin 4) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T), count H vertices T) =
      H.degree (vertices i) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

theorem sum_codegree_counts (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 4 ↪ Fin v) (i j : Fin 4) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T), count H vertices T) =
      H.codegree (vertices i) (vertices j) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

def pairLabels : Fin 6 → Finset (Fin 4) := ![{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}]
def highLabels : Fin 5 → Finset (Fin 4) := ![{0,1,2},{0,1,3},{0,2,3},{1,2,3},{0,1,2,3}]
def first : Fin 6 → Fin 4 := ![0,0,0,1,1,2]
def second : Fin 6 → Fin 4 := ![1,2,3,2,3,3]

def recovered (m : ℕ) (deg : Fin 4 → ℕ) (co : Fin 6 → ℕ) (high : Fin 5 → ℕ)
    (T : Finset (Fin 4)) : ℕ :=
  let pairs : Fin 6 → ℕ := ![co 0-high 0-high 1-high 4,
    co 1-high 0-high 2-high 4,co 2-high 1-high 2-high 4,
    co 3-high 0-high 3-high 4,co 4-high 1-high 3-high 4,co 5-high 2-high 3-high 4]
  let singles : Fin 4 → ℕ := ![deg 0-pairs 0-pairs 1-pairs 2-high 0-high 1-high 2-high 4,
    deg 1-pairs 0-pairs 3-pairs 4-high 0-high 1-high 3-high 4,
    deg 2-pairs 1-pairs 3-pairs 5-high 0-high 2-high 3-high 4,
    deg 3-pairs 2-pairs 4-pairs 5-high 1-high 2-high 3-high 4]
  if T=∅ then m-singles 0-singles 1-singles 2-singles 3-
    pairs 0-pairs 1-pairs 2-pairs 3-pairs 4-pairs 5-high 0-high 1-high 2-high 3-high 4 else
  if T={0} then singles 0 else
  if T={1} then singles 1 else
  if T={0,1} then pairs 0 else
  if T={2} then singles 2 else
  if T={0,2} then pairs 1 else
  if T={1,2} then pairs 3 else
  if T={0,1,2} then high 0 else
  if T={3} then singles 3 else
  if T={0,3} then pairs 2 else
  if T={1,3} then pairs 4 else
  if T={0,1,3} then high 1 else
  if T={2,3} then pairs 5 else
  if T={0,2,3} then high 2 else
  if T={1,2,3} then high 3 else
  high 4

theorem cons_val_five {α : Type*} {n : ℕ} (a : α) (u : Fin (n+5) → α) :
    Matrix.vecCons a u 5 = Matrix.vecHead (Matrix.vecTail (Matrix.vecTail (Matrix.vecTail (Matrix.vecTail u)))) := rfl

set_option maxHeartbeats 4000000 in
theorem actual_recovered (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (T : Finset (Fin 4)) : count H vertices T = recovered H.edges.card
      (fun i => H.degree (vertices i))
      (fun i => H.codegree (vertices (first i)) (vertices (second i)))
      (fun i => count H vertices (highLabels i)) T := by
  have hall := sum_all_counts H vertices
  have hd0 := sum_degree_counts H vertices 0
  have hd1 := sum_degree_counts H vertices 1
  have hd2 := sum_degree_counts H vertices 2
  have hd3 := sum_degree_counts H vertices 3
  have hc01 := sum_codegree_counts H vertices 0 1
  have hc02 := sum_codegree_counts H vertices 0 2
  have hc03 := sum_codegree_counts H vertices 0 3
  have hc12 := sum_codegree_counts H vertices 1 2
  have hc13 := sum_codegree_counts H vertices 1 3
  have hc23 := sum_codegree_counts H vertices 2 3
  rw [label_univ] at hall hd0 hd1 hd2 hd3 hc01 hc02 hc03 hc12 hc13 hc23
  simp +decide only [labels,List.toFinset_cons,List.toFinset_nil,Finset.filter_insert,
    Finset.filter_singleton,Finset.filter_empty,Finset.sum_insert,Finset.sum_singleton,
    Finset.sum_empty,Finset.mem_insert,Finset.mem_singleton,Finset.notMem_empty,
    if_true,if_false] at hall hd0 hd1 hd2 hd3 hc01 hc02 hc03 hc12 hc13 hc23
  have ht := mem_labels T
  simp only [labels,List.mem_cons,List.not_mem_nil,or_false] at ht
  rcases ht with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp +decide only [recovered,first,second,highLabels,Matrix.cons_val_zero,
      Matrix.cons_val_one,Matrix.cons_val_two,Matrix.cons_val_three,Matrix.cons_val_four,
      cons_val_five,Matrix.head_cons,Matrix.tail_cons,if_true,if_false] <;> omega

/-- Canonical increasing one-based position signature of an abstract label. -/
def canonicalType (positions : Fin 4 ↪ Fin v) (T : Finset (Fin 4)) : List ℕ :=
  (T.image fun i => (positions i).val + 1).sort (· ≤ ·)

/-- An executable representative of the canonical type; unlike the quotient
sort implementation this finite insertion sort reduces in the kernel. -/
def executableType (positions : Fin 4 ↪ Fin v) (T : Finset (Fin 4)) : List ℕ :=
  (((List.finRange 4).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (positions : Fin 4 ↪ Fin v) (T : Finset (Fin 4)) :
    executableType positions T = canonicalType positions T := by
  have hn : (((List.finRange 4).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange 4).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [executableType,canonicalType,List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

theorem canonicalType_injective (positions : Fin 4 ↪ Fin v) :
    Function.Injective (canonicalType positions) := by
  intro A B h
  have hs := congrArg List.toFinset h
  simp only [canonicalType, Finset.sort_toFinset] at hs
  exact Finset.image_injective (fun i j hij =>
    positions.injective (Fin.ext (Nat.add_right_cancel hij))) hs

theorem position_fiber_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin 4 ↪ Fin v) (T : Finset (Fin 4)) :
    multiplicity H.edges (positionType vertices positions) (canonicalType positions T) =
      count H vertices T := by
  unfold multiplicity fiber count
  congr 1
  apply Finset.filter_congr
  intro e _
  change (canonicalType positions (lockSignature vertices e) = canonicalType positions T) ↔ _
  exact (canonicalType_injective positions).eq_iff

def rawProfile (positions : Fin 4 ↪ Fin v) (μ : Finset (Fin 4) → ℕ)
    (centers : List ℕ) : Numeric.Profile where
  v := v
  positions := canonicalType positions Finset.univ
  types := labels.map fun T => ⟨canonicalType positions T, μ T⟩
  correctionCenters := centers

def profile (positions : Fin 4 ↪ Fin v) (μ : Finset (Fin 4) → ℕ)
    (centers : List ℕ) : Numeric.Profile := pruneZero (rawProfile positions μ centers)

theorem raw_table (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 4 ↪ Fin v)
    (μ : Finset (Fin 4) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ) :
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
theorem realizes_profile (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 4 ↪ Fin v)
    (μ : Finset (Fin 4) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ)
    (valid : Numeric.validProfile (profile positions μ centers) 33) :
    RealizesProfile H vertices positions (profile positions μ centers) 33 := by
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices positions μ hμ centers)⟩
  simp [profile, pruneZero, rawProfile, canonicalType]

end Aris4Math.ThirtyThree.QuadProfiles

#print axioms Aris4Math.ThirtyThree.QuadProfiles.actual_recovered
#print axioms Aris4Math.ThirtyThree.QuadProfiles.realizes_profile

import Aris4Math.TypeCounting
import Mathlib.Tactic.FinCases
import Mathlib.Data.Fin.VecNotation

/-! The actual three-lock profile at 23 vertices, recovered from degrees,
unit pair codegrees and absence of a triple edge. -/

open scoped BigOperators

namespace Aris4Math.TripleLockProfiles

open Aris4Math.TypeCounting

def threeVertices (x y z : Fin 23) (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z) :
    Fin 3 ↪ Fin 23 :=
  ⟨![x,y,z], by
    intro i j h
    fin_cases i <;> fin_cases j <;> simp_all⟩

def threePositions : Fin 3 ↪ Fin 23 :=
  ⟨fun i => ⟨i.val + 10, by omega⟩, by
    intro i j h
    apply Fin.ext
    exact Nat.add_right_cancel (congrArg Fin.val h)⟩

/-- The eight label sets, an enumeration of three lock indices only. -/
theorem label_univ : (Finset.univ : Finset (Finset (Fin 3))) =
    {∅, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}} := by decide +kernel

def count (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 3 ↪ Fin 23)
    (T : Finset (Fin 3)) : ℕ := multiplicity H.edges (lockSignature vertices) T

theorem sum_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 3 ↪ Fin 23)
    (types : Finset (Finset (Fin 3))) :
    (∑ T ∈ types, count H vertices T) =
      (H.edges.filter fun e => lockSignature vertices e ∈ types).card := by
  exact Finset.sum_card_fiberwise_eq_card_filter H.edges types (lockSignature vertices)

theorem sum_all_counts (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 3 ↪ Fin 23) :
    (∑ T : Finset (Fin 3), count H vertices T) = H.edges.card := by
  simpa only [Finset.mem_univ, Finset.filter_true] using sum_counts H vertices Finset.univ

theorem sum_degree_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 3 ↪ Fin 23) (i : Fin 3) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T), count H vertices T) =
      H.degree (vertices i) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

theorem sum_codegree_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 3 ↪ Fin 23) (i j : Fin 3) :
    (∑ T ∈ Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T), count H vertices T) =
      H.codegree (vertices i) (vertices j) := by
  have h := sum_counts H vertices (Finset.univ.filter (fun T => i ∈ T ∧ j ∈ T))
  simpa only [Finset.mem_filter, Finset.mem_univ, true_and, mem_lockSignature] using h

theorem triple_count_zero (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 3 ↪ Fin 23)
    (noTriple : ∀ e ∈ H.edges, ¬ (vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e)) :
    count H vertices {0,1,2} = 0 := by
  unfold count multiplicity fiber
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro e he
  obtain ⟨he, ht⟩ := Finset.mem_filter.mp he
  apply noTriple e he
  have hx : 0 ∈ lockSignature vertices e := by rw [ht]; decide
  have hy : 1 ∈ lockSignature vertices e := by rw [ht]; decide
  have hz : 2 ∈ lockSignature vertices e := by rw [ht]; decide
  exact ⟨(mem_lockSignature _ _ _).mp hx, (mem_lockSignature _ _ _).mp hy,
    (mem_lockSignature _ _ _).mp hz⟩

set_option maxHeartbeats 2000000 in
/-- Exact fiber counts follow by partitioning actual edges over eight labels;
only the label sets are enumerated, never the hypergraphs or permutations. -/
theorem counts_677 (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 3 ↪ Fin 23)
    (edges32 : H.edges.card = 32)
    (d0 : H.degree (vertices 0) = 6) (d1 : H.degree (vertices 1) = 7)
    (d2 : H.degree (vertices 2) = 7)
    (c01 : H.codegree (vertices 0) (vertices 1) = 1)
    (c02 : H.codegree (vertices 0) (vertices 2) = 1)
    (c12 : H.codegree (vertices 1) (vertices 2) = 1)
    (noTriple : ∀ e ∈ H.edges, ¬ (vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e)) :
    count H vertices ∅ = 15 ∧ count H vertices {0} = 4 ∧
    count H vertices {1} = 5 ∧ count H vertices {2} = 5 ∧
    count H vertices {0,1} = 1 ∧ count H vertices {0,2} = 1 ∧
    count H vertices {1,2} = 1 ∧ count H vertices {0,1,2} = 0 := by
  have hall := sum_all_counts H vertices
  have hd0 := sum_degree_counts H vertices 0
  have hd1 := sum_degree_counts H vertices 1
  have hd2 := sum_degree_counts H vertices 2
  have hc01 := sum_codegree_counts H vertices 0 1
  have hc02 := sum_codegree_counts H vertices 0 2
  have hc12 := sum_codegree_counts H vertices 1 2
  have hz := triple_count_zero H vertices noTriple
  rw [edges32, label_univ] at hall
  rw [d0, label_univ] at hd0
  rw [d1, label_univ] at hd1
  rw [d2, label_univ] at hd2
  rw [c01, label_univ] at hc01
  rw [c02, label_univ] at hc02
  rw [c12, label_univ] at hc12
  simp +decide only [Finset.filter_insert, Finset.filter_singleton, Finset.sum_insert,
    Finset.sum_singleton, Finset.mem_insert, Finset.mem_singleton,
    if_true, if_false] at hall hd0 hd1 hd2 hc01 hc02 hc12
  omega

/-- Canonical one-based position list associated to a label set. -/
def canonicalType (T : Finset (Fin 3)) : List ℕ :=
  (T.image fun i => i.val + 11).sort (· ≤ ·)

theorem positionType_eq (vertices : Fin 3 ↪ Fin 23) (e : Finset (Fin 23)) :
    positionType vertices threePositions e = canonicalType (lockSignature vertices e) := by
  simp only [positionType, positionSignature, threePositions, canonicalType,
    Function.Embedding.coeFn_mk, Nat.add_assoc]

theorem canonicalType_injective : Function.Injective canonicalType := by
  intro A B h
  have hs := congrArg List.toFinset h
  simp only [canonicalType, Finset.sort_toFinset] at hs
  apply Finset.image_injective (fun i j hij => Fin.ext (Nat.add_right_cancel hij)) hs

theorem position_fiber_count (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 3 ↪ Fin 23) (T : Finset (Fin 3)) :
    multiplicity H.edges (positionType vertices threePositions) (canonicalType T) =
      count H vertices T := by
  unfold multiplicity fiber count
  congr 1
  apply Finset.filter_congr
  intro e he
  rw [positionType_eq, canonicalType_injective.eq_iff]


theorem canonical_empty : canonicalType ∅ = [] := by
  have hi : (∅ : Finset (Fin 3)).image (fun i => i.val + 11) = ([] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_0 : canonicalType {0} = [11] := by
  have hi : ({0} : Finset (Fin 3)).image (fun i => i.val + 11) = ([11] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([11] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_1 : canonicalType {1} = [12] := by
  have hi : ({1} : Finset (Fin 3)).image (fun i => i.val + 11) = ([12] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([12] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_2 : canonicalType {2} = [13] := by
  have hi : ({2} : Finset (Fin 3)).image (fun i => i.val + 11) = ([13] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([13] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_01 : canonicalType {0,1} = [11,12] := by
  have hi : ({0,1} : Finset (Fin 3)).image (fun i => i.val + 11) = ([11,12] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([11,12] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_02 : canonicalType {0,2} = [11,13] := by
  have hi : ({0,2} : Finset (Fin 3)).image (fun i => i.val + 11) = ([11,13] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([11,13] : List ℕ).Nodup)).mpr (by decide)

theorem canonical_12 : canonicalType {1,2} = [12,13] := by
  have hi : ({1,2} : Finset (Fin 3)).image (fun i => i.val + 11) = ([12,13] : List ℕ).toFinset := by
    decide +kernel
  rw [canonicalType, hi]
  exact (List.toFinset_sort (· ≤ ·) (by decide : ([12,13] : List ℕ).Nodup)).mpr (by decide)

theorem canonicalType_covers (T : Finset (Fin 3)) :
    canonicalType T ∈ Numeric.v23_677.types.map Numeric.EdgeType.locks ∨ T = {0,1,2} := by
  have ht : T ∈ ({∅, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}} : Finset (Finset (Fin 3))) := by
    rw [← label_univ]
    exact Finset.mem_univ _
  simp only [Finset.mem_insert, Finset.mem_singleton] at ht
  rcases ht with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · rw [canonical_empty]; left; decide +kernel
  · rw [canonical_0]; left; decide +kernel
  · rw [canonical_1]; left; decide +kernel
  · rw [canonical_2]; left; decide +kernel
  · rw [canonical_01]; left; decide +kernel
  · rw [canonical_02]; left; decide +kernel
  · rw [canonical_12]; left; decide +kernel
  · exact Or.inr rfl


/-- The 677 table describes the actual hypergraph under the chosen embedding. -/
theorem realizes_677 (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 3 ↪ Fin 23)
    (edges32 : H.edges.card = 32)
    (d0 : H.degree (vertices 0) = 6) (d1 : H.degree (vertices 1) = 7)
    (d2 : H.degree (vertices 2) = 7)
    (c01 : H.codegree (vertices 0) (vertices 1) = 1)
    (c02 : H.codegree (vertices 0) (vertices 2) = 1)
    (c12 : H.codegree (vertices 1) (vertices 2) = 1)
    (noTriple : ∀ e ∈ H.edges, ¬ (vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e)) :
    RealizesProfile H vertices threePositions Numeric.v23_677 := by
  have counts := counts_677 H vertices edges32 d0 d1 d2 c01 c02 c12 noTriple
  refine ⟨rfl, Numeric.v23_677_valid, ?_, ?_⟩
  · decide +kernel
  · constructor
    · decide +kernel
    · intro e he
      rw [positionType_eq]
      rcases canonicalType_covers (lockSignature vertices e) with h | h
      · exact h
      · exfalso
        apply noTriple e he
        have hx : 0 ∈ lockSignature vertices e := by rw [h]; decide
        have hy : 1 ∈ lockSignature vertices e := by rw [h]; decide
        have hz : 2 ∈ lockSignature vertices e := by rw [h]; decide
        exact ⟨(mem_lockSignature _ _ _).mp hx, (mem_lockSignature _ _ _).mp hy,
          (mem_lockSignature _ _ _).mp hz⟩
    · intro t ht
      simp only [Numeric.v23_677, List.mem_cons, List.not_mem_nil, or_false] at ht
      rcases ht with rfl | rfl | rfl | rfl | rfl | rfl | rfl
      · simpa only [canonical_empty] using
          (position_fiber_count H vertices ∅).trans counts.1
      · simpa only [canonical_0] using
          (position_fiber_count H vertices {0}).trans counts.2.1
      · simpa only [canonical_1] using
          (position_fiber_count H vertices {1}).trans counts.2.2.1
      · simpa only [canonical_2] using
          (position_fiber_count H vertices {2}).trans counts.2.2.2.1
      · simpa only [canonical_01] using
          (position_fiber_count H vertices {0,1}).trans counts.2.2.2.2.1
      · simpa only [canonical_02] using
          (position_fiber_count H vertices {0,2}).trans counts.2.2.2.2.2.1
      · simpa only [canonical_12] using
          (position_fiber_count H vertices {1,2}).trans counts.2.2.2.2.2.2.1

/-- Direct interface for the three actual vertices selected by LowDegree. -/
theorem realizes_677_of_vertices (H : Simple5Hypergraph (Fin 23))
    (edges32 : H.edges.card = 32) (x y z : Fin 23)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (dx : H.degree x = 6) (dy : H.degree y = 7) (dz : H.degree z = 7)
    (cxy : H.codegree x y = 1) (cxz : H.codegree x z = 1) (cyz : H.codegree y z = 1)
    (noTriple : ∀ e ∈ H.edges, ¬ (x ∈ e ∧ y ∈ e ∧ z ∈ e)) :
    RealizesProfile H (threeVertices x y z hxy hxz hyz) threePositions Numeric.v23_677 := by
  apply realizes_677 H _ edges32
  · exact dx
  · exact dy
  · exact dz
  · exact cxy
  · exact cxz
  · exact cyz
  · exact noTriple

end Aris4Math.TripleLockProfiles

#print axioms Aris4Math.TripleLockProfiles.counts_677
#print axioms Aris4Math.TripleLockProfiles.position_fiber_count

#print axioms Aris4Math.TripleLockProfiles.realizes_677
#print axioms Aris4Math.TripleLockProfiles.realizes_677_of_vertices

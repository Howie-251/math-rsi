import Aris4Math.ThirtyThree.OrdinaryLink
import Aris4Math.TypeCounting

/-! Actual pure-singleton link families for any finite number of locks. -/
namespace Aris4Math.ThirtyThree.PureLink

open scoped BigOperators
open Aris4Math.LinkCounting Aris4Math.LinkDeletion Aris4Math.TypeCounting

variable {v s : ℕ}

def pureEdges (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) : Finset (Finset (Fin v)) :=
  H.edges.filter fun e => lockSignature vertices e = {j}

def freeVertices (vertices : Fin s ↪ Fin v) : Finset (Fin v) :=
  Finset.univ \ (Finset.univ.image vertices)

theorem freeVertices_card (vertices : Fin s ↪ Fin v) :
    (freeVertices vertices).card = v-s := by
  rw [freeVertices,Finset.card_sdiff_of_subset (Finset.subset_univ _),
    Finset.card_image_of_injective _ vertices.injective]
  simp

theorem pure_center_mem (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) (e : Finset (Fin v)) (he : e ∈ pureEdges H vertices j) : vertices j ∈ e := by
  apply (mem_lockSignature vertices e j).mp
  rw [(Finset.mem_filter.mp he).2]
  simp

theorem pureEdges_subset (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) : pureEdges H vertices j ⊆ H.incidentEdges (vertices j) := by
  intro e he
  exact Finset.mem_filter.mpr ⟨(Finset.mem_filter.mp he).1,pure_center_mem H vertices j e he⟩

theorem pure_free_filter (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) (e : Finset (Fin v)) (he : e ∈ pureEdges H vertices j) :
    (freeVertices vertices).filter (fun z => z ∈ e) = e.erase (vertices j) := by
  ext z
  simp only [freeVertices,Finset.mem_filter,Finset.mem_sdiff,Finset.mem_univ,true_and,
    Finset.mem_erase]
  constructor
  · rintro ⟨hz,he⟩
    refine ⟨?_,he⟩
    rintro rfl
    exact hz (Finset.mem_image.mpr ⟨j,Finset.mem_univ _,rfl⟩)
  · rintro ⟨hne,hze⟩
    refine ⟨?_,hze⟩
    intro hz
    obtain ⟨l,_,hl⟩ := Finset.mem_image.mp hz
    have hle : l ∈ lockSignature vertices e := (mem_lockSignature _ _ _).mpr (by rw [hl]; exact hze)
    rw [(Finset.mem_filter.mp he).2,Finset.mem_singleton] at hle
    exact hne (hl.symm.trans (congrArg vertices hle))

def pureBadPairs (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) : Finset (Finset (Finset (Fin v))) :=
  (H.badLinkPairs (vertices j)).filter fun p => p ⊆ pureEdges H vertices j

theorem pureBadPairs_eq (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) : pureBadPairs H vertices j =
      ((pureEdges H vertices j).powersetCard 2).filter fun p =>
        (commonWithin (Finset.univ.erase (vertices j)) p).Nonempty := by
  ext p
  simp only [pureBadPairs,Simple5Hypergraph.badLinkPairs,Finset.mem_filter,Finset.mem_powersetCard]
  constructor
  · rintro ⟨⟨⟨_,hc⟩,hn⟩,hs⟩
    exact ⟨⟨hs,hc⟩,hn⟩
  · rintro ⟨⟨hs,hc⟩,hn⟩
    exact ⟨⟨⟨hs.trans (pureEdges_subset H vertices j),hc⟩,hn⟩,hs⟩

theorem pure_incidence_sum (H : Simple5Hypergraph (Fin v)) (vertices : Fin s ↪ Fin v)
    (j : Fin s) :
    (∑ z ∈ freeVertices vertices, ((pureEdges H vertices j).filter fun e => z ∈ e).card) =
      4*(pureEdges H vertices j).card := by
  simp only [Finset.card_eq_sum_ones,Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    _ = ∑ _e ∈ pureEdges H vertices j, 4 := by
      apply Finset.sum_congr rfl
      intro e he
      rw [Finset.sum_boole,pure_free_filter H vertices j e he,
        Finset.card_erase_of_mem (pure_center_mem H vertices j e he),
        H.five_uniform e (Finset.mem_filter.mp he).1]
      norm_num
    _ = _ := by simp [Nat.mul_comm]

theorem pure_intersection_upper (H : Simple5Hypergraph (Fin v))
    (vertices : Fin s ↪ Fin v) (j : Fin s) :
    (∑ p ∈ (pureEdges H vertices j).powersetCard 2,
      (commonWithin (Finset.univ.erase (vertices j)) p).card) ≤
        3*(pureBadPairs H vertices j).card := by
  calc
    _ ≤ ∑ p ∈ (pureEdges H vertices j).powersetCard 2,
        if (commonWithin (Finset.univ.erase (vertices j)) p).Nonempty then 3 else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      split_ifs with hn
      · apply H.link_pair_intersection_le_three (vertices j) p
        obtain ⟨hs,hc⟩ := Finset.mem_powersetCard.mp hp
        exact Finset.mem_powersetCard.mpr ⟨hs.trans (pureEdges_subset H vertices j),hc⟩
      · simp [Finset.not_nonempty_iff_eq_empty.mp hn]
    _ = _ := by
      rw [← Finset.sum_filter,← pureBadPairs_eq]
      simp [Nat.mul_comm]

/-- Pure link incidence on exactly the free vertices. All pairs counted here
are a literal subfamily of the original bad-link pairs. -/
theorem pure_bad_pair_budget (H : Simple5Hypergraph (Fin v))
    (vertices : Fin s ↪ Fin v) (j : Fin s) :
    4*(pureEdges H vertices j).card ≤ 3*(pureBadPairs H vertices j).card + (v-s) := by
  classical
  have lower := Finset.sum_le_sum (s := freeVertices vertices) (fun z _ =>
    show ((pureEdges H vertices j).filter fun e => z ∈ e).card ≤
      (((pureEdges H vertices j).filter fun e => z ∈ e).card.choose 2) + 1 by
        have h := pred_le_choose_two (((pureEdges H vertices j).filter fun e => z ∈ e).card)
        omega)
  rw [Finset.sum_add_distrib] at lower
  simp only [Finset.sum_const,nsmul_eq_mul,Nat.cast_id,mul_one] at lower
  rw [pure_incidence_sum,← sum_common_card,freeVertices_card] at lower
  have compare :
      (∑ p ∈ (pureEdges H vertices j).powersetCard 2, (commonWithin (freeVertices vertices) p).card) ≤
      ∑ p ∈ (pureEdges H vertices j).powersetCard 2,
        (commonWithin (Finset.univ.erase (vertices j)) p).card := by
    apply Finset.sum_le_sum
    intro p _
    apply Finset.card_le_card
    intro z hz
    have hzdata : z ∈ freeVertices vertices ∧ ∀ e ∈ p, z ∈ e := by
      simpa only [commonWithin,Finset.mem_filter] using hz
    have hne : z ≠ vertices j := by
      rintro rfl
      exact (Finset.mem_sdiff.mp hzdata.1).2 (Finset.mem_image.mpr ⟨j,Finset.mem_univ _,rfl⟩)
    simpa only [commonWithin,Finset.mem_filter] using
      And.intro (Finset.mem_erase.mpr ⟨hne,Finset.mem_univ z⟩) hzdata.2
  have upper := pure_intersection_upper H vertices j
  omega

theorem pure_bad_pair_lower (H : Simple5Hypergraph (Fin v))
    (vertices : Fin s ↪ Fin v) (j : Fin s) :
    (4*(pureEdges H vertices j).card + 2 - (v-s))/3 ≤ (pureBadPairs H vertices j).card := by
  have h := pure_bad_pair_budget H vertices j
  omega

/-- An actual edge is pure at a lock iff its canonical positional type is the
singleton consisting of that lock's one-based position. -/
theorem pure_iff_type (vertices positions : Fin s ↪ Fin v) (j : Fin s)
    (e : Finset (Fin v)) : lockSignature vertices e = {j} ↔
      positionType vertices positions e = [(positions j).val+1] := by
  constructor
  · intro h
    simp [positionType,positionSignature,h]
  · intro h
    have hf : Function.Injective (fun i => (positions i).val+1) := by
      intro i l hi
      exact positions.injective (Fin.ext (Nat.add_right_cancel hi))
    apply Finset.image_injective hf
    have hs := congrArg List.toFinset h
    simpa only [positionType,positionSignature,Finset.sort_toFinset,List.toFinset_cons,
      List.toFinset_nil,Finset.image_singleton] using hs

theorem pure_card_multiplicity (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin s ↪ Fin v) (j : Fin s) :
    (pureEdges H vertices j).card =
      multiplicity H.edges (positionType vertices positions) [(positions j).val+1] := by
  unfold pureEdges multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  exact pure_iff_type vertices positions j e

end Aris4Math.ThirtyThree.PureLink

#print axioms Aris4Math.ThirtyThree.PureLink.pure_bad_pair_lower
#print axioms Aris4Math.ThirtyThree.PureLink.pure_card_multiplicity

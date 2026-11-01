import Aris4Math.ThirtyThree.OrdinaryLink
import Aris4Math.TypeCounting

/-! Bad-pair quotas for actual edge families avoiding an arbitrary set of
vertices. The center is the only removed vertex that belongs to these edges. -/
namespace Aris4Math.ThirtyThree.AvoidedLink

open scoped BigOperators
open Aris4Math.LinkCounting Aris4Math.LinkDeletion Aris4Math.TypeCounting

variable {V : Type*} [Fintype V] [DecidableEq V]

def avoidedEdges (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    Finset (Finset V) :=
  (H.incidentEdges x).filter fun e => Disjoint e R

omit [Fintype V] in
theorem mem_avoidedEdges (H : Simple5Hypergraph V) (x : V) (R : Finset V)
    (e : Finset V) :
    e ∈ avoidedEdges H x R ↔ e ∈ H.edges ∧ x ∈ e ∧ Disjoint e R := by
  simp [avoidedEdges, Simple5Hypergraph.incidentEdges, and_assoc]

omit [Fintype V] in
theorem avoidedEdges_subset (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    avoidedEdges H x R ⊆ H.incidentEdges x := Finset.filter_subset _ _

def availableVertices (x : V) (R : Finset V) : Finset V :=
  Finset.univ \ insert x R

theorem availableVertices_card (x : V) (R : Finset V) (hx : x ∉ R) :
    (availableVertices x R).card = Fintype.card V - 1 - R.card := by
  rw [availableVertices, Finset.card_sdiff_of_subset (Finset.subset_univ _),
    Finset.card_insert_of_notMem hx]
  simp only [Finset.card_univ]
  omega

def avoidedBadPairs (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    Finset (Finset (Finset V)) :=
  (H.badLinkPairs x).filter fun p => p ⊆ avoidedEdges H x R

theorem avoidedBadPairs_eq (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    avoidedBadPairs H x R =
      ((avoidedEdges H x R).powersetCard 2).filter fun p =>
        (commonWithin (Finset.univ.erase x) p).Nonempty := by
  ext p
  simp only [avoidedBadPairs, Simple5Hypergraph.badLinkPairs, Finset.mem_filter,
    Finset.mem_powersetCard]
  constructor
  · rintro ⟨⟨⟨_, hc⟩, hn⟩, hs⟩
    exact ⟨⟨hs, hc⟩, hn⟩
  · rintro ⟨⟨hs, hc⟩, hn⟩
    exact ⟨⟨⟨hs.trans (avoidedEdges_subset H x R), hc⟩, hn⟩, hs⟩

theorem available_filter (H : Simple5Hypergraph V) (x : V) (R : Finset V)
    (e : Finset V) (he : e ∈ avoidedEdges H x R) :
    (availableVertices x R).filter (fun z => z ∈ e) = e.erase x := by
  obtain ⟨_, _, hdisj⟩ := (mem_avoidedEdges H x R e).mp he
  ext z
  simp only [availableVertices, Finset.mem_filter, Finset.mem_sdiff,
    Finset.mem_univ, true_and, Finset.mem_insert, not_or, Finset.mem_erase]
  constructor
  · rintro ⟨⟨hne, _⟩, hz⟩
    exact ⟨hne, hz⟩
  · rintro ⟨hne, hz⟩
    exact ⟨⟨hne, fun hR => Finset.disjoint_left.mp hdisj hz hR⟩, hz⟩

theorem avoided_incidence_sum (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    (∑ z ∈ availableVertices x R, ((avoidedEdges H x R).filter fun e => z ∈ e).card) =
      4 * (avoidedEdges H x R).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    _ = ∑ _e ∈ avoidedEdges H x R, 4 := by
      apply Finset.sum_congr rfl
      intro e he
      obtain ⟨heH, hxe, _⟩ := (mem_avoidedEdges H x R e).mp he
      rw [Finset.sum_boole, available_filter H x R e he,
        Finset.card_erase_of_mem hxe, H.five_uniform e heH]
      norm_num
    _ = _ := by simp [Nat.mul_comm]

theorem avoided_intersection_upper (H : Simple5Hypergraph V) (x : V) (R : Finset V) :
    (∑ p ∈ (avoidedEdges H x R).powersetCard 2,
      (commonWithin (Finset.univ.erase x) p).card) ≤
        3 * (avoidedBadPairs H x R).card := by
  calc
    _ ≤ ∑ p ∈ (avoidedEdges H x R).powersetCard 2,
        if (commonWithin (Finset.univ.erase x) p).Nonempty then 3 else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      split_ifs with hn
      · apply H.link_pair_intersection_le_three x p
        obtain ⟨hs, hc⟩ := Finset.mem_powersetCard.mp hp
        exact Finset.mem_powersetCard.mpr ⟨hs.trans (avoidedEdges_subset H x R), hc⟩
      · simp [Finset.not_nonempty_iff_eq_empty.mp hn]
    _ = _ := by
      rw [← Finset.sum_filter, ← avoidedBadPairs_eq]
      simp [Nat.mul_comm]

/-- All pairs here are a filtered subfamily of the original deletion set.
No pair-covering assumption is needed. -/
theorem avoided_bad_pair_budget (H : Simple5Hypergraph V) (x : V) (R : Finset V)
    (hx : x ∉ R) :
    4 * (avoidedEdges H x R).card ≤
      3 * (avoidedBadPairs H x R).card + (Fintype.card V - 1 - R.card) := by
  have lower := Finset.sum_le_sum (s := availableVertices x R) (fun z _ =>
    show ((avoidedEdges H x R).filter fun e => z ∈ e).card ≤
      (((avoidedEdges H x R).filter fun e => z ∈ e).card.choose 2) + 1 by
        have h := pred_le_choose_two (((avoidedEdges H x R).filter fun e => z ∈ e).card)
        omega)
  rw [Finset.sum_add_distrib] at lower
  simp only [Finset.sum_const, nsmul_eq_mul, Nat.cast_id, mul_one] at lower
  rw [avoided_incidence_sum, ← sum_common_card, availableVertices_card x R hx] at lower
  have compare :
      (∑ p ∈ (avoidedEdges H x R).powersetCard 2,
        (commonWithin (availableVertices x R) p).card) ≤
      ∑ p ∈ (avoidedEdges H x R).powersetCard 2,
        (commonWithin (Finset.univ.erase x) p).card := by
    apply Finset.sum_le_sum
    intro p _
    apply Finset.card_le_card
    intro z hz
    have hzdata : z ∈ availableVertices x R ∧ ∀ e ∈ p, z ∈ e := by
      simpa only [commonWithin, Finset.mem_filter] using hz
    have hne : z ≠ x := fun h => (Finset.mem_sdiff.mp hzdata.1).2
      (Finset.mem_insert.mpr (Or.inl h))
    simpa only [commonWithin, Finset.mem_filter] using
      And.intro (Finset.mem_erase.mpr ⟨hne, Finset.mem_univ z⟩) hzdata.2
  have upper := avoided_intersection_upper H x R
  omega

theorem avoided_bad_pair_lower (H : Simple5Hypergraph V) (x : V) (R : Finset V)
    (hx : x ∉ R) :
    (4 * (avoidedEdges H x R).card + 2 - (Fintype.card V - 1 - R.card)) / 3 ≤
      (avoidedBadPairs H x R).card := by
  have h := avoided_bad_pair_budget H x R hx
  omega

end Aris4Math.ThirtyThree.AvoidedLink

#print axioms Aris4Math.ThirtyThree.AvoidedLink.avoided_bad_pair_lower

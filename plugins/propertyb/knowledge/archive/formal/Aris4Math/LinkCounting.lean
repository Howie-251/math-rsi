import Aris4Math.Structure
import Mathlib.Data.Finset.Powerset

open scoped BigOperators

namespace Aris4Math.LinkCounting

variable {V : Type*} [DecidableEq V]

/-- The vertices of W common to every edge in the finite family p. -/
def commonWithin (W : Finset V) (p : Finset (Finset V)) : Finset V :=
  W.filter fun y => ∀ e ∈ p, y ∈ e

theorem pair_filter (F : Finset (Finset V)) (y : V) :
    (F.powersetCard 2).filter (fun p => ∀ e ∈ p, y ∈ e) =
      (F.filter fun e => y ∈ e).powersetCard 2 := by
  ext p
  simp only [Finset.mem_filter, Finset.mem_powersetCard]
  constructor
  · rintro ⟨⟨hsub, hc⟩, hall⟩
    exact ⟨fun e he => Finset.mem_filter.mpr ⟨hsub he, hall e he⟩, hc⟩
  · rintro ⟨hsub, hc⟩
    exact ⟨⟨fun e he => (Finset.mem_filter.mp (hsub he)).1, hc⟩,
      fun e he => (Finset.mem_filter.mp (hsub he)).2⟩

/-- Double counting actual unordered edge pairs and their common vertices. -/
theorem sum_common_card (F : Finset (Finset V)) (W : Finset V) :
    (∑ p ∈ F.powersetCard 2, (commonWithin W p).card) =
      ∑ y ∈ W, ((F.filter fun e => y ∈ e).card.choose 2) := by
  simp only [commonWithin, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro y _
  rw [← Finset.sum_filter, ← Finset.card_eq_sum_ones, pair_filter,
    Finset.card_powersetCard]
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]

theorem pred_le_choose_two (n : Nat) : n - 1 ≤ n.choose 2 := by
  cases n with
  | zero => simp
  | succ n =>
      rw [Nat.choose_succ_succ]
      simp

end Aris4Math.LinkCounting

namespace Aris4Math.Simple5Hypergraph

variable {V : Type*} [Fintype V] [DecidableEq V]

def incidentEdges (H : Simple5Hypergraph V) (x : V) : Finset (Finset V) :=
  H.edges.filter fun e => x ∈ e

/-- Distinct unordered pairs of edges through x with another common point. -/
def badLinkPairs (H : Simple5Hypergraph V) (x : V) : Finset (Finset (Finset V)) :=
  ((H.incidentEdges x).powersetCard 2).filter fun p =>
    (LinkCounting.commonWithin (Finset.univ.erase x) p).Nonempty

theorem link_intersection_sum (H : Simple5Hypergraph V) (x : V) :
    (∑ p ∈ (H.incidentEdges x).powersetCard 2,
      (LinkCounting.commonWithin (Finset.univ.erase x) p).card) =
      ∑ y ∈ Finset.univ.erase x, (H.codegree x y).choose 2 := by
  rw [LinkCounting.sum_common_card]
  apply Finset.sum_congr rfl
  intro y _
  congr 2
  ext e
  simp [incidentEdges, and_assoc]

theorem link_excess_le_intersection_sum (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (x : V) :
    4 * H.degree x - (Fintype.card V - 1) ≤
      ∑ p ∈ (H.incidentEdges x).powersetCard 2,
        (LinkCounting.commonWithin (Finset.univ.erase x) p).card := by
  rw [H.link_intersection_sum, ← H.sum_codegree_excess cover x]
  exact Finset.sum_le_sum fun y _ => LinkCounting.pred_le_choose_two (H.codegree x y)

omit [Fintype V] in
/-- Distinct actual five-element edges share at most four vertices. -/
theorem distinct_edge_inter_card_le_four (H : Simple5Hypergraph V)
    {e f : Finset V} (he : e ∈ H.edges) (hf : f ∈ H.edges) (hne : e ≠ f) :
    (e ∩ f).card ≤ 4 := by
  have ce := H.five_uniform e he
  have cf := H.five_uniform f hf
  have hi := Finset.card_le_card (Finset.inter_subset_left (s₁ := e) (s₂ := f))
  by_contra hlarge
  have ci : (e ∩ f).card = 5 := by omega
  have hie : e ∩ f = e :=
    Finset.eq_of_subset_of_card_le Finset.inter_subset_left (by omega)
  have hef : e ⊆ f := by
    rw [← hie]
    exact Finset.inter_subset_right
  exact hne (Finset.eq_of_subset_of_card_le hef (by omega))

/-- A distinct pair of incident edges shares at most three other vertices. -/
theorem link_pair_intersection_le_three (H : Simple5Hypergraph V) (x : V)
    (p : Finset (Finset V)) (hp : p ∈ (H.incidentEdges x).powersetCard 2) :
    (LinkCounting.commonWithin (Finset.univ.erase x) p).card ≤ 3 := by
  obtain ⟨hsub, hc⟩ := Finset.mem_powersetCard.mp hp
  obtain ⟨e, f, hne, rfl⟩ := Finset.card_eq_two.mp hc
  have he := Finset.mem_filter.mp (hsub (Finset.mem_insert_self _ _))
  have hf := Finset.mem_filter.mp
    (hsub (Finset.mem_insert_of_mem (Finset.mem_singleton_self f)))
  have hcommon : LinkCounting.commonWithin (Finset.univ.erase x) {e, f} =
      (e ∩ f).erase x := by
    ext y
    simp [LinkCounting.commonWithin]
  rw [hcommon, Finset.card_erase_of_mem (Finset.mem_inter.mpr ⟨he.2, hf.2⟩)]
  have bound := H.distinct_edge_inter_card_le_four he.1 hf.1 hne
  omega

/-- The total link intersection incidence is at most three per actual bad
unordered pair. Zero-intersection pairs contribute zero. -/
theorem link_intersection_sum_le (H : Simple5Hypergraph V) (x : V) :
    (∑ p ∈ (H.incidentEdges x).powersetCard 2,
      (LinkCounting.commonWithin (Finset.univ.erase x) p).card) ≤
      3 * (H.badLinkPairs x).card := by
  calc
    _ ≤ ∑ p ∈ (H.incidentEdges x).powersetCard 2,
        if (LinkCounting.commonWithin (Finset.univ.erase x) p).Nonempty then 3 else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      split_ifs with hn
      · exact H.link_pair_intersection_le_three x p hp
      · simp [Finset.not_nonempty_iff_eq_empty.mp hn]
    _ = 3 * (H.badLinkPairs x).card := by
      rw [← Finset.sum_filter]
      simp [badLinkPairs, Nat.mul_comm]

/-- P8 for the actual hypergraph, with distinct unordered edge pairs. -/
theorem link_bad_pair_lower_bound (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (x : V) :
    (4 * H.degree x - (Fintype.card V - 1) + 2) / 3 ≤
      (H.badLinkPairs x).card := by
  have lower := H.link_excess_le_intersection_sum cover x
  have upper := H.link_intersection_sum_le x
  omega

end Aris4Math.Simple5Hypergraph

#print axioms Aris4Math.Simple5Hypergraph.link_bad_pair_lower_bound

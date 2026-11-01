import Aris4Math.LinkDeletion

/-!
# Ordinary link pairs after deleting the unique two-lock edge

The finite families here contain actual edges of H. Their unordered pairs are
literally a subset of the existing bad-link pairs used by `LinkDeletion`.
No pair-covering hypothesis is needed for the ordinary-link incidence bound.
-/

namespace Aris4Math.ThirtyThree.OrdinaryLink

open scoped BigOperators
open Aris4Math.LinkCounting Aris4Math.LinkDeletion

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Edges through x that avoid the other lock y. -/
def ordinaryEdges (H : Simple5Hypergraph V) (x y : V) : Finset (Finset V) :=
  (H.incidentEdges x).filter fun e => y ∉ e

omit [Fintype V] in
theorem mem_ordinaryEdges (H : Simple5Hypergraph V) (x y : V) (e : Finset V) :
    e ∈ ordinaryEdges H x y ↔ e ∈ H.edges ∧ x ∈ e ∧ y ∉ e := by
  simp [ordinaryEdges, Simple5Hypergraph.incidentEdges, and_assoc]

omit [Fintype V] in
theorem ordinaryEdges_subset (H : Simple5Hypergraph V) (x y : V) :
    ordinaryEdges H x y ⊆ H.incidentEdges x := Finset.filter_subset _ _

/-- Actual ordinary-ordinary unordered bad pairs. -/
def ordinaryBadPairs (H : Simple5Hypergraph V) (x y : V) :
    Finset (Finset (Finset V)) :=
  ((ordinaryEdges H x y).powersetCard 2).filter fun p =>
    (commonWithin (Finset.univ.erase x) p).Nonempty

/-- This is exactly a filtered subfamily of the bad pairs already used for
deletion; there is no newly invented count detached from actual H. -/
theorem ordinaryBadPairs_eq_filter (H : Simple5Hypergraph V) (x y : V) :
    ordinaryBadPairs H x y =
      (H.badLinkPairs x).filter fun p => p ⊆ ordinaryEdges H x y := by
  ext p
  simp only [ordinaryBadPairs, Simple5Hypergraph.badLinkPairs,
    Finset.mem_filter, Finset.mem_powersetCard]
  constructor
  · rintro ⟨⟨hsub, hc⟩, hn⟩
    exact ⟨⟨⟨hsub.trans (ordinaryEdges_subset H x y), hc⟩, hn⟩, hsub⟩
  · rintro ⟨⟨⟨_, hc⟩, hn⟩, hsub⟩
    exact ⟨⟨hsub, hc⟩, hn⟩

theorem ordinaryBadPairs_subset (H : Simple5Hypergraph V) (x y : V) :
    ordinaryBadPairs H x y ⊆ H.badLinkPairs x := by
  rw [ordinaryBadPairs_eq_filter]
  exact Finset.filter_subset _ _

omit [Fintype V] in
/-- The ordinary edge count removes precisely the actual codegree. -/
theorem ordinaryEdges_card_add_codegree (H : Simple5Hypergraph V) (x y : V) :
    (ordinaryEdges H x y).card + H.codegree x y = H.degree x := by
  have h := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.incidentEdges x) (fun e => y ∈ e)
  have hboth : (H.incidentEdges x).filter (fun e => y ∈ e) =
      H.edges.filter (fun e => x ∈ e ∧ y ∈ e) := by
    ext e
    simp [Simple5Hypergraph.incidentEdges, and_assoc]
  rw [hboth] at h
  change H.codegree x y + (ordinaryEdges H x y).card = H.degree x at h
  omega

omit [Fintype V] in
theorem ordinaryEdges_card (H : Simple5Hypergraph V) (x y : V)
    (one : H.codegree x y = 1) :
    (ordinaryEdges H x y).card = H.degree x - 1 := by
  have h := ordinaryEdges_card_add_codegree H x y
  omega

/-- Each ordinary edge contributes four incidences outside the two locks. -/
theorem ordinary_incidence_sum (H : Simple5Hypergraph V) (x y : V) :
    (∑ z ∈ (Finset.univ.erase x).erase y,
      ((ordinaryEdges H x y).filter fun e => z ∈ e).card) =
      4 * (ordinaryEdges H x y).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    _ = ∑ _e ∈ ordinaryEdges H x y, 4 := by
      apply Finset.sum_congr rfl
      intro e he
      rw [Finset.sum_boole]
      obtain ⟨heH, hxe, hye⟩ := (mem_ordinaryEdges H x y e).mp he
      have hfilter : (((Finset.univ : Finset V).erase x).erase y).filter
          (fun z => z ∈ e) = e.erase x := by
        ext z
        simp only [Finset.mem_filter, Finset.mem_erase, Finset.mem_univ, and_true]
        constructor
        · rintro ⟨⟨_, hzx⟩, hze⟩
          exact ⟨hzx, hze⟩
        · rintro ⟨hzx, hze⟩
          exact ⟨⟨fun hzy => hye (hzy ▸ hze), hzx⟩, hze⟩
      rw [hfilter, Finset.card_erase_of_mem hxe, H.five_uniform e heH]
      norm_num
    _ = _ := by simp [Nat.mul_comm]

/-- No ordinary pair contributes more than three common noncenter vertices. -/
theorem ordinary_intersection_sum_le (H : Simple5Hypergraph V) (x y : V) :
    (∑ p ∈ (ordinaryEdges H x y).powersetCard 2,
      (commonWithin (Finset.univ.erase x) p).card) ≤
      3 * (ordinaryBadPairs H x y).card := by
  calc
    _ ≤ ∑ p ∈ (ordinaryEdges H x y).powersetCard 2,
        if (commonWithin (Finset.univ.erase x) p).Nonempty then 3 else 0 := by
      apply Finset.sum_le_sum
      intro p hp
      split_ifs with hn
      · apply H.link_pair_intersection_le_three x p
        obtain ⟨hsub, hc⟩ := Finset.mem_powersetCard.mp hp
        exact Finset.mem_powersetCard.mpr
          ⟨hsub.trans (ordinaryEdges_subset H x y), hc⟩
      · simp [Finset.not_nonempty_iff_eq_empty.mp hn]
    _ = _ := by
      rw [← Finset.sum_filter]
      simp [ordinaryBadPairs, Nat.mul_comm]

/-- Incidence excess on V minus the two locks is supplied by actual ordinary
bad pairs. Zero-incidence vertices cause no difficulty: n ≤ choose(n,2)+1
holds even at n=0. No coverage or edge-count hypothesis is used. -/
theorem ordinary_bad_pair_budget (H : Simple5Hypergraph V) (x y : V)
    (hne : x ≠ y) :
    4 * (ordinaryEdges H x y).card ≤
      3 * (ordinaryBadPairs H x y).card + (Fintype.card V - 2) := by
  let W := ((Finset.univ : Finset V).erase x).erase y
  have Wcard : W.card = Fintype.card V - 2 := by
    have hy : y ∈ (Finset.univ : Finset V).erase x :=
      Finset.mem_erase.mpr ⟨hne.symm, Finset.mem_univ y⟩
    simp [W, Finset.card_erase_of_mem hy, Nat.sub_sub]
  have scalar (n : ℕ) : n ≤ n.choose 2 + 1 := by
    have h := pred_le_choose_two n
    omega
  have lower := Finset.sum_le_sum (s := W) (fun z _ =>
    scalar (((ordinaryEdges H x y).filter fun e => z ∈ e).card))
  rw [Finset.sum_add_distrib] at lower
  simp only [Finset.sum_const, nsmul_eq_mul, Nat.cast_id, mul_one] at lower
  rw [ordinary_incidence_sum H x y, ← sum_common_card, Wcard] at lower
  have compare :
      (∑ p ∈ (ordinaryEdges H x y).powersetCard 2, (commonWithin W p).card) ≤
      ∑ p ∈ (ordinaryEdges H x y).powersetCard 2,
        (commonWithin (Finset.univ.erase x) p).card := by
    apply Finset.sum_le_sum
    intro p _
    apply Finset.card_le_card
    intro z hz
    have hzdata : z ∈ W ∧ ∀ e ∈ p, z ∈ e := by
      simpa only [commonWithin, Finset.mem_filter] using hz
    simpa only [commonWithin, Finset.mem_filter] using
      And.intro (Finset.mem_of_mem_erase hzdata.1) hzdata.2
  have upper := ordinary_intersection_sum_le H x y
  omega

/-- The unique two-lock edge leaves exactly degree(x)-1 ordinary edges. -/
theorem ordinary_bad_pair_budget_of_codegree_one (H : Simple5Hypergraph V)
    (x y : V) (hne : x ≠ y) (one : H.codegree x y = 1) :
    4 * (H.degree x - 1) ≤
      3 * (ordinaryBadPairs H x y).card + (Fintype.card V - 2) := by
  rw [← ordinaryEdges_card H x y one]
  exact ordinary_bad_pair_budget H x y hne

/-- The new count used for the (8,8) configuration on twenty vertices. -/
theorem four_le_ordinary_bad_pairs_of_twenty (H : Simple5Hypergraph V)
    (x y : V) (hne : x ≠ y) (one : H.codegree x y = 1)
    (vertices20 : Fintype.card V = 20) (degree8 : H.degree x = 8) :
    4 ≤ (ordinaryBadPairs H x y).card := by
  have h := ordinary_bad_pair_budget_of_codegree_one H x y hne one
  rw [vertices20, degree8] at h
  omega

/-- Count all actual bad pairs at a base weight c, and count the ordinary
subfamily's extra a-c once. The ordinary weight already includes both ordered
directions. This avoids double deletion of the same pair. -/
theorem enhanced_bad_weight_lower (H : Simple5Hypergraph V) (x y : V)
    (w : Finset V × Finset V → ℚ) (q r : ℕ) (c a : ℚ)
    (hq : q ≤ (H.badLinkPairs x).card)
    (hr : r ≤ (ordinaryBadPairs H x y).card)
    (hc : 0 ≤ c) (hca : c ≤ a)
    (base : ∀ p ∈ H.badLinkPairs x, c ≤ unorderedWeight w p)
    (ordinary : ∀ p ∈ ordinaryBadPairs H x y, a ≤ unorderedWeight w p) :
    (q : ℚ) * c + (r : ℚ) * (a - c) ≤
      ∑ p ∈ H.badLinkPairs x, unorderedWeight w p := by
  have filter : (H.badLinkPairs x).filter (fun p => p ∈ ordinaryBadPairs H x y) =
      ordinaryBadPairs H x y := by
    rw [Finset.filter_mem_eq_inter]
    exact Finset.inter_eq_right.mpr (ordinaryBadPairs_subset H x y)
  have each (p : Finset (Finset V)) (hp : p ∈ H.badLinkPairs x) :
      c + (if p ∈ ordinaryBadPairs H x y then a - c else 0) ≤ unorderedWeight w p := by
    split_ifs with ho
    · have h := ordinary p ho
      linarith
    · simpa using base p hp
  have sum_bound := Finset.sum_le_sum each
  rw [Finset.sum_add_distrib, ← Finset.sum_filter, filter] at sum_bound
  simp only [Finset.sum_const, nsmul_eq_mul] at sum_bound
  have qbound : (q : ℚ) * c ≤ ((H.badLinkPairs x).card : ℚ) * c :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hq) hc
  have rbound : (r : ℚ) * (a - c) ≤
      ((ordinaryBadPairs H x y).card : ℚ) * (a - c) :=
    mul_le_mul_of_nonneg_right (by exact_mod_cast hr) (sub_nonneg.mpr hca)
  linarith

/-- The same verified lower bound on the existing directed deletion set. -/
theorem enhanced_directed_bad_weight_lower (H : Simple5Hypergraph V) (x y : V)
    (w : Finset V × Finset V → ℚ) (q r : ℕ) (c a : ℚ)
    (hq : q ≤ (H.badLinkPairs x).card)
    (hr : r ≤ (ordinaryBadPairs H x y).card)
    (hc : 0 ≤ c) (hca : c ≤ a)
    (base : ∀ p ∈ H.badLinkPairs x, c ≤ unorderedWeight w p)
    (ordinary : ∀ p ∈ ordinaryBadPairs H x y, a ≤ unorderedWeight w p) :
    (q : ℚ) * c + (r : ℚ) * (a - c) ≤
      ∑ d ∈ directedBadPairs H x, w d := by
  rw [directed_bad_sum]
  exact enhanced_bad_weight_lower H x y w q r c a hq hr hc hca base ordinary

/-- The concrete (8,8) caller derives both counts from H. Only the actual
weight inequalities remain for the conditional-permutation type calculation. -/
theorem weight_lower_of_twenty_degree_eight (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (x y : V) (hne : x ≠ y)
    (one : H.codegree x y = 1) (vertices20 : Fintype.card V = 20)
    (degree8 : H.degree x = 8) (w : Finset V × Finset V → ℚ)
    (base : ∀ p ∈ H.badLinkPairs x, (21 / 2210 : ℚ) ≤ unorderedWeight w p)
    (ordinary : ∀ p ∈ ordinaryBadPairs H x y,
      (126 / 12155 : ℚ) ≤ unorderedWeight w p) :
    (1239 / 24310 : ℚ) ≤ ∑ p ∈ H.badLinkPairs x, unorderedWeight w p := by
  have hq : 5 ≤ (H.badLinkPairs x).card := by
    have h := H.link_bad_pair_lower_bound cover x
    simpa [vertices20, degree8] using h
  have hr := four_le_ordinary_bad_pairs_of_twenty H x y hne one vertices20 degree8
  have h := enhanced_bad_weight_lower H x y w 5 4 (21 / 2210) (126 / 12155)
    hq hr (by norm_num) (by norm_num) base ordinary
  norm_num at h ⊢
  exact h

end Aris4Math.ThirtyThree.OrdinaryLink

#print axioms Aris4Math.ThirtyThree.OrdinaryLink.ordinaryBadPairs_eq_filter
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.ordinary_bad_pair_budget_of_codegree_one
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.four_le_ordinary_bad_pairs_of_twenty
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.enhanced_bad_weight_lower
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.enhanced_directed_bad_weight_lower
#print axioms Aris4Math.ThirtyThree.OrdinaryLink.weight_lower_of_twenty_degree_eight

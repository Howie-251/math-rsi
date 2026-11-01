import Aris4Math.LinkCounting
import Aris4Math.ConditionalUnion

/-! Actual unordered link pairs and their two ordered deletion directions. -/

open scoped BigOperators

namespace Aris4Math.LinkDeletion

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Sum the two actual directions of a two-edge family. No symmetry of the
bookkeeping weights is assumed. -/
def unorderedWeight (w : Finset V × Finset V → ℚ) (p : Finset (Finset V)) : ℚ :=
  ∑ d ∈ p.offDiag, w d

/-- Ordered pairs contributed by the actual bad link pairs through x. -/
def directedBadPairs (H : Simple5Hypergraph V) (x : V) :
    Finset (Finset V × Finset V) := (H.badLinkPairs x).biUnion Finset.offDiag

omit [Fintype V] in
theorem pair_eq_of_mem_offDiag {p : Finset (Finset V)} (hp : p.card = 2)
    {a b : Finset V} (hab : (a,b) ∈ p.offDiag) : p = {a,b} := by
  obtain ⟨ha, hb, hne⟩ := Finset.mem_offDiag.mp hab
  have hsub : {a,b} ⊆ p := by simp only [Finset.insert_subset_iff, Finset.singleton_subset_iff]; exact ⟨ha,hb⟩
  have hcard : ({a,b} : Finset (Finset V)).card = 2 := by simp [hne]
  exact (Finset.eq_of_subset_of_card_le hsub (by rw [hp,hcard])).symm

theorem badPair_card (H : Simple5Hypergraph V) (x : V)
    (p : Finset (Finset V)) (hp : p ∈ H.badLinkPairs x) : p.card = 2 :=
  (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hp).1).2

theorem badPair_subset (H : Simple5Hypergraph V) (x : V)
    (p : Finset (Finset V)) (hp : p ∈ H.badLinkPairs x) : p ⊆ H.incidentEdges x :=
  (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hp).1).1

theorem directions_disjoint (H : Simple5Hypergraph V) (x : V)
    (p q : Finset (Finset V)) (hp : p ∈ H.badLinkPairs x) (hq : q ∈ H.badLinkPairs x)
    (hne : p ≠ q) : Disjoint p.offDiag q.offDiag := by
  apply Finset.disjoint_left.mpr
  intro d hdp hdq
  exact hne ((pair_eq_of_mem_offDiag (badPair_card H x p hp) hdp).trans
    (pair_eq_of_mem_offDiag (badPair_card H x q hq) hdq).symm)

/-- No directed pair is contributed twice by different unordered bad pairs. -/
theorem directed_bad_sum (H : Simple5Hypergraph V) (x : V)
    (w : Finset V × Finset V → ℚ) :
    (∑ d ∈ directedBadPairs H x, w d) = ∑ p ∈ H.badLinkPairs x, unorderedWeight w p := by
  unfold directedBadPairs unorderedWeight
  apply Finset.sum_biUnion
  intro p hp q hq hne
  exact directions_disjoint H x p q hp hq hne

theorem directed_bad_subset (H : Simple5Hypergraph V) (x : V) :
    directedBadPairs H x ⊆ H.edges.offDiag := by
  intro d hd
  obtain ⟨p, hp, hdp⟩ := Finset.mem_biUnion.mp hd
  obtain ⟨ha, hb, hne⟩ := Finset.mem_offDiag.mp hdp
  have hsub := badPair_subset H x p hp
  exact Finset.mem_offDiag.mpr
    ⟨(Finset.mem_filter.mp (hsub ha)).1, (Finset.mem_filter.mp (hsub hb)).1, hne⟩

/-- Every selected direction is a real noncontributor: its two edges share
x and at least one distinct other vertex. -/
theorem directed_bad_intersection (H : Simple5Hypergraph V) (x : V)
    (d : Finset V × Finset V) (hd : d ∈ directedBadPairs H x) :
    (d.1 ∩ d.2).card ≠ 1 := by
  obtain ⟨p, hp, hdp⟩ := Finset.mem_biUnion.mp hd
  obtain ⟨ha, hb, _⟩ := Finset.mem_offDiag.mp hdp
  have hsub := badPair_subset H x p hp
  have hx : x ∈ d.1 ∩ d.2 := Finset.mem_inter.mpr
    ⟨(Finset.mem_filter.mp (hsub ha)).2, (Finset.mem_filter.mp (hsub hb)).2⟩
  obtain ⟨y, hy⟩ := (Finset.mem_filter.mp hp).2
  have hydata : y ∈ Finset.univ.erase x ∧ (∀ e ∈ p, y ∈ e) := by
    simpa only [LinkCounting.commonWithin, Finset.mem_filter] using hy
  have hyx : y ≠ x := (Finset.mem_erase.mp hydata.1).1
  have hymem : y ∈ d.1 ∩ d.2 := Finset.mem_inter.mpr ⟨hydata.2 d.1 ha, hydata.2 d.2 hb⟩
  intro hcard
  obtain ⟨z, hz⟩ := Finset.card_eq_one.mp hcard
  rw [hz, Finset.mem_singleton] at hx hymem
  exact hyx (hymem.trans hx.symm)

/-- The number of distinct ordered deletion entries is exactly twice the
number of actual unordered bad link pairs. -/
theorem directed_bad_card (H : Simple5Hypergraph V) (x : V) :
    (directedBadPairs H x).card = 2 * (H.badLinkPairs x).card := by
  unfold directedBadPairs
  rw [Finset.card_biUnion (fun p hp q hq hne => directions_disjoint H x p q hp hq hne)]
  have hc (p : Finset (Finset V)) (hp : p ∈ H.badLinkPairs x) : p.offDiag.card = 2 := by
    rw [Finset.offDiag_card, badPair_card H x p hp]
  simp_rw [Finset.sum_congr rfl hc]
  simp [Nat.mul_comm]

/-- A uniform lower bound on actual unordered weights yields a deletion
lower bound from any proven count q. This does not double q: the unordered
weight already sums the two possibly unequal directions. -/
theorem uniform_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (w : Finset V × Finset V → ℚ) (q : ℕ) (c : ℚ)
    (hq : q ≤ (H.badLinkPairs x).card) (hc : 0 ≤ c)
    (hw : ∀ p ∈ H.badLinkPairs x, c ≤ unorderedWeight w p) :
    (q : ℚ) * c ≤ ∑ d ∈ directedBadPairs H x, w d := by
  rw [directed_bad_sum]
  calc
    _ ≤ ((H.badLinkPairs x).card : ℚ) * c := mul_le_mul_of_nonneg_right (by exact_mod_cast hq) hc
    _ = ∑ _p ∈ H.badLinkPairs x, c := by simp
    _ ≤ _ := Finset.sum_le_sum hw


omit [Fintype V] in
/-- An unordered two-edge family carries exactly its forward plus reverse
weights, which need not coincide. -/
theorem unorderedWeight_pair (w : Finset V × Finset V → ℚ)
    (a b : Finset V) (hab : a ≠ b) :
    unorderedWeight w {a,b} = w (a,b) + w (b,a) := by
  have hp : ({a,b} : Finset (Finset V)).offDiag = {(a,b),(b,a)} := by
    ext d
    rcases d with ⟨c,d⟩
    simp only [Finset.mem_offDiag, Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq]
    aesop
  unfold unorderedWeight
  rw [hp]
  simp [hab]

/-- P8 followed by an actual, direction-sensitive weight lower bound. -/
theorem covering_bad_weight_lower (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (x : V) (w : Finset V × Finset V → ℚ) (c : ℚ) (hc : 0 ≤ c)
    (hw : ∀ p ∈ H.badLinkPairs x, c ≤ unorderedWeight w p) :
    (((4 * H.degree x - (Fintype.card V - 1) + 2) / 3 : ℕ) : ℚ) * c ≤
      ∑ d ∈ directedBadPairs H x, w d :=
  uniform_bad_weight_lower H x w _ c (H.link_bad_pair_lower_bound cover x) hc hw

/-- A finite capacity of exceptional (possibly zero-weight) slots is allowed.
Only slots outside this exception family are charged the common lower bound. -/
theorem exceptional_weight_lower {α : Type*} [DecidableEq α]
    (s exceptions : Finset α) (w : α → ℚ) (q cap : ℕ) (c : ℚ)
    (hq : q ≤ s.card) (hcap : exceptions.card ≤ cap) (hc : 0 ≤ c)
    (hnonneg : ∀ p ∈ s, 0 ≤ w p)
    (hgood : ∀ p ∈ s, p ∉ exceptions → c ≤ w p) :
    ((q - cap : ℕ) : ℚ) * c ≤ ∑ p ∈ s, w p := by
  have hcard : q - cap ≤ (s \ exceptions).card := by
    have := Finset.card_le_card_sdiff_add_card (s := s) (t := exceptions)
    omega
  calc
    _ ≤ (((s \ exceptions).card : ℕ) : ℚ) * c :=
      mul_le_mul_of_nonneg_right (by exact_mod_cast hcard) hc
    _ = ∑ _p ∈ s \ exceptions, c := by simp
    _ ≤ ∑ p ∈ s \ exceptions, w p := Finset.sum_le_sum fun p hp =>
      hgood p (Finset.mem_sdiff.mp hp).1 (Finset.mem_sdiff.mp hp).2
    _ ≤ ∑ p ∈ s, w p := Finset.sum_le_sum_of_subset_of_nonneg
      Finset.sdiff_subset (fun p hp _ => hnonneg p hp)

/-- The capacity-sensitive lower bound applied to real bad unordered pairs. -/
theorem exceptional_bad_weight_lower (H : Simple5Hypergraph V) (x : V)
    (exceptions : Finset (Finset (Finset V))) (w : Finset V × Finset V → ℚ)
    (q cap : ℕ) (c : ℚ) (hq : q ≤ (H.badLinkPairs x).card)
    (hcap : exceptions.card ≤ cap) (hc : 0 ≤ c)
    (hnonneg : ∀ p ∈ H.badLinkPairs x, 0 ≤ unorderedWeight w p)
    (hgood : ∀ p ∈ H.badLinkPairs x, p ∉ exceptions → c ≤ unorderedWeight w p) :
    ((q - cap : ℕ) : ℚ) * c ≤ ∑ d ∈ directedBadPairs H x, w d := by
  rw [directed_bad_sum]
  exact exceptional_weight_lower _ exceptions (unorderedWeight w) q cap c hq hcap hc hnonneg hgood


/-- Checking forward-plus-reverse weights on incident edge pairs suffices;
every bad unordered pair is automatically one such distinct pair. -/
theorem unordered_bound_of_incident_bound (H : Simple5Hypergraph V) (x : V)
    (w : Finset V × Finset V → ℚ) (c : ℚ)
    (hw : ∀ a ∈ H.incidentEdges x, ∀ b ∈ H.incidentEdges x, a ≠ b →
      c ≤ w (a,b) + w (b,a)) :
    ∀ p ∈ H.badLinkPairs x, c ≤ unorderedWeight w p := by
  intro p hp
  obtain ⟨a,b,hab,hpab⟩ := Finset.card_eq_two.mp (badPair_card H x p hp)
  have hsub := badPair_subset H x p hp
  rw [hpab] at hsub ⊢
  rw [unorderedWeight_pair w a b hab]
  exact hw a (hsub (by simp)) b (hsub (by simp)) hab

omit [Fintype V] [DecidableEq V] in
/-- At most two exceptional actual edges create at most one distinct
unordered pair, irrespective of whether that pair is really bad. -/
theorem exceptional_pair_capacity (S : Finset (Finset V)) (hS : S.card ≤ 2) :
    (S.powersetCard 2).card ≤ 1 := by
  rw [Finset.card_powersetCard]
  simpa using Nat.choose_le_choose 2 hS

/-- A reusable form of the v=23 last-center argument: all directions are
nonnegative, and every pair not consisting of two exceptional actual edges
has weight at least c. The two exceptional edges cost at most one slot. -/
theorem two_exceptional_edges_weight_lower (H : Simple5Hypergraph V) (x : V)
    (S : Finset (Finset V)) (hS : S.card ≤ 2)
    (w : Finset V × Finset V → ℚ) (q : ℕ) (c : ℚ)
    (hq : q ≤ (H.badLinkPairs x).card) (hc : 0 ≤ c)
    (hnonneg : ∀ a ∈ H.incidentEdges x, ∀ b ∈ H.incidentEdges x, a ≠ b →
      0 ≤ w (a,b) + w (b,a))
    (hgood : ∀ a ∈ H.incidentEdges x, ∀ b ∈ H.incidentEdges x, a ≠ b →
      (a ∉ S ∨ b ∉ S) → c ≤ w (a,b) + w (b,a)) :
    ((q - 1 : ℕ) : ℚ) * c ≤ ∑ d ∈ directedBadPairs H x, w d := by
  apply exceptional_bad_weight_lower H x (S.powersetCard 2) w q 1 c hq
    (exceptional_pair_capacity S hS) hc
    (unordered_bound_of_incident_bound H x w 0 hnonneg)
  intro p hp hnot
  obtain ⟨a,b,hab,hpab⟩ := Finset.card_eq_two.mp (badPair_card H x p hp)
  have hsub := badPair_subset H x p hp
  have hout : a ∉ S ∨ b ∉ S := by
    by_contra hn
    push_neg at hn
    apply hnot
    apply Finset.mem_powersetCard.mpr
    constructor
    · rw [hpab]
      simpa only [Finset.insert_subset_iff, Finset.singleton_subset_iff] using hn
    · exact badPair_card H x p hp
  rw [hpab] at hsub ⊢
  rw [unorderedWeight_pair w a b hab]
  exact hgood a (hsub (by simp)) b (hsub (by simp)) hab hout

section FinitePositions

variable {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]
open Aris4Math.EndpointCounting Aris4Math.ConditionalUnion

omit [DecidableEq ι] in
/-- The actual bad-link weight is a valid subtraction from the actual critical
pair probability sum. The selected directions and their zero contribution
are conclusions, not assumptions supplied by the application. -/
theorem critical_sum_le_link_deletion (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (x k : Fin v)
    (w : Finset (Fin v) × Finset (Fin v) → ℚ) (d : ℚ)
    (upper : ∀ p ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k) ≤ w p)
    (lower : d ≤ ∑ p ∈ H.badLinkPairs x, unorderedWeight w p) :
    (∑ p ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Aris4Math.Greedy.CriticalPair (p.1.map σ.toEmbedding) (p.2.map σ.toEmbedding) k)) ≤
      (∑ p ∈ H.edges.offDiag, w p) - d := by
  apply pair_sum_le_weighted_deletion vertices positions H.edges k w (directedBadPairs H x) d
    upper (directed_bad_subset H x) (directed_bad_intersection H x)
  rwa [directed_bad_sum]

end FinitePositions

end Aris4Math.LinkDeletion

#print axioms Aris4Math.LinkDeletion.directed_bad_sum
#print axioms Aris4Math.LinkDeletion.directed_bad_subset
#print axioms Aris4Math.LinkDeletion.directed_bad_intersection
#print axioms Aris4Math.LinkDeletion.directed_bad_card
#print axioms Aris4Math.LinkDeletion.uniform_bad_weight_lower

#print axioms Aris4Math.LinkDeletion.unorderedWeight_pair
#print axioms Aris4Math.LinkDeletion.covering_bad_weight_lower
#print axioms Aris4Math.LinkDeletion.exceptional_bad_weight_lower
#print axioms Aris4Math.LinkDeletion.critical_sum_le_link_deletion

#print axioms Aris4Math.LinkDeletion.unordered_bound_of_incident_bound
#print axioms Aris4Math.LinkDeletion.two_exceptional_edges_weight_lower

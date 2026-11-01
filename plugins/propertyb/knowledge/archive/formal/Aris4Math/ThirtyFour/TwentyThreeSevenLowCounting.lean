import Aris4Math.SevenPoint
import Aris4Math.Structure

/-! Seven actual low vertices cannot have the two-triple residue on every
six-subset. Counts are over original edges, so different edges with the same
trace retain their multiplicities. No finite table is checked here. -/
namespace Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting
open scoped BigOperators
variable {V : Type*} [DecidableEq V]

/-- The two features of the six-lock residue used by the deletion argument. -/
def TwoTripleTraceShape (H : Simple5Hypergraph V) (S : Finset V) : Prop :=
  (∀ e ∈ H.edges, (e ∩ S).card ≤ 3) ∧
    (H.edges.filter (fun e => (e ∩ S).card = 3)).card = 2

/-- A seven-point trace of size four or five survives a suitable deletion. -/
theorem seven_traces_small (H : Simple5Hypergraph V) (W : Finset V)
    (seven : W.card = 7)
    (deletions : ∀ x ∈ W, ∀ e ∈ H.edges, (e ∩ W.erase x).card ≤ 3) :
    ∀ e ∈ H.edges, (e ∩ W).card ≤ 3 := by
  intro e he
  have bound : e.card = 5 := H.five_uniform e he
  have outside : (W \ e).Nonempty := by
    apply Finset.card_pos.mp
    have lower := Finset.le_card_sdiff e W
    rw [seven, bound] at lower
    omega
  obtain ⟨x, hx⟩ := outside
  obtain ⟨hxW, hxe⟩ := Finset.mem_sdiff.mp hx
  have survives : e ∩ W.erase x = e ∩ W := by
    rw [Finset.inter_erase, Finset.erase_eq_of_notMem]
    exact fun mem => hxe (Finset.mem_inter.mp mem).1
  simpa only [survives] using deletions x hxW e he

/-- Once traces have size at most three, triple traces after deletion are
exactly the original triple-producing edges avoiding the deleted point. -/
theorem triple_edges_after_deletion (H : Simple5Hypergraph V) (W : Finset V)
    (small : ∀ e ∈ H.edges, (e ∩ W).card ≤ 3) (x : V) (hx : x ∈ W) :
    H.edges.filter (fun e => (e ∩ W.erase x).card = 3) =
      (H.edges.filter (fun e => (e ∩ W).card = 3)).filter (fun e => x ∉ e) := by
  ext e
  simp only [Finset.mem_filter]
  constructor
  · rintro ⟨he, hthree⟩
    have hxe : x ∉ e := by
      intro hxe
      have erased := Finset.card_erase_add_one (Finset.mem_inter.mpr ⟨hxe, hx⟩)
      rw [← Finset.inter_erase, hthree] at erased
      have bound := small e he
      omega
    have survives : e ∩ W.erase x = e ∩ W := by
      rw [Finset.inter_erase, Finset.erase_eq_of_notMem]
      exact fun mem => hxe (Finset.mem_inter.mp mem).1
    exact ⟨⟨he, by simpa only [survives] using hthree⟩, hxe⟩
  · rintro ⟨⟨he, hthree⟩, hxe⟩
    refine ⟨he, ?_⟩
    rw [Finset.inter_erase, Finset.erase_eq_of_notMem]
    · exact hthree
    · exact fun mem => hxe (Finset.mem_inter.mp mem).1

/-- The same original edges are counted in all seven deletion views:
7 * 2 = 4 * b is impossible over the natural numbers. -/
theorem exists_deletion_not_two_triple_trace_shape
    (H : Simple5Hypergraph V) (W : Finset V) (seven : W.card = 7) :
    ∃ x ∈ W, ¬ TwoTripleTraceShape H (W.erase x) := by
  by_contra none
  have each : ∀ x ∈ W, TwoTripleTraceShape H (W.erase x) := by
    intro x hx
    by_contra notshape
    exact none ⟨x, hx, notshape⟩
  have small := seven_traces_small H W seven (fun x hx => (each x hx).1)
  let triples := H.edges.filter (fun e => (e ∩ W).card = 3)
  have each_count (x : V) (hx : x ∈ W) :
      (triples.filter (fun e => x ∉ e)).card = 2 := by
    have eq := (each x hx).2
    rw [triple_edges_after_deletion H W small x hx] at eq
    exact eq
  have left : (∑ x ∈ W, (triples.filter (fun e => x ∉ e)).card) = 14 := by
    calc
      _ = ∑ _x ∈ W, 2 := Finset.sum_congr rfl each_count
      _ = 14 := by simp [seven]
  have right : (∑ e ∈ triples, (W \ e).card) = triples.card * 4 := by
    calc
      _ = ∑ _e ∈ triples, 4 := by
        apply Finset.sum_congr rfl
        intro e he
        have trace := (Finset.mem_filter.mp he).2
        rw [Finset.card_sdiff, seven, trace]
      _ = _ := by simp
  have impossible := SevenPoint.absent_incidence_count W triples
  rw [left, right] at impossible
  omega

/-- Every seven actual degree-six vertices contain a six-subset that avoids
the unique six-low residue. This is independent of the number of edges. -/
theorem exists_six_lows_not_two_triple_trace_shape [Fintype V]
    (H : Simple5Hypergraph V) (many : 7 ≤ H.sixVertices.card) :
    ∃ S : Finset V, S ⊆ H.sixVertices ∧ S.card = 6 ∧ ¬ TwoTripleTraceShape H S := by
  obtain ⟨W, sub, seven⟩ := Finset.exists_subset_card_eq many
  obtain ⟨x, hx, notshape⟩ := exists_deletion_not_two_triple_trace_shape H W seven
  refine ⟨W.erase x, (Finset.erase_subset x W).trans sub, ?_, notshape⟩
  rw [Finset.card_erase_of_mem hx, seven]

/-- Actual six-subset classification is the only outstanding premise of
this final analytic step. It must be supplied by the 4→5→6 local classifiers. -/
theorem propertyB_of_six_low_classification [Fintype V]
    (H : Simple5Hypergraph V) (many : 7 ≤ H.sixVertices.card)
    (classify : ¬ PropertyB H → ∀ S : Finset V,
      S ⊆ H.sixVertices → S.card = 6 → TwoTripleTraceShape H S) : PropertyB H := by
  by_contra notB
  obtain ⟨S, sub, six, notshape⟩ := exists_six_lows_not_two_triple_trace_shape H many
  exact notshape (classify notB S sub six)

end Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting
#print axioms Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting.exists_deletion_not_two_triple_trace_shape
#print axioms Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting.propertyB_of_six_low_classification

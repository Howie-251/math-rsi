import Aris4Math.Traces
import Aris4Math.TraceRecovery

/-! Actual six-degree lock selection and trace counts at 25 vertices.
All blocks are the existing `H.multiTraces` of real edge intersections. -/

namespace Aris4Math.ThirtyThree.TwentyFiveStructure

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

theorem sixVertices_card_ge_ten (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (vertices25 : Fintype.card V = 25) :
    10 ≤ H.sixVertices.card := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices25] at h
    omega
  have each (x : V) : 7 ≤ H.degree x + if H.degree x = 6 then 1 else 0 := by
    have hd := minimum x
    split_ifs <;> omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have budget : 7 * Fintype.card V ≤ 165 + H.sixVertices.card := by
    simpa [Finset.sum_add_distrib, H.sum_degrees, edges33,
      Simple5Hypergraph.sixVertices, Nat.mul_comm] using h
  rw [vertices25] at budget
  omega

theorem exists_ten_six_degree_unit (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (vertices25 : Fintype.card V = 25) :
    ∃ W : Finset V, W.card = 10 ∧ (∀ x ∈ W, H.degree x = 6) ∧ H.UnitCodegrees W := by
  obtain ⟨W, hsub, hc⟩ := Finset.exists_subset_card_eq
    (sixVertices_card_ge_ten H cover edges33 vertices25)
  have degree (x : V) (hx : x ∈ W) : H.degree x = 6 :=
    (Finset.mem_filter.mp (hsub hx)).2
  refine ⟨W, hc, degree, ?_⟩
  intro x hx y _ hne
  exact H.codegree_eq_one_of_twenty_five cover vertices25 (degree x hx) hne

omit [Fintype V] in
/-- Every lock pair occurs in exactly one actual multipoint block. -/
theorem trace_pairs_sum (H : Simple5Hypergraph V) (W : Finset V)
    (unit : H.UnitCodegrees W) :
    (∑ B ∈ H.multiTraces W, B.card.choose 2) = W.card.choose 2 := by
  have union : (H.multiTraces W).biUnion (fun B => B.powersetCard 2) = W.powersetCard 2 := by
    ext P
    constructor
    · intro hP
      obtain ⟨B, hB, hPB⟩ := Finset.mem_biUnion.mp hP
      obtain ⟨hsub, hc⟩ := Finset.mem_powersetCard.mp hPB
      exact Finset.mem_powersetCard.mpr ⟨hsub.trans (H.multiTraces_subset W hB), hc⟩
    · intro hP
      obtain ⟨hsub, hc⟩ := Finset.mem_powersetCard.mp hP
      obtain ⟨B, ⟨hB, hPB⟩, _⟩ := H.existsUnique_multiTrace_containing_pair W unit hsub hc
      exact Finset.mem_biUnion.mpr ⟨B, hB, Finset.mem_powersetCard.mpr ⟨hPB, hc⟩⟩
  have disjoint : ∀ B ∈ H.multiTraces W, ∀ C ∈ H.multiTraces W, B ≠ C →
      Disjoint (B.powersetCard 2) (C.powersetCard 2) := by
    intro B hB C hC hne
    apply Finset.disjoint_left.mpr
    intro P hPB hPC
    have hsub : P ⊆ B ∩ C := Finset.subset_inter
      (Finset.mem_powersetCard.mp hPB).1 (Finset.mem_powersetCard.mp hPC).1
    have hcard := Finset.card_le_card hsub
    have hi := H.multiTraces_inter_card_le_one W unit hB hC hne
    have hc := (Finset.mem_powersetCard.mp hPB).2
    omega
  have h := Finset.card_biUnion disjoint
  rw [union, Finset.card_powersetCard] at h
  simpa only [Finset.card_powersetCard] using h.symm

omit [Fintype V] in
/-- Sum actual block incidences, with no multiplicity assumption supplied. -/
theorem trace_incidence_sum (H : Simple5Hypergraph V) (W : Finset V) :
    (∑ x ∈ W, ((H.multiTraces W).filter fun B => x ∈ B).card) =
      ∑ B ∈ H.multiTraces W, B.card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro B hB
  rw [← Finset.sum_filter]
  have hfilter : W.filter (fun x => x ∈ B) = B := by
    rw [Finset.filter_mem_eq_inter]
    exact Finset.inter_eq_right.mpr (H.multiTraces_subset W hB)
  rw [hfilter]

omit [Fintype V] in
theorem trace_incidence_le_six (H : Simple5Hypergraph V) (W : Finset V)
    (unit : H.UnitCodegrees W) (degrees : ∀ x ∈ W, H.degree x = 6) :
    (∑ B ∈ H.multiTraces W, B.card) ≤ 6 * W.card := by
  rw [← trace_incidence_sum]
  have each (x : V) (hx : x ∈ W) : ((H.multiTraces W).filter fun B => x ∈ B).card ≤ 6 := by
    have h := H.singleton_typeCount_add_blocks W unit hx
    rw [degrees x hx] at h
    omega
  have h := Finset.sum_le_sum each
  simpa [Nat.mul_comm] using h

omit [Fintype V] in
/-- Without a block of size at least four, ten degree-six locks have at
least ten actual three-point blocks. This is a global incidence proof. -/
theorem ten_le_triple_count (H : Simple5Hypergraph V) (W : Finset V)
    (ten : W.card = 10) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6)
    (small : ∀ B ∈ H.multiTraces W, B.card ≤ 3) :
    10 ≤ ((H.multiTraces W).filter fun B => B.card = 3).card := by
  have pairs := trace_pairs_sum H W unit
  have incidence := trace_incidence_le_six H W unit degrees
  have identity : 2 * (∑ B ∈ H.multiTraces W, B.card.choose 2) =
      (∑ B ∈ H.multiTraces W, B.card) +
        3 * ((H.multiTraces W).filter fun B => B.card = 3).card := by
    rw [Finset.mul_sum, Finset.card_eq_sum_ones, Finset.sum_filter,
      Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro B hB
    have lower := ((H.mem_multiTraces W B).mp hB).2
    have upper := small B hB
    have cases : B.card = 2 ∨ B.card = 3 := by omega
    rcases cases with h | h <;> simp [h]
  rw [ten] at pairs incidence
  have choose : Nat.choose 10 2 = 45 := by decide
  rw [choose] at pairs
  norm_num at pairs incidence
  omega

omit [Fintype V] in
/-- A fixed triple of a ten-element set occurs in exactly 21 eight-subsets.
The bijection removes that triple, leaving a five-subset of its complement. -/
theorem eight_subsets_containing_triple (W B : Finset V)
    (ten : W.card = 10) (sub : B ⊆ W) (three : B.card = 3) :
    ((W.powersetCard 8).filter fun S => B ⊆ S).card = 21 := by
  have bij : ((W.powersetCard 8).filter fun S => B ⊆ S).card =
      ((W \ B).powersetCard 5).card := by
    apply Finset.card_bij (fun S _ => S \ B)
    · intro S hS
      obtain ⟨hSW, hcS⟩ := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hS).1
      have hBS := (Finset.mem_filter.mp hS).2
      apply Finset.mem_powersetCard.mpr
      constructor
      · intro z hz
        obtain ⟨hzS, hzB⟩ := Finset.mem_sdiff.mp hz
        exact Finset.mem_sdiff.mpr ⟨hSW hzS, hzB⟩
      · rw [Finset.card_sdiff_of_subset hBS, hcS, three]
    · intro S hS T hT same
      have hBS := (Finset.mem_filter.mp hS).2
      have hBT := (Finset.mem_filter.mp hT).2
      rw [← Finset.union_sdiff_of_subset hBS, ← Finset.union_sdiff_of_subset hBT, same]
    · intro C hC
      obtain ⟨hCW, hcC⟩ := Finset.mem_powersetCard.mp hC
      have disjoint : Disjoint B C := by
        apply Finset.disjoint_left.mpr
        intro z hzB hzC
        exact (Finset.mem_sdiff.mp (hCW hzC)).2 hzB
      refine ⟨B ∪ C, ?_, ?_⟩
      · apply Finset.mem_filter.mpr
        constructor
        · apply Finset.mem_powersetCard.mpr
          constructor
          · exact Finset.union_subset sub (hCW.trans Finset.sdiff_subset)
          · rw [Finset.card_union_of_disjoint disjoint, three, hcC]
        · exact Finset.subset_union_left
      · ext z
        simp only [Finset.mem_sdiff, Finset.mem_union]
        constructor
        · rintro ⟨hzB | hzC, hnB⟩
          · exact False.elim (hnB hzB)
          · exact hzC
        · intro hzC
          exact ⟨Or.inr hzC, (Finset.mem_sdiff.mp (hCW hzC)).2⟩
  rw [bij, Finset.card_powersetCard, Finset.card_sdiff_of_subset sub, ten, three]
  decide

omit [Fintype V] in
/-- Average over all 45 eight-subsets. This theorem concerns an arbitrary
family of actual triples, without requiring a classification or an enumeration. -/
theorem exists_eight_subset_preserving_five_triples
    (W : Finset V) (T : Finset (Finset V))
    (ten : W.card = 10) (inside : ∀ B ∈ T, B ⊆ W)
    (triples : ∀ B ∈ T, B.card = 3) (many : 10 ≤ T.card) :
    ∃ S ⊆ W, S.card = 8 ∧ 5 ≤ (T.filter fun B => B ⊆ S).card := by
  have count : (∑ S ∈ W.powersetCard 8, (T.filter fun B => B ⊆ S).card) =
      21 * T.card := by
    simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
    rw [Finset.sum_comm]
    calc
      _ = ∑ _B ∈ T, 21 := by
        apply Finset.sum_congr rfl
        intro B hB
        rw [← Finset.sum_filter, ← Finset.card_eq_sum_ones]
        exact eight_subsets_containing_triple W B ten (inside B hB) (triples B hB)
      _ = _ := by simp [Nat.mul_comm]
  by_contra hn
  have each (S : Finset V) (hS : S ∈ W.powersetCard 8) :
      (T.filter fun B => B ⊆ S).card ≤ 4 := by
    obtain ⟨hsub, hc⟩ := Finset.mem_powersetCard.mp hS
    have hnot : ¬ 5 ≤ (T.filter fun B => B ⊆ S).card := fun h => hn ⟨S,hsub,hc,h⟩
    omega
  have upper := Finset.sum_le_sum each
  rw [count] at upper
  have subsets : (W.powersetCard 8).card = 45 := by
    rw [Finset.card_powersetCard, ten]
    decide
  simp only [Finset.sum_const, subsets, nsmul_eq_mul, Nat.cast_id] at upper
  omega

omit [Fintype V] in
/-- A block retained in its entirety is an actual block on the smaller locks. -/
theorem retained_trace (H : Simple5Hypergraph V) (W S B : Finset V)
    (sub : S ⊆ W) (block : B ∈ H.multiTraces W) (retained : B ⊆ S) :
    B ∈ H.multiTraces S := by
  obtain ⟨⟨e, he, trace⟩, large⟩ := (H.mem_multiTraces W B).mp block
  apply (H.mem_multiTraces S B).mpr
  refine ⟨⟨e, he, ?_⟩, large⟩
  apply Finset.Subset.antisymm
  · intro z hz
    rw [← trace]
    exact Finset.mem_inter.mpr ⟨(Finset.mem_inter.mp hz).1, sub (Finset.mem_inter.mp hz).2⟩
  · intro z hz
    have hze : z ∈ e := Finset.mem_of_mem_inter_left (trace.symm ▸ hz)
    exact Finset.mem_inter.mpr ⟨hze, retained hz⟩

omit [Fintype V] in
theorem small_traces_on_subset (H : Simple5Hypergraph V) (W S : Finset V)
    (sub : S ⊆ W) (small : ∀ B ∈ H.multiTraces W, B.card ≤ 3) :
    ∀ B ∈ H.multiTraces S, B.card ≤ 3 := by
  intro B hB
  obtain ⟨⟨e, he, trace⟩, large⟩ := (H.mem_multiTraces S B).mp hB
  have hsub : e ∩ S ⊆ e ∩ W := Finset.inter_subset_inter_left sub
  have hcard := Finset.card_le_card hsub
  rw [trace] at hcard
  have hC : e ∩ W ∈ H.multiTraces W :=
    (H.mem_multiTraces W _).mpr ⟨⟨e,he,rfl⟩, by omega⟩
  have hsmall := small _ hC
  omega

omit [Fintype V] in
/-- The average-selected eight-subset has at least five actual triple traces. -/
theorem exists_eight_actual_triples (H : Simple5Hypergraph V) (W : Finset V)
    (ten : W.card = 10) (unit : H.UnitCodegrees W)
    (degrees : ∀ x ∈ W, H.degree x = 6)
    (small : ∀ B ∈ H.multiTraces W, B.card ≤ 3) :
    ∃ S ⊆ W, S.card = 8 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
      (∀ B ∈ H.multiTraces S, B.card ≤ 3) ∧
      5 ≤ ((H.multiTraces S).filter fun B => B.card = 3).card := by
  let T := (H.multiTraces W).filter fun B => B.card = 3
  have inside : ∀ B ∈ T, B ⊆ W := fun B hB => H.multiTraces_subset W (Finset.mem_filter.mp hB).1
  have triples : ∀ B ∈ T, B.card = 3 := fun _ hB => (Finset.mem_filter.mp hB).2
  obtain ⟨S, hSW, hS, many⟩ := exists_eight_subset_preserving_five_triples W T ten
    inside triples (ten_le_triple_count H W ten unit degrees small)
  refine ⟨S, hSW, hS, (fun x hx => degrees x (hSW hx)),
    (fun x hx y hy ne => unit x (hSW hx) y (hSW hy) ne),
    small_traces_on_subset H W S hSW small, ?_⟩
  apply many.trans
  apply Finset.card_le_card
  intro B hB
  obtain ⟨hBT, retained⟩ := Finset.mem_filter.mp hB
  exact Finset.mem_filter.mpr
    ⟨retained_trace H W S B hSW (Finset.mem_filter.mp hBT).1 retained, triples B hBT⟩

omit [Fintype V] in
/-- Every point of eight degree-six locks lies in a triple if no block is
larger than three. Otherwise it would require seven distinct two-point blocks. -/
theorem every_point_in_triple (H : Simple5Hypergraph V) (S : Finset V)
    (eight : S.card = 8) (unit : H.UnitCodegrees S)
    (degrees : ∀ x ∈ S, H.degree x = 6)
    (small : ∀ B ∈ H.multiTraces S, B.card ≤ 3) :
    ∀ x ∈ S, ∃ B ∈ H.multiTraces S, B.card = 3 ∧ x ∈ B := by
  intro x hx
  by_contra hn
  let F := (H.multiTraces S).filter fun B => x ∈ B
  have pair (B : Finset V) (hB : B ∈ F) : B.card = 2 := by
    have hb := (Finset.mem_filter.mp hB).1
    have lower := ((H.mem_multiTraces S B).mp hb).2
    have upper := small B hb
    have hnot : B.card ≠ 3 := fun h => hn ⟨B, hb, h, (Finset.mem_filter.mp hB).2⟩
    omega
  have cover_other : S.erase x ⊆ F.biUnion (fun B => B.erase x) := by
    intro y hy
    obtain ⟨hne, hyS⟩ := Finset.mem_erase.mp hy
    obtain ⟨B, ⟨hB,hxB,hyB⟩, _⟩ := H.existsUnique_multiTrace_pair S unit hx hyS hne.symm
    exact Finset.mem_biUnion.mpr
      ⟨B,Finset.mem_filter.mpr ⟨hB,hxB⟩,Finset.mem_erase.mpr ⟨hne,hyB⟩⟩
  have upper : (S.erase x).card ≤ F.card := by
    calc
      _ ≤ (F.biUnion (fun B => B.erase x)).card := Finset.card_le_card cover_other
      _ ≤ ∑ B ∈ F, (B.erase x).card := Finset.card_biUnion_le
      _ = ∑ _B ∈ F, 1 := by
        apply Finset.sum_congr rfl
        intro B hB
        rw [Finset.card_erase_of_mem (Finset.mem_filter.mp hB).2, pair B hB]
      _ = F.card := by simp
  have degree := H.singleton_typeCount_add_blocks S unit hx
  rw [degrees x hx] at degree
  rw [Finset.card_erase_of_mem hx, eight] at upper
  change H.typeCount S {x} + F.card = 6 at degree
  omega

/-- Complete structural fork from the original 25-vertex input: either six
degree-six locks have a large actual block, or eight such locks have at least
five triples and every point lies in a triple. Classification is not assumed. -/
theorem exists_six_large_or_eight_triples (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (vertices25 : Fintype.card V = 25) :
    (∃ S : Finset V, S.card = 6 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
      ∃ B ∈ H.multiTraces S, 4 ≤ B.card) ∨
    (∃ S : Finset V, S.card = 8 ∧ (∀ x ∈ S, H.degree x = 6) ∧ H.UnitCodegrees S ∧
      (∀ B ∈ H.multiTraces S, B.card ≤ 3) ∧
      5 ≤ ((H.multiTraces S).filter fun B => B.card = 3).card ∧
      ∀ x ∈ S, ∃ B ∈ H.multiTraces S, B.card = 3 ∧ x ∈ B) := by
  obtain ⟨W, ten, degrees, unit⟩ := exists_ten_six_degree_unit H cover edges33 vertices25
  by_cases large : ∃ B ∈ H.multiTraces W, 4 ≤ B.card
  · left
    obtain ⟨B, hB, hlarge⟩ := large
    have upper := H.multiTraces_card_le_five W hB
    obtain ⟨S,hBS,hSW,six⟩ := Finset.exists_subsuperset_card_eq
      (H.multiTraces_subset W hB) (show B.card ≤ 6 by omega) (show 6 ≤ W.card by omega)
    exact ⟨S, six, (fun x hx => degrees x (hSW hx)),
      (fun x hx y hy ne => unit x (hSW hx) y (hSW hy) ne),
      B, retained_trace H W S B hSW hB hBS, hlarge⟩
  · right
    have small : ∀ B ∈ H.multiTraces W, B.card ≤ 3 := by
      intro B hB
      have hnot : ¬ 4 ≤ B.card := fun h => large ⟨B,hB,h⟩
      omega
    obtain ⟨S, _, eight, sdegrees, sunit, ssmall, many⟩ :=
      exists_eight_actual_triples H W ten unit degrees small
    exact ⟨S,eight,sdegrees,sunit,ssmall,many,
      every_point_in_triple H S eight sunit sdegrees ssmall⟩

end Aris4Math.ThirtyThree.TwentyFiveStructure

#print axioms Aris4Math.ThirtyThree.TwentyFiveStructure.exists_ten_six_degree_unit
#print axioms Aris4Math.ThirtyThree.TwentyFiveStructure.ten_le_triple_count
#print axioms Aris4Math.ThirtyThree.TwentyFiveStructure.exists_eight_subset_preserving_five_triples
#print axioms Aris4Math.ThirtyThree.TwentyFiveStructure.exists_six_large_or_eight_triples

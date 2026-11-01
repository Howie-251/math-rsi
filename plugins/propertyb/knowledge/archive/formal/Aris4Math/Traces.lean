import Mathlib.Data.Finset.Powerset
import Aris4Math.Structure
import Aris4Math.Avoidance

/-! Actual hypergraph traces and their exact multiplicities.
The type and block data below are derived from H.edges, not assumed profiles. -/
open scoped BigOperators

namespace Aris4Math.Simple5Hypergraph

variable {V : Type*} [DecidableEq V]

/-- Pairwise codegree one inside the chosen lock set. -/
def UnitCodegrees (H : Simple5Hypergraph V) (S : Finset V) : Prop :=
  ∀ x ∈ S, ∀ y ∈ S, x ≠ y → H.codegree x y = 1

/-- All actual exact intersection types, including empty and singleton types. -/
def traceTypes (H : Simple5Hypergraph V) (S : Finset V) : Finset (Finset V) :=
  H.edges.image fun e => e ∩ S

/-- Distinct actual traces with at least two lock points. -/
def multiTraces (H : Simple5Hypergraph V) (S : Finset V) : Finset (Finset V) :=
  (H.traceTypes S).filter fun B => 2 ≤ B.card

/-- Number of actual edges having the specified exact trace. -/
def typeCount (H : Simple5Hypergraph V) (S T : Finset V) : Nat :=
  (H.edges.filter fun e => e ∩ S = T).card

theorem mem_multiTraces (H : Simple5Hypergraph V) (S B : Finset V) :
    B ∈ H.multiTraces S ↔ (∃ e ∈ H.edges, e ∩ S = B) ∧ 2 ≤ B.card := by
  simp [multiTraces, traceTypes]

theorem multiTraces_subset (H : Simple5Hypergraph V) (S : Finset V)
    {B : Finset V} (hB : B ∈ H.multiTraces S) : B ⊆ S := by
  obtain ⟨⟨e, _, rfl⟩, _⟩ := (H.mem_multiTraces S B).mp hB
  exact Finset.inter_subset_right

theorem multiTraces_card_le_five (H : Simple5Hypergraph V) (S : Finset V)
    {B : Finset V} (hB : B ∈ H.multiTraces S) : B.card ≤ 5 := by
  obtain ⟨⟨e, he, rfl⟩, _⟩ := (H.mem_multiTraces S B).mp hB
  exact (Finset.card_le_card Finset.inter_subset_left).trans_eq (H.five_uniform e he)

/-- An actual pair of codegree one determines its global edge uniquely. -/
theorem edges_eq_of_codegree_one (H : Simple5Hypergraph V) {x y : V}
    (hxy : H.codegree x y = 1) {e f : Finset V}
    (he : e ∈ H.edges) (hf : f ∈ H.edges)
    (hxe : x ∈ e) (hye : y ∈ e) (hxf : x ∈ f) (hyf : y ∈ f) : e = f := by
  apply Finset.card_le_one.mp (le_of_eq hxy)
    e (Finset.mem_filter.mpr ⟨he, hxe, hye⟩)
    f (Finset.mem_filter.mpr ⟨hf, hxf, hyf⟩)

/-- Two actual edges with the same multipoint trace must be equal. -/
theorem edge_eq_of_same_large_trace (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {e f : Finset V}
    (he : e ∈ H.edges) (hf : f ∈ H.edges)
    (same : e ∩ S = f ∩ S) (large : 2 ≤ (e ∩ S).card) : e = f := by
  obtain ⟨x, hx, y, hy, hne⟩ := Finset.one_lt_card.mp (by omega : 1 < (e ∩ S).card)
  have hxf : x ∈ f ∩ S := same ▸ hx
  have hyf : y ∈ f ∩ S := same ▸ hy
  exact H.edges_eq_of_codegree_one
    (unit x (Finset.mem_inter.mp hx).2 y (Finset.mem_inter.mp hy).2 hne)
    he hf (Finset.mem_inter.mp hx).1 (Finset.mem_inter.mp hy).1
    (Finset.mem_inter.mp hxf).1 (Finset.mem_inter.mp hyf).1

/-- Every multipoint trace has actual multiplicity exactly one. -/
theorem typeCount_eq_one_of_multiTrace (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {B : Finset V} (hB : B ∈ H.multiTraces S) :
    H.typeCount S B = 1 := by
  obtain ⟨⟨e, he, htrace⟩, hlarge⟩ := (H.mem_multiTraces S B).mp hB
  have lower : 1 ≤ H.typeCount S B :=
    Finset.one_le_card.mpr ⟨e, Finset.mem_filter.mpr ⟨he, htrace⟩⟩
  have upper : H.typeCount S B ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro f hf g hg
    rcases Finset.mem_filter.mp hf with ⟨hf, hftrace⟩
    rcases Finset.mem_filter.mp hg with ⟨hg, hgtrace⟩
    exact H.edge_eq_of_same_large_trace S unit hf hg
      (hftrace.trans hgtrace.symm) (hftrace.symm ▸ hlarge)
  omega

/-- Every distinct pair of locks lies in exactly one multipoint block. -/
theorem existsUnique_multiTrace_pair (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {x y : V} (hx : x ∈ S) (hy : y ∈ S) (hne : x ≠ y) :
    ∃! B, B ∈ H.multiTraces S ∧ x ∈ B ∧ y ∈ B := by
  have hcard : (H.edges.filter fun e => x ∈ e ∧ y ∈ e).card = 1 := unit x hx y hy hne
  obtain ⟨e, he⟩ := Finset.card_pos.mp (by omega : 0 < (H.edges.filter fun e => x ∈ e ∧ y ∈ e).card)
  rcases Finset.mem_filter.mp he with ⟨he, hxe, hye⟩
  have hlarge : 2 ≤ (e ∩ S).card := by
    apply Nat.succ_le_of_lt
    exact Finset.one_lt_card.mpr ⟨x, Finset.mem_inter.mpr ⟨hxe, hx⟩,
      y, Finset.mem_inter.mpr ⟨hye, hy⟩, hne⟩
  refine ⟨e ∩ S, ⟨(H.mem_multiTraces S _).mpr ⟨⟨e, he, rfl⟩, hlarge⟩,
    Finset.mem_inter.mpr ⟨hxe, hx⟩, Finset.mem_inter.mpr ⟨hye, hy⟩⟩, ?_⟩
  intro B hB
  obtain ⟨⟨f, hf, hftrace⟩, _⟩ := (H.mem_multiTraces S B).mp hB.1
  have hxf : x ∈ f := Finset.mem_of_mem_inter_left (hftrace.symm ▸ hB.2.1)
  have hyf : y ∈ f := Finset.mem_of_mem_inter_left (hftrace.symm ▸ hB.2.2)
  have hfe := H.edges_eq_of_codegree_one (unit x hx y hy hne) hf he hxf hyf hxe hye
  simpa [hfe] using hftrace.symm

/-- Distinct blocks meet in at most one point. -/
theorem multiTraces_inter_card_le_one (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {B C : Finset V}
    (hB : B ∈ H.multiTraces S) (hC : C ∈ H.multiTraces S) (hne : B ≠ C) :
    (B ∩ C).card ≤ 1 := by
  apply Finset.card_le_one.mpr
  intro x hx y hy
  by_contra hxy
  have hxB := (Finset.mem_inter.mp hx).1
  have hxC := (Finset.mem_inter.mp hx).2
  have hyB := (Finset.mem_inter.mp hy).1
  have hyC := (Finset.mem_inter.mp hy).2
  obtain ⟨D, _, unique⟩ := H.existsUnique_multiTrace_pair S unit
    (H.multiTraces_subset S hB hxB) (H.multiTraces_subset S hB hyB) hxy
  exact hne ((unique B ⟨hB, hxB, hyB⟩).trans (unique C ⟨hC, hxC, hyC⟩).symm)

/-- Fiber counting over any finite family of proposed types. -/
theorem sum_typeCount (H : Simple5Hypergraph V) (S : Finset V) (types : Finset (Finset V)) :
    (∑ B ∈ types, H.typeCount S B) =
      (H.edges.filter fun e => e ∩ S ∈ types).card := by
  exact Finset.sum_card_fiberwise_eq_card_filter H.edges types (fun e => e ∩ S)

/-- A type absent from the actual image has count zero. -/
theorem typeCount_eq_zero_of_not_traceTypes (H : Simple5Hypergraph V) (S B : Finset V)
    (absent : B ∉ H.traceTypes S) : H.typeCount S B = 0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro e he
  rcases Finset.mem_filter.mp he with ⟨he, ht⟩
  exact absent (Finset.mem_image.mpr ⟨e, he, ht⟩)

/-- Every large type is counted exactly once when present, and zero otherwise. -/
theorem typeCount_large (H : Simple5Hypergraph V) (S B : Finset V)
    (unit : H.UnitCodegrees S) (large : 2 ≤ B.card) :
    H.typeCount S B = if B ∈ H.multiTraces S then 1 else 0 := by
  split_ifs with h
  · exact H.typeCount_eq_one_of_multiTrace S unit h
  · apply H.typeCount_eq_zero_of_not_traceTypes S B
    intro ht
    exact h (Finset.mem_filter.mpr ⟨ht, large⟩)

/-- Multipoint edges are in bijection with their actual blocks. -/
theorem card_multiTrace_edges (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) :
    (H.edges.filter fun e => 2 ≤ (e ∩ S).card).card = (H.multiTraces S).card := by
  have filters : (H.edges.filter fun e => e ∩ S ∈ H.multiTraces S) =
      H.edges.filter (fun e => 2 ≤ (e ∩ S).card) := by
    apply Finset.filter_congr
    intro e he
    have ht : e ∩ S ∈ H.traceTypes S := Finset.mem_image.mpr ⟨e, he, rfl⟩
    simp [multiTraces, ht]
  rw [← filters, ← H.sum_typeCount]
  calc
    (∑ B ∈ H.multiTraces S, H.typeCount S B) = ∑ _B ∈ H.multiTraces S, 1 :=
      Finset.sum_congr rfl (fun _ hB => H.typeCount_eq_one_of_multiTrace S unit hB)
    _ = _ := by simp

/-- The same bijection restricted to blocks through a particular lock. -/
theorem card_multiTrace_edges_through (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {x : V} (hx : x ∈ S) :
    (H.edges.filter fun e => x ∈ e ∧ 2 ≤ (e ∩ S).card).card =
      ((H.multiTraces S).filter fun B => x ∈ B).card := by
  let Bs := (H.multiTraces S).filter fun B => x ∈ B
  have filters : (H.edges.filter fun e => e ∩ S ∈ Bs) =
      H.edges.filter (fun e => x ∈ e ∧ 2 ≤ (e ∩ S).card) := by
    apply Finset.filter_congr
    intro e he
    have ht : e ∩ S ∈ H.traceTypes S := Finset.mem_image.mpr ⟨e, he, rfl⟩
    simp [Bs, multiTraces, ht, hx, and_comm]
  rw [← filters, ← H.sum_typeCount]
  calc
    (∑ B ∈ Bs, H.typeCount S B) = ∑ _B ∈ Bs, 1 :=
      Finset.sum_congr rfl (fun _ hB =>
        H.typeCount_eq_one_of_multiTrace S unit (Finset.mem_filter.mp hB).1)
    _ = _ := by simp [Bs]

/-- An edge through a lock has singleton trace exactly when its trace has size one. -/
theorem trace_singleton_iff_card_one (e S : Finset V) {x : V} (hxS : x ∈ S) (hxe : x ∈ e) :
    e ∩ S = {x} ↔ (e ∩ S).card = 1 := by
  constructor
  · intro h
    simp [h]
  · intro hc
    obtain ⟨y, hy⟩ := Finset.card_eq_one.mp hc
    have hxy : x = y := by simpa [hy] using Finset.mem_inter.mpr ⟨hxe, hxS⟩
    simpa [hxy] using hy

/-- Actual degree splits into singleton edges and multipoint blocks through the lock. -/
theorem singleton_typeCount_add_blocks (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {x : V} (hx : x ∈ S) :
    H.typeCount S {x} + ((H.multiTraces S).filter fun B => x ∈ B).card = H.degree x := by
  have single : ((H.edges.filter fun e => x ∈ e).filter fun e => e ∩ S = {x}) =
      H.edges.filter (fun e => e ∩ S = {x}) := by
    ext e
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨he, _⟩, ht⟩
      exact ⟨he, ht⟩
    · rintro ⟨he, ht⟩
      have hxe : x ∈ e := Finset.mem_of_mem_inter_left (ht.symm ▸ Finset.mem_singleton_self x)
      exact ⟨⟨he, hxe⟩, ht⟩
  have multi : ((H.edges.filter fun e => x ∈ e).filter fun e => ¬ e ∩ S = {x}) =
      H.edges.filter (fun e => x ∈ e ∧ 2 ≤ (e ∩ S).card) := by
    ext e
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨he, hxe⟩, hn⟩
      have pos : 0 < (e ∩ S).card := Finset.card_pos.mpr ⟨x, Finset.mem_inter.mpr ⟨hxe, hx⟩⟩
      have neqone : (e ∩ S).card ≠ 1 := fun hc => hn ((trace_singleton_iff_card_one e S hx hxe).mpr hc)
      exact ⟨he, hxe, by omega⟩
    · rintro ⟨he, hxe, hl⟩
      refine ⟨⟨he, hxe⟩, ?_⟩
      intro ht
      have hc := (trace_singleton_iff_card_one e S hx hxe).mp ht
      omega
  have split := Finset.filter_card_add_filter_neg_card_eq_card
    (s := H.edges.filter fun e => x ∈ e) (fun e => e ∩ S = {x})
  rw [single, multi, H.card_multiTrace_edges_through S unit hx] at split
  exact split

/-- Singleton types are recovered from actual degrees and actual block incidences. -/
theorem singleton_typeCount_eq (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {x : V} (hx : x ∈ S) :
    H.typeCount S {x} = H.degree x - ((H.multiTraces S).filter fun B => x ∈ B).card := by
  have h := H.singleton_typeCount_add_blocks S unit hx
  omega

/-- Singleton traces are exactly singleton subsets of the chosen lock set. -/
theorem trace_mem_singletons_iff (e S : Finset V) :
    e ∩ S ∈ S.image (fun x => ({x} : Finset V)) ↔ (e ∩ S).card = 1 := by
  constructor
  · intro h
    obtain ⟨x, _, ht⟩ := Finset.mem_image.mp h
    rw [← ht]
    simp
  · intro hc
    obtain ⟨x, ht⟩ := Finset.card_eq_one.mp hc
    have hx : x ∈ S := Finset.mem_of_mem_inter_right (ht.symm ▸ Finset.mem_singleton_self x)
    exact Finset.mem_image.mpr ⟨x, hx, ht.symm⟩

/-- Summing singleton type counts counts exactly the edges of trace size one. -/
theorem sum_singleton_typeCount (H : Simple5Hypergraph V) (S : Finset V) :
    (∑ x ∈ S, H.typeCount S {x}) = (H.edges.filter fun e => (e ∩ S).card = 1).card := by
  calc
    (∑ x ∈ S, H.typeCount S {x}) =
        ∑ B ∈ S.image (fun x => ({x} : Finset V)), H.typeCount S B := by
      rw [Finset.sum_image]
      intro x _ y _ h
      exact Finset.singleton_injective h
    _ = (H.edges.filter fun e => e ∩ S ∈ S.image (fun x => ({x} : Finset V))).card :=
      H.sum_typeCount S _
    _ = _ := by
      congr 1
      apply Finset.filter_congr
      intro e _
      exact trace_mem_singletons_iff e S

/-- Partition every actual edge by trace size 0, 1, or at least 2. -/
theorem typeCount_partition (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) :
    H.typeCount S ∅ + (∑ x ∈ S, H.typeCount S {x}) + (H.multiTraces S).card = H.edges.card := by
  rw [H.sum_singleton_typeCount, ← H.card_multiTrace_edges S unit]
  simp only [typeCount, Finset.card_eq_sum_ones, Finset.sum_filter, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro e _
  by_cases hz : e ∩ S = ∅
  · simp [hz]
  · have pos : 0 < (e ∩ S).card := Nat.pos_of_ne_zero (fun h => hz (Finset.card_eq_zero.mp h))
    by_cases ho : (e ∩ S).card = 1
    · simp [hz, ho]
    · have large : 2 ≤ (e ∩ S).card := by omega
      simp [hz, ho, large]

/-- Empty type is recovered from total edge count and the other exact types. -/
theorem empty_typeCount_eq (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) :
    H.typeCount S ∅ = H.edges.card - (H.multiTraces S).card - ∑ x ∈ S, H.typeCount S {x} := by
  have h := H.typeCount_partition S unit
  omega

/-- An arbitrary two-point subset of S lies in a unique actual block. -/
theorem existsUnique_multiTrace_containing_pair (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {P : Finset V} (hPS : P ⊆ S) (hP : P.card = 2) :
    ∃! B, B ∈ H.multiTraces S ∧ P ⊆ B := by
  obtain ⟨x, y, hne, rfl⟩ := Finset.card_eq_two.mp hP
  have hx : x ∈ S := hPS (by simp)
  have hy : y ∈ S := hPS (by simp)
  obtain ⟨B, hB, unique⟩ := H.existsUnique_multiTrace_pair S unit hx hy hne
  refine ⟨B, ⟨hB.1, ?_⟩, ?_⟩
  · intro z hz
    rcases Finset.mem_insert.mp hz with rfl | hz
    · exact hB.2.1
    · have hzy : z = y := Finset.mem_singleton.mp hz
      simpa only [hzy] using hB.2.2
  · intro C hC
    exact unique C ⟨hC.1, hC.2 (by simp), hC.2 (by simp)⟩

/-- If every block is a pair, pair covering determines the entire block family. -/
theorem multiTraces_eq_pairs (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) (pairs : ∀ B ∈ H.multiTraces S, B.card = 2) :
    H.multiTraces S = S.powersetCard 2 := by
  ext P
  constructor
  · intro hP
    exact Finset.mem_powersetCard.mpr ⟨H.multiTraces_subset S hP, pairs P hP⟩
  · intro hP
    rcases Finset.mem_powersetCard.mp hP with ⟨hPS, cardP⟩
    obtain ⟨B, ⟨hB, sub⟩, _⟩ := H.existsUnique_multiTrace_containing_pair S unit hPS cardP
    have eq : P = B := Finset.eq_of_subset_of_card_le sub (by rw [pairs B hB, cardP])
    exact eq.symm ▸ hB

/-- With exactly one large block, all other blocks are precisely its uncovered pairs. -/
theorem multiTraces_eq_one_large_block (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) {B : Finset V} (hB : B ∈ H.multiTraces S)
    (otherPairs : ∀ C ∈ H.multiTraces S, C = B ∨ C.card = 2) :
    H.multiTraces S = insert B ((S.powersetCard 2).filter fun P => ¬ P ⊆ B) := by
  ext C
  constructor
  · intro hC
    rcases otherPairs C hC with rfl | cardC
    · exact Finset.mem_insert_self _ _
    · by_cases eq : C = B
      · exact Finset.mem_insert.mpr (Or.inl eq)
      · apply Finset.mem_insert_of_mem
        apply Finset.mem_filter.mpr
        refine ⟨Finset.mem_powersetCard.mpr ⟨H.multiTraces_subset S hC, cardC⟩, ?_⟩
        intro sub
        obtain ⟨D, _, unique⟩ := H.existsUnique_multiTrace_containing_pair S unit
          (H.multiTraces_subset S hC) cardC
        exact eq ((unique C ⟨hC, Finset.Subset.refl _⟩).trans (unique B ⟨hB, sub⟩).symm)
  · intro hC
    rcases Finset.mem_insert.mp hC with rfl | hC
    · exact hB
    · rcases Finset.mem_filter.mp hC with ⟨hCS, uncovered⟩
      rcases Finset.mem_powersetCard.mp hCS with ⟨subS, cardC⟩
      obtain ⟨D, ⟨hD, subD⟩, _⟩ := H.existsUnique_multiTrace_containing_pair S unit subS cardC
      rcases otherPairs D hD with eq | cardD
      · exact False.elim (uncovered (eq ▸ subD))
      · have eq : C = D := Finset.eq_of_subset_of_card_le subD (by rw [cardD, cardC])
        exact eq.symm ▸ hD

/-- A block containing the whole lock set leaves no room for another block. -/
theorem multiTraces_eq_singleton_of_full_block (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) (full : S ∈ H.multiTraces S) :
    H.multiTraces S = {S} := by
  ext B
  constructor
  · intro hB
    apply Finset.mem_singleton.mpr
    by_contra hne
    have inter := H.multiTraces_inter_card_le_one S unit hB full hne
    rw [Finset.inter_eq_left.mpr (H.multiTraces_subset S hB)] at inter
    have large := ((H.mem_multiTraces S B).mp hB).2
    omega
  · intro hB
    simpa only [Finset.mem_singleton.mp hB] using full

/-- Analytic K4 classification, with exact pair completion and no block enumeration. -/
theorem classify_four_lock_traces (H : Simple5Hypergraph V) (S : Finset V)
    (unit : H.UnitCodegrees S) (four : S.card = 4) :
    H.multiTraces S = S.powersetCard 2 ∨
    (∃ B ⊆ S, B.card = 3 ∧
      H.multiTraces S = insert B ((S.powersetCard 2).filter fun P => ¬ P ⊆ B)) ∨
    H.multiTraces S = {S} := by
  by_cases full : S ∈ H.multiTraces S
  · exact Or.inr (Or.inr (H.multiTraces_eq_singleton_of_full_block S unit full))
  · have small : ∀ B ∈ H.multiTraces S, B.card ≤ 3 := by
      intro B hB
      have sub := H.multiTraces_subset S hB
      have upper := Finset.card_le_card sub
      rw [four] at upper
      by_contra hlarge
      have eq : B = S := Finset.eq_of_subset_of_card_le sub (by rw [four]; omega)
      exact full (eq ▸ hB)
    by_cases triple : ∃ B ∈ H.multiTraces S, B.card = 3
    · obtain ⟨B, hB, three⟩ := triple
      have others : ∀ C ∈ H.multiTraces S, C = B ∨ C.card = 2 := by
        intro C hC
        by_cases eq : C = B
        · exact Or.inl eq
        · apply Or.inr
          have inter := H.multiTraces_inter_card_le_one S unit hC hB eq
          have total := Finset.card_union_add_card_inter C B
          have unionSmall : (C ∪ B).card ≤ 4 := by
            rw [← four]
            exact Finset.card_le_card (Finset.union_subset
              (H.multiTraces_subset S hC) (H.multiTraces_subset S hB))
          have lower := ((H.mem_multiTraces S C).mp hC).2
          omega
      exact Or.inr (Or.inl ⟨B, H.multiTraces_subset S hB, three,
        H.multiTraces_eq_one_large_block S unit hB others⟩)
    · apply Or.inl
      apply H.multiTraces_eq_pairs S unit
      intro B hB
      have lower := ((H.mem_multiTraces S B).mp hB).2
      have upper := small B hB
      have notThree : B.card ≠ 3 := fun h => triple ⟨B, hB, h⟩
      omega

/-- Restricting an actual edge to a deleted lock set commutes with deletion. -/
theorem trace_erase (e S : Finset V) (u : V) :
    e ∩ S.erase u = (e ∩ S).erase u := by
  ext x
  simp only [Finset.mem_inter, Finset.mem_erase]
  tauto

/-- Actual block deletion is exactly the operation used by the avoidance theorem. -/
theorem multiTraces_erase (H : Simple5Hypergraph V) (S : Finset V) (u : V) :
    H.multiTraces (S.erase u) = Avoidance.restrictBlocks (H.multiTraces S) u := by
  ext B
  constructor
  · intro hB
    obtain ⟨⟨e, he, ht⟩, large⟩ := (H.mem_multiTraces (S.erase u) B).mp hB
    have eraseEq : (e ∩ S).erase u = B := (trace_erase e S u).symm.trans ht
    have largeOrig : 2 ≤ (e ∩ S).card :=
      (eraseEq.symm ▸ large).trans Finset.card_erase_le
    apply Finset.mem_filter.mpr
    refine ⟨?_, large⟩
    exact Finset.mem_image.mpr ⟨e ∩ S,
      (H.mem_multiTraces S _).mpr ⟨⟨e, he, rfl⟩, largeOrig⟩, eraseEq⟩
  · intro hB
    rcases Finset.mem_filter.mp hB with ⟨hi, large⟩
    obtain ⟨C, hC, hCB⟩ := Finset.mem_image.mp hi
    obtain ⟨⟨e, he, ht⟩, _⟩ := (H.mem_multiTraces S C).mp hC
    apply (H.mem_multiTraces (S.erase u) B).mpr
    exact ⟨⟨e, he, (trace_erase e S u).trans ((congrArg (fun T => T.erase u) ht).trans hCB)⟩,
      large⟩

/-- Six actual locks at v=25 avoid even the weaker exceptional two-triple shape. -/
theorem exists_six_good_locks [Fintype V] (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices25 : Fintype.card V = 25) :
    ∃ S : Finset V, S.card = 6 ∧ (∀ x ∈ S, H.degree x = 6) ∧
      H.UnitCodegrees S ∧ ¬ Avoidance.TwoTripleShape (H.multiTraces S) := by
  obtain ⟨W, seven, degrees, unit⟩ := H.exists_seven_six_degree_codegree_one cover edges32 vertices25
  obtain ⟨u, hu, good⟩ := Avoidance.exists_deletion_not_two_triple_shape
    W (H.multiTraces W) seven (fun _ hB => H.multiTraces_subset W hB)
    (fun _ hB => H.multiTraces_card_le_five W hB)
  refine ⟨W.erase u, ?_, ?_, ?_, ?_⟩
  · rw [Finset.card_erase_of_mem hu, seven]
  · intro x hx
    exact degrees x (Finset.mem_of_mem_erase hx)
  · intro x hx y hy hne
    exact unit x (Finset.mem_of_mem_erase hx) y (Finset.mem_of_mem_erase hy) hne
  · rwa [H.multiTraces_erase]

end Aris4Math.Simple5Hypergraph

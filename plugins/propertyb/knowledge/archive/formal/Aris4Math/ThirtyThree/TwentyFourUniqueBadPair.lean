import Aris4Math.LowDegree
import Aris4Math.LinkDeletion

/-! The actual unique bad link pair of a degree-six vertex on 24 vertices.
The two three-element arms are extracted from original edges, not supplied as
additional profile data. No edge-count assumption is needed for this lemma. -/

open scoped BigOperators

namespace Aris4Math.ThirtyThree.TwentyFourUniqueBadPair

variable {V : Type*} [Fintype V] [DecidableEq V]

theorem exists_unique_bad_partner (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices24 : Fintype.card V = 24)
    {x : V} (degree6 : H.degree x = 6) :
    ∃ z, z ≠ x ∧ H.codegree x z = 2 ∧
      ∀ y, y ≠ x → y ≠ z → H.codegree x y = 1 := by
  have total : (∑ y ∈ Finset.univ.erase x, (H.codegree x y - 1)) = 1 := by
    rw [H.sum_codegree_excess cover x, degree6, vertices24]
  obtain ⟨z, hz, positive⟩ := Finset.sum_pos_iff.mp (show
      0 < ∑ y ∈ Finset.univ.erase x, (H.codegree x y - 1) by omega)
  have zne : z ≠ x := (Finset.mem_erase.mp hz).1
  have upper := Finset.single_le_sum
    (f := fun y => H.codegree x y - 1) (fun y _ => Nat.zero_le _) hz
  change H.codegree x z - 1 ≤ ∑ y ∈ Finset.univ.erase x, (H.codegree x y - 1) at upper
  rw [total] at upper
  have ztwo : H.codegree x z = 2 := by omega
  have zbad : z ∈ H.badPartners x := Finset.mem_filter.mpr ⟨hz, by omega⟩
  have atMost := H.badPartners_card_le_one_of_twenty_four cover vertices24 degree6
  refine ⟨z, zne, ztwo, ?_⟩
  intro y yne yz
  have lower := H.one_le_codegree cover yne.symm
  by_contra hone
  have ybad : y ∈ H.badPartners x := Finset.mem_filter.mpr
    ⟨Finset.mem_erase.mpr ⟨yne, Finset.mem_univ y⟩, by omega⟩
  exact yz (Finset.card_le_one.mp atMost y ybad z zbad)

theorem exists_unique_bad_pair (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices24 : Fintype.card V = 24)
    {x : V} (degree6 : H.degree x = 6) :
    ∃ z E F, z ≠ x ∧ H.codegree x z = 2 ∧ E ∈ H.edges ∧ F ∈ H.edges ∧
      E ≠ F ∧ E ∩ F = {x,z} ∧ H.badLinkPairs x = {{E,F}} := by
  obtain ⟨z, zne, ztwo, others⟩ :=
    exists_unique_bad_partner H cover vertices24 degree6
  obtain ⟨E, F, ef, pair⟩ := Finset.card_eq_two.mp ztwo
  have memE : E ∈ H.edges ∧ x ∈ E ∧ z ∈ E := by
    apply Finset.mem_filter.mp
    rw [pair]
    exact Finset.mem_insert_self _ _
  have memF : F ∈ H.edges ∧ x ∈ F ∧ z ∈ F := by
    apply Finset.mem_filter.mp
    rw [pair]
    exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
  have inter : E ∩ F = {x,z} := by
    ext y
    constructor
    · intro hy
      obtain ⟨ye, yf⟩ := Finset.mem_inter.mp hy
      by_cases yx : y = x
      · simp [yx]
      by_cases yz : y = z
      · simp [yz]
      exact (ef (H.edge_unique_of_codegree_one (others y yx yz)
        memE.1 memF.1 memE.2.1 ye memF.2.1 yf)).elim
    · intro hy
      rcases Finset.mem_insert.mp hy with h | h
      · subst y
        exact Finset.mem_inter.mpr ⟨memE.2.1, memF.2.1⟩
      · have h := Finset.mem_singleton.mp h
        subst y
        exact Finset.mem_inter.mpr ⟨memE.2.2, memF.2.2⟩
  have pairBad : ({E,F} : Finset (Finset V)) ∈ H.badLinkPairs x := by
    apply Finset.mem_filter.mpr
    constructor
    · apply Finset.mem_powersetCard.mpr
      constructor
      · intro e he
        rcases Finset.mem_insert.mp he with h | h
        · subst e
          exact Finset.mem_filter.mpr ⟨memE.1, memE.2.1⟩
        · have h := Finset.mem_singleton.mp h
          subst e
          exact Finset.mem_filter.mpr ⟨memF.1, memF.2.1⟩
      · simp [ef]
    · refine ⟨z, ?_⟩
      simp [LinkCounting.commonWithin, zne, memE.2.2, memF.2.2]
  have onlyPair : ∀ p ∈ H.badLinkPairs x, p = {E,F} := by
    intro p hp
    have pc := LinkDeletion.badPair_card H x p hp
    have ps := LinkDeletion.badPair_subset H x p hp
    obtain ⟨y, hy⟩ := (Finset.mem_filter.mp hp).2
    have ydata : y ≠ x ∧ ∀ e ∈ p, y ∈ e := by
      simpa [LinkCounting.commonWithin] using hy
    have suby : p ⊆ H.edges.filter (fun e => x ∈ e ∧ y ∈ e) := by
      intro e he
      have hx := Finset.mem_filter.mp (ps he)
      exact Finset.mem_filter.mpr ⟨hx.1, hx.2, ydata.2 e he⟩
    have cy : 2 ≤ H.codegree x y := by
      have h := Finset.card_le_card suby
      simpa [pc, Simple5Hypergraph.codegree] using h
    have yz : y = z := by
      by_contra h
      have h1 := others y ydata.1 h
      omega
    have sub : p ⊆ {E,F} := by simpa [yz, pair] using suby
    exact Finset.eq_of_subset_of_card_le sub (by simp [pc, ef])
  refine ⟨z, E, F, zne, ztwo, memE.1, memF.1, ef, inter, ?_⟩
  ext p
  simp only [Finset.mem_singleton]
  exact ⟨onlyPair p, fun h => h ▸ pairBad⟩

theorem exists_unique_bad_pair_arms (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices24 : Fintype.card V = 24)
    {x : V} (degree6 : H.degree x = 6) :
    ∃ z E F A B, z ≠ x ∧ H.codegree x z = 2 ∧ E ∈ H.edges ∧ F ∈ H.edges ∧
      E ≠ F ∧ E ∩ F = {x,z} ∧ H.badLinkPairs x = {{E,F}} ∧
      A = E \ {x,z} ∧ B = F \ {x,z} ∧ A.card = 3 ∧ B.card = 3 ∧
      Disjoint A B ∧ E = {x,z} ∪ A ∧ F = {x,z} ∪ B := by
  obtain ⟨z,E,F,zne,ztwo,he,hf,ef,inter,bad⟩ :=
    exists_unique_bad_pair H cover vertices24 degree6
  have subE : ({x,z} : Finset V) ⊆ E := by rw [← inter]; exact Finset.inter_subset_left
  have subF : ({x,z} : Finset V) ⊆ F := by rw [← inter]; exact Finset.inter_subset_right
  have paircard : ({x,z} : Finset V).card = 2 := by simp [Ne.symm zne]
  refine ⟨z,E,F,E \ {x,z},F \ {x,z},zne,ztwo,he,hf,ef,inter,bad,rfl,rfl,?_,?_,?_,?_,?_⟩
  · rw [Finset.card_sdiff_of_subset subE, H.five_uniform E he, paircard]
  · rw [Finset.card_sdiff_of_subset subF, H.five_uniform F hf, paircard]
  · apply Finset.disjoint_left.mpr
    intro y ha hb
    have yin : y ∈ E ∩ F := Finset.mem_inter.mpr
      ⟨(Finset.mem_sdiff.mp ha).1, (Finset.mem_sdiff.mp hb).1⟩
    exact (Finset.mem_sdiff.mp ha).2 (inter ▸ yin)
  · exact (Finset.union_sdiff_of_subset subE).symm
  · exact (Finset.union_sdiff_of_subset subF).symm

end Aris4Math.ThirtyThree.TwentyFourUniqueBadPair

#print axioms Aris4Math.ThirtyThree.TwentyFourUniqueBadPair.exists_unique_bad_pair_arms

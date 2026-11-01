import Aris4Math.General.Structure.Definitions
import Aris4Math.General.RS.Lift
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! The uncovered-pair quotient for arbitrary uniformity and edge budgets.
Pair covering is derived from an arbitrary original counterexample. -/
namespace Aris4Math.General.RS

open scoped BigOperators
universe u v

noncomputable def pushEdges {V : Type u} {W : Type v}
    (E : Finset (Finset V)) (f : V → W) : Finset (Finset W) := by
  classical
  exact E.image (fun e => e.image f)

theorem pushEdges_card_le {V : Type u} {W : Type v}
    (E : Finset (Finset V)) (f : V → W) : (pushEdges E f).card ≤ E.card := by
  classical
  exact Finset.card_image_le

theorem uniform_pushEdges {V : Type u} {W : Type v}
    (E : Finset (Finset V)) {k : ℕ} (hU : Uniform E k) (f : V → W)
    (hinj : ∀ e ∈ E, Set.InjOn f (e : Set V)) : Uniform (pushEdges E f) k := by
  classical
  intro e he
  obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp he
  rw [Finset.card_image_of_injOn (hinj a ha)]
  exact hU a ha

theorem propertyB_of_pushEdges {V : Type u} {W : Type v}
    (E : Finset (Finset V)) (f : V → W)
    (hB : PropertyB (pushEdges E f)) : PropertyB E := by
  classical
  obtain ⟨c, hc⟩ := hB
  refine ⟨c ∘ f, ?_⟩
  intro e he
  obtain ⟨⟨x, hx, hcx⟩, ⟨y, hy, hcy⟩⟩ :=
    hc _ (Finset.mem_image.mpr ⟨e, he, rfl⟩)
  obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
  obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
  exact ⟨⟨a, ha, hcx⟩, ⟨b, hb, hcy⟩⟩

noncomputable def mergeVertexGeneral {V : Type u} (x y : V) (hxy : x ≠ y)
    (z : V) : {z : V // z ≠ y} := by
  classical
  exact if hz : z = y then ⟨x, hxy⟩ else ⟨z, hz⟩

theorem mergeVertexGeneral_injOn {V : Type u} (E : Finset (Finset V))
    (x y : V) (hxy : x ≠ y)
    (hnone : ∀ e ∈ E, ¬(x ∈ e ∧ y ∈ e)) :
    ∀ e ∈ E, Set.InjOn (mergeVertexGeneral x y hxy) (e : Set V) := by
  classical
  intro e he a ha b hb hab
  have hval := congrArg Subtype.val hab
  by_cases hay : a = y
  · subst a
    by_cases hby : b = y
    · exact hby.symm
    · have hxb : x = b := by simpa [mergeVertexGeneral, hby] using hval
      exact False.elim (hnone e he ⟨hxb ▸ hb, ha⟩)
  · by_cases hby : b = y
    · subst b
      have hax : a = x := by simpa [mergeVertexGeneral, hay] using hval
      exact False.elim (hnone e he ⟨hax ▸ ha, hb⟩)
    · simpa [mergeVertexGeneral, hay, hby] using hval

/-- No original counterexample hypothesis beyond finite vertices, uniformity
and the edge budget is used to obtain pair coverage. -/
theorem exists_pair_covering_counterexample {V : Type u} [Finite V]
    (E : Finset (Finset V)) {k N : ℕ} (hU : Uniform E k)
    (hM : E.card ≤ N) (hB : ¬ PropertyB E) :
    ∃ n : ℕ, ∃ K : Finset (Finset (Fin n)),
      Uniform K k ∧ K.card ≤ N ∧ ¬ PropertyB K ∧ PairCovering K := by
  classical
  letI := Fintype.ofFinite V
  let P : ℕ → Prop := fun n => ∃ K : Finset (Finset (Fin n)),
    Uniform K k ∧ K.card ≤ N ∧ ¬ PropertyB K
  have hex : ∃ n, P n := by
    let f := Fintype.equivFin V
    refine ⟨Fintype.card V, relabel f E, (uniform_relabel_iff f E k).mpr hU, ?_, ?_⟩
    · simpa using hM
    · exact fun h => hB ((propertyB_relabel_iff f E).mp h)
  obtain ⟨K, hKU, hKM, hKB⟩ := Nat.find_spec hex
  refine ⟨Nat.find hex, K, hKU, hKM, hKB, ?_⟩
  intro x y hxy
  by_contra hnone
  have hnot : ∀ e ∈ K, ¬(x ∈ e ∧ y ∈ e) := by
    intro e he hboth
    exact hnone ⟨e, he, hboth⟩
  let W := {z : Fin (Nat.find hex) // z ≠ y}
  let f := mergeVertexGeneral x y hxy
  let L := pushEdges K f
  have hLU : Uniform L k := uniform_pushEdges K hKU f
    (mergeVertexGeneral_injOn K x y hxy hnot)
  have hLM : L.card ≤ N := (pushEdges_card_le K f).trans hKM
  have hLB : ¬ PropertyB L := fun h => hKB (propertyB_of_pushEdges K f h)
  let g := Fintype.equivFin W
  have hP : P (Fintype.card W) :=
    ⟨relabel g L, (uniform_relabel_iff g L k).mpr hLU,
      by simpa using hLM, fun h => hLB ((propertyB_relabel_iff g L).mp h)⟩
  have hless : Fintype.card W < Nat.find hex := by
    simpa [W] using (Fintype.card_subtype_lt (p := fun z => z ≠ y) (x := y) (by simp))
  exact (not_le_of_gt hless) (Nat.find_min' hex hP)

/-- Counting actual ordered vertex pairs against actual ordered edge pairs. -/
theorem pairCovering_count {n k : ℕ} (K : Finset (Finset (Fin n)))
    (hU : Uniform K k) (hpair : PairCovering K) :
    n * (n - 1) ≤ k * (k - 1) * K.card := by
  classical
  have hsub : (Finset.univ : Finset (Fin n)).offDiag ⊆
      K.biUnion Finset.offDiag := by
    intro p hp
    obtain ⟨e, he, hx, hy⟩ := hpair p.1 p.2 (Finset.mem_offDiag.mp hp).2.2
    exact Finset.mem_biUnion.mpr ⟨e, he,
      Finset.mem_offDiag.mpr ⟨hx, hy, (Finset.mem_offDiag.mp hp).2.2⟩⟩
  have hcount := (Finset.card_le_card hsub).trans Finset.card_biUnion_le
  have heq : (∑ e ∈ K, e.offDiag.card) = K.card * (k * k - k) := by
    calc
      _ = ∑ _e ∈ K, (k * k - k) := by
        apply Finset.sum_congr rfl
        intro e he
        rw [Finset.offDiag_card, hU e he]
      _ = _ := by simp
  rw [heq, Finset.offDiag_card] at hcount
  simpa [Nat.mul_sub_left_distrib, Nat.mul_comm, Nat.mul_left_comm,
    Nat.mul_assoc] using hcount

theorem not_propertyB_card_pos {V : Type u} (E : Finset (Finset V))
    (hB : ¬ PropertyB E) : 0 < E.card := by
  by_contra h
  have hE : E = ∅ := Finset.card_eq_zero.mp (by omega)
  subst E
  exact hB ⟨fun _ => false, by simp [Bichromatic]⟩

theorem uniform_le_vertices_of_not_propertyB {n k : ℕ}
    (K : Finset (Finset (Fin n))) (hU : Uniform K k) (hB : ¬ PropertyB K) : k ≤ n := by
  obtain ⟨e, he⟩ := Finset.card_pos.mp (not_propertyB_card_pos K hB)
  rw [← hU e he]
  exact le_trans (Finset.card_le_univ e) (by simp)

/-- Convenient caller package, including the edge budget version of pair counting. -/
theorem pairCovering_vertex_bound {n k N : ℕ} (K : Finset (Finset (Fin n)))
    (hU : Uniform K k) (hM : K.card ≤ N) (hB : ¬ PropertyB K)
    (hpair : PairCovering K) :
    0 < K.card ∧ k ≤ n ∧ n * (n - 1) ≤ k * (k - 1) * N := by
  exact ⟨not_propertyB_card_pos K hB, uniform_le_vertices_of_not_propertyB K hU hB,
    (pairCovering_count K hU hpair).trans (Nat.mul_le_mul_left _ hM)⟩

end Aris4Math.General.RS

#print axioms Aris4Math.General.RS.exists_pair_covering_counterexample
#print axioms Aris4Math.General.RS.pairCovering_count
#print axioms Aris4Math.General.RS.pairCovering_vertex_bound

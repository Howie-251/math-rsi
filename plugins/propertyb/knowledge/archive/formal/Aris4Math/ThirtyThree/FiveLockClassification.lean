import Aris4Math.ThirtyThree.MultiLockRecovery

/-! Complete labelled large-trace classification on five unit-codegree locks.
Every actual large trace has multiplicity one. Two distinct large traces meet
in at most one lock, so at most two such traces can occur. -/
namespace Aris4Math.ThirtyThree.FiveLockClassification

open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.MultiLockRecovery

variable {v : ℕ}

def actualLarge (H : Simple5Hypergraph (Fin v)) (vertices : Fin 5 ↪ Fin v) :
    Finset (Finset (Fin 5)) :=
  Finset.univ.filter fun T => 3 ≤ T.card ∧ 0 < count H vertices T

theorem actual_count_le_one (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,hij⟩ := Finset.one_lt_card.mp (show 1 < T.card by omega)
  exact (count_le_codegree H vertices T i j hi hj).trans_eq (unit i j hij)

theorem actual_high_indicator (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = if T ∈ actualLarge H vertices then 1 else 0 := by
  have hu := actual_count_le_one H vertices unit T large
  by_cases ht : T ∈ actualLarge H vertices
  · have hp := (Finset.mem_filter.mp ht).2.2
    simp only [if_pos ht]
    omega
  · have hn : ¬ 0 < count H vertices T := by
      intro hp
      exact ht (Finset.mem_filter.mpr ⟨Finset.mem_univ _,large,hp⟩)
    simp only [if_neg ht]
    omega

theorem actual_intersection_le_one (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (T U : Finset (Fin 5)) (hT : T ∈ actualLarge H vertices)
    (hU : U ∈ actualLarge H vertices) (hne : T ≠ U) : (T ∩ U).card ≤ 1 := by
  by_contra large
  obtain ⟨i,hi,j,hj,hij⟩ := Finset.one_lt_card.mp (show 1 < (T ∩ U).card by omega)
  obtain ⟨e,he⟩ := Finset.card_pos.mp ((Finset.mem_filter.mp hT).2.2)
  obtain ⟨f,hf⟩ := Finset.card_pos.mp ((Finset.mem_filter.mp hU).2.2)
  obtain ⟨heH,het⟩ := Finset.mem_filter.mp he
  obtain ⟨hfH,hfu⟩ := Finset.mem_filter.mp hf
  have hie : vertices i ∈ e := (mem_lockSignature vertices e i).mp
    (het.symm ▸ (Finset.mem_inter.mp hi).1)
  have hje : vertices j ∈ e := (mem_lockSignature vertices e j).mp
    (het.symm ▸ (Finset.mem_inter.mp hj).1)
  have hif : vertices i ∈ f := (mem_lockSignature vertices f i).mp
    (hfu.symm ▸ (Finset.mem_inter.mp hi).2)
  have hjf : vertices j ∈ f := (mem_lockSignature vertices f j).mp
    (hfu.symm ▸ (Finset.mem_inter.mp hj).2)
  have hef := H.edges_eq_of_codegree_one (unit i j hij) heH hfH hie hje hif hjf
  exact hne (het.symm.trans ((congrArg (lockSignature vertices) hef).trans hfu))

def Admissible (F : Finset (Finset (Fin 5))) : Prop :=
  (∀ T ∈ F, 3 ≤ T.card) ∧
    (∀ T ∈ F, ∀ U ∈ F, T ≠ U → (T ∩ U).card ≤ 1)

theorem actual_admissible (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) :
    Admissible (actualLarge H vertices) := by
  refine ⟨?_, ?_⟩
  · intro T hT
    exact (Finset.mem_filter.mp hT).2.1
  · intro T hT U hU hne
    exact actual_intersection_le_one H vertices unit T U hT hU hne

/-- Two distinct large traces already cover all five locks; a third trace
meeting both in at most one point would have size at most two. -/
theorem admissible_card_le_two (F : Finset (Finset (Fin 5))) (hF : Admissible F) :
    F.card ≤ 2 := by
  by_contra hc
  obtain ⟨A,B,C,hA,hB,hC,hAB,hAC,hBC⟩ :=
    Finset.two_lt_card_iff.mp (show 2 < F.card by omega)
  have hAc := hF.1 A hA
  have hBc := hF.1 B hB
  have hCc := hF.1 C hC
  have hInt := hF.2 A hA B hB hAB
  have hUnion := Finset.card_union_add_card_inter A B
  have hUpper : (A ∪ B).card ≤ 5 := by simpa using Finset.card_le_univ (A ∪ B)
  have hAll : A ∪ B = Finset.univ :=
    Finset.eq_univ_of_card _ (by simp only [Fintype.card_fin]; omega)
  have hCA : (C ∩ A).card ≤ 1 := hF.2 C hC A hA hAC.symm
  have hCB : (C ∩ B).card ≤ 1 := hF.2 C hC B hB hBC.symm
  have hCupper : C.card ≤ (C ∩ A).card + (C ∩ B).card := by
    calc
      _ = (C ∩ (A ∪ B)).card := by rw [hAll, Finset.inter_univ]
      _ = ((C ∩ A) ∪ (C ∩ B)).card := by rw [Finset.inter_union_distrib_left]
      _ ≤ _ := Finset.card_union_le _ _
  omega

/-- The complete labelled domain: empty family, sixteen single large traces,
and fifteen compatible pairs of triples. -/
def families : Fin 32 → Finset (Finset (Fin 5)) := ![
  ∅,
  {{0,1,2}},
  {{0,1,3}},
  {{0,2,3}},
  {{1,2,3}},
  {{0,1,2,3}},
  {{0,1,4}},
  {{0,2,4}},
  {{1,2,4}},
  {{0,1,2,4}},
  {{0,3,4}},
  {{1,3,4}},
  {{0,1,3,4}},
  {{2,3,4}},
  {{0,2,3,4}},
  {{1,2,3,4}},
  {{0,1,2,3,4}},
  {{0,1,2},{0,3,4}},
  {{0,1,2},{1,3,4}},
  {{0,1,2},{2,3,4}},
  {{0,1,3},{0,2,4}},
  {{0,1,3},{1,2,4}},
  {{0,1,3},{2,3,4}},
  {{0,2,3},{0,1,4}},
  {{0,2,3},{1,2,4}},
  {{0,2,3},{1,3,4}},
  {{1,2,3},{0,1,4}},
  {{1,2,3},{0,2,4}},
  {{1,2,3},{0,3,4}},
  {{0,1,4},{2,3,4}},
  {{0,2,4},{1,3,4}},
  {{1,2,4},{0,3,4}}]

theorem families_admissible : ∀ i, Admissible (families i) := by
  unfold Admissible
  decide +kernel

theorem families_injective : Function.Injective families := by decide +kernel

theorem singleton_complete : ∀ T : Finset (Fin 5), 3 ≤ T.card →
    ∃ i : Fin 32, families i = {T} := by decide +kernel

theorem pair_complete : ∀ T U : Finset (Fin 5), 3 ≤ T.card → 3 ≤ U.card →
    (T ∩ U).card ≤ 1 → ∃ i : Fin 32, families i = {T,U} := by decide +kernel

/-- Coverage uses the analytic cardinality bound before consulting the explicit
single- and double-trace tables. There is no enumeration of hypergraphs. -/
theorem admissible_in_table (F : Finset (Finset (Fin 5))) (hF : Admissible F) :
    ∃ i : Fin 32, families i = F := by
  have hc := admissible_card_le_two F hF
  have cases : F.card = 0 ∨ F.card = 1 ∨ F.card = 2 := by omega
  rcases cases with zero | one | two
  · have he := Finset.card_eq_zero.mp zero
    subst F
    exact ⟨0, rfl⟩
  · obtain ⟨T,rfl⟩ := Finset.card_eq_one.mp one
    exact singleton_complete T (hF.1 T (by simp))
  · obtain ⟨T,U,hne,rfl⟩ := Finset.card_eq_two.mp two
    exact pair_complete T U (hF.1 T (by simp)) (hF.1 U (by simp))
      (hF.2 T (by simp) U (by simp) hne)

def high (i : Fin 32) (T : Finset (Fin 5)) : ℕ :=
  if T ∈ families i then 1 else 0

/-- Every actual large trace, with its true multiplicity, belongs to one of the
32 labelled cases. The table index is produced from H. -/
theorem actual_high_in_table (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) :
    ∃ i : Fin 32, ∀ T, 3 ≤ T.card → count H vertices T = high i T := by
  obtain ⟨i,hi⟩ := admissible_in_table (actualLarge H vertices) (actual_admissible H vertices unit)
  refine ⟨i, ?_⟩
  intro T hT
  rw [high, hi]
  exact actual_high_indicator H vertices unit T hT

/-- The table and low-order actual data recover every actual multiplicity,
including pairs, singleton traces, and the empty trace. -/
theorem actual_recovered_in_table (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 5 ↪ Fin v)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (low : Finset (Fin 5) → ℕ)
    (hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T) :
    ∃ i : Fin 32, ∀ T, count H vertices T = recovered low (high i) T := by
  obtain ⟨i,hi⟩ := actual_high_in_table H vertices unit
  exact ⟨i, actual_recovered H vertices low (high i) hlow hi⟩

end Aris4Math.ThirtyThree.FiveLockClassification

#print axioms Aris4Math.ThirtyThree.FiveLockClassification.actual_admissible
#print axioms Aris4Math.ThirtyThree.FiveLockClassification.admissible_card_le_two

#print axioms Aris4Math.ThirtyThree.FiveLockClassification.actual_recovered_in_table

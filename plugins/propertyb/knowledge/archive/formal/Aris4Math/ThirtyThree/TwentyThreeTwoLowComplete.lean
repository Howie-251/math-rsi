import Aris4Math.ThirtyThree.TwentyThreeTwoLow
import Aris4Math.ThirtyThree.TwentyThreeTwoLowCatalog
import Aris4Math.ThirtyThree.TwentyThreeSelection
import Aris4Math.ThirtyThree.TwentyThreeHighPair

namespace Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeTwoLowHighCatalog (pairDegree Admissible)
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_card largeTypes_injective
  largeTypes_complete highValue pairSum)
open TwentyThreeTwoLowData TwentyThreeTwoLowFacts
open TwentyThreeTwoLowCatalog (degreeData)

private theorem large_has_unit_pair : ∀ T : Finset (Fin 5), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ ({i,j} : Finset (Fin 5)) ≠ {0,1} ∧
      ({i,j} : Finset (Fin 5)) ≠ {2,3} := by decide +kernel

theorem large_count_le_one (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,not01,not23⟩ := large_has_unit_pair T large
  have unit : pairDegree a b i j = 1 := by simp [pairDegree,not01,not23]
  have bound := count_le_codegree H vertices T i j hi hj
  simpa only [pairs i j ij,unit] using bound

def actualBits (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) :
    Fin 16 → Bool := fun a => decide (count H vertices (largeTypes a) = 1)

theorem actual_bit_count (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (t : Fin 16) :
    (if actualBits H vertices t then 1 else 0) = count H vertices (largeTypes t) := by
  have bound := large_count_le_one H vertices a b pairs (largeTypes t) (largeTypes_card t)
  by_cases hc : count H vertices (largeTypes t) = 1
  · simp [actualBits,hc]
  · have hz : count H vertices (largeTypes t) = 0 := by omega
    simp [actualBits,hz]

theorem highValue_at (h : Fin 16 → Bool) (a : Fin 16) :
    highValue h (largeTypes a) = if h a then 1 else 0 := by
  have eq : (∃ b : Fin 16, largeTypes b = largeTypes a ∧ h b = true) ↔ h a = true := by
    constructor
    · rintro ⟨b,eq,hb⟩
      have ba := largeTypes_injective eq
      simpa only [ba] using hb
    · intro ha
      exact ⟨a,rfl,ha⟩
  simp only [highValue,eq]

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualBits H vertices) T := by
  obtain ⟨t,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  exact (actual_bit_count H vertices a b pairs t).symm

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (a b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j) :
    Admissible a b (actualBits H vertices) := by
  intro i j ij
  let indices := Finset.univ.filter fun a : Fin 16 => i ∈ largeTypes a ∧ j ∈ largeTypes a
  have image : indices.image largeTypes = supers {i,j} 3 := by
    ext T
    simp only [Finset.mem_image,indices,Finset.mem_filter,Finset.mem_univ,true_and,supers]
    constructor
    · rintro ⟨a,⟨hi,hj⟩,rfl⟩
      exact ⟨by simp only [Finset.insert_subset_iff,Finset.singleton_subset_iff]; exact ⟨hi,hj⟩,
        largeTypes_card a⟩
    · rintro ⟨sub,large⟩
      obtain ⟨a,rfl⟩ := largeTypes_complete T large
      exact ⟨a,⟨sub (by simp),sub (by simp)⟩,rfl⟩
  have sum_eq : pairSum (actualBits H vertices) i j =
      ∑ T ∈ supers {i,j} 3, count H vertices T := by
    unfold pairSum
    simp_rw [actual_bit_count H vertices a b pairs]
    rw [← Finset.sum_filter]
    change (∑ a ∈ indices, count H vertices (largeTypes a)) = _
    rw [← image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

/-- Relabeling the five locks preserves each actual multiplicity after the
corresponding image of its label subset. -/
theorem count_relabel (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (σ : Fin 5 ≃ Fin 5) (T : Finset (Fin 5)) :
    count H (σ.toEmbedding.trans vertices) T = count H vertices (T.image σ) := by
  have sig (e : Finset (Fin 23)) :
      (lockSignature (σ.toEmbedding.trans vertices) e).image σ = lockSignature vertices e := by
    ext j
    constructor
    · intro hj
      obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hj
      exact (mem_lockSignature vertices e (σ i)).mpr
        ((mem_lockSignature (σ.toEmbedding.trans vertices) e i).mp hi)
    · intro hj
      apply Finset.mem_image.mpr
      refine ⟨σ.symm j,?_,σ.apply_symm_apply j⟩
      apply (mem_lockSignature (σ.toEmbedding.trans vertices) e (σ.symm j)).mpr
      simpa using (mem_lockSignature vertices e j).mp hj
  unfold count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  constructor
  · intro hs
    exact (sig e).symm.trans (congrArg (fun S : Finset (Fin 5) => S.image σ) hs)
  · intro hs
    apply Finset.image_injective σ.injective
    exact (sig e).trans hs


theorem propertyB_of_large (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 23) (c : Case)
    (degrees : ∀ i, H.degree (vertices i) = degreeData i)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) =
      pairDegree ((params c).1.val+1) ((params c).2.val+1) i j)
    (large : ∀ T, 3 ≤ T.card → count H vertices T = counts c T) : PropertyB H := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low c T := by
    apply upper_eq_of_low_data
    · simp [low,edges33]
    · intro i
      rw [degrees]
      fin_cases i <;> simp [low,degreeData]
    · intro i j ij
      rw [pairs i j ij]
      simp [low,pairDegree,ij]
  apply TwentyThreeTwoLow.propertyB_of_counts H vertices c
  intro T
  exact (actual_recovered H vertices (low c) (counts c) hlow large T).trans
    (recovery_formula c T)

theorem propertyB_of_structured_locks (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 23) (a b : ℕ)
    (ha : 1 ≤ a ∧ a ≤ 3) (hb : 1 ≤ b ∧ b ≤ 3)
    (degrees : ∀ i, H.degree (vertices i) = degreeData i)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j) :
    PropertyB H := by
  obtain ⟨c,σ,ca,cb,degreePreserve,preserve,large⟩ := TwentyThreeTwoLowCatalog.classify a b
    (actualBits H vertices) ha hb (actual_admissible H vertices a b pairs)
  let newVertices := σ.toEmbedding.trans vertices
  apply propertyB_of_large H edges33 newVertices c
  · intro i
    change H.degree (vertices (σ i)) = _
    rw [degrees,degreePreserve]
  · intro i j ij
    change H.codegree (vertices (σ i)) (vertices (σ j)) = _
    rw [pairs (σ i) (σ j) (σ.injective.ne ij),preserve,ca,cb]
  · intro T hT
    rw [show newVertices = σ.toEmbedding.trans vertices from rfl,count_relabel]
    rw [actual_high_value H vertices a b pairs (T.image σ)
      (by simpa only [Finset.card_image_of_injective _ σ.injective] using hT)]
    exact large T hT

private theorem ordered_pair01 : ∀ i j : Fin 5, i < j →
    (({i,j} : Finset (Fin 5)) = {0,1} ↔ i = 0 ∧ j = 1) := by decide +kernel
private theorem ordered_pair23 : ∀ i j : Fin 5, i < j →
    (({i,j} : Finset (Fin 5)) = {2,3} ↔ i = 2 ∧ j = 3) := by decide +kernel

theorem propertyB_of_two_sixes (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count2 : H.sixVertices.card = 2) : PropertyB H := by
  obtain ⟨f,inj,degrees,unit⟩ :=
    TwentyThreeSelection.exists_two_sixes_three_sevens_of_count H cover edges33
      (Fintype.card_fin 23) count2
  let vertices : Fin 5 ↪ Fin 23 := ⟨f,inj⟩
  have h01 : f 0 ≠ f 1 := inj.ne (by decide)
  have h23 : f 2 ≠ f 3 := inj.ne (by decide)
  have d0 : H.degree (f 0) = 6 := by simpa using degrees 0
  have d2 : H.degree (f 2) = 7 := by simpa using degrees 2
  have d3 : H.degree (f 3) = 7 := by simpa using degrees 3
  by_cases high : 4 ≤ H.codegree (f 2) (f 3)
  · exact TwentyThreeHighPair.propertyB_of_high_pair H edges33 (f 2) (f 3) h23 d2 d3 high
  let a := H.codegree (f 0) (f 1)
  let b := H.codegree (f 2) (f 3)
  have ha : 1 ≤ a ∧ a ≤ 3 := ⟨H.one_le_codegree cover h01,
    TwentyThreeSelection.six_codegree_le_three H cover (Fintype.card_fin 23) d0 h01⟩
  have hb : 1 ≤ b ∧ b ≤ 3 := ⟨H.one_le_codegree cover h23,by dsimp [b]; omega⟩
  have ordered : ∀ i j : Fin 5, i < j →
      H.codegree (f i) (f j) = pairDegree a b i j := by
    intro i j hij
    by_cases h01 : i = 0 ∧ j = 1
    · obtain ⟨rfl,rfl⟩ := h01
      rfl
    by_cases h23 : i = 2 ∧ j = 3
    · obtain ⟨rfl,rfl⟩ := h23
      rfl
    rw [unit i j hij h01 h23]
    have n01 := mt (ordered_pair01 i j hij).mp h01
    have n23 := mt (ordered_pair23 i j hij).mp h23
    simp [pairDegree,n01,n23]
  have pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree a b i j := by
    intro i j ij
    rcases lt_or_gt_of_ne ij with lt | gt
    · exact ordered i j lt
    · change H.codegree (f i) (f j) = _
      rw [H.codegree_comm,ordered j i gt]
      simp only [pairDegree,Finset.pair_comm j i]
  exact propertyB_of_structured_locks H edges33 vertices a b ha hb degrees pairs

end Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete
#print axioms Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete.propertyB_of_two_sixes

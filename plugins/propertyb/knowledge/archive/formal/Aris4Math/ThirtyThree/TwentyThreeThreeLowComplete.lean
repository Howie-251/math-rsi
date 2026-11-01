import Aris4Math.ThirtyThree.TwentyThreeThreeLow
import Aris4Math.ThirtyThree.TwentyThreeThreeLowCatalog
import Aris4Math.ThirtyThree.TwentyThreeSelection
import Aris4Math.ThirtyThree.TwentyThreeHighPair

namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_card largeTypes_injective largeTypes_complete)
open TwentyThreeThreeLowHighCatalog TwentyThreeThreeLowData TwentyThreeThreeLowFacts
open TwentyThreeThreeLowCatalog (degreeData)

def actualHigh (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23) :
    Fin 16 → ℕ := fun t => count H vertices (largeTypes t)

theorem highValue_at (h : Fin 16 → ℕ) (t : Fin 16) : highValue h (largeTypes t) = h t := by
  simp [highValue,largeTypes_injective.eq_iff]

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (T : Finset (Fin 5)) (large : 3 ≤ T.card) :
    count H vertices T = highValue (actualHigh H vertices) T := by
  obtain ⟨t,rfl⟩ := largeTypes_complete T large
  rw [highValue_at]
  rfl

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j) :
    Admissible e b (actualHigh H vertices) := by
  intro i j ij
  let indices := Finset.univ.filter fun t : Fin 16 => i ∈ largeTypes t ∧ j ∈ largeTypes t
  have image : indices.image largeTypes = supers {i,j} 3 := by
    ext T
    simp only [Finset.mem_image,indices,Finset.mem_filter,Finset.mem_univ,true_and,supers]
    constructor
    · rintro ⟨t,⟨hi,hj⟩,rfl⟩
      exact ⟨by simp only [Finset.insert_subset_iff,Finset.singleton_subset_iff]; exact ⟨hi,hj⟩,
        largeTypes_card t⟩
    · rintro ⟨sub,large⟩
      obtain ⟨t,rfl⟩ := largeTypes_complete T large
      exact ⟨t,⟨sub (by simp),sub (by simp)⟩,rfl⟩
  have sum_eq : pairSum (actualHigh H vertices) i j =
      ∑ T ∈ supers {i,j} 3, count H vertices T := by
    unfold pairSum actualHigh
    rw [← Finset.sum_filter]
    change (∑ t ∈ indices, count H vertices (largeTypes t)) = _
    rw [← image,Finset.sum_image]
    intro a _ b _ eq
    exact largeTypes_injective eq
  rw [sum_eq]
  exact (high_pair_budget H vertices i j ij).trans_eq (pairs i j ij)

private theorem large_has_unit_pair : ∀ t : Fin 16, t ≠ 0 →
    ∃ i ∈ largeTypes t, ∃ j ∈ largeTypes t, i ≠ j ∧
      ({i,j} : Finset (Fin 5)) ≠ {0,1} ∧ ({i,j} : Finset (Fin 5)) ≠ {0,2} ∧
      ({i,j} : Finset (Fin 5)) ≠ {1,2} ∧ ({i,j} : Finset (Fin 5)) ≠ {3,4} := by decide +kernel

theorem actual_rest (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j)
    (t : Fin 16) (ht : t ≠ 0) : actualHigh H vertices t ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,n01,n02,n12,n34⟩ := large_has_unit_pair t ht
  have bound := count_le_codegree H vertices (largeTypes t) i j hi hj
  simpa only [pairs i j ij,pairDegree,if_neg n01,if_neg n02,if_neg n12,if_neg n34]
    using bound

theorem actual_first (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 5 ↪ Fin 23)
    (e : Fin 3 → ℕ) (b : ℕ) (he : e 0+e 1 ≤ 2)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j) :
    actualHigh H vertices 0 ≤ 2 := by
  have h01 := count_le_codegree H vertices (largeTypes 0) 0 1 (by decide) (by decide)
  have h02 := count_le_codegree H vertices (largeTypes 0) 0 2 (by decide) (by decide)
  rw [pairs 0 1 (by decide)] at h01
  rw [pairs 0 2 (by decide)] at h02
  have p01 : pairDegree e b 0 1 = e 0+1 := by rfl
  have p02 : pairDegree e b 0 2 = e 1+1 := by rfl
  rw [p01] at h01
  rw [p02] at h02
  unfold actualHigh
  omega

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
      pairDegree (lowExcess c) (highCodegree c) i j)
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
  apply TwentyThreeThreeLow.propertyB_of_counts H vertices c
  intro T
  exact (actual_recovered H vertices (low c) (counts c) hlow large T).trans
    (recovery_formula c T)

theorem propertyB_of_structured_locks (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 23) (e : Fin 3 → ℕ) (b : ℕ)
    (he : ∀ i, e i ≤ 2)
    (h01 : e 0+e 1 ≤ 2) (h02 : e 0+e 2 ≤ 2) (h12 : e 1+e 2 ≤ 2)
    (hb : 1 ≤ b ∧ b ≤ 3)
    (degrees : ∀ i, H.degree (vertices i) = degreeData i)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j) :
    PropertyB H := by
  obtain ⟨c,σ,degreePreserve,preserve,large⟩ := TwentyThreeThreeLowCatalog.classify e b
    (actualHigh H vertices) he h01 h02 h12 hb (actual_first H vertices e b h01 pairs)
    (actual_rest H vertices e b pairs) (actual_admissible H vertices e b pairs)
  let newVertices := σ.toEmbedding.trans vertices
  apply propertyB_of_large H edges33 newVertices c
  · intro i
    change H.degree (vertices (σ i)) = _
    rw [degrees,degreePreserve]
  · intro i j ij
    change H.codegree (vertices (σ i)) (vertices (σ j)) = _
    rw [pairs (σ i) (σ j) (σ.injective.ne ij),preserve]
  · intro T hT
    rw [show newVertices = σ.toEmbedding.trans vertices from rfl,count_relabel]
    rw [actual_high_value H vertices (T.image σ)
      (by simpa only [Finset.card_image_of_injective _ σ.injective] using hT)]
    exact large T hT

theorem propertyB_of_three_sixes (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (count3 : H.sixVertices.card = 3) : PropertyB H := by
  obtain ⟨f,inj,degrees,unit⟩ :=
    TwentyThreeSelection.exists_three_sixes_two_sevens_of_count H cover edges33
      (Fintype.card_fin 23) count3
  let vertices : Fin 5 ↪ Fin 23 := ⟨f,inj⟩
  have distinct (i j : Fin 5) (ij : i ≠ j) : f i ≠ f j := inj.ne ij
  have positive (i j : Fin 5) (ij : i ≠ j) : 1 ≤ H.codegree (f i) (f j) :=
    H.one_le_codegree cover (distinct i j ij)
  have d3 : H.degree (f 3) = 7 := by simpa using degrees 3
  have d4 : H.degree (f 4) = 7 := by simpa using degrees 4
  by_cases high : 4 ≤ H.codegree (f 3) (f 4)
  · exact TwentyThreeHighPair.propertyB_of_high_pair H edges33 (f 3) (f 4)
      (distinct 3 4 (by decide)) d3 d4 high
  let e : Fin 3 → ℕ := ![H.codegree (f 0) (f 1)-1,
    H.codegree (f 0) (f 2)-1,H.codegree (f 1) (f 2)-1]
  let b := H.codegree (f 3) (f 4)
  have hb : 1 ≤ b ∧ b ≤ 3 := ⟨positive 3 4 (by decide),by dsimp [b]; omega⟩
  have row (i j k : Fin 5) (hi : i.val < 3) (ij : i ≠ j) (ik : i ≠ k) (jk : j ≠ k) :
      (H.codegree (f i) (f j)-1)+(H.codegree (f i) (f k)-1) ≤ 2 := by
    have di : H.degree (f i) = 6 := by rw [degrees,if_pos hi]
    have h := TwentyThreeSelection.six_subset_excess_le_two H cover
      (Fintype.card_fin 23) di {f j,f k}
      (by simp [distinct i j ij,distinct i k ik])
    simpa only [Finset.sum_pair (distinct j k jk)] using h
  have h01 : e 0+e 1 ≤ 2 := row 0 1 2 (by decide) (by decide) (by decide) (by decide)
  have h02 : e 0+e 2 ≤ 2 := by
    have h := row 1 0 2 (by decide) (by decide) (by decide) (by decide)
    rw [H.codegree_comm (f 1) (f 0)] at h
    exact h
  have h12 : e 1+e 2 ≤ 2 := by
    have h := row 2 0 1 (by decide) (by decide) (by decide) (by decide)
    rw [H.codegree_comm (f 2) (f 0),H.codegree_comm (f 2) (f 1)] at h
    exact h
  have he : ∀ i, e i ≤ 2 := by
    intro i
    fin_cases i
    · change e 0 ≤ 2
      omega
    · change e 1 ≤ 2
      omega
    · change e 2 ≤ 2
      omega
  have add01 := Nat.sub_add_cancel (positive 0 1 (by decide))
  have add02 := Nat.sub_add_cancel (positive 0 2 (by decide))
  have add12 := Nat.sub_add_cancel (positive 1 2 (by decide))
  have ordered : ∀ i j : Fin 5, i < j →
      H.codegree (f i) (f j) = pairDegree e b i j := by
    intro i j ij
    fin_cases i <;> fin_cases j <;> simp only [Fin.lt_def] at ij <;> norm_num at ij
    all_goals first | exact add01.symm | exact add02.symm | exact add12.symm |
      exact unit _ _ (by decide) (by decide) | rfl
  have pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e b i j := by
    intro i j ij
    rcases lt_or_gt_of_ne ij with lt | gt
    · exact ordered i j lt
    · change H.codegree (f i) (f j) = _
      rw [H.codegree_comm,ordered j i gt]
      simp only [pairDegree,Finset.pair_comm j i]
  exact propertyB_of_structured_locks H edges33 vertices e b he h01 h02 h12 hb degrees pairs

end Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete.propertyB_of_structured_locks

#print axioms Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete.propertyB_of_three_sixes

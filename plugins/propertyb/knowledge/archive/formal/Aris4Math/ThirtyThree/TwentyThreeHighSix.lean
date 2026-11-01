import Aris4Math.ThirtyThree.TwentyThreeHighSixCatalog
import Aris4Math.ThirtyThree.TwentyThreeClusterSelection

/-! Actual six-lock matching inputs with a genuine trace of size at least four. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighSix
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeHighSixData TwentyThreeHighSixCatalog

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (k : Fin 22)
    (actual : ∀ T, count H vertices T = counts k T) : PropertyB H := by
  obtain ⟨valid,bare⟩ := certificates k
  have real := TwentyThreeHighSixProfiles.realizes_profile H vertices (positions k) (counts k) actual
    (centers k) (by simpa only [←p_eq] using valid)
  rw [←p_eq] at real
  by_cases hk : k=0
  · subst k
    obtain ⟨strict,bounds⟩ := refined_certificate
    apply RefinedDeletion.propertyB_of_refined_deletion H vertices (positions 0) (p 0) real rfl
      loss avoided multipliers quotas
    · intro j _; exact (bounds j).1
    · intro j _; exact (bounds j).2.1
    · intro j _; exact (bounds j).2.2.1
    · intro j _; exact (bounds j).2.2.2
    · intro x hx
      have ne (j : Fin 6) : x ≠ (positions 0 j).val+1 := by
        intro eq
        apply hx
        rw [eq]
        change _ ∈ List.ofFn (fun j => (positions 0 j).val+1)
        exact List.mem_ofFn.mpr ⟨j,rfl⟩
      simp only [loss,if_neg (ne 0),if_neg (ne 1),if_neg (ne 2),if_neg (ne 3),if_neg (ne 4),if_neg (ne 5)]
    · exact strict
  · exact ProfileApplication.propertyB_of_uncorrected_profile H vertices (positions k) (p k)
      real rfl (by simp [p,TripleProfiles.pruneZero,centers,hk]) (bare hk)

theorem low_pair : ∀ i j : Fin 6, i ≠ j → lowData {i,j} = pairDegree i j := by
  decide +kernel

theorem propertyB_of_large (H : Simple5Hypergraph (Fin 23)) (edges33 : H.edges.card = 33)
    (vertices : Fin 6 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 7)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (k : Fin 22) (large : ∀ T, 3 ≤ T.card → count H vertices T = counts k T) : PropertyB H := by
  have low : ∀ T, T.card ≤ 2 → upperCount H vertices T = lowData T := by
    apply upper_eq_of_low_data H vertices lowData
    · simp [lowData,edges33]
    · intro i; simp [lowData]
      exact (degrees i).symm
    · intro i j ij
      rw [pairs i j ij]
      exact low_pair i j ij
  apply propertyB_of_counts H vertices k
  intro T
  exact (actual_recovered H vertices lowData (counts k) low large T).trans (recovery_formula k T)

theorem count_relabel (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (σ : Fin 6 ≃ Fin 6) (T : Finset (Fin 6)) :
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
    exact (sig e).symm.trans (congrArg (fun S : Finset (Fin 6) => S.image σ) hs)
  · intro hs
    apply Finset.image_injective σ.injective
    exact (sig e).trans hs

theorem large_count_le_one (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (T : Finset (Fin 6)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,unit⟩ := large_has_unit_pair T large
  have bound := count_le_codegree H vertices T i j hi hj
  simpa only [pairs i j ij,unit] using bound

theorem zero_of_unit_overlap (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (P T : Finset (Fin 6)) (pLarge : 3 ≤ P.card) (tLarge : 3 ≤ T.card) (ne : P ≠ T)
    (positive : 1 ≤ count H vertices P) (i j : Fin 6) (ij : i ≠ j)
    (ip : i ∈ P) (jp : j ∈ P) (it : i ∈ T) (jt : j ∈ T)
    (unit : H.codegree (vertices i) (vertices j) = 1) : count H vertices T = 0 := by
  have sub : ({P,T} : Finset (Finset (Fin 6))) ⊆ supers {i,j} 3 := by
    intro U hU
    simp only [Finset.mem_insert,Finset.mem_singleton] at hU
    rcases hU with rfl | rfl
    · simp [supers,ip,jp,pLarge,Finset.insert_subset_iff]
    · simp [supers,it,jt,tLarge,Finset.insert_subset_iff]
  have small := Finset.sum_le_sum_of_subset_of_nonneg sub
    (fun U _ _ => Nat.zero_le (count H vertices U))
  have large := high_pair_budget H vertices i j ij
  have sum : count H vertices P + count H vertices T ≤ H.codegree (vertices i) (vertices j) := by
    simpa [Finset.sum_pair ne] using small.trans large
  omega

def actualBits (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23) (c : Fin 3) :
    Fin 10 → Bool := fun a => decide ((allowed c a).Nonempty ∧ count H vertices (allowed c a) = 1)

theorem actual_block (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (c : Fin 3) (pivotCount : count H vertices (pivot c) = 1)
    (a : Fin 11) (nonempty : (blocks c a).Nonempty) :
    (if active (actualBits H vertices c) a then 1 else 0) = count H vertices (blocks c a) := by
  revert nonempty
  refine Fin.cases ?_ (fun b => ?_) a
  · intro _
    simpa [active,blocks] using pivotCount.symm
  · intro nonempty
    change (allowed c b).Nonempty at nonempty
    have large : 3 ≤ (allowed c b).card := by
      have cases := blocks_card c b.succ
      change allowed c b = ∅ ∨ _ at cases
      rcases cases with empty | bounds
      · exact False.elim (nonempty.ne_empty empty)
      · exact bounds.1
    have bound := large_count_le_one H vertices pairs (allowed c b) large
    change (if decide ((allowed c b).Nonempty ∧ count H vertices (allowed c b) = 1) then 1 else 0) = count H vertices (allowed c b)
    by_cases h : count H vertices (allowed c b) = 1
    · simp [h,nonempty]
    · have hz : count H vertices (allowed c b) = 0 := by omega
      simp [hz]

theorem actual_high_value (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (c : Fin 3) (pivotCount : count H vertices (pivot c) = 1)
    (T : Finset (Fin 6)) (large : 3 ≤ T.card) :
    count H vertices T = highValue c (actualBits H vertices c) T := by
  have nonempty : T.Nonempty := Finset.card_pos.mp (by omega)
  by_cases occurs : ∃ a, blocks c a = T
  · obtain ⟨a,rfl⟩ := occurs
    have unique : (∃ b, blocks c b = blocks c a ∧ active (actualBits H vertices c) b = true) ↔
        active (actualBits H vertices c) a = true := by
      constructor
      · rintro ⟨b,eq,hb⟩
        have ba := blocks_injective c a b nonempty eq.symm
        simpa only [←ba] using hb
      · intro ha; exact ⟨a,rfl,ha⟩
    simp only [highValue,unique]
    exact (actual_block H vertices pairs c pivotCount a nonempty).symm
  · have omitted : ∀ a, blocks c a ≠ T := by simpa only [not_exists] using occurs
    have hz : count H vertices T = 0 := by
      by_cases small : T.card ≤ 5
      · obtain ⟨i,it,j,jt,ip,jp,ij,unit⟩ := omitted_unit_overlap c T large small omitted
        exact zero_of_unit_overlap H vertices (pivot c) T (by have := (pivot_card c).1; omega)
          large (omitted 0) (by omega) i j ij ip jp it jt ((pairs i j ij).trans unit)
      · exact count_eq_zero_of_large H vertices T (by omega)
    rw [hz]
    simp only [highValue]
    split_ifs with h
    · obtain ⟨a,ha,_⟩ := h
      exact False.elim (omitted a ha)
    · rfl

theorem actual_admissible (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (c : Fin 3) (pivotCount : count H vertices (pivot c) = 1) :
    Admissible c (actualBits H vertices c) := by
  constructor
  · intro a empty; simp [actualBits,empty]
  · intro i j ij
    let indices := Finset.univ.filter fun a : Fin 11 => i ∈ blocks c a ∧ j ∈ blocks c a
    have nonempty (a) (ha : a ∈ indices) : (blocks c a).Nonempty :=
      ⟨i,(Finset.mem_filter.mp ha).2.1⟩
    have injective : Set.InjOn (blocks c) indices := by
      intro a ha b _ eq
      exact blocks_injective c a b (nonempty a ha) eq
    have sub : indices.image (blocks c) ⊆ supers {i,j} 3 := by
      intro T hT
      obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp hT
      obtain ⟨ip,jp⟩ := (Finset.mem_filter.mp ha).2
      have large : 3 ≤ (blocks c a).card := by
        rcases blocks_card c a with empty | bounds
        · exact False.elim ((nonempty a ha).ne_empty empty)
        · exact bounds.1
      simp [supers,ip,jp,large,Finset.insert_subset_iff]
    have sum_eq : pairSum c (actualBits H vertices c) i j =
        ∑ T ∈ indices.image (blocks c), count H vertices T := by
      rw [Finset.sum_image injective]
      unfold pairSum
      rw [←Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro a ha
      exact actual_block H vertices pairs c pivotCount a (nonempty a ha)
    rw [sum_eq]
    exact (Finset.sum_le_sum_of_subset_of_nonneg sub (fun U _ _ => Nat.zero_le (count H vertices U))).trans
      ((high_pair_budget H vertices i j ij).trans_eq (pairs i j ij))

theorem propertyB_of_pivot (H : Simple5Hypergraph (Fin 23)) (edges33 : H.edges.card = 33)
    (vertices : Fin 6 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 7)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree i j)
    (c : Fin 3) (pivotCount : count H vertices (pivot c) = 1) : PropertyB H := by
  obtain ⟨s,cs,hs⟩ := covers c (actualBits H vertices c) (actual_admissible H vertices pairs c pivotCount)
  let σ := permutation (relabel s)
  let newVertices := σ.toEmbedding.trans vertices
  apply propertyB_of_large H edges33 newVertices (fun i => degrees (σ i))
    (fun i j ij => (pairs (σ i) (σ j) (σ.injective.ne ij)).trans (permutation_preserves _ i j))
    (representative s)
  intro T large
  rw [show newVertices = σ.toEmbedding.trans vertices from rfl,count_relabel]
  rw [actual_high_value H vertices pairs c pivotCount (T.image σ)
    (by simpa only [Finset.card_image_of_injective _ σ.injective] using large)]
  rw [funext hs,←cs]
  exact representative_counts s T large

/-- No trace table is assumed: the large trace is an actual edge witness. -/
theorem propertyB_of_six_case (H : Simple5Hypergraph (Fin 23)) (edges33 : H.edges.card = 33)
    (selected : TwentyThreeClusterSelection.SixCase H) : PropertyB H := by
  obtain ⟨f,inj,degrees,forward,e,he,large⟩ := selected
  let vertices : Fin 6 ↪ Fin 23 := ⟨f,inj⟩
  have pairs (i j : Fin 6) (ij : i ≠ j) :
      H.codegree (vertices i) (vertices j) = pairDegree i j := by
    rcases lt_or_gt_of_ne ij with h | h
    · exact forward i j h
    · change H.codegree (f i) (f j) = _
      rw [H.codegree_comm,forward j i h,pairDegree_comm]
      rfl
  let T := lockSignature vertices e
  have big : 4 ≤ T.card := by
    change 4 ≤ (Finset.univ.filter fun i => f i ∈ e).card
    rw [TwentyThreeClusterSelection.indexed_trace_card f inj e]
    exact large
  have positive : 0 < count H vertices T := Finset.card_pos.mpr
    ⟨e,Finset.mem_filter.mpr ⟨he,rfl⟩⟩
  have small : T.card ≤ 5 := by
    by_contra h
    have hz := count_eq_zero_of_large H vertices T (by omega)
    omega
  have one : count H vertices T = 1 := by
    have upper := large_count_le_one H vertices pairs T (by omega)
    omega
  obtain ⟨c,r,eq⟩ := pivot_covers T big small
  let σ := permutation r
  let newVertices := σ.toEmbedding.trans vertices
  apply propertyB_of_pivot H edges33 newVertices (fun i => degrees (σ i))
    (fun i j ij => (pairs (σ i) (σ j) (σ.injective.ne ij)).trans (permutation_preserves r i j)) c
  rw [show newVertices = σ.toEmbedding.trans vertices from rfl,count_relabel,eq]
  exact one

end Aris4Math.ThirtyThree.TwentyThreeHighSix

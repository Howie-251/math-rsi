import Aris4Math.ThirtyThree.TwentyThreeFourLowStructure
import Aris4Math.ThirtyThree.TwentyThreeFourLowCatalog
import Aris4Math.ThirtyThree.TwentyThreeFourLowBare

namespace Aris4Math.ThirtyThree.TwentyThreeFourLowActual
open scoped BigOperators
open Aris4Math.TypeCounting
open QuadProfiles (first second highLabels)
open TwentyThreeFourLowCatalog (co pairBudget high highBudget)

theorem actual_pair_values (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 6) :
    ∃ r : Fin 56, ∀ i, H.codegree (vertices (first i)) (vertices (second i)) = co r i := by
  have apart (i : Fin 6) : first i ≠ second i := by fin_cases i <;> decide
  have upper (i : Fin 6) := TwentyThreeSelection.six_codegree_le_three H cover
    (Fintype.card_fin 23) (degrees (first i)) (vertices.injective.ne (apart i))
  let e : Fin 6 → Fin 3 := fun i =>
    ⟨H.codegree (vertices (first i)) (vertices (second i)) - 1, by have h := upper i; omega⟩
  have values (i : Fin 6) : (e i).val+1 =
      H.codegree (vertices (first i)) (vertices (second i)) := by
    have low := H.one_le_codegree cover (vertices.injective.ne (apart i))
    dsimp [e]
    omega
  have bounds (i : Fin 4) := TwentyThreeSelection.indexed_six_excess_le_two H cover
    (Fintype.card_fin 23) vertices vertices.injective i (degrees i)
  have b0 := bounds 0
  have b1 := bounds 1
  have b2 := bounds 2
  have b3 := bounds 3
  rw [show (Finset.univ.erase (0 : Fin 4)) = {1,2,3} from by decide] at b0
  rw [show (Finset.univ.erase (1 : Fin 4)) = {0,2,3} from by decide] at b1
  rw [show (Finset.univ.erase (2 : Fin 4)) = {0,1,3} from by decide] at b2
  rw [show (Finset.univ.erase (3 : Fin 4)) = {0,1,2} from by decide] at b3
  simp +decide only [Finset.sum_insert,Finset.sum_singleton,Finset.mem_insert,
    Finset.mem_singleton] at b0 b1 b2 b3
  have budget : pairBudget e := by
    unfold pairBudget
    dsimp [e,first,second]
    simp only [H.codegree_comm (vertices 1) (vertices 0),
      H.codegree_comm (vertices 2) (vertices 0), H.codegree_comm (vertices 2) (vertices 1),
      H.codegree_comm (vertices 3) (vertices 0), H.codegree_comm (vertices 3) (vertices 1),
      H.codegree_comm (vertices 3) (vertices 2)] at b1 b2 b3
    exact ⟨by omega,by omega,by omega,by omega⟩
  obtain ⟨r,hr⟩ := TwentyThreeFourLowCatalog.pair_covers e budget
  exact ⟨r,fun i => (values i).symm.trans (hr i)⟩

theorem actual_high_budget (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (r : Fin 56) (pairs : ∀ i, H.codegree (vertices (first i)) (vertices (second i)) = co r i)
    (a b c d : Fin 3) (q : Fin 2)
    (actual : ∀ i, QuadProfiles.count H vertices (highLabels i) = high a b c d q i) :
    highBudget r a b c d q := by
  have bound (i : Fin 6) := MultiLockRecovery.high_pair_budget H vertices (first i) (second i)
    (by fin_cases i <;> decide)
  have expanded (i : Fin 6) :
      MultiLockRecovery.supers {first i,second i} 3 =
        (![({highLabels 0,highLabels 1,highLabels 4} : Finset (Finset (Fin 4))),
          {highLabels 0,highLabels 2,highLabels 4}, {highLabels 1,highLabels 2,highLabels 4},
          {highLabels 0,highLabels 3,highLabels 4}, {highLabels 1,highLabels 3,highLabels 4},
          {highLabels 2,highLabels 3,highLabels 4}] i) := by
    fin_cases i <;> decide +kernel
  have hb (i : Fin 6) := bound i
  simp only [expanded,pairs] at hb
  have b0 := hb 0
  have b1 := hb 1
  have b2 := hb 2
  have b3 := hb 3
  have b4 := hb 4
  have b5 := hb 5
  simp only [Matrix.cons_val_zero,Matrix.cons_val_one,Matrix.cons_val_two,
    Matrix.cons_val_three,Matrix.cons_val_four,QuadProfiles.cons_val_five,
    Matrix.head_cons,Matrix.tail_cons] at b0 b1 b2 b3 b4 b5
  have distinct : ∀ i j : Fin 5, i ≠ j → highLabels i ≠ highLabels j := by decide +kernel
  simp +decide only [Finset.sum_insert,Finset.sum_singleton,Finset.mem_insert,Finset.mem_singleton]
    at b0 b1 b2 b3 b4 b5
  change ∀ i, MultiLockRecovery.count H vertices (highLabels i) = high a b c d q i at actual
  simp only [actual,high,Matrix.cons_val_zero,Matrix.cons_val_one,
    Matrix.cons_val_two,Matrix.cons_val_three,Matrix.cons_val_four,
    Matrix.head_cons,Matrix.tail_cons] at b0 b1 b2 b3 b4 b5
  unfold highBudget
  omega

theorem count_relabel (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (σ : Fin 4 ≃ Fin 4) (T : Finset (Fin 4)) :
    QuadProfiles.count H (σ.toEmbedding.trans vertices) T =
      QuadProfiles.count H vertices (T.image σ) := by
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
  unfold QuadProfiles.count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro e _
  constructor
  · intro hs
    exact (sig e).symm.trans (congrArg (fun S : Finset (Fin 4) => S.image σ) hs)
  · intro hs
    apply Finset.image_injective σ.injective
    exact (sig e).trans hs

/-- Every actual four-low input reaches a checked representative after a
genuine relabeling. All bounded parameters come from its actual edge counts. -/
theorem actual_representative (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (vertices : Fin 4 ↪ Fin 23) (degrees : ∀ i, H.degree (vertices i) = 6) :
    ∃ k : Fin 50, ∃ w : Fin 4 ↪ Fin 23,
      (∀ i, H.degree (w i) = 6) ∧
      (∀ T, QuadProfiles.count H w T = TwentyThreeFourLowCatalog.counts k T) := by
  obtain ⟨r,pairs⟩ := actual_pair_values H cover vertices degrees
  have bounds := TwentyThreeFourLowStructure.actual_high_bounds H cover vertices degrees
  let a : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 0),bounds.1 0⟩
  let b : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 1),bounds.1 1⟩
  let c : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 2),bounds.1 2⟩
  let d : Fin 3 := ⟨QuadProfiles.count H vertices (highLabels 3),bounds.1 3⟩
  let q : Fin 2 := ⟨QuadProfiles.count H vertices (highLabels 4),bounds.2⟩
  have actual : ∀ i, QuadProfiles.count H vertices (highLabels i) = high a b c d q i := by
    intro i
    fin_cases i <;> rfl
  obtain ⟨k,σ,hk⟩ := TwentyThreeFourLowCatalog.classify r a b c d q
    (actual_high_budget H vertices r pairs a b c d q actual)
  refine ⟨k,σ.toEmbedding.trans vertices,(fun i => degrees (σ i)),?_⟩
  intro T
  rw [count_relabel,QuadProfiles.actual_recovered,edges33]
  rw [show (fun i => H.degree (vertices i)) = (fun _ => 6) from funext degrees]
  rw [show (fun i => H.codegree (vertices (first i)) (vertices (second i))) = co r from funext pairs]
  rw [show (fun i => QuadProfiles.count H vertices (highLabels i)) = high a b c d q from funext actual]
  exact hk T

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem bare_counts : ∀ k : Fin 47, ∀ T : Finset (Fin 4),
    TwentyThreeFourLowCatalog.counts ⟨k.val+3,by omega⟩ T =
      TwentyThreeFourLowBare.counts k T := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem unit_counts : ∀ k : Fin 3, ∀ i j : Fin 4, i ≠ j →
    (∑ T ∈ (Finset.univ.filter fun T : Finset (Fin 4) => i ∈ T ∧ j ∈ T),
      TwentyThreeFourLowCatalog.counts ⟨k.val,by omega⟩ T) = 1 := by decide +kernel

theorem unit_of_actual (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (k : Fin 3)
    (actual : ∀ T, QuadProfiles.count H vertices T =
      TwentyThreeFourLowCatalog.counts ⟨k.val,by omega⟩ T) :
    ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1 := by
  intro i j ij
  rw [← QuadProfiles.sum_codegree_counts H vertices i j]
  simpa only [actual] using unit_counts k i j ij

/-- All nonunit representatives already return Property B. Only the three
unit-codegree representatives require the separate actual-bad-slot caller. -/
theorem propertyB_or_unit_counts (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many : 4 ≤ H.sixVertices.card) :
    PropertyB H ∨ ∃ vertices : Fin 4 ↪ Fin 23, ∃ k : Fin 3,
      (∀ i, H.degree (vertices i) = 6) ∧
      (∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) ∧
      (∀ T, QuadProfiles.count H vertices T =
        TwentyThreeFourLowCatalog.counts ⟨k.val,by omega⟩ T) := by
  obtain ⟨f,inj,degrees⟩ := TwentyThreeSelection.exists_four_sixes H many
  obtain ⟨k,w,degree,actual⟩ := actual_representative H cover edges33 ⟨f,inj⟩ degrees
  by_cases small : k.val < 3
  · let j : Fin 3 := ⟨k.val,small⟩
    have hk : (⟨j.val,by omega⟩ : Fin 50) = k := Fin.ext rfl
    have countj : ∀ T, QuadProfiles.count H w T =
        TwentyThreeFourLowCatalog.counts ⟨j.val,by omega⟩ T := by simpa only [hk] using actual
    exact Or.inr ⟨w,j,degree,unit_of_actual H w j countj,countj⟩
  · let j : Fin 47 := ⟨k.val-3,by omega⟩
    have hk : (⟨j.val+3,by omega⟩ : Fin 50) = k := by apply Fin.ext; dsimp [j]; omega
    apply Or.inl
    apply TwentyThreeFourLowBare.propertyB_of_counts H w j
    intro T
    rw [actual,← hk,bare_counts]

end Aris4Math.ThirtyThree.TwentyThreeFourLowActual

#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowActual.actual_representative
#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowActual.propertyB_or_unit_counts

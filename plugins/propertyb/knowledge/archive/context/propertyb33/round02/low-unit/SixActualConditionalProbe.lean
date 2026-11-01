import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalogData
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixHighCatalog
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalog
open scoped BigOperators
open TwentyThreeLowUnitSixCatalogData TwentyThreeLowUnitSixHighCatalog
def capacity (e : Fin 3) (p : Fin 15) : ℕ := pairDegree e (first p) (second p)
def Admissible (e : Fin 3) (F : Finset (Fin 41)) : Prop :=
  ∀ p, ∑ a ∈ F, cost a p ≤ capacity e p
end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalog

namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixActual
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeLowUnitSixCatalogData
open TwentyThreeLowUnitSixHighCatalog
open TwentyThreeLowUnitSixCatalog (capacity Admissible)

private theorem has_unit_pair : ∀ T : Finset (Fin 6), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ ({i,j} : Finset (Fin 6)) ≠ {0,1} ∧
      ({i,j} : Finset (Fin 6)) ≠ {2,3} := by decide +kernel

theorem large_count_le_one (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (e : Fin 3)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j)
    (T : Finset (Fin 6)) (large : 3 ≤ T.card) : count H vertices T ≤ 1 := by
  obtain ⟨i,hi,j,hj,ij,not01,not23⟩ := has_unit_pair T large
  have bound := count_le_codegree H vertices T i j hi hj
  simpa [pairs i j ij,pairDegree,not01,not23] using bound

def actualFamily (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23) :
    Finset (Fin 41) := Finset.univ.filter fun a => count H vertices (largeType a) = 1

theorem actual_high_value (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (e : Fin 3)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j)
    (T : Finset (Fin 6)) (large : 3 ≤ T.card) :
    count H vertices T = if T ∈ (actualFamily H vertices).image largeType then 1 else 0 := by
  have member : T ∈ (actualFamily H vertices).image largeType ↔ count H vertices T = 1 := by
    constructor
    · rintro h
      obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp h
      exact (Finset.mem_filter.mp ha).2
    · intro hc
      have small : T.card ≤ 5 := by
        by_contra hn
        have zero := count_eq_zero_of_large H vertices T (by omega)
        omega
      obtain ⟨a,rfl⟩ := largeType_complete T large small
      exact Finset.mem_image.mpr ⟨a,Finset.mem_filter.mpr ⟨Finset.mem_univ _,hc⟩,rfl⟩
  have bound := large_count_le_one H vertices e pairs T large
  by_cases one : count H vertices T = 1
  · simp [member,one]
  · have zero : count H vertices T = 0 := by omega
    simp [member,zero]

theorem actual_admissible (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (e : Fin 3)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j) :
    Admissible e (actualFamily H vertices) := by
  intro p
  let J := (actualFamily H vertices).filter fun a =>
    first p ∈ largeType a ∧ second p ∈ largeType a
  have value (a : Fin 41) (ha : a ∈ J) : count H vertices (largeType a) = 1 :=
    (Finset.mem_filter.mp (Finset.mem_filter.mp ha).1).2
  have imageSub : J.image largeType ⊆ supers {first p,second p} 3 := by
    intro T hT
    obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp hT
    obtain ⟨_,hfirst,hsecond⟩ := Finset.mem_filter.mp ha
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _,?_,(largeType_cards a).1⟩
    simp only [Finset.insert_subset_iff,Finset.singleton_subset_iff]
    exact ⟨hfirst,hsecond⟩
  have sum_eq : (∑ a ∈ actualFamily H vertices, cost a p) =
      ∑ T ∈ J.image largeType, count H vertices T := by
    calc
      (∑ a ∈ actualFamily H vertices, cost a p) = ∑ a ∈ J, 1 := by
        simp only [J,Finset.sum_filter,cost]
      _ = ∑ a ∈ J, count H vertices (largeType a) := by
        apply Finset.sum_congr rfl
        intro a ha
        exact (value a ha).symm
      _ = ∑ T ∈ J.image largeType, count H vertices T := by
        rw [Finset.sum_image]
        intro a _ b _ eq
        exact largeType_injective eq
  rw [sum_eq]
  exact (Finset.sum_le_sum_of_subset imageSub).trans
    ((high_pair_budget H vertices (first p) (second p) (distinct_pair p)).trans_eq
      (pairs (first p) (second p) (distinct_pair p)))

theorem count_relabel (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 6 ↪ Fin 23)
    (σ : Fin 6 ≃ Fin 6) (T : Finset (Fin 6)) :
    count H (σ.toEmbedding.trans vertices) T = count H vertices (T.image σ) := by
  have sig (edge : Finset (Fin 23)) :
      (lockSignature (σ.toEmbedding.trans vertices) edge).image σ = lockSignature vertices edge := by
    ext j
    constructor
    · intro hj
      obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hj
      exact (mem_lockSignature vertices edge (σ i)).mpr
        ((mem_lockSignature (σ.toEmbedding.trans vertices) edge i).mp hi)
    · intro hj
      apply Finset.mem_image.mpr
      refine ⟨σ.symm j,?_,σ.apply_symm_apply j⟩
      apply (mem_lockSignature (σ.toEmbedding.trans vertices) edge (σ.symm j)).mpr
      simpa using (mem_lockSignature vertices edge j).mp hj
  unfold count multiplicity fiber
  congr 1
  apply Finset.filter_congr
  intro edge _
  constructor
  · intro hs
    exact (sig edge).symm.trans (congrArg (fun S : Finset (Fin 6) => S.image σ) hs)
  · intro hs
    apply Finset.image_injective σ.injective
    exact (sig edge).trans hs

theorem actual_representative
    (classification : ∀ e : Fin 3, ∀ F : Finset (Fin 41), Admissible e F →
      ∃ c : Case, ∃ σ : Fin 6 ≃ Fin 6,
        extra c = e ∧ (∀ i, degreeData (σ i) = degreeData i) ∧
          (∀ i j, pairDegree e (σ i) (σ j) = pairDegree e i j) ∧
          (largeFamily c).image (fun T => T.image σ) = F.image largeType)
    (recovery : ∀ c : Case, ∀ T : Finset (Fin 6),
      recovered (low (extra c)) (high c) T = counts c T)
    (H : Simple5Hypergraph (Fin 23))
    (edges33 : H.edges.card = 33) (vertices : Fin 6 ↪ Fin 23) (e : Fin 3)
    (degrees : ∀ i, H.degree (vertices i) = degreeData i)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = pairDegree e i j) :
    ∃ c : Case, ∃ w : Fin 6 ↪ Fin 23, ∀ T, count H w T = counts c T := by
  obtain ⟨c,σ,extra_eq,degreePreserve,pairPreserve,family⟩ :=
    classification e (actualFamily H vertices)
      (actual_admissible H vertices e pairs)
  let w := σ.toEmbedding.trans vertices
  have hlow : ∀ T, T.card ≤ 2 → upperCount H w T = low (extra c) T := by
    apply upper_eq_of_low_data
    · simp [low,edges33]
    · intro i
      change low (extra c) {i} = H.degree (vertices (σ i))
      rw [degrees,degreePreserve]
      by_cases hi : i = 5
      · subst i; simp [low,degreeData]
      · simp [low,degreeData,hi,Ne.symm hi]
    · intro i j ij
      change low (extra c) {i,j} = H.codegree (vertices (σ i)) (vertices (σ j))
      rw [pairs (σ i) (σ j) (σ.injective.ne ij),pairPreserve,extra_eq]
      simp [low,pairDegree,ij]
  have hhigh : ∀ T, 3 ≤ T.card → count H w T = high c T := by
    intro T hT
    rw [show w = σ.toEmbedding.trans vertices from rfl,count_relabel,
      actual_high_value H vertices e pairs (T.image σ)
        (by simpa only [Finset.card_image_of_injective _ σ.injective] using hT),← family]
    have member : T.image σ ∈ (largeFamily c).image (fun U => U.image σ) ↔ T ∈ largeFamily c := by
      constructor
      · intro hm
        obtain ⟨U,hU,eq⟩ := Finset.mem_image.mp hm
        have equal := Finset.image_injective σ.injective eq
        simpa only [equal] using hU
      · intro hm
        exact Finset.mem_image.mpr ⟨T,hm,rfl⟩
    simp only [member,high]
  refine ⟨c,w,fun T => ?_⟩
  exact (actual_recovered H w (low (extra c)) (high c) hlow hhigh T).trans
    (recovery c T)

end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixActual
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixActual.actual_representative

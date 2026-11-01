import Aris4Math.ThirtyFour.WeightedSubsetSelection
import Aris4Math.ThirtyThree.TwentyThreeSelection

/-! Actual minimum-weight six-lock selection for the 23-point, 34-edge
minimum-degree-seven branch. The weighted graph is derived from H. -/
namespace Aris4Math.ThirtyFour.TwentyThreeSevenSelection

open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeSelection (sevenVertices mem_sevenVertices)
open WeightedSubsetSelection

def excess (H : Simple5Hypergraph (Fin 23)) (x y : Fin 23) : ℕ :=
  if x=y then 0 else H.codegree x y-1

theorem excess_symm (H : Simple5Hypergraph (Fin 23)) (x y : Fin 23) :
    excess H x y = excess H y x := by
  simp only [excess,eq_comm,H.codegree_comm x y]

@[simp] theorem excess_self (H : Simple5Hypergraph (Fin 23)) (x : Fin 23) :
    excess H x x=0 := by simp [excess]

theorem at_least_fourteen (H : Simple5Hypergraph (Fin 23)) (size : H.edges.card=34)
    (minimum : ∀ x, 7 ≤ H.degree x) : 14 ≤ (sevenVertices H).card := by
  have each (x : Fin 23) : 8 ≤ H.degree x + if H.degree x=7 then 1 else 0 := by
    have low := minimum x
    split_ifs <;> omega
  have total := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have degreeSum := H.sum_degrees
  rw [size] at degreeSum
  have h : 184 ≤ 170 + (sevenVertices H).card := by
    simpa [Finset.sum_add_distrib,degreeSum,sevenVertices] using total
  omega

theorem full_weighted_degree (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (x : Fin 23) (dx : H.degree x=7) : degree (excess H) Finset.univ x=6 := by
  have erase := Finset.sum_erase_add (s := Finset.univ) (fun y => excess H x y) (Finset.mem_univ x)
  dsimp only at erase
  rw [excess_self,Nat.add_zero] at erase
  have same : (∑ y ∈ (Finset.univ : Finset (Fin 23)).erase x, excess H x y) =
      ∑ y ∈ (Finset.univ : Finset (Fin 23)).erase x, (H.codegree x y-1) := by
    apply Finset.sum_congr rfl
    intro y hy
    have ne := (Finset.mem_erase.mp hy).1
    simp [excess,ne.symm]
  rw [same,H.sum_codegree_excess cover x] at erase
  simpa [degree,dx] using erase.symm

theorem sevens_weighted_degree (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (x : Fin 23) (hx : x ∈ sevenVertices H) :
    degree (excess H) (sevenVertices H) x ≤ 6 := by
  have bound := Finset.sum_le_sum_of_subset (Finset.subset_univ (sevenVertices H))
    (f := excess H x)
  change degree (excess H) (sevenVertices H) x ≤ degree (excess H) Finset.univ x at bound
  rw [full_weighted_degree H cover x ((mem_sevenVertices H x).mp hx)] at bound
  exact bound

/-- A genuine six-subset of the degree-seven vertices, with all structural
bounds used by the local classification. No numeric profile is an input. -/
theorem actual_minimum_six (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x, 7 ≤ H.degree x) :
    ∃ S : Finset (Fin 23), S.card=6 ∧
      IsMinimum (excess H) (sevenVertices H) S ∧ energy (excess H) S ≤ 12 ∧
      (∀ x ∈ S, degree (excess H) S x ≤ 3) ∧
      (∀ x ∈ S, degree (excess H) S x=3 → energy (excess H) S ≤ 8) := by
  exact exists_six (excess H) (excess_symm H) (excess_self H) (sevenVertices H)
    (at_least_fourteen H size minimum) (sevens_weighted_degree H cover)

theorem outside_eights_of_fourteen (H : Simple5Hypergraph (Fin 23))
    (size : H.edges.card=34) (minimum : ∀ x, 7 ≤ H.degree x)
    (fourteen : (sevenVertices H).card=14) :
    ∀ y, y ∉ sevenVertices H → H.degree y=8 := by
  have each (x : Fin 23) : 8 ≤ H.degree x + if H.degree x=7 then 1 else 0 := by
    have low := minimum x
    split_ifs <;> omega
  have sevenSum : (∑ x : Fin 23, if H.degree x=7 then 1 else 0)=14 := by
    simpa [sevenVertices] using fourteen
  have sums : (∑ _x : Fin 23, (8 : ℕ))=
      ∑ x : Fin 23, (H.degree x + if H.degree x=7 then 1 else 0) := by
    simp [Finset.sum_add_distrib,H.sum_degrees,size,sevenSum]
  have exactEach := (Finset.sum_eq_sum_iff_of_le (fun x _ => each x)).mp sums
  intro y hy
  have notSeven : H.degree y ≠ 7 := fun eq => hy ((mem_sevenVertices H y).mpr eq)
  have eq := exactEach y (Finset.mem_univ y)
  simpa [notSeven] using eq.symm

/-- The equality-table input follows directly from saturation. The stronger
global two-K7 description is not needed to select the actual seventh lock. -/
theorem equality_degree_eight_lock (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x, 7 ≤ H.degree x)
    (S : Finset (Fin 23)) (card : S.card=6)
    (minimal : IsMinimum (excess H) (sevenVertices H) S)
    (equal : energy (excess H) S=12) :
    ∃ y : Fin 23, H.degree y=8 ∧ y ∉ S ∧ ∀ x ∈ S, H.codegree x y=1 := by
  have many := at_least_fourteen H size minimum
  have internal : ∀ x ∈ S, degree (excess H) S x ≤ 2 := by
    intro x hx
    have bound := vertex_bound (excess H) (excess_symm H) (excess_self H)
      (sevenVertices H) S minimal 6 (sevens_weighted_degree H cover)
      (by omega) x hx
    rw [card,equal] at bound
    norm_num at bound
    have seven : 7 ≤ (sevenVertices H).card-7 := by omega
    nlinarith
  obtain ⟨fourteen,saturated⟩ := six_equality_saturation (excess H) (excess_symm H)
    (excess_self H) (sevenVertices H) S minimal card many
    (sevens_weighted_degree H cover) internal equal
  obtain ⟨y,_,outside⟩ := Finset.exists_mem_notMem_of_card_lt_card
    (s := sevenVertices H) (t := Finset.univ) (by simp [fourteen])
  refine ⟨y,outside_eights_of_fourteen H size minimum fourteen y outside,
    fun hy => outside (minimal.1 hy),?_⟩
  intro x hx
  have xSeven := (mem_sevenVertices H x).mp (minimal.1 hx)
  have xy : x ≠ y := by intro eq; subst y; exact outside (minimal.1 hx)
  have bound := Finset.sum_le_sum_of_subset
    (Finset.subset_univ (insert y (sevenVertices H))) (f := excess H x)
  change degree (excess H) (insert y (sevenVertices H)) x ≤
    degree (excess H) Finset.univ x at bound
  rw [degree_insert (excess H) (sevenVertices H) x y outside,
    saturated x hx,full_weighted_degree H cover x xSeven] at bound
  have low := H.one_le_codegree cover xy
  simp only [excess,if_neg xy] at bound
  omega

end Aris4Math.ThirtyFour.TwentyThreeSevenSelection

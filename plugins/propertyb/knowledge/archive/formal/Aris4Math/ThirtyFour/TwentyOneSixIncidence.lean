import Aris4Math.ThirtyFour.TwentyOneFiveStructure
namespace Aris4Math.ThirtyFour.TwentyOneSixIncidence
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles

/-- Two prescribed neighbors consume the actual codegree excess. -/
theorem pair_excess (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z) (dx : H.degree x=6) :
    H.codegree x y+H.codegree x z≤6 := by
  have sub : ({y,z} : Finset (Fin 21))⊆Finset.univ.erase x := by
    intro a ha
    simp only [Finset.mem_insert,Finset.mem_singleton] at ha
    rcases ha with rfl | rfl <;> simp [xy.symm,xz.symm]
  have h := Finset.sum_le_sum_of_subset sub (f := fun a => H.codegree x a-1)
  rw [H.sum_codegree_excess cover x,dx] at h
  simp only [Fintype.card_fin] at h
  have hy := H.one_le_codegree cover xy
  have hz := H.one_le_codegree cover xz
  simp only [Finset.sum_insert (show y∉({z} : Finset (Fin 21)) by simpa using yz),Finset.sum_singleton] at h
  omega

theorem inventories {v : ℕ} (H : Simple5Hypergraph (Fin v)) (x y z : Fin v)
    (xy : x≠y) (xz : x≠z) (yz : y≠z) :
    H.codegree x y+H.codegree x z≤H.degree x+tripleCodegree H x y z ∧
    H.codegree x y+H.codegree y z≤H.degree y+tripleCodegree H x y z ∧
    H.codegree x z+H.codegree y z≤H.degree z+tripleCodegree H x y z := by
  have hx := TwentyOneFiveStructure.pair_inventory H y x z xy.symm yz xz
  have hy := TwentyOneFiveStructure.pair_inventory H x y z xy xz yz
  have hz := TwentyOneFiveStructure.pair_inventory H x z y xz xy yz.symm
  have tc1 : tripleCodegree H y x z=tripleCodegree H x y z := by
    simp only [tripleCodegree,and_left_comm]
  have tc2 : tripleCodegree H x z y=tripleCodegree H x y z := by
    simp only [tripleCodegree,and_comm,and_left_comm,and_assoc]
  rw [H.codegree_comm y x,tc1] at hx
  rw [H.codegree_comm z y,tc2] at hz
  exact ⟨hx,hy,hz⟩

/-- Charge an arbitrary already-selected neighbor set before counting other bad partners. -/
theorem outside_bad_budget (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x : Fin 21) (dx : H.degree x=6) (T : Finset (Fin 21)) (apart : x∉T) :
    (H.badPartners x\T).card+(∑ y∈T,(H.codegree x y-1))≤4 := by
  let A:=H.badPartners x\T
  have sub : A∪T⊆Finset.univ.erase x := by
    intro y hy
    rcases Finset.mem_union.mp hy with ha | ht
    · exact (Finset.mem_filter.mp (Finset.mem_sdiff.mp ha).1).1
    · exact Finset.mem_erase.mpr ⟨fun eq => apart (eq ▸ ht),Finset.mem_univ y⟩
  have lower : A.card≤∑y∈A,(H.codegree x y-1) := by
    calc
      _=∑_y∈A,(1:ℕ) := by simp
      _≤_ := by
        apply Finset.sum_le_sum
        intro y hy
        have hbad := (Finset.mem_filter.mp (Finset.mem_sdiff.mp hy).1).2
        omega
  have bound := Finset.sum_le_sum_of_subset sub (f := fun y=>H.codegree x y-1)
  rw [Finset.sum_union (Finset.sdiff_disjoint),H.sum_codegree_excess cover x,dx] at bound
  simp only [Fintype.card_fin] at bound
  change A.card+(∑y∈T,(H.codegree x y-1))≤4
  dsimp only [A] at lower ⊢
  omega
end Aris4Math.ThirtyFour.TwentyOneSixIncidence

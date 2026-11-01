import Aris4Math.ThirtyFour.TwentySevenMany

namespace Aris4Math.ThirtyFour.TwentyStructure
open scoped BigOperators

def eights (H : Simple5Hypergraph (Fin 20)) : Finset (Fin 20) :=
  Finset.univ.filter (fun x => H.degree x=8)

theorem mem_eights (H : Simple5Hypergraph (Fin 20)) (x : Fin 20) :
    x ∈ eights H ↔ H.degree x=8 := by simp [eights]

theorem eights_budget (H : Simple5Hypergraph (Fin 20)) (size : H.edges.card=34)
    (minimum : ∀ x, 7 ≤ H.degree x) :
    10 ≤ 2*(TwentySevenMany.sevens H).card+(eights H).card := by
  have each (x : Fin 20) : 9 ≤ H.degree x +
      (if x ∈ TwentySevenMany.sevens H then 2 else 0) + (if x ∈ eights H then 1 else 0) := by
    by_cases seven : H.degree x=7
    · simp [TwentySevenMany.sevens,eights,seven]
    by_cases eight : H.degree x=8
    · simp [TwentySevenMany.sevens,eights,eight]
    have lo := minimum x
    simp only [TwentySevenMany.mem_sevens,mem_eights,seven,eight,if_false,add_zero]
    omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have budget : 180 ≤ 170 + 2*(TwentySevenMany.sevens H).card+(eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,Nat.mul_comm] using sum
  omega
/-- A large actual vertex set still has a point outside any prescribed pair. -/
theorem exists_third (S : Finset (Fin 20)) (size : 3 ≤ S.card) (x y : Fin 20) :
    ∃ z ∈ S, z ≠ x ∧ z ≠ y := by
  by_contra hn
  have sub : S ⊆ {x,y} := by
    intro z hz
    by_cases zx : z=x
    · simp [zx]
    by_cases zy : z=y
    · simp [zy]
    exact False.elim (hn ⟨z,hz,zx,zy⟩)
  have bound := Finset.card_le_card sub
  have pairBound := Finset.card_insert_le x {y}
  simp only [Finset.card_singleton] at pairBound
  omega

theorem eights_at_least_ten (H : Simple5Hypergraph (Fin 20)) (size : H.edges.card=34)
    (minimum : ∀ x, 8 ≤ H.degree x) : 10 ≤ (eights H).card := by
  have absent : TwentySevenMany.sevens H=∅ := by
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro x hx
    have dx := (TwentySevenMany.mem_sevens H x).mp hx
    have lo := minimum x
    omega
  have budget := eights_budget H size (fun x => (by have := minimum x; omega))
  simpa [absent] using budget

theorem exists_fourth (S : Finset (Fin 20)) (size : 4 ≤ S.card) (x y z : Fin 20) :
    ∃ w ∈ S, w ≠ x ∧ w ≠ y ∧ w ≠ z := by
  have bound : ({x,y,z} : Finset (Fin 20)).card ≤ 3 := by
    have a := Finset.card_insert_le x ({y,z} : Finset (Fin 20))
    have b := Finset.card_insert_le y ({z} : Finset (Fin 20))
    simp only [Finset.card_singleton] at b
    omega
  obtain ⟨w,hw,out⟩ := Finset.exists_mem_notMem_of_card_lt_card (s := {x,y,z}) (t := S) (by omega)
  refine ⟨w,hw,?_⟩
  simpa only [Finset.mem_insert,Finset.mem_singleton,not_or] using out

end Aris4Math.ThirtyFour.TwentyStructure

import Aris4Math.ThirtyThree.TwentyThreeSelection

/-! A genuine seventh lock for the exactly-six-low branch. The degree and
codegree budgets use the same H; internal unit pairs are not needed. -/
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyThreeSelection

def medium (H : Simple5Hypergraph (Fin 23)) : Finset (Fin 23) :=
  Finset.univ.filter fun z => H.degree z=7 ∨ H.degree z=8

theorem ten_medium (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (six : H.sixVertices.card=6) : 10≤(medium H).card := by
  have each (x : Fin 23) : 9 ≤ H.degree x +
      (if H.degree x=6 then 3 else 0) +
      (if H.degree x=7 ∨ H.degree x=8 then 2 else 0) := by
    have minimum := min_degree_six H cover (Fintype.card_fin 23) x
    split_ifs <;> omega
  have total := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have lowSum : (∑ x : Fin 23, if H.degree x=6 then 3 else 0)=3*H.sixVertices.card := by
    rw [← Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices,Nat.mul_comm]
  have mediumSum : (∑ x : Fin 23, if H.degree x=7 ∨ H.degree x=8 then 2 else 0)=
      2*(medium H).card := by
    rw [← Finset.sum_filter]
    simp [medium,Nat.mul_comm]
  rw [Finset.sum_add_distrib,Finset.sum_add_distrib,H.sum_degrees,lowSum,mediumSum,edges,six] at total
  norm_num at total
  omega

/-- There is an actual degree-seven/eight point outside all six selected lows
whose total codegree excess against those lows is at most one. -/
theorem exists_seventh (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges : H.edges.card=34) (six : H.sixVertices.card=6)
    (f : Fin 6 ↪ Fin 23) (degrees : ∀ i, H.degree (f i)=6) :
    ∃ z : Fin 23, (H.degree z=7 ∨ H.degree z=8) ∧
      (∀ i, f i≠z) ∧ (∑ i : Fin 6, (H.codegree (f i) z-1))≤1 := by
  have many := ten_medium H cover edges six
  have outside (i : Fin 6) : f i∉medium H := by
    simp [medium,degrees i]
  have cap (i : Fin 6) : (∑ z∈medium H, (H.codegree (f i) z-1))≤2 :=
    six_subset_excess_le_two H cover (Fintype.card_fin 23) (degrees i) (medium H) (outside i)
  have bound : (∑ z∈medium H, ∑ i : Fin 6, (H.codegree (f i) z-1))≤12 := by
    rw [Finset.sum_comm]
    have total := Finset.sum_le_sum (s := Finset.univ) (fun i _ => cap i)
    simpa using total
  have good : ∃ z∈medium H, (∑ i : Fin 6, (H.codegree (f i) z-1))≤1 := by
    by_contra none
    have lower : ∀ z∈medium H, 2≤∑ i : Fin 6, (H.codegree (f i) z-1) := by
      intro z hz
      by_contra small
      exact none ⟨z,hz,by omega⟩
    have total := Finset.sum_le_sum lower
    have numeric : 2*(medium H).card≤12 := by
      have h := total.trans bound
      simpa [Nat.mul_comm] using h
    omega
  obtain ⟨z,hz,hcap⟩ := good
  refine ⟨z,(Finset.mem_filter.mp hz).2,?_,hcap⟩
  intro i eq
  exact outside i (eq ▸ hz)

end Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection
#print axioms Aris4Math.ThirtyFour.TwentyThreeSixLowExtraSelection.exists_seventh

import Aris4Math.ThirtyThree.QuadProfiles

namespace Aris4Math.ThirtyFour.QuadIncidence
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.TypeCounting

def tripleFirst : Fin 4 → Fin 4 := ![0,0,0,1]
def tripleSecond : Fin 4 → Fin 4 := ![1,1,2,2]
def tripleThird : Fin 4 → Fin 4 := ![2,3,3,3]

theorem triple_count {v : ℕ} (H : Simple5Hypergraph (Fin v)) (f : Fin 4 ↪ Fin v) (j : Fin 4) :
    tripleCodegree H (f (tripleFirst j)) (f (tripleSecond j)) (f (tripleThird j)) =
      count H f (highLabels j.castSucc) + count H f (highLabels 4) := by
  have h := sum_counts H f (Finset.univ.filter (fun T =>
    tripleFirst j ∈ T ∧ tripleSecond j ∈ T ∧ tripleThird j ∈ T))
  have right : (H.edges.filter (fun e => lockSignature f e ∈ Finset.univ.filter
      (fun T => tripleFirst j ∈ T ∧ tripleSecond j ∈ T ∧ tripleThird j ∈ T))).card =
      tripleCodegree H (f (tripleFirst j)) (f (tripleSecond j)) (f (tripleThird j)) := by
    simp only [Finset.mem_filter,Finset.mem_univ,true_and,mem_lockSignature,tripleCodegree]
  rw [right] at h
  rw [← h,label_univ]
  fin_cases j <;> simp +decide [labels,highLabels,tripleFirst,tripleSecond,tripleThird,
    Finset.filter_insert,Finset.filter_singleton,Finset.filter_empty,
    Finset.sum_insert,Finset.sum_singleton,Finset.sum_empty]
end Aris4Math.ThirtyFour.QuadIncidence

import Aris4Math.ThirtyThree.TwentyFourFiveMatching
namespace Test
open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyFourFiveMatching
def largeTypes : Fin 16 → Finset (Fin 5) := ![{0,1,2},{0,1,3},{0,2,3},{1,2,3},{0,1,2,3},{0,1,4},{0,2,4},{1,2,4},{0,1,2,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
def pairSum (h : Fin 16 → Bool) (i j : Fin 5) : ℕ := ∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then if h a then 1 else 0 else 0
def FastAdmissible (h : Fin 16 → Bool) : Prop :=
  ((if h 0 then 1 else 0) + (if h 1 then 1 else 0) + (if h 4 then 1 else 0) + (if h 5 then 1 else 0) + (if h 8 then 1 else 0) + (if h 11 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 2 ∧
  ((if h 0 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 1 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 0 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 1 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 2 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 2 ∧
  ((if h 6 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 9 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1
set_option maxHeartbeats 1000000 in
theorem fast (h : Fin 16 → Bool) (ha : ∀i j : Fin 5, i≠j→pairSum h i j≤ pairDegree i j) : FastAdmissible h := by
  unfold FastAdmissible
  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩
  · have hb := ha 0 1 (by decide)
    rw [show pairDegree 0 1 = 2 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 2 (by decide)
    rw [show pairDegree 0 2 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 3 (by decide)
    rw [show pairDegree 0 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 4 (by decide)
    rw [show pairDegree 0 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 2 (by decide)
    rw [show pairDegree 1 2 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 3 (by decide)
    rw [show pairDegree 1 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 4 (by decide)
    rw [show pairDegree 1 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 3 (by decide)
    rw [show pairDegree 2 3 = 2 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 4 (by decide)
    rw [show pairDegree 2 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 3 4 (by decide)
    rw [show pairDegree 3 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
end Test

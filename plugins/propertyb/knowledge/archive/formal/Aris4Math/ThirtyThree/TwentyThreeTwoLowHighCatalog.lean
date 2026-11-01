import Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog

/-! Shared maximal two-disjoint-pair budget catalogue. The degree pattern is
not fixed: both the two-low and one-low-bad-high 23-point branches use it. -/
namespace Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog
open scoped BigOperators
open TwentyFourMatchingHighCatalog (largeTypes highValue pairSum)

def pairDegree (a b : ℕ) (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} then a else
  if ({i,j} : Finset (Fin 5)) = {2,3} then b else 1

def Admissible (a b : ℕ) (h : Fin 16 → Bool) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree a b i j

def catalog : Fin 55 → Fin 16 → Bool := ![![false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![true,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,true,true,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,true,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![true,true,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,true,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,true,true,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,true,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,true,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,false,true,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,true,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,true,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,true,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,true,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,true,false,false,false,false,false,false],![false,false,false,false,false,false,false,true,false,true,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,true,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,true,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false,true,false,false,false,false,false],![false,false,false,false,false,false,true,false,false,false,true,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,true,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,true,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![true,true,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,true,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,true,true,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,true,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![true,false,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![true,true,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,true,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,true,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,true,true,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,true,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,false,true,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false],![false,false,true,false,false,false,false,false,false,false,false,false,false,false,true,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true]]

def FastAdmissible (h : Fin 16 → Bool) : Prop :=
  ((if h 0 then 1 else 0) + (if h 1 then 1 else 0) + (if h 4 then 1 else 0) + (if h 5 then 1 else 0) + (if h 8 then 1 else 0) + (if h 11 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 3 ∧
  ((if h 0 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 1 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 0 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 1 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 2 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 3 ∧
  ((if h 6 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 9 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1

set_option maxHeartbeats 1000000 in
theorem admissible_fast (h : Fin 16 → Bool) (ha : Admissible 3 3 h) : FastAdmissible h := by
  unfold FastAdmissible
  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩
  · have hb := ha 0 1 (by decide)
    rw [show pairDegree 3 3 0 1 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 2 (by decide)
    rw [show pairDegree 3 3 0 2 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 3 (by decide)
    rw [show pairDegree 3 3 0 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 4 (by decide)
    rw [show pairDegree 3 3 0 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 2 (by decide)
    rw [show pairDegree 3 3 1 2 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 3 (by decide)
    rw [show pairDegree 3 3 1 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 4 (by decide)
    rw [show pairDegree 3 3 1 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 3 (by decide)
    rw [show pairDegree 3 3 2 3 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 4 (by decide)
    rw [show pairDegree 3 3 2 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 3 4 (by decide)
    rw [show pairDegree 3 3 3 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb


set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem covers_vector : ∀ b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool,
    FastAdmissible ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] → ∃ s : Fin 55, ∀ a, ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] a = catalog s a := by
  intro b0 b1 b2 b3
  cases b0 <;> cases b1 <;> cases b2 <;> cases b3 <;>
    unfold FastAdmissible <;> decide +kernel

theorem covers_max (h : Fin 16 → Bool) (admissible : Admissible 3 3 h) :
    ∃ s : Fin 55, ∀ a, h a = catalog s a := by
  have hv : ![h 0,h 1,h 2,h 3,h 4,h 5,h 6,h 7,h 8,h 9,h 10,h 11,h 12,h 13,h 14,h 15] = h := by
    funext a
    fin_cases a <;> rfl
  have bound := covers_vector (h 0) (h 1) (h 2) (h 3) (h 4) (h 5) (h 6) (h 7) (h 8) (h 9) (h 10) (h 11) (h 12) (h 13) (h 14) (h 15)
  rw [hv] at bound
  exact bound (admissible_fast h admissible)


theorem covers (a b : ℕ) (h : Fin 16 → Bool) (ha : a ≤ 3) (hb : b ≤ 3)
    (admissible : Admissible a b h) : ∃ s : Fin 55, ∀ i, h i = catalog s i := by
  apply covers_max h
  intro i j ij
  apply (admissible i j ij).trans
  unfold pairDegree
  split_ifs <;> omega

end Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog.covers

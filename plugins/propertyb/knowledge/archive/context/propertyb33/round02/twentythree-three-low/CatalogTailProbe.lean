import Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog

namespace Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog
open scoped BigOperators
open TwentyFourMatchingHighCatalog (largeTypes largeTypes_injective largeTypes_complete)

def pairDegree (e : Fin 3 → ℕ) (b : ℕ) (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} then e 0+1 else
  if ({i,j} : Finset (Fin 5)) = {0,2} then e 1+1 else
  if ({i,j} : Finset (Fin 5)) = {1,2} then e 2+1 else
  if ({i,j} : Finset (Fin 5)) = {3,4} then b else 1

def pairSum (h : Fin 16 → ℕ) (i j : Fin 5) : ℕ :=
  ∑ t : Fin 16, if i ∈ largeTypes t ∧ j ∈ largeTypes t then h t else 0

def highValue (h : Fin 16 → ℕ) (T : Finset (Fin 5)) : ℕ :=
  ∑ t : Fin 16, if largeTypes t = T then h t else 0

def Admissible (e : Fin 3 → ℕ) (b : ℕ) (h : Fin 16 → ℕ) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree e b i j

def catalog : Fin 131 → Fin 16 → ℕ := ![![0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],![0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],![0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],![0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],![0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],![0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],![0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],![0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],![0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],![0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],![0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0],![0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],![0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],![0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],![0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],![0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],![0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],![0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],![0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],![0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],![0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],![0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],![0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0],![0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],![0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],![0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],![0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],![0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],![0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],![0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],![0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0],![0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],![0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],![0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0],![0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],![0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],![0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],![0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],![0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],![0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],![1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],![1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],![1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],![1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],![1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],![1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],![1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],![1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],![1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],![1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],![1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0],![1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],![1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],![1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],![1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],![1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],![1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],![1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],![1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],![1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],![1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],![1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],![1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0],![1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],![1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],![1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],![1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],![1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],![1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],![1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],![1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0],![1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],![1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],![1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0],![1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],![1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],![1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],![1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],![1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],![1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],![2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],![2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],![2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],![2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],![2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],![2,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],![2,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],![2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![2,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],![2,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],![2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![2,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],![2,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],![2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],![2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],![2,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],![2,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],![2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],![2,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],![2,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],![2,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],![2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],![2,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![2,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],![2,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],![2,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],![2,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],![2,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0],![2,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],![2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],![2,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],![2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],![2,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],![2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

def FastAdmissible (h : Fin 16 → ℕ) : Prop :=
  (h 0 + h 1 + h 4 + h 5 + h 8 + h 11 + h 15) ≤ 3 ∧
  (h 0 + h 2 + h 4 + h 6 + h 8 + h 13 + h 15) ≤ 3 ∧
  (h 1 + h 2 + h 4 + h 9 + h 11 + h 13 + h 15) ≤ 1 ∧
  (h 5 + h 6 + h 8 + h 9 + h 11 + h 13 + h 15) ≤ 1 ∧
  (h 0 + h 3 + h 4 + h 7 + h 8 + h 14 + h 15) ≤ 3 ∧
  (h 1 + h 3 + h 4 + h 10 + h 11 + h 14 + h 15) ≤ 1 ∧
  (h 5 + h 7 + h 8 + h 10 + h 11 + h 14 + h 15) ≤ 1 ∧
  (h 2 + h 3 + h 4 + h 12 + h 13 + h 14 + h 15) ≤ 1 ∧
  (h 6 + h 7 + h 8 + h 12 + h 13 + h 14 + h 15) ≤ 1 ∧
  (h 9 + h 10 + h 11 + h 12 + h 13 + h 14 + h 15) ≤ 3

set_option maxHeartbeats 1000000 in
theorem admissible_fast (h : Fin 16 → ℕ) (ha : Admissible (fun _ => 2) 3 h) :
    FastAdmissible h := by
  unfold FastAdmissible
  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩
  · have hb := ha 0 1 (by decide)
    rw [show pairDegree (fun _ => 2) 3 0 1 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 2 (by decide)
    rw [show pairDegree (fun _ => 2) 3 0 2 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 3 (by decide)
    rw [show pairDegree (fun _ => 2) 3 0 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 4 (by decide)
    rw [show pairDegree (fun _ => 2) 3 0 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 2 (by decide)
    rw [show pairDegree (fun _ => 2) 3 1 2 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 3 (by decide)
    rw [show pairDegree (fun _ => 2) 3 1 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 4 (by decide)
    rw [show pairDegree (fun _ => 2) 3 1 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 3 (by decide)
    rw [show pairDegree (fun _ => 2) 3 2 3 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 4 (by decide)
    rw [show pairDegree (fun _ => 2) 3 2 4 = 1 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 3 4 (by decide)
    rw [show pairDegree (fun _ => 2) 3 3 4 = 3 from by decide +kernel] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb

variable (coverAssumption : ∀ n : Fin 3, ∀ b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 : Bool,
    FastAdmissible ![n.val,(if b0 then 1 else 0),(if b1 then 1 else 0),(if b2 then 1 else 0),(if b3 then 1 else 0),(if b4 then 1 else 0),(if b5 then 1 else 0),(if b6 then 1 else 0),(if b7 then 1 else 0),(if b8 then 1 else 0),(if b9 then 1 else 0),(if b10 then 1 else 0),(if b11 then 1 else 0),(if b12 then 1 else 0),(if b13 then 1 else 0),(if b14 then 1 else 0)] → ∃ s : Fin 131, ∀ a, ![n.val,(if b0 then 1 else 0),(if b1 then 1 else 0),(if b2 then 1 else 0),(if b3 then 1 else 0),(if b4 then 1 else 0),(if b5 then 1 else 0),(if b6 then 1 else 0),(if b7 then 1 else 0),(if b8 then 1 else 0),(if b9 then 1 else 0),(if b10 then 1 else 0),(if b11 then 1 else 0),(if b12 then 1 else 0),(if b13 then 1 else 0),(if b14 then 1 else 0)] a = catalog s a)

include coverAssumption in
theorem covers_max (h : Fin 16 → ℕ) (first : h 0 ≤ 2)
    (rest : ∀ i : Fin 16, i ≠ 0 → h i ≤ 1)
    (admissible : Admissible (fun _ => 2) 3 h) :
    ∃ s : Fin 131, ∀ a, h a = catalog s a := by
  have hb (i : Fin 16) (hi : i ≠ 0) :
      (if decide (h i = 1) then 1 else 0) = h i := by
    have b := rest i hi
    by_cases eq : h i = 1
    · simp [eq]
    · have z : h i = 0 := by omega
      simp [z]
  have hv : ![h 0,(if decide (h 1 = 1) then 1 else 0),(if decide (h 2 = 1) then 1 else 0),(if decide (h 3 = 1) then 1 else 0),(if decide (h 4 = 1) then 1 else 0),(if decide (h 5 = 1) then 1 else 0),(if decide (h 6 = 1) then 1 else 0),(if decide (h 7 = 1) then 1 else 0),(if decide (h 8 = 1) then 1 else 0),(if decide (h 9 = 1) then 1 else 0),(if decide (h 10 = 1) then 1 else 0),(if decide (h 11 = 1) then 1 else 0),(if decide (h 12 = 1) then 1 else 0),(if decide (h 13 = 1) then 1 else 0),(if decide (h 14 = 1) then 1 else 0),(if decide (h 15 = 1) then 1 else 0)] = h := by
    funext a
    fin_cases a <;> simp only [Matrix.cons_val_zero,Matrix.cons_val_succ,Matrix.head_cons] <;>
      first | rfl | exact hb _ (by decide)
  have bound := coverAssumption ⟨h 0,by omega⟩ (decide (h 1 = 1)) (decide (h 2 = 1)) (decide (h 3 = 1)) (decide (h 4 = 1)) (decide (h 5 = 1)) (decide (h 6 = 1)) (decide (h 7 = 1)) (decide (h 8 = 1)) (decide (h 9 = 1)) (decide (h 10 = 1)) (decide (h 11 = 1)) (decide (h 12 = 1)) (decide (h 13 = 1)) (decide (h 14 = 1)) (decide (h 15 = 1))
  change (FastAdmissible ![h 0,(if decide (h 1 = 1) then 1 else 0),(if decide (h 2 = 1) then 1 else 0),(if decide (h 3 = 1) then 1 else 0),(if decide (h 4 = 1) then 1 else 0),(if decide (h 5 = 1) then 1 else 0),(if decide (h 6 = 1) then 1 else 0),(if decide (h 7 = 1) then 1 else 0),(if decide (h 8 = 1) then 1 else 0),(if decide (h 9 = 1) then 1 else 0),(if decide (h 10 = 1) then 1 else 0),(if decide (h 11 = 1) then 1 else 0),(if decide (h 12 = 1) then 1 else 0),(if decide (h 13 = 1) then 1 else 0),(if decide (h 14 = 1) then 1 else 0),(if decide (h 15 = 1) then 1 else 0)] → _) at bound
  rw [hv] at bound
  exact bound (admissible_fast h admissible)

end Aris4Math.ThirtyThree.TwentyThreeThreeLowHighCatalog

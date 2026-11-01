import Aris4Math.ThirtyThree.TwentyFourFiveMatching

/-! Complete finite large-trace classification for the two-pair matching case. -/
namespace Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog
open scoped BigOperators
open TwentyFourFiveMatching (pairDegree)

def largeTypes : Fin 16 → Finset (Fin 5) := ![{0,1,2},{0,1,3},{0,2,3},{1,2,3},{0,1,2,3},{0,1,4},{0,2,4},{1,2,4},{0,1,2,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]

def highValue (h : Fin 16 → Bool) (T : Finset (Fin 5)) : ℕ :=
  if ∃ a : Fin 16, largeTypes a = T ∧ h a = true then 1 else 0

def pairSum (h : Fin 16 → Bool) (i j : Fin 5) : ℕ :=
  ∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then
    if h a then 1 else 0 else 0

def Admissible (h : Fin 16 → Bool) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree i j

def catalog : Fin 51 → Fin 16 → Bool := ![![false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![true,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,true,true,false,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,true,false,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,true,false,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,true,true,false,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,true,true,false,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,true,false,false,false,false,false,false,false,false,false],![false,false,false,true,false,false,true,false,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,true,false,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,true,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,true,false,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,true,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,true,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,true,false,false,false,false,false,false],![false,false,false,false,false,false,false,true,false,true,false,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,true,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,true,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false,true,false,false,false,false,false],![false,false,false,false,false,false,true,false,false,false,true,false,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,true,false,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,true,false,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![true,false,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![true,true,false,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,true,false,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,true,false,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![true,false,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,true,false,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,true,false,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,true,true,false,false,false,false,false,false,true,false,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,false],![false,false,false,true,false,false,false,false,false,false,false,false,false,true,false,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false],![false,false,true,false,false,false,false,false,false,false,false,false,false,false,true,false],![false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true]]

def group : Fin 51 → Fin 18 := ![0,3,3,8,3,3,8,13,1,5,5,11,11,15,16,2,7,7,2,7,7,4,9,2,7,7,6,2,7,7,6,4,9,1,11,11,15,5,5,16,10,12,12,12,12,17,4,9,4,9,14]
def permutationFn : Fin 8 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,3,2,4],![1,0,2,3,4],![1,0,3,2,4],![2,3,0,1,4],![2,3,1,0,4],![3,2,0,1,4],![3,2,1,0,4]]
def inverseFn : Fin 8 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,3,2,4],![1,0,2,3,4],![1,0,3,2,4],![2,3,0,1,4],![3,2,0,1,4],![2,3,1,0,4],![3,2,1,0,4]]
def selectedPermutation : Fin 51 → Fin 8 := ![0,6,4,4,2,0,0,0,4,6,4,5,4,0,4,3,5,1,1,4,3,6,6,2,7,0,0,0,6,2,1,4,4,0,1,0,4,2,0,0,0,6,4,2,0,0,2,2,0,0,0]

theorem permutation_left : ∀ r i, inverseFn r (permutationFn r i) = i := by decide +kernel
theorem permutation_right : ∀ r i, permutationFn r (inverseFn r i) = i := by decide +kernel

def permutation (r : Fin 8) : Fin 5 ≃ Fin 5 where
  toFun := permutationFn r
  invFun := inverseFn r
  left_inv := permutation_left r
  right_inv := permutation_right r

theorem largeTypes_injective : Function.Injective largeTypes := by decide +kernel
theorem largeTypes_card : ∀ a, 3 ≤ (largeTypes a).card := by decide +kernel
theorem largeTypes_complete : ∀ T : Finset (Fin 5), 3 ≤ T.card → ∃ a, largeTypes a = T := by decide +kernel

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
theorem admissible_fast (h : Fin 16 → Bool) (ha : Admissible h) : FastAdmissible h := by
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

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem covers_vector : ∀ b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool,
    FastAdmissible ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] → ∃ s : Fin 51, ∀ a, ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] a = catalog s a := by
  intro b0 b1 b2 b3
  cases b0 <;> cases b1 <;> cases b2 <;> cases b3 <;>
    unfold FastAdmissible <;> decide +kernel

theorem covers (h : Fin 16 → Bool) (admissible : Admissible h) :
    ∃ s : Fin 51, ∀ a, h a = catalog s a := by
  have hv : ![h 0,h 1,h 2,h 3,h 4,h 5,h 6,h 7,h 8,h 9,h 10,h 11,h 12,h 13,h 14,h 15] = h := by
    funext a
    fin_cases a <;> rfl
  have bound := covers_vector (h 0) (h 1) (h 2) (h 3) (h 4) (h 5) (h 6) (h 7) (h 8) (h 9) (h 10) (h 11) (h 12) (h 13) (h 14) (h 15)
  rw [hv] at bound
  exact bound (admissible_fast h admissible)

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem representatives : ∀ s : Fin 51,
    (∀ i j, pairDegree (permutation (selectedPermutation s) i)
      (permutation (selectedPermutation s) j) = pairDegree i j) ∧
    (∀ T : Finset (Fin 5), 3 ≤ T.card →
      highValue (catalog s) (T.image (permutation (selectedPermutation s))) =
        TwentyFourFiveMatchingData.counts (group s) T) := by
  intro s
  fin_cases s <;> decide +kernel

theorem classify (h : Fin 16 → Bool) (admissible : Admissible h) :
    ∃ k : Fin 18, ∃ σ : Fin 5 ≃ Fin 5,
      (∀ i j, pairDegree (σ i) (σ j) = pairDegree i j) ∧
      (∀ T : Finset (Fin 5), 3 ≤ T.card →
        highValue h (T.image σ) = TwentyFourFiveMatchingData.counts k T) := by
  obtain ⟨s,hs⟩ := covers h admissible
  have heq : h = catalog s := funext hs
  rw [heq]
  exact ⟨group s,permutation (selectedPermutation s),representatives s⟩

end Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog
#print axioms Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog.classify

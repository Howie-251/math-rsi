import Aris4Math.ThirtyThree.TwentyThreeHighSixData

/-! Complete matching-trace classification using an actual trace of size ≥4. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighSixCatalog
open scoped BigOperators
open TwentyThreeHighSixData (counts)
def pairDegree (i j : Fin 6) : ℕ := if i.val/2=j.val/2 then 2 else 1
theorem pairDegree_comm (i j : Fin 6) : pairDegree i j = pairDegree j i := by simp [pairDegree,eq_comm]
def lowData (T : Finset (Fin 6)) : ℕ :=
  if T=∅ then 33 else if T.card=1 then 7 else
  if T={0,1} ∨ T={2,3} ∨ T={4,5} then 2 else 1
def pivot : Fin 3 → Finset (Fin 6) := ![{0,1,2,3},{0,1,2,4},{0,1,2,3,4}]
def allowed : Fin 3 → Fin 10 → Finset (Fin 6) := ![![{0,1,4},{2,3,4},{0,1,5},{2,3,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{3,4,5},{2,3,4,5}],![{0,1,3},{0,1,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{3,4,5},∅,∅,∅],![{0,1,5},{2,3,5},∅,∅,∅,∅,∅,∅,∅,∅]]
def blocks (c : Fin 3) : Fin 11 → Finset (Fin 6) := Fin.cons (pivot c) (allowed c)
def active (h : Fin 10 → Bool) : Fin 11 → Bool := Fin.cons true h
def highValue (c : Fin 3) (h : Fin 10 → Bool) (T : Finset (Fin 6)) : ℕ :=
  if ∃ a : Fin 11, blocks c a = T ∧ active h a = true then 1 else 0
def pairSum (c : Fin 3) (h : Fin 10 → Bool) (i j : Fin 6) : ℕ :=
  ∑ a : Fin 11, if i ∈ blocks c a ∧ j ∈ blocks c a then if active h a then 1 else 0 else 0
def Admissible (c : Fin 3) (h : Fin 10 → Bool) : Prop :=
  (∀ a, allowed c a = ∅ → h a = false) ∧
  ∀ i j, i ≠ j → pairSum c h i j ≤ pairDegree i j
theorem pivot_card : ∀ c, 4 ≤ (pivot c).card ∧ (pivot c).card ≤ 5 := by decide +kernel
theorem blocks_card : ∀ c a, blocks c a = ∅ ∨ (3 ≤ (blocks c a).card ∧ (blocks c a).card ≤ 5) := by decide +kernel
theorem blocks_injective : ∀ c a b, (blocks c a).Nonempty → blocks c a = blocks c b → a=b := by decide +kernel
theorem large_has_unit_pair : ∀ T : Finset (Fin 6), 3 ≤ T.card →
    ∃ i ∈ T, ∃ j ∈ T, i ≠ j ∧ pairDegree i j = 1 := by decide +kernel
theorem omitted_unit_overlap : ∀ c T, 3 ≤ T.card → T.card ≤ 5 →
    (∀ a : Fin 11, blocks c a ≠ T) →
    ∃ i ∈ T, ∃ j ∈ T, i ∈ pivot c ∧ j ∈ pivot c ∧ i ≠ j ∧ pairDegree i j = 1 := by decide +kernel
def permutationFn : Fin 48 → Fin 6 → Fin 6 := ![![0,1,2,3,4,5],![0,1,2,3,5,4],![0,1,3,2,4,5],![0,1,3,2,5,4],![1,0,2,3,4,5],![1,0,2,3,5,4],![1,0,3,2,4,5],![1,0,3,2,5,4],![0,1,4,5,2,3],![0,1,4,5,3,2],![0,1,5,4,2,3],![0,1,5,4,3,2],![1,0,4,5,2,3],![1,0,4,5,3,2],![1,0,5,4,2,3],![1,0,5,4,3,2],![2,3,0,1,4,5],![2,3,0,1,5,4],![2,3,1,0,4,5],![2,3,1,0,5,4],![3,2,0,1,4,5],![3,2,0,1,5,4],![3,2,1,0,4,5],![3,2,1,0,5,4],![2,3,4,5,0,1],![2,3,4,5,1,0],![2,3,5,4,0,1],![2,3,5,4,1,0],![3,2,4,5,0,1],![3,2,4,5,1,0],![3,2,5,4,0,1],![3,2,5,4,1,0],![4,5,0,1,2,3],![4,5,0,1,3,2],![4,5,1,0,2,3],![4,5,1,0,3,2],![5,4,0,1,2,3],![5,4,0,1,3,2],![5,4,1,0,2,3],![5,4,1,0,3,2],![4,5,2,3,0,1],![4,5,2,3,1,0],![4,5,3,2,0,1],![4,5,3,2,1,0],![5,4,2,3,0,1],![5,4,2,3,1,0],![5,4,3,2,0,1],![5,4,3,2,1,0]]
def inverseFn : Fin 48 → Fin 6 → Fin 6 := ![![0,1,2,3,4,5],![0,1,2,3,5,4],![0,1,3,2,4,5],![0,1,3,2,5,4],![1,0,2,3,4,5],![1,0,2,3,5,4],![1,0,3,2,4,5],![1,0,3,2,5,4],![0,1,4,5,2,3],![0,1,5,4,2,3],![0,1,4,5,3,2],![0,1,5,4,3,2],![1,0,4,5,2,3],![1,0,5,4,2,3],![1,0,4,5,3,2],![1,0,5,4,3,2],![2,3,0,1,4,5],![2,3,0,1,5,4],![3,2,0,1,4,5],![3,2,0,1,5,4],![2,3,1,0,4,5],![2,3,1,0,5,4],![3,2,1,0,4,5],![3,2,1,0,5,4],![4,5,0,1,2,3],![5,4,0,1,2,3],![4,5,0,1,3,2],![5,4,0,1,3,2],![4,5,1,0,2,3],![5,4,1,0,2,3],![4,5,1,0,3,2],![5,4,1,0,3,2],![2,3,4,5,0,1],![2,3,5,4,0,1],![3,2,4,5,0,1],![3,2,5,4,0,1],![2,3,4,5,1,0],![2,3,5,4,1,0],![3,2,4,5,1,0],![3,2,5,4,1,0],![4,5,2,3,0,1],![5,4,2,3,0,1],![4,5,3,2,0,1],![5,4,3,2,0,1],![4,5,2,3,1,0],![5,4,2,3,1,0],![4,5,3,2,1,0],![5,4,3,2,1,0]]
theorem permutation_left : ∀ r i, inverseFn r (permutationFn r i) = i := by decide +kernel
theorem permutation_right : ∀ r i, permutationFn r (inverseFn r i) = i := by decide +kernel
def permutation (r : Fin 48) : Fin 6 ≃ Fin 6 where
  toFun := permutationFn r
  invFun := inverseFn r
  left_inv := permutation_left r
  right_inv := permutation_right r
theorem permutation_preserves : ∀ r i j, pairDegree (permutation r i) (permutation r j) = pairDegree i j := by decide +kernel
theorem pivot_covers : ∀ T : Finset (Fin 6), 4 ≤ T.card → T.card ≤ 5 →
    ∃ c : Fin 3, ∃ r : Fin 48, (pivot c).image (permutation r) = T := by decide +kernel
def canonical : Fin 58 → Fin 3 := ![0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]
def catalog : Fin 58 → Fin 10 → Bool := ![![false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false],![true,true,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false],![false,true,true,false,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,false],![true,false,false,true,false,false,false,false,false,false],![false,false,true,true,false,false,false,false,false,false],![false,false,false,false,true,false,false,false,false,false],![false,true,false,false,true,false,false,false,false,false],![false,false,false,true,true,false,false,false,false,false],![false,false,false,false,false,true,false,false,false,false],![false,true,false,false,false,true,false,false,false,false],![false,false,false,true,false,true,false,false,false,false],![false,false,false,false,true,true,false,false,false,false],![false,true,false,false,true,true,false,false,false,false],![false,false,false,true,true,true,false,false,false,false],![false,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,false,true,false,false,false],![false,false,false,true,false,false,true,false,false,false],![false,false,false,false,false,false,false,true,false,false],![true,false,false,false,false,false,false,true,false,false],![false,false,true,false,false,false,false,true,false,false],![false,false,false,false,true,false,false,true,false,false],![false,false,false,false,false,true,false,true,false,false],![false,false,false,false,false,false,true,true,false,false],![false,false,false,false,false,false,false,false,true,false],![true,false,false,false,false,false,false,false,true,false],![false,false,true,false,false,false,false,false,true,false],![false,false,false,false,true,false,false,false,true,false],![false,false,false,false,false,true,false,false,true,false],![false,false,false,false,false,false,true,false,true,false],![false,false,false,false,false,false,false,true,true,false],![true,false,false,false,false,false,false,true,true,false],![false,false,true,false,false,false,false,true,true,false],![false,false,false,false,false,false,false,false,false,true],![true,false,false,false,false,false,false,false,false,true],![false,false,true,false,false,false,false,false,false,true],![false,false,false,false,true,false,false,false,false,true],![false,false,false,false,false,true,false,false,false,true],![false,false,false,false,false,false,true,false,false,true],![false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false],![false,false,true,false,false,false,false,false,false,false],![false,false,false,true,false,false,false,false,false,false],![false,false,false,false,true,false,false,false,false,false],![false,false,false,false,false,true,false,false,false,false],![true,false,false,false,false,true,false,false,false,false],![false,true,false,false,false,true,false,false,false,false],![false,false,false,false,false,false,true,false,false,false],![true,false,false,false,false,false,true,false,false,false],![false,true,false,false,false,false,true,false,false,false],![false,false,false,false,false,false,false,false,false,false],![true,false,false,false,false,false,false,false,false,false],![false,true,false,false,false,false,false,false,false,false],![true,true,false,false,false,false,false,false,false,false]]
def representative : Fin 58 → Fin 22 := ![0,1,1,7,1,8,1,8,7,14,17,17,14,17,17,16,20,20,15,19,19,14,17,17,18,18,19,14,17,17,18,18,19,16,20,20,15,19,19,19,19,21,2,3,3,10,10,11,5,9,12,5,12,9,4,6,6,13]
def relabel : Fin 58 → Fin 48 := ![32,44,36,36,40,32,32,36,32,41,38,34,40,36,32,24,10,8,24,44,40,33,46,42,13,9,28,32,44,40,12,8,24,8,26,24,8,36,32,12,8,0,30,46,30,29,28,26,37,37,42,21,26,21,36,44,36,36]
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem covers_vector : ∀ c : Fin 3, ∀ b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 : Bool,
    Admissible c ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9] → ∃ s : Fin 58, canonical s = c ∧
      ∀ a, ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9] a = catalog s a := by
  intro c
  fin_cases c <;> intro b0 b1 b2 <;> cases b0 <;> cases b1 <;> cases b2 <;> unfold Admissible <;> decide +kernel
theorem covers (c : Fin 3) (h : Fin 10 → Bool) (ha : Admissible c h) :
    ∃ s : Fin 58, canonical s = c ∧ ∀ a, h a = catalog s a := by
  have hv : ![h 0,h 1,h 2,h 3,h 4,h 5,h 6,h 7,h 8,h 9] = h := by funext a; fin_cases a <;> rfl
  have hb := covers_vector c (h 0) (h 1) (h 2) (h 3) (h 4) (h 5) (h 6) (h 7) (h 8) (h 9)
  rw [hv] at hb
  exact hb ha
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem representative_counts : ∀ s T, 3 ≤ T.card →
    highValue (canonical s) (catalog s) (T.image (permutation (relabel s))) = counts (representative s) T := by
  intro s
  fin_cases s <;> decide +kernel
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovery_formula : ∀ s T,
    MultiLockRecovery.recovered lowData (counts s) T = counts s T := by
  intro s
  fin_cases s <;> decide +kernel
end Aris4Math.ThirtyThree.TwentyThreeHighSixCatalog

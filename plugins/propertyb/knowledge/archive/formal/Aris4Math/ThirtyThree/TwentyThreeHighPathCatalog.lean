import Aris4Math.ThirtyThree.TwentyThreeHighPathData

/-! Complete local Boolean-trace classification for P3 and P3+K2. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighPathCatalog
open scoped BigOperators
open TwentyThreeHighPathData (extra catalog counts)
def largeTypes : Fin 16 → Finset (Fin 5) := ![{0,1,2},{0,1,3},{0,2,3},{1,2,3},{0,1,2,3},{0,1,4},{0,2,4},{1,2,4},{0,1,2,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]
theorem largeTypes_injective : Function.Injective largeTypes := by decide +kernel
theorem largeTypes_card : ∀ a, 3 ≤ (largeTypes a).card := by decide +kernel
theorem largeTypes_complete : ∀ T : Finset (Fin 5), 3 ≤ T.card → ∃ a, largeTypes a = T := by decide +kernel
def pairDegree (e : Fin 2) (i j : Fin 5) : ℕ :=
  if ({i,j} : Finset (Fin 5)) = {0,1} ∨ ({i,j} : Finset (Fin 5)) = {1,2} then 2 else
  if ({i,j} : Finset (Fin 5)) = {3,4} then e.val+1 else 1
def lowData (e : Fin 2) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then 7 else
  if T = {0,1} ∨ T = {1,2} then 2 else if T = {3,4} then e.val+1 else 1
def highValue (h : Fin 16 → Bool) (T : Finset (Fin 5)) : ℕ :=
  if ∃ a : Fin 16, largeTypes a = T ∧ h a = true then 1 else 0
def pairSum (h : Fin 16 → Bool) (i j : Fin 5) : ℕ :=
  ∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then
    if h a then 1 else 0 else 0
def Admissible (e : Fin 2) (h : Fin 16 → Bool) : Prop :=
  ∀ i j : Fin 5, i ≠ j → pairSum h i j ≤ pairDegree e i j

def FastAdmissible (e : Fin 2) (h : Fin 16 → Bool) : Prop :=
  ((if h 0 then 1 else 0) + (if h 1 then 1 else 0) + (if h 4 then 1 else 0) + (if h 5 then 1 else 0) + (if h 8 then 1 else 0) + (if h 11 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 2 ∧
  ((if h 0 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 1 then 1 else 0) + (if h 2 then 1 else 0) + (if h 4 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 6 then 1 else 0) + (if h 8 then 1 else 0) + (if h 9 then 1 else 0) + (if h 11 then 1 else 0) + (if h 13 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 0 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 2 ∧
  ((if h 1 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 5 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 2 then 1 else 0) + (if h 3 then 1 else 0) + (if h 4 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 6 then 1 else 0) + (if h 7 then 1 else 0) + (if h 8 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ 1 ∧
  ((if h 9 then 1 else 0) + (if h 10 then 1 else 0) + (if h 11 then 1 else 0) + (if h 12 then 1 else 0) + (if h 13 then 1 else 0) + (if h 14 then 1 else 0) + (if h 15 then 1 else 0) : ℕ) ≤ e.val+1

set_option maxHeartbeats 1000000 in
theorem admissible_fast (e : Fin 2) (h : Fin 16 → Bool) (ha : Admissible e h) : FastAdmissible e h := by
  unfold FastAdmissible
  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩
  · have hb := ha 0 1 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 2 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 3 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 0 4 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 2 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 3 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 1 4 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 3 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 2 4 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb
  · have hb := ha 3 4 (by decide)
    norm_num [pairDegree] at hb
    simp only [pairSum,Fin.sum_univ_succ] at hb
    simpa [largeTypes,Nat.add_assoc] using hb

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem covers_vector : ∀ e : Fin 2, ∀ b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool,
    FastAdmissible e ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] → ∃ s : Fin 115, extra s = e ∧
      ∀ a, ![b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15] a = catalog s a := by
  intro e
  fin_cases e <;> intro b0 b1 b2 b3 <;>
    cases b0 <;> cases b1 <;> cases b2 <;> cases b3 <;>
    unfold FastAdmissible <;> decide +kernel

theorem covers (e : Fin 2) (h : Fin 16 → Bool) (admissible : Admissible e h) :
    ∃ s : Fin 115, extra s = e ∧ ∀ a, h a = catalog s a := by
  have hv : ![h 0,h 1,h 2,h 3,h 4,h 5,h 6,h 7,h 8,h 9,h 10,h 11,h 12,h 13,h 14,h 15] = h := by funext a; fin_cases a <;> rfl
  have bound := covers_vector e (h 0) (h 1) (h 2) (h 3) (h 4) (h 5) (h 6) (h 7) (h 8) (h 9) (h 10) (h 11) (h 12) (h 13) (h 14) (h 15)
  rw [hv] at bound
  exact bound (admissible_fast e h admissible)

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem catalog_counts : ∀ s T, 3 ≤ T.card → highValue (catalog s) T = counts s T := by
  intro s
  fin_cases s <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recovery_formula : ∀ s T,
    MultiLockRecovery.recovered (lowData (extra s)) (counts s) T = counts s T := by
  intro s
  fin_cases s <;> decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeHighPathCatalog

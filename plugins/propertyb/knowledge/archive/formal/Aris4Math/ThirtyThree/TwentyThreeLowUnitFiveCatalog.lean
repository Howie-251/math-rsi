import Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveBare
import Aris4Math.ThirtyThree.TwentyThreeTwoLowHighCatalog

namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog
open MultiLockRecovery
open TwentyThreeTwoLowHighCatalog
open TwentyFourMatchingHighCatalog (highValue)

def low (a : ℕ) (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then (if 4 ∈ T then 6 else 7) else
  if T = {0,1} then a else if T = {2,3} then 3 else 1

def permFn : Fin 24 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,3,2,4],![0,2,1,3,4],![0,2,3,1,4],![0,3,1,2,4],![0,3,2,1,4],![1,0,2,3,4],![1,0,3,2,4],![1,2,0,3,4],![1,2,3,0,4],![1,3,0,2,4],![1,3,2,0,4],![2,0,1,3,4],![2,0,3,1,4],![2,1,0,3,4],![2,1,3,0,4],![2,3,0,1,4],![2,3,1,0,4],![3,0,1,2,4],![3,0,2,1,4],![3,1,0,2,4],![3,1,2,0,4],![3,2,0,1,4],![3,2,1,0,4]]
def invFn : Fin 24 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![0,1,3,2,4],![0,2,1,3,4],![0,3,1,2,4],![0,2,3,1,4],![0,3,2,1,4],![1,0,2,3,4],![1,0,3,2,4],![2,0,1,3,4],![3,0,1,2,4],![2,0,3,1,4],![3,0,2,1,4],![1,2,0,3,4],![1,3,0,2,4],![2,1,0,3,4],![3,1,0,2,4],![2,3,0,1,4],![3,2,0,1,4],![1,2,3,0,4],![1,3,2,0,4],![2,1,3,0,4],![3,1,2,0,4],![2,3,1,0,4],![3,2,1,0,4]]
theorem left_inverse : ∀ r i, invFn r (permFn r i) = i := by decide +kernel
theorem right_inverse : ∀ r i, permFn r (invFn r i) = i := by decide +kernel
def permutation (r : Fin 24) : Fin 5 ≃ Fin 5 :=
  ⟨permFn r,invFn r,left_inverse r,right_inverse r⟩
def winner : Fin 3 → Fin 55 → Fin 75 := ![![0,1,1,0,2,2,3,4,5,0,0,0,6,6,7,0,8,9,10,8,9,10,11,0,8,9,10,12,8,9,10,12,11,0,13,14,14,0,15,15,16,17,18,0,0,0,19,19,20,0,21,22,21,22,23],![24,25,25,26,27,27,28,29,30,31,31,0,32,32,33,34,35,36,37,35,36,37,38,39,35,36,37,40,35,36,37,40,38,39,41,42,42,43,44,44,45,46,47,48,48,0,49,49,50,51,52,53,52,53,54],![55,56,56,57,56,56,57,58,59,60,60,61,62,62,63,64,65,66,66,65,66,66,67,68,65,66,66,69,65,66,66,69,67,68,59,62,62,63,60,60,61,64,70,71,71,72,71,71,72,73,67,68,67,68,74]]
def perm : Fin 3 → Fin 55 → Fin 24 := ![![0,0,1,0,0,6,0,0,0,0,0,0,0,6,0,0,0,0,0,6,6,6,0,0,1,1,1,0,7,7,7,1,1,0,0,0,1,0,0,6,0,0,0,0,0,0,0,6,0,0,0,0,6,6,0],![0,0,1,0,0,6,0,0,0,0,1,0,0,6,0,0,0,0,0,6,6,6,0,0,1,1,1,0,7,7,7,1,1,1,0,0,1,0,0,6,0,0,0,0,1,0,0,6,0,0,0,0,6,6,0],![0,0,1,0,16,17,16,0,0,0,1,0,0,6,0,0,0,0,16,6,6,17,0,0,1,1,22,0,7,7,23,1,1,1,16,16,22,16,16,17,16,16,0,0,1,0,16,17,16,0,16,16,17,17,0]]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem choice_exact : ∀ a : Fin 3, ∀ s : Fin 55,
    Admissible (a.val+1) 3 (catalog s) →
    ∀ T : Finset (Fin 5),
      recovered (low (a.val+1)) (highValue (catalog s))
        (T.image (permutation (perm a s))) =
          TwentyThreeLowUnitFiveBare.counts (winner a s) T := by
  intro a s
  fin_cases a <;> fin_cases s <;> unfold Admissible <;> decide +kernel

theorem classify (a : ℕ) (h : Fin 16 → Bool)
    (ha : 1 ≤ a ∧ a ≤ 3) (admissible : Admissible a 3 h) :
    ∃ k : Fin 75, ∃ σ : Fin 5 ≃ Fin 5, ∀ T : Finset (Fin 5),
      recovered (low a) (highValue h) (T.image σ) =
        TwentyThreeLowUnitFiveBare.counts k T := by
  obtain ⟨s,hs⟩ := covers a 3 h ha.2 (by omega) admissible
  have heq : h = catalog s := funext hs
  subst h
  let aa : Fin 3 := ⟨a-1,by omega⟩
  have ae : aa.val+1 = a := by dsimp [aa]; omega
  refine ⟨winner aa s,permutation (perm aa s),?_⟩
  have result := choice_exact aa s
  rw [ae] at result
  exact result admissible

end Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog.classify

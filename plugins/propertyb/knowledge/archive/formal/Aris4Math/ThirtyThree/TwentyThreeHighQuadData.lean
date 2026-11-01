import Aris4Math.ThirtyThree.QuadProfiles
import Aris4Math.ThirtyThree.TwentyTwoPureDeletion
import Aris4Math.ThirtyThree.CustomDeletion

/-! Seven complete labeled four-lock profiles: degrees seven, pair 01
of codegree three, every other pair of codegree one. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighQuadData
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open scoped BigOperators

def co : Fin 6 → ℕ := ![3,1,1,1,1,1]
def high : Fin 7 → Fin 5 → ℕ := ![![0,0,0,0,0],![0,0,0,0,1],![0,0,0,1,0],![0,0,1,0,0],![0,1,0,0,0],![1,0,0,0,0],![1,1,0,0,0]]
def positionFn : Fin 7 → Fin 4 → Fin 23 := ![![4,12,10,11],![4,13,10,11],![12,4,10,11],![4,12,10,11],![4,13,11,10],![4,13,10,11],![4,13,10,11]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Fin 7) : Fin 4 ↪ Fin 23 := ⟨positionFn i,positionFn_injective i⟩
def counts (i : Fin 7) : Finset (Fin 4) → ℕ := recovered 33 (fun _ => 7) co (high i)
def p (i : Fin 7) : Numeric.Profile :=
  pruneZero ⟨23, executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T,counts i T⟩), none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Fin 7) : p i =
    profile (positions i) (counts i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 7 → Numeric.Profile := ![⟨23,[5,11,12,13],[⟨[],13⟩,⟨[5],2⟩,⟨[13],2⟩,⟨[5,13],3⟩,⟨[11],4⟩,⟨[5,11],1⟩,⟨[11,13],1⟩,⟨[12],4⟩,⟨[5,12],1⟩,⟨[12,13],1⟩,⟨[11,12],1⟩],none,[5,13,11,12]⟩,⟨23,[5,11,12,14],[⟨[],10⟩,⟨[5],4⟩,⟨[14],4⟩,⟨[5,14],2⟩,⟨[11],6⟩,⟨[12],6⟩,⟨[5,11,12,14],1⟩],none,[5,14,11,12]⟩,⟨23,[5,11,12,13],[⟨[],12⟩,⟨[13],2⟩,⟨[5],3⟩,⟨[5,13],3⟩,⟨[11],5⟩,⟨[11,13],1⟩,⟨[12],5⟩,⟨[12,13],1⟩,⟨[5,11,12],1⟩],none,[13,5,11,12]⟩,⟨23,[5,11,12,13],[⟨[],12⟩,⟨[5],3⟩,⟨[13],2⟩,⟨[5,13],3⟩,⟨[11],5⟩,⟨[11,13],1⟩,⟨[12],5⟩,⟨[12,13],1⟩,⟨[5,11,12],1⟩],none,[5,13,11,12]⟩,⟨23,[5,11,12,14],[⟨[],12⟩,⟨[5],3⟩,⟨[14],3⟩,⟨[5,14],2⟩,⟨[12],4⟩,⟨[5,12],1⟩,⟨[12,14],1⟩,⟨[11],5⟩,⟨[5,11,14],1⟩,⟨[11,12],1⟩],none,[5,14,12,11]⟩,⟨23,[5,11,12,14],[⟨[],12⟩,⟨[5],3⟩,⟨[14],3⟩,⟨[5,14],2⟩,⟨[11],5⟩,⟨[5,11,14],1⟩,⟨[12],4⟩,⟨[5,12],1⟩,⟨[12,14],1⟩,⟨[11,12],1⟩],none,[5,14,11,12]⟩,⟨23,[5,11,12,14],[⟨[],11⟩,⟨[5],4⟩,⟨[14],4⟩,⟨[5,14],1⟩,⟨[11],5⟩,⟨[5,11,14],1⟩,⟨[12],5⟩,⟨[5,12,14],1⟩,⟨[11,12],1⟩],none,[5,14,11,12]⟩]
theorem p_eq_computed (i : Fin 7) : p i = computed i := by fin_cases i <;> rfl
def c : Fin 7 → Fin 4 → ℚ := ![![0,0,36/4199,36/4199],![0,0,0,0],![0,0,0,36/4199],![0,0,0,36/4199],![0,0,36/4199,0],![0,0,0,36/4199],![0,0,0,0]]
def d : Fin 7 → Fin 4 → ℚ := ![![1/1938,42/4199,6/4199,6/4199],![1/1938,42/4199,42/4199,42/4199],![42/4199,1/1938,42/4199,6/4199],![1/1938,42/4199,42/4199,6/4199],![1/1938,42/4199,6/4199,42/4199],![1/1938,42/4199,42/4199,6/4199],![1/1938,42/4199,42/4199,42/4199]]
def lossAt : Fin 7 → Fin 4 → ℚ := ![![0,0,36/4199,36/4199],![0,0,84/4199,84/4199],![0,0,42/4199,6/323],![0,0,42/4199,6/323],![0,0,36/4199,42/4199],![0,0,42/4199,36/4199],![0,0,42/4199,42/4199]]

def loss (i : Fin 7) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then lossAt i 0 else
  if k=(positions i 1).val+1 then lossAt i 1 else
  if k=(positions i 2).val+1 then lossAt i 2 else
  if k=(positions i 3).val+1 then lossAt i 3 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem certificates : ∀ i : Fin 7,
    Numeric.validProfile (p i) 33 ∧
    (∑ k : Fin 23, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 4, let k := (positions i j).val+1
      0 ≤ c i j ∧ 0 ≤ d i j ∧
      loss i k ≤ 2*c i j + ((4*counts i {j}+2-19)/3 : ℕ)*d i j -
        TwentyTwoPureDeletion.penaltySum (p i) k (c i j) (d i j) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeHighQuadData

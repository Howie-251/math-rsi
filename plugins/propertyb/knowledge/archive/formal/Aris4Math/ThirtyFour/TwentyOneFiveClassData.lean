import Aris4Math.ThirtyFour.TwentyOneFiveQuadData
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

namespace Aris4Math.ThirtyFour.TwentyOneFiveClassification
open Aris4Math.ThirtyFour.TwentyOneFiveQuadData (Case coData highData)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Kind := Fin 4
def degrees : Kind → Fin 4 → ℕ := ![![5,7,7,7],![5,7,7,8],![5,7,8,8],![5,8,8,8]]
def co (a b c : ℕ) : Fin 6 → ℕ := ![1,1,1,a,b,c]
def Assumptions (kind : Kind) (c : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  (kind=0 → c 3=2 ∧ c 4=2 ∧ c 5=2 ∧ h 4=1) ∧
  (kind=1 → c 3=2 ∧ h 0+h 4=1 ∧ h 1+h 4=0 ∧ h 2+h 4=0) ∧
  (kind=2 → h 0+h 4=0 ∧ h 1+h 4=0)
instance (k c h) : Decidable (Assumptions k c h) := by unfold Assumptions; infer_instance

def Residue (kind : Kind) (c : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  (kind=2 ∧ c 3=1 ∧ c 4=1 ∧ ∀ j, h j=0) ∨ (kind=3 ∧ h 4=0)
instance (k c h) : Decidable (Residue k c h) := by unfold Residue; infer_instance

def Suitable (kind : Kind) (c : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  ∃ i : Case, (∀ j, degrees kind j=TwentyOneFiveQuadData.degree i j) ∧
    (∀ j, c j=coData i j) ∧ ∀ j, h j=highData i j
instance (k c h) : Decidable (Suitable k c h) := by unfold Suitable; infer_instance

theorem coverage : ∀ kind : Kind, ∀ a b c : Fin 2, ∀ h : Fin 5 → Fin 3,
    Assumptions kind (co (a.val+1) (b.val+1) (c.val+1)) (fun j => (h j).val) →
    (∀ j, highPairSum (fun z => (h z).val) j ≤ co (a.val+1) (b.val+1) (c.val+1) j) →
    Residue kind (co (a.val+1) (b.val+1) (c.val+1)) (fun j => (h j).val) ∨
      Suitable kind (co (a.val+1) (b.val+1) (c.val+1)) (fun j => (h j).val) := by
  intro kind a b c
  fin_cases kind <;> fin_cases a <;> fin_cases b <;> fin_cases c <;> decide +kernel
end Aris4Math.ThirtyFour.TwentyOneFiveClassification

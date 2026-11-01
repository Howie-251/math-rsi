import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.TwentyOneDeletion
import Aris4Math.ThirtyThree.CustomDeletion
import Aris4Math.ThirtyThree.OrdinaryLink

/-! All 24 labelled three-lock profiles for the 21-vertex structural alternatives.
The finite table records only degrees, codegrees, triple count and lock positions;
actual multiplicity recovery and actual link deletion are proved separately. -/
namespace Aris4Math.ThirtyThree.TwentyOneTriples

open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
open Aris4Math.ThirtyThree.OrdinaryLink

structure Data where
  d : ℕ
  e : ℕ
  f : ℕ
  a : ℕ
  b : ℕ
  c : ℕ
  t : ℕ
  boost : Bool
  deriving DecidableEq

def data : Fin 24 → Data := ![
  ⟨5,8,8,1,1,1,0,false⟩,
  ⟨6,7,7,2,2,1,0,false⟩,
  ⟨6,7,7,2,2,1,1,false⟩,
  ⟨6,7,7,2,2,2,0,false⟩,
  ⟨6,7,7,2,2,2,1,false⟩,
  ⟨6,7,7,2,2,2,2,false⟩,
  ⟨6,7,8,2,1,1,0,false⟩,
  ⟨7,7,7,1,1,1,0,false⟩,
  ⟨7,7,7,1,1,1,1,true⟩,
  ⟨7,7,7,1,1,2,0,false⟩,
  ⟨7,7,7,1,1,2,1,true⟩,
  ⟨7,7,7,1,2,1,0,false⟩,
  ⟨7,7,7,1,2,1,1,true⟩,
  ⟨7,7,7,1,2,2,0,false⟩,
  ⟨7,7,7,1,2,2,1,false⟩,
  ⟨7,7,7,2,1,1,0,false⟩,
  ⟨7,7,7,2,1,1,1,true⟩,
  ⟨7,7,7,2,1,2,0,false⟩,
  ⟨7,7,7,2,1,2,1,false⟩,
  ⟨7,7,7,2,2,1,0,false⟩,
  ⟨7,7,7,2,2,1,1,false⟩,
  ⟨7,7,7,2,2,2,0,false⟩,
  ⟨7,7,7,2,2,2,1,false⟩,
  ⟨7,7,7,2,2,2,2,false⟩]

def positionFn : Fin 24 → Fin 3 → Fin 21 := ![
  ![10,11,12],
  ![11,8,9],
  ![11,8,9],
  ![10,8,12],
  ![10,8,12],
  ![10,8,12],
  ![11,8,9],
  ![9,10,11],
  ![9,10,11],
  ![10,8,12],
  ![10,8,12],
  ![8,10,12],
  ![8,10,12],
  ![8,9,11],
  ![8,9,11],
  ![8,12,10],
  ![8,12,10],
  ![8,11,9],
  ![8,11,9],
  ![11,8,9],
  ![11,8,9],
  ![8,10,12],
  ![8,10,12],
  ![8,10,12]]

theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide

def positions (i : Fin 24) : Fin 3 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def degree (i : Fin 24) : Fin 3 → ℕ := ![(data i).d,(data i).e,(data i).f]
def codegree (i : Fin 24) : Fin 3 → Fin 3 → ℕ :=
  ![![0,(data i).a,(data i).b],![(data i).a,0,(data i).c],![(data i).b,(data i).c,0]]
def other (j : Fin 3) : Fin 3 := if j=0 then 1 else 0

def μ (i : Fin 24) : Finset (Fin 3) → ℕ :=
  recovered 33 (data i).d (data i).e (data i).f (data i).a (data i).b (data i).c (data i).t

def p (i : Fin 24) : Numeric.Profile :=
  pruneZero ⟨21, executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩), none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Fin 24) : p i =
    profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]

def computed : Fin 24 → Numeric.Profile := ![
  ⟨21,[11,12,13],[⟨[],15⟩,⟨[11],3⟩,⟨[12],6⟩,⟨[13],6⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩],none,[11,12,13]⟩,
  ⟨21,[9,10,12],[⟨[],18⟩,⟨[12],2⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,12],2⟩,⟨[10,12],2⟩,⟨[9,10],1⟩],none,[12,9,10]⟩,
  ⟨21,[9,10,12],[⟨[],17⟩,⟨[12],3⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,10,12],1⟩],none,[12,9,10]⟩,
  ⟨21,[9,11,13],[⟨[],19⟩,⟨[11],2⟩,⟨[9],3⟩,⟨[13],3⟩,⟨[9,11],2⟩,⟨[11,13],2⟩,⟨[9,13],2⟩],none,[11,9,13]⟩,
  ⟨21,[9,11,13],[⟨[],18⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[13],4⟩,⟨[9,11],1⟩,⟨[11,13],1⟩,⟨[9,13],1⟩,⟨[9,11,13],1⟩],none,[11,9,13]⟩,
  ⟨21,[9,11,13],[⟨[],17⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[13],5⟩,⟨[9,11,13],2⟩],none,[11,9,13]⟩,
  ⟨21,[9,10,12],[⟨[],16⟩,⟨[12],3⟩,⟨[9],4⟩,⟨[10],6⟩,⟨[9,12],2⟩,⟨[10,12],1⟩,⟨[9,10],1⟩],none,[12,9,10]⟩,
  ⟨21,[10,11,12],[⟨[],15⟩,⟨[10],5⟩,⟨[11],5⟩,⟨[12],5⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩],none,[10,11,12]⟩,
  ⟨21,[10,11,12],[⟨[],14⟩,⟨[10],6⟩,⟨[11],6⟩,⟨[12],6⟩,⟨[10,11,12],1⟩],none,[10,11,12]⟩,
  ⟨21,[9,11,13],[⟨[],16⟩,⟨[11],5⟩,⟨[9],4⟩,⟨[13],4⟩,⟨[9,11],1⟩,⟨[11,13],1⟩,⟨[9,13],2⟩],none,[11,9,13]⟩,
  ⟨21,[9,11,13],[⟨[],15⟩,⟨[11],6⟩,⟨[9],5⟩,⟨[13],5⟩,⟨[9,13],1⟩,⟨[9,11,13],1⟩],none,[11,9,13]⟩,
  ⟨21,[9,11,13],[⟨[],16⟩,⟨[9],4⟩,⟨[11],5⟩,⟨[13],4⟩,⟨[9,11],1⟩,⟨[9,13],2⟩,⟨[11,13],1⟩],none,[9,11,13]⟩,
  ⟨21,[9,11,13],[⟨[],15⟩,⟨[9],5⟩,⟨[11],6⟩,⟨[13],5⟩,⟨[9,13],1⟩,⟨[9,11,13],1⟩],none,[9,11,13]⟩,
  ⟨21,[9,10,12],[⟨[],17⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[12],3⟩,⟨[9,10],1⟩,⟨[9,12],2⟩,⟨[10,12],2⟩],none,[9,10,12]⟩,
  ⟨21,[9,10,12],[⟨[],16⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[12],4⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,10,12],1⟩],none,[9,10,12]⟩,
  ⟨21,[9,11,13],[⟨[],16⟩,⟨[9],4⟩,⟨[13],4⟩,⟨[11],5⟩,⟨[9,13],2⟩,⟨[9,11],1⟩,⟨[11,13],1⟩],none,[9,13,11]⟩,
  ⟨21,[9,11,13],[⟨[],15⟩,⟨[9],5⟩,⟨[13],5⟩,⟨[11],6⟩,⟨[9,13],1⟩,⟨[9,11,13],1⟩],none,[9,13,11]⟩,
  ⟨21,[9,10,12],[⟨[],17⟩,⟨[9],4⟩,⟨[12],3⟩,⟨[10],4⟩,⟨[9,12],2⟩,⟨[9,10],1⟩,⟨[10,12],2⟩],none,[9,12,10]⟩,
  ⟨21,[9,10,12],[⟨[],16⟩,⟨[9],5⟩,⟨[12],4⟩,⟨[10],5⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,10,12],1⟩],none,[9,12,10]⟩,
  ⟨21,[9,10,12],[⟨[],17⟩,⟨[12],3⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,12],2⟩,⟨[10,12],2⟩,⟨[9,10],1⟩],none,[12,9,10]⟩,
  ⟨21,[9,10,12],[⟨[],16⟩,⟨[12],4⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,10,12],1⟩],none,[12,9,10]⟩,
  ⟨21,[9,11,13],[⟨[],18⟩,⟨[9],3⟩,⟨[11],3⟩,⟨[13],3⟩,⟨[9,11],2⟩,⟨[9,13],2⟩,⟨[11,13],2⟩],none,[9,11,13]⟩,
  ⟨21,[9,11,13],[⟨[],17⟩,⟨[9],4⟩,⟨[11],4⟩,⟨[13],4⟩,⟨[9,11],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[9,11,13],1⟩],none,[9,11,13]⟩,
  ⟨21,[9,11,13],[⟨[],16⟩,⟨[9],5⟩,⟨[11],5⟩,⟨[13],5⟩,⟨[9,11,13],2⟩],none,[9,11,13]⟩]

theorem p_eq_computed (i : Fin 24) : p i = computed i := by
  fin_cases i <;> rfl

def loss (i : Fin 24) (k : ℕ) : ℚ :=
  if (data i).boost ∧ k=11 then 252/12155 else Numeric.deduction (p i) k

def q (d : ℕ) : ℕ := (4*d-20+2)/3

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ i : Fin 24,
    Numeric.validProfile (p i) 33 ∧
    (∑ k : Fin 21, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ((data i).boost → 11 ∈ (p i).correctionCenters) ∧
    ∀ j : Fin 3, let k := (positions i j).val+1
      if (data i).boost ∧ k=11 then
        degree i j = 7 ∧ codegree i j (other j) = 1 ∧
        (∀ t ∈ (p i).types, k ∈ t.locks →
          (positions i (other j)).val+1 ∉ t.locks → t.locks = [11]) ∧
        (126/12155 : ℚ) ≤ Numeric.pairWeight (p i) ⟨[11],0⟩ ⟨[11],0⟩ 11 +
          Numeric.pairWeight (p i) ⟨[11],0⟩ ⟨[11],0⟩ 11
      else
        0 ≤ threshold (p i) k ∧
        Numeric.deduction (p i) k ≤ (q (degree i j) : ℚ)*threshold (p i) k -
          penaltySum (p i) k (threshold (p i) k) := by
  simp only [loss,p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

end Aris4Math.ThirtyThree.TwentyOneTriples

#print axioms Aris4Math.ThirtyThree.TwentyOneTriples.certificates

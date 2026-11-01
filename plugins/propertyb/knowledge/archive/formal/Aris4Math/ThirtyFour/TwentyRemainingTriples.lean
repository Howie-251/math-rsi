import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

/-! Seventeen labelled three-lock degree-eight cases; actual multiplicities and
actual total/pure bad-pair quotas are supplied by general proved interfaces. -/
namespace Aris4Math.ThirtyFour.TwentyRemainingTriples
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
namespace RD
export Aris4Math.ThirtyThree.RefinedDeletion (avoidedPositions avoidedCount penaltySum realized_refined_deduction)
end RD

abbrev Case := Fin 88
structure Data where
  a : ℕ
  b : ℕ
  c : ℕ
  t : ℕ
  high : Bool
  deriving DecidableEq
def data : Case → Data := ![⟨1,1,3,0,true⟩,⟨1,1,3,1,true⟩,⟨1,2,3,0,true⟩,⟨1,2,3,1,true⟩,⟨1,3,1,0,true⟩,⟨1,3,1,1,true⟩,⟨1,3,2,0,true⟩,⟨1,3,2,1,true⟩,⟨1,3,3,0,true⟩,⟨1,3,3,1,true⟩,⟨2,1,3,0,true⟩,⟨2,1,3,1,true⟩,⟨2,2,3,0,true⟩,⟨2,2,3,1,true⟩,⟨2,2,3,2,true⟩,⟨2,3,1,0,true⟩,⟨2,3,1,1,true⟩,⟨2,3,2,0,true⟩,⟨2,3,2,1,true⟩,⟨2,3,2,2,true⟩,⟨2,3,3,0,true⟩,⟨2,3,3,1,true⟩,⟨2,3,3,2,true⟩,⟨3,1,1,0,true⟩,⟨3,1,1,1,true⟩,⟨3,1,2,0,true⟩,⟨3,1,2,1,true⟩,⟨3,1,3,0,true⟩,⟨3,1,3,1,true⟩,⟨3,2,1,0,true⟩,⟨3,2,1,1,true⟩,⟨3,2,2,0,true⟩,⟨3,2,2,1,true⟩,⟨3,2,2,2,true⟩,⟨3,2,3,0,true⟩,⟨3,2,3,1,true⟩,⟨3,2,3,2,true⟩,⟨3,3,1,0,true⟩,⟨3,3,1,1,true⟩,⟨3,3,2,0,true⟩,⟨3,3,2,1,true⟩,⟨3,3,2,2,true⟩,⟨3,3,3,0,true⟩,⟨3,3,3,1,true⟩,⟨3,3,3,2,true⟩,⟨3,3,3,3,true⟩,⟨1,1,1,0,true⟩,⟨1,1,1,1,true⟩,⟨1,2,1,1,true⟩,⟨2,1,1,1,true⟩,⟨1,1,1,0,false⟩,⟨1,1,1,1,false⟩,⟨1,1,3,1,false⟩,⟨1,3,1,1,false⟩,⟨3,1,1,1,false⟩,⟨1,2,3,0,false⟩,⟨2,1,3,0,false⟩,⟨1,3,2,0,false⟩,⟨2,3,1,0,false⟩,⟨3,1,2,0,false⟩,⟨3,2,1,0,false⟩,⟨1,2,3,1,false⟩,⟨2,1,3,1,false⟩,⟨1,3,2,1,false⟩,⟨2,3,1,1,false⟩,⟨3,1,2,1,false⟩,⟨3,2,1,1,false⟩,⟨1,3,3,0,false⟩,⟨3,1,3,0,false⟩,⟨3,3,1,0,false⟩,⟨1,3,3,1,false⟩,⟨3,1,3,1,false⟩,⟨3,3,1,1,false⟩,⟨2,2,3,2,false⟩,⟨2,3,2,2,false⟩,⟨3,2,2,2,false⟩,⟨2,3,3,0,false⟩,⟨3,2,3,0,false⟩,⟨3,3,2,0,false⟩,⟨2,3,3,1,false⟩,⟨3,2,3,1,false⟩,⟨3,3,2,1,false⟩,⟨2,3,3,2,false⟩,⟨3,2,3,2,false⟩,⟨3,3,2,2,false⟩,⟨3,3,3,1,false⟩,⟨3,3,3,2,false⟩,⟨3,3,3,3,false⟩]
def positionFn : Case → Fin 3 → Fin 20 := ![![9,10,8],![9,10,8],![9,8,10],![9,8,10],![10,9,8],![10,9,8],![8,9,10],![8,9,10],![8,9,10],![8,9,10],![9,10,8],![9,10,8],![9,10,8],![9,10,8],![9,10,8],![10,8,9],![10,9,8],![10,9,8],![10,9,8],![10,9,8],![9,8,10],![9,8,10],![9,8,10],![10,8,9],![10,8,9],![9,10,8],![8,10,9],![9,10,8],![9,10,8],![10,8,9],![10,8,9],![10,8,9],![10,8,9],![10,8,9],![9,10,8],![9,10,8],![9,10,8],![10,8,9],![10,8,9],![10,8,9],![10,8,9],![10,8,9],![9,10,8],![9,10,8],![10,8,9],![10,8,9],![6,5,7],![6,5,7],![10,9,8],![10,8,9],![6,5,7],![6,5,7],![9,10,8],![10,9,8],![10,8,9],![8,9,10],![8,10,9],![9,8,10],![10,8,9],![9,10,8],![10,9,8],![9,8,10],![9,10,8],![8,9,10],![10,9,8],![8,10,9],![10,8,9],![8,9,10],![8,10,9],![10,8,9],![8,9,10],![8,10,9],![10,8,9],![9,10,8],![10,9,8],![10,8,9],![8,9,10],![8,10,9],![10,8,9],![8,9,10],![8,10,9],![10,8,9],![8,9,10],![8,10,9],![10,8,9],![9,10,8],![9,10,8],![9,10,8]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 3 ↪ Fin 20 := ⟨positionFn i,positionFn_injective i⟩
def degree (i : Case) (j : Fin 3) : ℕ := if (data i).high && decide (j=0) then 7 else 8
def μ (i : Case) : Finset (Fin 3) → ℕ := recovered 34 (degree i 0) (degree i 1) (degree i 2) (data i).a (data i).b (data i).c (data i).t

def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨20,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Case) : p i =
    profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨20,[9,10,11],[⟨[],16⟩,⟨[10],5⟩,⟨[11],4⟩,⟨[9],4⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[10],6⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[9],4⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[10,11],2⟩,⟨[9,11],3⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],5⟩,⟨[9],5⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[10],6⟩,⟨[9],4⟩,⟨[10,11],1⟩,⟨[9,11],3⟩,⟨[9,10],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],4⟩,⟨[10],7⟩,⟨[9],5⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],3⟩,⟨[10],5⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[9,11],3⟩,⟨[10,11],2⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],4⟩,⟨[10],6⟩,⟨[11],4⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[9],3⟩,⟨[10],4⟩,⟨[11],2⟩,⟨[9,10],1⟩,⟨[9,11],3⟩,⟨[10,11],3⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],4⟩,⟨[10],5⟩,⟨[11],3⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10,11],2⟩,⟨[9,10],1⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],5⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[10],3⟩,⟨[11],3⟩,⟨[9],3⟩,⟨[10,11],2⟩,⟨[9,10],2⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[11],4⟩,⟨[9],4⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],5⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],2⟩,⟨[9],5⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[10,11],3⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[10],6⟩,⟨[9],5⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],2⟩,⟨[10],4⟩,⟨[9],3⟩,⟨[10,11],2⟩,⟨[9,11],3⟩,⟨[9,10],2⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],3⟩,⟨[10],5⟩,⟨[9],4⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10],1⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],4⟩,⟨[10],6⟩,⟨[9],5⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],19⟩,⟨[10],2⟩,⟨[9],3⟩,⟨[11],2⟩,⟨[9,10],2⟩,⟨[10,11],3⟩,⟨[9,11],3⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[10],3⟩,⟨[9],4⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[10,11],2⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[9],5⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10],6⟩,⟨[9,11],3⟩,⟨[10,11],1⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10],7⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],3⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10,11],3⟩,⟨[9,10],1⟩,⟨[9,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],4⟩,⟨[11],4⟩,⟨[10],6⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[9],4⟩,⟨[10,11],3⟩,⟨[9,10],1⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10,11],2⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],2⟩,⟨[9],4⟩,⟨[10],5⟩,⟨[9,11],3⟩,⟨[10,11],2⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10],6⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],2⟩,⟨[9],3⟩,⟨[10],4⟩,⟨[9,11],3⟩,⟨[10,11],2⟩,⟨[9,10],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10],5⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10],6⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],19⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9],3⟩,⟨[10,11],3⟩,⟨[9,10],2⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[10],3⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10,11],2⟩,⟨[9,10],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10,11],1⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],1⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,11],3⟩,⟨[10,11],3⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],2⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],19⟩,⟨[11],1⟩,⟨[9],3⟩,⟨[10],3⟩,⟨[9,11],3⟩,⟨[10,11],3⟩,⟨[9,10],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],2⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[9,10,11],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],20⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[9],2⟩,⟨[10,11],3⟩,⟨[9,10],3⟩,⟨[9,11],3⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],19⟩,⟨[10],2⟩,⟨[11],3⟩,⟨[9],3⟩,⟨[10,11],2⟩,⟨[9,10],2⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[9,10,11],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,10,11],3⟩],none,[11,9,10]⟩,⟨20,[6,7,8],[⟨[],14⟩,⟨[7],5⟩,⟨[6],6⟩,⟨[8],6⟩,⟨[6,7],1⟩,⟨[7,8],1⟩,⟨[6,8],1⟩],none,[7,6,8]⟩,⟨20,[6,7,8],[⟨[],13⟩,⟨[7],6⟩,⟨[6],7⟩,⟨[8],7⟩,⟨[6,7,8],1⟩],none,[7,6,8]⟩,⟨20,[9,10,11],[⟨[],14⟩,⟨[11],5⟩,⟨[10],7⟩,⟨[9],6⟩,⟨[9,11],1⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],14⟩,⟨[11],5⟩,⟨[9],6⟩,⟨[10],7⟩,⟨[9,11],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[6,7,8],[⟨[],13⟩,⟨[7],6⟩,⟨[6],6⟩,⟨[8],6⟩,⟨[6,7],1⟩,⟨[7,8],1⟩,⟨[6,8],1⟩],none,[7,6,8]⟩,⟨20,[6,7,8],[⟨[],12⟩,⟨[7],7⟩,⟨[6],7⟩,⟨[8],7⟩,⟨[6,7,8],1⟩],none,[7,6,8]⟩,⟨20,[9,10,11],[⟨[],14⟩,⟨[10],7⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],14⟩,⟨[11],5⟩,⟨[10],7⟩,⟨[9],5⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],14⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[10],7⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[10],4⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[9,11],2⟩,⟨[10,11],3⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[9,10],1⟩,⟨[10,11],3⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],4⟩,⟨[9],5⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[10,11],3⟩,⟨[9,11],2⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[10,11],3⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],4⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10,11],3⟩,⟨[9,10],1⟩,⟨[9,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[9],5⟩,⟨[10,11],3⟩,⟨[9,11],2⟩,⟨[9,10],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[10],6⟩,⟨[9],5⟩,⟨[11],4⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,9,11]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[10],6⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[9],5⟩,⟨[10],6⟩,⟨[11],4⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],4⟩,⟨[10],6⟩,⟨[9],5⟩,⟨[10,11],1⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[9],5⟩,⟨[11],4⟩,⟨[10],6⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10],6⟩,⟨[9,11],2⟩,⟨[10,11],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[11],2⟩,⟨[9,10],1⟩,⟨[9,11],3⟩,⟨[10,11],3⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],4⟩,⟨[11],2⟩,⟨[10],4⟩,⟨[9,11],3⟩,⟨[9,10],1⟩,⟨[10,11],3⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],2⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,11],3⟩,⟨[10,11],3⟩,⟨[9,10],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[11],3⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[11],3⟩,⟨[10],5⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],3⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[10],6⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],5⟩,⟨[10],6⟩,⟨[9],5⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[11,10,9]⟩,⟨20,[9,10,11],[⟨[],15⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[10],6⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[9],3⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[9,10],2⟩,⟨[9,11],3⟩,⟨[10,11],3⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[9],3⟩,⟨[11],2⟩,⟨[10],3⟩,⟨[9,11],3⟩,⟨[9,10],2⟩,⟨[10,11],3⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[11],2⟩,⟨[9],3⟩,⟨[10],3⟩,⟨[9,11],3⟩,⟨[10,11],3⟩,⟨[9,10],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[11],3⟩,⟨[9,10],1⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[9],4⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[9,10],1⟩,⟨[10,11],2⟩,⟨[9,10,11],1⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[11],3⟩,⟨[9],4⟩,⟨[10],4⟩,⟨[9,11],2⟩,⟨[10,11],2⟩,⟨[9,10],1⟩,⟨[9,10,11],1⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[11],4⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[9,10,11],2⟩],none,[9,10,11]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[9],5⟩,⟨[11],4⟩,⟨[10],5⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[9,10,11],2⟩],none,[9,11,10]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[11],4⟩,⟨[9],5⟩,⟨[10],5⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[9,10,11],2⟩],none,[11,9,10]⟩,⟨20,[9,10,11],[⟨[],18⟩,⟨[10],3⟩,⟨[11],3⟩,⟨[9],3⟩,⟨[10,11],2⟩,⟨[9,10],2⟩,⟨[9,11],2⟩,⟨[9,10,11],1⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],17⟩,⟨[10],4⟩,⟨[11],4⟩,⟨[9],4⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[9,11],1⟩,⟨[9,10,11],2⟩],none,[10,11,9]⟩,⟨20,[9,10,11],[⟨[],16⟩,⟨[10],5⟩,⟨[11],5⟩,⟨[9],5⟩,⟨[9,10,11],3⟩],none,[10,11,9]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i = computed i := by
  fin_cases i <;> rfl
def losses : Case → Fin 3 → ℚ := ![![(63/2431),(0/1),(0/1)],![(378/12155),(252/12155),(42/2431)],![(42/2431),(0/1),(0/1)],![(126/12155),(42/2431),(0/1)],![(0/1),(105/2431),(0/1)],![(0/1),(504/12155),(42/2431)],![(0/1),(84/2431),(0/1)],![(0/1),(378/12155),(0/1)],![(0/1),(42/2431),(0/1)],![(0/1),(126/12155),(0/1)],![(42/2431),(0/1),(0/1)],![(126/12155),(0/1),(42/2431)],![(21/2431),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(126/12155),(252/12155),(42/2431)],![(0/1),(42/2431),(42/2431)],![(0/1),(378/12155),(42/2431)],![(0/1),(63/2431),(0/1)],![(0/1),(126/12155),(0/1)],![(0/1),(378/12155),(42/2431)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(42/2431),(0/1)],![(0/1),(0/1),(105/2431)],![(0/1),(42/2431),(504/12155)],![(0/1),(0/1),(42/2431)],![(0/1),(0/1),(378/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(42/2431)],![(0/1),(0/1),(84/2431)],![(0/1),(42/2431),(378/12155)],![(0/1),(0/1),(63/2431)],![(0/1),(0/1),(126/12155)],![(0/1),(42/2431),(378/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(42/2431)],![(0/1),(0/1),(42/2431)],![(0/1),(42/2431),(126/12155)],![(0/1),(0/1),(21/2431)],![(0/1),(0/1),(0/1)],![(0/1),(42/2431),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(252/12155),(126/12155)],![(15/3094),(27/3094),(18/1547)],![(27/3094),(18/1547),(45/3094)],![(252/12155),(504/12155),(84/2431)],![(252/12155),(84/2431),(504/12155)],![(27/3094),(27/3094),(18/1547)],![(18/1547),(18/1547),(45/3094)],![(504/12155),(252/12155),(42/2431)],![(252/12155),(504/12155),(42/2431)],![(252/12155),(42/2431),(504/12155)],![(42/2431),(42/2431),(0/1)],![(42/2431),(0/1),(42/2431)],![(42/2431),(42/2431),(0/1)],![(0/1),(42/2431),(42/2431)],![(42/2431),(0/1),(42/2431)],![(0/1),(42/2431),(42/2431)],![(378/12155),(42/2431),(0/1)],![(378/12155),(0/1),(42/2431)],![(42/2431),(378/12155),(0/1)],![(0/1),(378/12155),(42/2431)],![(42/2431),(0/1),(378/12155)],![(0/1),(42/2431),(378/12155)],![(0/1),(42/2431),(0/1)],![(0/1),(0/1),(42/2431)],![(0/1),(0/1),(42/2431)],![(42/2431),(126/12155),(0/1)],![(42/2431),(0/1),(126/12155)],![(0/1),(42/2431),(126/12155)],![(378/12155),(252/12155),(42/2431)],![(252/12155),(378/12155),(42/2431)],![(252/12155),(42/2431),(378/12155)],![(0/1),(21/2431),(0/1)],![(0/1),(0/1),(21/2431)],![(0/1),(0/1),(21/2431)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(42/2431),(126/12155),(0/1)],![(42/2431),(0/1),(126/12155)],![(0/1),(42/2431),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(126/12155),(252/12155),(252/12155)]]
def usePure : Case → Fin 3 → Bool := ![![false,false,false],![true,false,false],![false,false,false],![true,false,false],![false,false,false],![false,true,false],![false,false,false],![false,true,false],![false,false,false],![false,true,false],![false,false,false],![true,false,false],![false,false,false],![false,false,false],![true,false,false],![false,false,false],![false,true,false],![false,false,false],![false,true,false],![false,true,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,true,false],![true,true,false],![false,true,false],![false,false,true],![true,true,false],![true,true,false],![true,false,false],![false,true,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![true,false,false],![true,false,false],![false,true,false],![false,true,false],![false,false,true],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,true,false],![false,false,true],![false,false,true],![true,false,false],![false,true,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,true,false],![false,false,true],![false,false,true],![false,false,false],![false,false,false],![true,false,false]]
def loss (i : Case) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then losses i 0 else
  if k=(positions i 1).val+1 then losses i 1 else
  if k=(positions i 2).val+1 then losses i 2 else 0

def R (j : Fin 3) (_ : Fin 1) : Finset (Fin 3) := Finset.univ.erase j
def pureQ (i : Case) (j : Fin 3) : ℕ := (4*μ i {j}+2-17)/3
def pureWeight (i : Case) (j : Fin 3) : ℚ :=
  2 * Numeric.pairWeight (p i) ⟨[(positions i j).val+1],0⟩
    ⟨[(positions i j).val+1],0⟩ ((positions i j).val+1)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 20, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 3, let k := (positions i j).val+1
      if usePure i j then
        0 ≤ pureWeight i j ∧
        (∀ z : Fin 1, pureQ i j ≤
          (4*RD.avoidedCount (p i) k (RD.avoidedPositions (positions i) (R j z))+2-
            (20-1-(R j z).card))/3) ∧
        loss i k ≤ (∑ _z : Fin 1, (pureQ i j : ℚ)*pureWeight i j) -
          RD.penaltySum (p i) k (fun z => RD.avoidedPositions (positions i) (R j z))
            (fun _z => pureWeight i j)
      else
        0 ≤ threshold (p i) k ∧
        loss i k ≤ (((4*degree i j-19+2)/3 : ℕ) : ℚ)*threshold (p i) k - penaltySum (p i) k (threshold (p i) k) := by
  intro i
  fin_cases i <;> simp only [loss,pureWeight,p_eq_computed] <;>
    unfold Numeric.validProfile <;> decide +kernel

theorem realizes34 (H : Simple5Hypergraph (Fin 20)) (vertices : Fin 3 ↪ Fin 20)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (vertices : Fin 3 ↪ Fin 20) (i : Case)
    (hd : ∀ j, H.degree (vertices j) = degree i j)
    (ha : H.codegree (vertices 0) (vertices 1) = (data i).a)
    (hb : H.codegree (vertices 0) (vertices 2) = (data i).b)
    (hc : H.codegree (vertices 1) (vertices 2) = (data i).c)
    (ht : tripleCodegree H (vertices 0) (vertices 1) (vertices 2) = (data i).t) : PropertyB H := by
  obtain ⟨valid,strict,bounds⟩ := certificates i
  have hm : ∀ T, count H vertices T = μ i T := by
    intro T
    rw [actual_recovered,triple_count_eq,edges34,hd 0,hd 1,hd 2,ha,hb,hc,ht]
    rfl
  have real := realizes34 H vertices i hm valid
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    have hb := bounds j
    dsimp only at hb
    by_cases hp : usePure i j = true
    · rw [if_pos hp] at hb
      obtain ⟨nonneg,quota,bound⟩ := hb
      exact RD.realized_refined_deduction H vertices (positions i) (p i) real j
        (R j) (fun _ : Fin 1 => pureWeight i j) (fun _ => pureQ i j) _
        (fun _ => nonneg) (fun _ => by simp [R]) quota bound
    · rw [if_neg hp] at hb
      apply realized_threshold_deduction H cover vertices (positions i) (p i) real j _ ((4*degree i j-19+2)/3) _ _ rfl
      · rw [hd]
      · exact hb.1
      · exact hb.2
  · intro k hk
    have absent : ∀ j : Fin 3, k ≠ (positions i j).val+1 := by
      intro j he
      apply hk
      simp only [p,pruneZero]
      exact List.mem_ofFn.mpr ⟨j,he.symm⟩
    simp [loss,absent 0,absent 1,absent 2]
  · exact strict

def Matches (a b c t : ℕ) (high : Bool) (i : Case) : Prop :=
  a=(data i).a ∧ b=(data i).b ∧ c=(data i).c ∧ t=(data i).t ∧ (data i).high=high
instance (a b c t : ℕ) (high : Bool) (i : Case) : Decidable (Matches a b c t high i) := by
  unfold Matches; infer_instance

def Suitable (seven : Bool) (a b c t : ℕ) : Prop := ∃ i : Case, Matches a b c t seven i
instance (seven : Bool) (a b c t : ℕ) : Decidable (Suitable seven a b c t) := by
  unfold Suitable Matches; infer_instance

set_option maxHeartbeats 0 in
theorem seven_high_strict : ∀ a b c t : Fin 4,
    1 ≤ a.val → 1 ≤ b.val → 1 ≤ c.val →
    t.val ≤ a.val → t.val ≤ b.val → t.val ≤ c.val →
    (a.val=3 ∨ b.val=3 ∨ c.val=3) → Suitable true a.val b.val c.val t.val := by decide +kernel

theorem propertyB_of_suitable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card=34) (x y z : Fin 20)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z) (seven : Bool)
    (dx : H.degree x=if seven then 7 else 8) (dy : H.degree y=8) (dz : H.degree z=8)
    (suitable : Suitable seven (H.codegree x y) (H.codegree x z) (H.codegree y z)
      (tripleCodegree H x y z)) : PropertyB H := by
  obtain ⟨i,ha,hb,hc,ht,kind⟩ := suitable
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,kind,threeVertices] using dx
    · simpa [degree,kind,threeVertices] using dy
    · simpa [degree,kind,threeVertices] using dz
  · exact ha
  · exact hb
  · exact hc
  · exact ht

end Aris4Math.ThirtyFour.TwentyRemainingTriples
#print axioms Aris4Math.ThirtyFour.TwentyRemainingTriples.propertyB_of_suitable

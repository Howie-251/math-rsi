import Aris4Math.ThirtyThree.TripleProfiles
import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

/-! Seventeen labelled three-lock degree-eight cases; actual multiplicities and
actual total/pure bad-pair quotas are supplied by general proved interfaces. -/
namespace Aris4Math.ThirtyFour.TwentyOneFiveTriples
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.TripleProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
namespace RD
export Aris4Math.ThirtyThree.RefinedDeletion (avoidedPositions avoidedCount penaltySum realized_refined_deduction)
end RD

abbrev Case := Fin 74
structure Data where
  a : ℕ
  b : ℕ
  c : ℕ
  t : ℕ
  d : ℕ
  e : ℕ
  deriving DecidableEq
def data : Case → Data := ![⟨1,1,3,0,8,8⟩,⟨1,1,3,1,8,8⟩,⟨1,1,4,0,8,8⟩,⟨1,1,4,1,8,8⟩,⟨1,1,5,0,8,8⟩,⟨1,1,5,1,8,8⟩,⟨1,1,6,0,8,8⟩,⟨1,1,6,1,8,8⟩,⟨1,1,7,0,8,8⟩,⟨1,1,7,1,8,8⟩,⟨1,1,8,1,8,8⟩,⟨1,1,1,0,5,5⟩,⟨1,1,1,1,5,5⟩,⟨1,1,1,0,5,6⟩,⟨1,1,1,1,5,6⟩,⟨1,1,1,0,5,7⟩,⟨1,1,1,1,5,7⟩,⟨1,1,1,0,5,8⟩,⟨1,1,1,1,5,8⟩,⟨1,1,1,0,6,6⟩,⟨1,1,1,1,6,6⟩,⟨1,1,2,0,6,6⟩,⟨1,1,2,1,6,6⟩,⟨1,1,3,0,6,6⟩,⟨1,1,3,1,6,6⟩,⟨1,1,4,0,6,6⟩,⟨1,1,4,1,6,6⟩,⟨1,1,5,0,6,6⟩,⟨1,1,5,1,6,6⟩,⟨1,1,6,1,6,6⟩,⟨1,1,1,0,6,7⟩,⟨1,1,1,1,6,7⟩,⟨1,1,2,0,6,7⟩,⟨1,1,2,1,6,7⟩,⟨1,1,3,0,6,7⟩,⟨1,1,3,1,6,7⟩,⟨1,1,4,0,6,7⟩,⟨1,1,4,1,6,7⟩,⟨1,1,5,0,6,7⟩,⟨1,1,5,1,6,7⟩,⟨1,1,6,1,6,7⟩,⟨1,1,1,0,6,8⟩,⟨1,1,1,1,6,8⟩,⟨1,1,2,0,6,8⟩,⟨1,1,2,1,6,8⟩,⟨1,1,3,0,6,8⟩,⟨1,1,3,1,6,8⟩,⟨1,1,4,0,6,8⟩,⟨1,1,4,1,6,8⟩,⟨1,1,5,0,6,8⟩,⟨1,1,5,1,6,8⟩,⟨1,1,6,1,6,8⟩,⟨1,1,1,0,7,7⟩,⟨1,1,1,1,7,7⟩,⟨1,1,2,0,7,7⟩,⟨1,1,3,0,7,7⟩,⟨1,1,3,1,7,7⟩,⟨1,1,4,0,7,7⟩,⟨1,1,4,1,7,7⟩,⟨1,1,5,0,7,7⟩,⟨1,1,5,1,7,7⟩,⟨1,1,6,0,7,7⟩,⟨1,1,6,1,7,7⟩,⟨1,1,7,1,7,7⟩,⟨1,1,1,1,7,8⟩,⟨1,1,3,0,7,8⟩,⟨1,1,3,1,7,8⟩,⟨1,1,4,0,7,8⟩,⟨1,1,4,1,7,8⟩,⟨1,1,5,0,7,8⟩,⟨1,1,5,1,7,8⟩,⟨1,1,6,0,7,8⟩,⟨1,1,6,1,7,8⟩,⟨1,1,7,1,7,8⟩]
def positionFn : Case → Fin 3 → Fin 21 := ![![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![9,11,10],![9,11,10],![9,11,10],![9,11,10],![9,11,10],![9,11,10],![9,11,10],![9,11,10],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![9,11,10],![9,11,10],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![9,11,10],![9,11,10],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![9,11,10],![9,11,10],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![9,11,10],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11],![10,9,11]]
theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 3 ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def degree (i : Case) (j : Fin 3) : ℕ := ![5,(data i).d,(data i).e] j
def μ (i : Case) : Finset (Fin 3) → ℕ := recovered 34 (degree i 0) (degree i 1) (degree i 2) (data i).a (data i).b (data i).c (data i).t

def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩

theorem p_eq (i : Case) : p i =
    profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Case → Numeric.Profile := ![⟨21,[10,11,12],[⟨[],18⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],17⟩,⟨[11],4⟩,⟨[10],5⟩,⟨[12],5⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],6⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],7⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,12],6⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[10,12],7⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[11],4⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[11],5⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[11],5⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[11],6⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[11],6⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[11],7⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[11],4⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[10],4⟩,⟨[12],5⟩,⟨[11],5⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],2⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],1⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],24⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],24⟩,⟨[11],4⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[11],5⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[10],4⟩,⟨[12],5⟩,⟨[11],6⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],2⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],5⟩,⟨[10,12],1⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],3⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],4⟩,⟨[12],1⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[11],6⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],17⟩,⟨[10],4⟩,⟨[12],5⟩,⟨[11],7⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],5⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],2⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],6⟩,⟨[10,12],1⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],4⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],5⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],4⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],3⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[12],2⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[10],3⟩,⟨[12],5⟩,⟨[11],5⟩,⟨[10,12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],17⟩,⟨[10],4⟩,⟨[12],6⟩,⟨[11],6⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],3⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],2⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],4⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],3⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],6⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],23⟩,⟨[11],4⟩,⟨[10,12],6⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],16⟩,⟨[10],4⟩,⟨[12],6⟩,⟨[11],7⟩,⟨[10,11,12],1⟩],none,[10,12,11]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],3⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],3⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],18⟩,⟨[11],4⟩,⟨[10],4⟩,⟨[12],5⟩,⟨[10,12],2⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],3⟩,⟨[10],2⟩,⟨[12],3⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],4⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],19⟩,⟨[11],4⟩,⟨[10],3⟩,⟨[12],4⟩,⟨[10,12],3⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],3⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],5⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],20⟩,⟨[11],4⟩,⟨[10],2⟩,⟨[12],3⟩,⟨[10,12],4⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,12],6⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],21⟩,⟨[11],4⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[10,12],5⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩,⟨21,[10,11,12],[⟨[],22⟩,⟨[11],4⟩,⟨[12],1⟩,⟨[10,12],6⟩,⟨[10,11,12],1⟩],none,[11,10,12]⟩]
set_option maxHeartbeats 0 in
theorem p_eq_computed (i : Case) : p i = computed i := by
  fin_cases i <;> rfl
def losses : Case → Fin 3 → ℚ := ![![(0/1),(0/1),(0/1)],![(0/1),(126/12155),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(21/1105)],![(0/1),(0/1),(126/12155)],![(0/1),(0/1),(63/2210)],![(0/1),(0/1),(252/12155)],![(0/1),(0/1),(42/1105)],![(0/1),(0/1),(504/12155)],![(0/1),(21/2210),(21/1105)],![(0/1),(252/12155),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(21/2210),(21/2210)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(21/2210),(63/2210)],![(0/1),(252/12155),(252/12155)],![(0/1),(0/1),(0/1)],![(0/1),(21/2210),(21/1105)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(21/2210),(42/1105)],![(0/1),(252/12155),(504/12155)],![(0/1),(0/1),(126/12155)],![(0/1),(21/2210),(63/2210)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(21/1105),(63/2210)],![(0/1),(378/12155),(252/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(378/12155),(504/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(126/12155)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)],![(0/1),(0/1),(0/1)]]
def usePure : Case → Fin 3 → Bool := ![![false,false,false],![false,true,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,true],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,true],![false,false,false],![false,false,true],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false],![false,false,false]]
def loss (i : Case) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then losses i 0 else
  if k=(positions i 1).val+1 then losses i 1 else
  if k=(positions i 2).val+1 then losses i 2 else 0

def R (j : Fin 3) (_ : Fin 1) : Finset (Fin 3) := Finset.univ.erase j
def pureQ (i : Case) (j : Fin 3) : ℕ := (4*μ i {j}+2-18)/3
def pureWeight (i : Case) (j : Fin 3) : ℚ :=
  2 * Numeric.pairWeight (p i) ⟨[(positions i j).val+1],0⟩
    ⟨[(positions i j).val+1],0⟩ ((positions i j).val+1)

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 21, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 3, let k := (positions i j).val+1
      if usePure i j then
        0 ≤ pureWeight i j ∧
        (∀ z : Fin 1, pureQ i j ≤
          (4*RD.avoidedCount (p i) k (RD.avoidedPositions (positions i) (R j z))+2-
            (21-1-(R j z).card))/3) ∧
        loss i k ≤ (∑ _z : Fin 1, (pureQ i j : ℚ)*pureWeight i j) -
          RD.penaltySum (p i) k (fun z => RD.avoidedPositions (positions i) (R j z))
            (fun _z => pureWeight i j)
      else
        0 ≤ threshold (p i) k ∧
        loss i k ≤ (((4*degree i j-20+2)/3 : ℕ) : ℚ)*threshold (p i) k - penaltySum (p i) k (threshold (p i) k) := by
  intro i
  fin_cases i <;> simp only [loss,pureWeight,p_eq_computed] <;>
    unfold Numeric.validProfile <;> decide +kernel

theorem realizes34 (H : Simple5Hypergraph (Fin 21)) (vertices : Fin 3 ↪ Fin 21)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (vertices : Fin 3 ↪ Fin 21) (i : Case)
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
      apply realized_threshold_deduction H cover vertices (positions i) (p i) real j _ ((4*degree i j-20+2)/3) _ _ rfl
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

def Matches (d e c t : ℕ) (i : Case) : Prop :=
  d=(data i).d ∧ e=(data i).e ∧ c=(data i).c ∧ t=(data i).t
instance (d e c t : ℕ) (i : Case) : Decidable (Matches d e c t i) := by
  unfold Matches; infer_instance

def Suitable (d e c t : ℕ) : Prop := ∃ i : Case, Matches d e c t i
instance (d e c t : ℕ) : Decidable (Suitable d e c t) := by
  unfold Suitable Matches; infer_instance

theorem units (i : Case) : (data i).a=1 ∧ (data i).b=1 := by fin_cases i <;> decide

theorem propertyB_of_suitable (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (edges34 : H.edges.card=34) (x y z : Fin 21)
    (xy : x ≠ y) (xz : x ≠ z) (yz : y ≠ z)
    (dx : H.degree x=5) (a : H.codegree x y=1) (b : H.codegree x z=1)
    (suitable : Suitable (H.degree y) (H.degree z) (H.codegree y z)
      (tripleCodegree H x y z)) : PropertyB H := by
  obtain ⟨i,hd,he,hc,ht⟩ := suitable
  apply propertyB_of_data H cover edges34 (threeVertices x y z xy xz yz) i
  · intro j; fin_cases j
    · simpa [degree,threeVertices] using dx
    · simpa [degree,threeVertices] using hd
    · simpa [degree,threeVertices] using he
  · exact a.trans (units i).1.symm
  · exact b.trans (units i).2.symm
  · exact hc
  · exact ht

set_option maxHeartbeats 0 in
set_option synthInstance.maxSize 1000 in
theorem low_coverage : ∀ d e c : Fin 9, ∀ t : Fin 2,
    5 ≤ d.val → d.val ≤ 6 → d.val ≤ e.val →
    1 ≤ c.val → c.val ≤ d.val → 1+c.val ≤ d.val+t.val →
    (d.val=5 → c.val=1) → Suitable d.val e.val c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem seven_coverage : ∀ c : Fin 8, ∀ t : Fin 2,
    1 ≤ c.val → 1+c.val ≤ 7+t.val →
    (c.val=2 ∧ t.val=1) ∨ Suitable 7 7 c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem mixed_high : ∀ c : Fin 8, ∀ t : Fin 2,
    3 ≤ c.val → 1+c.val ≤ 7+t.val → Suitable 7 8 c.val t.val := by decide +kernel

set_option maxHeartbeats 0 in
theorem eight_high : ∀ c : Fin 9, ∀ t : Fin 2,
    3 ≤ c.val → 1+c.val ≤ 8+t.val → Suitable 8 8 c.val t.val := by decide +kernel

end Aris4Math.ThirtyFour.TwentyOneFiveTriples
#print axioms Aris4Math.ThirtyFour.TwentyOneFiveTriples.propertyB_of_suitable

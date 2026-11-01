import Aris4Math.ThirtyFour.TwentyFourMatchingSelection
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases
namespace Aris4Math.ThirtyFour.TwentyFourSixLowPairPatterns
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Pattern := Fin 3
abbrev Perm := Fin 24
def permFn : Perm→Fin 4→Fin 4 := ![![0,1,2,3],![0,1,3,2],![0,2,1,3],![0,2,3,1],![0,3,1,2],![0,3,2,1],![1,0,2,3],![1,0,3,2],![1,2,0,3],![1,2,3,0],![1,3,0,2],![1,3,2,0],![2,0,1,3],![2,0,3,1],![2,1,0,3],![2,1,3,0],![2,3,0,1],![2,3,1,0],![3,0,1,2],![3,0,2,1],![3,1,0,2],![3,1,2,0],![3,2,0,1],![3,2,1,0]]
theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 4) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
def first : Fin 6→Fin 4 := ![0,0,0,1,1,2]
def second : Fin 6→Fin 4 := ![1,2,3,2,3,3]
def index : Fin 4→Fin 4→Fin 6 := ![![0,0,1,2],![0,0,3,4],![1,3,0,5],![2,4,5,0]]
def adj (r : Fin 6→Bool) (i j : Fin 4) : Bool := r (index i j)
def IsMatching (r : Fin 6→Bool) : Prop :=
  ∀i j k,i≠j→i≠k→adj r i j=true→adj r i k=true→j=k
instance (r : Fin 6→Bool) : Decidable (IsMatching r) := by unfold IsMatching;infer_instance
def canonical (b : Pattern) (i j : Fin 4) : Bool :=
  decide ((1≤b.val ∧ ({i,j} : Finset (Fin 4))={0,1}) ∨
    (2≤b.val ∧ ({i,j} : Finset (Fin 4))={2,3}))
/-- Every matching on four labeled points has zero, one or two disjoint
pairs after an actual permutation. This finite domain is only 64 graphs. -/
theorem normalize : ∀r : Fin 6→Bool,IsMatching r→
    ∃b : Pattern,∃p : Perm,∀i j,i≠j→adj r (perm p i) (perm p j)=canonical b i j := by
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowPairPatterns
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowPairPatterns.normalize

import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyOnePairAssembly
namespace Aris4Math.ThirtyFour.TwentyOneEightPairs
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt
open NineteenPairs
set_option maxHeartbeats 0
set_option maxRecDepth 100000

theorem certificates : ∀ l : Fin 9,4≤l.val→
    Numeric.validProfile (pairProfile 21 10 21 8 8 l.val []) 34 ∧
    Numeric.totalBound (pairProfile 21 10 21 8 8 l.val [])<1 := by
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_high (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=8) (dy : H.degree y=8)
    (high : 4≤H.codegree x y) : PropertyB H := by
  have upper:=ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at upper
  obtain ⟨valid,strict⟩:=certificates ⟨H.codegree x y,by omega⟩ high
  have real:=realizes_pair_profile H size (by decide : 1≤10) (by decide : 10<21)
    (by decide : 21≤21) x y xy [] (by simpa only [dx,dy] using valid)
  apply ProfileApplication.propertyB_of_uncorrected_profile H (twoVertices x y xy)
    (positionsAt 21 10 21 (by decide) (by decide) (by decide))
    (pairProfile 21 10 21 (H.degree x) (H.degree y) (H.codegree x y) []) real rfl rfl
  simpa only [dx,dy] using strict
end Aris4Math.ThirtyFour.TwentyOneEightPairs
#print axioms Aris4Math.ThirtyFour.TwentyOneEightPairs.propertyB_of_high

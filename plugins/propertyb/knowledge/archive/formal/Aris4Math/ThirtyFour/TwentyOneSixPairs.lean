import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyOnePairAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSixPairs
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt
open NineteenPairs

def cases : List PairCase :=
  [⟨6,6,5,10,11⟩,⟨6,6,6,10,11⟩,
   ⟨7,6,5,10,11⟩,⟨7,6,6,10,11⟩,
   ⟨8,6,5,10,11⟩,⟨8,6,6,10,11⟩,
   ⟨7,7,5,10,11⟩,⟨7,7,6,10,11⟩,⟨7,7,7,10,11⟩,
   ⟨8,7,5,10,11⟩,⟨8,7,6,10,11⟩,⟨8,7,7,10,11⟩]
set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem certificates : ∀ c∈cases,
    Numeric.validProfile (pairProfile 21 10 11 c.d c.e c.l []) 34 ∧
    Numeric.totalBound (pairProfile 21 10 11 c.d c.e c.l [])<1 := by
  unfold Numeric.validProfile
  decide +kernel
set_option maxHeartbeats 0 in
theorem coverage : ∀ d e l : Fin 9,
    6≤d.val → d.val≤7 → d.val≤e.val → 5≤l.val → l.val≤d.val →
    (⟨e.val,d.val,l.val,10,11⟩ : PairCase)∈cases := by decide +kernel

theorem propertyB_of_high (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (x y : Fin 21) (xy : x≠y) (dx6 : 6≤H.degree x) (dx7 : H.degree x≤7)
    (dxy : H.degree x≤H.degree y) (dy8 : H.degree y≤8)
    (high : 5≤H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  have mem := coverage ⟨H.degree x,by omega⟩ ⟨H.degree y,by omega⟩
    ⟨H.codegree x y,by omega⟩ dx6 dx7 dxy high upper
  obtain ⟨valid,strict⟩ := certificates _ mem
  have real := realizes_pair_profile H size (by decide : 1≤10) (by decide : 10<11)
    (by decide : 11≤21) y x xy.symm [] (by simpa only [H.codegree_comm y x] using valid)
  apply ProfileApplication.propertyB_of_uncorrected_profile H
    (twoVertices y x xy.symm) (positionsAt 21 10 11 (by decide) (by decide) (by decide))
    (pairProfile 21 10 11 (H.degree y) (H.degree x) (H.codegree y x) []) real rfl rfl
  simpa only [H.codegree_comm y x] using strict
end Aris4Math.ThirtyFour.TwentyOneSixPairs
#print axioms Aris4Math.ThirtyFour.TwentyOneSixPairs.propertyB_of_high

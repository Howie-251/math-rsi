import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

/-! Actual high-codegree pairs at 24 vertices. These are complete coloring
branches, not numerical conditions left for a caller. -/
namespace Aris4Math.ThirtyFour.TwentyFourStrongCodegree
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt
open NineteenPairs

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem pair_certificates : ∀ d : Fin 9, d.val=7 ∨ d.val=8 →
    ∀ c : Fin 9, 5≤c.val → c.val≤d.val →
    Numeric.validProfile (pairProfile 24 1 14 d.val d.val c.val []) 34 ∧
    Numeric.totalBound (pairProfile 24 1 14 d.val d.val c.val [])<1 := by
  unfold Numeric.validProfile
  decide +kernel

/-- Both the actual trace multiplicities and the probability certificate are
constructed internally from the selected pair's degrees and codegree. -/
theorem propertyB_of_pair (H : Simple5Hypergraph (Fin 24))
    (size : H.edges.card=34) (x y : Fin 24) (xy : x≠y)
    (same : H.degree x=H.degree y) (degrees : H.degree x=7 ∨ H.degree x=8)
    (high : 5≤H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  have dsmall : H.degree x<9 := by omega
  have csmall : H.codegree x y<9 := by omega
  obtain ⟨valid,strict⟩ := pair_certificates ⟨H.degree x,dsmall⟩ degrees
    ⟨H.codegree x y,csmall⟩ high upper
  have real := realizes_pair_profile H size (by decide : 1≤1)
    (by decide : 1<14) (by decide : 14≤24) x y xy []
    (by simpa only [←same] using valid)
  apply ProfileApplication.propertyB_of_uncorrected_profile H (twoVertices x y xy)
    (positionsAt 24 1 14 (by decide) (by decide) (by decide))
    (pairProfile 24 1 14 (H.degree x) (H.degree y) (H.codegree x y) []) real rfl rfl
  simpa only [←same] using strict

theorem codegree_le_four (H : Simple5Hypergraph (Fin 24))
    (size : H.edges.card=34) (noB : ¬PropertyB H)
    (x y : Fin 24) (xy : x≠y)
    (same : H.degree x=H.degree y) (degrees : H.degree x=7 ∨ H.degree x=8) :
    H.codegree x y≤4 := by
  by_contra h
  exact noB (propertyB_of_pair H size x y xy same degrees (by omega))

end Aris4Math.ThirtyFour.TwentyFourStrongCodegree
#print axioms Aris4Math.ThirtyFour.TwentyFourStrongCodegree.propertyB_of_pair

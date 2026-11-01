import Aris4Math.ThirtyThree.TwentyOnePairs

namespace Aris4Math.ThirtyThree.TwentyTwoHighPair

open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.TwentyOnePairs

def p (l : ℕ) : Numeric.Profile := pairProfile 22 8 13 7 7 l []

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ l : Fin 8,3 ≤ l.val →
    Numeric.validProfile (p l.val) 33 ∧ Numeric.totalBound (p l.val) < 1 := by
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_high_pair (H : Simple5Hypergraph (Fin 22))
    (edges33 : H.edges.card=33) (x y : Fin 22) (hne : x ≠ y)
    (dx : H.degree x=7) (dy : H.degree y=7) (hlo : 3 ≤ H.codegree x y) : PropertyB H := by
  have hle : H.codegree x y ≤ 7 := by
    rw [← dx]
    apply Finset.card_le_card
    intro e he
    obtain ⟨he,hx,_⟩ := Finset.mem_filter.mp he
    exact Finset.mem_filter.mpr ⟨he,hx⟩
  obtain ⟨hv,hs⟩ := certificates ⟨H.codegree x y,by omega⟩ hlo
  have hv' : Numeric.validProfile (pairProfile 22 8 13 (H.degree x) (H.degree y) (H.codegree x y) []) 33 := by
    simpa only [dx,dy,p] using hv
  have real := realizes_pair_profile H edges33 (by decide : 1 ≤ 8) (by decide : 8 < 13)
    (by decide : 13 ≤ 22) x y hne [] hv'
  rw [dx,dy] at real
  exact ProfileApplication.propertyB_of_uncorrected_profile H
    (twoVertices x y hne) (positionsAt 22 8 13 (by decide) (by decide) (by decide))
    (p (H.codegree x y)) real rfl rfl hs

end Aris4Math.ThirtyThree.TwentyTwoHighPair
#print axioms Aris4Math.ThirtyThree.TwentyTwoHighPair.propertyB_of_high_pair

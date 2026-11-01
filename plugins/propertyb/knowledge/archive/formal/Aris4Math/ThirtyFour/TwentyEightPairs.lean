import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

namespace Aris4Math.ThirtyFour.TwentyEightPairs
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.TwentyOneDeletion
open Aris4Math.ThirtyFour.NineteenPairs

def cases : List PairCase :=
  [⟨8,8,4,1,11⟩,⟨8,8,5,1,11⟩,⟨8,8,6,1,11⟩,⟨8,8,7,1,11⟩,⟨8,8,8,1,11⟩]
def p (c : PairCase) : Numeric.Profile := pairProfile 20 c.a c.b c.d c.e c.l [c.a,c.b]
def q (d : ℕ) : ℕ := (4*d-19+2)/3

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem certificates : ∀ c ∈ cases,
    1 ≤ c.a ∧ c.a < c.b ∧ c.b ≤ 20 ∧
    Numeric.validProfile (p c) 34 ∧ Numeric.totalBound (p c) < 1 ∧
    ∀ j : Fin 2, let k := ![c.a,c.b] j; let d := ![c.d,c.e] j
      0 ≤ threshold (p c) k ∧
      Numeric.deduction (p c) k ≤ (q d : ℚ)*threshold (p c) k -
        penaltySum (p c) k (threshold (p c) k) := by
  unfold Numeric.validProfile
  decide +kernel

theorem propertyB_of_case (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (x y : Fin 20) (hne : x ≠ y)
    (c : PairCase) (hc : c ∈ cases)
    (dx : H.degree x = c.d) (dy : H.degree y = c.e) (hl : H.codegree x y = c.l) : PropertyB H := by
  obtain ⟨ha,hab,hb,hvalid,hstrict,hweights⟩ := certificates c hc
  have hvalid' : Numeric.validProfile
      (pairProfile 20 c.a c.b (H.degree x) (H.degree y) (H.codegree x y) [c.a,c.b]) 34 := by
    simpa only [dx,dy,hl] using hvalid
  have real := realizes_pair_profile H edges34 ha hab hb x y hne [c.a,c.b] hvalid'
  rw [dx,dy,hl] at real
  apply ProfileApplication.propertyB_of_corrected_profile H
    (twoVertices x y hne) (positionsAt 20 c.a c.b ha hab hb) (p c) real rfl
  · intro j _
    have hk : (positionsAt 20 c.a c.b ha hab hb j).val+1 = ![c.a,c.b] j := by
      fin_cases j <;> simp [positionsAt,Nat.sub_add_cancel ha,Nat.sub_add_cancel (by omega : 1 ≤ c.b)]
    rw [hk]
    have hd : H.degree (twoVertices x y hne j) = ![c.d,c.e] j := by
      fin_cases j
      · simpa [twoVertices] using dx
      · simpa [twoVertices] using dy
    obtain ⟨hn,hbound⟩ := hweights j
    apply realized_threshold_deduction H cover (twoVertices x y hne)
      (positionsAt 20 c.a c.b ha hab hb) (p c) real j _
      (q (![c.d,c.e] j)) (threshold (p c) (![c.a,c.b] j)) _ hk
    · simp only [hd,q]; exact le_rfl
    · exact hn
    · exact hbound
  · exact hstrict

theorem propertyB_of_high (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (x y : Fin 20) (ne : x ≠ y)
    (dx : H.degree x=8) (dy : H.degree y=8) (high : 4 ≤ H.codegree x y) : PropertyB H := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
  rw [dx] at upper
  have mem : (⟨8,8,H.codegree x y,1,11⟩ : PairCase) ∈ cases := by
    interval_cases h : H.codegree x y <;> decide
  exact propertyB_of_case H cover size x y ne _ mem dx dy rfl

end Aris4Math.ThirtyFour.TwentyEightPairs
#print axioms Aris4Math.ThirtyFour.TwentyEightPairs.propertyB_of_case

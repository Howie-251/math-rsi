from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
x=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/LOW_DEGREE_SIX_VERIFIED.json'))
cases=[]
for c in x['cases']:
 d,e=c['ds'];a,b=c['pos'];l=c['ls'][0]
 if a>b:a,b=b,a;d,e=e,d
 cases.append((d,e,l,a,b))
header='''import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyThree.TwentyOnePairAssembly

namespace Aris4Math.ThirtyFour.TwentyLow
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.DoubleLockProfiles
open Aris4Math.ThirtyThree.DoubleLockAt Aris4Math.ThirtyThree.TwentyOneDeletion
open Aris4Math.ThirtyFour.NineteenPairs

'''
s=header+'def cases : List PairCase :=\n  ['+','.join('⟨'+','.join(map(str,c))+'⟩' for c in cases)+']\n'
s+='''def p (c : PairCase) : Numeric.Profile := pairProfile 20 c.a c.b c.d c.e c.l [c.a,c.b]
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

end Aris4Math.ThirtyFour.TwentyLow
#print axioms Aris4Math.ThirtyFour.TwentyLow.propertyB_of_case
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyLow.lean').write_text(s)

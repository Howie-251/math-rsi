from pathlib import Path
from fractions import Fraction as F
import json,sys
ROOT=Path(__file__).resolve().parents[4]
raw=json.load(open(ROOT/'context/propertyb34/round01/twentyone-math/ONE_SEVEN_FIVE_DUAL_JOINT.json'))['results']
vec=lambda xs:'!['+','.join(map(str,xs))+']'
rat=lambda x:f'({F(x).numerator}/{F(x).denominator})'
fs=lambda m:'{'+','.join(str(j) for j in range(5) if m>>j&1)+'}' if m else '∅'
for index,r in enumerate(raw):
 name=f'TwentyOneSixJoint{index}'
 ns={int(t):n for t,n in r['counts'].items() if n};N=len(r['layouts']);Q=max(sum(q['center']==i for q in r['quotas']) for i in range(5))
 ds=[sum(n for t,n in ns.items() if t>>i&1) for i in range(5)]
 assert ds==[6,7,8,8,8]
 sys.path.insert(0,str(ROOT/'context/propertyb34/round01/twentyone-math'))
 from verify_joint import verify
 checked=verify(r,v=21,ds=ds)
 Path(__file__).with_name(f'SIX_JOINT_{index}_REPLAY.json').write_text(json.dumps(checked,indent=2)+'\n')
 qs=[]
 for i in range(5):
  row=[q for q in r['quotas'] if q['center']==i]
  assert all('kind' not in q for q in row)
  qs.append(row+[dict(avoid=0,delta='0',q=0)]*(Q-len(row)))
 s=f'''import Aris4Math.ThirtyFour.MixedLayoutFive
namespace Aris4Math.ThirtyFour.{name}Data
open scoped BigOperators
open Aris4Math.ThirtyThree.FiveProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
set_option maxRecDepth 100000
abbrev Layout := Fin {N}
abbrev Quota := Fin {Q}
'''
 s+='def μ (T : Finset (Fin 5)) : ℕ := '+''.join(f'if T={fs(t)} then {ns[t]} else ' for t in sorted(ns))+'0\n'
 s+='def support : Finset (Finset (Fin 5)) := {'+','.join(fs(t) for t in sorted(ns))+'}\n'
 s+='def positionFn : Layout → Fin 5 → Fin 21 := '+vec(vec(k-1 for k in z['positions']) for z in r['layouts'])+'\n'
 s+='''theorem positionFn_injective : ∀ l, Function.Injective (positionFn l) := by decide +kernel
def positions (l : Layout) : Fin 5 ↪ Fin 21 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions l) Finset.univ,
    labels.map (fun T => ⟨executableType (positions l) T, μ T⟩),none,
    List.ofFn (fun j => (positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile (positions l) μ (List.ofFn fun j => (positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
 profiles=[]
 for z in r['layouts']:
  pos=z['positions'];ts=[]
  for t in sorted(ns):ts.append('⟨['+','.join(map(str,sorted(pos[j] for j in range(5) if t>>j&1)))+f'],{ns[t]}⟩')
  profiles.append('⟨21,['+','.join(map(str,sorted(pos)))+'],['+','.join(ts)+'],none,['+','.join(map(str,pos))+']⟩')
 s+='def computed : Layout → Numeric.Profile := '+vec(profiles)+'\n'
 s+='''theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
'''
 s+='def gamma : Layout → ℚ := '+vec(rat(z['probability']) for z in r['layouts'])+'\n'
 s+='def beta : Layout → Fin 5 → ℚ := '+vec(vec(rat(b) for b in z['betas']) for z in r['layouts'])+'\n'
 s+='def R : Fin 5 → Quota → Finset (Fin 5) := '+vec(vec(fs(q['avoid']) for q in row) for row in qs)+'\n'
 s+='def delta : Fin 5 → Quota → ℚ := '+vec(vec(rat(q['delta']) for q in row) for row in qs)+'\n'
 s+='def quota : Fin 5 → Quota → ℕ := '+vec(vec(q['q'] for q in row) for row in qs)+'\n'
 s+=f'end Aris4Math.ThirtyFour.{name}Data\n'
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}Data.lean').write_text(s)
 s=f'''import Aris4Math.ThirtyFour.{name}Data
namespace Aris4Math.ThirtyFour.{name}Numeric
open scoped BigOperators
open {name}Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option synthInstance.maxSize 2000

theorem data_valid :
    (∀ T, 0<μ T → T ∈ support) ∧
    (∀ l, Numeric.validProfile (p l) 34) ∧
    (∀ l, (p l).emptyPairCap=none) ∧
    (∀ l j, (positions l j).val+1 ∈ (p l).correctionCenters) ∧
    (∀ l, 0 ≤ gamma l) ∧ (∑ l, gamma l)=1 ∧
    (∀ l j, 0 ≤ beta l j) ∧ (∀ l j, beta l j ≤ gamma l) ∧
    (∀ j q, 0 ≤ delta j q) ∧ (∀ j q, j ∉ R j q) ∧
    (∀ j q, quota j q ≤ (4*available support μ j (R j q)+2-(21-1-(R j q).card))/3) := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

theorem strict :
    (∑ l, gamma l*free (positions l) (p l)) +
    (∑ l, ∑ j, ((gamma l-beta l j)*a positions p l j+beta l j*c positions p l j)) -
    (∑ j, ((∑ q, (quota j q : ℚ)*delta j q)-
      penalty support μ beta (weights positions p) j (R j) (delta j))) < 1 := by
  simp only [MixedLayoutFive.weights_eq,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.{name}Numeric
#print axioms Aris4Math.ThirtyFour.{name}Numeric.strict
'''
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}Numeric.lean').write_text(s)
 s=f'''import Aris4Math.ThirtyFour.{name}Numeric
namespace Aris4Math.ThirtyFour.{name}
open {name}Data {name}Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (vertices : Fin 5 ↪ Fin 21)
    (counts : ∀ T, count H vertices T=μ T) : PropertyB H := by
  obtain ⟨covers,valid,nocap,centers,gn,mass,bn,bg,dn,avoids,quota_valid⟩ := data_valid
  have real (l) : Aris4Math.TypeCounting.RealizesProfile H vertices (positions l) (p l) 34 := by
    rw [p_eq]
    apply MixedLayoutFive.realizes H vertices (positions l) μ counts
    rw [← p_eq]
    exact valid l
  exact MixedLayoutApplication.propertyB_of_mixed_layouts H vertices support μ counts covers
    positions p real nocap centers gamma beta R delta quota gn mass bn bg dn avoids quota_valid strict
end Aris4Math.ThirtyFour.{name}
#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_counts
'''
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
 print(name,N,'layouts',Q,'quota slots',checked['bound'])

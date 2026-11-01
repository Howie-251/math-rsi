from pathlib import Path
from fractions import Fraction
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import *
raw=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/SEVEN_MANY_VERIFIED.json'))['cases']
D=[]
for r in raw:
 if len(r['ds'])!=4:continue
 counts={int(k):v for k,v in r['counts'].items()};p0=Profile(20,5,r['pos'],counts)
 losses=[];pure=[]
 for j,d in enumerate(r['ds']):
  qt=link_certificate(p0,j,link_q_lower(20,5,d))['deduction'];qp=max(0,(4*counts.get(1<<j,0)+2-16)//3)
  pl=qp*2*pair_weight(20,5,p0.positions,1<<j,1<<j,p0.positions[j]);losses.append(max(qt,pl));pure.append(pl>qt)
 assert total_bound(rows(p0,deductions=dict(zip(p0.positions,losses))))<1
 kind=0 if r['ds']==[7]*4 else (1 if r['ls'][2]==1 else 2)
 D.append(dict(kind=kind,high=[counts.get(m,0) for m in (7,11,13,14,15)],counts=counts,pos=r['pos'],loss=losses,pure=pure))
assert len(D)==63
vec=lambda a:'!['+','.join(map(str,a))+']'
rat=lambda r:f'({r.numerator}/{r.denominator})'
type_list=lambda p,c:'['+','.join('⟨['+','.join(map(str,sorted(p[j] for j in range(4) if mask>>j&1)))+f'],{c[mask]}⟩' for mask in range(16) if c.get(mask,0))+']'
s='''import Aris4Math.ThirtyThree.QuadProfiles
import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

/-! Sixty-three complete local four-lock profiles for (7,7,7,7) with all
codegrees two and (7,7,7,8) with all cross-codegrees uniformly one or two. -/
namespace Aris4Math.ThirtyFour.TwentySevenQuad
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.QuadProfiles Aris4Math.ThirtyThree.TwentyOneDeletion
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero table_pruneZero)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
namespace RD
export Aris4Math.ThirtyThree.RefinedDeletion (avoidedPositions avoidedCount penaltySum realized_refined_deduction)
end RD
abbrev Case := Fin 63
def degree (kind : Fin 3) : Fin 4 → ℕ := ![7,7,7,if kind=0 then 7 else 8]
def co (kind : Fin 3) : Fin 6 → ℕ := if kind=1 then ![2,2,1,2,1,1] else fun _ => 2
'''
s+='def kindOf : Case → Fin 3 := '+vec([d['kind'] for d in D])+'\n'
s+='def high : Case → Fin 5 → ℕ := '+vec([vec(d['high']) for d in D])+'\n'
s+='def positionFn : Case → Fin 4 → Fin 20 := '+vec([vec([p-1 for p in d['pos']]) for d in D])+'\n'
s+='''theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 4 ↪ Fin 20 := ⟨positionFn i,positionFn_injective i⟩
def μ (i : Case) : Finset (Fin 4) → ℕ := recovered 34 (degree (kindOf i)) (co (kindOf i)) (high i)
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨20,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i = profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
s+='def computed : Case → Numeric.Profile := '+vec([f'⟨20,[{",".join(map(str,sorted(d["pos"])))}],{type_list(d["pos"],d["counts"])},none,[{",".join(map(str,d["pos"]))}]⟩' for d in D])+'\n'
s+='''theorem p_eq_computed (i : Case) : p i = computed i := by fin_cases i <;> rfl
'''
s+='def losses : Case → Fin 4 → ℚ := '+vec([vec([rat(x) for x in d['loss']]) for d in D])+'\n'
s+='def usePure : Case → Fin 4 → Bool := '+vec([vec([str(x).lower() for x in d['pure']]) for d in D])+'\n'
template=(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenTriples.lean').read_text()
a=template.index('def loss (');b=template.index('def Matches')
body=template[a:b]
body=body.replace('Fin 3','Fin 4').replace('then losses i 2 else 0','then losses i 2 else\n  if k=(positions i 3).val+1 then losses i 3 else 0')
body=body.replace('+2-17','+2-16').replace('degree i j','degree (kindOf i) j')
body=body.replace('absent 2]','absent 2,absent 3]')
a=body.index('    (ha : H.codegree');b=body.index(' : PropertyB H := by',a)
body=body[:a]+'''    (hc : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = co (kindOf i) j)
    (ht : ∀ a, count H vertices (highLabels a) = high i a)'''+body[b:]
a=body.index('    rw [actual_recovered');b=body.index('  have real :=',a)
body=body[:a]+'''    rw [actual_recovered,edges34]
    rw [show (fun j => H.degree (vertices j)) = degree (kindOf i) from funext hd,
      show (fun j => H.codegree (vertices (first j)) (vertices (second j))) = co (kindOf i) from funext hc,
      show (fun j => count H vertices (highLabels j)) = high i from funext ht]
    rfl
'''+body[b:]
s+=body
s+='''set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem coverage : ∀ kind : Fin 3, ∀ h : Fin 5 → Fin 3,
    (∀ j, highPairSum (fun a => (h a).val) j ≤ co kind j) →
    ∃ i : Case, kindOf i=kind ∧ ∀ a, (h a).val=high i a := by
  intro kind
  fin_cases kind <;> decide +kernel

theorem propertyB_of_quad (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (edges34 : H.edges.card = 34) (vertices : Fin 4 ↪ Fin 20) (kind : Fin 3)
    (hd : ∀ j, H.degree (vertices j) = degree kind j)
    (hc : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = co kind j) : PropertyB H := by
  have coSmall : ∀ kind : Fin 3, ∀ j, co kind j ≤ 2 := by decide
  have bounded := high_le_two H vertices (fun j => by rw [hc]; exact coSmall kind j)
  let h : Fin 5 → Fin 3 := fun a => ⟨count H vertices (highLabels a),by have := bounded a; omega⟩
  have inventory : ∀ j, highPairSum (fun a => (h a).val) j ≤ co kind j := by
    intro j
    change highPairSum (fun a => count H vertices (highLabels a)) j ≤ co kind j
    rw [← hc j]
    exact high_inventory H vertices j
  obtain ⟨i,kindEq,ht⟩ := coverage kind h inventory
  apply propertyB_of_data H cover edges34 vertices i
  · simpa only [kindEq] using hd
  · simpa only [kindEq] using hc
  · exact ht

end Aris4Math.ThirtyFour.TwentySevenQuad
#print axioms Aris4Math.ThirtyFour.TwentySevenQuad.propertyB_of_quad
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenQuad.lean').write_text(s)
Path(__file__).with_name('TWENTY_SEVEN_QUAD_DATA.json').write_text(json.dumps(json_value(D),indent=2)+'\n')
print('cases',len(D))

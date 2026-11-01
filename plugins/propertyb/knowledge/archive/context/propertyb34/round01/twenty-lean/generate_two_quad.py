from pathlib import Path
from fractions import Fraction as F
import sys,json
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,total_bound,pair_weight,link_q_lower,json_value
raw=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/SEVEN_TWO_VERIFIED.json'))['cases']
D=[]
for r in raw:
 if r['ds']!=[7,7,8,8]:continue
 counts={int(k):v for k,v in r['counts'].items()};pos=tuple(r['pos']);p=Profile(20,5,pos,counts)
 ds=[]
 for j,c in enumerate(r['cs']):
  bit=1<<j;k=pos[j]
  if r['certificate_kind']=='avoided_dual':
   dual=[(x['avoid'],F(x['alpha']),x['q']) for x in c['dual']]
  else:
   types=[t for t,n in counts.items() if n and t&bit];inv=[]
   for ii,t in enumerate(types):
    for u in types[ii:]:
     cap=counts[t]*(counts[t]-1)//2 if t==u else counts[t]*counts[u]
     if cap:inv.append((pair_weight(20,5,pos,t,u,k)+pair_weight(20,5,pos,u,t,k),cap,t==u==bit))
   total=c['q_total'];pure=c['q_pure'];wp=2*pair_weight(20,5,pos,bit,bit,k)
   best=None
   for a in {F(0),wp,*[w for w,_,_ in inv]}:
    b=max(F(0),wp-a)
    loss=total*a+pure*b-sum(cap*max(F(0),a+(b if purepair else 0)-w) for w,cap,purepair in inv)
    if best is None or loss>best[0]:best=(loss,a,b)
   assert best[0]==F(c['loss']),(best,c)
   dual=[(0,best[1],total),(15^bit,best[2],pure)]
  assert len(dual)<=2
  dual=dual+[(0,F(0),0)]*(2-len(dual))
  # Check the same exact dual inequality without trusting the floating proposal.
  main=sum(a*q for R,a,q in dual);pen=F(0);types=[t for t,n in counts.items() if n and t&bit]
  for ii,t in enumerate(types):
   for u in types[ii:]:
    cap=counts[t]*(counts[t]-1)//2 if t==u else counts[t]*counts[u]
    w=pair_weight(20,5,pos,t,u,k)+pair_weight(20,5,pos,u,t,k)
    threshold=sum(a for R,a,q in dual if not (t|u)&R)
    pen+=cap*max(F(0),threshold-w)
  assert F(c['loss'])<=main-pen
  for R,a,q in dual:
   assert a>=0 and not R&bit
   available=sum(n for t,n in counts.items() if t&bit and not t&R)
   assert q<=max(0,(4*available+2-(19-R.bit_count()))//3)
  ds.append(dual)
 D.append(dict(co=r['ls'],high=r['t3']+[r['t4']],pos=pos,counts=counts,loss=[F(c['loss']) for c in r['cs']],dual=ds,bound=F(r['bound'])))
assert len(D)==168
vec=lambda xs:'!['+','.join(map(str,xs))+']'
rat=lambda x:f'({x.numerator}/{x.denominator})'
fs=lambda m:'{' +','.join(str(j) for j in range(4) if m>>j&1)+'}' if m else '∅'
types=lambda d:'['+','.join('⟨['+','.join(map(str,sorted(d['pos'][j] for j in range(4) if m>>j&1)))+f'],{d["counts"][m]}⟩' for m in range(16) if d['counts'].get(m,0))+']'
s='''import Aris4Math.ThirtyThree.QuadProfiles
import Aris4Math.ThirtyThree.RefinedDeletion

namespace Aris4Math.ThirtyFour.TwentySevenTwoQuadData
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open Aris4Math.ThirtyThree.RefinedDeletion
abbrev Case := Fin 168
def degree : Fin 4 → ℕ := ![7,7,8,8]
'''
s+='def coData : Case → Fin 6 → ℕ := '+vec(vec(d['co']) for d in D)+'\n'
s+='def highData : Case → Fin 5 → ℕ := '+vec(vec(d['high']) for d in D)+'\n'
s+='def positionFn : Case → Fin 4 → Fin 20 := '+vec(vec(x-1 for x in d['pos']) for d in D)+'\n'
s+='''theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide
def positions (i : Case) : Fin 4 ↪ Fin 20 := ⟨positionFn i,positionFn_injective i⟩
def μ (i : Case) : Finset (Fin 4) → ℕ := recovered 34 degree (coData i) (highData i)
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨20,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i = profile (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
s+='def computed : Case → Numeric.Profile := '+vec(f'⟨20,[{",".join(map(str,sorted(d["pos"])))}],{types(d)},none,[{",".join(map(str,d["pos"]))}]⟩' for d in D)+'\n'
s+='set_option maxHeartbeats 0 in\ntheorem p_eq_computed (i : Case) : p i = computed i := by fin_cases i <;> rfl\n'
s+='def lossAt : Case → Fin 4 → ℚ := '+vec(vec(rat(x) for x in d['loss']) for d in D)+'\n'
for name,typ,index,fmt in [('avoid','Finset (Fin 4)',0,fs),('alpha','ℚ',1,rat),('quota','ℕ',2,str)]:
 s+=f'def {name} : Case → Fin 4 → Fin 2 → {typ} := '+vec(vec(vec(fmt(t[index]) for t in center) for center in d['dual']) for d in D)+'\n'
s+='''def loss (i : Case) (k : ℕ) : ℚ :=
  if k=(positions i 0).val+1 then lossAt i 0 else
  if k=(positions i 1).val+1 then lossAt i 1 else
  if k=(positions i 2).val+1 then lossAt i 2 else
  if k=(positions i 3).val+1 then lossAt i 3 else 0
end Aris4Math.ThirtyFour.TwentySevenTwoQuadData
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenTwoQuadData.lean').write_text(s)
s='''import Aris4Math.ThirtyFour.TwentySevenTwoQuadData
namespace Aris4Math.ThirtyFour.TwentySevenTwoQuadNumeric
open scoped BigOperators
open Aris4Math.ThirtyFour.TwentySevenTwoQuadData
open Aris4Math.ThirtyThree.RefinedDeletion
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧
    (∑ k : Fin 20, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-loss i (k.val+1)))) < 1 ∧
    ∀ j : Fin 4,
      loss i ((positions i j).val+1)=lossAt i j ∧
      (∀ z, 0 ≤ alpha i j z) ∧ (∀ z, j ∉ avoid i j z) ∧
      (∀ z, quota i j z ≤
        (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (avoid i j z))+2-
          (20-1-(avoid i j z).card))/3) ∧
      lossAt i j ≤ (∑ z : Fin 2, (quota i j z : ℚ)*alpha i j z) -
        penaltySum (p i) ((positions i j).val+1)
          (fun z => avoidedPositions (positions i) (avoid i j z)) (alpha i j) := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel
end Aris4Math.ThirtyFour.TwentySevenTwoQuadNumeric
#print axioms Aris4Math.ThirtyFour.TwentySevenTwoQuadNumeric.certificates
'''
(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenTwoQuadNumeric.lean').write_text(s)
Path(__file__).with_name('TWO_QUAD_DATA.json').write_text(json.dumps(json_value(D),indent=2)+'\n')
print('168 profiles, exact nested/avoided duals recomputed; max',max(d['bound'] for d in D))

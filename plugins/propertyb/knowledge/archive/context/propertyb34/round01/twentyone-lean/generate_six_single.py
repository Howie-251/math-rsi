from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import sys,json
from itertools import combinations
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,pair_weight,rows,total_bound,json_value
raw=[]
for file in ('MULTIPLE_SIX_WITNESSES','SIX_WITH_SEVENS_WITNESSES','EQUALITY_QUAD'):
 raw+=json.load(open(ROOT/f'context/propertyb34/round01/twentyone-math/{file}.json'))['cases']
raw+=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/TWENTYONE_SIX_REDUCTION_VERIFIED.json'))['witnesses']
G=defaultdict(dict)
for r in raw:
 if len(r['ds']) not in (2,3,4,5):continue
 ns={int(t):n for t,n in r['counts'].items() if n}
 G[tuple(r['ds'])][tuple(sorted(ns.items()))]=r
vec=lambda a:'!['+','.join(map(str,a))+']'
rat=lambda r:f'({F(r).numerator}/{F(r).denominator})'
for degrees,rdict in G.items():
 n=len(degrees);name='TwentyOneSix'+{2:'Pair',3:'Triple',4:'Quad',5:'Five'}[n]+''.join(map(str,degrees));D=[]
 fs=lambda m:'{'+','.join(str(j) for j in range(n) if m>>j&1)+'}' if m else '∅'
 for r in rdict.values():
  ns={int(t):k for t,k in r['counts'].items() if k};pos=tuple(r['pos']);ds=[];loss=[]
  for j,c in enumerate(r['cs']):
   bit=1<<j;k=pos[j];types=[t for t in ns if t&bit];inv=[]
   for ii,t in enumerate(types):
    for u in types[ii:]:
     cap=ns[t]*(ns[t]-1)//2 if t==u else ns[t]*ns[u]
     if cap:inv.append((pair_weight(21,5,pos,t,u,k)+pair_weight(21,5,pos,u,t,k),cap,t,u))
   if 'dual' in c:
    dual=[(z['avoid'],F(z['alpha']),z['q']) for z in c['dual']]
   else:
    total=c['q_total'];pure=c['q_pure'];wp=2*pair_weight(21,5,pos,bit,bit,k);best=None
    for a in {F(0),wp,*[w for w,_,_,_ in inv]}:
     b=max(F(0),wp-a)
     value=total*a+pure*b-sum(cap*max(F(0),a+(b if t==u==bit else 0)-w) for w,cap,t,u in inv)
     if best is None or value>best[0]:best=(value,a,b)
    dual=[(0,best[1],total),(((1<<n)-1)^bit,best[2],pure)]
   value=sum(a*q for R,a,q in dual)-sum(cap*max(F(0),sum(a for R,a,q in dual if not (t|u)&R)-w) for w,cap,t,u in inv)
   assert value>=F(c['loss']),(degrees,r['counts'],j,value,c['loss'])
   for R,a,q in dual:
    av=sum(k for t,k in ns.items() if t&bit and not t&R)
    assert a>=0 and not R&bit and q<=max(0,(4*av+2-(20-R.bit_count()))//3)
   ds.append(dual);loss.append(value)
  p=Profile(21,5,pos,ns);bound=total_bound(rows(p,deductions=dict(zip(pos,loss))));assert bound<1
  D.append(dict(counts=ns,pos=pos,dual=ds,loss=loss,bound=bound,co=[sum(k for t,k in ns.items() if t&mask==mask) for mask in ([sum(1<<i for i in pair) for pair in combinations(range(n),2)])],t=ns.get(7,0)))
 N=len(D);Q=max(len(d) for r in D for d in r['dual'])
 for d in D:
  for row in d['dual']:row.extend([(0,F(0),0)]*(Q-len(row)))
 s=f'''import Aris4Math.ThirtyFour.SingleLayoutApplication
namespace Aris4Math.ThirtyFour.{name}Data
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles
open scoped BigOperators
set_option maxRecDepth 100000
abbrev Case := Fin {N}
abbrev Quota := Fin {Q}
def degree : Fin {n} → ℕ := {vec(degrees)}
def labels : List (Finset (Fin {n})) := [{','.join(fs(t) for t in range(1<<n))}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀ T, T∈labels := by decide +kernel
'''
 s+=f'def μ : Case → Finset (Fin {n}) → ℕ := '+vec('fun T => '+''.join(f'if T={fs(t)} then {k} else ' for t,k in sorted(d['counts'].items()))+'0' for d in D)+'\n'
 s+=f'def co : Case → Fin {len(D[0]["co"])} → ℕ := '+vec(vec(d['co']) for d in D)+'\n'
 if n==4:s+='def high : Case → Fin 5 → ℕ := '+vec(vec(d['counts'].get(t,0) for t in [7,11,13,14,15]) for d in D)+'\n'
 if n==3:s+='def triple : Case → ℕ := '+vec(d['t'] for d in D)+'\n'
 s+=f'def positionFn : Case → Fin {n} → Fin 21 := '+vec(vec(k-1 for k in d['pos']) for d in D)+'\n'
 s+=f'''theorem positionFn_injective : ∀ i, Function.Injective (positionFn i) := by decide +kernel
def positions (i : Case) : Fin {n} ↪ Fin 21 := ⟨positionFn i,positionFn_injective i⟩
def p (i : Case) : Numeric.Profile :=
  pruneZero ⟨21,executableType (positions i) Finset.univ,
    labels.map (fun T => ⟨executableType (positions i) T, μ i T⟩),none,
    List.ofFn (fun j => (positions i j).val+1)⟩
theorem p_eq (i : Case) : p i=profile labels (positions i) (μ i) (List.ofFn fun j => (positions i j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
 ts=lambda d:'['+','.join('⟨['+','.join(map(str,sorted(d['pos'][j] for j in range(n) if t>>j&1)))+f'],{k}⟩' for t,k in sorted(d['counts'].items()))+']'
 s+='def computed : Case → Numeric.Profile := '+vec('⟨21,['+','.join(map(str,sorted(d['pos'])))+'],'+ts(d)+',none,['+','.join(map(str,d['pos']))+']⟩' for d in D)+'\n'
 s+='set_option maxHeartbeats 0 in\ntheorem p_eq_computed (i : Case) : p i=computed i := by fin_cases i <;> rfl\n'
 s+=f'def loss : Case → Fin {n} → ℚ := '+vec(vec(rat(q) for q in d['loss']) for d in D)+'\n'
 for var,typ,index,fmt in [('R',f'Finset (Fin {n})',0,fs),('α','ℚ',1,rat),('quota','ℕ',2,str)]:
  s+=f'def {var} : Case → Fin {n} → Quota → {typ} := '+vec(vec(vec(fmt(q[index]) for q in row) for row in d['dual']) for d in D)+'\n'
 if n==3:
  s+='''set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.TripleProfiles.recovered 34
    (degree 0) (degree 1) (degree 2) (co i 0) (co i 1) (co i 2) (triple i) T := by decide +kernel
'''
 if n==4:
  s+='''set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.QuadProfiles.recovered 34
    degree (co i) (high i) T := by decide +kernel
'''
 if n==5:
  s+='''def upper (i : Case) (T : Finset (Fin 5)) : ℕ :=
  ∑ U : Finset (Fin 5), if T⊆U then μ i U else 0
set_option maxHeartbeats 0 in
theorem μ_eq_recovered : ∀ i T, μ i T=Aris4Math.ThirtyThree.MultiLockRecovery.recovered (upper i) (μ i) T := by decide +kernel
'''
 s+=f'end Aris4Math.ThirtyFour.{name}Data\n'
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}Data.lean').write_text(s)
 s=f'''import Aris4Math.ThirtyFour.{name}Data
namespace Aris4Math.ThirtyFour.{name}Numeric
open scoped BigOperators
open {name}Data
open Aris4Math.ThirtyThree.RefinedDeletion
open MixedLayoutApplication (centerLoss)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem certificates : ∀ i : Case,
    Numeric.validProfile (p i) 34 ∧ (p i).emptyPairCap=none ∧
    (∀ j, (positions i j).val+1∈(p i).correctionCenters) ∧
    (∀ j z, 0≤α i j z) ∧ (∀ j z, j∉R i j z) ∧
    (∀ j z, quota i j z ≤
      (4*avoidedCount (p i) ((positions i j).val+1) (avoidedPositions (positions i) (R i j z))+2-
        (21-1-(R i j z).card))/3) ∧
    (∀ j, loss i j ≤ (∑ z, (quota i j z : ℚ)*α i j z)-
      penaltySum (p i) ((positions i j).val+1) (fun z => avoidedPositions (positions i) (R i j z)) (α i j)) ∧
    (∑ k : Fin 21, min (Numeric.boundA (p i) (k.val+1))
      (min (Numeric.boundB (p i) (k.val+1)) (Numeric.boundC (p i) (k.val+1)-centerLoss (positions i) (loss i) (k.val+1))))<1 := by
  intro i
  fin_cases i <;> simp only [p_eq_computed] <;> unfold Numeric.validProfile <;> decide +kernel
end Aris4Math.ThirtyFour.{name}Numeric
#print axioms Aris4Math.ThirtyFour.{name}Numeric.certificates
'''
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}Numeric.lean').write_text(s)
 s=f'''import Aris4Math.ThirtyFour.{name}Numeric
namespace Aris4Math.ThirtyFour.{name}
open {name}Data {name}Numeric
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (vertices : Fin {n} ↪ Fin 21)
    (i : Case) (counts : ∀ T, count H vertices T=μ i T) : PropertyB H := by
  obtain ⟨valid,nocap,centers,nonneg,avoids,quotas,deduction,strict⟩ := certificates i
  have real : Aris4Math.TypeCounting.RealizesProfile H vertices (positions i) (p i) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions i) labels labels_nodup mem_labels (μ i) counts
    rw [← p_eq]; exact valid
  exact SingleLayoutApplication.propertyB_of_single_layout H vertices (positions i) (p i) real
    nocap centers (R i) (α i) (quota i) (loss i) nonneg avoids quotas deduction strict
'''
 if n==3:s+='''
theorem propertyB_of_data (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (vertices : Fin 3 ↪ Fin 21) (i : Case)
    (hd : ∀ j, H.degree (vertices j)=degree j)
    (ha : H.codegree (vertices 0) (vertices 1)=co i 0)
    (hb : H.codegree (vertices 0) (vertices 2)=co i 1)
    (hc : H.codegree (vertices 1) (vertices 2)=co i 2)
    (ht : Aris4Math.ThirtyThree.TripleProfiles.tripleCodegree H (vertices 0) (vertices 1) (vertices 2)=triple i) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  change Aris4Math.ThirtyThree.TripleProfiles.count H vertices T=_
  rw [Aris4Math.ThirtyThree.TripleProfiles.actual_recovered,
    Aris4Math.ThirtyThree.TripleProfiles.triple_count_eq,size,hd 0,hd 1,hd 2,ha,hb,hc,ht]
'''
 if n==4:s+='''
theorem propertyB_of_data (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (vertices : Fin 4 ↪ Fin 21) (i : Case)
    (hd : ∀ j, H.degree (vertices j)=degree j)
    (hc : ∀ j, H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j))=co i j)
    (ht : ∀ j, count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j)=high i j) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  change Aris4Math.ThirtyThree.QuadProfiles.count H vertices T=_
  rw [Aris4Math.ThirtyThree.QuadProfiles.actual_recovered,size]
  rw [show (fun j=>H.degree (vertices j))=degree from funext hd,
    show (fun j=>H.codegree (vertices (Aris4Math.ThirtyThree.QuadProfiles.first j))
      (vertices (Aris4Math.ThirtyThree.QuadProfiles.second j)))=co i from funext hc,
    show (fun j=>Aris4Math.ThirtyThree.QuadProfiles.count H vertices (Aris4Math.ThirtyThree.QuadProfiles.highLabels j))=high i from funext ht]
'''
 if n==5:s+='''
theorem propertyB_of_low_high (H : Simple5Hypergraph (Fin 21))
    (vertices : Fin 5 ↪ Fin 21) (i : Case)
    (low : ∀ T,T.card≤2→Aris4Math.ThirtyThree.MultiLockRecovery.upperCount H vertices T=upper i T)
    (high : ∀ T,3≤T.card→count H vertices T=μ i T) : PropertyB H := by
  apply propertyB_of_counts H vertices i
  intro T
  rw [μ_eq_recovered]
  exact Aris4Math.ThirtyThree.MultiLockRecovery.actual_recovered H vertices (upper i) (μ i) low high T
'''
 s+=f'end Aris4Math.ThirtyFour.{name}\n#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_counts\n'
 (ROOT/f'formal/Aris4Math/ThirtyFour/{name}.lean').write_text(s)
 Path(__file__).with_name(name+'_REPLAY.json').write_text(json.dumps(json_value(D),indent=2)+'\n')
 print(name,N,'max',max(d['bound'] for d in D),flush=True)

"""Replay existing finite mixtures only; no layout or probability optimization."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement
import sys,json
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'formal/Aris4Math/ThirtyFour';HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,pair_weight,json_value
SRC=ROOT/'context/propertyb34-hour1-20261013/high-math'
orig=json.loads((SRC/'MIXED_SIX_v24_low6_badnone.json').read_text())['results']
vec=lambda a:'!['+','.join(map(str,a))+']'
rat=lambda x:f'({F(x).numerator}/{F(x).denominator}:ℚ)'
fs=lambda m:'{'+','.join(str(j) for j in range(6) if m>>j&1)+'}' if m else '∅'
for group in map(int,sys.argv[1:] or ['7']):
 name=f'TwentyFourSixLowUnitAverage{group}';ns={int(t):k for t,k in orig[group]['counts'].items() if k}
 if group==0:
  # A prescribed 120-element subfamily of the original 720 layouts.
  # Its exact average is checked below, without using any group-theory assertion.
  permutations=set()
  for a in range(5):
   for b in range(5):
    for c in range(5):
     for d in range(5):
      if (a*d-b*c)%5==0:continue
      image=[]
      for x in range(6):
       num,den=(a,c) if x==5 else ((a*x+b)%5,(c*x+d)%5)
       image.append(5 if den==0 else num*pow(den,-1,5)%5)
      assert len(set(image))==6
      permutations.add(tuple(image))
  assert len(permutations)==120
  layouts=[tuple(10+x for x in p) for p in sorted(permutations)]
  gamma=[F(1,120)]*120;cb=[F(679,6630)]*6
  source={'bound':'2203/2210'}
 elif group==4:
  source=next(x for x in json.loads((SRC/'MIXED_LAYOUT_LP.json').read_text())['results'] if x['group']==4)
  layouts=[tuple(z['positions']) for z in source['witnesses']];gamma=[F(z['probability']) for z in source['witnesses']]
  cb=[F(z['maximum']) for z in source['centers']]
 else:
  source=next(x for x in json.loads((SRC/'AUTOMORPHISM_AVERAGE.json').read_text())['results'] if x['group']==group)
  perm=source['source_relabeling'];layouts=[tuple(source['positions'][a[perm[j]]] for j in range(6)) for a in source['used_auto']]
  gamma=[F(1,len(layouts))]*len(layouts);cb=[F(source['centers'][perm[j]]['maximum']) for j in range(6)]
 slots=[(j,t,u) for j in range(6) for t,u in combinations_with_replacement(sorted(ns),2) if (t&u)==1<<j and (t!=u or ns[t]>=2)]
 data=[]
 for pos in layouts:
  rr=rows(Profile(24,5,pos,ns)); aa=[min(rr[k-1]['A'],rr[k-1]['B']) for k in pos];cc=[rr[k-1]['C'] for k in pos]
  free=sum((r['bound'] for r in rr if r['k'] not in pos),F())
  vv=[min(aa[j],cc[j]-pair_weight(24,5,pos,t,u,pos[j])-pair_weight(24,5,pos,u,t,pos[j])) for j,t,u in slots]
  data.append(dict(pos=pos,free=free,a=aa,c=cc,value=vv))
 assert sum(gamma)==1
 assert all(sum(g*d['value'][s] for g,d in zip(gamma,data))<=cb[j] for s,(j,t,u) in enumerate(slots))
 total=sum(g*d['free'] for g,d in zip(gamma,data))+sum(cb);assert total==F(source['bound']) and total<1
 L=len(layouts);S=len(slots)
 head=f'''import Aris4Math.ThirtyFour.TwentyFourSlotAverageCache
import Aris4Math.ThirtyFour.TwentyFourSixLowUnitData
namespace Aris4Math.ThirtyFour.{name}
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open Aris4Math.ThirtyThree.ActualBadSlot
open LocalProfiles MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Layout := Fin {L}
abbrev SlotIndex := Fin {S}
def μ := TwentyFourSixLowUnitData.μ {group}
def labels : List (Finset (Fin 6)) := [{','.join(fs(t) for t in range(64))}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def positionFn : Layout→Fin 6→Fin 24 := {vec(vec(k-1 for k in pos) for pos in layouts)}
theorem positionFn_injective : ∀l,Function.Injective (positionFn l) := by
  intro l;fin_cases l <;> decide +kernel
def positions (l : Layout) : Fin 6↪Fin 24 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨24,executableType (positions l) Finset.univ,
    labels.map (fun T=>⟨executableType (positions l) T,μ T⟩),none,
    List.ofFn (fun j=>(positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j=>(positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
'''
 ts=lambda pos:'['+','.join('⟨['+','.join(map(str,sorted(pos[j] for j in range(6) if t>>j&1)))+f'],{k}⟩' for t,k in sorted(ns.items()))+']'
 head+='def computed : Layout→Numeric.Profile := '+vec('⟨24,['+','.join(map(str,sorted(pos)))+'],'+ts(pos)+',none,['+','.join(map(str,pos))+']⟩' for pos in layouts)+'\n'
 head+='theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl\n'
 head+='def gamma : Layout→ℚ := '+vec(rat(g) for g in gamma)+'\n'
 head+='def centerBound : Fin 6→ℚ := '+vec(rat(z) for z in cb)+'\n'
 head+=f'abbrev PositiveIndex := Fin {len(ns)}\n'
 head+='def positive : PositiveIndex→Finset (Fin 6) := '+vec(fs(t) for t in sorted(ns))+'\n'
 head+='def slot : SlotIndex→Slot 6 := '+vec(f'⟨{j},{fs(t)},{fs(u)}⟩' for j,t,u in slots)+'\n'
 for key,typ in [('free','ℚ'),('a','Fin 6→ℚ'),('c','Fin 6→ℚ'),('value','SlotIndex→ℚ')]:
  head+=f'def {key}Value : Layout→{typ} := '+vec(rat(d[key]) if key=='free' else vec(rat(x) for x in d[key]) for d in data)+'\n'
 end=f'end Aris4Math.ThirtyFour.{name}\n'
 (OUT/f'{name}Data.lean').write_text(head+end)
 header=lambda imports:'\n'.join(f'import Aris4Math.ThirtyFour.{n}' for n in imports)+f'\nnamespace Aris4Math.ThirtyFour.{name}\nopen scoped BigOperators\nopen Aris4Math.ThirtyThree.ActualBadSlot\nopen MixedLayoutApplication TwentyFourSlotAverageTable\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
 core=header([name+'Data'])+'''
theorem data_valid :
    (∀l,Numeric.validProfile (p l) 34) ∧ (∀l,(p l).emptyPairCap=none) ∧
    (∀l j,(positions l j).val+1∈(p l).correctionCenters) ∧
    (∀l,0≤gamma l) ∧ (∑l,gamma l)=1 := by
  simp only [p_eq_computed]
  unfold Numeric.validProfile
  decide +kernel

theorem positive_complete : ∀T,0<μ T→∃t,positive t=T := by decide +kernel

theorem complete_positive : ∀j t u,Admissible μ j (positive t) (positive u)→∃s,
    (slot s).center=j ∧
    (((slot s).left=positive t ∧ (slot s).right=positive u) ∨
     ((slot s).left=positive u ∧ (slot s).right=positive t)) := by
  intro j;fin_cases j <;> decide +kernel

theorem complete : ∀j T U,Admissible μ j T U→∃s,
    (slot s).center=j ∧
    (((slot s).left=T ∧ (slot s).right=U) ∨
     ((slot s).left=U ∧ (slot s).right=T)) := by
  intro j T U h
  obtain ⟨t,rfl⟩ := positive_complete T h.2.1
  obtain ⟨u,rfl⟩ := positive_complete U h.2.2.1
  exact complete_positive j t u h

theorem averages_bounds : ∀s,(∑l,gamma l*valueValue l s)≤centerBound (slot s).center := by
  intro s;fin_cases s <;> decide +kernel

theorem averages : (∀s,(∑l,gamma l*valueValue l s)≤centerBound (slot s).center) ∧
    (∑l,gamma l*freeValue l)+(∑j,centerBound j)<1 := by
  exact ⟨averages_bounds,by decide +kernel⟩
'''
 (OUT/f'{name}Core.lean').write_text(core+end)
 for b in range((L+4)//5):
  body=header([name+'Data'])
  for l in range(5*b,min(L,5*b+5)):
   body+=f'''
theorem rows_{l} : TwentyFourSlotAverageCache.cachedFree (positions {l}) (p {l})=freeValue {l} ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions {l}) (p {l}) j=aValue {l} j ∧
      TwentyFourSlotAverageCache.cachedC (positions {l}) (p {l}) j=cValue {l} j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
'''
  (OUT/f'{name}Rows{b}.lean').write_text(body+end)
 for b in range((L+4)//5):
  body=header([name+'Data'])
  for l in range(5*b,min(L,5*b+5)):
   body+=f'''
theorem slots_{l} : ∀s,min (aValue {l} (slot s).center)
    (cValue {l} (slot s).center-
      (LocalProfiles.executableWeights positions p {l} (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p {l} (slot s).center (slot s).right (slot s).left))=valueValue {l} s := by
  simp only [LocalProfiles.executableWeights,p_eq_computed]
  decide +kernel
'''
  (OUT/f'{name}Slots{b}.lean').write_text(body+end)
 comb=header([name+'Core']+[name+f'{t}{b}' for t in ['Rows','Slots'] for b in range((L+4)//5)])
 comb+='theorem rows_exact (l : Layout) : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=freeValue l ∧\n    (∀j,TwentyFourSlotAverageCache.cachedA (positions l) (p l) j=aValue l j ∧\n      TwentyFourSlotAverageCache.cachedC (positions l) (p l) j=cValue l j) := by\n  fin_cases l\n'+''.join(f'  · exact rows_{l}\n' for l in range(L))
 comb+='''theorem slots_exact (l : Layout) : ∀s,min (aValue l (slot s).center)
    (cValue l (slot s).center-
      (LocalProfiles.executableWeights positions p l (slot s).center (slot s).left (slot s).right+
       LocalProfiles.executableWeights positions p l (slot s).center (slot s).right (slot s).left))=valueValue l s := by
  fin_cases l
'''+''.join(f'  · exact slots_{l}\n' for l in range(L))
 comb+='''theorem free_exact (l : Layout) : free (positions l) (p l)=freeValue l := by
  rw [TwentyFourSlotAverageCache.free_eq _ _ (data_valid.1 l) (data_valid.2.1 l)]
  exact (rows_exact l).1

theorem entry_exact (l : Layout) (s : SlotIndex) : contribution positions p l (slot s)=valueValue l s := by
  rw [TwentyFourSlotAverageCache.contribution_eq _ _ l _ (data_valid.1 l) (data_valid.2.1 l),
    ((rows_exact l).2 _).1,((rows_exact l).2 _).2]
  exact slots_exact l s

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (vertices : Fin 6↪Fin 24)
    (counts : ∀T,Aris4Math.ThirtyThree.MultiLockRecovery.count H vertices T=μ T)
    (degrees : ∀j,H.degree (vertices j)=6)
    (unit : ∀i j,i≠j→H.codegree (vertices i) (vertices j)=1) : PropertyB H := by
  have real (l : Layout) : Aris4Math.TypeCounting.RealizesProfile H vertices (positions l) (p l) 34 := by
    rw [p_eq]
    apply LocalProfiles.realizes H vertices (positions l) labels labels_nodup mem_labels μ counts
    rw [←p_eq];exact data_valid.1 l
  apply propertyB_of_table H cover vertices μ counts degrees unit positions p real
    data_valid.2.1 data_valid.2.2.1 gamma data_valid.2.2.2.1 data_valid.2.2.2.2
    slot complete valueValue entry_exact centerBound averages.1
  simpa only [free_exact] using averages.2
'''
 (OUT/f'{name}.lean').write_text(comb+end+f'#print axioms Aris4Math.ThirtyFour.{name}.propertyB_of_counts\n')
 (HERE/f'{name}_REPLAY.json').write_text(json.dumps(json_value(dict(group=group,source=str(SRC),slots=slots,layouts=data,gamma=gamma,centerBound=cb,bound=total)),indent=2)+'\n')
 print(name,L,S,'exact',total,flush=True)

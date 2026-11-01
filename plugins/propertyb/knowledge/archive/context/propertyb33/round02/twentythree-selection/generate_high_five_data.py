"""Complete labeled single-matching data, using the recorded exact numerical witnesses.
Generated Lean checks the certificates and the local classification separately.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations, combinations
import json
import sys

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'computations'))
sys.dont_write_bytecode=True
from multilock import Profile,pair_weight,rows,total_bound

SRC=ROOT/'context/propertyb33/round01/large-math'
base=json.loads((SRC/'SEVEN_MATCHING_FIVE_V23.json').read_text())['results']
base=[r for r in base if r['extra']<=1]
refine={}
large=[b for b in range(32) if b.bit_count()>=3]
pairs=[(1<<i)|(1<<j) for i,j in combinations(range(5),2)]
perms=list(permutations(range(5)))

def vec(xs): return '!['+','.join(map(str,xs))+']'
def lst(xs): return '['+','.join(map(str,xs))+']'
def fs(t): return '{'+','.join(str(i) for i in range(5) if t>>i&1)+'}' if t else '∅'
def trans(t,p): return sum(1<<p[i] for i in range(5) if t>>i&1)

def dual(p,j):
 bit=1<<j;k=p.positions[j];ts=[t for t in p.counts if t&bit];inv=[]
 for ix,t in enumerate(ts):
  for u in ts[ix:]:
   cap=p.counts[t]*(p.counts[t]-1)//2 if t==u else p.counts[t]*p.counts[u]
   if cap:inv.append((cap,pair_weight(23,5,p.positions,t,u,k)+pair_weight(23,5,p.positions,u,t,k),t==u==bit))
 r=max(0,(4*p.counts.get(bit,0)+2-18)//3);wpp=next((w for cap,w,b in inv if b),Fraction(0));options=[]
 for c in {Fraction(0),*(w for cap,w,b in inv)}:
  for d in {Fraction(0),max(Fraction(0),wpp-c)}:
   loss=2*c+r*d-sum(cap*max(Fraction(0),c+(d if b else 0)-w) for cap,w,b in inv)
   options.append((loss,c,d))
 loss,c,d=max(options)
 return [0,31^bit],[c,d],[2,r],loss

known={}
for original in base:
 key=(original['extra'],original['group']);r=refine.get(key,original)
 ns={int(t):n for t,n in r['counts'].items()};pos=r['positions']
 for perm in perms:
  changed=tuple(sorted((trans(t,perm),n) for t,n in ns.items()))
  changedpos=[None]*5
  for a,b in enumerate(perm):changedpos[b]=pos[a]
  known[key[0],changed]=(original,r,perm,changedpos)

data=[]
for extra in (0,1):
 co={t:2 if extra and t==3 else 1 for t in pairs}
 for bits in range(1<<16):
  ns={t:1 for a,t in enumerate(large) if bits>>a&1}
  rem={t:n-sum(b&t==t for b in ns) for t,n in co.items()}
  if min(rem.values())<0:continue
  ns.update({t:n for t,n in rem.items() if n})
  for j in range(5):ns[1<<j]=7-sum(n for t,n in ns.items() if t>>j&1)
  ns[0]=33-sum(ns.values());assert min(ns.values())>=0
  ns={t:n for t,n in ns.items() if n}
  old,r,perm,pos=known[extra,tuple(sorted(ns.items()))]
  p=Profile(23,5,tuple(pos),ns);cert=[None]*5
  if (extra,old['group']) in refine:
   for a,b in enumerate(perm):
    z=r['certificates'][a];ds=z['dual'];assert len(ds)<=2
    rr=[trans(x['avoid'],perm) for x in ds];aa=[Fraction(x['alpha']) for x in ds];qq=[x['q'] for x in ds]
    while len(rr)<2:rr.append(0);aa.append(Fraction(0));qq.append(0)
    cert[b]=(rr,aa,qq,Fraction(z['loss']))
  else:
   cert=[dual(p,j) for j in range(5)]
   for a,b in enumerate(perm):assert cert[b][3]==Fraction(r['certificates'][a]['loss'])
  bound=total_bound(rows(p,deductions={pos[j]:cert[j][3] for j in range(5)}))
  assert bound==Fraction(r['bound']) and bound<1
  data.append(dict(extra=extra,bits=bits,counts=ns,positions=pos,cert=cert,bound=bound,group=old['group']))
assert [sum(r['extra']==e for r in data) for e in (0,1)]==[32,41]

lines=['import Aris4Math.ThirtyThree.FiveProfiles','import Aris4Math.ThirtyThree.RefinedDeletion','',
 '/-! Complete labeled zero/one matching pair numeric inputs. Each row is checked in Lean. -/',
 'namespace Aris4Math.ThirtyThree.TwentyThreeHighFiveData','open FiveProfiles',
 'open TripleProfiles (pruneZero)','open RefinedDeletion','open scoped BigOperators','',
 'def extra : Fin 73 → Fin 2 := '+vec(r['extra'] for r in data),
 'def positionFn : Fin 73 → Fin 5 → Fin 23 := '+vec(vec(p-1 for p in r['positions']) for r in data),
 'theorem positionFn_injective : ∀ k, Function.Injective (positionFn k) := by decide +kernel',
 'def positions (k : Fin 73) : Fin 5 ↪ Fin 23 := ⟨positionFn k,positionFn_injective k⟩',
 'def counts : Fin 73 → Finset (Fin 5) → ℕ := '+vec('(fun T => '+''.join('if T = '+fs(t)+' then '+str(n)+' else ' for t,n in sorted(r['counts'].items()))+'0)' for r in data),
 'def catalog : Fin 73 → Fin 16 → Bool := '+vec(vec('true' if r['bits']>>a&1 else 'false' for a in range(16)) for r in data),
 'def p (k : Fin 73) : Numeric.Profile :=',
 '  pruneZero ⟨23,executableType (positions k) Finset.univ,',
 '    labels.map (fun T => ⟨executableType (positions k) T,counts k T⟩),none,',
 '    List.ofFn (fun j => (positions k j).val+1)⟩',
 'theorem p_eq (k : Fin 73) : p k = profile (positions k) (counts k)',
 '    (List.ofFn fun j => (positions k j).val+1) := by',
 '  simp only [p,executableType_eq,profile,rawProfile]']
computed=[]
for r in data:
 ts=['⟨'+lst(sorted(r['positions'][j] for j in range(5) if t>>j&1))+','+str(n)+'⟩' for t,n in sorted(r['counts'].items())]
 computed.append('⟨23,'+lst(sorted(r['positions']))+','+lst(ts)+',none,'+lst(r['positions'])+'⟩')
lines += ['def computed : Fin 73 → Numeric.Profile := '+vec(computed),
 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem p_eq_computed (k : Fin 73) : p k = computed k := by fin_cases k <;> rfl']
lines += ['def avoided : Fin 73 → Fin 5 → Fin 2 → Finset (Fin 5) := '+vec(vec(vec(fs(z) for z in c[0]) for c in r['cert']) for r in data),
 'def multipliers : Fin 73 → Fin 5 → Fin 2 → ℚ := '+vec(vec(vec(c[1]) for c in r['cert']) for r in data),
 'def quotas : Fin 73 → Fin 5 → Fin 2 → ℕ := '+vec(vec(vec(c[2]) for c in r['cert']) for r in data),
 'def lossAt : Fin 73 → Fin 5 → ℚ := '+vec(vec(c[3] for c in r['cert']) for r in data),
 'def loss (i : Fin 73) (k : ℕ) : ℚ :=',
 *['  if k=(positions i '+str(j)+').val+1 then lossAt i '+str(j)+' else' for j in range(5)],'  0',
 '', 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem certificates : ∀ k : Fin 73, Numeric.validProfile (p k) 33 ∧',
 '    (∑ x : Fin 23, min (Numeric.boundA (p k) (x.val+1))',
 '      (min (Numeric.boundB (p k) (x.val+1)) (Numeric.boundC (p k) (x.val+1)-loss k (x.val+1)))) < 1 ∧',
 '    ∀ j : Fin 5,',
 '      (∀ i, 0 ≤ multipliers k j i) ∧ (∀ i, j ∉ avoided k j i) ∧',
 '      (∀ i, quotas k j i ≤',
 '        (4 * avoidedCount (p k) ((positions k j).val+1) (avoidedPositions (positions k) (avoided k j i))',
 '          + 2 - (23 - 1 - (avoided k j i).card)) / 3) ∧',
 '      loss k ((positions k j).val+1) ≤ (∑ i, (quotas k j i : ℚ) * multipliers k j i) -',
 '        penaltySum (p k) ((positions k j).val+1)',
 '          (fun i => avoidedPositions (positions k) (avoided k j i)) (multipliers k j) := by',
 '  simp only [p_eq_computed]','  unfold Numeric.validProfile','  intro k',
 '  fin_cases k <;> decide +kernel','',
 'end Aris4Math.ThirtyThree.TwentyThreeHighFiveData','']
(ROOT/'formal/Aris4Math/ThirtyThree/TwentyThreeHighFiveData.lean').write_text('\n'.join(lines))
(Path(__file__).parent/'HIGH_FIVE_GENERATION.json').write_text(json.dumps([
 dict(extra=r['extra'],bits=r['bits'],source_group=r['group'],bound=str(r['bound']),
      positions=r['positions'],counts=r['counts'],dual=[dict(avoid=c[0],alpha=list(map(str,c[1])),q=c[2],loss=str(c[3])) for c in r['cert']]) for r in data],indent=2)+'\n')
print('Generated 32+41 complete labeled zero/one matching profiles, all exact Python bounds <1.')

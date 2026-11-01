"""Complete labeled P3(+K2) data, using the recorded exact numerical witnesses.
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
base=json.loads((SRC/'SIX_SEVEN_MATCHING_V23.json').read_text())['results']
refine={r['group']:r for r in json.loads((SRC/'SIX_SEVEN_MATCHING_REFINEMENT_V23.json').read_text())['results']}

def vec(xs): return '!['+','.join(map(str,xs))+']'
def lst(xs): return '['+','.join(map(str,xs))+']'
def fs(t): return '{'+','.join(str(i) for i in range(6) if t>>i&1)+'}' if t else '∅'
def trans(t,p): return sum(1<<p[i] for i in range(6) if t>>i&1)

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

data=[]
for old in base:
 if not any(int(t).bit_count()>=4 and n for t,n in old['counts'].items()):continue
 r=refine.get(old['group'],old)
 ns={int(t):n for t,n in r['counts'].items()};pos=r['positions']
 p=Profile(23,5,tuple(pos),ns)
 if old['group']==4:
  cert=[]
  for z in r['certificates']:
   ds=z['dual'];assert len(ds)<=2
   rr=[x['avoid'] for x in ds];aa=[Fraction(x['alpha']) for x in ds];qq=[x['q'] for x in ds]
   while len(rr)<2:rr.append(0);aa.append(Fraction(0));qq.append(0)
   cert.append((rr,aa,qq,Fraction(z['loss'])))
  bound=total_bound(rows(p,deductions={pos[j]:cert[j][3] for j in range(6)}))
  assert bound==Fraction(r['bound']) and bound<1
 else:
  cert=None;bound=total_bound(rows(p));assert bound<1
 data.append(dict(counts=ns,positions=pos,cert=cert,bound=bound,group=old['group']))
assert len(data)==22 and data[0]['group']==4

lines=['import Aris4Math.ThirtyThree.TwentyThreeHighSixProfiles','import Aris4Math.ThirtyThree.RefinedDeletion','',
 '/-! Six-lock matching representatives with a trace of size at least four; exact probability data. -/',
 'namespace Aris4Math.ThirtyThree.TwentyThreeHighSixData','open TwentyThreeHighSixProfiles',
 'open TripleProfiles (pruneZero)','open RefinedDeletion','open scoped BigOperators','',
 'def positionFn : Fin 22 → Fin 6 → Fin 23 := '+vec(vec(p-1 for p in r['positions']) for r in data),
 'theorem positionFn_injective : ∀ k, Function.Injective (positionFn k) := by decide +kernel',
 'def positions (k : Fin 22) : Fin 6 ↪ Fin 23 := ⟨positionFn k,positionFn_injective k⟩',
 'def counts : Fin 22 → Finset (Fin 6) → ℕ := '+vec('(fun T => '+''.join('if T = '+fs(t)+' then '+str(n)+' else ' for t,n in sorted(r['counts'].items()))+'0)' for r in data),
 'def centers (k : Fin 22) : List ℕ := if k=0 then List.ofFn (fun j => (positions k j).val+1) else []',
 'def p (k : Fin 22) : Numeric.Profile :=',
 '  pruneZero ⟨23,executableType (positions k) Finset.univ,',
 '    labels.map (fun T => ⟨executableType (positions k) T,counts k T⟩),none,',
 '    centers k⟩',
 'theorem p_eq (k : Fin 22) : p k = profile (positions k) (counts k)',
 '    (centers k) := by',
 '  simp only [p,executableType_eq,profile,rawProfile]']
computed=[]
for r in data:
 ts=['⟨'+lst(sorted(r['positions'][j] for j in range(6) if t>>j&1))+','+str(n)+'⟩' for t,n in sorted(r['counts'].items())]
 computed.append('⟨23,'+lst(sorted(r['positions']))+','+lst(ts)+',none,'+(lst(r['positions']) if r['group']==4 else '[]')+'⟩')
lines += ['def computed : Fin 22 → Numeric.Profile := '+vec(computed),
 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem p_eq_computed (k : Fin 22) : p k = computed k := by fin_cases k <;> rfl']
lines += [
 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem certificates : ∀ k : Fin 22, Numeric.validProfile (p k) 33 ∧',
 '    (k ≠ 0 → Numeric.totalBound (p k) < 1) := by',
 '  simp only [p_eq_computed]','  unfold Numeric.validProfile','  intro k',
 '  fin_cases k <;> decide +kernel',
 'def avoided : Fin 6 → Fin 2 → Finset (Fin 6) := '+vec(vec(fs(z) for z in c[0]) for c in data[0]['cert']),
 'def multipliers : Fin 6 → Fin 2 → ℚ := '+vec(vec(c[1]) for c in data[0]['cert']),
 'def quotas : Fin 6 → Fin 2 → ℕ := '+vec(vec(c[2]) for c in data[0]['cert']),
 'def lossAt : Fin 6 → ℚ := '+vec(c[3] for c in data[0]['cert']),
 'def loss (k : ℕ) : ℚ :=',
 *['  if k=(positions 0 '+str(j)+').val+1 then lossAt '+str(j)+' else' for j in range(6)],'  0',
 '', 'set_option maxHeartbeats 0 in','set_option maxRecDepth 100000 in',
 'theorem refined_certificate :',
 '    (∑ x : Fin 23, min (Numeric.boundA (p 0) (x.val+1))',
 '      (min (Numeric.boundB (p 0) (x.val+1)) (Numeric.boundC (p 0) (x.val+1)-loss (x.val+1)))) < 1 ∧',
 '    ∀ j : Fin 6,',
 '      (∀ i, 0 ≤ multipliers j i) ∧ (∀ i, j ∉ avoided j i) ∧',
 '      (∀ i, quotas j i ≤',
 '        (4 * avoidedCount (p 0) ((positions 0 j).val+1) (avoidedPositions (positions 0) (avoided j i))',
 '          + 2 - (23 - 1 - (avoided j i).card)) / 3) ∧',
 '      loss ((positions 0 j).val+1) ≤ (∑ i, (quotas j i : ℚ) * multipliers j i) -',
 '        penaltySum (p 0) ((positions 0 j).val+1)',
 '          (fun i => avoidedPositions (positions 0) (avoided j i)) (multipliers j) := by',
 '  simp only [p_eq_computed]','  decide +kernel','',
 'end Aris4Math.ThirtyThree.TwentyThreeHighSixData','']
(ROOT/'formal/Aris4Math/ThirtyThree/TwentyThreeHighSixData.lean').write_text('\n'.join(lines))
(Path(__file__).parent/'HIGH_SIX_GENERATION.json').write_text(json.dumps([
 dict(source_group=r['group'],bound=str(r['bound']),positions=r['positions'],counts=r['counts']) for r in data],indent=2)+'\n')
print('Generated 22 representatives: 21 bare, one refined.')

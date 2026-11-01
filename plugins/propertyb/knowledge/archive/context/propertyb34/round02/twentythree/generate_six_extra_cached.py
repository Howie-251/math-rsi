"""Reuse the checked Joint3 caching method for the unchanged 31-layout certificate."""
from pathlib import Path
from fractions import Fraction as Q
import json

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'formal/Aris4Math/ThirtyFour'
BASE='TwentyThreeSixLowExtra7Joint16Cached'
DATA='TwentyThreeSixLowExtra7Joint16Data'
NS='Aris4Math.ThirtyFour.'+BASE+'Numeric'
old=(OUT/'TwentyThreeSixLowExtra7Joint16Numeric.lean').read_text()
source=json.loads((ROOT/'context/propertyb34/round01/middle-math/MIXED_LOW_23.json').read_text())
x=next(r['joint'] for r in source['results'] if r['group']==16 and r['degrees'][-1]==7)
assert len(x['layouts'])==31
scale=x['scale']
rat=lambda x:f'({Q(x).numerator}/{Q(x).denominator}:ℚ)'
vec=lambda xs:'!['+','.join(xs)+']'
def write(name,s):
 p=OUT/(name+'.lean')
 if not p.exists() or p.read_text()!=s:p.write_text(s)

core=old[:old.index('theorem strict :')].replace(
 'import Aris4Math.ThirtyFour.'+DATA,
 'import Aris4Math.ThirtyFour.'+DATA+'\nimport Aris4Math.ThirtyFour.CachedRows').replace(
 'TwentyThreeSixLowExtra7Joint16Numeric',BASE+'Numeric')
peer=(OUT/'TwentyThreeFiveLowStrictJoint3CachedCore.lean').read_text()
api=peer[peer.index('def cachedFree'):peer.index('/-- Exact proposed values')].replace('Fin 5','Fin 7')
core+=api
core+='def freeValue : Layout → ℚ := '+vec(rat(Q(z['free'],scale)) for z in x['layouts'])+'\n'
for key,field in [('a','a'),('c','c')]:
 core+=f'def {key}Value : Layout → Fin 7 → ℚ := '+vec(vec(rat(Q(c[field],scale)) for c in z['centers']) for z in x['layouts'])+'\n'
penalties=[sum((Q(p)*s['capacity'] for p,s in zip(x['penalties'],x['slots']) if s['center']==j),Q()) for j in range(7)]
core+='def penaltyValue : Fin 7 → ℚ := '+vec(rat(z)for z in penalties)+'\n'
end='end '+NS+'\n'
write(BASE+'Core',core+end)
def header(imports):
 return ''.join(f'import Aris4Math.ThirtyFour.{i}\n'for i in imports)+f'namespace {NS}\nopen scoped BigOperators\nopen {DATA}\nopen MixedLayoutApplication MixedLayoutCounts\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n'

rowblocks=[]
for b,start in enumerate(range(0,31,4)):
 s=header([BASE+'Core'])
 for i in range(start,min(start+4,31)):
  s+=f'''theorem rows_{i} : cachedFree {i}=freeValue {i} ∧
      (∀ j : Fin 7, cachedCenterA {i} j=aValue {i} j ∧ cachedCenterC {i} j=cValue {i} j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
'''
 write(BASE+f'Rows{b}',s+end)
 rowblocks.append(BASE+f'Rows{b}')
for j in range(7):
 s=header([BASE+'Core'])+f'''theorem penalty_{j} : penalty support μ beta (weights positions p) {j} (R {j}) (delta {j})=penaltyValue {j} := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel
'''+end
 write(BASE+f'Penalty{j}',s)
s=header(rowblocks+[BASE+f'Penalty{j}'for j in range(7)])
s+='''theorem rows_exact (l : Layout) : cachedFree l=freeValue l ∧
    (∀ j : Fin 7, cachedCenterA l j=aValue l j ∧ cachedCenterC l j=cValue l j) := by
  fin_cases l
'''+''.join(f'  · exact rows_{i}\n'for i in range(31))
s+='''theorem free_exact (l : Layout) : cachedFree l=freeValue l := (rows_exact l).1
theorem a_exact (l : Layout) (j : Fin 7) : cachedCenterA l j=aValue l j := ((rows_exact l).2 j).1
theorem c_exact (l : Layout) (j : Fin 7) : cachedCenterC l j=cValue l j := ((rows_exact l).2 j).2
theorem penalty_exact (j : Fin 7) : penalty support μ beta (weights positions p) j (R j) (delta j)=penaltyValue j := by
  fin_cases j
'''+''.join(f'  · exact penalty_{j}\n'for j in range(7))
strict=old[old.index('theorem strict :'):old.index('end Aris4Math.')]
s+=strict[:strict.index(' := by')]+''' := by
  simp_rw [free_eq,a_eq,c_eq,free_exact,a_exact,c_exact,penalty_exact]
  decide +kernel
'''+end+f'#print axioms {NS}.strict\n'
write(BASE+'Numeric',s)
(HERE/'SIX_EXTRA_CACHED_MANIFEST.txt').write_text('\n'.join('Aris4Math.ThirtyFour.'+n for n in [DATA,BASE+'Core']+rowblocks+[BASE+f'Penalty{j}'for j in range(7)]+[BASE+'Numeric'])+'\n')
(HERE/'SIX_EXTRA_CACHED_EXPORT.json').write_text(json.dumps(dict(layouts=31,rows_per_block=4,penalties=list(map(str,penalties)),status='exported, not Lean checked'),indent=2)+'\n')
print('31 unchanged layouts, 8 row blocks, 7 exact penalty blocks; not built')

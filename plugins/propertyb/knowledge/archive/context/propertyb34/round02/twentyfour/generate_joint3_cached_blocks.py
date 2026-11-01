"""Preserve the existing twenty-layout certificate; split kernel arithmetic only."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys
ROOT=Path(__file__).resolve().parents[4]; HERE=Path(__file__).resolve().parent
OUT=ROOT/'formal/Aris4Math/ThirtyFour'; BASE='TwentyThreeFiveLowStrictJoint3Cached'
NS='Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric'
old=(OUT/'TwentyThreeFiveLowStrictJoint3Numeric.lean').read_text()
core=(HERE/'Joint3CachedAPIProbe.lean').read_text();end=f'end {NS}\n';core=core[:-len(end)]
x=json.loads((HERE/'JOINT3_SOURCE.json').read_text());scale=x['scale'];assert len(x['layouts'])==20
rat=lambda z:f'({Q(z).numerator}/{Q(z).denominator}:ℚ)'
vec=lambda a:'!['+','.join(a)+']'
core+='\n/-- Exact proposed values; each entry is checked against its original profile below. -/\n'
core+='def freeValue : Layout → ℚ := '+vec(rat(Q(z['free'],scale)) for z in x['layouts'])+'\n'
core+='def aValue : Layout → Fin 5 → ℚ := '+vec(vec(rat(Q(c['a'],scale)) for c in z['centers']) for z in x['layouts'])+'\n'
core+='def cValue : Layout → Fin 5 → ℚ := '+vec(vec(rat(Q(c['c'],scale)) for c in z['centers']) for z in x['layouts'])+'\n'
(OUT/f'{BASE}Core.lean').write_text(core+end)
header=lambda imports:'\n'.join(f'import Aris4Math.ThirtyFour.{t}' for t in imports)+f'\nnamespace {NS}\nopen scoped BigOperators\nopen TwentyThreeFiveLowStrictJoint3Data\nopen MixedLayoutApplication MixedLayoutCounts\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
for b in range(4):
 s=header([BASE+'Core'])
 for i in range(5*b,5*b+5):
  s+=f'''\ntheorem rows_{i} : cachedFree {i} = freeValue {i} ∧
    (∀ j : Fin 5, cachedCenterA {i} j = aValue {i} j ∧ cachedCenterC {i} j = cValue {i} j) := by
  simp only [cachedFree,cachedCenterA,cachedCenterC,p_eq_computed]
  decide +kernel
'''
 (OUT/f'{BASE}Rows{b}.lean').write_text(s+end+f'#print axioms {NS}.rows_{5*b+4}\n')
s=header([BASE+'Core'])
for j in range(5):
 assert sum((Q(p)*sl['capacity'] for p,sl in zip(x['penalties'],x['slots']) if sl['center']==j),Q())==0
 s+=f'''\ntheorem penalty_{j} : penalty support μ beta (weights positions p) {j} (R {j}) (delta {j}) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel
'''
s+='''
theorem penalty_zero (j : Fin 5) : penalty support μ beta (weights positions p) j (R j) (delta j) = 0 := by
  fin_cases j
'''+''.join(f'  · exact penalty_{j}\n' for j in range(5))
(OUT/f'{BASE}Penalty.lean').write_text(s+end+f'#print axioms {NS}.penalty_zero\n')
s=header([BASE+f'Rows{b}' for b in range(4)]+[BASE+'Penalty'])
s+='''
theorem rows_exact (l : Layout) : cachedFree l = freeValue l ∧
    (∀ j : Fin 5, cachedCenterA l j = aValue l j ∧ cachedCenterC l j = cValue l j) := by
  fin_cases l
'''+''.join(f'  · exact rows_{i}\n' for i in range(20))
s+='''
theorem free_exact (l : Layout) : cachedFree l = freeValue l := (rows_exact l).1
theorem a_exact (l : Layout) (j : Fin 5) : cachedCenterA l j = aValue l j := ((rows_exact l).2 j).1
theorem c_exact (l : Layout) (j : Fin 5) : cachedCenterC l j = cValue l j := ((rows_exact l).2 j).2
'''
strict=old[old.index('theorem strict :'):old.index('end Aris4Math.')]
s+=strict[:strict.index(' := by')]+''' := by
  simp_rw [free_eq,a_eq,c_eq,free_exact,a_exact,c_exact,penalty_zero]
  decide +kernel
'''+end+f'#print axioms {NS}.strict\n'
(HERE/'Joint3CachedNumericCombination.lean').write_text(s)
if '--assemble' in sys.argv:(OUT/f'{BASE}Numeric.lean').write_text(s)
# Inline Core+one block gives a faithful bounded pilot before official Core build.
for b in [0,3]:
 body=(OUT/f'{BASE}Rows{b}.lean').read_text();body=body[body.index('namespace '):]
 (HERE/f'Joint3CachedBlock{b}Probe.lean').write_text(core+end+body)
print('Core, Rows0..3, Penalty ready; final combination', 'installed' if '--assemble' in sys.argv else 'staged only')

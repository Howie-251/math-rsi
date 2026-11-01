from pathlib import Path
import sys,json
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'formal/Aris4Math/ThirtyFour';NAME='TwentyFourSixLowUnitAverage0'
sys.path.insert(0,str(ROOT/'computations'));from multilock import Profile,rows
r=json.loads((Path(__file__).parent/(NAME+'_REPLAY.json')).read_text())
src=json.loads((ROOT/'context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_badnone.json').read_text())['results'][0]
rr=rows(Profile(24,5,tuple(r['layouts'][0]['pos']),src['counts']))
vec=lambda a:'!['+','.join(a)+']';rat=lambda x:f'({F(x).numerator}/{F(x).denominator}:ℚ)'
head=f'''import Aris4Math.ThirtyFour.{NAME}Data
import Aris4Math.ThirtyFour.TwentyFourCachedCongruence
namespace Aris4Math.ThirtyFour.{NAME}
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
''';end=f'end Aris4Math.ThirtyFour.{NAME}\n'
s=head
s+='def referenceA : Fin 24→ℚ := '+vec(rat(min(x['A'],x['B'])) for x in rr)+'\n'
s+='def referenceC : Fin 24→ℚ := '+vec(rat(x['C']) for x in rr)+'\n'
s+='''theorem geometry : ∀l,(p l).v=(p 0).v ∧ (p l).positions=(p 0).positions ∧
    (p l).types.toFinset=(p 0).types.toFinset := by
  intro l;fin_cases l <;> decide +kernel

theorem free_positions : ∀l,
    Finset.univ.filter (fun k : Fin 24=>¬∃j,positions l j=k)=
      Finset.univ.filter (fun k : Fin 24=>¬∃j,positions 0 j=k) := by
  intro l;fin_cases l <;> decide +kernel

theorem reference_rows : ∀k : Fin 24,
    min (CachedRows.cachedA (p 0) (k.val+1) true)
      (CachedRows.cachedA (p 0) (k.val+1) false)=referenceA k ∧
    CachedRows.cachedC (p 0) (k.val+1)=referenceC k := by
  intro k;fin_cases k <;> decide +kernel

theorem reference_free : TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0)=freeValue 0 := by
  unfold TwentyFourSlotAverageCache.cachedFree
  decide +kernel

theorem stored_rows : ∀l j,referenceA (positions l j)=aValue l j ∧
    referenceC (positions l j)=cValue l j := by
  intro l;fin_cases l <;> decide +kernel

theorem rows_exact (l : Layout) : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=freeValue l ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions l) (p l) j=aValue l j ∧
      TwentyFourSlotAverageCache.cachedC (positions l) (p l) j=cValue l j) := by
  have eq (k : ℕ) := TwentyFourCachedCongruence.rows (p l) (p 0)
    (geometry l).1 (geometry l).2.1 (geometry l).2.2 k
  constructor
  · have same : TwentyFourSlotAverageCache.cachedFree (positions l) (p l)=
        TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0) := by
      unfold TwentyFourSlotAverageCache.cachedFree
      rw [free_positions l]
      apply Finset.sum_congr rfl
      intro k _
      rw [(eq _).1 true,(eq _).1 false,(eq _).2]
    rw [same,reference_free]
    rfl
  · intro j
    unfold TwentyFourSlotAverageCache.cachedA TwentyFourSlotAverageCache.cachedC
    rw [(eq _).1 true,(eq _).1 false,(eq _).2,
      (reference_rows _).1,(reference_rows _).2]
    exact stored_rows l j
'''
(OUT/(NAME+'Rows.lean')).write_text(s+end)
p=OUT/(NAME+'.lean');s=p.read_text();s='\n'.join(x for x in s.splitlines() if not (x.startswith('import') and NAME+'Rows' in x))+'\n';s=f'import Aris4Math.ThirtyFour.{NAME}Rows\n'+s
a=s.index('theorem rows_exact');b=s.index('theorem slots_exact',a);s=s[:a]+s[b:];p.write_text(s)

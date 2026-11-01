"""Interface-only probes. Coverage/classification parameters remain explicit;
these files are not substitutes for the final production theorem."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
SRC=ROOT/'formal/Aris4Math/ThirtyFour'
def body(path):return '\n'.join(l for l in path.read_text().splitlines()if not l.startswith('import '))
trace=body(SRC/'TwentyThreeTraceShape.lean')
sparse=body(SRC/'TwentyThreeSparseTrace.lean')
for n,word in [(4,'Five'),(5,'Six')]:
 prefix=f'TwentyThree{word}LowPromotion'
 imports='import Aris4Math.ThirtyFour.TwentyThreeLowPromotionBase\nimport Aris4Math.ThirtyFour.TwentyThreeSevenLowCounting\n'
 old=''
 if n==4:imports+='import Aris4Math.ThirtyFour.TwentyThreeFourLowClassified\n'
 else:
  rows=json.loads((ROOT/'context/propertyb34/round01/middle-math/EXTEND_LOW_23_5.json').read_text())['results']
  def fs(t):return '{'+','.join(str(i)for i in range(5)if t>>i&1)+'}'if t else '∅'
  def mu(r):return '(fun T => '+''.join(f'if T={fs(int(t))} then {m} else 'for t,m in sorted(r['counts'].items(),key=lambda a:int(a[0]))if m)+'0)'
  old='namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified\nabbrev Residue := Fin 2\ndef residualCounts : Residue → Finset (Fin 5) → ℕ := !['+','.join(mu(rows[i])for i in [0,2])+']\nend Aris4Math.ThirtyFour.TwentyThreeFiveLowClassified\n'
 data=body(SRC/(prefix+'Data.lean'));actual=body(SRC/(prefix+'.lean'))
 if n==5:
  v='''variable (checkedOldClassifier : ∀ (H : Simple5Hypergraph (Fin 23)), H.PairCovering →
    H.edges.card=34 → ∀ (f : Fin 5 ↪ Fin 23),
    (∀ i, H.degree (f i)=6) → ¬ PropertyB H →
    ∃ r : TwentyThreeFiveLowClassified.Residue, ∃ σ : Equiv.Perm (Fin 5),
      ∀ T, count H (σ.toEmbedding.trans f) T=TwentyThreeFiveLowClassified.residualCounts r T)
include checkedOldClassifier

'''
  actual=actual.replace('theorem old_actual',v+'theorem old_actual').replace('TwentyThreeFiveLowClassified.actual_residual H','checkedOldClassifier H').replace(':= old_actual H',':= old_actual checkedOldClassifier H').replace('exact actual_of_covered H','exact actual_of_covered checkedOldClassifier H')
 actual=actual.replace('/-- Complete actual extension', 'variable (checkedCoverage : ∀ c values, values∈catalogue c → covered c values)\ninclude checkedCoverage\n\n/-- Complete actual extension')
 actual=actual.replace('(coverage c values member)','(checkedCoverage c values member)').replace(':= actual_extension H',':= actual_extension '+('checkedOldClassifier 'if n==5 else'')+'checkedCoverage H')
 out=HERE/('FiveLowMomentActualProbe.lean'if n==4 else'SixLowActualProbe.lean')
 out.write_text(imports+trace+'\n'+sparse+'\n'+old+'\n'+data+'\n'+actual+'\n')

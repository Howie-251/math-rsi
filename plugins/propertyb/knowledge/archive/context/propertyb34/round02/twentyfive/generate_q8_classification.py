"""Direct, complete q=8 degree-color classification and actual-H binding."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math';F=ROOT/'formal/Aris4Math/ThirtyFour'
def fs(xs):return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t):return fs([i for i in range(9) if t>>i&1])
def li(ts):return '['+','.join(tr(t) for t in ts)+']'
old=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())['orbits'];cert=json.loads((HERE/'Q8_COLORED_CERTIFICATES.json').read_text())['rows'];rows=[]
for r in cert:
 big=old[r['base']];low=fs([i for i in range(9) if i!=r['high']])
 if 'rejection' in r:
  no=r['rejection'];witness='⟨0,![0,1,2,3,4,5,6,7,8]⟩';reject='some (.inl ⟨'+li(big)+','+li(no['incident'])+','+str(no['vertex'])+'⟩)'
 else:witness='⟨'+str(r['target'])+',!['+','.join(map(str,r['permutation']))+']⟩';reject='none'
 rows.append('⟨'+li(big)+','+low+','+witness+','+reject+'⟩')
name='TwentyFiveEightLowClassifiedData'
s=f'''import Aris4Math.ThirtyFour.TwentyFiveOneHighTable
import Aris4Math.ThirtyFour.TwentyFiveUnit9Data
import Aris4Math.ThirtyFour.TwentyFiveEightLowInventoryData
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveColoredRows
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
batches=[rows[i:i+64] for i in range(0,len(rows),64)]
for j,batch in enumerate(batches):s+=f'def rows{j} : List (Row 9 840) := ['+',\n'.join(batch)+']\n'
s+='def rows : List (Row 9 840) := '+' ++ '.join(f'rows{j}' for j in range(len(batches)))+'\n'
s+=f'end Aris4Math.ThirtyFour.{name}\n';(F/(name+'.lean')).write_text(s)
targets=[]
for j in range(len(batches)):
 name=f'TwentyFiveEightLowClassifiedBatch{j}';targets.append(name)
 s=f'''import Aris4Math.ThirtyFour.TwentyFiveEightLowClassifiedData
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveColoredRows TwentyFiveEightLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows{j}.all (fun r => decide (Check 8 TwentyFiveEightLowInventoryData.big r))=true := by decide +kernel
end Aris4Math.ThirtyFour.{name}
''';(F/(name+'.lean')).write_text(s)
name='TwentyFiveEightLowClassified';s=''.join('import Aris4Math.ThirtyFour.'+t+'\n' for t in targets)
s+='''import Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
import Aris4Math.ThirtyFour.TwentyFiveUnit9Actual
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery TwentyFiveUnitExtension
open TwentyFiveColoredRows TwentyFiveColoredActual TwentyFiveEightLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem sources : rows.map source=TwentyFiveOneHighTable.sources TwentyFiveUnit9Data.catalogue := by decide +kernel
theorem checked : rows.all (fun r => decide (Check 8 TwentyFiveEightLowInventoryData.big r))=true := by
  simp only [rows,List.all_append,'''+','.join(f'TwentyFiveEightLowClassifiedBatch{j}.checked' for j in range(len(batches)))+''',Bool.true_and]

theorem actual (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 9↪Fin 25) (unit : Unit H f)
    (degrees : ∀ i,H.degree (f i)=standard 8 i) :
    ∃ c : Fin 840, ∃ σ : Equiv.Perm (Fin 9),
      large H (σ.toEmbedding.trans f)=TwentyFiveEightLowInventory.big c ∧
      (∀ i,H.degree ((σ.toEmbedding.trans f) i)=standard 8 i) ∧
      (∀ T,count H (σ.toEmbedding.trans f) T=TwentyFiveEightLow.μ c T) := by
  obtain ⟨c,σ,family,degree,counts⟩ := TwentyFiveColoredActual.actual H edges f unit 8 degrees
    (by decide +kernel) TwentyFiveUnit9Data.catalogue TwentyFiveUnit9Actual.actual
    TwentyFiveEightLowInventoryData.big
    (TwentyFiveOneHighTable.table _ _ rows sources checked)
  refine ⟨c,σ,family,degree,?_⟩
  intro T
  rw [counts T]
  exact TwentyFiveEightLowInventory.recovered c T
end Aris4Math.ThirtyFour.TwentyFiveEightLowClassified
''';(F/(name+'.lean')).write_text(s)
(HERE/'Q8_CLASSIFICATION_BUILD_MANIFEST.json').write_text(json.dumps({'data':'TwentyFiveEightLowClassifiedData','batches':targets,'aggregate':name},indent=2)+'\n');print('generated 3366 direct q8 rows and actual classified caller')

"""Make explicit selected/permutation rows from saved 8/9-lock certificates."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math';F=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(HERE));from generate_unit_extension_certificates import choices,family,trace

def main(level):
 n=level-1;old=json.loads((S/f'UNIT_CATALOGUE_{n}.json').read_text())['orbits'];new=json.loads((S/f'UNIT_CATALOGUE_{level}.json').read_text())['orbits'];records=json.loads((HERE/f'UNIT_EXTENSION_{level}_CERTIFICATES.json').read_text())['records']
 name=f'TwentyFiveUnit{level}Data';oldexpr=f'TwentyFiveUnit{n}Data.catalogue'
 s=f'''import Aris4Math.ThirtyFour.TwentyFiveUnitRows
import Aris4Math.ThirtyFour.TwentyFiveUnit{n}Data
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
 s+=f'def catalogue : Fin {len(new)} → Finset (Finset (Fin {level})) := !['+',\n'.join(family(b,level) for b in new)+']\n'
 s+=f'def candidates : Fin {len(old)} → List (Finset (Fin {n})) := !['+',\n'.join('['+','.join(trace(t,n) for t in r['candidates'])+']' for r in records)+']\n'
 batches=[];picked=[]
 for r in records:
  i=r['parent'];rows=[]
  for selected,w in zip(choices(r['candidates']),r['certificates']):
   rows.append('⟨'+family(selected,n)+',⟨'+str(w['target'])+',!['+','.join(map(str,w['permutation']))+']⟩⟩')
  chunks=[rows[j:j+128] for j in range(0,len(rows),128)];batches.append(len(chunks))
  for j,chunk in enumerate(chunks):s+=f'def rows{i}_{j} : List (Row {n} {len(new)}) := ['+',\n'.join(chunk)+']\n'
  s+=f'def rows{i} : List (Row {n} {len(new)}) := '+' ++ '.join(f'rows{i}_{j}' for j in range(len(chunks)))+'\n'
  s+=f'def witnesses{i} : List (Witness {level} {len(new)}) := rows{i}.map Row.witness\n'
  if i==len(old)-1:picked=rows[:5]
 s+=f'end Aris4Math.ThirtyFour.{name}\n';(F/(name+'.lean')).write_text(s)
 targets=[]
 for i,num in enumerate(batches):
  for j in range(num):
   name=f'TwentyFiveUnit{level}Rows{i}Batch{j}';targets.append(name)
   s=f'''import Aris4Math.ThirtyFour.TwentyFiveUnit{level}Data
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit{level}Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows{i}_{j}.all (fun r => decide (Checks catalogue ({oldexpr} {i}) r.selected r.witness))=true := by decide +kernel
end Aris4Math.ThirtyFour.{name}
''';(F/(name+'.lean')).write_text(s)
 name=f'TwentyFiveUnit{level}Checked'
 s=''.join('import Aris4Math.ThirtyFour.'+t+'\n' for t in targets)
 s+=f'namespace Aris4Math.ThirtyFour.{name}\nopen TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit{level}Data\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
 for i,num in enumerate(batches):
  s+=f'''theorem selected{i} : rows{i}.map Row.selected=choices (candidates {i}) ∅ := by decide +kernel
theorem checked{i} : List.Forall₂ (Checks catalogue ({oldexpr} {i}))
  (choices (candidates {i}) ∅) witnesses{i} := by
  rw [← selected{i}]
  apply checked_rows
  simp only [rows{i},List.all_append,'''+','.join(f'TwentyFiveUnit{level}Rows{i}Batch{j}.checked' for j in range(num))+''',Bool.true_and]
'''
 s+=f'end Aris4Math.ThirtyFour.{name}\n';(F/(name+'.lean')).write_text(s)
 (HERE/f'UNIT_{level}_FAST_ROWS_BUILD_MANIFEST.json').write_text(json.dumps({'batch_size':128,'rows':sum(len(r['certificates']) for r in records),'targets':targets},indent=2)+'\n')
 (HERE/f'UNIT_{level}_FAST_ROWS_PILOT.json').write_text(json.dumps({'parent':len(old)-1,'big':old[-1],'catalogue':new,'rows':picked},indent=2)+'\n')
 print(json.dumps({'level':level,'targets':len(targets),'rows':sum(len(r['certificates']) for r in records)}))
if __name__=='__main__':main(int(sys.argv[1]))

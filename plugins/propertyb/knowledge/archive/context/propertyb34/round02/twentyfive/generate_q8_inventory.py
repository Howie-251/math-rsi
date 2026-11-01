"""Sparse exact inventory proofs for the saved q=8 nine/tenth-lock cases."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math';F=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(S));from unit_catalogue import fullblocks

def fs(xs):return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n):return fs([i for i in range(n) if t>>i&1])
def li(ts,n):return '['+','.join(tr(t,n) for t in ts)+']'
def fa(ts,n):return '{'+','.join(tr(t,n) for t in ts)+'}' if ts else '∅'
def generate(label,rows,n):
 ns='TwentyFive'+label+'Inventory';source='TwentyFive'+label
 bigs=[[int(t) for t,v in c['counts'].items() if v and int(t).bit_count()>=3] for c in rows]
 s=f'''import Aris4Math.ThirtyFour.TwentyFiveColoredActual
import Aris4Math.ThirtyFour.TwentyFiveInventorySupport
import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
import Aris4Math.ThirtyFour.{source}Data
namespace Aris4Math.ThirtyFour.{ns}Data
open TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
 s+=f'def big : Fin {len(rows)} → Finset (Finset (Fin {n})) := !['+',\n'.join(fa(b,n) for b in bigs)+']\n'
 s+=f'def blockLabels : Fin {len(rows)} → List (Finset (Fin {n})) := !['+',\n'.join(li(fullblocks(b,n),n) for b in bigs)+']\n'
 s+=f'def full (c : Fin {len(rows)}) := (blockLabels c).toFinset\n'
 s+=f'end Aris4Math.ThirtyFour.{ns}Data\n';(F/(ns+'Data.lean')).write_text(s)
 targets=[]
 for start in range(0,len(rows),32):
  j=start//32;name=ns+'Batch'+str(j);targets.append(name)
  s=f'import Aris4Math.ThirtyFour.{ns}Data\nnamespace Aris4Math.ThirtyFour.{ns}\nopen {ns}Data TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
  for i in range(start,min(start+32,len(rows))):
   b=bigs[i];s+=f'''theorem completion{i} : pairCompletion (big {i})=full {i} := by
  have same : big {i}=({li(b,n)} : List (Finset (Fin {n}))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check {li(b,n)} {li(fullblocks(b,n),n)}=true
  decide +kernel

theorem recovered{i} : ∀ T : Finset (Fin {n}),
    inventory 34 (standard 8) (full {i}) T={source}.Case{i}.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : {source}.Case{i}.labels.all
      (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels {i})))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T ({source}.Case{i}.support T pos))
  · decide +kernel
'''
  s+=f'end Aris4Math.ThirtyFour.{ns}\n';(F/(name+'.lean')).write_text(s)
 s=''.join('import Aris4Math.ThirtyFour.'+name+'\n' for name in targets)
 s+=f'namespace Aris4Math.ThirtyFour.{ns}\nopen TwentyFiveUnitCounts TwentyFiveColoredActual Aris4Math.K6Classification\nexport {ns}Data (big blockLabels full)\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n'
 s+=f'theorem completion : ∀ c,pairCompletion (big c)=full c := by\n  intro c\n  fin_cases c\n'
 for i in range(len(rows)):s+=f'  · exact completion{i}\n'
 s+=f'theorem recovered (c : Fin {len(rows)}) (T : Finset (Fin {n})) :\n  inventory 34 (standard 8) (pairCompletion (big c)) T={source}.μ c T := by\n  fin_cases c\n'
 for i in range(len(rows)):s+=f'  · rw [completion{i}]; exact recovered{i} T\n'
 s+=f'end Aris4Math.ThirtyFour.{ns}\n';(F/(ns+'.lean')).write_text(s)
 return {'data':ns+'Data','batches':targets,'aggregate':ns}
q8=json.loads((S/'V25_NINE_Q8_BOUNDS.json').read_text())['results'];tenth=[c for g in json.loads((S/'V25_Q8_TENTH_BOUNDS.json').read_text())['results'] for c in g['cases']]
manifest=[generate('EightLow',q8,9),generate('EightLowTenth',tenth,10)]
(HERE/'Q8_INVENTORY_BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n');print('generated q8 sparse inventories 840+20')

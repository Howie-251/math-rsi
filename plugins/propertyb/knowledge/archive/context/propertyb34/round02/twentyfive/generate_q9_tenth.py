"""Recover all six q=9 residue/last-degree extensions and their real bijections."""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'context/propertyb34/round01/high-math'
FORMAL=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(SOURCE))
from unit_catalogue import fullblocks,canonical
from generate_unit_extension_certificates import choices

def fs(xs): return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n): return fs([i for i in range(n) if t>>i&1])
def fam(ts,n): return '{'+','.join(tr(t,n) for t in ts)+'}' if ts else '∅'

q9=json.loads((SOURCE/'V25_NINE_Q9_CATALOGUE.json').read_text())['results']
groups=json.loads((SOURCE/'V25_TENTH_BOUNDS.json').read_text())['results']
rows=[c for g in groups for c in g['cases']]
target_degrees=[g['new_degree'] for g in groups for _ in g['cases']]
target_indices={tuple(sorted((int(k),v) for k,v in c['counts'].items() if v)):i for i,c in enumerate(rows)}
allrecords=[]
for g in groups:
    big=q9[g['base']]['large_blocks'];d=g['new_degree']
    candidates=[t for t in fullblocks(big,9) if t.bit_count()<=4]
    certificates=[];feasible_count=0
    for selected in choices(candidates):
        ext=[t for t in big if t not in selected]+[t|512 for t in selected]
        bs=fullblocks(ext,10)
        singles=[(6 if i<9 else d)-sum(bool(t>>i&1) for t in bs) for i in range(10)]
        empty=34-len(bs)-sum(singles)
        feasible=min(singles)>=0 and empty>=0
        if feasible:
            feasible_count+=1
            _,perm=canonical(ext,10,[0]*9+[1],True)
            move=lambda t:sum(1<<perm[i] for i in range(10) if t>>i&1)
            counts={t:1 for t in bs};counts.update({1<<i:s for i,s in enumerate(singles)});counts[0]=empty
            moved=tuple(sorted((move(t),v) for t,v in counts.items() if v))
            idx=target_indices[moved]
        else:
            perm=list(range(10));idx=0
        certificates.append(dict(target=idx,permutation=perm,feasible=feasible))
    assert feasible_count==g['labelled_extensions']
    allrecords.append(dict(base=g['base'],degree=d,candidates=candidates,certificates=certificates,
                           choices=len(certificates),feasible=feasible_count))
Path(__file__).with_name('Q9_TENTH_EXTENSION_CERTIFICATES.json').write_text(json.dumps(allrecords,indent=2)+'\n')

s='''import Aris4Math.ThirtyFour.TwentyFiveInventorySupport
import Aris4Math.ThirtyFour.TwentyFiveUnitConditional
import Aris4Math.ThirtyFour.TwentyFiveNineLowInventory
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory
open TwentyFiveUnitCounts Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def big : Fin 25 → Finset (Finset (Fin 10)) := !['+',\n'.join(fam([int(t) for t,v in c['counts'].items() if v and int(t).bit_count()>=3],10) for c in rows)+']\n'
s+='def blockLabels : Fin 25 → List (Finset (Fin 10)) := !['+',\n'.join('['+','.join(tr(t,10) for t in fullblocks([int(t) for t,v in c['counts'].items() if v and int(t).bit_count()>=3],10))+']' for c in rows)+']\n'
s+='def full (c : Fin 25) : Finset (Finset (Fin 10)) := (blockLabels c).toFinset\n'
s+='def lastDegree : Fin 25 → ℕ := !['+','.join(map(str,target_degrees))+']\n'
s+='def degrees (c : Fin 25) (i : Fin 10) : ℕ := if i.val<9 then 6 else lastDegree c\n'
s+='theorem completion : ∀ c,pairCompletion (big c)=full c := by decide +kernel\n'
for i,c in enumerate(rows):
 s+=f'''theorem recovered{i} : ∀ T : Finset (Fin 10),
+  inventory 34 (degrees {i}) (full {i}) T=TwentyFiveNineLowTenth.Case{i}.μ T := by
+  apply TwentyFiveInventorySupport.eq_of_support
+  · have included : (TwentyFiveNineLowTenth.Case{i}.labels).all
+        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels {i})))=true := by decide +kernel
+    intro T pos
+    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case{i}.support T pos))
+  · decide +kernel
+'''.replace('\n+','\n')
s+='theorem recovered (c : Fin 25) (T : Finset (Fin 10)) :\n  inventory 34 (degrees c) (pairCompletion (big c)) T=TwentyFiveNineLowTenth.μ c T := by\n  rw [completion]\n  fin_cases c\n'
for i in range(len(rows)): s+=f'  · exact recovered{i} T\n'
s+='end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory\n'
(FORMAL/'TwentyFiveNineLowTenthInventory.lean').write_text(s)

s='''import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthCoverage
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitConditional
open Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def base : Fin 6 → Fin 147 := ![0,0,3,3,6,6]
def lastDegree : Fin 6 → ℕ := ![6,7,6,7,6,7]
def degrees (g : Fin 6) (i : Fin 10) : ℕ := if i.val<9 then 6 else lastDegree g
def oldBig (g : Fin 6) := TwentyFiveNineLowInventory.big (base g)
'''
s+='def candidates : Fin 6 → List (Finset (Fin 9)) := !['+',\n'.join('['+','.join(tr(t,9) for t in g['candidates'])+']' for g in allrecords)+']\n'
s+='''theorem candidates_eq : ∀ g,(candidates g).toFinset=
  (pairCompletion (oldBig g)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (g : Fin 6) (T : Finset (Fin 9))
    (mem : T∈pairCompletion (oldBig g)) (small : T.card≤4) : T∈candidates g := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
'''
for i,g in enumerate(allrecords):
 s+=f'def witnesses{i} : List (Witness 10 25) := ['+',\n'.join('⟨'+str(w['target'])+',!['+','.join(map(str,w['permutation']))+']⟩' for w in g['certificates'])+']\n'
 s+=f'theorem checked{i} : List.Forall₂\n  (TwentyFiveUnitConditional.Checks (degrees {i}) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig {i}))\n  (choices (candidates {i}) ∅) witnesses{i} := by decide +kernel\n'
s+='def witnesses : Fin 6 → List (Witness 10 25) := !['+','.join(f'witnesses{i}' for i in range(6))+']\n'
s+='theorem checked (g : Fin 6) : List.Forall₂\n  (TwentyFiveUnitConditional.Checks (degrees g) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig g))\n  (choices (candidates g) ∅) (witnesses g) := by\n  fin_cases g\n'
for i in range(6):s+=f'  · exact checked{i}\n'
s+='end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthCoverage\n'
(FORMAL/'TwentyFiveNineLowTenthCoverage.lean').write_text(s)

print(json.dumps([{k:v for k,v in g.items() if k not in ('candidates','certificates')} for g in allrecords]))

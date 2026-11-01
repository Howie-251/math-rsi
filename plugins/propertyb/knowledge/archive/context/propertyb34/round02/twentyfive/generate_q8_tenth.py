"""Recover explicit tenth-lock witnesses for the two q=8 residues."""
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;S=ROOT/'context/propertyb34/round01/high-math';F=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(S));sys.path.insert(0,str(HERE));from unit_catalogue import fullblocks,canonical
from generate_unit_extension_certificates import choices

def fs(xs):return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n):return fs([i for i in range(n) if t>>i&1])
def li(ts,n):return '['+','.join(tr(t,n) for t in ts)+']'
def fa(ts,n):return '{'+','.join(tr(t,n) for t in ts)+'}' if ts else '∅'
q8=json.loads((S/'V25_NINE_Q8_CATALOGUE.json').read_text())['results'];groups=json.loads((S/'V25_Q8_TENTH_BOUNDS.json').read_text())['results'];targets=[c for g in groups for c in g['cases']];index={};colors=[0]*8+[1]*2
for i,r in enumerate(targets):
 big=[int(t) for t,v in r['counts'].items() if v and int(t).bit_count()>=3];key,p=canonical(big,10,colors,True);index.setdefault(key,(i,p))
records=[];render=[];start=time.monotonic()
for g in groups:
 big=q8[g['base']]['large_blocks'];candidates=[t for t in fullblocks(big,9) if t.bit_count()<=4];certs=[];rows=[];feasible=0
 for chosen in choices(candidates):
  ext=[t for t in big if t not in chosen]+[t|512 for t in chosen];blocks=fullblocks(ext,10);degree=[6]*8+[7,7];inc=[sum(bool(t>>i&1) for t in blocks) for i in range(10)];bad=next((i for i in range(10) if inc[i]>degree[i]),None)
  if bad is not None:
   target=0;perm=list(range(10));incident=[t for t in blocks if t>>bad&1][:degree[bad]+1];reject='some (.inl ⟨'+li(ext,10)+','+li(incident,10)+','+str(bad)+'⟩)';certs.append(dict(selected=chosen,rejection={'vertex':bad,'incident':incident}))
  elif len(blocks)+sum(d-i for d,i in zip(degree,inc))>34:
   target=0;perm=list(range(10));reject='some (.inr '+li(blocks,10)+')';certs.append(dict(selected=chosen,budget_rejection=True))
  else:
   key,sourceperm=canonical(ext,10,colors,True);target,targetperm=index[key];inverse=[targetperm.index(i) for i in range(10)];perm=[inverse[sourceperm[i]] for i in range(10)];move=lambda t:sum(1<<perm[i] for i in range(10) if t>>i&1);counts={t:1 for t in blocks};counts.update({1<<i:degree[i]-inc[i] for i in range(10)});counts[0]=34-len(blocks)-sum(degree[i]-inc[i] for i in range(10));assert {move(t):v for t,v in counts.items() if v}=={int(t):v for t,v in targets[target]['counts'].items() if v};reject='none';feasible+=1;certs.append(dict(selected=chosen,target=target,permutation=perm))
  witness='⟨'+str(target)+',!['+','.join(map(str,perm))+']⟩';rows.append('⟨'+fa(chosen,9)+',⟨'+li(ext,10)+','+fs(list(range(8)))+','+witness+','+reject+'⟩⟩')
 assert feasible==g['labelled_extensions'];records.append(dict(base=g['base'],candidates=candidates,certificates=certs,feasible=feasible));render.append(rows)
(HERE/'Q8_TENTH_EXTENSION_CERTIFICATES.json').write_text(json.dumps(records,indent=2)+'\n')
name='TwentyFiveEightLowTenthRowsData';s=f'''import Aris4Math.ThirtyFour.TwentyFiveEightLowInventory
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventoryData
import Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveConditionalBudgetRows TwentyFiveColoredActual
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def base : Fin 2 → Fin 840 := ![0,10]
def oldBig (g : Fin 2) := TwentyFiveEightLowInventory.big (base g)
'''
s+='def candidates : Fin 2 → List (Finset (Fin 9)) := !['+',\n'.join(li(r['candidates'],9) for r in records)+']\n';nums=[]
for g,rows in enumerate(render):
 batches=[rows[i:i+64] for i in range(0,len(rows),64)];nums.append(len(batches))
 for j,b in enumerate(batches):s+=f'def rows{g}_{j} : List (Row 9 20) := ['+',\n'.join(b)+']\n'
 s+=f'def rows{g} : List (Row 9 20) := '+' ++ '.join(f'rows{g}_{j}' for j in range(len(batches)))+'\n'
s+=f'end Aris4Math.ThirtyFour.{name}\n';(F/(name+'.lean')).write_text(s)
targets=[]
for g,num in enumerate(nums):
 for j in range(num):
  name=f'TwentyFiveEightLowTenthRows{g}Batch{j}';targets.append(name)
  s=f'''import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRowsData
namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveConditionalBudgetRows TwentyFiveColoredActual TwentyFiveEightLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows{g}_{j}.all (fun r => decide (Check 8
    TwentyFiveEightLowTenthInventoryData.big (oldBig {g}) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.{name}
''';(F/(name+'.lean')).write_text(s)
name='TwentyFiveEightLowTenthCoverage';s=''.join('import Aris4Math.ThirtyFour.'+t+'\n' for t in targets)
s+=f'''namespace Aris4Math.ThirtyFour.{name}
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveConditionalBudgetRows TwentyFiveColoredActual
open Aris4Math.K6Classification
export TwentyFiveEightLowTenthRowsData (base oldBig candidates)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem candidates_eq : ∀ g,(candidates g).toFinset=
    (pairCompletion (oldBig g)).filter (fun T => T.card≤4) := by
  intro g
  rw [oldBig,TwentyFiveEightLowInventory.completion]
  fin_cases g <;> decide +kernel

theorem candidates_complete (g : Fin 2) (T : Finset (Fin 9))
    (mem : T∈pairCompletion (oldBig g)) (small : T.card≤4) : T∈candidates g := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
'''
for g,num in enumerate(nums):
 s+=f'''theorem selected{g} : TwentyFiveEightLowTenthRowsData.rows{g}.map Row.selected=choices (candidates {g}) ∅ := by decide +kernel
def witnesses{g} : List (Witness 10 20) := TwentyFiveEightLowTenthRowsData.rows{g}.map (fun r => r.colored.witness)
theorem checked{g} : List.Forall₂
    (TwentyFiveUnitConditional.Checks (standard 8) TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (oldBig {g}))
    (choices (candidates {g}) ∅) witnesses{g} := by
  rw [← selected{g}]
  apply checked_rows
  simp only [TwentyFiveEightLowTenthRowsData.rows{g},List.all_append,'''+','.join(f'TwentyFiveEightLowTenthRows{g}Batch{j}.checked' for j in range(num))+''',Bool.true_and]
'''
s+='def witnesses : Fin 2 → List (Witness 10 20) := ![witnesses0,witnesses1]\n'
s+='''theorem checked (g : Fin 2) : List.Forall₂
    (TwentyFiveUnitConditional.Checks (standard 8) TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (oldBig g))
    (choices (candidates g) ∅) (witnesses g) := by
  fin_cases g
  · exact checked0
  · exact checked1
'''+f'end Aris4Math.ThirtyFour.{name}\n';(F/(name+'.lean')).write_text(s)
(HERE/'Q8_TENTH_BUILD_MANIFEST.json').write_text(json.dumps({'data':'TwentyFiveEightLowTenthRowsData','batches':targets,'aggregate':name},indent=2)+'\n');print(json.dumps({'groups':[{k:v for k,v in r.items() if k!='certificates' and k!='candidates'} for r in records],'rows':[len(r) for r in render],'elapsed':time.monotonic()-start}))

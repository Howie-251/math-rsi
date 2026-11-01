"""Compile saved q=9 witnesses to direct rows and short degree obstructions.
No layouts or canonical representatives are searched here.
"""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'context/propertyb34/round01/high-math'
FORMAL=ROOT/'formal/Aris4Math/ThirtyFour'
sys.path.insert(0,str(SOURCE));sys.path.insert(0,str(HERE))
from unit_catalogue import fullblocks
from generate_unit_extension_certificates import choices

def fs(xs):return '{'+','.join(map(str,xs))+'}' if xs else '∅'
def tr(t,n):return fs([i for i in range(n) if t>>i&1])
def family(ts,n):return '{'+','.join(tr(t,n) for t in ts)+'}' if ts else '∅'
def listed(ts,n):return '['+','.join(tr(t,n) for t in ts)+']'
def rejection(big,n,degrees):
 bs=fullblocks(big,n)
 for i,d in enumerate(degrees):
  bad=[t for t in bs if t>>i&1]
  if len(bad)>d:return 'some ⟨'+listed(big,n)+','+listed(bad[:d+1],n)+','+str(i)+'⟩'
 raise ValueError('No degree obstruction')

def write(name,s): (FORMAL/(name+'.lean')).write_text(s)
def hdr(name,imports,opens):
 return ''.join('import Aris4Math.ThirtyFour.'+x+'\n' for x in imports)+'namespace Aris4Math.ThirtyFour.'+name+'\nopen '+opens+'\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'

def chunks(xs,size):return [xs[i:i+size] for i in range(0,len(xs),size)]

q9=json.loads((SOURCE/'V25_NINE_Q9_CATALOGUE.json').read_text())['results']
uncolored=json.loads((SOURCE/'UNIT_CATALOGUE_9.json').read_text())['orbits']
indices={c['base']:c['id'] for c in q9}
groups=json.loads((HERE/'Q9_TENTH_EXTENSION_CERTIFICATES.json').read_text())
build=[]
# First filter: explicit family, target index, optional short incident-list refutation.
name='TwentyFiveNineLowClassifiedData'
s=hdr(name,['TwentyFiveUnit9Data','TwentyFiveNineLowInventory','TwentyFiveConditionalRows'],'TwentyFiveConditionalRows')
rows=[]
for i,big in enumerate(uncolored):
 rows.append('⟨'+family(big,9)+','+str(indices.get(i,0))+','+('none' if i in indices else rejection(big,9,[6]*9))+'⟩')
batches=chunks(rows,64)
for j,batch in enumerate(batches):s+=f'def rows{j} : List (FamilyRow 9 147) := ['+',\n'.join(batch)+']\n'
s+='def rows : List (FamilyRow 9 147) := '+ ' ++ '.join(f'rows{j}' for j in range(len(batches)))+'\n'
s+='end Aris4Math.ThirtyFour.'+name+'\n';write(name,s)
for j in range(len(batches)):
 name='TwentyFiveNineLowClassifiedBatch'+str(j)
 s=hdr(name,['TwentyFiveNineLowClassifiedData'],'TwentyFiveConditionalRows TwentyFiveNineLowClassifiedData')
 s+=f'theorem checked : rows{j}.all (fun r => decide (FamilyCheck (fun _ => 6) TwentyFiveNineLowInventory.big r))=true := by decide +kernel\n'
 s+='end Aris4Math.ThirtyFour.'+name+'\n';write(name,s);build.append(name)
name='TwentyFiveNineLowClassified'
s=hdr(name,['TwentyFiveUnit9Actual']+['TwentyFiveNineLowClassifiedBatch'+str(j) for j in range(len(batches))],
 'Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts TwentyFiveConditionalRows TwentyFiveNineLowClassifiedData')
s+='''theorem sources : rows.map FamilyRow.source=List.ofFn TwentyFiveUnit9Data.catalogue := by decide +kernel

theorem checked : rows.all (fun r => decide (FamilyCheck (fun _ => 6) TwentyFiveNineLowInventory.big r))=true := by
  simp only [rows,List.all_append,'''+','.join(f'TwentyFiveNineLowClassifiedBatch{j}.checked' for j in range(len(batches)))+''',Bool.true_and]

theorem feasible_case (c : Fin 374)
    (feasible : Feasible 34 (fun _ => 6) (pairCompletion (TwentyFiveUnit9Data.catalogue c))) :
    ∃ d : Fin 147, TwentyFiveUnit9Data.catalogue c=TwentyFiveNineLowInventory.big d := by
  have mem : TwentyFiveUnit9Data.catalogue c∈rows.map FamilyRow.source := by
    rw [sources]
    exact List.mem_ofFn.mpr ⟨c,rfl⟩
  obtain ⟨r,mem,same⟩ := List.mem_map.mp mem
  have quick := of_decide_eq_true (List.all_eq_true.mp checked r mem)
  refine ⟨r.target,?_⟩
  rw [← same] at feasible ⊢
  exact family_sound (fun _ => 6) TwentyFiveNineLowInventory.big r quick feasible

/-- Every actual nine-low unit choice is represented with its true counts. -/
theorem actual (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 9 ↪ Fin 25) (unit : Unit H f) (degrees : ∀ i, H.degree (f i)=6) :
    ∃ c : Fin 147, ∃ σ : Equiv.Perm (Fin 9),
      large H (σ.toEmbedding.trans f)=TwentyFiveNineLowInventory.big c ∧
      (∀ T, count H (σ.toEmbedding.trans f) T=TwentyFiveNineLow.μ c T) := by
  obtain ⟨c,σ,same⟩ := TwentyFiveUnit9Actual.actual H f unit
  let g := σ.toEmbedding.trans f
  have gUnit : Unit H g := unit_relabel H f unit σ
  obtain ⟨counts,feasible⟩ := actual_inventory H g gUnit (fun _ => 6) (fun i => degrees (σ i))
  rw [edges,show large H g=TwentyFiveUnit9Data.catalogue c from same] at counts feasible
  obtain ⟨d,normal⟩ := feasible_case c feasible
  refine ⟨d,σ,same.trans normal,?_⟩
  intro T
  rw [counts T,normal]
  exact TwentyFiveNineLowInventory.recovered d T
end Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
''';write(name,s)
# Last extensions: raw selected blocks alongside each permutation/refutation.
name='TwentyFiveNineLowTenthRowsData'
s=hdr(name,['TwentyFiveNineLowTenthInventory','TwentyFiveConditionalRows'],
 'TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitConditional TwentyFiveConditionalRows Aris4Math.K6Classification')
s+='''def base : Fin 6 → Fin 147 := ![0,0,3,3,6,6]
def lastDegree : Fin 6 → ℕ := ![6,7,6,7,6,7]
def degrees (g : Fin 6) (i : Fin 10) : ℕ := if i.val<9 then 6 else lastDegree g
def oldBig (g : Fin 6) := TwentyFiveNineLowInventory.big (base g)
'''
s+='def candidates : Fin 6 → List (Finset (Fin 9)) := !['+',\n'.join(listed(g['candidates'],9) for g in groups)+']\n'
ns=[];numbatches=[];all_rows=[]
for gidx,g in enumerate(groups):
 big=q9[g['base']]['large_blocks'];rlist=[]
 for chosen,w in zip(choices(g['candidates']),g['certificates']):
  ext=[t for t in big if t not in chosen]+[t|512 for t in chosen]
  wit='⟨'+str(w['target'])+',!['+','.join(map(str,w['permutation']))+']⟩'
  reject='none' if w['feasible'] else rejection(ext,10,[6]*9+[g['degree']])
  rlist.append('⟨'+family(chosen,9)+','+wit+','+reject+'⟩')
 bs=chunks(rlist,64);numbatches.append(len(bs));all_rows.append(rlist)
 for j,chunk in enumerate(bs):s+=f'def rows{gidx}_{j} : List (Row 9 25) := ['+',\n'.join(chunk)+']\n'
 s+=f'def rows{gidx} : List (Row 9 25) := '+' ++ '.join(f'rows{gidx}_{j}' for j in range(len(bs)))+'\n'
s+='end Aris4Math.ThirtyFour.'+name+'\n';write(name,s)
for g,num in enumerate(numbatches):
 for j in range(num):
  name=f'TwentyFiveNineLowTenthRows{g}Batch{j}'
  s=hdr(name,['TwentyFiveNineLowTenthRowsData'],'TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData')
  s+=f'theorem checked : rows{g}_{j}.all (fun r => decide (QuickCheck (degrees {g}) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig {g}) r))=true := by decide +kernel\n'
  s+='end Aris4Math.ThirtyFour.'+name+'\n';write(name,s);ns.append(name);build.append(name)
name='TwentyFiveNineLowTenthCoverage'
s=hdr(name,ns,'TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitConditional TwentyFiveConditionalRows Aris4Math.K6Classification')
s+='export TwentyFiveNineLowTenthRowsData (base lastDegree degrees oldBig candidates)\n'
s+='''theorem candidates_eq : ∀ g,(candidates g).toFinset=
  (pairCompletion (oldBig g)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (g : Fin 6) (T : Finset (Fin 9))
    (mem : T∈pairCompletion (oldBig g)) (small : T.card≤4) : T∈candidates g := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
'''
for g,num in enumerate(numbatches):
 s+=f'''theorem selected{g} : TwentyFiveNineLowTenthRowsData.rows{g}.map Row.selected=choices (candidates {g}) ∅ := by decide +kernel

def witnesses{g} : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows{g}.map Row.witness

theorem checked{g} : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees {g}) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig {g}))
  (choices (candidates {g}) ∅) witnesses{g} := by
  rw [← selected{g}]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows{g},List.all_append,'''+','.join(f'TwentyFiveNineLowTenthRows{g}Batch{j}.checked' for j in range(num))+''',Bool.true_and]
'''
s+='def witnesses : Fin 6 → List (Witness 10 25) := !['+','.join(f'witnesses{i}' for i in range(6))+']\n'
s+='''theorem checked (g : Fin 6) : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees g) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig g))
  (choices (candidates g) ∅) (witnesses g) := by
  fin_cases g
'''
for g in range(6):s+=f'  · exact checked{g}\n'
s+='end Aris4Math.ThirtyFour.'+name+'\n';write(name,s)
(HERE/'Q9_FAST_ROWS_BUILD_MANIFEST.json').write_text(json.dumps({'batch_size':64,'filter_rows':374,'tenth_rows':sum(len(x) for x in all_rows),'targets':build},indent=2)+'\n')
(HERE/'Q9_FAST_ROWS_PILOT.json').write_text(json.dumps({'filter':rows[:5],'tenth':all_rows[0][:5]},indent=2)+'\n')
print(json.dumps({'filter_rows':374,'tenth_rows':sum(len(x) for x in all_rows),'batches':len(build),'tenth_batches':numbatches}))

"""Materialize the existing word-coefficient recipe as newfree-solverinput."""
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;START=time.process_time()
pred=json.loads((OUT/'PREDICTION.json').read_text());assert pred['frozen_before_free_parameter_enumeration']
monom=[tuple(int(i==j) for i in range(8)) for j in range(8)]
for k in range(8,20):monom.append(tuple(monom[k-2][j]-monom[k-4][j]+monom[k-6][j]-monom[k-8][j] for j in range(8)))
arcs=[]
for phase,var in zip([1,12,11,16],[None,0,1,2]):arcs.extend([(phase,var,1,0),((-phase)%20,var,-1,(-phase)%20)])
layers=[set() for _ in range(20)];counts=[0]*5

def add(phase,form,depth,last):
 counts[depth]+=1;layers[phase].add(form)
 if depth==4:return
 for k,(dp,var,sign,shift) in enumerate(arcs):
  if last is not None and k==(last^1):continue
  ff=form
  if var is not None:
   ff=list(form)
   for j,x in enumerate(monom[(phase+shift)%20]):ff[var*8+j]+=sign*x
   ff=tuple(ff)
  add((phase+dp)%20,ff,depth+1,k)
add(0,(0,)*24,0,None)
old=json.loads((OUT.parent/'RESULT.json').read_text())
cached={c['r']:c for c in old['primitive61_cases']}
with (OUT/'coefficients.txt').open('w') as f:
 f.write('8\n')
 for r in pred['primitive_order20_roots']:
  c=cached[r];assert c['covered_by_phase'][10]<61
  f.write(f"{r} {c['parameters']['B']} {c['parameters']['D']} {c['covered_by_phase'][10]}\n")
  for phase in range(20):
   rows=sorted({tuple(sum(v[8*block+j]*pow(r,j,61) for j in range(8))%61 for block in range(3)) for v in layers[phase]})
   f.write(f'{len(rows)}\n')
   for a,b,c in rows:f.write(f'{a} {b} {c}\n')
(OUT/'INPUT_SCOPE.json').write_text(json.dumps({'roots':8,'reducedword_counts':counts,'formal_capacity_by_phase':[len(x) for x in layers],
 'cached_canonical_rejections_reused':8,'old_numeric_cases_rerun':0,'source_graphs_reverified':0,'CPU_seconds':time.process_time()-START},indent=2)+'\n')
print('newfree solvercoeffinput ready;8cachedcanonicalrejections retained, no oldnumeric cases rerun')

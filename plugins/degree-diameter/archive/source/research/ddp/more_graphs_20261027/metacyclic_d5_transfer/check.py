"""Fixed two-orbit C5 pattern: formal capacity then four-rootp311 transfer."""
from pathlib import Path
import json,time,resource,subprocess
START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(85,90))
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3]
s=json.loads((OUT/'SOURCE_AND_POLYNOMIALS.json').read_text())
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_symbolic_capacity']
monom=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
# id,destination,phase change,variable block,sign,coefficient power
arcs={0:[(0,0,1,None,1,0),(1,0,4,None,-1,4)],1:[(2,1,2,0,1,0),(3,1,3,0,-1,3)]}
for j,(phase,var) in enumerate([(0,None),(2,1),(3,2),(1,3),(0,4)]):
 arcs[0].append((4+2*j,1,phase,var,1,0));arcs[1].append((5+2*j,0,(-phase)%5,var,-1,(-phase)%5))
forms=[];walk_counts=[]
for startside in [0,1]:
 layers={(side,phase):set() for side in [0,1] for phase in range(5)};counts=[0]*6
 def walk(side,phase,form,depth,previous):
  counts[depth]+=1;layers[side,phase].add(form)
  if depth==5:return
  for edge,other,change,var,sign,shift in arcs[side]:
   if previous is not None and edge==(previous^1):continue
   f=form
   if var is not None:
    f=list(form);m=monom[(phase+shift)%5]
    for k in range(4):f[var*4+k]+=sign*m[k]
    f=tuple(f)
   walk(other,(phase+change)%5,f,depth+1,edge)
 walk(startside,0,(0,)*20,0,None)
 forms.append(layers);walk_counts.append(counts)
capacity=[[{'end_side':side,'end_phase':phase,'distinct_forms':len(fs)} for (side,phase),fs in sorted(layer.items())] for layer in forms]
mincap=min(r['distinct_forms'] for row in capacity for r in row)
result={'status':'FORMAL_CAPACITY_COMPLETE','source_p':281,'target_p':311,'target_n':3110,'target_Delta':7,'target_D':5,
 'pattern':'two-copy Fp semidirect C5; sideA internalphase+/-1,sideB+/-2; crossphases0,2,3,1,0',
 'gauge':'Atranslation0,S4translation1;freevariablesB,S1,S2,S3; coefficientringZ[z]/Phi5',
 'reduced_walk_counts_by_length':walk_counts,'free_form_capacities_by_root':capacity,'minimum_free_form_capacity':mincap,
 'source_graph_reverified':False,'old_BFS_repeated':False,'new_graphs_generated':0,'numerical_target_cases':[],'new_lower_bounds':0}
poly=[s['source_canonical_polynomials'][name] for name in ['b','s1','s2','s3']]+[[1,0,0,0]]
def multiply(a,b):
 c=[0]*5
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[(i+j)%5]+=x*y
 return [c[i]-c[4] for i in range(4)]
def substitute(f):
 out=[0]*4
 for j in range(5):
  v=multiply(f[4*j:4*j+4],poly[j])
  for k in range(4):out[k]+=v[k]
 return tuple(out)
if mincap<311:
 result.update(status='FIXED_PHASE_PATTERN_CAPACITY_BELOW311',scope_closed='Entire fixedtwo-base C5 quotient pattern over primesp>=311, not onlychosenpolynomial lifts; all otherpatterns/groups remainopen.')
 root,side,phase=min((root,side,phase) for root in range(2) for(side,phase),fs in forms[root].items() if len(fs)==mincap)
 (OUT/'capacity_witness.json').write_text(json.dumps({'root_side':root,'end_side':side,'end_phase':phase,'distinct_forms':mincap,'forms':sorted(forms[root][side,phase])},indent=2)+'\n')
else:
 substituted=[{k:{substitute(f) for f in fs} for k,fs in layer.items()} for layer in forms]
 cpoly=[[{'end_side':side,'end_phase':phase,'distinct_integer_polynomials':len(fs)} for(side,phase),fs in sorted(layer.items())]for layer in substituted]
 minpoly=min(r['distinct_integer_polynomials'] for layer in cpoly for r in layer)
 result.update(canonical_polynomial_capacities_by_root=cpoly,minimum_canonical_polynomial_capacity=minpoly)
 if minpoly<311:
  result.update(status='CANONICAL_POLYNOMIAL_LIFT_CAPACITY_BELOW311',scope_closed='This frozen minimalheightcyclotomic lift only; freephasepattern isnot excluded.')
  root,side,phase=min((root,side,phase) for root in range(2) for(side,phase),fs in substituted[root].items() if len(fs)==minpoly)
  (OUT/'capacity_witness.json').write_text(json.dumps({'root_side':root,'end_side':side,'end_phase':phase,'distinct_polynomials':minpoly,'polynomials':sorted(substituted[root][side,phase])},indent=2)+'\n')
 else:
  p=311;roots=[r for r in range(2,p) if pow(r,5,p)==1]
  assert len(roots)==4
  result['target_primitive_fifth_roots']=roots
  for r in roots:
   evaluate=lambda f:sum(c*pow(r,j,p) for j,c in enumerate(f))%p
   vv={name:evaluate(s['source_canonical_polynomials'][name]) for name in ['b','s1','s2','s3']}
   layers=[];full=True
   for origin in range(2):
    row=[]
    for(side,phase),fs in sorted(substituted[origin].items()):
     values={evaluate(f) for f in fs};missing=sorted(set(range(p))-values)
     row.append({'end_side':side,'end_phase':phase,'covered':len(values),'missing':missing})
     full=full and not missing
    layers.append(row)
   case={'r':r,'p':p,'n':10*p,'parameters':vv,'root_layer_coverage':layers,'all_layers_full':bool(full),'graph_generated':False}
   if full:
    q=5*p;n=2*q;edges=set()
    encode=lambda x,i:x*5+i
    inv=lambda x,i:(-pow(r,(-i)%5,p)*x%p,(-i)%5)
    cross=[(0,0),(vv['s1'],2),(vv['s2'],3),(vv['s3'],1),(1,0)]
    for x in range(p):
     for i in range(5):
      for side,(u,j) in enumerate([(0,1),(vv['b'],2)]):
       for a,b in [(u,j),inv(u,j)]:
        z=side*q+encode(x,i);w=side*q+encode((x+pow(r,i,p)*a)%p,(i+b)%5);edges.add(tuple(sorted((z,w))))
      for a,b in cross:edges.add(tuple(sorted((encode(x,i),q+encode((x+pow(r,i,p)*a)%p,(i+b)%5)))))
    assert len(edges)==n*7//2
    path=OUT/f'graph_d7_D5_n{n}_r{r}.edges'
    with path.open('w') as out:
     out.write(f'{n} {len(edges)}\n')
     for a,b in sorted(edges):out.write(f'{a} {b}\n')
    verify=subprocess.run([str(ROOT/'computations/ddp/verify_graph'),str(path),'7','5'],capture_output=True,text=True)
    case.update(graph_generated=True,edge_file=path.name,independent_check_returncode=verify.returncode,independent_check=json.loads(verify.stdout))
    (OUT/f'independent_r{r}.json').write_text(verify.stdout)
    assert verify.returncode==0
    result['new_graphs_generated']+=1
    print('HIT',r,path,flush=True)
   result['numerical_target_cases'].append(case)
  result['status']='FOUR_ROOT_TRANSFER_COMPLETE_WITH_HITS' if result['new_graphs_generated'] else 'FOUR_ROOT_TRANSFER_COMPLETE_NO_HIT'
  result['scope_closed']='Exactly this frozen canonicalpolynomiallift atp311 andall4primitivefifthroots; noothercoefficientrepresentations/fields/groups excluded.'
result['CPU_seconds']=time.process_time()-START;result['pending']=[]
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='numerical_target_cases'},ensure_ascii=False,indent=2))
for c in result['numerical_target_cases']:
 print('CASE',c['r'],'full',c['all_layers_full'],'coveredbyroot',[[q['covered'] for q in l]for l in c['root_layer_coverage']])

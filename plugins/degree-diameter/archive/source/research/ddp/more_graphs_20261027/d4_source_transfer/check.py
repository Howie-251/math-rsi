"""One source-derivedC20 D4 rule: targetfieldcapacity, then fixedCRT lifts."""
from pathlib import Path
import json,time,resource,subprocess
START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(55,60))
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3]
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_capacity_test']
# Phi20=t8-t6+t4-t2+1; monomial powers0..19 in degree<8 basis.
monom=[tuple(int(i==j) for i in range(8)) for j in range(8)]
for k in range(8,20):monom.append(tuple(monom[k-2][i]-monom[k-4][i]+monom[k-6][i]-monom[k-8][i] for i in range(8)))
assert monom[10]==(-1,0,0,0,0,0,0,0)
# Positive sourcephases1,12,11,16; A=0,freeB/C/D in blocks0/1/2.
phases=[1,12,11,16];arcs=[]
for j,(phase,var) in enumerate(zip(phases,[None,0,1,2])):
 arcs.extend([(phase,var,1,0),((-phase)%20,var,-1,(-phase)%20)])
layers=[set() for _ in range(20)];walk_counts=[0]*5
# Left-prepending enumerates all reduced groupwords for the source right-action multiplication.
def walk(phase,form,depth,last):
 walk_counts[depth]+=1;layers[phase].add(form)
 if depth==4:return
 for k,(dp,var,sign,shift) in enumerate(arcs):
  if last is not None and k==(last^1):continue
  nf=form
  if var is not None:
   nf=list(form);v=monom[(phase+shift)%20]
   for t in range(8):nf[var*8+t]+=sign*v[t]
   nf=tuple(nf)
  walk((phase+dp)%20,nf,depth+1,k)
walk(0,(0,)*24,0,None)
capacity=[len(s) for s in layers]
result={'status':'CAPACITY_COMPLETE','target_Delta':8,'target_D':4,'saved_baseline_order':1100,'baseline_read_date':'2026-10-27',
 'source_m':55,'source_quotient':20,'source_action':2,'source_reverified':False,'old_source_BFS':0,
 'positive_generator_phases':phases,'walk_counts_by_length':walk_counts,'free_B_C_D_Phi20_capacity_by_phase':capacity,'minimum_free_capacity':min(capacity),
 'primitive61_cases':[],'CRT_cases':[],'graphs_generated':0,'independent_full_graph_checks':0,'new_lower_bounds':0}
independent_done=False

def maybe_export(case,m,r,values):
 global independent_done
 if not case['all_phase_layers_full']:return
 n=20*m;generators=[(1,0),(12,values['B']),(11,1),(16,values['D'])];full=[]
 for dp,b in generators:full.extend([(dp,b),((-dp)%20,-b*pow(r,-dp,m)%m)])
 es=set()
 for phase in range(20):
  for x in range(m):
   u=phase*m+x
   for dp,b in full:es.add(tuple(sorted((u,((phase+dp)%20)*m+(x*pow(r,dp,m)+b)%m))))
 assert len(es)==4*n
 path=OUT/f'graph_d8_D4_n{n}_m{m}_r{r}.edges'
 with path.open('w') as f:
  f.write(f'{n} {len(es)}\n')
  for u,v in sorted(es):f.write(f'{u} {v}\n')
 case['graph_generated']=True;case['edge_file']=path.name;result['graphs_generated']+=1
 if not independent_done:
  q=subprocess.run([str(ROOT/'computations/ddp/verify_graph'),str(path),'8','4'],capture_output=True,text=True)
  assert q.returncode==0,(q.stdout,q.stderr)
  (OUT/'first_hit_independent.json').write_text(q.stdout)
  case['independent_check']=json.loads(q.stdout);result['independent_full_graph_checks']+=1;independent_done=True
 print('HIT',json.dumps({'m':m,'r':r,'n':n,'edge_file':path.name}),flush=True)

if min(capacity)<61:
 result['primitive61_status']='FREE_PHASE_PATTERN_CAPACITY_REJECTED'
 j=capacity.index(min(capacity));(OUT/'primitive_capacity_witness.json').write_text(json.dumps({'phase':j,'capacity':capacity[j],'forms':sorted(layers[j])},indent=2)+'\n')
else:
 polynomial_B=[-2,0,0,0,0,0,0,0];polynomial_C=[1,0,0,0,0,0,0,0];polynomial_D=[1,1,0,0,1,0,0,0]
 polys=[polynomial_B,polynomial_C,polynomial_D]
 def substitute(f):
  out=[0]*8
  for var in range(3):
   for i,a in enumerate(f[8*var:8*var+8]):
    for j,b in enumerate(polys[var]):
     if a and b:
      for k,c in enumerate(monom[i+j]):out[k]+=a*b*c
  return tuple(out)
 fixed=[{substitute(f) for f in layer} for layer in layers]
 fixedcap=[len(v) for v in fixed];result['fixed_polynomial_Phi20_capacity_by_phase']=fixedcap;result['minimum_fixed_capacity']=min(fixedcap)
 if min(fixedcap)<61:
  result['primitive61_status']='FIXED_POLYNOMIAL_CAPACITY_REJECTED'
  j=fixedcap.index(min(fixedcap));(OUT/'primitive_fixed_capacity_witness.json').write_text(json.dumps({'phase':j,'capacity':fixedcap[j],'polynomials':sorted(fixed[j])},indent=2)+'\n')
 else:
  roots=[r for r in range(2,61) if pow(r,20,61)==1 and pow(r,10,61)!=1 and pow(r,4,61)!=1];assert len(roots)==8
  result['primitive61_status']='NUMERIC_ALL8_ROOTS_COMPLETE'
  for r in roots:
   values={'B':(pow(r,10,61)-1)%61,'C':1,'D':(1+r+pow(r,4,61))%61}
   covered=[{sum(c*pow(r,j,61) for j,c in enumerate(f))%61 for f in fs} for fs in fixed]
   case={'m':61,'r':r,'n_hypothetical':1220,'parameters':values,'covered_by_phase':[len(v) for v in covered],'missing_by_phase':[sorted(set(range(61))-v) for v in covered],
    'all_phase_layers_full':all(len(v)==61 for v in covered),'graph_generated':False}
   maybe_export(case,61,r,values);result['primitive61_cases'].append(case)

# This branch keeps the actual composite source integer rule, not Phi20.
if not result['graphs_generated']:
 candidates=[m for m in range(56,161) if (2**20-1)%m==0];assert candidates==[75,93,123,155]
 result['CRT_candidate_divisors_complete_range']=candidates
 for m in candidates:
  r=2;values={'B':1023%m,'C':1,'D':19%m};generators=[(1,0),(12,values['B']),(11,1),(16,19%m)];numeric=[]
  for dp,b in generators:numeric.extend([(dp,b),((-dp)%20,-b*pow(2,-dp,m)%m)])
  cov=[set() for _ in range(20)]
  def direct(phase,x,depth,last):
   cov[phase].add(x)
   if depth==4:return
   for k,(dp,b) in enumerate(numeric):
    if last is not None and k==(last^1):continue
    direct((phase+dp)%20,(x+pow(2,phase,m)*b)%m,depth+1,k)
  direct(0,0,0,None)
  order=next(j for j in range(1,21) if pow(2,j,m)==1)
  case={'m':m,'r':2,'n_hypothetical':20*m,'action_order':order,'parameters':values,'covered_by_phase':[len(v) for v in cov],
   'missing_by_phase':[sorted(set(range(m))-v) for v in cov],'all_phase_layers_full':all(len(v)==m for v in cov),'graph_generated':False}
  maybe_export(case,m,2,values);result['CRT_cases'].append(case)
result['status']='COMPLETE_WITH_HITS' if result['graphs_generated'] else 'COMPLETE_FIXED_SOURCE_RULE_NO_HIT'
result['scope']='Lozsource fixedphases1/12/11/16,integerB=r10-1,C=1,D=1+r+r4,A=0; p61 primitive20 target gated byPhi20 capacity; ifnohit, exactlyall4divisors75/93/123/155 atliteralr2. Nootheroffsets/phasepatterns tested.'
result['actual_D']=None;result['ordinary_bad_unordered_pairs']=None;result['CPU_seconds']=time.process_time()-START;result['pending']=[]
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['primitive61_cases','CRT_cases']},ensure_ascii=False,indent=2))
for section in ['primitive61_cases','CRT_cases']:
 for c in result[section]:print(section,c['m'],c['r'],'full',c['all_phase_layers_full'],'root_missing',sum(c['m']-k for k in c['covered_by_phase']),'phase_coverage',c['covered_by_phase'])

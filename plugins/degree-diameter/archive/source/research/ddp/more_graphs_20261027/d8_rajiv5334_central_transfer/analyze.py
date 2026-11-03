"""One centralC3 expansion of the fixed Rajiv5334 projection; reduced words, no BFS."""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time,resource,sys
resource.setrlimit(resource.RLIMIT_CPU,(55,55));START=time.process_time();H=Path(__file__).resolve().parent;ROOT=H.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(name,obj):
 def strings(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in strings(v)]
  if isinstance(z,(tuple,list)):return[t for v in z for t in strings(v)]
  return[]
 assert not screen('\n'.join(strings(obj)));(H/name).write_text(json.dumps(obj,indent=2)+'\n')
assert not(H/'terminal.json').exists(),'Fixed centralC3 scope already terminal'
save('PREDICTION.json',dict(status='FROZEN_BEFORE_ORDER_OR_MULTIPLICITY_CHECK',prediction='Some fixedbase endpoint may have fewerthan3distinct mod3 signedgenerator-countvectors within5steps, obstructing alltrivialcentralC3assignments.',
 source='context/DD_PORTFOLIO_START_20261026/baselines/generator_specs.json:d8_D5',base_quotient=21,base_fibre=127,action=25,positive_phases=[2,3,6,8],positive_fibre_voltages=[60,122,81,42],target_order=8001,target_Delta=8,target_D=5,source_C2_not_reverified=True,
 CPU_budget=60,workers=1,no_other_fields_offsets_or_seeds=True))
save('PLAN.json',dict(scope='Only fixed C21semidirectF127 projection and all four-generator centralvoltages inC3; notallRajiv5334 transfers.',steps=[
 'Check25 exactmultiplicativeorder modulo127 andthe right-action group law.',
 'Enumerate all22409 inverse-reduced8letter words oflength<=5, collectexactinteger andmod3signedcountvectors at eachbaseendpoint.',
 'If any endpoint has fewerthan3mod3vectors, savecompletewitness andstop withoutvoltageassignments.',
 'Otherwise freezeall81centralvoltageassignments andexactlycheckallbaseendpointC3images;exportonlyafullhit.'],
 prior_ledger='Known5334baseline ispreviouslyverified, notnew; old2810C5two-copycyclotomictransfer andUT3F9centralcapacity aredifferentclosedscopes.'))
P=127;M=21;R=25;ph=[2,3,6,8];bs=[60,122,81,42]
order=next(k for k in range(1,127) if pow(R,k,P)==1);assert order==21 and pow(R,M,P)==1
positive=[(ph[i],bs[i]) for i in range(4)];signed=[]
for i,(u,b) in enumerate(positive):
 signed.append((i,1,u,b));signed.append((i,-1,(-u)%M,(-b*pow(R,-u,P))%P))
assert len({(u,b) for i,s,u,b in signed})==8
# Each record stores literal word,signed count vector, and alreadycomputedbaseendpoint.
byendpoint=[[] for _ in range(M*P)];level=[(0,0,(),(0,0,0,0),None)];byendpoint[0].append(('',(0,0,0,0)))
wordcount=1
for depth in range(1,6):
 nxt=[]
 for phase,x,word,c,last in level:
  for i,s,u,b in signed:
   if last==(i,-s):continue
   nphase=(phase+u)%M;nx=(x*pow(R,u,P)+b)%P;v=list(c);v[i]+=s;v=tuple(v);w=word+(chr(65+i) if s==1 else chr(97+i),)
   nxt.append((nphase,nx,w,v,(i,s)));byendpoint[nphase*P+nx].append((''.join(w),v));wordcount+=1
 level=nxt
assert wordcount==22409
integer_sets=[];mod3sets=[];hist_integer=Counter();hist_mod3=Counter();hist_words=Counter()
for routes in byendpoint:
 iv={v for w,v in routes};mv={tuple(x%3 for x in v) for v in iv};integer_sets.append(iv);mod3sets.append(mv);hist_integer[len(iv)]+=1;hist_mod3[len(mv)]+=1;hist_words[len(routes)]+=1
min_integer=min(map(len,integer_sets));min_mod3=min(map(len,mod3sets));bottlenecks=[i for i,s in enumerate(mod3sets) if len(s)<3]
profile=dict(base_order=M*P,reduced_words=wordcount,action25_order=order,
 minimum_integer_countvectors=min_integer,minimum_mod3_countvectors=min_mod3,
 integer_vector_count_histogram={str(k):v for k,v in sorted(hist_integer.items())},mod3_vector_count_histogram={str(k):v for k,v in sorted(hist_mod3.items())},route_count_histogram={str(k):v for k,v in sorted(hist_words.items())},
 baseendpoints_below3mod3vectors=len(bottlenecks),CPU_seconds=time.process_time()-START)
save('MULTIPLICITY.json',profile);print('MULTIPLICITY '+json.dumps(profile),flush=True)
results=[];hit=None
if bottlenecks:
 j=min(bottlenecks,key=lambda i:(len(mod3sets[i]),i));routes=byendpoint[j]
 witness=dict(endpoint_phase=j//P,endpoint_fibre=j%P,base_vertex_id=j,rightlaw='(i,x)(j,y)=(i+j,x*25^j+y)',
 all_reduced_routes_length_atmost5=[dict(word=w,integer_signedcounts=list(v),mod3_signedcounts=[a%3 for a in v]) for w,v in routes],
 integer_signedcountvectors=[list(v) for v in sorted(integer_sets[j])],mod3_signedcountvectors=[list(v) for v in sorted(mod3sets[j])],
 upper_central_residues_for_every_assignment=len(mod3sets[j]),needed_residues=3,
 obstruction='For anyfixedcentralvoltageomega, reachablecentralvaluesatthisbaseendpointaresubset{dot(omega,c):cinsavedmod3vectors},sotheircountisbelow3.')
 save('OBSTRUCTION.json',witness);status='EXACT_FIXED_BASE_TRIVIAL_C3_CAPACITY_OBSTRUCTION';print('OBSTRUCTION '+json.dumps(witness),flush=True)
else:
 assignments=[list(a) for a in product(range(3),repeat=4)];assert len(assignments)==81
 save('ASSIGNMENT_SCOPE.json',dict(status='FROZEN_BEFORE_ASSIGNMENT_COVERAGE',assignments=assignments,common_sign_quotient_used=False,translation_scope_fixed=True))
 for omega in assignments:
  missing=0;bad=[]
  for j,vs in enumerate(mod3sets):
   z={sum(a*b for a,b in zip(omega,v))%3 for v in vs}
   if len(z)<3:
    missing+=3-len(z)
    if len(bad)<8:bad.append(dict(base_phase=j//P,base_fibre=j%P,missing_central=sorted({0,1,2}-z)))
  results.append(dict(omega=omega,missing_identityroot_endpoints_within5=missing,missing_sample=bad))
  if not missing:hit=omega;break
 save('ASSIGNMENT_RESULTS.json',dict(cases_tested=len(results),stopped_at_first_full_hit=hit is not None,results=results))
 if hit is not None:
  crt=[b+127*((z-b)%3) for b,z in zip(bs,hit)];assert pow(25,21,381)==1
  gens=set()
  for u,b in zip(ph,crt):gens.add((u,b));gens.add(((-u)%21,(-b*pow(25,-u,381))%381))
  assert len(gens)==8
  edges=set()
  for i in range(21):
   for x in range(381):
    v=i*381+x
    for u,b in gens:
     w=((i+u)%21)*381+(x*pow(25,u,381)+b)%381;assert v!=w;edges.add(tuple(sorted((v,w))))
  assert len(edges)==32004
  (H/'graph_d8_D5_n8001.edges').write_text('8001 32004\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
  save('hit.json',dict(m=21,n=381,a=25,positive_generators=[[u,b] for u,b in zip(ph,crt)],central_voltages=hit,base_translations=bs,
  vertex_label='phase*381+CRTtranslation',order=8001,edges=32004,max_degree=8,identityroot_reducedword_coverage_full=True,
  global_cover_basis='Cayley lefttranslations preserve rightgenerator adjacency; allgroupvertices within5fromidentity impliesallpairdistance<=5.',
  root_independent_acceptance_pending=True,new_record_claimed=False))
  status='COMPLETE8001_CENTRAL_TRANSFER_CANDIDATE_AWAIT_ROOT'
 else:status='COMPLETE_ALL81_FIXEDCENTRAL_ASSIGNMENTS_NO_HIT'
final=dict(status=status,base_order=2667,target_order=8001,target_Delta=8,target_D=5,action_order=order,reduced_words=22409,
 integer_countvector_minimum=min_integer,mod3_countvector_minimum=min_mod3,capacity_obstructed=bool(bottlenecks),obstruction_endpoint_count=len(bottlenecks),
 central_assignments_tested=len(results),hit=hit,new_graph_generated=hit is not None,record_claimed=False,
 scope='OnlydirectcentralC3 withfixedC21semidirectF127action25andtranslations60/122/81/42;notalloriginal5334mechanisms,otherextensionsoroffsets.',
 source_C2_BFS_repeated=False,new_BFS=False,old_graph_reproduced=False,CPU_seconds=time.process_time()-START,workers=1,extra_seeds=0)
save('RESULT.json',final);save('terminal.json',final);print('FINAL '+json.dumps(final),flush=True)

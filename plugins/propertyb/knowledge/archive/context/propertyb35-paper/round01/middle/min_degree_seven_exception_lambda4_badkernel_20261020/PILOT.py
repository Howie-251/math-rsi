"""Only18 exceptional spectra's explicitlambda4 branches; exclude potentialbadK cost<=7 using reused gates and old3-layout relevant-key pilot. No lambda5 claim."""
from pathlib import Path
from itertools import combinations,product,permutations
from fractions import Fraction
from collections import defaultdict,Counter
from math import comb
import json,time,sys
P=Path(__file__).resolve().parent;B=P.parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));from subset_position_dp import SubsetEngine
st=time.process_time();limit=4.6
strong=json.loads((B/'min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json').read_text());exception=set(strong['spectra_with_unexcluded_pairs']);old=json.loads((ROOT/'context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/RESULT.json').read_text());source=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text());source={j['spectrum_id']:j for j in source['jobs']}
jobs=[j for j in old['jobs'] if j['spectrum_id'] in exception and not j['strict']];assert len(jobs)==6
known={tuple(z['quad']) for z in json.loads((B/'c13_remaining_actual_quads_20261020/ALL_RESULT.json').read_text())['quad_support']};known.add((8,8,8,8))
previous=json.loads((B/'min_degree_seven_residual_cap12_pilot_20261020/RESULT.json').read_text());prior_cases={tuple(z['counts']):z for z in previous['checked_cases'] if not z['legacy']};prior_quads={tuple(z['quad']) for z in previous['full_missing_quad_projection']};prior_quads.discard((10,10,10,10))
newPcoupled=json.loads((ROOT/'context/propertyb35-paper/round01/root/vertex_flag_capacity_20261020/COUPLED_RESULT.json').read_text());coupled={(j['spectrum_id'],tuple(k['n']),k['tau']):k for j in newPcoupled['jobs'] if j['role']=='lambda4' for k in j['keys']}
keys=[];support=defaultdict(list);projection=[]
for j in jobs:
 sid=j['spectrum_id'];ds=j['degrees'];missing=[];qall=sorted(set(combinations(ds,4)))
 for q in qall:
  if q in known or q.count(7)>=3 or (q==(9,10,10,10) and ds.count(7)>=5):continue
  missing.append(q)
  for i,k in enumerate(j['keys']):
   if not k['strict']:support[q].append((sid,i,k,ds))
 for i,k in enumerate(j['keys']):
  if not k['strict']:keys.append({'spectrum_id':sid,'source_key_index':i,'key':k,'degrees':ds})
 projection.append({'spectrum_id':sid,'degrees':ds,'actual_quad_count':len(qall),'known_or_analytically_empty':len(qall)-len(missing),'missing_quads':missing,'source_remaining_keys':sum(not k['strict'] for k in j['keys'])})
assert len(keys)==24
pairs=(3,5,6,9,10,12);cross=(5,6,9,10);tris=(7,11,13,14);menu=((8,9,20,21),(9,10,20,21),(9,20,10,21));group=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}];maps=[tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in group]
def image(ns,mp):
 out=[0]*16
 for m,n in enumerate(ns):out[mp[m]]=n
 return tuple(out)
def degree(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4))
def h17(s):return max(0,s-34,2*s-85) if 17<=s<=68 else 10**9
patterns=[]
for vals in product(range(1,5),repeat=6):
 cost=sum(comb(v-1,2) for v in vals)
 if cost>=8:continue
 inc=dict(zip(pairs,vals))
 for tri in (0,*tris):
  base=[0]*16
  if tri:base[tri]=1
  for m,v in inc.items():base[m]=v-int(bool(tri) and tri&m==m)
  if min(base)<0 or base[3]<1 or base[12]<1 or sum(base[m] for m in cross)<13:continue
  patterns.append((base,inc,tri,cost))
queue=[];quadrecords=[];allcases=[]
for q,contexts in sorted(support.items()):
 labeled=set()
 for ds in set(permutations(q)):
  for base,inc,tri,cost in patterns:
   ns=base.copy()
   for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
   ns[0]=35-sum(ds)+sum(inc.values())-int(bool(tri))
   if min(ns)>=0:labeled.add(tuple(ns))
 reps=sorted({min(image(ns,mp) for mp in maps) for ns in labeled});entries=[]
 for ns in reps:
  inc={m:sum(n for T,n in enumerate(ns) if T&m==m) for m in pairs};cost=sum(comb(v-1,2) for v in inc.values());ds=degree(ns);outside=sum(h17(4*d-sum(v for T,v in inc.items() if T>>i&1)) for i,d in enumerate(ds));active=[]
  for sid,ki,k,whole_ds in contexts:
   D=max(whole_ds);outsideD=whole_ds.count(D)>q.count(D);required=cost+max(outside,max(0,4*D-40) if outsideD else 0)
   if k['tau']>=required:active.append({'spectrum_id':sid,'source_key_index':ki,'tau':k['tau'],'required_tau':required})
  e={'quad':q,'counts':ns,'degrees':ds,'K6_cost':cost,'selected_K_row_tau_lower':cost+outside,'active_contexts':active,'active':bool(active)};entries.append(e)
  if not active:continue
  oldcase=prior_cases.get(ns)
  if oldcase is not None:
   assert oldcase['best']['strict'];e['best']=oldcase['best'];e['reused_verified_previous_case']=True;allcases.append(e)
  else:queue.append(e)
 quadrecords.append({'quad':q,'already_full_domain_in_previous36':q in prior_quads,'low_cost_labeled_count':len(labeled),'low_cost_representatives':len(reps),'low_cost_labeled_keys':sorted(labeled),'entries':entries})
print('DOMAIN','QUADS',len(quadrecords),'GENUINELY_NEW_QUADS',sum(not z['already_full_domain_in_previous36'] for z in quadrecords),'NEW_ACTIVE',len(queue),'REUSED',len(allcases),'CPU',time.process_time()-st,flush=True)
for e in queue:
 if time.process_time()-st>limit:break
 ns=e['counts'];engine=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});engine.inv={m:(0,0,[]) for m in engine.inv};vals=[]
 for pos in menu:
  lock={k:1<<i for i,k in enumerate(pos)};left=0;v=0
  for k in range(1,22):pivot=lock.get(k,0);v+=engine.value(k,left,pivot);left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(v,engine.D)),'strict':v<engine.D})
 e['menu']=vals;e['best']=min(vals,key=lambda z:Fraction(z['bound']));e['reused_verified_previous_case']=False;allcases.append(e)
 if not e['best']['strict']:e['expanded35_masks']=[m for m,n in enumerate(ns) for _ in range(n)]
checked={tuple(z['counts']):z for z in allcases};results=[]
for item in keys:
 sid,ki,k=item['spectrum_id'],item['source_key_index'],item['key'];active=[e for q in quadrecords for e in q['entries'] if any(x['spectrum_id']==sid and x['source_key_index']==ki for x in e['active_contexts'])];unprocessed=[e for e in active if tuple(e['counts']) not in checked];failed=[checked[tuple(e['counts'])] for e in active if tuple(e['counts']) in checked and not checked[tuple(e['counts'])]['best']['strict']];cost8=not unprocessed and not failed;caps=k['caps'].copy();v=k['new_twice_L'];dense=False
 if cost8 and k['tau']<=10:
  caps[3]=min(caps[3],12*k['n'][3]+18);v=6864*k['n'][1]+sum(dw*min(k['newP'],sum(caps[i:])) for i,dw in enumerate((36,84,210,462,924)));dense=True
 c=coupled[sid,tuple(k['n']),k['tau']];results.append({**item,'cost_ge8_caller_complete_in_pilot':cost8,'active_lowcost_representatives':len(active),'unprocessed':len(unprocessed),'failed_lowcost':len(failed),'dense_tau_le10_applied':dense,'new_caps':caps,'twice_L_with_dense_and_old_verified_P':v,'strict':v<5445440,'coupled_P_candidate_not_used':c['P'],'coupled_candidate_twice_L_original_caps':c['twice_L']})
out={'status':'COMPLETE_RELEVANT_COST_LE7_PILOT' if len(allcases)==len(queue)+sum(z.get('reused_verified_previous_case',False) for z in allcases) else 'CPU_BOUNDED_PARTIAL','scope':__doc__,'all18_exception_ids':sorted(exception),'source_old_vertex_P_file':'../../root/vertex_flag_capacity_20261020/RESULT.json','source24_keys_in6_spectra':keys,'actual_quad_projection':projection,'complete_missing_quad_lowcost_domains':quadrecords,'new_layouts':False,'new_active_cases':sum(not z['reused_verified_previous_case'] for z in allcases),'new_active_total':len(queue),'reused_verified_cases':sum(z['reused_verified_previous_case'] for z in allcases),'all_checked_cases':allcases,'all_new_nonstrict':[z for z in allcases if not z['best']['strict']],'key_refinement':results,'newly_strict_key_count':sum(z['strict'] for z in results),'remaining_key_count':sum(not z['strict'] for z in results),'cpu_seconds':time.process_time()-st};(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'NEW',out['new_active_cases'],'FAIL',len(out['all_new_nonstrict']),'STRICTKEYS',out['newly_strict_key_count'],'REMAIN',out['remaining_key_count'],'CPU',out['cpu_seconds'])

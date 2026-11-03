"""Two-root voltage-word capacity, then exactly two fixed canonical lifts.
No source graph is loaded; no graph BFS or parameter search is performed.
"""
import collections,datetime,importlib.util,json,pathlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(14,15))
P=pathlib.Path(__file__).resolve().parent
ROOT=P.parents[3]
start=time.process_time()
def save(name,d):
 (P/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
source={
 'source_name':'Michel de Messieres 684, October5 2026',
 'primary_url':'https://doi.org/10.5281/zenodo.23167440',
 'official_description_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html',
 'source_data':'research/ddp/m1_sources/684_recovered_construction.json',
 'source_reconstruction':'research/ddp/m1_sources/recover_684.py',
 'source_m':38,'source_quotient':9,'source_action':23,
 'operation':'(a,b)*(c,d)=(a+r^b*c modp,b+d mod9); arcs multiply coordinates on the right.',
 'positive_internal_type0':[[4,4],[25,3]],'positive_internal_type1':[[10,1],[23,6]],
 'cross_type0_to_type1':[[2,2],[2,6],[24,3]],
 'independent_translation_variable_order':['u0','u1','v0','v1','t0','t1','t2'],
 'phase_pattern_internal_type0':[4,3],'phase_pattern_internal_type1':[1,6],'phase_pattern_cross':[2,6,3],
 'inverse':'(a,b)^-1=(-r^(-b)*a modp,-b mod9)',
 'known_source_n':684,'source_graph_loaded_or_reverified':False,
 'fixed_low_coefficient_lift':['r^8-1','r^7','r^6-1','r','2','2','r^7-1'],
 'lift_scope':'One explicit low-coefficient polynomial identity per source voltage; not claimed to be a uniquely intended author family.'}
pred={
 'prediction_id':'P_MICHEL43_CROSS_LAYER','frozen_before_capacity_and_numeric_test':True,
 'falsifiable_prediction':'Among the two fixed canonical lifts r6/r36, at least one complete cross-side quotient slot of43 endpoints is reached within4 steps; full774 coverage is a separate stronger requirement.',
 'target_Delta':7,'target_D':4,'savedL':684,'baseline_as_of':'2026-10-27',
 'n':{'actual':None,'hypothetical':774},'p':43,'quotient':9,'roots':[6,36],
 'action_orders':[3,3],'freeform_gate':'For each actual r, both identity roots and all18 target side/phase slots must have at least43 distinct linear endpoint forms in all7 free translations. A failed slot excludes that action for every translation assignment.',
 'canonical_rule':source['fixed_low_coefficient_lift'],
 'canonical_positive_phases':[4,3,1,6,2,6,3],
 'allowed_numeric_cases':2,'no_other_phase_prime_offset_search':True,
 'source_BFS':0,'workers':1,'CPU_budget_seconds':15,
 'r1_abelian_inherited_obstruction':'Same-side root ball upper bound327<group387; no r1 test.'}
# Durable prediction and exact source precede every new capacity computation.
save('SOURCE.json',source);save('PREDICTION.json',pred)
phase=[4,3,1,6,2,6,3]
origin=[0,0,1,1,0,0,0];dest=[0,0,1,1,1,1,1]


def forms(r):
 arcs=[[] for _ in range(2)]
 for j,ph in enumerate(phase):
  e=[0]*7;e[j]=1
  f=[0]*7;f[j]=(-pow(r,(-ph)%9,43))%43
  arcs[origin[j]].append((2*j,dest[j],ph,tuple(e)))
  arcs[dest[j]].append((2*j+1,origin[j],(-ph)%9,tuple(f)))
 allslots=[]
 for root in range(2):
  slots=[[set() for _ in range(9)] for __ in range(2)]
  initial=(root,0,(0,)*7,-1)
  current=[initial];slots[root][0].add((0,)*7);counts=[1]
  for length in range(1,5):
   nxt=[]
   for side,b,v,prev in current:
    for label,target,d,w in arcs[side]:
     if prev>=0 and label==(prev^1):continue
     new=tuple((a+pow(r,b,43)*c)%43 for a,c in zip(v,w))
     nb=(b+d)%9;slots[target][nb].add(new)
     nxt.append((target,nb,new,label))
   current=nxt;counts.append(len(nxt))
  assert counts==[1,7,42,252,1512]
  allslots.append(slots)
 return allslots

capacity_start=time.process_time();data=[];formcache={}
for r in [6,36]:
 assert pow(r,3,43)==1 and r!=1
 slots=forms(r);formcache[r]=slots
 table=[];failed=[]
 for root in range(2):
  rows=[]
  for side in range(2):
   row=[len(slots[root][side][ph]) for ph in range(9)];rows.append(row)
   failed += [{'root':root,'target_side':side,'phase':ph,'capacity':n} for ph,n in enumerate(row) if n<43]
  table.append(rows)
 data.append({'r':r,'order':3,'capacity_root_side_phase':table,'minimum_capacity':min(n for rows in table for row in rows for n in row),'failed_slots':failed,'status':'CAPACITY_REJECTED' if failed else 'CAPACITY_PASSED'})
capacity_cpu=time.process_time()-capacity_start
save('CAPACITY.json',{'status':'COMPLETE_TWO_ACTION_FORM_CAPACITY','actions':data,'slots_per_action':36,'words_by_length_per_root':[1,7,42,252,1512],'capacity_CPU_seconds':capacity_cpu})
print('CAPACITY',[(a['r'],a['minimum_capacity'],a['failed_slots'][:1]) for a in data],flush=True)
# Exactly the predeclared two low-coefficient lifts, only where capacity permits.
numeric_start=time.process_time();numeric=[]
for a in data:
 if a['failed_slots']:continue
 r=a['r'];values=[(pow(r,8,43)-1)%43,pow(r,7,43),(pow(r,6,43)-1)%43,r,2,2,(pow(r,7,43)-1)%43]
 cov=[];missing=[];crossfull=[]
 for root in range(2):
  rows=[]
  for side in range(2):
   rows.append([])
   for ph in range(9):
    ends={sum(c*v for c,v in zip(f,values))%43 for f in formcache[r][root][side][ph]}
    rows[side].append(len(ends))
    if len(ends)<43:missing.append({'root':root,'target_side':side,'phase':ph,'missing_translations':sorted(set(range(43))-ends)})
    if side!=root and len(ends)==43:crossfull.append({'root':root,'target_side':side,'phase':ph})
  cov.append(rows)
 numeric.append({'r':r,'translation_values':values,'coverage_root_side_phase':cov,'missing_slots':missing,'complete_cross_side_slots':crossfull,'root_endpoint_missing_counts':[sum(43-n for row in rows for n in row) for rows in cov],'full774_hit':not missing})
numeric_cpu=time.process_time()-numeric_start
prediction=('NOT_REACHED_CAPACITY_REJECTED' if not numeric else ('SUPPORTED' if any(a['complete_cross_side_slots'] for a in numeric) else 'REFUTED'))
result={'status':'COMPLETE_FIXED_PATTERN_CAPACITY_REJECTED' if not numeric else 'COMPLETE_TWO_CANONICAL_LIFTS',
 'prediction_id':pred['prediction_id'],'prediction_verdict':prediction,'target_Delta':7,'target_D':4,'savedL':684,
 'n':{'actual':None,'hypothetical':774},'actual_D':None,'ordinary_bad_unordered_pairs':None,
 'actions':data,'canonical_lifts_executed':len(numeric),'canonical_results':numeric,'full_hits':sum(a['full774_hit'] for a in numeric),
 'new_graphs_generated':0,'all_source_BFS':0,'source_graph_loaded_or_reverified':False,'independent_checks':0,
 'capacity_CPU_seconds':capacity_cpu,'canonical_lifts_CPU_seconds':numeric_cpu,'total_process_CPU_seconds':time.process_time()-start,
 'CPU_scope':'Python process including source/prediction writes, freeforms and at most two canonical evaluations; no compilation.',
 'scope':'Only p43, quotient9, action roots6/36, exact recovered Michel684 phase pattern and declared polynomial lift; capacity rejection, when present, covers all7 free translation variables for that action.',
 'pending':[],'decision':'No automatic offset, phase or prime search. Report actual two-root coverage; parent decides any later four-variable finite model only from genuine full-layer feedback.'}
save('RESULT.json',result)
save('terminal.json',{k:v for k,v in result.items() if k not in ['actions','canonical_results']})
print('FINAL',prediction,'canonical',len(numeric),'fullhits',result['full_hits'],'CPU',result['total_process_CPU_seconds'],flush=True)

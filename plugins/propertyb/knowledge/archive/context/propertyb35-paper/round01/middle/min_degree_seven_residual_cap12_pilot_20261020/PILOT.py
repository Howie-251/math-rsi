"""Only missing quads affecting63 actual survivor keys in13 full-lambda4 spectra; old fixed3 positions, bounded5CPU pilot."""
from pathlib import Path
from itertools import product,permutations
from collections import defaultdict,Counter
from fractions import Fraction
from math import comb
import json,time,sys
P=Path(__file__).resolve().parent;B=P.parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));from subset_position_dp import SubsetEngine
st=time.process_time();limit=4.6
root=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text());proj={j['spectrum_id']:j for j in json.loads((B/'min_degree_seven_cap12_transfer_20261020/PROJECTION.json').read_text())};high=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/HIGH_ROW_CHECK.json').read_text());G={j['D']:j['G_D_tau0_through140'] for j in high['tables']}
jobs=[j for j in root['jobs'] if not j['strict'] and not j['lambda4_subcase_only']];assert len(jobs)==13 and sum(j['survivor_count'] for j in jobs)==63
support=defaultdict(list)
for j in jobs:
 for q in proj[j['spectrum_id']]['missing']:support[tuple(q)].append(j)
assert len(support)==37
cross=(5,6,9,10);pairs=(3,5,6,9,10,12);tris=(7,11,13,14);menu=((8,9,20,21),(9,10,20,21),(9,20,10,21))
group=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}];maps=[tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in group]
def image(ns,mp):
 out=[0]*16
 for m,n in enumerate(ns):out[mp[m]]=n
 return tuple(out)
def degree(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4))
# h17 independently obtained by exact itemwise integer cost DP.
h={0:0}
for _ in range(17):
 nxt={}
 for s,c in h.items():
  for l in (1,2,3,4):nxt[s+l]=min(nxt.get(s+l,10**9),c+comb(l-1,2))
 h=nxt
for s in range(70):assert h.get(s,10**9)==(max(0,s-34,2*s-85) if 17<=s<=68 else 10**9)
def tau_data(ns):
 ds=degree(ns);inc={pair:sum(n for m,n in enumerate(ns) if m&pair==pair) for pair in pairs};cost=sum(comb(l-1,2) for l in inc.values());outside=sum(h.get(4*ds[i]-sum(v for m,v in inc.items() if m>>i&1),10**9) for i in range(4));return cost,outside,cost+outside
patterns=[]
for vals in product(range(1,5),repeat=6):
 inc=dict(zip(pairs,vals))
 for tri in (0,*tris):
  ns=[0]*16
  if tri:ns[tri]=1
  for m,v in inc.items():ns[m]=v-int(bool(tri) and tri&m==m)
  if ns[3]<1 or ns[12]<1 or min(ns)<0 or sum(ns[m] for m in cross)<13:continue
  patterns.append((ns,inc,tri))
legacy=json.loads((B/'generic_c3_thirteen_pilot_20261020/RESULT.json').read_text());assert len(legacy['cases'])==310
allquad=[];queue=[];case_results=[]
for q,src in sorted(support.items()):
 if q==(10,10,10,10):
  cases={tuple(z['counts']):z for z in legacy['cases']};kind='REUSE_EXISTING310_LABELS_NO_NEW_BOUND'
 else:
  keys=set()
  for ds in set(permutations(q)):
   for base,inc,tri in patterns:
    ns=base.copy()
    for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
    ns[0]=35-sum(ds)+sum(inc.values())-int(bool(tri))
    if min(ns)>=0:keys.add(tuple(ns))
  cases={min(image(ns,mp) for mp in maps):None for ns in keys};kind='NEW_D8_ORBITS'
  labeled=sorted(keys)
 casesout=[]
 for ns,old in sorted(cases.items()):
  kcost,extcost,need=tau_data(ns);contexts=[]
  for j in src:
   # SelectedK-to-exterior rowpairs are disjoint acrossall4 selected points.
   # If an actual maximum-degree point necessarily remains outsideK, its row may overlap those rows; use max, not addition.
   outsideD=j['degrees'].count(j['D'])>q.count(j['D']);required=kcost+max(extcost,max(0,4*j['D']-40) if outsideD else 0)
   for ki,key in enumerate(j['survivors']):
    if key['tau']>=required and G[j['D']][key['tau']]>=13:contexts.append({'spectrum_id':j['spectrum_id'],'survivor_index':ki,'tau':key['tau'],'required_tau':required,'outside_seven_pool':j['degrees'].count(7)-q.count(7)})
  entry={'quad':q,'counts':ns,'degrees':degree(ns),'K6_tau_cost':kcost,'K_to_exterior_tau_lower':extcost,'minimum_tau_selected_K':need,'active_contexts':contexts,'active':bool(contexts),'legacy':old is not None}
  casesout.append(entry)
  if not contexts:continue
  if old is not None:
   entry['best']={'positions':old['positions'],'bound':old['bound'],'strict':old['strict']};entry['legacy_source']='../generic_c3_thirteen_pilot_20261020/RESULT.json';case_results.append(entry)
  else:queue.append(entry)
 allquad.append({'quad':q,'source_spectrum_ids':[j['spectrum_id'] for j in src],'source_keys':sum(j['survivor_count'] for j in src),'domain_kind':kind,'labeled_count':len(cases) if q==(10,10,10,10) else len(keys),'representative_count':len(cases),'minimum_tau_across_domain':min((x['minimum_tau_selected_K'] for x in casesout),default=None),'active_representatives':sum(x['active'] for x in casesout),'all_cases':casesout,'labeled_keys':None if q==(10,10,10,10) else labeled})
print('DOMAIN','QUADS',len(allquad),'NEW_ACTIVE_REPS',len(queue),'CPU',time.process_time()-st,flush=True)
# Start with smaller actual relevant quad domains; no layout extension.
size=Counter(tuple(x['quad']) for x in queue);queue.sort(key=lambda x:(size[tuple(x['quad'])],tuple(x['quad']),x['counts']))
processed=0
for entry in queue:
 if time.process_time()-st>limit:break
 ns=entry['counts'];e=SubsetEngine(21,4,{m:n for m,n in enumerate(ns) if n});e.inv={p:(0,0,[]) for p in e.inv};vals=[]
 for pos in menu:
  locks={k:1<<i for i,k in enumerate(pos)};left=0;u=0
  for at in range(1,22):pivot=locks.get(at,0);u+=e.value(at,left,pivot);left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(u,e.D)),'strict':u<e.D})
 entry['menu']=vals;entry['best']=min(vals,key=lambda x:Fraction(x['bound']));case_results.append(entry);processed+=1
 if not entry['best']['strict']:entry['expanded35_masks']=[m for m,n in enumerate(ns) for _ in range(n)]
# Reused old nonstrict cases also get actual35 inventory expansion.
for z in case_results:
 if not z['best']['strict']:z['expanded35_masks']=[m for m,n in enumerate(z['counts']) for _ in range(n)]
bycase={tuple(z['counts']):z for z in case_results};contextout=[]
for j in jobs:
 for ki,key in enumerate(j['survivors']):
  qstates=[]
  for qrec in allquad:
   if j['spectrum_id'] not in qrec['source_spectrum_ids']:continue
   active=[x for x in qrec['all_cases'] if any(z['spectrum_id']==j['spectrum_id'] and z['survivor_index']==ki for z in x['active_contexts'])]
   missing=[x for x in active if tuple(x['counts']) not in bycase];failed=[x for x in active if tuple(x['counts']) in bycase and not bycase[tuple(x['counts'])]['best']['strict']]
   qstates.append({'quad':qrec['quad'],'tau_eligible_representatives':len(active),'unprocessed':len(missing),'nonstrict':len(failed),'cap12_gate_discovered':not missing and not failed})
  contextout.append({'spectrum_id':j['spectrum_id'],'survivor_index':ki,'key':key,'missing_quad_states':qstates,'all_missing_quad_gates_discovered':all(x['cap12_gate_discovered'] for x in qstates)})
out={'status':'COMPLETE_FIXED3_RELEVANT_PILOT' if processed==len(queue) else 'CPU_BOUNDED_RELEVANT_PILOT','scope':__doc__,'source_spectra':13,'source_survivor_keys':63,'missing_quads':37,'new_quads':36,'h17_itemwise_DP_checked':True,'full_missing_quad_projection':allquad,'new_eligible_representatives':len(queue),'new_processed':processed,'new_unprocessed':len(queue)-processed,'reused310':True,'checked_cases':case_results,'all_nonstrict':[x for x in case_results if not x['best']['strict']],'context_scope':contextout,'all_missing_gates_discovered_contexts':[{'spectrum_id':z['spectrum_id'],'survivor_index':z['survivor_index']} for z in contextout if z['all_missing_quad_gates_discovered']],'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'NEWCHECKED',processed,'FAIL',len(out['all_nonstrict']),'COMPLETE_CONTEXTS',len(out['all_missing_gates_discovered_contexts']),'CPU',out['cpu_seconds'])

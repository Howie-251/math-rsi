from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();base=json.loads((P/'COARSE_PILOT_RESULT.json').read_text());s=base['selected_profile'];mu=s['high_trace_counts'];Nh=[0]*4
for m in range(8):
 for u in range(m,8):
  Nh[(m&u).bit_count()]+=comb(mu[m],2) if m==u else mu[m]*mu[u]
assert sum(Nh)==595
Q=1+sum(s['pair_codegrees']);EH=sum(Nh[2:]);assert EH==sum(comb(c,2) for c in s['pair_codegrees'])-2*comb(s['triple'],2)
def transport_cost(n,maximum=False):
 cc=list(n);cost=0
 for h in range(3,-1,-1):
  rem=Nh[h]
  for j in (range(h,5) if maximum else range(4,h-1,-1)):
   take=min(rem,cc[j]);rem-=take;cc[j]-=take;cost+=take*comb(j-h,2)
  if rem:return None
 assert not any(cc)
 return cost
kept=[];reason={'n3_n4_pool':0,'high_overlap_distribution':0,'lowpair_cost':0}
for z in base['all_remaining']:
 n=z['n']
 if n[3]+n[4]>EH+Q:reason['n3_n4_pool']+=1;continue
 lo=transport_cost(n);hi=transport_cost(n,True)
 if lo is None or hi is None:reason['high_overlap_distribution']+=1;continue
 if not lo<=Q<=hi:reason['lowpair_cost']+=1;continue
 kept.append({**z,'low_pair_transport_min':lo,'low_pair_transport_max':hi})
r={'status':'COMPLETE_ONE_PROFILE_SHARED_POOL_NECESSARY_FILTER','scope':'Rechecks only the previously nonstrict keys; old strict keys remain strict. Same original high-overlap row totals Nh and seven-pair-repeat total Q. Exact Monge transportation extrema are safe necessary bounds, not realizability. No fresh moment/profile sweep.','selected_profile':s,'Nh_counts_exact':Nh,'Q_low_pair_repeats':Q,'high_overlap_at_least_two_pairs':EH,'original_complete_profile_keys':base['complete_moment_keys_in_selected_profile'],'input_nonstrict':len(base['all_remaining']),'rejected_by':reason,'remaining':len(kept),'maximum_twice_L':max((z['twice_L'] for z in kept),default=None),'maximum_witness':max(kept,key=lambda z:z['twice_L']) if kept else None,'first_remaining':kept[:5],'all_remaining':kept,'cpu_seconds':time.process_time()-start}
assert r['cpu_seconds']<5
(P/'COARSE_SHARED_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print({k:v for k,v in r.items() if k not in ['all_remaining','first_remaining']})

"""Exact lastsource ownblue05/35roles and newlemma scalar/endpoint cases."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
last=list(map(json.loads,(HERE.parent/'p6_tail79_common_gate_20261020/IF_MIXED8_ACCEPTED_TAIL1.jsonl').open()))
assert len(last)==1;r=last[0]
assert r['source_key']==[[6,2,0],0,[[0,1,5],[2,3,4]],[0,1,1,1,0,0,0,0,0,0,0,1,0,1,1]]
T=[31,35,28,5,9,17,36,40,48]+[1]*4+[2]*6+[4]*4+[8]*4+[16]*4+[32]*4
assert T==r['trace_masks'] and len(T)==35
assert [sum(m>>v&1 for m in T) for v in range(6)]==[9,8,8,8,8,8]
assert sum(5-m.bit_count() for m in T)==126
blue=(1<<0)|(1<<5);roles=[];cnt={'P':Counter(),'N':Counter()}
for i,m in enumerate(T):
 sign='P' if m&blue==m else ('N' if m&blue==0 else 'proper');k=5-m.bit_count()
 roles.append({'source_index':i,'trace_mask':m,'trace':[v for v in range(6) if m>>v&1],'outside_size':k,'role':sign})
 if sign!='proper':cnt[sign][k]+=1
assert dict(cnt['P'])=={4:8} and dict(cnt['N'])=={2:1,4:18}
saved=next(c for c in r['menus'] if c['blue']==[0,5]);assert saved['roles']==[[q['source_index'],q['role'],q['outside_size']] for q in roles]
assert saved['signature'][:8]==[8,0,0,0,0,1,0,18]
# Endpoint positivefreq a<=6 sinceN2 already consumes oneD7 index.
frequency_cases=[]
for af in range(7):
 for ag in range(7):
  case='low_blue_mixed8' if min(af,ag)<=2 else ('high_red_blue_foursmall' if max(af,ag)>=4 else 'three_three_fivesmall')
  assert case!='three_three_fivesmall' or (af,ag)==(3,3)
  frequency_cases.append([af,ag,case])
assert F(5,18)+F(1,9)==F(7,18)<1
# Independent alternative proof's disjoint threegroups bound scales with largest a.
# 9a-(3a+2)=6a-2>=16 for all a>=3, no boundedsize enumeration needed.
assert 6*3-2==16
# All index/source keys in the acceptedtailchain were already complete; preserve prefixcounts.
counts=[115052,8020,363,47,60,59,19,1];assert sum(counts)==123621
out={'status':'PASS','own_source_key':r['source_key'],'blue':[0,5],'roles35':roles,
 'positive_count_by_size':{str(k):cnt['P'][k] for k in range(1,5)},'negative_count_by_size':{str(k):cnt['N'][k] for k in range(1,5)},
 'signature_P4P3P2P1_N1N2N3N4':[8,0,0,0,0,1,0,18],
 'P_degrees':[9,8,8,8,8,8],'all_external_degree':7,'external_vertex_count':18,'external_occurrence_total':126,
 'actual_signedD7_binding':'P is hitting; each edge has a nonempty Ptrace. Blue05 gives each indexed edge atmostone remaining monochrome risk. Signedindices through actual exteriorvertex are a subset of its seven indexedHedges.',
 'endpoint_frequency_cases':frequency_cases,'five_disjoint_probability':str(F(7,18)),
 'historical_necessary_P_domain_chain_counts':counts,'chain_total':sum(counts),
 'scope':'ExactPsource and general signedlemma arithmetic only; no exteriorincidence/H realization fabricated.','cpu_seconds':time.process_time()-start}
(HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('roles35','endpoint_frequency_cases')})

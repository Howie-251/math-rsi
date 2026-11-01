"""Independent row-first complete15+15 clean7 lift domains and30 original35-index zero-quota replays; S4 transport of two tau8 double-singleton sources."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();pairs=(3,5,6,9,10,12);results=[];allrows=[]
for file in ('LOW_TAU_SEVEN_PILOT.json','LOW_TAU_SINGLETON_ONE.json'):
 d=json.loads((P/file).read_text());assert d['status']=='COMPLETE_ONE_SOURCE';mu=d['source_Kcounts'];high=d['source_Kdegrees'].index(11);keys=set()
 for row in product((1,2),repeat=4):
  if row[high]!=2:continue
  for a,b,c in product(range(3),repeat=3):
   cp=(a,b,c,row[0]-a-b,row[1]-a-c,row[2]-b-c)
   if min(cp)<0 or cp[3]+cp[4]+cp[5]!=row[3] or any(x>mu[m] for x,m in zip(cp,pairs)):continue
   c0=7-sum(cp)
   if 0<=c0<=mu[0]:keys.add(cp)
 assert keys=={tuple(x['cp']) for x in d['cases']} and len(keys)==15
 values=[]
 for z in d['cases']:
  ns={int(m):n for m,n in z['counts'].items()};masks=[m for m,n in sorted(ns.items()) for _ in range(n)];assert len(masks)==35
  assert sum(n for m,n in ns.items() if m&1)==7
  types=[frozenset(i+1 for i in range(5) if m>>i&1) for m in masks];rr=independent_rows(21,tuple(z['best']['positions']),types);v=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction());assert v==Fraction(z['best']['bound'])<1
  values.append(v);allrows.append({'source_file':file,'cp':z['cp'],'c0':z['c0'],'expanded35_masks':masks,'positions':z['best']['positions'],'bound':str(v),'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]})
 results.append({'source_file':file,'source_Kcounts':mu,'independent_domain':15,'original35_certificates':15,'maximum_bound':str(max(values))})
base=json.loads((P/'LOW_TAU_SEVEN_PILOT.json').read_text())['source_Kcounts'];old=json.loads((P/'RESULT.json').read_text());trans=[]
for z in old['all_nonstrict']:
 if z['legacy'] or z['quad']!=[9,10,10,11] or z['K6_tau_cost']!=8 or z['minimum_tau_selected_K']!=8:continue
 found=None
 for perm in permutations(range(4)):
  out=[0]*16
  for m,n in enumerate(z['counts']):out[sum(1<<perm[i] for i in range(4) if m>>i&1)]=n
  if out==base:found=perm;break
 assert found is not None;trans.append({'actual_Kcounts':z['counts'],'actual_to_canonical_K_permutation':found,'canonical_Kcounts':base,'transport_counts_and_positions_not_H_automorphism':True})
assert len(trans)==2
(P/'LOW_TAU_VERIFY_ROWS.json').write_text(json.dumps(allrows,indent=2)+'\n');out={'status':'PASS_COMPLETE_TWO_LOCAL_SOURCES_AND_TRANSPORTS','scope':__doc__,'Nfree':16,'original35_index_certificates':30,'rows':630,'two_source_domains':results,'double_singleton_transports':trans,'strict':30,'cpu_seconds':time.process_time()-st};(P/'LOW_TAU_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

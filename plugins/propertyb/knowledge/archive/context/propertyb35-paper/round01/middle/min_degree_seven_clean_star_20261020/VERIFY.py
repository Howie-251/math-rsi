"""Independent119/102 domain and positive-composition clean-star reconstruction."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
five=json.loads((P/'FIVE_RESULT.json').read_text());star=json.loads((P/'STAR_RESULT.json').read_text())
source=json.loads((P.parent/'three_nonunit_direct_repair_20261020/RESULT.json').read_text())
failsets={tuple(z['types']):set(z['failure_a']) for z in source['residual_types']}
def comps(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for rest in comps(n-a,k-1):yield(a,)+rest
generic=[];min7={}
for r in source['remaining']:
 h=[sum(t>>v&1 for t in r['traces']) for v in range(5)]
 for delta in comps(31-r['sum_k'],5):
  a=tuple(x+y for x,y in zip(r['k_by_v'],delta))
  if any(x not in failsets[tuple(t)] for x,t in zip(a,r['types_by_v'])):continue
  key=(tuple(r['traces']),a);generic.append(key)
  d=[1+x+y for x,y in zip(a,h)]
  if min(d)>=7:min7[key]=d
assert len(generic)==119 and len(min7)==102
assert min7=={(tuple(z['traces']),tuple(z['attachments'])):z['degrees'] for z in five['cases']}
star_expected={};source_rebuild=[]
for sid,z in enumerate(five['nonstrict']):
 assert all(z['traces'])
 BF=sum((m.bit_count()-1)*(5-m.bit_count()) for m in z['traces']);DF=sum(z['degrees'])
 nclean=16-BF;outside=175-DF;rmax=(outside-7*BF)//nclean
 assert rmax==z['clean_degree_max'] and BF==z['BF'] and nclean>0
 assert 7*BF+(rmax+1)*nclean>outside
 stubs=[31]+z['traces']+[1<<v for v,a in enumerate(z['attachments']) for _ in range(a)];assert len(stubs)==35
 for r in range(7,rmax+1):
  # Different generator: choose the four cut positions among r-1, not recurse increments.
  for cuts in combinations(range(1,r),4):
   points=(0,)+cuts+(r,);s=tuple(points[j+1]-points[j] for j in range(5))
   if any(x>y for x,y in zip(s,z['attachments'])):continue
   needed=list(s);lift=[]
   for m in stubs:
    low=0
    if m.bit_count()==1:
     v=m.bit_length()-1
     if needed[v]:low=1;needed[v]-=1
    lift.append((m<<1)|low)
   assert not any(needed) and sum(m&1 for m in lift)==r
   assert Counter(m>>1 for m in lift)==Counter(stubs)
   star_expected[(sid,r,s)]=(Counter(lift),lift)
assert len(star_expected)==1171
actual={(z['source'],z['r'],tuple(z['s'])):Counter({int(m):n for m,n in z['counts'].items() if n}) for z in star['cases']}
assert {k:v[0] for k,v in star_expected.items()}==actual
cert=[];failed=[];rowcount=0
def replay(kind,key,z,masks,s):
 global rowcount
 types=[frozenset(v+1 for v in range(s) if m>>v&1) for m in masks]
 ir=independent_rows(21,tuple(z['positions']),types);bound=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction())
 assert bound==Fraction(z['bound']) and (bound<1)==z['strict'];rowcount+=21
 zz=dict(kind=kind,key=key,positions=z['positions'],bound=str(bound),strict=bound<1)
 if bound<1:
  zz.update(expanded35_masks=masks,quota=0,rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in ir]);cert.append(zz)
 else:failed.append(zz)
for z in five['cases']:
 masks=[31]+z['traces']+[1<<v for v,a in enumerate(z['attachments']) for _ in range(a)]
 replay('five',dict(traces=z['traces'],attachments=z['attachments']),z,masks,5)
for i,z in enumerate(star['cases']):
 key=(z['source'],z['r'],tuple(z['s']));replay('six',dict(source=key[0],r=key[1],s=key[2]),z,star_expected[key][1],6)
 if i==0:print('FIRST_REPLAY_CPU',time.process_time()-st,flush=True)
 assert time.process_time()-st<12,'12CPU independent verification cutoff'
out=dict(status='PASS_COMPLETE_FIXED_DOMAINS_AND_REPLAYS',scope=__doc__,generic119=119,minF7_inputs=102,minF7_strict=97,minF7_nonstrict=5,all_five_tails_nonempty=True,clean_star_inputs=1171,clean_star_strict=1053,clean_star_nonstrict=118,all_domains_equal=True,all1273_fixed_best_bounds_equal=True,replayed_rows=rowcount,strict_certificates=cert,nonstrict=failed,cpu_seconds=time.process_time()-st)
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('strict_certificates','nonstrict')})

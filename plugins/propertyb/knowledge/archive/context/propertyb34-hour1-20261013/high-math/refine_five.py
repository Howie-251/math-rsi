from pathlib import Path
import sys,json,time
from itertools import combinations
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,json_value
from enumerate_pair_partitions import enumerate_partitions,canonical_large_blocks,exact_types
from pure_quota import certificate as pure
from avoided_lock_quotas import certificate as avoided
start=time.perf_counter(); by={}
for part in enumerate_partitions(5):
 c=canonical_large_blocks(part,5)
 counts=exact_types(part,5,degree=7,edges=34)['counts_by_mask']
 for s in range(6,16):
  pos=tuple(range(s,s+5));p=Profile(24,5,pos,counts)
  cs=[pure(p,i) for i in range(5)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(5)});b=total_bound(rs)
  if c not in by or b<by[c]['bound']:by[c]=dict(large=c,bound=b,positions=pos,counts=counts,certificates=cs)
for key,z in by.items():
 p=Profile(24,5,z['positions'],z['counts']);cs=[avoided(p,i) for i in range(5)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(5)});z['avoided_bound']=total_bound(rs);z['avoided_certificates']=cs
 print(key,z['bound'],z['avoided_bound'],flush=True)
Path(__file__).with_name('FIVE_REFINED.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=list(by.values()))),indent=2)+'\n')

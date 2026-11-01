"""Independent direct global-inclusive Mobius reconstruction of two genuine center partitions.
Literal restricted-growth partition generation; exact domain and S2xS3 transports; fixed certificate replay only.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from replay_r3 import fixed

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(32))
def main():
 start=time.time();partitions=[]
 for word in product(range(3),repeat=3):
  if word[0] or any(word[i]>max(word[:i])+1 for i in (1,2)):continue
  blocks=tuple(sum(1<<i for i,a in enumerate(word) if a==j) for j in range(max(word)+1));assert all(blocks);partitions.append(blocks)
 assert len(partitions)==5
 inc=lambda P,A:int(any(B&A==A for B in P));expected=set()
 for P1,P2 in product(partitions,repeat=2):
  for c12,c13,c23 in product(range(1,5),repeat=3):
   for tt in range(min(c12,c13,c23)+1):
    high={1:10,2:10,4:10,3:c12,5:c13,6:c23,7:tt};I={}
    for t in range(1,32):
     low=t&3;A=t>>2
     if low==0:I[t]=high[A]
     elif low==1:I[t]=7 if A==0 else inc(P1,A)
     elif low==2:I[t]=7 if A==0 else inc(P2,A)
     else:I[t]=1 if A==0 else 0
    ns={t:sum((-1)**(u.bit_count()-t.bit_count())*v for u,v in I.items() if u&t==t) for t in range(1,32)};ns[0]=35-sum(ns.values())
    if min(ns.values())>=0:expected.add(key(ns))
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert len(expected)==2533 and expected=={key(r['counts']) for r in dom['labelled']}
 for r in dom['labelled']:
  ns={int(t):v for t,v in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_high_permutation'];swap=r['from_representative_low_swap']
  def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(p[i]+2) for i in range(3) if t>>(i+2)&1)
  assert key({move(t):v for t,v in ns.items()})==key(r['counts'])
 dp=json.loads((HERE/'DP.json').read_text());assert dp['complete'] and len(dp['cases'])==358
 vals=[]
 for r in dp['cases']:
  assert sum(r['counts'].values())==35
  assert [sum(v for t,v in r['counts'].items() if int(t)>>i&1) for i in range(5)]==[7,7,10,10,10]
  val=fixed(r);assert val==Q(r['bound'])<1;vals.append(val)
 diagnosis=json.loads((HERE.parents[1]/'DIAGNOSIS.json').read_text())['pairs'];strong=[]
 for r in diagnosis:
  if r['degrees']==[10,10] and r['codegree']>=5:assert fixed(r)<1;strong.append(r['codegree'])
 assert strong==list(range(5,11))
 result=dict(status='PASS',scope=__doc__,partitions_per_center=5,high_pair_domain=[1,2,3,4],strong_10_10_exclusions=strong,labelled_count=2533,orbit_count=358,transport_checks=2533,all_fixed_strict=True,max_bound=str(max(vals)),max_id=vals.index(max(vals)),elapsed_seconds=time.time()-start)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

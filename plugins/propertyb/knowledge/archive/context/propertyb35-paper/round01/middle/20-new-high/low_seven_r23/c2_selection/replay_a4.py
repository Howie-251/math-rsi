"""Independent all-partitions/full-inclusive Mobius A>=4 domain, true transports and fixed/dual replay.
No DP, optimizer, or matching generator is called.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from replay_r3 import fixed,joint

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(64))
def main():
 start=time.time();Ps=[]
 for word in product(range(4),repeat=4):
  if word[0] or any(word[i]>max(word[:i])+1 for i in range(1,4)):continue
  Ps.append(tuple(sum(1<<i for i,x in enumerate(word) if x==j) for j in range(max(word)+1)))
 assert len(Ps)==15
 pairs=[sum(1<<i for i in S) for S in combinations(range(4),2)];trips=[sum(1<<i for i in S) for S in combinations(range(4),3)];inc=lambda P,A:int(any(B&A==A for B in P));expected=set();partpairs=0
 for P1,P2 in product(Ps,repeat=2):
  e1={e for e in pairs if inc(P1,e)};e2={e for e in pairs if inc(P2,e)}
  if e1&e2:continue
  edges=e1|e2
  if any(sum(e>>i&1 for e in edges)>1 for i in range(4)):continue
  partpairs+=1
  ranges=[(0,) if any(T&e==e for e in edges) else (0,1) for T in trips]
  for ts in product(*ranges):
   for quad in range(min(ts)+1):
    high={1<<i:8 for i in range(4)};high.update({e:2 for e in pairs});high.update(dict(zip(trips,ts)));high[15]=quad;I={}
    for t in range(1,64):
     lo=t&3;A=t>>2
     if not lo:I[t]=high[A]
     elif lo==1:I[t]=7 if not A else inc(P1,A)
     elif lo==2:I[t]=7 if not A else inc(P2,A)
     else:I[t]=2 if not A else 0
    ns={t:sum((-1)**(u.bit_count()-t.bit_count())*v for u,v in I.items() if u&t==t) for t in range(1,64)};ns[0]=35-sum(ns.values())
    if min(ns.values())>=0:expected.add(key(ns))
 assert partpairs==25
 dom=json.loads((HERE/'A4_DOMAIN.json').read_text());assert len(expected)==77 and expected=={key(r['counts']) for r in dom['labelled']}
 for r in dom['labelled']:
  ns={int(t):v for t,v in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_high_permutation'];swap=r['from_representative_low_swap']
  def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(p[i]+2) for i in range(4) if t>>(i+2)&1)
  assert key({move(t):v for t,v in ns.items()})==key(r['counts'])
 dp=json.loads((HERE/'A4_DP.json').read_text());assert dp['complete'] and len(dp['cases'])==11;values={r['id']:fixed(r) for r in dp['cases']};pure=sum(v<1 for v in values.values());jointcount=0
 for z in json.loads((HERE/'A4_JOINT.json').read_text())['results']:
  verified=joint.verify(z,v=20,s=6,expected_degrees=[7,7,8,8,8,8]);values[z['source_id']]=Q(verified['bound']);jointcount+=1
 assert all(v<1 for v in values.values())
 out=dict(status='PASS',scope=__doc__,RGS_partitions=15,genuine_partition_pairs=25,labelled_count=77,orbit_count=11,transports=77,fixed_strict=pure,joint_strict=jointcount,all_strict=True,max_final_bound=str(max(values.values())),max_final_id=max(values,key=values.get),elapsed_seconds=time.time()-start)
 (HERE/'A4_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

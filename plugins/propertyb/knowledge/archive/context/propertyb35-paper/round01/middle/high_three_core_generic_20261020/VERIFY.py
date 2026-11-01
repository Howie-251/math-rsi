"""Second triple/h-domain representations and fixed35-index replay; never imports DP/PILOT."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def partitions(xs):
 if not xs:yield [];return
 x=xs[0]
 for pp in partitions(xs[1:]):
  yield [[x]]+pp
  for j in range(len(pp)):yield pp[:j]+[[x]+pp[j]]+pp[j+1:]

def replay(r):
 ns={int(t):n for t,n in r['counts'].items()};s=len(r['degrees']);pos=r['positions']
 stubs=[frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
 assert len(stubs)==35
 p=Profile(21,5,pos,ns);cs=[certificate(p,i) for i in range(s)]
 rr=independent_rows(21,pos,stubs)
 value=F(0)
 for k,row in enumerate(rr,1):
  loss=cs[pos.index(k)]['loss'] if k in pos else F(0)
  assert row['C']-loss>=0
  value+=min(row['A'],row['B'],row['C']-loss)
 assert value==F(r['bound'])
 assert (value<1)==r['strict']
 return value

def main():
 st=time.process_time();a=json.loads((HERE/'PILOT.json').read_text());b=json.loads((HERE/'EXTENDED.json').read_text())
 # Independent precise-trace coordinates: q + three residual exact-pair slots.
 domains=set()
 for q in range(2,5):
  for pp in product(range(5-q),repeat=3):
   ns={7:q,3:pp[0],5:pp[1],6:pp[2]}
   for i in range(3):ns[1<<i]=8-sum(v for t,v in ns.items() if t>>i&1)
   ns[0]=35-sum(ns.values())
   if min(ns.values())>=0:domains.add(tuple(ns.get(t,0) for t in range(8)))
 saved={tuple(r['counts'].get(str(t),0) for t in range(8)) for r in a['cases']}
 assert domains==saved and len(domains)==36
 expected=set()
 for sid in a['nonstrict_ids']:
  ns={int(t):n for t,n in a['cases'][sid]['counts'].items()}
  for margin in product((1,2),repeat=3):
   xs=[i for i,m in enumerate(margin) for _ in range(m)]
   for pp in partitions(xs):
    if len(pp)>6 or any(len(v)!=len(set(v)) for v in pp):continue
    hh=[0]*8;hh[0]=6-len(pp)
    for block in pp:hh[sum(1<<i for i in block)]+=1
    if any(hh[t]>ns.get(t,0) for t in range(8)):continue
    expected.add((sid,tuple(margin),tuple(hh)))
 found={(r['parameters']['source_id'],tuple(r['parameters']['x_margins']),tuple(r['parameters']['h'])) for r in b['cases']}
 assert b['complete'] and expected==found and len(found)==len(b['cases'])==298
 vals=[replay(r) for r in a['cases']+a['low_xBB_cases']+b['cases']]
 bad=[r for r in b['cases'] if not r['strict']]
 assert len(bad)==19
 shapes=sorted({(tuple(sorted(a['cases'][r['parameters']['source_id']]['parameters']['pairs'])),a['cases'][r['parameters']['source_id']]['parameters']['triple']) for r in bad})
 assert shapes==[((2,2,2),2),((2,2,3),2)]
 out=dict(status='PASS',complete_three_lock_keys=36,complete_actual_star_keys=298,
          direct_three_lock_strict=27,four_lock_strict=279,four_lock_nonstrict=19,
          fixed_original35_profiles=len(vals),independent_rows=21*len(vals),
          remaining_shapes=shapes,max_direct=str(max(map(F,[r['bound'] for r in a['cases']]))),
          max_extended=str(max(map(F,[r['bound'] for r in b['cases']]))),
          CPU_seconds=time.process_time()-st)
 (HERE/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()

"""Independent saved-certificate replay and actual-profile binding for root's new 23-point branches."""
from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from verify_joint_layout import verify

def main():
 start=perf_counter();names=[f'FEW_LOW23_{low}_{h}.json' for low,hs in [(1,range(2,6)),(2,range(1,6))] for h in hs]
 names+=['MIXED_LOW_23_4.json','TWO_HIGH_23_4.json','MORE_HIGH_23_4_3.json','FIFTH_LOW_23.json']
 summaries=[];pure=joint=0
 for name in names:
  d=json.loads((HERE/name).read_text());assert d['complete'];nstrict=0;nres=0;mx=Q(0)
  for w in d['results']:
   ns={int(t):n for t,n in w['counts'].items()};ds=w['degrees'];s=len(ds)
   assert sum(ns.values())==34 and all(n>=0 and t.bit_count()<=5 for t,n in ns.items())
   assert all(sum(n for t,n in ns.items() if t&(1<<i))==ds[i] for i in range(s))
   lam=lambda i,j:sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))
   assert all(lam(i,j)>=1 for i in range(s) for j in range(i))
   assert all(sum(lam(i,j)-1 for j in range(s) if i!=j)<=4*ds[i]-22 for i in range(s))
   if Q(w['final_bound'])>=1:nres+=1;continue
   if 'joint' in w:
    assert {int(t):n for t,n in w['joint']['counts'].items()}==ns
    z=verify(w['joint'],23,s,ds);b=Q(z['bound']);joint+=1
   else:
    z=SubsetEngine(23,s,ns).verify(dict(positions=w['positions'],bound=Q(w['bound']),counts=ns));b=z['bound'];pure+=1
   assert b==Q(w['final_bound']) and b<1;nstrict+=1;mx=max(mx,b)
  summaries.append(dict(source=name,profiles=len(d['results']),strict=nstrict,residuals=nres,max_strict_bound=str(mx),all_actual_bindings=True,all_saved_strict_certificates_replayed=True))
  print(name,nstrict,'strict',nres,'residuals',flush=True)
 out=dict(scope=__doc__,all_sources_complete=True,pure_checks=pure,joint_checks=joint,coverage_scope='Probability replay and binding; mathematical catalogue coverage is by complete promotion/projection in the proof, not a second generator implementation.',sources=summaries,elapsed_seconds=perf_counter()-start)
 (HERE/'NEW23_CERTIFICATES_VERIFIED.json').write_text(json.dumps(out,indent=2)+'\n');print('total',pure,joint,'seconds',perf_counter()-start,flush=True)
if __name__=='__main__':main()

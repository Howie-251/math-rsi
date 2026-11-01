"""Independent injection and exact rational dual checks for new low-lock tables."""
from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from verify_joint_layout import verify

def main(name):
 start=perf_counter();d=json.loads((HERE/name).read_text());v=d['v'];s=4 if name.startswith('FOUR') else int(Path(name).stem.split('_')[-1]);out=[]
 for w in d['results']:
  if Q(w['final_bound'])>=1:continue
  ns={int(t):n for t,n in w['counts'].items()}
  assert sum(ns.values())==34 and all(t.bit_count()<=5 for t in ns)
  assert all(sum(n for t,n in ns.items() if t&(1<<i))==6 for i in range(s))
  if 'overlap' in w or 'joint' in w:
   z=w.get('overlap',w.get('joint'));assert {int(t):n for t,n in z['counts'].items()}==ns
   r=verify(z,v,s,[6]*s);r['method']='exact_shared_vector_dual'
  else:
   z=dict(bound=Q(w['bound']),positions=w['positions'],counts=ns);r=SubsetEngine(v,s,ns).verify(z)
   r=dict(group=w['group'],bound=str(r['bound']),method='independent_ABC_nested_quota')
  assert Q(r['bound'])==Q(w['final_bound']);out.append(r)
 (HERE/(Path(name).stem+'_VERIFIED.json')).write_text(json.dumps(dict(source=name,strict_count=len(out),complete_strict_replay=len(out)==sum(Q(w['final_bound'])<1 for w in d['results']),max_bound=str(max((Q(r['bound']) for r in out),default=Q())),results=out,elapsed_seconds=perf_counter()-start),indent=2)+'\n')
 print(name,'strict',len(out),'max',max((Q(r['bound']) for r in out),default=Q()),'seconds',perf_counter()-start)
if __name__=='__main__':
 for name in sys.argv[1:]:main(name)

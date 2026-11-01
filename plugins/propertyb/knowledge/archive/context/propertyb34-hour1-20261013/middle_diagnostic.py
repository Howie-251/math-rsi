"""T34 middle-vertex exact profile diagnostics; no selection/completeness claim."""
import sys, json, time
from pathlib import Path
from itertools import combinations
ROOT=Path(__file__).resolve().parents[2]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows

def evaluate(v,ds,lam):
    dx,dy=ds
    counts={0:34-dx-dy+lam,1:dx-lam,2:dy-lam,3:lam}
    opts=[]
    for pos in combinations(range(1,v+1),2):
        p=Profile(v,5,pos,counts)
        cs=[certificate(p,i) for i in range(2)]
        rr=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(2)})
        opts.append(dict(v=v,degrees=ds,codegree=lam,positions=pos,counts=counts,
                         bound=total_bound(rr),rows=rr,certificates=cs))
    best=min(opts,key=lambda x:x['bound'])
    stubs=[frozenset(i+1 for i in range(2) if t&(1<<i)) for t,n in counts.items() for _ in range(n)]
    other=independent_rows(v,best['positions'],stubs)
    for a,b in zip(best['rows'],other):
        assert all(a[k]==b[k] for k in ['A','B','C'])
        assert a['bound']==min(b['A'],b['B'],b['C']-a['deduction'])
    best['independent_ABC_agree']=True
    best['all_increasing_positions']=len(opts)
    return best

if __name__=='__main__':
    start=time.perf_counter();cases=[]
    for v in (22,23):
        for ds in [(6,6),(6,7),(6,8),(7,7)]:
            for lam in range(1,min(ds)+1):
                best=evaluate(v,ds,lam);cases.append(best)
                print(v,ds,lam,best['positions'],best['bound'],flush=True)
    Path(__file__).with_name('MIDDLE_DOUBLE_RESULTS.json').write_text(json.dumps(json_value(dict(
        scope='All two-lock increasing placements; pure/total quotas; supplied profiles only, actual selection not asserted.',
        elapsed_seconds=time.perf_counter()-start,cases=cases)),indent=2)+'\n')

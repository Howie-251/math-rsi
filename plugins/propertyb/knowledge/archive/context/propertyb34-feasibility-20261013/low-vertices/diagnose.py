"""Exact bounded T34 low-vertex diagnostics. No hypergraph search or proof claim."""
from pathlib import Path
import sys, json, time
from fractions import Fraction
from itertools import combinations

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'computations'))
sys.path.insert(0, str(ROOT / 'computations/propertyb33/round01'))
from multilock import Profile, rows, total_bound, link_certificate, link_q_lower, json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows


def one(v, m, degrees, positions, quota):
    if len(degrees) == 1:
        counts = {0: m-degrees[0], 1: degrees[0]}
    else:
        dx, dy = degrees
        counts = {0: m+1-dx-dy, 1: dx-1, 2: dy-1, 3: 1}
    p = Profile(v, 5, positions, counts)
    cs = [certificate(p, i) if quota == 'nested_pure' else
          dict(loss=link_certificate(p, i, link_q_lower(v, 5, d))['deduction'])
          for i, d in enumerate(degrees)]
    rs = rows(p, deductions={positions[i]: c['loss'] for i,c in enumerate(cs)})
    return dict(v=v, m=m, degrees=degrees, positions=positions, counts=counts,
                quota=quota, certificates=cs, rows=rs, bound=total_bound(rs))


def check_independent(case):
    stubs = [frozenset(i+1 for i in range(len(case['positions'])) if t & (1 << i))
             for t,n in case['counts'].items() for _ in range(n)]
    own = independent_rows(case['v'], case['positions'], stubs)
    for a,b in zip(case['rows'], own):
        for term in ('A','B','C'):
            assert a[term] == b[term]
        assert a['bound'] == min(b['A'], b['B'], b['C']-a['deduction'])
    case['independent_endpoint_and_pair_rows_agree'] = True


def main():
    start=time.perf_counter(); out=[]
    for v in (19,20):
      for m in (33,34):
        for dx in range(5,9):
          positions = [(k,) for k in range(v//2-2, v//2+4)]
          options = [one(v,m,(dx,),p,'nested_pure') for p in positions]
          best=min(options,key=lambda x:x['bound']); check_independent(best)
          best['tested_positions']=positions; best['kind']='single'
          out.append(best)
          print(v,m,(dx,),best['positions'],best['bound'],flush=True)
          size=2*(v-1)-4*dx
          dymax=dx+(5*m-v*dx)//size
          for dy in range(dx,dymax+1):
            positions=[(k,k+1) for k in range(v//2-2,v//2+3)]
            options=[one(v,m,(dx,dy),p,'nested_pure') for p in positions]
            best=min(options,key=lambda x:x['bound'])
            # When cheap central windows fail, fully diagnose positions for
            # this particular two-lock profile, not a domain of hypergraphs.
            scope='five_contiguous_central_windows'
            if best['bound'] >= 1:
              positions=list(combinations(range(1,v+1),2))
              options=[one(v,m,(dx,dy),p,'nested_pure') for p in positions]
              best=min(options,key=lambda x:x['bound']);scope='all_increasing_positions'
            check_independent(best)
            best['tested_position_count']=len(positions);best['position_scope']=scope
            best['kind']='unit_double';best['unit_partner_upper']=dymax
            best['center_total_only_bound_at_same_positions']=one(v,m,(dx,dy),best['positions'],'total')['bound']
            out.append(best)
            print(v,m,(dx,dy),best['positions'],best['bound'],scope,flush=True)
    result=dict(scope='Exact rational formula diagnostics. Unit-pair coverage comes from degree/total-incidence argument; no T34 Lean result.', elapsed_seconds=time.perf_counter()-start,cases=out)
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
    print('elapsed',result['elapsed_seconds'])

if __name__=='__main__':main()

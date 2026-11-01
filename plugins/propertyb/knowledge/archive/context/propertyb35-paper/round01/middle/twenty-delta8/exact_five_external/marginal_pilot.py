"""All fifteen actual degree9 points share the five exact cross-codegree marginals.
Necessary pattern relaxation only, not a hypergraph enumeration or positive existence claim.
"""
from pathlib import Path
from itertools import product,combinations
import json,time,sys
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;start=time.time();rs=json.loads((HERE.parent/'five_join/FIVE_REMAINDERS.json').read_text())['cases'];g=json.loads((HERE/'mixed_triples/GENERAL_GATE.json').read_text())['cases'];allowed={(r['codegrees'][0],*sorted(r['codegrees'][1:])) for r in g if not r['strict']};out=[]
for r in rs:
 ns={int(t):n for t,n in r['counts'].items()};cs={(i,j):sum(n for t,n in ns.items() if t>>i&1 and t>>j&1) for i,j in combinations(range(5),2)};marg=[32-sum(c for ij,c in cs.items() if i in ij) for i in range(5)]
 patterns=[p for p in product((1,2,3),repeat=5) if all((c,*sorted((p[i],p[j]))) in allowed for (i,j),c in cs.items())]
 A=np.array([(1,*p) for p in patterns],dtype=float).T;b=np.array([15,*marg],dtype=float)
 z=linprog(np.zeros(len(patterns)),A_eq=A,b_eq=b,bounds=(0,None),method='highs') if patterns else None
 out.append(dict(core_id=r['id'],counts=r['counts'],pair_codegrees={str(ij):c for ij,c in cs.items()},external_cross_marginals=marg,allowed_patterns=patterns,pattern_count=len(patterns),lp_feasible=bool(z is not None and z.success),lp_status=None if z is None else z.message,lp_weights=None if z is None or not z.success else z.x.tolist()))
 print(r['id'],'patterns',len(patterns),'feasible',out[-1]['lp_feasible'],flush=True)
result=dict(scope=__doc__,complete=True,core_count=len(out),infeasible_relaxations=sum(not r['lp_feasible'] for r in out),cases=out,elapsed_seconds=time.time()-start);(HERE/'MARGINAL_PILOT.json').write_text(json.dumps(result,indent=2)+'\n');print('infeasible',result['infeasible_relaxations'],'of',len(out),'seconds',time.time()-start)

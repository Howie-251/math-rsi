"""Second replay with the original binomial probability implementation."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import importlib.util,json,time
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('submitted_component_kernel',HERE.parent/'small31_33/diagnose.py')
x=importlib.util.module_from_spec(spec);spec.loader.exec_module(x)
c=x.c

def delete(v,pos,ell,j):
    typ=[t for t,n in ell.items() if n and t>>j&1];cells=[]
    for i,t in enumerate(typ):
        for u in typ[i:]:
            cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
            if cap:cells.append((c.weight(v,pos,pos[j],t,u)+c.weight(v,pos,pos[j],u,t),cap,t|u))
    costs=[]
    for R in range(1<<len(pos)):
        if R>>j&1:continue
        f=sum(n for t,n in ell.items() if t>>j&1 and not t&R)
        need=x.quota(v-R.bit_count(),f);cost=Q(0)
        for w,cap,union in sorted(cells):
            if not union&R:
                take=min(need,cap);cost+=take*w;need-=take
        assert need==0
        costs.append(cost)
    return max(costs)
c.bad_pair_deletion=delete
start=time.process_time();data=json.loads((HERE/'CERTIFICATE.json').read_text());rows=[]
for r in data['rows']:
    ell={int(t):n for t,n in r['ell'].items()}
    value=c.profile_bound(34,tuple(r['positions']),ell)
    assert value==Q(r['U'])<1
    rows.append(dict(kind=r['kind'],tau=r.get('tau'),U=str(value),exact_match=True))
for q in data['quotas']:
    assert x.quota(q['N']+1,q['f'])==q['q']
result=dict(status='PASS',profiles=len(rows),quota_entries=len(data['quotas']),method='Original binomial probability kernel plus submitted component DP, compared with independent injection/component-knapsack certificate',cpu_seconds=time.process_time()-start,rows=rows)
(HERE/'REPLAY_ORIGINAL.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

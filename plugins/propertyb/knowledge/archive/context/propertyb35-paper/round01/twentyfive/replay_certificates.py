"""Replay strict chosen rows with the binomial ordered-type-pair implementation.
Also compare numeric unit catalogues to parameter-free Lean data definitions.
This is an independent arithmetic formula, not an independent catalogue enumeration.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import ast,sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(R/'computations')]
from multilock import Profile,rows,total_bound,pair_weight
st=time.perf_counter()

def compare_data(n):
    text=(R/f'formal/Aris4Math/ThirtyFour/TwentyFiveUnit{n}Data.lean').read_text()
    literal=text.split('def catalogue',1)[1].split(':= ![',1)[1].split(']',1)[0]
    data=ast.literal_eval('['+literal.replace('∅','[]').replace('{','[').replace('}',']')+']')
    masks=[sorted(sum(1<<i for i in b) for b in family) for family in data]
    numeric=json.loads((S/f'UNIT_CATALOGUE_{n}.json').read_text())['orbits']
    assert masks==numeric
    return dict(n=n,entries=len(data),all_entries_equal=True,parameter_free_cover=f'TwentyFiveUnit{n}Actual.actual')

def loss(p,i):
    bit=1<<i;ts=sorted(t for t in p.counts if t&bit)
    d=sum(p.counts[t] for t in ts);assert d==7
    total=(4*d-24+2)//3
    pure=max(0,(4*p.counts.get(bit,0)-(25-len(p.positions))+2)//3)
    inv=[]
    for j,t in enumerate(ts):
      for u in ts[j:]:
        cap=comb(p.counts[t],2) if t==u else p.counts[t]*p.counts[u]
        if cap:
          w=pair_weight(25,5,p.positions,t,u,p.positions[i])+pair_weight(25,5,p.positions,u,t,p.positions[i])
          inv.append([w,cap,t==u==bit])
    left=pure;ded=Q()
    for row in sorted(inv):
      if row[2]:
        k=min(left,row[1]);left-=k;row[1]-=k;ded+=k*row[0]
    assert left==0
    left=max(total-pure,0)
    for row in sorted(inv):
      k=min(left,row[1]);left-=k;ded+=k*row[0]
    assert left==0
    return ded

checks=[]
for fn in ('UNIT9_SCREEN.json','UNIT8_SCREEN.json','UNIT7_SCREEN.json','A8_EXTENSION.json'):
    src=json.loads((P/fn).read_text());rs=src['results'];count=0;maximum=Q()
    for row in rs:
        if not row.get('feasible',True) or Q(row['bound'])>=1:continue
        ns={int(t):c for t,c in row['counts'].items() if c}
        assert sum(ns.values())==35
        p=Profile(25,5,row['positions'],ns)
        for i in range(len(p.positions)):
          for j in range(i):
            co=sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)
            assert co in (1,2)
        dd={p.positions[i]:loss(p,i) for i in range(len(p.positions))}
        assert dd=={int(k):Q(v) for k,v in row['losses'].items()}
        rr=rows(p,deductions=dd)
        v=total_bound(rr)
        assert v==Q(row['bound']) and v<1
        maximum=max(v,maximum);count+=1
    checks.append(dict(file=fn,strict_witnesses=count,maximum=str(maximum),all_binomial_rows_equal=True))
out=dict(scope=__doc__,catalogue_data_comparisons=[compare_data(n) for n in (7,8,9)],checks=checks,elapsed_seconds=time.perf_counter()-st)
(P/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

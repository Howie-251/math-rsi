"""Independent labelled-injection and exact repaired-dual replay, no scipy."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability

def weight(v,pos,t,u,i):
 bit=1<<i;k=pos[i];left=sum(1<<j for j,p in enumerate(pos) if p<k);right=sum(1<<j for j,p in enumerate(pos) if p>k)
 if t&u!=bit or (t^bit)&~left or (u^bit)&~right:return Q()
 return injection_probability(v-len(pos),k-1-left.bit_count(),v-k-right.bit_count(),5-t.bit_count(),5-u.bit_count(),False)

def check_profile(ns,s,v,ds):
 assert sum(ns.values())==34 and all(t.bit_count()<=5 and n>=0 for t,n in ns.items())
 assert all(sum(n for t,n in ns.items() if t&(1<<i))==ds[i] for i in range(s))
 return [frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in ns.items() for _ in range(n)]

def verify(x,v,ds):
 s=len(ds);ns={int(t):n for t,n in x['counts'].items()};stubs=check_profile(ns,s,v,ds);slots=x['slots'];expected=[]
 for i in range(s):
  for t,u in combinations_with_replacement(sorted(t for t in ns if t&(1<<i)),2):
   cap=ns[t]*(ns[t]-1)//2 if t==u else ns[t]*ns[u]
   if cap:expected.append(dict(center=i,t=t,u=u,capacity=cap))
 assert expected==slots
 quota=Q();demand=[Q() for _ in slots]
 for q in x['quotas']:
  i,R=q['center'],q['avoid'];delta=Q(q['delta']);assert delta>=0 and not R&(1<<i)
  n=sum(c for t,c in ns.items() if t&(1<<i) and not t&R)
  bound=max(0,(4*n-(v-1-R.bit_count())+2)//3)
  ids=[j for j,z in enumerate(slots) if z['center']==i and not (z['t']|z['u'])&R]
  assert n==q['edge_count'] and bound==q['q'] and ids==q['slots']
  quota+=delta*bound
  for j in ids:demand[j]+=delta
 mass=Q();free=Q();linear=Q();ws=[Q() for _ in slots]
 for z in x['layouts']:
  g=Q(z['probability']);assert g>0;mass+=g;pos=z['positions']
  assert len(set(pos))==s and all(1<=p<=v for p in pos)
  rs=independent_rows(v,pos,stubs)
  f=sum((r['bound'] for r in rs if r['k'] not in pos),Q());assert f==Q(z['free'],x['scale']);free+=g*f
  for i,(c,beta0) in enumerate(zip(z['centers'],z['betas'])):
   beta=Q(beta0);assert 0<=beta<=g
   row=rs[pos[i]-1];a=min(row['A'],row['B']);cval=row['C']
   assert a==Q(c['a'],x['scale']) and cval==Q(c['c'],x['scale'])
   linear+=(g-beta)*a+beta*cval
   weights=[]
   for j,slot in enumerate(slots):
    if slot['center']!=i:continue
    t,u=slot['t'],slot['u'];w=weight(v,pos,t,u,i)+weight(v,pos,u,t,i)
    weights.append(w);ws[j]+=beta*w
   assert weights==[Q(w,x['scale']) for w in c['weights']]
 assert mass==1
 penalties=[max(Q(),d-w) for d,w in zip(demand,ws)]
 assert penalties==[Q(z) for z in x['penalties']]
 penalty=sum((a*z['capacity'] for a,z in zip(penalties,slots)),Q())
 bound=free+linear-quota+penalty
 assert (free,linear,quota,penalty)==tuple(Q(x[k]) for k in ['free_average','linear_part','quota_part','capacity_penalty'])
 assert bound==Q(x['bound'])<1
 return dict(graph=x['graph'],group=x['group'],bound=str(bound),layouts=len(x['layouts']),independent_ABC_weights=True,quota_capacity_and_dual=True)


if __name__=='__main__':
 source=Path(sys.argv[1]);data=json.loads(source.read_text());original=json.loads(Path(data['source']).read_text());start=perf_counter();out=[]
 assert data['complete']
 for x in data['results']:
  r=original['cases'][x['graph']]
  assert {int(t):n for t,n in r['counts'].items()}=={int(t):n for t,n in x['counts'].items()}
  z=verify(x,r['v'],r['ds']);out.append(z);print(z,flush=True)
 target=source.with_name(source.stem+'_VERIFIED.json');target.write_text(json.dumps(dict(source=str(source),count=len(out),seconds=perf_counter()-start,results=out),indent=2)+'\n')

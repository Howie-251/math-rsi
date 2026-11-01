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

def check_profile(ns,s,v,expected_degrees=None):
 assert sum(ns.values())==34 and all(t.bit_count()<=5 and n>0 for t,n in ns.items())
 ds=expected_degrees if expected_degrees is not None else [7]*s
 assert len(ds)==s and all(sum(n for t,n in ns.items() if t&(1<<i))==ds[i] for i in range(s))
 return [frozenset(i+1 for i in range(s) if t&(1<<i)) for t,n in ns.items() for _ in range(n)]

def verify(x,v=22,s=6,expected_degrees=None):
 ns={int(t):n for t,n in x['counts'].items()};stubs=check_profile(ns,s,v,expected_degrees);slots=x['slots'];expected=[]
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
  ids=[j for j,z in enumerate(slots) if z['center']==i and not (z['t']|z['u'])&R];coeffs=[1]*len(ids)
  if q.get('kind')=='overlap':
   bound=max(0,4*n-(v-1-R.bit_count()))
   pairs=[(j,min(3,(slots[j]['t']&slots[j]['u']).bit_count()-1+min(5-slots[j]['t'].bit_count(),5-slots[j]['u'].bit_count()))) for j in ids]
   ids=[j for j,h in pairs if h];coeffs=[h for j,h in pairs if h]
   assert coeffs==q['coefficients']
  else:assert q.get('kind') is None and 'coefficients' not in q
  assert n==q['edge_count'] and bound==q['q'] and ids==q['slots']
  quota+=delta*bound
  for j,h in zip(ids,coeffs):demand[j]+=delta*h
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

def verify_avoided(x):
 v,s=22,6;ns={int(t):n for t,n in x['counts'].items()};stubs=check_profile(ns,s,v);pos=x['positions'];rs=independent_rows(v,pos,stubs);losses={}
 for i,c in enumerate(x['certificates']):
  main=Q();penalty=Q()
  for d in c['dual']:
   R=d['avoid'];alpha=Q(d['alpha']);assert alpha>=0 and not R&(1<<i)
   n=sum(c for t,c in ns.items() if t&(1<<i) and not t&R)
   q=max(0,(4*n-(v-1-R.bit_count())+2)//3)
   assert n==d['edge_count'] and q==d['q'];main+=alpha*q
  for t,u in combinations_with_replacement(sorted(t for t in ns if t&(1<<i)),2):
   cap=ns[t]*(ns[t]-1)//2 if t==u else ns[t]*ns[u]
   if not cap:continue
   w=weight(v,pos,t,u,i)+weight(v,pos,u,t,i)
   demand=sum((Q(d['alpha']) for d in c['dual'] if not (t|u)&d['avoid']),Q())
   penalty+=cap*max(Q(),demand-w)
  loss=max(Q(),main-penalty);assert loss==Q(c['loss']);losses[pos[i]]=loss
 bound=sum((min(r['A'],r['B'],r['C']-losses.get(r['k'],Q())) for r in rs),Q())
 assert bound==Q(x['bound'])<1
 return dict(graph=x['graph'],group=x['group'],bound=str(bound),independent_ABC_weights=True,quota_capacity_and_dual=True)

if __name__=='__main__':
 start=perf_counter();out=[]
 source=json.loads((ROOT/'context/propertyb34-hour1-20261013/MIDDLE_SIX_RESIDUE_RESULTS.json').read_text())
 originals={(g['graph'],w['group']):{int(t):n for t,n in w['counts'].items()} for g in source['results'] for w in g['witnesses'] if Q(w['bound'])>=1}
 for x in json.loads((HERE/'JOINT_LAYOUT_CERTIFICATES.json').read_text())['results']:
  assert {int(t):n for t,n in x['counts'].items()}==originals[x['graph'],x['group']]
  z=verify(x);out.append(z);print(z,flush=True)
 for x in json.loads((HERE/'AVOIDED_THIRTEEN.json').read_text())['results']:
  if Q(x['bound'])<1:
   assert {int(t):n for t,n in x['counts'].items()}==originals[x['graph'],x['group']]
   z=verify_avoided(x);out.append(z);print(z,flush=True)
 assert len(out)==13 and len({(x['graph'],x['group']) for x in out})==13
 assert set(originals)=={(x['graph'],x['group']) for x in out}
 (HERE/'THIRTEEN_INDEPENDENT.json').write_text(json.dumps(dict(scope=__doc__,all13_strict=True,exact_source_profile_binding=True,elapsed_seconds=perf_counter()-start,results=out),indent=2)+'\n')

"""Shared actual bad-count vector across layouts; exact repaired dual witness.
LP is proposal only. The exact bound uses gamma>=0 sum=1, 0<=beta<=gamma,
alpha=gamma-beta, avoided-quota deltas>=0, and explicit capacity penalties.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from math import comb
from time import perf_counter
import sys,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from multilock import json_value
from fast_position_dp import Engine

def inventory(ns,s,v):
 slots=[];quotas=[];bycenter=[]
 for i in range(s):
  ts=sorted(t for t in ns if t&(1<<i));ids=[]
  for h,t in enumerate(ts):
   for u in ts[h:]:
    cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
    if cap:ids.append(len(slots));slots.append(dict(center=i,t=t,u=u,capacity=cap))
  bycenter.append(ids)
  for R in range(1<<s):
   if R&(1<<i):continue
   n=sum(ns[t] for t in ts if not t&R)
   q=max(0,(4*n-(v-1-R.bit_count())+2)//3)
   if q:quotas.append(dict(center=i,avoid=R,edge_count=n,q=q,slots=[j for j in ids if not (slots[j]['t']|slots[j]['u'])&R]))
 return slots,quotas,bycenter

def layout(eng,ns,slots,bycenter,pos,perm):
 s=eng.s;move=lambda t:sum(1<<perm[i] for i in range(s) if t&(1<<i))
 mapped={t:move(t) for t in ns};cs={mapped[t]:n for t,n in ns.items()};free=0;centers=[None]*s
 for k in range(1,eng.v+1):
  j=sum(p<k for p in pos);pivot=k in pos;aa,bb,cc=eng.states[k,j,pivot]
  A=sum(n*aa[t] for t,n in cs.items());B=sum(n*bb[t] for t,n in cs.items())
  C=sum(cs.get(t,0)*(cs.get(u,0)-int(t==u))*w for (t,u),w in cc.items())
  if not pivot:free+=min(A,B,C);continue
  i=perm.index(j);weights=[]
  for sid in bycenter[i]:
   z=slots[sid];t,u=mapped[z['t']],mapped[z['u']]
   weights.append(cc.get((t,u),0)+cc.get((u,t),0))
  centers[i]=dict(a=min(A,B),c=C,weights=weights)
 return dict(free=free,centers=centers,positions=tuple(pos[perm[i]] for i in range(s)))

def solve_profile(eng,w,permutation_limit=120):
 s=eng.s;D=eng.D;ns={int(t):n for t,n in w['counts'].items()}
 slots,quotas,bycenter=inventory(ns,s,eng.v);nz=len(slots)
 ps=list(permutations(range(s)));step=max(1,len(ps)//permutation_limit);ps=ps[::step]
 if s==6 and eng.v==22:
  poses=[tuple(sorted(w['positions']))]+[tuple(range(a,a+s)) for a in (7,8,9,10,11)]
 else:
  center=(eng.v-s)//2+1
  poses=[tuple(sorted(w['positions']))]+[tuple(range(a,a+s)) for a in range(max(1,center-2),min(eng.v-s+2,center+3))]
  poses+=[tuple(range(eng.v-s+1,eng.v+1)),tuple(range(center,center+s-1))+(eng.v,),tuple(range(center,center+s-2))+(eng.v-1,eng.v)]
 ls=[];seen=set()
 for pos in dict.fromkeys(poses):
  for perm in ps:
   z=layout(eng,ns,slots,bycenter,pos,perm)
   key=(z['free'],tuple((c['a'],c['c'],tuple(c['weights'])) for c in z['centers']))
   if key in seen:continue
   seen.add(key);ls.append(z)
 nl=len(ls);tcol=nz+nl*s;nvar=tcol+1;rr=[];cc=[];vals=[];rhs=[];qr=[];lr=[]
 def add(items,b):
  r=len(rhs);rhs.append(b)
  for c,v in items:
   if v:rr.append(r);cc.append(c);vals.append(v)
  return r
 for q in quotas:qr.append(add([(j,-1) for j in q['slots']],-q['q']))
 for l,z in enumerate(ls):
  yr=[]
  for i,c in enumerate(z['centers']):
   y=nz+l*s+i
   ra=add([(y,1)],c['a']/D)
   rb=add([(y,1)]+[(sid,v/D) for sid,v in zip(bycenter[i],c['weights'])],c['c']/D)
   yr.append((ra,rb))
  rt=add([(tcol,1)]+[(nz+l*s+i,-1) for i in range(s)],z['free']/D)
  lr.append((rt,yr))
 mat=coo_matrix((vals,(rr,cc)),shape=(len(rhs),nvar)).tocsr()
 cost=np.zeros(nvar);cost[tcol]=-1
 res=linprog(cost,A_ub=mat,b_ub=rhs,bounds=[(0,z['capacity']) for z in slots]+[(None,None)]*(nl*s+1),method='highs',options={'time_limit':30})
 if not res.success:return dict(graph=w['graph'],group=w['group'],status=res.message,layout_count=nl)
 rational=lambda x:max(Q(),Q(round(float(x)*10000000),10000000))
 gs=[rational(-res.ineqlin.marginals[rt]) for rt,_ in lr];mass=sum(gs,Q());assert mass>0
 ds=[rational(-res.ineqlin.marginals[r])/mass for r in qr]
 free=Q();linear=Q();weight=[Q() for _ in slots];cert=[]
 for z,(rt,yr),g0 in zip(ls,lr,gs):
  g=g0/mass
  if not g:continue
  free+=g*Q(z['free'],D);betas=[]
  for i,(c,(_,rb)) in enumerate(zip(z['centers'],yr)):
   beta=min(g,rational(-res.ineqlin.marginals[rb])/mass);alpha=g-beta;betas.append(beta)
   linear+=alpha*Q(c['a'],D)+beta*Q(c['c'],D)
   for sid,v in zip(bycenter[i],c['weights']):weight[sid]+=beta*Q(v,D)
  cert.append(dict(probability=g,betas=betas,**z))
 quota_total=sum((delta*q['q'] for delta,q in zip(ds,quotas)),Q())
 penalty=Q();penalties=[]
 for j,z in enumerate(slots):
  demand=sum((delta for delta,q in zip(ds,quotas) if j in q['slots']),Q())
  kappa=max(Q(),demand-weight[j]);penalty+=kappa*z['capacity'];penalties.append(kappa)
 bound=free+linear-quota_total+penalty
 assert sum(c['probability'] for c in cert)==1
 return dict(graph=w['graph'],group=w['group'],old_bound=w['bound'],layout_count=nl,LP_bound=float(-res.fun),bound=bound,free_average=free,linear_part=linear,quota_part=quota_total,capacity_penalty=penalty,counts=ns,scale=D,slots=slots,quotas=[dict(**q,delta=d) for q,d in zip(quotas,ds) if d],penalties=penalties,layouts=cert)

def main():
 source=Path(sys.argv[1]);start=perf_counter();data=json.loads(source.read_text());cases=data['cases'];s=len(cases[0]['ds']);eng=Engine(cases[0]['v'],s);out=[]
 for idx,w in enumerate(cases):
  if Q(w['bound'])<1:continue
  ww=dict(w,positions=w['pos'],graph=idx,group=source.stem);z=solve_profile(eng,ww,permutation_limit=int(sys.argv[2]) if len(sys.argv)>2 else 120);out.append(z)
  print(idx,z.get('bound',z.get('status')),z.get('LP_bound'),'seconds',perf_counter()-start,flush=True)
  source.with_name(source.stem+'_JOINT.json').write_text(json.dumps(json_value(dict(source=str(source),complete=False,seconds=perf_counter()-start,results=out)),indent=2)+'\n')
  if perf_counter()-start>180:break
 else:
  source.with_name(source.stem+'_JOINT.json').write_text(json.dumps(json_value(dict(source=str(source),complete=True,seconds=perf_counter()-start,results=out)),indent=2)+'\n')

if __name__=='__main__':main()

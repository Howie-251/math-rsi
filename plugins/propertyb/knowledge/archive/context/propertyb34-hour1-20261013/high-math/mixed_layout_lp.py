"""Minimax mixture of labelled lock placements for actual unique low bad slots.
Floating LP proposes nonnegative weights. They are normalized as exact Fractions;
only the exact maximum-per-center objective is treated as a certificate.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from math import comb
import json,sys,time
import numpy as np
from scipy.optimize import linprog
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'computations'),str(Path(__file__).parent)]
from fast_position_dp import Engine
from multilock import Profile,rows,total_bound,pair_weight,json_value
from independent_structure_bounds import independent_rows,injection_probability
from mixed_six import trans

def inventory(ns,s,v):
 out=[]
 for i in range(s):
  bit=1<<i;ts=sorted(t for t in ns if t&bit);pure=max(0,(4*ns.get(bit,0)-(v-s)+2)//3);ss=[]
  for j,t in enumerate(ts):
   for u in ts[j:]:
    cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
    if cap and t&u==bit and (not pure or t==u==bit):ss.append((t,u))
  assert ss;out.append(ss)
 return out

def vector(eng,ns,slots,pos,perm):
 s=eng.s;v=eng.v;move=lambda t:sum(1<<perm[i] for i in range(s) if t&(1<<i));mp={t:move(t) for t in ns};counts={mp[t]:n for t,n in ns.items()};inv=[perm.index(j) for j in range(s)];free=0;vals=[None]*s
 for k in range(1,v+1):
  j=sum(p<k for p in pos);pivot=k in pos;aa,bb,cc=eng.states[k,j,pivot]
  A=sum(n*aa[t] for t,n in counts.items());B=sum(n*bb[t] for t,n in counts.items());base=min(A,B)
  C=sum(counts.get(t,0)*(counts.get(u,0)-int(t==u))*w for (t,u),w in cc.items()) if base else 0
  if not pivot:free+=min(base,C);continue
  i=inv[j];values=[]
  for t,u in slots[i]:
   mt,mu=mp[t],mp[u];loss=cc.get((mt,mu),0)+cc.get((mu,mt),0);assert C>=loss;values.append(min(base,C-loss))
  vals[i]=values
 return free,[x for xs in vals for x in xs]

def solve_one(eng,x,layouts):
 s=eng.s;ns={int(t):n for t,n in x['counts'].items()};slots=inventory(ns,s,eng.v);vectors=[];seen=set()
 for pos in layouts:
  for perm in permutations(range(s)):
   f,g=vector(eng,ns,slots,pos,perm);key=f,tuple(g)
   if key in seen:continue
   seen.add(key);vectors.append(dict(free=f,values=g,positions=tuple(pos[perm[i]] for i in range(s))))
 n=len(vectors);idx=[i for i,ss in enumerate(slots) for _ in ss];m=len(idx)
 mat=np.zeros((m,n+s));mat[:,:n]=np.asarray([z['values'] for z in vectors],dtype=float).T/eng.D
 for r,i in enumerate(idx):mat[r,n+i]=-1
 c=np.asarray([z['free']/eng.D for z in vectors]+[1]*s);eq=np.asarray([[1]*n+[0]*s],dtype=float)
 r=linprog(c,A_ub=mat,b_ub=np.zeros(m),A_eq=eq,b_eq=[1],bounds=(0,None),method='highs')
 if not r.success:raise RuntimeError(r.message)
 ps=[max(Fraction(),Fraction(round(float(p)*100000),100000)) if p>1e-9 else Fraction() for p in r.x[:n]];total=sum(ps,Fraction());ps=[p/total for p in ps]
 free=sum((p*Fraction(z['free'],eng.D) for p,z in zip(ps,vectors)),Fraction());av=[sum((p*Fraction(z['values'][j],eng.D) for p,z in zip(ps,vectors)),Fraction()) for j in range(m)];centers=[];off=0
 for i,ss in enumerate(slots):
  vv=av[off:off+len(ss)];off+=len(ss);centers.append(dict(center=i,slots=ss,averages=vv,maximum=max(vv)))
 bound=free+sum(z['maximum'] for z in centers)
 witnesses=[dict(probability=p,positions=z['positions']) for p,z in zip(ps,vectors) if p]
 return dict(group=x['group'],counts=ns,candidate_layout_vectors=n,LP_objective=float(r.fun),bound=bound,free_average=free,centers=centers,witnesses=witnesses)

if __name__=='__main__':
 start=time.perf_counter();eng=Engine(24,6);source=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low6_badnone.json').read_text());out=[]
 layouts=[tuple(range(a,a+6)) for a in (10,9,8,11)]+[(10,11,12,13,14,24),(9,10,11,12,13,24),(10,11,12,13,23,24),(8,9,10,11,12,14)]
 for x in source['results']:
  if x['group'] not in (1,3,4,5,8):continue
  z=solve_one(eng,x,layouts);out.append(z);print(x['group'],z['bound'],float(z['bound']),len(z['witnesses']),'sec',time.perf_counter()-start,flush=True)
  Path(__file__).with_name('MIXED_LAYOUT_LP.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')

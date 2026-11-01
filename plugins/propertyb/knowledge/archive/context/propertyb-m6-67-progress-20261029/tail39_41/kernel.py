import importlib.util,json,time,itertools
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
spec=importlib.util.spec_from_file_location('f',ROOT/'context/propertyb-m6-66-20261029/pilot/FOUR.py');f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f);c=f.c;c.M=66
from fractions import Fraction as F
orig=c.bad_pair_deletion

def deletion(v,pos,ell,j):
 bit=1<<j;other=((1<<len(pos))-1)^bit;typ=[T for T,n in ell.items() if n and T&bit];best=orig(v,pos,ell,j)
 cells=[]
 for ai,T in enumerate(typ):
  for U in typ[ai:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 for R in range(1<<len(pos)):
  if R&~other:continue
  d=sum(n for T,n in ell.items() if T&bit and not T&R);q=max(0,c.ceilings(5*d-(v-1-R.bit_count()),4));cost=F(0)
  for _,cap,w in sorted((cell for cell in cells if not cell[0]&R),key=lambda z:z[2]):
   take=min(q,cap);cost+=take*w;q-=take
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=deletion

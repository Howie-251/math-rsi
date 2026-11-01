from pathlib import Path
import importlib.util,itertools,json,time
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('d',P.parent/'small31_33/diagnose.py');d=importlib.util.module_from_spec(s);s.loader.exec_module(d)
c=d.c
from fractions import Fraction
# Use each avoided quota individually against the same actual cell vector.
def mxdelete(v,pos,ell,j):
 bit=1<<j;typ=[T for T,n in ell.items() if n and T&bit];cells=[]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 best=Fraction(0)
 for R in range(1<<len(pos)):
  if R&bit:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R);q=d.quota(v-R.bit_count(),f);cost=Fraction(0)
  for union,cap,w in sorted((a for a in cells if not a[0]&R),key=lambda a:a[2]):
   use=min(q,cap);cost+=use*w;q-=use
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=mxdelete

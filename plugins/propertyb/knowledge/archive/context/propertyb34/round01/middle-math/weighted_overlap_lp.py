"""Bounded proposal experiment; exact independent replay is a separate step."""
from pathlib import Path
from fractions import Fraction as Q
from time import perf_counter
import json
from joint_layout_lp import inventory,solve_profile,Engine,json_value
HERE=Path(__file__).resolve().parent

def overlap_inventory(ns,s,v):
 slots,qs,bc=inventory(ns,s,v)
 for i in range(s):
  for R in range(1<<s):
   if R&(1<<i):continue
   n=sum(c for t,c in ns.items() if t&(1<<i) and not t&R)
   q=max(0,4*n-(v-1-R.bit_count()))
   if not q:continue
   ids=[];hs=[]
   for j in bc[i]:
    z=slots[j];t,u=z['t'],z['u']
    if (t|u)&R:continue
    h=min(3,(t&u).bit_count()-1+min(5-t.bit_count(),5-u.bit_count()))
    if h:ids.append(j);hs.append(h)
   qs.append(dict(center=i,avoid=R,edge_count=n,q=q,slots=ids,coefficients=hs,kind='overlap'))
 return slots,qs,bc

def main():
 start=perf_counter();eng=Engine(22,3);source=json.loads((HERE/'TWENTYTWO_SIX_TRIPLES.json').read_text());out=[]
 for g in source['groups']:
  for w in g['profiles']:
   if Q(w.get('joint',w).get('bound','9'))<1:continue
   z=solve_profile(eng,w,quota_builder=overlap_inventory);out.append(z)
   print(w['graph'],w['group'],w['codegrees'],w['common'],z.get('bound',z.get('status')),flush=True)
  if perf_counter()-start>120:break
 (HERE/'WEIGHTED_OVERLAP_RESULTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=perf_counter()-start,results=out)),indent=2)+'\n')

if __name__=='__main__':main()

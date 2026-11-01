from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate

def from_intersections(s,d,inter):
 f={0:35}|{1<<i:d for i in range(s)}|inter
 n={}
 for mask in sorted(range(1<<s),key=int.bit_count,reverse=True):
  n[mask]=f.get(mask,0)-sum(x for t,x in n.items() if t&mask==mask)
 return n

def test(s,d,c,trip=0,quad=0):
 inter={m: c if m.bit_count()==2 else trip if m.bit_count()==3 else quad if m.bit_count()==4 else 0 for m in range(1<<s) if m.bit_count()>=2}
 ns=from_intersections(s,d,inter)
 if min(ns.values())<0:return None
 layouts=set(tuple(range(k,k+s)) for k in range(1,21-s))
 vals=[evaluate(19,ns,p) for p in layouts]
 z=min(vals,key=lambda x:x['bound'])
 return {'s':s,'d':d,'c':c,'trip':trip,'quad':quad,'ns':ns,'pos':z['positions'],'bound':str(z['bound'])}
if __name__=='__main__':
 for s in [4,5,6]:
  for d in [8,9]:
   for c in [1,2,3]:
    for t in [0,1,2]:
     z=test(s,d,c,t)
     if z:print(z,flush=True)

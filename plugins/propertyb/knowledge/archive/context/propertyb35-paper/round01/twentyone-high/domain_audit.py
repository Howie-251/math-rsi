"""Independent top-down exact inventory recovery for all small degree6-reduction input domains."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,product
import json,time
HERE=Path(__file__).parent

def recover(inc,s):
 ns={}
 for m in sorted(range(1<<s),key=int.bit_count,reverse=True):ns[m]=inc[m]-sum(n for t,n in ns.items() if t&m==m)
 return ns if min(ns.values())>=0 else None

def key(ns,s):return tuple(ns.get(m,ns.get(str(m),0)) for m in range(1<<s))
def inc_for(ds,pairs,high):return {m:0 for m in range(1<<len(ds))}|{0:35}|{1<<i:d for i,d in enumerate(ds)}|{sum(1<<i for i in ij):v for ij,v in pairs.items()}|high

def main():
 st=time.time();checks=[]
 def check(name,generated,s,predicate=lambda r:True):
  rr=[r for r in json.loads((HERE/name).read_text())['cases'] if predicate(r)];seen={key(r['counts'],s) for r in rr};assert seen==generated;checks.append(dict(file=name,inventory_count=len(seen)))
 seen=set()
 for ps in combinations_with_replacement(range(1,4),3):
  pm=dict(zip(combinations(range(3),2),ps))
  if any(sum(c-1 for ij,c in pm.items() if i in ij)>4 for i in range(3)):continue
  for t in range(min(ps)+1):
   ns=recover(inc_for([6]*3,pm,{7:t}),3)
   if ns is not None:seen.add(key(ns,3))
 check('TRIPLES.json',seen,3,lambda r:r['degrees']==[6,6,6])
 seen=set();trs=list(combinations(range(4),3))
 for ts in product(range(3),repeat=4):
  for q in range(min(ts)+1):
   ns=recover(inc_for([6]*4,{ij:2 for ij in combinations(range(4),2)},{sum(1<<i for i in S):t for S,t in zip(trs,ts)}|{15:q}),4)
   if ns is not None:seen.add(key(ns,4))
 check('FOUR_SIXES.json',seen,4)
 # Full low-low-partner triples, including symmetric mixed partner codegrees.
 seen=set()
 for d in (7,8,9):
  for xy in (1,2,3):
   for a in range(1,4):
    for b in range(a,4):
     if xy+max(a,b)-2>4:continue
     for t in range(min(xy,a,b)+1):
      ns=recover(inc_for([6,6,d],{(0,1):xy,(0,2):a,(1,2):b},{7:t}),3)
      if ns is not None:seen.add(key(ns,3))
 check('TWO_SIXES_TRIPLES.json',seen,3)
 allow={}
 for r in json.loads((HERE/'TWO_SIXES_TRIPLES.json').read_text())['cases']:
  if not r['strict'] and r['codegrees'][0]==2:allow.setdefault((r['degrees'][2],tuple(r['codegrees'][1:])),set()).add(r['triple'])
 seen=set()
 for d in (7,8):
  for cs in combinations_with_replacement((1,2),3):
   pm={ij:2 for ij in combinations(range(3),2)}|{(i,3):cs[i] for i in range(3)};opts=[(0,1,2)]+[allow[(d,(cs[i],cs[j]))] for i,j in combinations(range(3),2)]
   for ts in product(*opts):
    for q in range(min(ts)+1):
     ns=recover(inc_for([6,6,6,d],pm,{sum(1<<i for i in S):t for S,t in zip(trs,ts)}|{15:q}),4)
     if ns is not None:seen.add(key(ns,4))
 check('THREE_SIXES_FOUR.json',seen,4)
 seen=set()
 for d,e in [(7,7),(7,8),(8,8)]:
  for c in range(1,4 if d==7 else 5):
   pm={ij:2 if ij[1]<3 else c if ij[0]==3 else 1 for ij in combinations(range(5),2)}
   for gs in product((0,1),repeat=3):
    ns=recover(inc_for([6,6,6,d,e],pm,{7:2}|{(1<<i)|24:g for i,g in enumerate(gs)}),5)
    if ns is not None:seen.add(key(ns,5))
 check('THREE_SIXES_FIVE_T2.json',seen,5)
 seen=set();lp=list(combinations(range(3),2));defects=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
 for T in (0,1):
  choices=defects if T==0 else [(0,0,0)]
  for az,bz in product(choices,repeat=2):
   for c in range(1,5):
    pm={ij:2 if ij[1]<3 else c if ij[0]==3 else 1 for ij in combinations(range(5),2)}
    for gs in product((0,1),repeat=3):
     for hs in product(*[range(min(a,b,gs[i],gs[j])+1) for (i,j),a,b in zip(lp,az,bz)]):
      high={7:T}|{(1<<i)|24:g for i,g in enumerate(gs)}
      for (i,j),a,b,h in zip(lp,az,bz,hs):high[(1<<i)|(1<<j)|8]=a;high[(1<<i)|(1<<j)|16]=b;high[(1<<i)|(1<<j)|24]=h
      ns=recover(inc_for([6,6,6,8,8],pm,high),5)
      if ns is not None:seen.add(key(ns,5))
 check('THREE_SIXES_TWO_EIGHTS.json',seen,5)
 seen=set()
 for c in range(1,5):
  for a,b in product((0,1),repeat=2):
   ns=recover(inc_for([6,6,8,8],{(0,1):3,(0,2):1,(0,3):1,(1,2):1,(1,3):1,(2,3):c},{13:a,14:b}),4)
   if ns is not None:seen.add(key(ns,4))
 check('TWO_SIXES_UNIT_EIGHTS.json',seen,4)
 result=dict(status='PASS',scope=__doc__,checks=checks,elapsed_seconds=time.time()-st);(HERE/'DOMAIN_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()

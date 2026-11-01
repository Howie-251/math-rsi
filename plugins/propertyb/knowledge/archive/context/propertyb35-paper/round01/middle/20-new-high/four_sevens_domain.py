"""Complete M35 v20 four-degree7 domain after strong-codegree exclusion.
Six inclusive pair counts1/2, four inclusive triples0..min containing pair,
inclusive quadruple0..min triples, all exact inventories recovered and nonnegative.
True S4 relabellings only; lock positions must transport with the labels.
"""
from pathlib import Path
from itertools import combinations,permutations,product
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True
PAIRS=list(combinations(range(4),2));TRIPLES=list(combinations(range(4),3));PERMS=list(permutations(range(4)))
MOVES=[{t:sum(1<<p[i] for i in range(4) if t>>i&1) for t in range(16)} for p in PERMS]
def recover(ps,ts,q):
 I={1<<i:7 for i in range(4)};I.update({sum(1<<i for i in S):c for S,c in zip(PAIRS,ps)});I.update({sum(1<<i for i in S):c for S,c in zip(TRIPLES,ts)});I[15]=q
 ns={}
 for t in sorted(I,key=int.bit_count,reverse=True):ns[t]=I[t]-sum(n for u,n in ns.items() if u&t==t)
 ns[0]=35-sum(ns.values())
 return ns if min(ns.values())>=0 else None
def key(ns):return tuple(ns.get(t,0) for t in range(16))
def main():
 start=time.time();seen={};out=[];labelled=[]
 for ps in product((1,2),repeat=6):
  caps=[min(c for S,c in zip(PAIRS,ps) if set(S)<=set(T)) for T in TRIPLES]
  for ts in product(*(range(c+1) for c in caps)):
   for q in range(min(ts)+1):
    ns=recover(ps,ts,q)
    if ns is None:continue
    k=key(ns)
    if k in seen:
     index,perm=seen[k]
    else:
     index=len(out);out.append(dict(id=index,counts=ns,pairs=ps,triples=ts,four=q,labelled_count=0))
     for perm,move in zip(PERMS,MOVES):
      moved={move[t]:n for t,n in ns.items()};seen[key(moved)]=(index,perm)
     index,perm=seen[k]
    out[index]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=index,from_representative_permutation=perm))
 result=dict(scope=__doc__,labelled_count=len(labelled),orbit_count=len(out),orbits=out,labelled=labelled,elapsed_seconds=time.time()-start)
 (HERE/'FOUR_SEVENS_DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print('labelled',len(labelled),'orbits',len(out),'seconds',time.time()-start)
if __name__=='__main__':main()

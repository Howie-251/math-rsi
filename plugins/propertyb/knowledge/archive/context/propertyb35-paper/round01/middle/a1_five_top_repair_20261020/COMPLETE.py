"""Complete analytic K5 clique-packing families and one fixed six-lock bound."""
from pathlib import Path
from itertools import combinations,permutations
from math import comb
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from multilock import Profile,rows,total_bound,json_value
from independent_structure_bounds import independent_rows
st=time.process_time();pairs=list(combinations(range(5),2));allpairs=set(pairs)
triples=list(combinations(range(5),3));quads=list(combinations(range(5),4))
def fam(big):
 used=set(p for b in big for p in combinations(b,2));left=sorted(allpairs-used)
 for bits in range(1<<len(left)):
  yield tuple(sorted(tuple(b) for b in list(big)+[p for j,p in enumerate(left) if bits>>j&1]))
packings=list(fam([]))
for T in triples:packings.extend(fam([T]))
for a,b in combinations(triples,2):
 if len(set(a)&set(b))==1:packings.extend(fam([a,b]))
for Q in quads:packings.extend(fam([Q]))
assert len(packings)==len(set(packings))==2624

def code(pp):return tuple(sorted(sum(1<<i for i in t) for t in pp))
def inventory(ds,pp):
 ns={63^(1<<(i+1)):1 for i in range(5)};ns[1]=4
 for T in pp:ns[sum(1<<(i+1) for i in T)]=1
 for i,d in enumerate(ds):ns[1<<(i+1)]=d-4-sum(i in T for T in pp)
 ns[0]=35-sum(ns.values());assert min(ns.values())>=0 and sum(ns.values())==35
 return ns
out=[];domains=[];position=(9,10,11,12,13,14)
for n8 in range(6):
 ds=tuple([8]*n8+[9]*(5-n8));group=[g for g in permutations(range(5)) if all(ds[i]==ds[g[i]] for i in range(5))]
 domain={code(pp):pp for pp in packings if all(sum(len(T)-1 for T in pp if i in T)<=4*ds[i]-31 for i in range(5))}
 seen=set();representatives=[]
 for key in sorted(domain):
  if key in seen:continue
  pp=domain[key];image={tuple(sorted(sum(1<<g[i] for i in range(5) if m>>i&1) for m in key)) for g in group}
  assert image<=domain.keys();assert not image&seen;seen|=image;representatives.append((key,pp,len(image)))
 assert seen==domain.keys()
 domains.append(dict(eight_count=n8,degrees=list(ds),labelled_count=len(domain),orbit_count=len(representatives),labelled_keys=[list(k) for k in sorted(domain)]))
 for key,pp,orbit_size in representatives:
  ns=inventory(ds,pp);rr=rows(Profile(21,5,position,ns));value=total_bound(rr)
  stubs=[frozenset(i+1 for i in range(6) if m>>i&1) for m,n in ns.items() for _ in range(n)]
  ir=independent_rows(21,position,stubs)
  assert all((r['A'],r['B'],r['C'])==(v['A'],v['B'],v['C']) for r,v in zip(rr,ir))
  assert sum(min(r['A'],r['B'],r['C']) for r in ir)==value
  out.append(dict(eight_count=n8,degrees=[9]+list(ds),packing=list(key),orbit_size=orbit_size,counts=ns,positions=position,bound=value,strict=value<1,all_deductions_zero=True))
  assert time.process_time()-st<12,'Explicit bounded CPU ceiling'
result=dict(complete=True,all_packings=2624,total_labels=sum(d['labelled_count'] for d in domains),total_orbits=len(out),domains=domains,cases=out,strict=sum(r['strict'] for r in out),max=max(r['bound'] for r in out),cpu_seconds=time.process_time()-st)
(P/'COMPLETE.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print({k:str(v) for k,v in result.items() if k not in ['domains','cases']})

"""Second domain generation only; no selector, signed probability or source code import.

High traces: ordered Cartesian words -> multiset keys -> explicit orbit partition.
J: force uncovered P-pairs first, then allocate residual integer multiplicities
under endpoint capacities. Compare complete source-key sets, not counts alone.
"""
import argparse,itertools as it,json,time,resource
from pathlib import Path
P=Path(__file__).resolve().parent;SOURCE=P.parent
V=tuple(range(6));C=frozenset(range(5));PAIRS=list(it.combinations(V,2))
INVENTORIES=((6,2,0),(5,1,1),(4,3,0),(3,2,1))
TRI=list(it.combinations(V,3));QUAD=list(it.combinations(V,4))

def key(inv,nine,T,J):return (tuple(inv),nine,tuple(tuple(A) for A in T),tuple(J))
def expected_sources():
 ans=set();counts={}
 for name in ('CENSUS_PASSED.jsonl','CENSUS_NONGATED.jsonl'):
  count=0
  with (SOURCE/name).open() as f:
   for line in f:
    d=json.loads(line);q=key(d['inventory'],d['nine'],d['higher'],d['J'])
    assert q not in ans,('duplicate archived key',q);ans.add(q);count+=1
  counts[name]=count
 return ans,counts

def high_partition(n3,n4,nine):
 # Ordered words differ from the original combinations-with-replacement generator.
 words=set()
 for t in it.product(TRI,repeat=n3):
  for q in it.product(QUAD,repeat=n4):
   T=tuple(sorted(t+q)); common=set(C)
   for A in T:common&=set(A)
   if not common:words.add(T)
 # Enumerate the genuine degree-preserving group, fixing 5 and the nine point.
 free=[i for i in range(5) if i!=nine]
 group=[]
 for p in it.permutations(free):
  perm=list(V)
  for src,dst in zip(free,p):perm[src]=dst
  assert perm[5]==5 and perm[nine]==nine
  group.append(perm)
 remaining=set(words);orbits=[]
 while remaining:
  T=next(iter(remaining));orbit={tuple(sorted(tuple(sorted(p[v] for v in A)) for A in T)) for p in group}
  assert orbit<=words
  # Whole group image is an orbit, so unvisited images all enter together.
  assert orbit<=remaining
  remaining-=orbit;orbits.append((min(orbit),len(orbit)))
 assert sum(s for T,s in orbits)==len(words)
 return sorted(orbits),len(words),len(group)

def generate_J(n2,degree,T):
 # mandatory[e] records coverage not supplied by the internal edge or a high trace.
 h=[sum(v in A for A in T) for v in V]
 w=[sum(len(A)-1 for A in T if v in A) for v in V]
 ci=[int(v in C) for v in V]
 cap=[min(degree[v]-ci[v]-h[v],4*degree[v]-18-4*ci[v]-w[v]) for v in V]
 forced=[int(not(set(e)<=C or any(set(e)<=set(A) for A in T))) for e in PAIRS]
 residual=n2-sum(forced)
 if residual<0:return
 avail=cap[:]
 for m,(a,b) in zip(forced,PAIRS):avail[a]-=m;avail[b]-=m
 if min(avail)<0:return
 J=forced[:]
 # Allocate all residual copies of each pair once; unlike the source generator,
 # capacities prune during construction and forced copies are already removed.
 def rec(k,r):
  if r==0:
   # Later residual multiplicities are zero, not stale recursive values.
   yield tuple(J);return
  if k==15 or sum(avail)<2*r:return
  active={v for e in PAIRS[k:] for v in e}
  if sum(avail[v] for v in active)<2*r:return
  a,b=PAIRS[k]
  for m in range(min(r,avail[a],avail[b])+1):
   J[k]=forced[k]+m;avail[a]-=m;avail[b]-=m
   yield from rec(k+1,r-m)
   avail[a]+=m;avail[b]+=m
  J[k]=forced[k]
 yield from rec(0,residual)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--max-cpu',type=float,default=60);ap.add_argument('--profile-cells',type=int,default=0);args=ap.parse_args()
 start=time.process_time();expected,source_counts=expected_sources();original=len(expected)
 generated=set();rows=[];cells=[];high_total=0;prefix=False
 for inv in INVENTORIES:
  n2,n3,n4=inv
  for nine in (0,5):
   if args.profile_cells and len(cells)>=args.profile_cells:prefix=True;break
   reps,labelled,order=high_partition(n3,n4,nine);high_total+=len(reps);cellcount=0
   degree=[8+int(v==nine) for v in V]
   for T,orbit_size in reps:
    count=0
    for J in generate_J(n2,degree,T):
     q=key(inv,nine,T,J)
     assert q not in generated,('duplicate generated key',q)
     assert q in expected,('new key absent from archived domain',q)
     generated.add(q);expected.remove(q);count+=1;cellcount+=1
     # Recompute all defining inequalities independently on the emitted input.
     ds=[sum(m for m,e in zip(J,PAIRS) if v in e) for v in V]
     assert sum(J)==n2
     u=[degree[v]-int(v in C)-sum(v in A for A in T)-ds[v] for v in V]
     assert min(u)>=0 and sum(u)==24+n3+2*n4
     for v in V:
      assert ds[v]+sum(len(A)-1 for A in T if v in A)<=4*degree[v]-18-4*int(v in C)
     assert all(set(e)<=C or any(set(e)<=set(A) for A in T) or J[k]>=1 for k,e in enumerate(PAIRS))
    rows.append({'inventory':inv,'nine':nine,'higher':T,'orbit_size':orbit_size,'necessary':count})
   cells.append({'inventory':inv,'nine':nine,'group_order':order,'labelled_high_families':labelled,'higher_orbits':len(reps),'necessary':cellcount})
   if time.process_time()-start>args.max_cpu:prefix=True;break
  if prefix:break
 if not prefix:
  assert not expected,('archived keys absent from independent domain',next(iter(expected)))
  assert len(generated)==original==123621 and high_total==169
  # Counts per representative are a separate consistency check after full set equality.
  census=json.load(open(SOURCE/'CENSUS.json'))
  archived={(tuple(r['inventory']),r['nine'],tuple(tuple(A) for A in r['higher'])):(r['necessary'],r['high_orbit_size']) for r in census['rows']}
  rebuilt={(tuple(r['inventory']),r['nine'],tuple(tuple(A) for A in r['higher'])):(r['necessary'],r['orbit_size']) for r in rows}
  assert archived==rebuilt
 out={'status':'PREFIX_ONLY' if prefix else 'PASS_COMPLETE_KEY_SET_EQUALITY','scope':__doc__,'source_counts':source_counts,'archived_total':original,'generated_count':len(generated),'archived_remaining':len(expected),'higher_orbits_completed':high_total,'cells':cells,'rows':rows,'comparison':'Every generated key removed from archived set; no generated duplicate; '+('prefix only, archived keys remain.' if prefix else 'final archived set empty.')+' No probability gate re-executed.','cpu_seconds':time.process_time()-start,'maxrss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 file=P/('PROFILE.json' if args.profile_cells else 'RESULT.json');file.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
if __name__=='__main__':main()

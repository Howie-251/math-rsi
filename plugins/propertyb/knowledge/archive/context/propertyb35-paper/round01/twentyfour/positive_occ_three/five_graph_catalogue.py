"""Exact five-set overlap multigraph catalogue. Standard library only; no H enumeration."""
from pathlib import Path
import itertools,json,time
from collections import Counter
from math import comb
HERE=Path(__file__).parent
EDGES=list(itertools.combinations(range(5),2))
PERMS=list(itertools.permutations(range(5)))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}
MAPS=[tuple(EDGE_INDEX[tuple(sorted((p[i],p[j])))] for i,j in EDGES) for p in PERMS]
def image(g,mapping):
 out=[0]*10
 for j,k in enumerate(mapping):out[k]=g[j]
 return tuple(out)
def degrees(g):return [sum(n for (a,b),n in zip(EDGES,g) if i in (a,b)) for i in range(5)]
def m2(g):return sum(g[i]*g[j] for i,e in enumerate(EDGES) for j,f in enumerate(EDGES) if i<j and not set(e)&set(f))
def domain():
 d=[0]*5;g=[0]*10
 def rec(j,E,M):
  if j==10:
   if 4<=E<=8 and 1<=M<=6:yield tuple(g)
   return
  a,b=EDGES[j];previous_disjoint=sum(g[k] for k in range(j) if not set(EDGES[k])&{a,b})
  for n in range(min(4-d[a],4-d[b],8-E)+1):
   if M+n*previous_disjoint>6:break
   g[j]=n;d[a]+=n;d[b]+=n
   yield from rec(j+1,E+n,M+n*previous_disjoint)
   d[a]-=n;d[b]-=n
  g[j]=0
 yield from rec(0,0,0)
def independent_domain():
 # Per-vertex recursion: assign all edges out of vertex i together.
 out=set();g=[0]*10;d=[0]*5
 def rec(i):
  if i==4:
   if 4<=sum(g)<=8 and 1<=m2(g)<=6:out.add(tuple(g))
   return
  js=list(range(i+1,5));idx=[EDGE_INDEX[i,j] for j in js]
  for vals in itertools.product(range(5),repeat=len(js)):
   if sum(vals)+d[i]>4 or any(d[j]+v>4 for j,v in zip(js,vals)):continue
   for j,k,v in zip(js,idx,vals):g[k]=v;d[j]+=v
   rec(i+1)
   for j,k,v in zip(js,idx,vals):g[k]=0;d[j]-=v
 rec(0);return out
def points(g):
 ps=[]
 for (i,j),n in zip(EDGES,g):
  for k in range(n):ps.append(dict(name=f'e{i}{j}_{k}',mask=(1<<i)|(1<<j),positive_degree=2,negative_degree_cap=5))
 for i,d in enumerate(degrees(g)):
  for k in range(4-d):ps.append(dict(name=f'p{i}_{k}',mask=1<<i,positive_degree=1,negative_degree_cap=6))
 return ps
def transversals(ps,k):
 out=[]
 for ids in itertools.combinations(range(len(ps)),k):
  mask=0
  for i in ids:mask|=ps[i]['mask']
  if mask==31:out.append(ids)
 return out
def ie_count(g,k=4):
 private=[4-d for d in degrees(g)];total=0;layers=[0]*6
 for mask in range(32):
  n=sum(private[i] for i in range(5) if mask>>i&1)+sum(v for (i,j),v in zip(EDGES,g) if mask>>i&1 and mask>>j&1)
  term=comb(n,k) if n>=k else 0
  layers[mask.bit_count()]+=term
  total+=(-1)**(5-mask.bit_count())*term
 return total,layers
def describe(g):
 ds=degrees(g);ps=points(g);c3=transversals(ps,3);c4=transversals(ps,4)
 formula=sum(g[i]*g[j]*(8-ds[next(iter(set(range(5))-set(e)-set(f)))]) for i,e in enumerate(EDGES) for j,f in enumerate(EDGES) if i<j and not set(e)&set(f))
 assert formula%2==0 and formula//2==len(c3)
 covers=[e for e,n in zip(EDGES,g) if n and all(not m or set(e)&set(f) for f,m in zip(EDGES,g))]
 min4=[t for t in c4 if not any(set(s)<=set(t) for s in c3)]
 callers=[]
 if len(c3)>=14:callers.append('C3_ge14')
 if covers:callers.append('supported_edge_endpoint_cover')
 ie,layers=ie_count(g);assert ie==len(c4)
 return dict(edge_vector=g,edges=[dict(endpoints=e,multiplicity=n) for e,n in zip(EDGES,g) if n],E=sum(g),M2=m2(g),degrees=ds,private_counts=[4-d for d in ds],union_size=len(ps),support_edges=sum(n>0 for n in g),degree_profile=sorted(ds,reverse=True),points=ps,C3=len(c3),C4=len(c4),C4_independent_IE=ie,C4_IE_layers=layers,minimal_C4=len(min4),candidate_red_size4_count=len(c3),candidate_red_size5_count=len(c4),three_point_transversals=c3,supported_edge_endpoint_covers=covers,callers=callers,aut_group_order=sum(image(g,m)==g for m in MAPS))
def main():
 st=time.time();dom=set(domain());ind=independent_domain();assert dom==ind
 left=set(dom);out=[]
 while left:
  g=min(left);orbit={image(g,m) for m in MAPS};assert orbit<=dom and min(orbit)==g
  desc=describe(g)
  for h in orbit:assert ie_count(h)[0]==desc['C4']
  out.append(dict(index=len(out),orbit_size=len(orbit),**desc));left-=orbit
 assert sum(z['orbit_size'] for z in out)==len(dom)
 result=dict(scope=__doc__,status='PASS',labeled_graphs=len(dom),orbits=len(out),elapsed_seconds=time.time()-st,summary=[dict(E=e,M2=m,orbits=sum(z['E']==e and z['M2']==m for z in out),labels=sum(z['orbit_size'] for z in out if z['E']==e and z['M2']==m),minimum_C4=min(z['C4'] for z in out if z['E']==e and z['M2']==m)) for e in range(4,9) for m in range(1,7) if any(z['E']==e and z['M2']==m for z in out)],minimum_C4=min(z['C4'] for z in out),maximum_C4=max(z['C4'] for z in out),minimum_C4_orbits=[z['index'] for z in out if z['C4']==min(a['C4'] for a in out)],caller_covered_orbits=sum(bool(z['callers']) for z in out),residual_orbits=[z['index'] for z in out if not z['callers']],graphs=out)
 (HERE/'five_graph_catalogue.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='graphs'},indent=2))
 for z in out:
  if not z['callers']:print('RESIDUAL',z['index'],z['edges'],'E/M2',z['E'],z['M2'],'deg',z['degree_profile'],'C3',z['C3'],'C4',z['C4'],flush=True)
if __name__=='__main__':main()

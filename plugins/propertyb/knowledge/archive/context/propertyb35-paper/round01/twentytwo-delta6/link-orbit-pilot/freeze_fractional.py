"""Reconstruct a rational basic solution and replay every exact aggregate inequality."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time();m=json.loads((HERE/'MODEL.json').read_text());s=json.loads((HERE/'SUMMARY.json').read_text());edges=m['edges'];edgekey=lambda e:json.dumps(e);ids={edgekey(e):i for i,e in enumerate(edges)};support=[ids[edgekey(z['edge'])]for z in s['LP_support']];values=[z['count']for z in s['LP_support']];t0=s['LP_maximin'];N=len(support)+1
P=[[Q(x)for x in r]for r in m['probabilities']];A=m['constraint_coefficients'];candidates=[]
for row,lo,hi in zip(A,m['lower'],m['upper']):
 val=sum(row[i]*x for i,x in zip(support,values));rs=[Q(row[i])for i in support]+[Q()]
 if abs(val-lo)<1e-6:candidates.append((rs,Q(lo)))
 if hi is not None and abs(val-hi)<1e-6:candidates.append((rs,Q(hi)))
for row in P:
 if abs(sum(float(row[i])*x for i,x in zip(support,values))-t0)<1e-6:candidates.append(([row[i]for i in support]+[-Q(1)],Q()))
for j,i in enumerate(support):
 if abs(values[j]-m['simple_orbit_capacities'][i])<1e-6:
  row=[Q()]*N;row[j]=1;candidates.append((row,Q(m['simple_orbit_capacities'][i])))
basis={}
for row,b in candidates:
 row=list(row)+[b]
 for p,rs in sorted(basis.items()):
  v=row[p]
  if v:row=[x-v*y for x,y in zip(row,rs)]
 pivot=next((j for j,x in enumerate(row[:-1])if x),None)
 if pivot is None:
  assert not row[-1];continue
 v=row[pivot];basis[pivot]=[x/v for x in row]
 if len(basis)==N:break
assert len(basis)==N,(len(basis),N)
sol=[Q()]*N
for p,row in sorted(basis.items(),reverse=True):sol[p]=row[-1]-sum(row[j]*sol[j]for j in range(p+1,N))
counts=[Q()for e in edges]
for i,x in zip(support,sol):counts[i]=x
t=sol[-1];scores=[sum(a*b for a,b in zip(counts,row))for row in P];marg=[sum(a*b for a,b in zip(counts,row))for row in A]
assert all(x>=0 and x<=cap for x,cap in zip(counts,m['simple_orbit_capacities']))
assert all(x>=lo and (hi is None or x<=hi)for x,lo,hi in zip(marg,m['lower'],m['upper']))
assert min(scores)==t and t>=1
out=dict(scope=__doc__,status='EXACT_FRACTIONAL_AGGREGATE_OBSTRUCTION',not_a_hypergraph=True,counts=[dict(edge=e,count=str(x))for e,x in zip(edges,counts)if x],exact_minimum_score=str(t),marginals=[str(x)for x in marg],constraints=m['constraint_names'],all_families_checked=len(P),all_edge_orbits=len(edges),linear_system_rank=N,cpu_seconds=time.process_time()-start)
(HERE/'FRACTIONAL_OBSTRUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

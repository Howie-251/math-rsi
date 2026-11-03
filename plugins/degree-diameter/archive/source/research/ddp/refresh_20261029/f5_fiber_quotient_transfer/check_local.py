#!/usr/bin/env python3
"""One fixed F5 local/linear diagnostic; no graphs, paths, or BFS."""
import itertools,json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
P=json.loads((HERE.parent/'f5_full_d20_D3/PARAMETERS.json').read_text())
C,T,D,rev=P['controller'],P['matrices'],P['directions'],P['inverse_ports']
p=5

def mv(A,x):return tuple(sum(a*b for a,b in zip(row,x))%5 for row in A)
def sub(x,y):return tuple((a-b)%5 for a,b in zip(x,y))
def rref(rows,n):
 A=[list(row) for row in rows];piv=[];original=list(range(len(A)));basis_rows=[]
 for c in range(n):
  s=next((i for i in range(len(piv),len(A)) if A[i][c]),None)
  if s is None:continue
  k=len(piv);A[k],A[s]=A[s],A[k];original[k],original[s]=original[s],original[k]
  inv=pow(A[k][c],-1,5);A[k]=[(v*inv)%5 for v in A[k]]
  for i in range(len(A)):
   if i!=k and A[i][c]:
    v=A[i][c];A[i]=[(x-v*y)%5 for x,y in zip(A[i],A[k])]
  piv.append(c);basis_rows.append(original[k])
  if len(piv)==len(A):break
 return A,piv,basis_rows

def rank(vecs):return len(rref(vecs,3)[1])
def nullspace(A,n):
 R,piv,_=rref(A,n);out=[]
 for c in range(n):
  if c in piv:continue
  x=[0]*n;x[c]=1
  for i,k in enumerate(piv):x[k]=(-R[i][c])%5
  out.append(x)
 return out

def orthogonal(v):
 k=next(i for i,x in enumerate(v) if x);out=[]
 for j in range(3):
  if j==k:continue
  w=[0]*3;w[j]=1;w[k]=-v[j]*pow(v[k],-1,5)%5;out.append(w)
 return out

rows=[];equation_info=[]
for a in range(30):
 for port,b in enumerate(C[a]):
  if a>b:continue
  direction=D[rev[port]]
  for u in orthogonal(direction):
   row=[0]*90
   for j in range(3):
    row[3*b+j]=u[j]
    row[3*a+j]=-sum(u[i]*T[port][i][j] for i in range(3))%5
   rows.append(row);equation_info.append(dict(a=a,b=b,port=port,annihilator=u))
R,piv,certificate_rows=rref(rows,90)
N=nullspace(rows,90)
assert len(rows)==120 and len(piv)+len(N)==90
# Preserve the exact finite matrix and its reduction, not merely a rank claim.
(HERE/'TRANSLATION_SYSTEM.json').write_text(json.dumps(dict(field=5,variable_order='3*a+i',rows=rows,equations=equation_info,pivots=piv,rref=R,nullspace_basis=N),indent=2)+'\n')
W=(1,0,0);rank_ports=[]
for port in range(4):
 r=rank([W,mv(T[port],W),D[rev[port]]])-1
 rank_ports.append(r)
# One fiber only: independently count scalar orbits of each port's true line.
scalar_results=[]
V=list(itertools.product(range(5),repeat=3))
for H in ([1,4],[1,2,3,4]):
 def canonical(x):return min(tuple(h*a%5 for a in x) for h in H)
 orbits=sorted(set(map(canonical,V)));hist={}
 for x in orbits:
  deg=0
  for port in range(4):
   y=mv(T[port],x);d=D[rev[port]]
   images={canonical(tuple((y[i]+t*d[i])%5 for i in range(3))) for t in range(5)}
   deg+=len(images)
  hist[deg]=hist.get(deg,0)+1
 scalar_results.append(dict(scalar_subgroup=H,fiber_orbits=len(orbits),graph_order=30*len(orbits),local_degree_distribution=hist,maximum_degree=max(hist),diameter_by_projection_and_Moore=3))
result=dict(status='COMPLETE_FIXED_ALGEBRA_DIAGNOSTIC',translation_system=dict(equations=120,variables=90,rank=len(piv),nullity=len(N)),fixed_direction_quotient=dict(W=[list(W)],order=750,port_ranks=rank_ports,degree=sum(5**r for r in rank_ports)),scalar_quotients=scalar_results,whole_graphs_generated=0,BFS_runs=0,parameter_sweep=False,CPU_seconds=time.process_time()-start)
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

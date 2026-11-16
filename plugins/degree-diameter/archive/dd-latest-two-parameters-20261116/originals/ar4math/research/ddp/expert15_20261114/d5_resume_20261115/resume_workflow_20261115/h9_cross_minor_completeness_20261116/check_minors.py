import time,resource
resource.setrlimit(resource.RLIMIT_CPU,(2,2));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
from pathlib import Path
import json,itertools
import sympy as S
P=Path(__file__).resolve().parent
start=time.monotonic()
x=S.symbols('u0 u1 u2 s v0 v1 v2')
def cross(a,b):return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def C(p,q):
 u,s,v=p[:3],p[3],p[4:];U,t,V=q[:3],q[3],q[4:];a=cross(v,V);b=cross(u,U)
 return[s*U[i]-t*u[i]+a[i]for i in range(3)]+[sum(u[i]*V[i]-v[i]*U[i]for i in range(3))]+[t*v[i]-s*V[i]+b[i]for i in range(3)]
cols=[C(x,[int(i==j)for i in range(7)])for j in range(7)]
A=[[cols[j][i]for j in range(7)]for i in range(7)]
checks=[]
for i in range(3):
 j=(i+1)%3;k=(i+2)%3
 for kind,rows,columns,coordinate in [('u',[i,3,4+j,4+k],[3,4+i,k,j],x[i]),('v',[4+i,3,j,k],[3,i,4+k,4+j],x[4+i])]:
  m=[[A[r][c]for c in columns]for r in rows];det=0
  for perm in itertools.permutations(range(4)):
   term=(-1)**sum(perm[a]>perm[b]for a in range(4)for b in range(a+1,4))
   for r,c in enumerate(perm):term*=m[r][c]
   det+=term
  det=S.expand(det);poly=S.Poly(det-coordinate**4,*x)
  checks.append(dict(kind=kind,index=i,rows=rows,columns=columns,matrix=[[str(z)for z in r]for r in m],determinant=str(det),expected=str(coordinate**4),integer_polynomial_zero=poly.is_zero))
r=dict(status='ALL_SIX_INTEGER_MINOR_IDENTITIES_PASS'if all(z['integer_polynomial_zero']for z in checks)else 'FIRST_FIXED_MINOR_FORMULA_FAIL',checks=checks,whole_CPU=time.process_time(),wall_seconds=time.monotonic()-start,coefficient_ring='Z exact, no reduction or sampling',new_cache_checks=0,BFS=0,SAT=0,Lean=0,new_graphs=0)
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))

import time,resource
resource.setrlimit(resource.RLIMIT_CPU,(4,4))
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
from pathlib import Path
import json
import sympy as S
P=Path(__file__).resolve().parent
start=time.monotonic()
x=S.symbols('x0:7');y=S.symbols('y0:7');vars=x+y
def dot(a,b):return sum(u*v for u,v in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def C(p,q):
 u,s,v=p[:3],p[3],p[4:];U,t,V=q[:3],q[3],q[4:];a=cross(v,V);b=cross(u,U)
 return [s*U[i]-t*u[i]+a[i]for i in range(3)]+[dot(u,V)-dot(v,U)]+[t*v[i]-s*V[i]+b[i]for i in range(3)]
def Q(p):return dot(p[:3],p[4:])-p[3]**2
def beta(p,q):return dot(p[:3],q[4:])+dot(q[:3],p[4:])-2*p[3]*q[3]
c=C(x,y);cc=C(x,c)
checks={}
checks.update({'square_'+str(i):cc[i]+beta(x,y)*x[i]+Q(x)*y[i]for i in range(7)})
checks['norm']=Q(c)-Q(x)*Q(y)+beta(x,y)**2
checks.update({'skew_'+str(i):c[i]+C(y,x)[i]for i in range(7)})
checks['beta_p_cross']=beta(x,c);checks['beta_q_cross']=beta(y,c)
def gr(i,j):return x[i]*y[j]-x[j]*y[i]
T=[gr(3,0)-gr(6,5),gr(3,1)-gr(4,6),gr(3,2)-gr(5,4),gr(1,2)-gr(3,4),gr(2,0)-gr(3,5),gr(0,1)-gr(3,6)]
for i,j in enumerate([0,1,2,4,5,6]):checks['Tits_'+str(i)]=c[j]-T[i]
results=[]
for name,e in checks.items():
 z=S.Poly(S.expand(e),*vars,modulus=3)
 results.append(dict(identity=name,zero=z.is_zero,degree=int(z.total_degree())if not z.is_zero else 0,nonzero_terms=[(list(m),int(k))for m,k in z.terms()if k]))
r=dict(status='ALL_UNIVERSAL_POLYNOMIAL_IDENTITIES_PASS'if all(t['zero']for t in results)else 'COUNTEREXAMPLE_POLYNOMIAL',identities=results,coefficient_field='F3 exact, hence every characteristic3 field',whole_CPU=time.process_time(),wall_seconds=time.monotonic()-start,small_actual_pair_checks=0,new_graphs=0,BFS=0,SAT=0,Lean=0)
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))

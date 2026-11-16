from pathlib import Path
import sympy as S
import time,json
P=Path(__file__).resolve().parent;AR=P.parents[5];start=time.process_time()
x=S.symbols('x0:7');y=S.symbols('y0:7');variables=x+y
def dot(a,b):return sum(u*v for u,v in zip(a,b))
def cr(a,b):return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def C(p,q):
 a=cr(p[4:],q[4:]);b=cr(p[:3],q[:3]);return[p[3]*q[i]-q[3]*p[i]+a[i]for i in range(3)]+[dot(p[:3],q[4:])-dot(p[4:],q[:3])]+[q[3]*p[4+i]-p[3]*q[4+i]+b[i]for i in range(3)]
def Q(p):return dot(p[:3],p[4:])-p[3]**2
def beta(p,q):return dot(p[:3],q[4:])+dot(q[:3],p[4:])-2*p[3]*q[3]
names=[f'(p {i})'for i in range(7)]+[f'(q {i})'for i in range(7)]
def leanpoly(expr,divide=1):
 poly=S.Poly(S.expand(expr),*variables);terms=[]
 for mon,coeff in poly.terms():
  if not coeff:continue
  assert int(coeff)%divide==0
  k=int(coeff)//divide;parts=[str(abs(k))]if abs(k)!=1 or not any(mon)else[]
  parts += [s if n==1 else f'{s} ^ {n}'for s,n in zip(names,mon)if n]
  term=' * '.join(parts)or'1';terms.append((' - 'if k<0 else' + ')+term)
 if not terms:return '0'
 t=''.join(terms);return ('-'if t.startswith(' - ')else'')+t[3:]
out=['import Mathlib.Tactic.Ring','import Mathlib.Data.Fin.VecNotation','import Mathlib.Tactic.FinCases','','/-! Exact universal characteristic-three cross identities. No graph diameter premise. -/','namespace DegreeDiameter.Portfolio.H9CrossRouting','variable {K : Type*} [CommRing K]','abbrev Vec7 (K : Type*) := Fin 7 → K', 'def norm (p : Vec7 K) : K := '+leanpoly(Q(x)), 'def polar (p q : Vec7 K) : K := '+leanpoly(beta(x,y)), 'def cross (p q : Vec7 K) : Vec7 K := !['+', '.join(leanpoly(z)for z in C(x,y))+']','']
cert=[]
def theorem(name,lhs,rhs,expr):
 quotient=leanpoly(expr,3);cert.append({'name':name,'integer_quotient_by_three':str(S.expand(expr)/3),'quotient_lean':quotient})
 out.extend([f'theorem {name} (h3 : (3 : K) = 0) (p q : Vec7 K) :',f'    {lhs} = {rhs} := by',f'  have h : {lhs} - ({rhs}) = (3 : K) * ({quotient}) := by','    simp [cross, norm, polar] <;> ring','  apply sub_eq_zero.mp','  rw [h, h3, zero_mul]',''])
cc=C(x,C(x,y));cross=C(x,y)
for i in range(7):theorem('square_'+str(i),f'cross p (cross p q) {i}',f'-(polar p q) * p {i} - norm p * q {i}',cc[i]+beta(x,y)*x[i]+Q(x)*y[i])
theorem('norm_cross','norm (cross p q)','norm p * norm q - (polar p q) ^ 2',Q(cross)-Q(x)*Q(y)+beta(x,y)**2)
for i in range(7):theorem('skew_'+str(i),f'cross q p {i}',f'-(cross p q {i})',C(y,x)[i]+cross[i])
theorem('polar_left_cross','polar p (cross p q)','0',beta(x,cross))
theorem('polar_right_cross','polar q (cross p q)','0',beta(y,cross))
def gr(i,j):return x[i]*y[j]-x[j]*y[i]
T=[gr(3,0)-gr(6,5),gr(3,1)-gr(4,6),gr(3,2)-gr(5,4),gr(1,2)-gr(3,4),gr(2,0)-gr(3,5),gr(0,1)-gr(3,6)]
for i,j in enumerate([0,1,2,4,5,6]):theorem('tits_'+str(i),f'cross p q {j}',leanpoly(T[i]),cross[j]-T[i])
out += ['theorem square (h3 : (3 : K) = 0) (p q : Vec7 K) :','    cross p (cross p q) = fun i => -(polar p q) * p i - norm p * q i := by','  funext i','  fin_cases i']
for i in range(7):out.append(f'  · exact square_{i} h3 p q')
out+=['','theorem skew (h3 : (3 : K) = 0) (p q : Vec7 K) :','    cross q p = -(cross p q) := by','  funext i','  fin_cases i']
for i in range(7):out.append(f'  · exact skew_{i} h3 p q')
out+=['','theorem null_polar_cross_witness (h3 : (3 : K) = 0) (p q : Vec7 K)','    (hp : norm p = 0) (hq : norm q = 0) (hb : polar p q = 0) :','    norm (cross p q) = 0 ∧ cross p (cross p q) = 0 := by','  constructor','  · rw [norm_cross h3, hp, hq, hb]; ring','  · rw [square h3]; funext i; simp [hp, hb]','','end DegreeDiameter.Portfolio.H9CrossRouting','','#print axioms DegreeDiameter.Portfolio.H9CrossRouting.square','#print axioms DegreeDiameter.Portfolio.H9CrossRouting.norm_cross','#print axioms DegreeDiameter.Portfolio.H9CrossRouting.skew','#print axioms DegreeDiameter.Portfolio.H9CrossRouting.null_polar_cross_witness']
extra=P/'COMMON_NEIGHBOR_PACKAGING.lean.txt'
if extra.exists():
 at=out.index('end DegreeDiameter.Portfolio.H9CrossRouting');out[at:at]=extra.read_text().splitlines()
 out.append('#print axioms DegreeDiameter.Portfolio.H9CrossRouting.null_polar_common_neighbor')
target=AR/'formal/DegreeDiameter/Portfolio/H9CrossRouting.lean';target.write_text('\n'.join(out)+'\n');(P/'INTEGER_CERTIFICATES.json').write_text(json.dumps(cert,indent=2)+'\n');(P/'GENERATION_RESULT.json').write_text(json.dumps({'identities':len(cert),'target':str(target),'CPU':time.process_time()-start,'assumptions':'CommRing K and explicit (3:K)=0 only; no graph diameter'},indent=2)+'\n');print(target)

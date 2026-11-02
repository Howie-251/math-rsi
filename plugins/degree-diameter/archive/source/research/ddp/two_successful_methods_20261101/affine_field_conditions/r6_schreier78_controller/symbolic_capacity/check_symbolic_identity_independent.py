"""Independent symbolic matrix/support and six Gaussian algebra cases only.
No voltage-profile search, controller/fiber generation, BFS, solver or Lean.
"""
from pathlib import Path
from itertools import product
import csv,json,time
HERE=Path(__file__).resolve().parent
start=time.process_time()
zero=(0,0,0,0,0,0)
def e(i,sign=1):return tuple(sign if j==i else 0 for j in range(6))
def plus(a,b):return tuple(a[i]+b[i] if i<5 else (a[i]+b[i])%2 for i in range(6))
def support_product(a,b):return {plus(x,y) for x in a for y in b}
A,B,C,S,T,H=[e(i) for i in range(6)]
Am,Bm,Cm,Sm,Tm=[e(i,-1) for i in range(5)]
# Directly from the six port rules, with 2h=0 only. No old word table imported.
K=[[{A,Am},{zero,S},{zero,T}],
   [{zero,Sm},{H},{zero,B,Cm}],
   [{zero,Tm},{zero,C,Bm},{H}]]
K3=[[set() for _ in range(3)] for _ in range(3)]
for i,j,k,l in product(range(3),repeat=4):
 K3[i][j]|=support_product(support_product(K[i][k],K[k][l]),K[l][j])
counts=[[len(K3[i][j]) for j in range(3)] for i in range(3)]
assert counts==[[40,46,46],[46,38,36],[46,36,38]],counts
F=K3[1][2]
R={zero,Sm,T,plus(Sm,T)}
U={zero,B,Cm}
Qpairs=[(0,0),(2,0),(0,-2),(1,0),(0,-1),(1,-1),(0,1),(2,1),(1,1),(-1,0),(-1,-2),(-1,-1)]
Q={ (b,c) for b,c in Qpairs }
Qforms={(0,b,c,0,0,0) for b,c in Q}
blocks=[support_product({A,Am},R),support_product({H},R),support_product(U,{S,Sm,T,Tm}),Qforms]
assert list(map(len,blocks))==[8,4,12,12]
assert sum(map(len,blocks))==len(set.union(*blocks))==36
assert set.union(*blocks)==F
with (HERE/'DISTINCT_1_TO_2_FORMS.tsv').open() as f:
 old={tuple(int(row[k]) for k in ['alpha0','alpha1','alpha2','sigma','tau','half']) for row in csv.DictReader(f,delimiter='\t')}
assert F==old
sums=[sum(v[i] for v in F) for i in range(6)]
gram=[[sum(v[i]*v[j] for v in F)%4 for j in range(5)] for i in range(5)]
assert sums==[0,8,-8,-6,6,4],sums
assert gram==[[0,0,0,0,0],[0,2,1,0,0],[0,1,2,0,0],[0,0,0,0,1],[0,0,0,1,0]],gram
# Check Q=(1+x+y^-1)^2(1+x^-1+y)-4(1+x+y^-1)
#         -(x/y+xy+1/(xy)) as an exact Laurent coefficient identity.
def poly_product(p,q):
 r={}
 for (a,b),c in p.items():
  for (d,e),f in q.items():r[a+d,b+e]=r.get((a+d,b+e),0)+c*f
 return r
u={(0,0):1,(1,0):1,(0,-1):1};v={(0,0):1,(-1,0):1,(0,1):1}
poly=poly_product(poly_product(u,u),v)
for key,c in u.items():poly[key]-=4*c
for key in [(1,-1),(1,1),(-1,-1)]:poly[key]-=1
assert {k:c for k,c in poly.items() if c}=={key:1 for key in Q}
# Six algebraic cases up to complex conjugation. All Gaussian arithmetic exact.
def ga(a,b):return(a[0]+b[0],a[1]+b[1])
def gm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def neg(a):return(-a[0],-a[1])
def power(a,n):
 if n<0:a=(a[0],-a[1]);n=-n
 out=(1,0)
 for _ in range(n):out=gm(out,a)
 return out
one=(1,0);minus=(-1,0);I=(0,1);minusI=(0,-1)
cases=[('x=±i,y=1',I,one),('x=±i,y=-1',I,minus),
       ('x=1,y=±i',one,I),('x=-1,y=±i',minus,I),
       ('x=y=±i',I,I),('x=-y=±i',I,minusI)]
table=[]
for label,x,y in cases:
 uvalue=ga(ga(one,x),power(y,-1));qvalue=(0,0)
 for b,c in Q:qvalue=ga(qvalue,gm(power(x,b),power(y,c)))
 assert qvalue[0]%2==qvalue[1]%2==0
 half=(qvalue[0]//2,qvalue[1]//2)
 difference=ga(half,neg(uvalue));summation=ga(half,uvalue)
 assert difference!=(0,0)
 assert summation==(0,0) or abs(summation[0])!=abs(summation[1])
 table.append({'case':label,'representative_x':x,'representative_y':y,'U':uvalue,'Q_over2':half,'Q_over2_minus_U':difference,'Q_over2_plus_U':summation})
result={'status':'PASS_INDEPENDENT_SHORT_GAUSSIAN_CHARACTER_OBSTRUCTION',
 'rule_read_from':'explicit six-port equations in parent PROOF.md, K matrix transcribed independently',
 'symbolic_method':'support of nine entries of K^3 over Laurent exponents with only half coefficient mod2',
 'base_pair_counts':counts,'F12_symbolic_support':36,'saved36forms_exact_match':True,
 'disjoint_block_sizes':[8,4,12,12],'sum_coefficients':sums,'Gram_mod4_first_five':gram,
 'Q_Laurent_identity':True,'Gaussian_cases_up_to_conjugation':table,
 'm36_half_mod4':2,'m36_balance_required':[9,9,9,9],
 'paper_implication':'sum forces T-S odd; square sum forces B,C not both even; character at i nonzero in all six root cases, contradicts uniformmod4',
 'conclusion':'even m<=34,controllerorder3m<=102 when this fixed six-port topology has complete A^3 coverage',
 'not_claimed':'No upper bound for general degree6 diameter3 or other topology; not controllerD<=3 alone; no global degree54/55 bound.',
 'profile_searches':0,'controller_fiber_BFS_solver_Lean_runs':0,
 'CPU_seconds_measured_executable_batch':time.process_time()-start,'CPU_budget_seconds':10,'all_jobs_terminal':True}
assert result['CPU_seconds_measured_executable_batch']<10
(HERE/'INDEPENDENT_PAPER_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','base_pair_counts','F12_symbolic_support','CPU_seconds_measured_executable_batch','profile_searches']},ensure_ascii=False))

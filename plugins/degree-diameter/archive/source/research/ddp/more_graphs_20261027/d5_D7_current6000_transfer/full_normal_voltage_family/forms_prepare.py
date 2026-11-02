import json,subprocess,time,resource
from pathlib import Path
OUT=Path(__file__).resolve().parent
start=time.process_time();children0=resource.getrusage(resource.RUSAGE_CHILDREN)
add=[[((a%3+b%3)%3)+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
mul=[[((a%3*(b%3)+2*(a//3)*(b//3))%3)+3*((a%3*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)]
neg=[next(b for b in range(9) if add[a][b]==0) for a in range(9)]
def mm(A,B):return tuple(add[mul[A[2*i]][B[j]]][mul[A[2*i+1]][B[2+j]]] for i in range(2) for j in range(2))
def mp(A,n):
 r=(1,0,0,1)
 for _ in range(n):r=mm(r,A)
 return r
def hm(h,k):
 u,v=h%3,h//3;a,b=k%3,k//3
 return (u+(-a if v%2 else a))%3+3*((v+b)%8)
def hi(h):
 u,v=h%3,h//3
 return (-(-1 if v%2 else 1)*u)%3+3*((-v)%8)
def qmul(q,r):
 z,h=q%5,q//5;zz,hh=r%5,r//5
 return (z+pow(2,h//3,5)*zz)%5+5*hm(h,hh)
def qi(q):
 z,h=q%5,q//5;H=hi(h)
 return -pow(2,H//3,5)*z%5+5*H
def packed(M):return sum(x<<(4*i) for i,x in enumerate(M))
def rm(R,M):return tuple(add[mul[R[2*i]][M[j]]][mul[R[2*i+1]][M[6+j]]] for i in range(2) for j in range(6))
I=(1,0,0,1);B=(0,2,1,2);K=(1,2,0,2)
# IDs match the actual producer: E0,A1/2,B3/4,Y5/6,D7/8.
rev=[0,2,1,4,3,6,5,8,7]
ports=[[(1,0),(1,1),(1,3),(0,5),(0,6)],[(0,0),(0,2),(0,4),(1,7),(1,8)]]
qpos={0:0,1:1+5*(1+3*4),3:4+5*(1+3*7),5:5*3,7:4+5*(1+3*4)}
qd=[0]*9
for d,q in qpos.items():qd[d]=q;qd[rev[d]]=qi(q)
models=[];lines=['2']+[' '.join(map(str,row)) for row in add]
for scalar in [4,8]:
 A=tuple(mul[scalar][x] for x in K)
 assert mp(A,8)==mp(B,3)==I and mm(A,B)==mm(mp(B,2),A)
 rho=[mm(mp(B,u),mp(A,v)) for v in range(8) for u in range(3)]
 R=[(0,)*12 for _ in range(9)]
 for d,j in [(1,0),(3,2),(7,4)]:
  M=[0]*12;M[j]=M[6+j+1]=1;R[d]=tuple(M)
  R[rev[d]]=tuple(neg[x] for x in rm(rho[hi(qd[d]//5)],R[d]))
  back=rm(rho[qd[d]//5],R[rev[d]])
  assert all(add[a][b]==0 for a,b in zip(R[d],back))
 lines.append(str(scalar))
 for base in range(2):
  for q in range(120):
   for target,d in ports[base]:
    qto=qmul(q,qd[d]);shift=packed(rm(rho[q//5],R[d]))
    lines.append(f'{d} {120*target+qto} {shift}')
 models.append({'scalar':scalar,'alpha':list(A),'beta':list(B),'quotient_darts':qd,'positive_coefficient_matrices':{'A':R[1],'B':R[3],'D':R[7]},'inverse_coefficient_cancellation':True})
(OUT/'FORMS_INPUT.txt').write_text('\n'.join(lines)+'\n')
meta={'field':{'q':9,'characteristic':3,'encoding':'a+3b, t^2=-1','add':add,'mul':mul,'neg':neg},'models':models,'inverse_dart_ids':rev,'base_ports':ports,'slot_encoding':'slot=rootbase*240+targetbase*120+q; q=z+5h; h=u+3v','input_variables':['VAx','VAy','VBx','VBy','VDx','VDy'],'coefficients':'rowmajor 2x6, packed 12 nibbles in uint64; field labels, not arithmetic mod9','input':'FORMS_INPUT.txt','parameter_evaluations':0,'graph_generation':0,'BFS':0}
(OUT/'FORMS_INPUT_META.json').write_text(json.dumps(meta,indent=2)+'\n')
subprocess.run(['g++','-O2','-std=c++17',str(OUT/'forms_export.cpp'),'-o',str(OUT/'forms_export')],check=True)
subprocess.run([str(OUT/'forms_export'),str(OUT/'FORMS_INPUT.txt'),str(OUT)],check=True)
result=json.loads((OUT/'FORMS_EXPORT_RESULT.json').read_text())
children=resource.getrusage(resource.RUSAGE_CHILDREN)
result['compile_prepare_export_CPU_seconds']=(time.process_time()-start)+(children.ru_utime-children0.ru_utime)+(children.ru_stime-children0.ru_stime)
result['field_tables']='FORMS_INPUT_META.json'
(OUT/'FORMS_EXPORT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'FORMS_TERMINAL.json').write_text(json.dumps({'status':result['status'],'running':False,'pending':[],'result':'FORMS_EXPORT_RESULT.json','parameter_evaluations':0,'graphs':0,'BFS':0},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='models'}))

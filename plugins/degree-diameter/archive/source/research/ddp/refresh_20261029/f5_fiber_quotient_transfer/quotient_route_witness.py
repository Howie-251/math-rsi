#!/usr/bin/env python3
"""Only the unique saved translation and one cached controller witness."""
import json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
P=json.loads((HERE.parent/'f5_full_d20_D3/PARAMETERS.json').read_text())
C,T,D,rev=P['controller'],P['matrices'],P['directions'],P['inverse_ports']
K=json.loads((HERE/'TRANSLATION_SYSTEM.json').read_text())['nullspace_basis']
assert len(K)==1
h=K[0][:3];assert h==[0,3,1] and all(K[0][3*a:3*a+3]==h for a in range(30))
pi=[[1,0,0],[0,1,2]]
def mv(A,x):return [sum(a*b for a,b in zip(row,x))%5 for row in A]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col))%5 for col in zip(*B)] for row in A]
def rank(A):
 A=[r[:] for r in A];k=0
 for j in range(len(A[0])):
  i=next((i for i in range(k,len(A)) if A[i][j]),None)
  if i is None:continue
  A[k],A[i]=A[i],A[k];t=pow(A[k][j],-1,5);A[k]=[x*t%5 for x in A[k]]
  for i in range(len(A)):
   if i!=k:
    t=A[i][j];A[i]=[(x-t*y)%5 for x,y in zip(A[i],A[k])]
  k+=1
  if k==len(A):break
 return k
shifts=[];port_ranks=[];relations=[]
for p in range(4):
 d=D[rev[p]];delta=[(a-b)%5 for a,b in zip(mv(T[p],h),h)]
 alpha=next(t for t in range(5) if [t*x%5 for x in d]==delta)
 shifts.append(alpha)
 # Full quotient port rank; no representative shortcut.
 port_ranks.append(rank([h,mv(T[p],h),d])-1)
 assert rank([h,d])==2
 # section(u,v)=(u,v,0); coefficients of its projected relation.
 relations.append(dict(port=p,linear=mm(pi,[r[:2] for r in T[p]]),noise=mv(pi,d)))
N=json.loads((HERE.parents[1]/'breadth_20261027_wave4/mizuno_d3_source/controller_structure.json').read_text())['NB3_counts']
a,b=0,3;ports=[2,0,2];vertices=[0]
for p in ports:vertices.append(C[vertices[-1]][p])
assert vertices==[0,2,1,3] and N[a][b]==1
assert a!=b and b not in C[a] and not set(C[a]).intersection(C[b])
cols=[mv(T[2],mv(T[0],D[rev[2]])),mv(T[2],D[rev[0]]),D[rev[2]]]
noise=[list(r) for r in zip(*cols)];projected=mm(pi,noise)
assert rank(noise)==3 and rank(projected)==2
result=dict(status='FIXED_TRANSLATION_QUOTIENT_AND_CACHED_COVER_BOUND_PROVED',h=h,projection_matrix=pi,
 T_h_minus_h_noise_coefficients=shifts,quotient=dict(n=750,degree=20,diameter=3,port_ranks=port_ranks,ordinary_cover_sheets=5,explicit_port_relations=relations),
 cached_witness=dict(controller_root=0,controller_target=3,controller_vertices=vertices,ports=ports,cached_NB3_count=1,no_shorter_controller_path=True,full_noise_matrix=noise,full_noise_rank=3,projected_noise_matrix=projected,projected_noise_rank=2,words_to_each_of25_target_points=5),
 ordinary_cover_D3_sheet_bound=5,scope='Only covers of this exact750 quotient, not other voltage/controller changes',new_path_enumerations=0,new_graphs=0,BFS_runs=0,CPU_seconds=time.process_time()-start)
(HERE/'QUOTIENT_AND_COVER_WITNESS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

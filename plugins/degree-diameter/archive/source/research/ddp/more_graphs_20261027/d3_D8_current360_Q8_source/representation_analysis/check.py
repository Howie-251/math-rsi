"""Only144 small action checks; no words, graphs or BFS."""
import json,time
from pathlib import Path
D=Path(__file__).resolve().parent
start=time.process_time()
raw=json.loads((D.parent/'AUTHOR_construction.json').read_text())
source=raw["construction"]["group"]["matrices"]
names=raw["construction"]["group"]["names"]
def mm(A,B,q):return [[sum(A[i][k]*B[k][j] for k in range(2))%q for j in range(2)] for i in range(2)]
def mv(A,v,q):return tuple(sum(A[i][j]*v[j] for j in range(2))%q for i in range(2))
def neg(A,q):return [[-x%q for x in row] for row in A]
def mats(q,u,v):
 I=[[1,0],[0,1]];i=[[0,1],[q-1,0]];j=[[u,v],[v,-u%q]];k=mm(i,j,q)
 return [I,i,j,k,neg(I,q),neg(i,q),neg(j,q),neg(k,q)]
assert source==mats(3,1,1)
table3=[[source.index(mm(x,y,3)) for y in source] for x in source]
e1=(1,0)
source_orbit={mv(A,e1,3):h for h,A in enumerate(source)}
assert len(source_orbit)==8
models=[]
for q,u,v,diam,bound in [(5,0,2,9,600),(7,2,3,10,1250)]:
 A=mats(q,u,v)
 assert len({str(x) for x in A})==8
 assert mm(A[1],A[1],q)==A[4] and mm(A[2],A[2],q)==A[4]
 assert mm(A[1],A[2],q)==A[3] and mm(A[2],A[1],q)==A[7]
 assert [[A.index(mm(x,y,q)) for y in A] for x in A]==table3
 lookup={(0,0):(0,0)}
 lookup.update({v:mv(A[h],e1,q) for v,h in source_orbit.items()})
 eqchecks=0;inversechecks=0
 for h in range(8):
  hi=table3[h].index(0)
  for sv,tv in lookup.items():
   assert lookup[mv(source[h],sv,3)]==mv(A[h],tv,q)
   assert lookup[tuple(-x%3 for x in sv)]==tuple(-x%q for x in tv)
   oldinv=tuple(-x%3 for x in mv(source[hi],sv,3))
   newinv=tuple(-x%q for x in mv(A[hi],tv,q))
   assert lookup[oldinv]==newinv
   eqchecks+=1;inversechecks+=1
 semi=[[1,0],[u,v],[0,q-1]]
 delta=(1-u+v)%q
 assert delta
 model={
 "q":q,"u":u,"v":v,"target_n":40*q*q,"target_D":diam,"savedL":bound,
 "matrices":A,"names":names,"abstract_Q8_mul_table":table3,
 "source_to_target_vector_lookup":[{"source":list(sv),"Q8_name":None if sv==(0,0) else names[source_orbit[sv]],"target":list(tv)} for sv,tv in sorted(lookup.items())],
 "links":[[0,2,[0,0],"1"],[0,3,[0,0],"1"],[0,4,[0,0],"1"],[1,4,[0,0],"1"],[1,2,[0,0],"-i"],[1,3,[0,1],"-j"]],
 "semi_edges":[[2,semi[0],"-1"],[3,semi[1],"-1"],[4,semi[2],"-1"]],
 "semi_difference_determinant":delta,"connected_by_voltage_generation":True,
 "action_equivariance_checks":eqchecks,"fresh_inverse_consistency_checks":inversechecks,
 "individual_order4_elements_split":q%4==1,
 "full_Q8_absolutely_irreducible":True,
 "nonzero_vector_Q8_orbits":(q*q-1)//8,
 "graph_generated":False,"wordscan_run":False,"BFS_run":False}
 models.append(model)
out={"status":"VALID_TWO_FROZEN_REPRESENTATIONS_AND_SOURCE_TORSOR_BINDING","source_p":3,"source_basis_change":"identity: literalsource is already standardi/j","models":models,"native_or_python_CPU_seconds":time.process_time()-start,"new_graphs":0,"BFS":0,"wordscan":0,"solver":0}
(D/"TARGET_CONTROLS.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":out["status"],"models":[{"q":m["q"],"semi":m["semi_edges"],"det":m["semi_difference_determinant"],"actionchecks":m["action_equivariance_checks"]} for m in models],"CPU":out["native_or_python_CPU_seconds"]}))

"""Only the new Redei15 PGL3(F3) mask orbit; reuse old coefficient indexing."""
from pathlib import Path
import importlib.util,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];start=time.process_time()
old=ROOT/'research/ddp/more_graphs_20261027/h9_baer_plane_pool'
shape=json.load(open(P.parent/'SHAPE.json'))
assert json.load(open(P/'PREDICTION.json'))['frozen_before_orbit_and_plane_pool']
coeff=[tuple(v)for v in json.load(open(old/'orbit.json'))['coefficient_points_PG2F9']]
idx={v:j for j,v in enumerate(coeff)}
spec=importlib.util.spec_from_file_location('old_h9_geometry',ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature/geometry.py');geom=importlib.util.module_from_spec(spec);spec.loader.exec_module(geom)
A=[[((x%3+y%3)%3)+3*((x//3+y//3)%3)for y in range(9)]for x in range(9)]
M=[[((x%3)*(y%3)+2*(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)for y in range(9)]for x in range(9)]
assert A==geom.ADD and M==geom.MUL and M[3][3]==2
I=geom.INV

def norm(v):
 s=I[next(x for x in v if x)];return tuple(M[s][x]for x in v)
def power(x,k):
 v=1
 for _ in range(k):v=M[v][x]
 return v
points={tuple(x)for x in shape['raw_points']}
assert len(points)==15 and all((1,x,power(x,5))in points for x in range(9))
perms=[]
for gi in range(3):
 perm=[]
 for x,y,z in coeff:
  q=(y,z,x)if gi==0 else(A[x][y],y,z)if gi==1 else(M[2][x],y,z)
  perm.append(idx[norm(q)])
 assert len(set(perm))==91;perms.append(perm)
initial=sum(1<<idx[v]for v in points)
orbit=[initial];which={initial:0};parents=[-1];gens=[-1];members=[]
for at,mask in enumerate(orbit):
 ids=[j for j in range(91)if(mask>>j)&1];assert len(ids)==15;members.append(ids)
 for gi,perm in enumerate(perms):
  out=sum(1<<perm[j]for j in ids)
  if out not in which:
   which[out]=len(orbit);orbit.append(out);parents.append(at);gens.append(gi)
assert 5616%len(orbit)==0
field_fixed={j for j,v in enumerate(coeff)if all(x<3 for x in v)}
assert len(field_fixed)==13
assert all(sum(j in field_fixed for j in ids)==5 for ids in members)
data={'status':'COMPLETE_NEW_REDEI15_PGL3F3_MASK_ORBIT','orbit_size':len(orbit),'group':'PGL3(F3)','group_order':5616,'mask_stabilizer_order':5616//len(orbit),
 'raw_points_per_set':15,'Frobenius_fixed_points_per_set':5,'fully_unsplit_pins_per_set':10,
 'coefficient_points_PG2F9':[list(x)for x in coeff],'generator_matrices':[[[0,1,0],[0,0,1],[1,0,0]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]],
 'generator_permutations':perms,'parent':parents,'generator':gens,'point_indices15':members,
 'mask_words_u64_decimal':[[str(mask&((1<<64)-1)),str(mask>>64)]for mask in orbit],
 'F9_field_check':'All81 multiplication andaddition entries agreewith existinggeometry.py androotprobeformula;u²=−1,encodinga+3b.',
 'generator_proof':'Coordinatecycle conjugates the transvection tocyclic elementaryroots, commutators giveall elementaryroots overF3, generatingSL3(F3). Sincegcd(3,2)=1, itsprojectiveimage isallPGL3(F3); diag2isalso included.',
 'old_Baer_masks_read_or_enumerated':False,'CPU_seconds':time.process_time()-start}
(P/'orbit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('ORBIT',len(orbit),'stabilizer',5616//len(orbit),'CPU',data['CPU_seconds'])

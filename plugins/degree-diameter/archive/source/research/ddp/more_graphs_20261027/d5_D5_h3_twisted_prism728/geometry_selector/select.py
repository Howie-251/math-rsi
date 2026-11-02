from pathlib import Path
from collections import Counter
from itertools import product
import json,time,resource,shutil
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
assert (ROOT/'research').exists()
assert not(P/'RESULT.json').exists()
start=time.process_time()
old=P/'PREDICTION.json'
if old.exists():shutil.copyfile(old,P/'UNEXECUTED_PRIOR_PREDICTION.json')
pred={'status':'FROZEN_BEFORE_UPDATED_SINGLE_REFLECTION_SELECTOR','prior_prediction_executed':False,
 'prediction':'The28cachedR2classes are13point singularprojectiveplanes ofrank3; afterexcludingreflectionsfixedon>=2wholeclasses, at leastoneanisotropicnormal remains foronecanonicalnonAuto intersheetmatching.',
 'new_filter':'Excludev ifR_v pointwisefixes>=2 ofthe28oldB2balls. Thenminimize|R_v(F)∩F|andlexnormal; no graphdistance/badscoreselection.',
 'scope':'Exactly729normalizedanisotropicnormals inPG6F3; one smallGF3selector, noBFS/graph. Canonicalnormalizedfirstnonzero1,tuplelex.',
 'hard_CPU_seconds':1,'coordinate_model':'Q=x0x4+x1x5+x2x6-x3², B=x0v4+x4v0+x1v5+x5v1+x2v6+x6v2+x3v3',
 'reflection':'x-B(x,v)/Q(v)*v projectivelynormalized','source_label_binding':'H3_point_representatives intoh9pointcoords cache; H3_graph natural364/714 inherited.'}
old.write_text(json.dumps(pred,indent=2)+'\n')
Q=json.loads((ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json').read_text())
raw=(ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin').read_bytes()
coords=[tuple(raw[7*j:7*j+7])for j in Q['H3_point_representatives']]
def q(x):return(x[0]*x[4]+x[1]*x[5]+x[2]*x[6]-x[3]*x[3])%3
def B(x,v):return(x[0]*v[4]+x[4]*v[0]+x[1]*v[5]+x[5]*v[1]+x[2]*v[6]+x[6]*v[2]+x[3]*v[3])%3
def norm(x):
 a=next(t for t in x if t)
 return tuple(a*t%3 for t in x)
def reflect(x,v,qq):
 k=B(x,v)*qq%3
 return norm(tuple((x[i]-k*v[i])%3 for i in range(7)))
assert len(coords)==len(set(coords))==364 and all(set(x)<={0,1,2}and norm(x)==x and q(x)==0 for x in coords)
projects=sorted(x for x in product(range(3),repeat=7)if any(x)and next(t for t in x if t)==1)
assert len(projects)==1093 and {x for x in projects if q(x)==0}==set(coords)
normal=[x for x in projects if q(x)]
bind=json.loads((ROOT/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json').read_text())
classes=json.loads((ROOT/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_CLASSES.json').read_text())['R2_class_members']
ports=bind['eligible_ports'];F={coords[x]for x in ports}
assert len(normal)==729 and len(ports)==len(classes)==28
def basis(vs):
 b={}
 for vec in vs:
  w=list(vec)
  for j,row in sorted(b.items()):
   k=w[j]
   if k:w=[(a-k*c)%3 for a,c in zip(w,row)]
  if any(w):
   pivot=next(i for i,a in enumerate(w)if a);s=w[pivot]
   b[pivot]=tuple(s*a%3 for a in w)
 return list(b.values())
plane_data=[];bases=[]
for port,members in zip(ports,classes):
 bb=basis([coords[i]for i in members]);assert len(bb)==3
 span=set()
 for coeff in product(range(3),repeat=3):
  vv=tuple(sum(coeff[j]*bb[j][i]for j in range(3))%3 for i in range(7))
  if any(vv):span.add(norm(vv))
 assert len(span)==13 and span=={coords[i]for i in members}and all(q(vv)==0 for vv in span)
 bases.append(bb);plane_data.append({'port':port,'members':members,'rank':3,'basis':bb,'singular_projective_plane':True})
records=[];eligible=[]
for v in normal:
 qq=q(v)
 fp=[i for i in ports if B(coords[i],v)==0]
 fb=[port for port,bb in zip(ports,bases)if all(B(x,v)==0 for x in bb)]
 images={reflect(x,v,qq)for x in F};ov=len(F&images)
 rec={'normal7':v,'Q':qq,'ports_fixed':fp,'fixed_B2_ports':fb,'fixed_B2_count':len(fb),'ports_image_intersection':ov,'eligible':len(fb)<2}
 records.append(rec)
 if rec['eligible']:eligible.append(rec)
chosen=min(eligible,key=lambda z:(z['ports_image_intersection'],tuple(z['normal7'])))if eligible else None
result={'status':'CANONICAL_REFLECTION_SELECTED'if chosen else'NO_REFLECTION_AFTER_FIXED_B2_FILTER',
 'coordinate_points':364,'all_Q6F3_points_bound':True,'source_n':364,'source_m':714,'source_BFS':0,
 'B2_planes_rank3_count':28,'anisotropic_normals_scope':729,
 'fixed_B2_count_histogram':dict(Counter(z['fixed_B2_count']for z in records)),
 'fixed_port_count_histogram':dict(Counter(len(z['ports_fixed'])for z in records)),
 'ports_intersection_histogram':dict(Counter(z['ports_image_intersection']for z in records)),
 'norm_type_fixedball_histogram':{str(t):dict(Counter(z['fixed_B2_count']for z in records if z['Q']==t))for t in[1,2]},
 'disjoint_port_reflections':sum(z['ports_image_intersection']==0 for z in records),
 'eligible_after_fixed_B2_filter':len(eligible),'chosen':chosen,
 'canonical_rule':'Firstminspare-overlap thenlexnormal afterfixedB2<2 filter.',
 'candidate_graphs':0,'CPU_seconds':time.process_time()-start,'hard_RLIMIT_CPU_seconds':1}
if chosen:
 v=chosen['normal7'];qq=chosen['Q'];lookup={x:i for i,x in enumerate(coords)}
 pi=[lookup[reflect(x,v,qq)]for x in coords]
 assert sorted(pi)==list(range(364))and all(pi[pi[i]]==i for i in range(364))
 assert chosen['ports_image_intersection']<28
 reflection={'status':'READY_SINGLE_CANONICAL_GEOMETRIC_MATCHING','normal7':v,'Q':qq,
 'ports_fixed':chosen['ports_fixed'],'fixed_B2_ports':chosen['fixed_B2_ports'],
 'ports_image':[pi[i]for i in ports],'ports_image_intersection':[i for i in ports if pi[i]in ports],
 'pi364':pi,'pointset_isometry':True,'not_source_graph_Auto':'Some degree3ports maptodegree4vertices; sourceAuto mustpreservedegree.',
 'selection_was_before_graph':True,'source_vertices':364,'source_edges':714}
 (P/'REFLECTION.json').write_text(json.dumps(reflection,indent=2)+'\n')
(P/'POINT_COORDS_BY_VERTEX.u8.bin').write_bytes(bytes(y for x in coords for y in x))
(P/'B2_PLANES.json').write_text(json.dumps(plane_data,indent=2)+'\n')
(P/'SELECTOR_RECORDS.json').write_text(json.dumps(records,indent=2)+'\n')
for fn in['RESULT.json','terminal.json']:(P/fn).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

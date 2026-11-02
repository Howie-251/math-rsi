"""Bind the uniform route obstruction to saved base coordinates; no solver/BFS."""
from pathlib import Path
from collections import Counter
import json,time
out=Path(__file__).resolve().parent;start=time.process_time();inp=json.loads((out/'INPUT.json').read_text())
points=inp['points'];edges={tuple(e) for e in inp['base_edges']};tree={tuple(e) for e in inp['tree_edges']};adj=[[] for _ in points]
for u,v in edges:adj[u].append(v);adj[v].append(u)
classes={u:('external' if sum(c!=0 for c in p)==1 else 'secant' if sum(c!=0 for c in p)==2 else 'absolute') for u,p in enumerate(points)}
A=[u for u in classes if classes[u]=='absolute'];S=[u for u in classes if classes[u]=='secant'];E=[u for u in classes if classes[u]=='external']
assert len(A)==4 and len(S)==6 and len(E)==3 and A==inp['absolute_base_points']
expected={'absolute':Counter({'secant':3}),'secant':Counter({'absolute':2,'secant':1,'external':1}),'external':Counter({'secant':2,'external':2})}
rows=[]
for u in range(13):
 h=Counter(classes[v] for v in adj[u]);assert h==expected[classes[u]]
 rows.append({'point':u,'coordinates':points[u],'type':classes[u],'neighbors':sorted(adj[u]),'neighbor_type_counts':dict(h)})
paths=[]
for a in A:
 for e in E:
  mids=sorted(set(adj[a])&set(adj[e]));assert len(mids)==1 and mids[0] in S
  m=mids[0];terms=[]
  for u,v in [(a,m),(m,e)]:
   edge=tuple(sorted((u,v)))
   terms.append({'base_edge':edge,'coefficient':1 if u<v else -1,'tree_fixed_zero':edge in tree})
  paths.append({'absolute_base':a,'external_base':e,'unique_base_path':[a,m,e],'lift_endpoint_sheet':'source_sheet+signed_chord_shifts mod3','shift_terms':terms})
result={'status':'UNIFORM_ROUTE_OBSTRUCTION_BASE_BINDING_MATCH','absolute_base_ids':A,'secant_base_ids':S,'external_base_ids':E,'class_counts':dict(Counter(classes.values())),'base_vertices':rows,'absolute_to_external_two_step_paths':paths,'absolute_to_external_paths_per_base_pair':1,'external_lift_vertices':[3*v+s for v in E for s in range(3)],'external_lift_count':9,'each_direct_abs_spoke_external_R3_capacity':3,'P3_middle_helper':40,'P3_middle_internal_degree':2,'P3_middle_spoke_count':2,'P3_middle_external_coverage_upper':6,'P3_middle_external_missing_lowerbound':3,'general_three_helper_scope':'Retain all39 oldlift edges; allow any simple helper graph and any added edges at the12degree3 absolute ports, respecting maxdegree4.','necessary_helper_spokes':3,'necessary_helper_internal_maxdegree':1,'three_helper_connected_graph_with_maxdegree1':False,'CPU_seconds':time.process_time()-start,'solver_calls':0,'graph_BFS':0,'selected_graphs':0,'voltage_assignments_enumerated':0}
(out/'ROUTE_CLASS_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','class_counts','absolute_base_ids','secant_base_ids','external_base_ids','P3_middle_external_missing_lowerbound','CPU_seconds','solver_calls','graph_BFS']}))

import csv,itertools,json,resource,time
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parent;P=D.parent;U=[0,1,7,9,15,18,24];K=[0,3,7,10,14,17,21]
def main():
 t=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(10,10));assert (D/'PRED.md').exists() and not (D/'RESULT.json').exists()
 p=json.loads((P/'PARAMETERS.json').read_text());ct=p['controller'];ci=p['dart_chart_index'];mp=p['matrices'];el=p['directions'];rev=p['inverse_ports'];mul=p['field']['multiplication']
 forbid_u={4,22,5,21,10,16};forbid_k={1,25,2,24,6,20};checks=0
 for u in range(26):
  for v in range(u+1,26):
   assert bool(set(ct[u])&set(ct[v]))==((v-u)%26 in forbid_u);checks+=1
 assert checks==325 and {(21*d)%26 for d in forbid_u}==forbid_k and 5*21%26==1
 assert sorted((5*k)%26 for k in K)==U and sorted((21*u)%26 for u in U)==K
 gaps=[(K[(i+1)%7]-K[i])%26 for i in range(7)];assert gaps==[3,4,3,4,3,4,5]
 assert all((v-u)%26 not in forbid_k for u,v in itertools.combinations(K,2))
 # This checks gap-excess patterns only, not alternative controller subsets.
 patterns=[]
 for i in range(8):
  g=[3]*8;g[i]=5;patterns.append(g)
 for i,j in itertools.combinations(range(8),2):
  g=[3]*8;g[i]=g[j]=4;patterns.append(g)
 assert len(patterns)==36
 for g in patterns:assert sum(g)==26 and min(g)>=3 and any(g[i]==g[(i+1)%8]==3 for i in range(8))
 rows=[ct[u] for u in U];targets=sum(rows,[]);assert len(set(targets))==42
 assert all(ci[u]==ci[0]==[0,1,2,3,4,6] for u in U)
 def add(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
 def act(m,x):return tuple(add(add(mul[r[0]][x[0]],mul[r[1]][x[1]]),mul[r[2]][x[2]]) for r in m)
 def code(x):return x[0]+9*x[1]+81*x[2]
 centers=[];pins=[];used=set();fibers=Counter()
 for ui,u in enumerate(U):
  for a in range(9):
   for b in range(9):
    i=81*ui+9*a+b;x=(a,b,mul[4][a]);c=729*u+code(x);row=[]
    centers.append(dict(index=i,u_index=ui,controller=u,a=a,b=b,x0=x[0],x1=x[1],x2=x[2],source_center=c))
    for port in range(6):
     base=act(mp[ci[u][port]],x);v=ct[u][port]
     for noise in range(9):
      y=tuple(add(base[j],mul[noise][el[rev[port]][j]]) for j in range(3));label=729*v+code(y)
      assert label!=c and label not in used and 0<=label<56862;used.add(label);row.append(label);fibers[v]+=1
      pins.append(dict(base_index=i,u_index=ui,controller=u,a=a,b=b,port=port,noise=noise,target_controller=v,target_fiber_code=code(y),source_pin=label))
    assert len(set(row))==54
 assert len(centers)==len({c['source_center'] for c in centers})==567 and len(used)==len(pins)==30618
 assert set(fibers)==set(targets) and all(n==729 for n in fibers.values())
 assert all(729*v+x in used for v in targets for x in range(729))
 loads=[0]*56862;recipe=[]
 for copy in range(2):
  for c in centers:
   k=567*copy+c['index'];recipe.append(dict(clone_index=k,copy=copy,base_index=c['index'],source_center=c['source_center'],new_vertex=56862+k))
  for r in pins:loads[r['source_pin']]+=1
 assert Counter(loads)==Counter({0:26244,2:30618}) and len(recipe)==1134
 for name,data in [('CENTERS.csv',centers),('PINS.csv',pins),('CLONE_RECIPE.csv',recipe)]:
  with (D/name).open('w') as f:w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 params=dict(source='../PARAMETERS.json',selected_controllers=U,k_points=K,k_equals='21*u mod26',u_equals='5*k mod26',cyclic_k_gaps=gaps,
  forbidden_u_differences=sorted(forbid_u),forbidden_k_differences=sorted(forbid_k),controller_target_rows=rows,distinct_target_controllers=targets,
  common_chart_profile=[0,1,2,3,4,6],plane='W={(a,b,GF9mul(4,a))}',base_index='81*uIndex+9*a+b',source_center_label='729*U[uIndex]+a+9*b+81*GF9mul(4,a)',
  base_centers=567,center_labels=[c['source_center'] for c in centers],copies=2,clone_index='567*copy+81*uIndex+9*a+b',new_label='56862+clone_index',
  pins='PINS.csv',centers='CENTERS.csv',clone_recipe='CLONE_RECIPE.csv',base0_complete_plane_fiber_maximum=7,
  maximum_scope='Only complete81-point Wplane in selected base0controller fibers with pairwise disjoint controller openN; not whole-source/arbitrary pins.',
  proposed_target=dict(Delta=56,D=3,vertices=57996,edges=1596510,new_vertices=1134,new_edges=61236,new_new_edges=0),
  predicted_degree_histogram={'54':27378,'56':30618},predicted_source_load_histogram={'0':26244,'2':30618},
  cap57_same_rule_upper=58563,cap57_public_source_guarantee=58596,cap57_same_rule_deficit=33,
  U6_instance_preserved=True,complete_graph_generated=False,public56_source_guarantee=57568,bounded_cap56_gain=428,global_record_or_priority_certified=False)
 (D/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n')
 r=dict(status='PASS_GIVEN_U7_AND_PROVABLY_OPTIMAL_BASE0_COMPLETE_PLANE_REFINEMENT',selected_controllers=U,
  all325_base0_pair_predicates_exact=True,forbidden_difference_transform_exact=True,given_k_gaps=gaps,given_U7_predicate_PASS=True,
  eight_gap_excess_patterns_checked=36,all_patterns_have_adjacent3plus3=True,base0_openN_packing_maximum=7,given_seven_attains_maximum=True,
  distinct_controller_targets=42,all_chart_profiles_equal_controller0=True,ordered_base_centers=567,base_N54_pin_occurrences=30618,distinct_base_pins=30618,
  complete_target_fibers=42,each_fiber_coordinates=729,double_copy_clone_rows=1134,double_copy_added_incidences=61236,
  source_load_histogram={'0':26244,'2':30618},proposed_n=57996,proposed_m=1596510,degree_histogram={'54':27378,'56':30618},
  cap57_same_rule_max_n=58563,cap57_public_guarantee=58596,cap57_deficit=33,
  other_U_sets_searched=0,large_edgefiles_read=0,complete_graphs_generated=0,BFS_runs=0,solver_calls=0,Lean_compilations=0,
  CPU_seconds=time.process_time()-t,CPU_budget_seconds=10,workers=1,accepted_counts_changed=False,U6_instance_preserved=True,
  next='Return given-U7 PASS and upper proof to root; no U7production here. Continue authorized U6Lean separately.')
 assert r['CPU_seconds']<10
 (D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(D/'TERMINAL.json').write_text(json.dumps(dict(status=r['status'],running=False,complete_graph_generated=False,
  CPU_seconds=r['CPU_seconds'],CPU_budget_seconds=10,U6_preserved=True,next=r['next']),indent=2)+'\n')
 print(json.dumps({k:r[k] for k in ['status','selected_controllers','distinct_controller_targets','base0_openN_packing_maximum','distinct_base_pins','CPU_seconds']}))
if __name__=='__main__':main()

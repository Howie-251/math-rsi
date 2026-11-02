import csv,datetime,json,re,resource,time
from collections import Counter
from pathlib import Path

R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
D=Path(__file__).resolve().parent;P=D.parent
U=[0,1,2,3,9,15]

def main():
 t=time.process_time();wall=time.monotonic()
 resource.setrlimit(resource.RLIMIT_CPU,(10,10))
 assert (D/'PRED.md').exists() and not (D/'RESULT.json').exists(),'one fixed precheck only'
 p=json.loads((P/'PARAMETERS.json').read_text());ct=p['controller'];charts=p['dart_chart_index'];mats=p['matrices'];ell=p['directions'];rev=p['inverse_ports'];mul=p['field']['multiplication']
 assert p['order']==56862 and p['degree']==54 and p['expected_edges']==1535274
 source_formal=json.loads((P/'formalization/FINAL_COMPILE_RESULT.json').read_text())
 clone_formal=json.loads((P/'single_fiber_plane55_graph/formalization/FINAL_COMPILE_RESULT.json').read_text())
 assert 'KERNEL_COMPLETE' in source_formal['status'] and clone_formal['certificate_premises']==[]
 text=(R/'formal/DegreeDiameter/Portfolio/F9PlaneClone55Inputs.lean').read_text()
 inv_rhs=re.search(r'^def pinInverse .*? := (.+)$',text,re.M).group(1)
 pin_inverse=json.loads(re.sub(r'F\.c(\d)',r'\1',inv_rhs).replace('!',''))
 assert len(pin_inverse)==6
 def add(a,b):return (a%3+b%3)%3+3*((a//3+b//3)%3)
 def av(a,b):return tuple(add(x,y) for x,y in zip(a,b))
 def scale(a,x):return tuple(mul[a][v] for v in x)
 def act(m,x):return tuple(add(add(mul[r[0]][x[0]],mul[r[1]][x[1]]),mul[r[2]][x[2]]) for r in m)
 def code(x):return x[0]+9*x[1]+81*x[2]
 target_rows=[ct[u] for u in U];targets=[v for row in target_rows for v in row]
 assert len(set(targets))==36
 profile=charts[0];assert profile==[0,1,2,3,4,6] and all(charts[u]==profile for u in U)
 centers=[];pins=[];allpins=set();fiber_counts=Counter();inverse_checks=0
 for ui,u in enumerate(U):
  for a in range(9):
   for b in range(9):
    x=(a,b,mul[4][a]);index=81*ui+9*a+b;owner=729*u+code(x)
    c=dict(index=index,u_index=ui,controller=u,a=a,b=b,x0=x[0],x1=x[1],x2=x[2],source_center=owner)
    centers.append(c);row=set()
    for port in range(6):
     v=ct[u][port];base=act(mats[charts[u][port]],x)
     for noise in range(9):
      y=av(base,scale(noise,ell[rev[port]]));label=729*v+code(y)
      assert act(pin_inverse[port],y)==(a,b,noise)
      inverse_checks+=1;assert label!=owner and 0<=label<56862 and label not in row
      row.add(label);pins.append(dict(base_index=index,u_index=ui,controller=u,a=a,b=b,port=port,noise=noise,target_controller=v,target_fiber_code=code(y),source_pin=label))
      fiber_counts[v]+=1
    assert len(row)==54 and not (row&allpins)
    allpins.update(row)
 assert len(centers)==486 and len({c['source_center'] for c in centers})==486
 assert len(pins)==len(allpins)==26244 and set(fiber_counts)==set(targets)
 assert all(fiber_counts[v]==729 for v in targets)
 assert all(729*v+x in allpins for v in targets for x in range(729))
 load=[0]*56862;recipes=[]
 for copy in range(2):
  for c in centers:
   k=486*copy+c['index'];recipes.append(dict(clone_index=k,copy=copy,base_index=c['index'],source_center=c['source_center'],new_vertex=56862+k))
  for row in pins:load[row['source_pin']]+=1
 assert len(recipes)==972 and Counter(load)==Counter({0:30618,2:26244})
 center_labels={c['source_center'] for c in centers}
 induced_edges=sum(r['source_pin'] in center_labels for r in pins)//2
 assert induced_edges==162
 for name,rows in [('CENTERS.csv',centers),('PINS.csv',pins),('CLONE_RECIPE.csv',recipes)]:
  with (D/name).open('w') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 params=dict(source='../PARAMETERS.json',source_vertices=56862,source_edges=1535274,source_degree=54,
  source_concrete_theorem='DegreeDiameter.Portfolio.F9Graph56862.concrete_order_degree_and_exact_D3',
  source_regular_theorem='DegreeDiameter.Portfolio.F9Graph56862.degree_fifty_four',
  existing_plane_inverse_theorem='DegreeDiameter.Portfolio.F9PlaneClone55.pinInverse_left',
  field='GF3[w]/(w²+1),codea+3b',selected_controllers=U,controller_target_rows=target_rows,distinct_target_controllers=targets,
  controller_target_double_index_injective=True,common_chart_profile=profile,plane='W={(a,b,GF9mul(4,a))}',eta=4,
  base_center_order='uIndex outer0..5,a middle0..8,b inner0..8',base_index='81*uIndex+9*a+b',
  source_center_label='729*U[uIndex]+a+9*b+81*GF9mul(4,a)',base_centers=486,center_labels=[c['source_center'] for c in centers],
  pin_inverse_matrices_reused=pin_inverse,immutable_source_fullN_size=54,distinct_original_source_pins=26244,complete_target_fibers=36,
  center_induced_edges=induced_edges,center_independence_required=False,multiplicity=2,clone_index='486*copy+baseIndex,copyouter0..1',
  proposed_new_label='56862+cloneIndex',base_centers_csv='CENTERS.csv',immutable_pin_formula_rows_csv='PINS.csv',proposed_clone_recipe_csv='CLONE_RECIPE.csv',
  proposed_target=dict(Delta=56,D=3,vertices=57834,edges=1587762,new_vertices=972,new_edges=52488,old_edges_retained=1535274,new_new_edges=0),
  predicted_degree_histogram={'54':31590,'56':26244},whole_source_packing_optimality_claimed=False,
  complete_extension_graph_generated=False,source_edge_file_read=False,public_gate='ROOT_SEPARATE_PENDING_PRIMARY_CONFIRMATION')
 (D/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n')
 result=dict(status='PASS_FIXED_SIX_U_PLANE_PACKING_AND_DOUBLE_LOAD_INTERFACE',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  selected_controllers=U,all_selected_controllers_base0=True,controller_target_rows=target_rows,distinct_target_controllers=36,
  common_chart_profile_matches_controller0=True,base_centers_distinct=486,ordered_center_labels_checked=486,
  base_full_neighborhoods_checked=486,each_base_source_neighborhood_size=54,pin_inverse_readbacks= inverse_checks,
  total_base_pin_occurrences=26244,distinct_base_pins=26244,base_max_pin_load=1,complete_target_fibers=36,all_fiber_coordinate_coverage=729,
  double_copy_clone_rows=972,double_copy_incidence_count=52488,all_source_vertex_loads_checked=56862,source_load_histogram={'0':30618,'2':26244},maximum_source_load=2,
  source_center_induced_edges=induced_edges,center_independence_assumed=False,immutable_original_source_only=True,
  source_formula_and_D3_inherited=True,source_graph_literal_edges_read=0,complete_graphs_generated=0,BFS_runs=0,Lean_compilations=0,solver_calls=0,
  workers=1,CPU_seconds=time.process_time()-t,wall_seconds=time.monotonic()-wall,CPU_budget_seconds=10,
  accepted_counts_changed=False,public_gate='ROOT_SEPARATE_PENDING_PRIMARY_CONFIRMATION',next='Return to root; no production/public comparison or continuation authorized by this precheck.')
 assert result['CPU_seconds']<10
 (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 (D/'TERMINAL.json').write_text(json.dumps(dict(status='FIXED_SIX_FIBER_DOUBLE56_INTERFACE_COMPLETE_RETURN_TO_ROOT',running=False,finite_interface_PASS=True,
  complete_graph_generated=False,source_edgefile_read=False,BFS_runs=0,Lean_compilations=0,solver_calls=0,CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=10,
  public_gate_pending=True,accepted_counts_changed=False,next='Root separate public gate and explicit later production decision required; no extra search.'),indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','distinct_target_controllers','base_centers_distinct','distinct_base_pins','maximum_source_load','CPU_seconds']}))

if __name__=='__main__':main()

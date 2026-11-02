import collections,json,time
from pathlib import Path
START=time.process_time();D=Path(__file__).resolve().parent;PARENT=D.parent;ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
a=json.loads((PARENT/'f4_c60_plane_blocks/RECIPE_d21.json').read_text());b=json.loads((PARENT/'f4_c60_plane_blocks/RECIPE_d22.json').read_text());P=json.loads((ROOT/'research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PARAMETERS.json').read_text());C=P['controller'];plane=a['plane_local_codes'];assert plane==b['plane_local_codes'] and len(plane)==16
summary=[]
for cap,r in [(23,[x+y for x,y in zip(a['controller_multiplicities'],b['controller_multiplicities'])]),(24,[2*y for y in b['controller_multiplicities']])]:
 k=cap-20;load=[sum(r[c]for c in row)for row in C];assert len(r)==60 and all(t<=k for t in load)
 centers=[];layers=[]
 for u in range(60):
  for copy in range(r[u]):
   layers.append(u)
   for code in plane:
    j=len(centers);centers.append(dict(clone_index=j,new_vertex=3840+j,owner=64*u+code,controller=u,multiplicity_copy=copy,plane_local_code=code))
 N={23:4336,24:4544}[cap];M={23:48320,24:52480}[cap];assert len(layers)=={23:31,24:44}[cap] and 3840+len(centers)==N and 38400+20*len(centers)==M
 hist=collections.Counter({20:len(centers)})
 for x in load:hist[20+x]+=64
 recipe=dict(status='FIXED_CANDIDATE_RECIPE_NOT_YET_PRODUCED',cap=cap,D=3,source_file='research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/graph_d20_D3_n3840.edges',source_parameter_file='research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PARAMETERS.json',source_D3_inherited=True,source_r_files=['f4_c60_plane_blocks/RECIPE_d21.json','f4_c60_plane_blocks/RECIPE_d22.json'],multiplicity_formula='r21+r22'if cap==23 else'2*r22',center_plane_normal=[1,1,2],center_plane_rhs=0,plane_local_codes=plane,controller_multiplicities=r,old_fiber_loads=load,controller_rows_checked=60,maximum_old_fiber_load=max(load),ordered_block_layers=layers,ordered_centers=centers,clone_count=len(centers),predicted_n=N,predicted_m=M,predicted_degree_histogram=dict(sorted(hist.items())),fixed_clone_pins='full original source open neighborhood of owner',new_new_edges=False,ordered_label_rule='new_vertex=3840+clone_index; controller ascending, copy ascending, listed plane order',graph_generated=False,public_comparison='PENDING_ROOT',global_record_claim=False)
 (D/f'RECIPE_d{cap}.json').write_text(json.dumps(recipe,indent=2)+'\n');summary.append(dict(cap=cap,blocks=len(layers),ordered_owners=len(centers),max_load=max(load),all60_capacity_rows=True,order=N,edges=M,graph_generated=False))
result=dict(status='PASS_PREPARATION_FIXED_TWO_RECIPES_ONLY',CPU_seconds=time.process_time()-START,aggregate_CPU_limit=30,recipes=summary,solver_calls=0,graph_generated=False,waiting_for_root_public_execution_notice=True)
assert result['CPU_seconds']<30
(D/'PREPARATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

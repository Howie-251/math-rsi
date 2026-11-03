import csv,datetime,json,math,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;P=D.parent;I=P/'six_fiber_double56_interface'
def children_cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def limits(seconds):
 def apply():resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
 return apply
def main():
 start=time.process_time();child0=children_cpu();wall=time.monotonic()
 assert (D/'PRED.md').exists() and not (D/'RESULT.json').exists() and not (D/'graph_d56_D3_n57834.edges').exists()
 ip=json.loads((I/'PARAMETERS.json').read_text());ir=json.loads((I/'RESULT.json').read_text())
 assert ir['status']=='PASS_FIXED_SIX_U_PLANE_PACKING_AND_DOUBLE_LOAD_INTERFACE'
 centers=[{k:int(v) for k,v in r.items()} for r in csv.DictReader((I/'CENTERS.csv').open())]
 pins=[[] for _ in range(486)]
 for r in csv.DictReader((I/'PINS.csv').open()):pins[int(r['base_index'])].append(int(r['source_pin']))
 assert len(centers)==486 and ip['selected_controllers']==[0,1,2,3,9,15]
 with (D/'EXPECTED_SOURCE_PINS.tsv').open('w') as f:
  for i,c in enumerate(centers):
   ui,a,b=i//81,(i%81)//9,i%9;assert c['index']==i and c['u_index']==ui and c['a']==a and c['b']==b
   assert c['source_center']==729*c['controller']+c['x0']+9*c['x1']+81*c['x2']
   assert len(pins[i])==len(set(pins[i]))==54
   f.write(' '.join(map(str,[i,ui,a,b,c['source_center']]+sorted(pins[i])))+'\n')
 params=dict(source_edge_file='../graph_d54_D3_n56862.edges',source_parameters='../PARAMETERS.json',source_n=56862,source_m=1535274,source_degree=54,
  interface='../six_fiber_double56_interface/PARAMETERS.json',selected_controllers=ip['selected_controllers'],plane=ip['plane'],eta=4,
  base_center_order='uIndex outer,a middle,b inner',base_index='81*uIndex+9*a+b',source_center_label=ip['source_center_label'],
  base_centers=486,base_center_labels=[c['source_center'] for c in centers],copies=2,clone_index='486*copy+81*uIndex+9*a+b',new_label='56862+clone_index',
  immutable_original_source_only=True,source_is_new55_graph=False,neighbors='exact54literal neighbors of original56862source center; repeated twice',
  ordered_expected_pins='EXPECTED_SOURCE_PINS.tsv',ordered_actual_source_pins='ORDERED_SOURCE_PINS.tsv',prefix_table='PREFIX_LOADS.csv',
  order=57834,degree_cap=56,expected_edges=1587762,new_vertices=972,new_edges=52488,new_new_edges=0,
  expected_degree_histogram={'54':31590,'56':26244},expected_source_load_histogram={'0':30618,'2':26244},
  edge_file='graph_d56_D3_n57834.edges',edge_file_format='No header;u v,0<=u<v<57834,global lexsorted',
  public_gate='../../../../public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md',public_source_guarantee=57568,
  bounded_target_gain=266,global_record_or_priority_certified=False,independent_acceptance='ROOT_FRESH_SEPARATE_TASK')
 (D/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n')
 prep=time.process_time()-start
 run=dict(status='RUNNING',started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),CPU_budget_seconds=30,workers=1,preparation_CPU_seconds=prep,compile_runs=1,production_runs=1)
 (D/'HANDLE.json').write_text(json.dumps(run,indent=2)+'\n')
 compile0=children_cpu();cmd=['g++','-std=c++17','-O2','-DNDEBUG','generate.cpp','-o','generate']
 with (D/'compile.stdout').open('w') as out,(D/'compile.stderr').open('w') as err:
  c=subprocess.run(cmd,cwd=D,stdout=out,stderr=err,preexec_fn=limits(max(1,math.floor(30-prep))),timeout=120)
 compilecpu=children_cpu()-compile0;run['compile']=dict(command=cmd,exit_code=c.returncode,CPU_seconds=compilecpu)
 if c.returncode:raise RuntimeError('fixed production compile failed')
 remaining=math.floor(30-(time.process_time()-start+children_cpu()-child0));assert remaining>0
 gen0=children_cpu();cmd=[str(D/'generate'),str(P/'graph_d54_D3_n56862.edges'),str(D/'EXPECTED_SOURCE_PINS.tsv'),str(D)]
 with (D/'generate.stdout').open('w') as out,(D/'generate.stderr').open('w') as err:
  g=subprocess.run(cmd,cwd=D,stdout=out,stderr=err,preexec_fn=limits(remaining),timeout=120)
 gencpu=children_cpu()-gen0;run['production']=dict(command=cmd,exit_code=g.returncode,CPU_seconds=gencpu,CPU_limit=remaining)
 if g.returncode:raise RuntimeError('fixed production failed')
 r=json.loads((D/'generate.stdout').read_text());r.update(total_measured_CPU_seconds_including_compile_preparation=time.process_time()-start+children_cpu()-child0,
  compile_CPU_seconds=compilecpu,producer_child_CPU_seconds=gencpu,preparation_CPU_seconds=prep,workers=1,CPU_budget_seconds=30,
  public_source_guarantee=57568,bounded_target_gain=266,global_record_or_priority_certified=False,
  independent_acceptance='PENDING_ROOT_FRESH_LITERAL_ACCEPTANCE',concrete_Lean='NOT_STARTED_SEPARATE300CPU_SCOPE',accepted_counts_changed=False)
 assert r['total_measured_CPU_seconds_including_compile_preparation']<30
 (D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
 run.update(status=r['status'],finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),total_measured_CPU_seconds=r['total_measured_CPU_seconds_including_compile_preparation'],wall_seconds=time.monotonic()-wall)
 (D/'BUILD_RUN.json').write_text(json.dumps(run,indent=2)+'\n');(D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',**{k:v for k,v in run.items() if k!='status'}),indent=2)+'\n')
 (D/'TERMINAL.json').write_text(json.dumps(dict(status='FIXED56_COMPLETE_FILE_CLOSED_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE',running=False,complete_edge_file_closed=True,
  graph_file='graph_d56_D3_n57834.edges',source55_graph_read=False,old_BFS_runs=0,field_revalidations=0,solver_calls=0,Lean_compilations=0,
  total_measured_CPU_seconds=r['total_measured_CPU_seconds_including_compile_preparation'],CPU_budget_seconds=30,accepted_counts_changed=False,
  next='Root fresh independent acceptance can start immediately;new56concreteLean is separate budget/scope.'),indent=2)+'\n')
 print(json.dumps({k:r[k] for k in ['status','vertices','edges','degree_histogram','source_load_histogram','total_measured_CPU_seconds_including_compile_preparation']}))
if __name__=='__main__':main()

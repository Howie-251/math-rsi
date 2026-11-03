import datetime,json,math,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;P=D.parent;U=[31,32,44,45,59,60,61,72,73,74]
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def limit(n):
 def f():resource.setrlimit(resource.RLIMIT_CPU,(n,n))
 return f
def main():
 start=time.process_time();before=childcpu();wall=time.monotonic();assert (D/'PRED.md').exists() and not (D/'RESULT.json').exists()
 p=json.loads((P/'PARAMETERS.json').read_text());ct=p['controller'];ci=p['dart_chart_index'];mp=p['matrices'];ell=p['directions'];rev=p['inverse_ports'];mul=p['field']['multiplication']
 targets=sum([ct[u] for u in U],[]);assert len(set(targets))==60
 def add(a,b):return(a%3+b%3)%3+3*((a//3+b//3)%3)
 def act(m,x):return tuple(add(add(mul[r[0]][x[0]],mul[r[1]][x[1]]),mul[r[2]][x[2]]) for r in m)
 def code(x):return x[0]+9*x[1]+81*x[2]
 centers=[];used=set();(D/'graphs').mkdir(exist_ok=True)
 with (D/'EXPECTED_SOURCE_PINS.tsv').open('w') as f:
  for ui,u in enumerate(U):
   for a in range(9):
    for b in range(9):
     i=81*ui+9*a+b;x=(a,b,mul[4][a]);c=729*u+code(x);pins=[]
     for port in range(6):
      base=act(mp[ci[u][port]],x);v=ct[u][port]
      for noise in range(9):
       y=tuple(add(base[j],mul[noise][ell[rev[port]][j]]) for j in range(3));pin=729*v+code(y)
       assert pin not in used and pin!=c;used.add(pin);pins.append(pin)
     assert len(set(pins))==54;centers.append(c);f.write(' '.join(map(str,[i,ui,a,b,c]+sorted(pins)))+'\n')
 assert len(centers)==810 and len(set(centers))==810 and len(used)==43740
 cases=[];public=[56540,57568,58596,59624,60652]
 for k in range(1,6):
  n=56862+810*k;degree=54+k;m=1535274+43740*k;name=f'd{degree}_n{n}';(D/'cases'/name).mkdir(parents=True,exist_ok=True)
  assert not (D/'graphs'/f'd{degree}_D3_n{n}.edges').exists()
  c=dict(k=k,degree_cap=degree,n=n,m=m,graph_file=f'graphs/d{degree}_D3_n{n}.edges',case_dir=f'cases/{name}',public_source_guarantee=public[k-1],bounded_gain=n-public[k-1]);cases.append(c)
 params=dict(source_edge_file='../graph_d54_D3_n56862.edges',source_parameters='../PARAMETERS.json',source_n=56862,source_m=1535274,source_degree=54,
  selected_controllers=U,controller_target_rows=[ct[u] for u in U],distinct_target_controllers=targets,plane='W={(a,b,GF9mul(4,a))}',eta=4,
  base_centers=810,base_center_labels=centers,base_index='81*uIndex+9*a+b',source_center_label='729*U[uIndex]+a+9*b+81*GF9mul(4,a)',
  clone_index='810*copy+baseIndex',new_label='56862+clone_index',neighbors='Immutable original56862-source fullN54 only',source_is_new55_graph=False,
  ordered_expected_pins='EXPECTED_SOURCE_PINS.tsv',ordered_actual_source_pins='ORDERED_SOURCE_PINS.tsv',prefix_table='PREFIX_LOADS.csv',
  source_parse_count_planned=1,base_pin_union=43740,base_pin_target_fibers=60,cases=cases,k6_produced=False,
  public_gate='../../../../public_baseline_audit/CONTROLLER_U10_DEGREE55_59_WINDOW_20261101.md',
  optimality_scope='Root accepted optimum10onlyfor fixedcontroller whole-layer plane model; point-level/nonrectangular not excluded.',
  global_record_or_priority_certified=False,accepted_counts_changed=False)
 (D/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n');prep=time.process_time()-start
 run=dict(status='RUNNING',CPU_budget_seconds=30,workers=1,preparation_CPU_seconds=prep,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 (D/'HANDLE.json').write_text(json.dumps(run,indent=2)+'\n');c0=childcpu();cmd=['g++','-std=c++17','-O2','-DNDEBUG','generate.cpp','-o','generate']
 with (D/'compile.stdout').open('w') as o,(D/'compile.stderr').open('w') as e:c=subprocess.run(cmd,cwd=D,stdout=o,stderr=e,preexec_fn=limit(max(1,math.floor(30-prep))),timeout=120)
 run['compile']=dict(command=cmd,exit_code=c.returncode,CPU_seconds=childcpu()-c0);assert c.returncode==0
 remaining=math.floor(30-(time.process_time()-start+childcpu()-before));assert remaining>0
 g0=childcpu();cmd=[str(D/'generate'),str(P/'graph_d54_D3_n56862.edges'),str(D/'EXPECTED_SOURCE_PINS.tsv'),str(D)]
 with (D/'generate.stdout').open('w') as log,(D/'generate.stderr').open('w') as err:
  proc=subprocess.Popen(cmd,cwd=D,stdout=subprocess.PIPE,stderr=err,text=True,preexec_fn=limit(remaining))
  for line in proc.stdout:log.write(line);log.flush();print(line.rstrip(),flush=True)
  proc.wait()
 run['production']=dict(command=cmd,exit_code=proc.returncode,CPU_seconds=childcpu()-g0,CPU_limit_seconds=remaining);assert proc.returncode==0
 result=dict(status='FIVE_COMPLETE_FIXED_U10_CASES_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE',source_parses=1,base_precheck=json.loads((D/'BASE_PRECHECK_RESULT.json').read_text()),cases=[],
  total_measured_CPU_seconds_including_compile_preparation=time.process_time()-start+childcpu()-before,CPU_budget_seconds=30,workers=1,
  complete_graph_files=5,k6_produced=False,old_BFS_runs=0,old_field_controller_checks_repeated=False,solver_calls=0,Lean_compilations=0,
  concrete_Lean='SEPARATE600CPU_SCOPE_NOT_STARTED',accepted_counts_changed=False)
 for c in cases:
  r=json.loads((D/c['case_dir']/'RESULT.json').read_text());assert r['file_closed'] and r['n']==c['n'] and r['m']==c['m'];result['cases'].append(dict(**c,actual=r))
 assert result['total_measured_CPU_seconds_including_compile_preparation']<30
 (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');run.update(status='TERMINAL',total_measured_CPU_seconds=result['total_measured_CPU_seconds_including_compile_preparation'],wall_seconds=time.monotonic()-wall)
 (D/'BUILD_RUN.json').write_text(json.dumps(run,indent=2)+'\n');(D/'HANDLE.json').write_text(json.dumps(run,indent=2)+'\n')
 (D/'TERMINAL.json').write_text(json.dumps(dict(status=result['status'],running=False,complete_files_closed=5,source_parses=1,k6_produced=False,
  total_measured_CPU_seconds=result['total_measured_CPU_seconds_including_compile_preparation'],CPU_budget_seconds=30,accepted_counts_changed=False,
  next='Fresh independent fivecase acceptance starts now; concreteLean is separate and no extra U/degree case is authorized.'),indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['status','complete_graph_files','source_parses','total_measured_CPU_seconds_including_compile_preparation']}),flush=True)
if __name__=='__main__':main()

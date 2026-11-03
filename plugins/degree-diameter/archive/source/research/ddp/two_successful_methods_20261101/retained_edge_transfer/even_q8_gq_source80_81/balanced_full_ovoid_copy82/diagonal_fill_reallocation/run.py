import csv,json,os,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;P=D.parent
def save(name,data):
 p=D/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(data,indent=2)+'\n');os.replace(t,p)
parameters=json.loads((P/'PARAMETERS.json').read_text());owners=parameters['ovoid_spread_owners'];delta=[]
with(P/'CENTERS.tsv').open()as f:
 for r in csv.DictReader(f,delimiter='\t'):
  if int(r['diagonal']):
   i=int(r['i']);j=int(r['j']);h=int(r['index']);assert j==owners[i]and h==65*i+j
   delta.append(dict(ovoid_index=i,spread_index=j,clone_index=h,clone_label=342290+h,deleted_edge=[342225+j,342290+h],added_edge=[342225+j,346515]))
assert len(delta)==65 and{r['spread_index']for r in delta}==set(range(65))
(D/'DELTA_INPUT.txt').write_text(''.join(f"{r['spread_index']} {r['clone_label']}\n"for r in delta))
save('EDGE_DELTA.json',dict(diagonal_rows=delta,deleted_edges=65,added_edges=65))
prep=time.process_time();steps=[]
def run(name,cmd,budget):
 before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
 def limit():resource.setrlimit(resource.RLIMIT_CPU,(budget,budget))
 with(D/(name+'.stdout')).open('w')as o,(D/(name+'.stderr')).open('w')as e:
  p=subprocess.Popen(cmd,cwd=D,stdout=o,stderr=e,preexec_fn=limit)
  save('HANDLE.json',dict(status='RUNNING',driver_pid=os.getpid(),child_pid=p.pid,step=name,command=cmd,remaining_CPU_budget=budget));p.wait()
 after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
 result=dict(step=name,exit_code=p.returncode,CPU_seconds=cpu,wall_seconds=time.monotonic()-start,command=cmd);steps.append(result);assert p.returncode==0,result
run('compile',['g++','-O2','-std=c++17','produce.cpp','-o','produce'],min(10,int(30-prep)))
source=P/'graph_d82_D3_n346515.edges';out=D/'graph_d82_D3_n346516.edges';partial=out.with_suffix('.edges.partial')
used=prep+sum(s['CPU_seconds']for s in steps);run('produce',[str(D/'produce'),str(source),str(partial),str(D/'DELTA_INPUT.txt')],int(30-used))
os.replace(partial,out);actual=json.loads((D/'produce.stdout').read_text());cpu=sum(s['CPU_seconds']for s in steps)+time.process_time()
assert cpu<30
save('PARAMETERS.json',dict(n=346516,m=14204970,max_degree=82,D_target=3,source_H_n=342290,source_H_m=13862745,source_H='../'+'../balanced/graph_d81_D3_n342290.edges',input_accepted346515='../graph_d82_D3_n346515.edges',center_table='../CENTERS.tsv',source_U_n=342225,original_fillers=[342225,342289],hub=346515,clone_labels=[342290,346514],diagonal_test='j=ovoid_spread_owners[i],not j=i',deleted65='diagonal clone--original own filler',added65='hub--all original fillers',old_H_edges_retained=True,format='n m header,strictlex a b,a<b',degree_histogram=actual['degree_histogram'],predicted_BFS=dict(diagonal=dict(roots=65,layers=[1,80,5250,341185]),offdiagonal=dict(roots=4160,layers=[1,81,5329,341105]),hub=dict(roots=1,layers=[1,65,5265,341185])),producer_BFS_runs=0,independent_acceptance='PENDING_SEPARATE_AGENT_66_ROOTS_ONLY',global_record_or_priority_claimed=False))
result=dict(**actual,CPU_seconds=cpu,CPU_budget_seconds=30,preparation_CPU_seconds=prep,steps=steps,source_parses=1,output=str(out),fresh_acceptance='PENDING',new_graphs_counted_by_producer=0,field_geometry_projection_Lean_solver_runs=0)
save('RESULT.json',result);terminal=dict(status='FIXED346516_PRODUCER_TERMINAL_FILE_CLOSED_FRESH_ACCEPTANCE_PENDING',running=False,active_processes=[],CPU_seconds=cpu,CPU_budget_seconds=30,output=str(out));save('TERMINAL.json',terminal);save('HANDLE.json',terminal);print(json.dumps(result),flush=True)

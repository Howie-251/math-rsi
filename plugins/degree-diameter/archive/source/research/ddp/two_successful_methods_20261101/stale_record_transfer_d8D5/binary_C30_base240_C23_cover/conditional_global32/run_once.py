from pathlib import Path
import json,subprocess,resource,time
B=Path(__file__).resolve().parent;P=B.parent;t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert not (B/'RESULT.json').exists()
f=load(P/'edge_voltage_packet/SIGNED_EDGE_FLOWS.json')['path_flows'];w=load(P/'edge_voltage_packet/VOLTAGE_WITNESS.json');prior=load(P/'allpair_edgeflow_gate/RESULT.json');base=dict(f[0]);chosen=w['selected_paths'][1:]
m=[[(dict(f[j]).get(e,0)-base.get(e,0))%23 for e in range(960)]+[i+1] for i,j in enumerate(chosen)];piv=[];rr=0
for c in range(960):
 k=next((k for k in range(rr,22) if m[k][c]),None)
 if k is None:continue
 m[rr],m[k]=m[k],m[rr];z=pow(m[rr][c],-1,23);m[rr]=[x*z%23 for x in m[rr]]
 for k in range(22):
  if k==rr:continue
  z=m[k][c]
  if z:m[k]=[(x-z*y)%23 for x,y in zip(m[k],m[rr])]
 piv.append(c);rr+=1
 if rr==22:break
assert rr==22
save('CONSTRAINT_RREF.json',{'field':23,'pivots':piv,'matrix_augmented':m,'selected_paths':chosen,'edge_order':'sameasedge_voltage_packet/VOLTAGE_WITNESS.json','free_variables':938,'uniform_sampling':'all938freecoordinatesuniformF23;22pivotsdeterministicallyreconstructed'})
with (B/'CONSTRAINTS.txt').open('w') as out:
 out.write('960 22\n'+' '.join(map(str,piv))+'\n')
 for row in m:out.write(' '.join(map(str,[row[-1]]+row[:-1]))+'\n')
c0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['g++','-O2','-std=c++17','run.cpp','-o','run'],cwd=B,capture_output=True,text=True);c1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'COMPILE.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
def limit():resource.setrlimit(resource.RLIMIT_CPU,(8,8))
r0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['./run'],cwd=B,capture_output=True,text=True,timeout=20,preexec_fn=limit);r1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'RUN.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
n=load(B/'NATIVE_RESULT.json');theta=list(map(int,(B/'BEST_VOLTAGE_VALUES.txt').read_text().split()));assert len(theta)==960
save('BEST_VOLTAGE.json',{'edges':w['edges'],'voltage':theta,'field':23,'best_sample':n['best_sample'],'diameter5':n['full_D5_hit'],'ordinary_simple_8regular_order':5520})
if n['full_D5_hit']:
 with (B/'CANDIDATE5520.edges').open('w') as out:
  out.write('5520 22080\n')
  for (u,v),t in zip(w['edges'],theta):
   for k in range(23):out.write(f'{23*u+k} {23*v+(k+t)%23}\n')
compilecpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime;childcpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime;parentcpu=time.process_time()-t0
r={'status':'FULL5520_COVER_CANDIDATE_SAVED_PENDING_FRESH_ACCEPTANCE' if n['full_D5_hit'] else 'NO_HIT_32_CONDITIONAL_GLOBAL_VOLTAGES_FAMILY_UNKNOWN_STOP','native':n,'P1_critical_preservation_supported':n['critical_packet_preserved_all'],'P2_joint_critical_first_diagonal_supported':n['joint_critical_and_first_diagonal_full_samples']>0,'compile_CPU':compilecpu,'child_CPU':childcpu,'parent_CPU':parentcpu,'prior_CPU':prior['samecase_CPU'],'new_prepare_CPU':.2,'samecase_CPU':prior['samecase_CPU']+.2+compilecpu+childcpu+parentcpu,'case_cap':20,'exact_allpair_phase_evaluations':n['samples']*28920,'new_paths_BFS_solver_Lean_ARIS':0,'target5520_graph_edgefile_generated':n['full_D5_hit'],'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'32samplesinfull960edgevoltageaffinespacesatisfying22criticalconstraints;notexhaustiveC23NO;voltageparametersdefinelegal8regularcoversbutnoneacceptedwithoutfullD5','terminal':True,'next':'newgraphacceptanceifhit;otherwiseSTOPno33rdsample_seed_hillclimb; revisitonlywithspecificglobalruleorswitchtoAreadgate'}
assert r['samecase_CPU']<20
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))

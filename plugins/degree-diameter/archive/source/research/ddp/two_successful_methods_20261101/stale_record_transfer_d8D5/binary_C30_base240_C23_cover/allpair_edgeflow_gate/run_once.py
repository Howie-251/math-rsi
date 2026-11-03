from pathlib import Path
import json,subprocess,resource,time
B=Path(__file__).resolve().parent;P=B.parent;t0=time.process_time()
def load(p):return json.loads(p.read_text())
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert not (B/'RESULT.json').exists()
w=load(P/'edge_voltage_packet/VOLTAGE_WITNESS.json');prior=load(P/'edge_voltage_packet/RESULT.json')
with (B/'INPUT.txt').open('w') as f:
 f.write('240 960\n')
 for (u,v),t in zip(w['edges'],w['voltage']):f.write(f'{u} {v} {t}\n')
c0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['g++','-O2','-std=c++17','run.cpp','-o','run'],cwd=B,capture_output=True,text=True);c1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'COMPILE.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
def limit():resource.setrlimit(resource.RLIMIT_CPU,(5,5))
r0=resource.getrusage(resource.RUSAGE_CHILDREN);ret=subprocess.run(['./run'],cwd=B,capture_output=True,text=True,timeout=15,preexec_fn=limit);r1=resource.getrusage(resource.RUSAGE_CHILDREN);(B/'RUN.log').write_text(ret.stdout+ret.stderr);ret.check_returncode()
n=load(B/'NATIVE_RESULT.json');compilecpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime;childcpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime;parentcpu=time.process_time()-t0
r={'status':'ALLPAIR_EDGEFLOW_CAPACITY_PASS_LOCAL_WITNESS_GLOBAL_FAIL' if n['allpair_flow_capacity_pass'] else 'COMPLETE_NO_ANY_INDEPENDENT_EDGE_C23_VOLTAGES_ON_FIXEDBASE','native':n,'P1_capacity_prediction_supported':n['allpair_flow_capacity_pass'],'P2_local_witness_fail_prediction_supported':n['witness_failing_packets']>0,'compile_CPU':compilecpu,'child_CPU':childcpu,'parent_CPU':parentcpu,'new_prep_CPU':.2,'prior_CPU':prior['samecase_CPU'],'samecase_CPU':prior['samecase_CPU']+.2+compilecpu+childcpu+parentcpu,'samecase_cap':10,'new_target_graph_BFS_source_revalidation_solver_Lean_ARIS':0,'new_accepted_graph_parameter_Lean':[0,0,0],'flow_cache':'ALL_PACKET_FLOWS.bin: perpacket native littleendian u32 count followed count*5i16; u<=v packet order fromPACKET_CACHE_OFFSETS.tsv','scope':'capacity passesonly necessaryforallantisymmetricC23 pointedgevoltages; existingexplicit21nonzerovoltagefailsglobalD5,notfamilyNO ifallflowpass','terminal':True,'next':'REASSESS_FIXED_CACHE_BEFORE_AUTHORIZING_ONE_GLOBAL_CONSTRUCTION_BATCH'}
assert r['samecase_CPU']<10
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))

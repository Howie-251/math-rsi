import time
START=time.process_time()
from pathlib import Path
import json,subprocess,resource
HERE=Path(__file__).resolve().parent
BASE=next(p for p in HERE.parents if(p/'STAGE_STATE.json').is_file())
SHARED=BASE/'stale_record_transfer_d5D4/source252_two_cut_star253/run'
PRIOR=.295155622+.25

def save(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('two104cohortbatch already attempted')
save(HERE/'ATTEMPT.json',{'status':'STARTED','prior_read_prep_CPU':PRIOR,'casecap':10})
assert SHARED.exists()
results=[];childrenCPU=0
for alias,filename in [('a_unlettered','source104a.header.edges'),('b','source104b.header.edges')]:
 d=HERE/(alias+'_run');d.mkdir(exist_ok=True)
 lines=(HERE/filename).read_text().splitlines();assert list(map(int,lines[0].split()))==[104,208]
 es=[tuple(map(int,l.split()))for l in lines[1:]if l.strip()];assert len(es)==len(set(tuple(sorted(x))for x in es))==208
 deg=[0]*104
 for u,v in es:assert 0<=u<104 and 0<=v<104 and u!=v;deg[u]+=1;deg[v]+=1
 assert set(deg)=={4}
 with(d/'SOURCE_CANONICAL.edges').open('w')as f:
  f.write('104 208 4\n')
  for u,v in sorted(tuple(sorted(x))for x in es):f.write(f'{u} {v}\n')
 save(d/'ENGINE_REFERENCE.json',{'generic_cpp':'stale_record_transfer_d5D4/source252_two_cut_star253/run.cpp','binary_used':str(SHARED.relative_to(BASE)),'compile_already_charged_to_source252case':True,'source_D4_revalidation':0,'sourcealias':alias})
 c0=resource.getrusage(resource.RUSAGE_CHILDREN)
 def limit():resource.setrlimit(resource.RLIMIT_CPU,(3,3))
 with(d/'RUN.log').open('w')as f:
  p=subprocess.Popen([str(SHARED)],cwd=d,stdout=f,stderr=subprocess.STDOUT,preexec_fn=limit)
  save(d/'HANDLE.json',{'PID':p.pid,'status':'RUNNING_ONE_SOURCE_ALL20904_TWOCUTS'})
  code=p.wait()
 c1=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime;childrenCPU+=cpu
 nat=json.loads((d/'NATIVE_RESULT.json').read_text())if(d/'NATIVE_RESULT.json').exists()else{'status':'UNKNOWN_CHILD_EXIT','code':code}
 item={'alias':alias,'native':nat,'actual_native_child_CPU':cpu,'output_directory':d.name};results.append(item);save(d/'RESULT.json',item)
r={'status':'TWO_SOURCE_TERMINAL_FULLHIT_PENDING_FRESH'if any(x['native'].get('full_hit')for x in results)else('COMPLETE_NO_BOTH_PUBLIC104_LITERALS_TWO_CUT_STAR'if all(x['native'].get('domain_complete')for x in results)else'UNKNOWN_ONE_OR_MORE_NATIVEWINDOWS'),'sources':results,'source104c':'oldcomplete20904NOinheritednotrerun','source_new_depth3_queries':sum(x['native'].get('source_depth3_support_queries',0)for x in results),'source_D4_revalidation_Lean_ARIS_solver':0,'parent_CPU':time.process_time()-START,'actual_children_CPU':childrenCPU,'prior_read_prep_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START+childrenCPU,'case_cap':10,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'twoofficial104a_unlettered/b literalinputs,alltwovertexdisjointsourcecuts+one4star;notgeneral105/4D4','next':'fresh/latestpublic/Lean/ARIS ifanyhit;otherwiseSTOPcohortNo_no3rdcut_orseed','terminal':True}
save(HERE/'RESULT.json',r);save(HERE/'TERMINAL.json',r)
print(json.dumps(r,ensure_ascii=False),flush=True)

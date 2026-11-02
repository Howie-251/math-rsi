#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PRIOR=json.loads((HERE.parent/'RESULT.json').read_text())['total_charged_CPU_seconds']
PREP=0.15
BUDGET=10.0
initial=resource.getrusage(resource.RUSAGE_CHILDREN)

def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime

def charged():
    return PRIOR+PREP+time.process_time()+child_cpu()

def save(name,data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def limit(seconds):
    def setup():
        n=max(1,math.ceil(seconds))
        resource.setrlimit(resource.RLIMIT_CPU,(n,n+1))
    return setup

save('HANDLE.json',{'pid':os.getpid(),'phase':'compile','running':True,'prior_case_CPU_seconds':PRIOR,'CPU_budget_seconds':BUDGET,'worker_count':1})
before=child_cpu()
with (HERE/'COMPILE.log').open('w') as log:
    compiler=subprocess.Popen(['g++','-O2','-std=c++17',str(HERE/'run.cpp'),'-o',str(HERE/'run')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(BUDGET-charged()-0.3))
    save('HANDLE.json',{'pid':os.getpid(),'child_pid':compiler.pid,'phase':'compile','running':True,'CPU_budget_seconds':BUDGET,'worker_count':1})
    code=compiler.wait()
compile_cpu=child_cpu()-before
if code:
    result={'status':'COMPILE_FAILED_NO_QUERY','exit_code':code}
else:
    remaining=BUDGET-charged()-0.3
    before=child_cpu()
    with (HERE/'RUN.log').open('w') as log:
        run=subprocess.Popen([str(HERE/'run'),str(HERE),str(remaining)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(remaining+0.1))
        save('HANDLE.json',{'pid':os.getpid(),'child_pid':run.pid,'phase':'three_modified_graph_multisource_R8_queries','running':True,'worker_count':1,'CPU_budget_seconds':BUDGET,'remaining_run_CPU_seconds':remaining})
        code=run.wait()
    run_cpu=child_cpu()-before
    if code:
        result={'status':'RUN_INTERRUPTED_UNKNOWN','exit_code':code}
    else:
        result=json.loads((HERE/'RAW_RESULT.json').read_text())
        result['status']='COMPLETE_NO_SINGLE_EDGE_SUBDIVISION_D9_ON_FIXED_SOURCE' if result['all_three_types_fail'] else ('NEWROOT_NECESSARY_SURVIVOR_OLDOLD_UNTESTED' if result['query_count']==3 else 'UNKNOWN_QUERY_CPU_CAP')
        result['actual_run_child_CPU_seconds']=run_cpu
result.update({'target':{'maximum_degree':6,'diameter':9,'subdivision_order':331388,'subdivision_edges':994162},
 'prediction':'All three inverse-generator edge types fail the modified endpoint-radius8 union.',
 'prediction_supported':result.get('all_three_types_fail',False),
 'source_coordinate_model':'RIGHT Cayley (j,n)*(a,c)=(j+a,n*41^a+c);label6763*j+n',
 'source_isomorphism':'inversion from the author left Cayley graph; old group/D9 facts inherited',
 'exact_scope':'All single old-edge subdivisions of this fixed inverse-closed six-generator Cayley source; three types exhaust edges by left translations.',
 'not_excluded':['other grafts','multiple subdivided edges','old-edge rewiring','other generators or fields','general degree6 diameter9 graphs'],
 'source_allroot_D9_validity_or_old_field_rechecks':0,'raw_graph_download_or_generation':0,'oldold_new_candidate_BFS':0,
 'solver_Lean_remote_install_hash':0,'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
 'actual_compile_CPU_seconds':compile_cpu,'driver_process_CPU_seconds':time.process_time(),
 'cumulative_charged_CPU_seconds':charged(),'cumulative_CPU_budget_seconds':BUDGET,'worker_count':1,
 'new_graph_parameter_Lean_increment':[0,0,0],'next':'STOP_NO_OLDPAIR_CHECK_OR_EXTRA_GRAFT'})
save('RESULT.json',result)
lines=['# Three single-edge-subdivision endpoint gates','',f"Actual status: {result['status']}",'']
for q in result.get('queries',[]):
    lines.append(f"- Generator{q['positive_generator']}: covered{q['covered_old_count']}, missing{q['missing_old_count']}; first target{q['first_missing_label']}={q['first_missing_coordinates']}. New subdivision root has distance at least10 to that target.")
lines += ['', 'The one depth8 multi-source traversal per type computes B8_H(1) union B8_H(s), H=G−{1,s}. A shortest path from new degree2 z first uses one endpoint and then stays in H, so its old-vertex distances are1+the endpoint minimum. No original-source radius9 check is needed or performed. A radius8 miss is a proved lower bound of10 for the new point; no unsupported exact distance10 or path is claimed.', '',
 'Every edge of the right Cayley graph is a left translate of {1,s} for one of the three positive generators; inverse orientations give the same representatives by translating with s. Left translation also transports the subdivided graph. Thus three failures exclude exactly every single-edge subdivision on this fixed source. A hypothetical pass would only certify new-root coverage, not old-old routes.', '',
 'The old source is reconstructed only implicitly from inherited group constants and true inverses; no raw adjacency is read/generated or AUTHOR main run. The author left/right convention is handled by the inherited inversion isomorphism. Old field/order/degree/D9 facts are not rechecked.', '',
 f"Budget inherits{PRIOR:.9f}, charges preparation{PREP}, compiler{compile_cpu:.9f}, actual queries and driver. Cumulative{charged():.9f}/10CPU, one worker. All work stops after these gates; no old-pair BFS, other edge modification, generator, field, solver, Lean or review follows."]
(HERE/'NOTE.md').write_text('\n'.join(lines)+'\n')
terminal={'status':result['status'],'running':False,'all_processes_terminal':True,'prior_case_CPU_seconds':PRIOR,
 'new_preparation_charge_seconds':PREP,'actual_compile_CPU_seconds':compile_cpu,'actual_run_child_CPU_seconds':result.get('actual_run_child_CPU_seconds',0),
 'driver_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),'cumulative_CPU_budget_seconds':BUDGET,
 'worker_count':1,'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal)
save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False,indent=2))

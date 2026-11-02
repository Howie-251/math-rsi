#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PRIOR=json.loads((HERE.parent/'NEXT_SHARED_TRANSLATION_SCOPE.json').read_text())['cumulative_case_charged_CPU_seconds']
BUDGET=20.0
PREP=0.2
initial=resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
def charged():return PRIOR+PREP+time.process_time()+child_cpu()
def save(name,value):(HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def limit(seconds):
    def setup():
        n=max(1,math.ceil(seconds));resource.setrlimit(resource.RLIMIT_CPU,(n,n+1))
    return setup
save('HANDLE.json',{'pid':os.getpid(),'phase':'compile','running':True,'worker_count':1,'cumulative_CPU_budget_seconds':BUDGET,'prior_case_CPU_seconds':PRIOR})
before=child_cpu()
with (HERE/'COMPILE.log').open('w') as log:
    compiler=subprocess.Popen(['g++','-O3','-std=c++17',str(HERE/'run.cpp'),'-o',str(HERE/'run')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(BUDGET-charged()-0.5))
    save('HANDLE.json',{'pid':os.getpid(),'child_pid':compiler.pid,'phase':'compile','running':True,'worker_count':1,'cumulative_CPU_budget_seconds':BUDGET})
    code=compiler.wait()
compile_cpu=child_cpu()-before
if code:result={'status':'COMPILE_FAILED_NO_PROJECTIVE_EVALUATION','exit_code':code}
else:
    remaining=BUDGET-charged()-0.6;before=child_cpu()
    with (HERE/'RUN.log').open('w') as log:
        process=subprocess.Popen([str(HERE/'run'),str(HERE),str(remaining)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(remaining+0.3))
        save('HANDLE.json',{'pid':os.getpid(),'child_pid':process.pid,'phase':'coefficient_generation_then_complete_projective_domain','running':True,'worker_count':1,'cumulative_CPU_budget_seconds':BUDGET,'run_CPU_limit_seconds':remaining,'actual_compile_CPU_seconds':compile_cpu})
        code=process.wait()
    run_cpu=child_cpu()-before
    if code:result={'status':'PROCESS_INTERRUPTED_UNKNOWN','exit_code':code}
    else:result=json.loads((HERE/'RAW_RESULT.json').read_text())
    result['actual_run_child_CPU_seconds']=run_cpu
phase0=json.loads((HERE/'PHASE0_RESULT.json').read_text()) if (HERE/'PHASE0_RESULT.json').exists() else None
result.update({'prediction':'At least one new representative covers all6959 normal endpoints at phase0; not a fullD9 prediction.',
 'prediction_phase0_supported':bool(phase0 and phase0['phase0_survivor_count']>0),'phase0_actual':phase0,
 'normalization':'Conjugate firstnormal to0, then remaining(cB,cC) is P1(F6959)+zero;skip inherited(1,1512) and disconnectedzero.',
 'new_domain':'6958 finite tau other than1512, plus infinity(0,1)',
 'inverse_phase_bridge':'Complete<=9 word sets obey U_-j=-beta^-j U_j;0..24 cover all49phases.',
 'exact_scope':'Only F6959,beta5155,fixed positive phases1/36/45,all three normal translations modulo conjugation/global scale.',
 'not_excluded':['the other41 actions','other fields','different phase sets','other Cayley connection sets','general degree6/D9 graphs'],
 'old_source_field_law_old_action_BFS_solver_ARIS_Lean_hash':0,
 'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,'actual_compile_CPU_seconds':compile_cpu,
 'driver_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),'cumulative_CPU_budget_seconds':BUDGET,'worker_count':1,
 'root_Wiki_modified':False,'graph_parameter_Lean_increment_before_root_acceptance':[0,0,0],
 'next':'STOP_REPORT_NO_OTHER_BETA_PHASE_TEMPLATE_OR_TIMER'})
save('RESULT.json',result)
note=f'''# Fixedβ5155 homogeneous-normal pilot

Actual status: {result['status']}. Phase0 feedback is saved separately before later phases; complete per-representative checked masks/failure witnesses are in REPRESENTATIVE_STATUS.csv. FORM_COUNTS.csv and COEFFICIENT_FORMS.u32 retain the new homogeneous endpoint forms generated once, without scalar1512 endpoint/BFS re-evaluation.

This is a fixedβ complete projective-domain experiment, not a bad-pair hill climb. The old experiment frozeτ1512; the new freedom is(cB,cC) modulo common scale, including infinity. Old1512NO and allzero-disconnected are inherited, not rerun. See PAPER_DOMAIN.md for the independent normalization, RIGHT recurrence and inverse-word proof.

Every generated word is an actual sequence of true inverse-paired Cayley darts. An image covering6959 in everyphase gives all identity endpoints within9; left translations give allpairs. Conversely, a missing endpoint in a complete NB<=9 image precludes any path<=9, since an immediate inverse pair in a shortest walk can be removed. The inverse-word map scales U_j by a nonzero factor onto U_-j, so testing phases0..24 is sufficient for all49. A singlephase survivor is not a graph result.

If a complete target was found, only one340991/1022973 graph was written and parameter work stopped; it remains pending root acceptance, with exactdiameter unset. If all6959 new representatives failed, combining the inherited1512NO and zeroNO excludes precisely thisβ5155/fixedphase all-normal family. If work stopped early, untouched masks remain explicitly unresolved; no full-family negative is inferred.

Budget inherits{PRIOR:.9f} and includes new preparation{PREP}, compiler{compile_cpu:.9f}, actual run and driver CPU; cumulative{charged():.9f}/20CPU, one worker. No nextaction, field, phase, seed, source validation/BFS, solver, ARIS, Lean or review is dispatched. Root alone owns acceptance/counts and global documents.
'''
(HERE/'NOTE.md').write_text(note)
terminal={'status':result['status'],'running':False,'all_processes_terminal':True,'prior_case_CPU_seconds':PRIOR,
 'new_preparation_charge_seconds':PREP,'actual_compile_CPU_seconds':compile_cpu,'actual_run_child_CPU_seconds':result.get('actual_run_child_CPU_seconds',0),
 'driver_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),'cumulative_CPU_budget_seconds':BUDGET,
 'worker_count':1,'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal);save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False,indent=2))

"""One bounded worker; cumulative sourcecase accounting, no retry/reset."""
from pathlib import Path
import json, resource, subprocess, time, math
START=time.process_time()
OUT=Path(__file__).resolve().parent
READGATE=json.loads((OUT.parent/'TERMINAL.json').read_text())['cumulative_charged_CPU_seconds']
PRIOR=json.loads((OUT/'format_guard_failure'/'TERMINAL.json').read_text())['cumulative_charged_CPU_seconds']
PREP=.15
CAP=20.
assert not (OUT/'TERMINAL.json').exists(), 'This sourcecase batch is run once only'
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    x=resource.getrusage(resource.RUSAGE_CHILDREN)
    return x.ru_utime+x.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def charged():return PRIOR+PREP+time.process_time()-START+child_cpu()
handle=dict(status='RUNNING',worker_count=1,prior_readgate_CPU_seconds=READGATE,prior_case_CPU_seconds=PRIOR,
    preparation_charge_seconds=PREP,cumulative_CPU_budget_seconds=CAP,no_timer_reset=True)
(OUT/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
compile_start=child_cpu()
with (OUT/'compile.log').open('w') as log:
    build=subprocess.run(['g++','-O2','-std=c++17',str(OUT/'run.cpp'),'-o',str(OUT/'run')],stdout=log,stderr=log)
compile_cpu=child_cpu()-compile_start
if build.returncode:
    result=dict(status='STOP_COMPILE_FAILURE',error='See compile.log',hit=False,
        whole_fixed_source_single_subdivision_family_excluded=False)
    run_cpu=0.
else:
    remaining=max(0.,CAP-charged()-.05)
    def child_limit():
        limit=max(1,math.ceil(remaining))
        resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
    run_start=child_cpu()
    with (OUT/'run.log').open('w') as log:
        run=subprocess.run([str(OUT/'run'),str(OUT.parent/'PRIMARY_360_ADJLIST.txt'),str(remaining),str(OUT)],
            stdout=log,stderr=log,preexec_fn=child_limit)
    run_cpu=child_cpu()-run_start
    if (OUT/'RAW_RESULT.json').is_file():result=json.loads((OUT/'RAW_RESULT.json').read_text())
    else:result=dict(status='UNKNOWN_WORKER_INTERRUPTED',returncode=run.returncode,hit=False,
        whole_fixed_source_single_subdivision_family_excluded=False)
result.update(prior_readgate_CPU_seconds=READGATE,prior_case_CPU_seconds=PRIOR,
    failed_format_attempt_inherited_without_timer_reset=True,
    source_literal_parses_cumulative=2,source_literal_successful_input_bindings=1,HTTP_download_calls_inherited=1,
    preparation_charge_seconds=PREP,
    actual_compile_CPU_seconds=compile_cpu,actual_run_child_CPU_seconds=run_cpu,
    driver_process_CPU_seconds=time.process_time()-START,cumulative_CPU_budget_seconds=CAP,
    worker_count=1,no_timer_reset=True,new_graph_parameter_Lean_increment_before_root_acceptance=[0,0,0],
    field_solver_Lean_ARIS_remote_install_hash=0,
    next='STOP_NOTIFY_ROOT_FRESH_ACCEPTANCE' if result.get('hit') else 'STOP_REPORT_EXACT_SCOPE_NO_MORE_SOURCE_OR_CUTS')
result['cumulative_charged_CPU_seconds']=charged()
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
nr=(OUT/'FIRST_NEWROOT_FAILURE.json')
oo=(OUT/'FIRST_OLDOLD_FAILURE.json')
detail=''
if nr.is_file():
    f=json.loads(nr.read_text());detail+='\nFirst newroot failure: '+json.dumps(f,ensure_ascii=False)+'\n'
if oo.is_file():
    f=json.loads(oo.read_text());detail+='\nFirst old-old failure and one old-source pair diagnostic: '+json.dumps(f,ensure_ascii=False)+'\n'
note=f'''# Chen360 single-edge subdivisions: actual bounded batch

Actual status:{result['status']}. Candidates finished:{result.get('candidates_finished',0)}/540.
NewrootR8 passes:{result.get('newroot_R8_passed',0)}; newroot rejections:{result.get('rejected_newroot_R8',0)};
old-old rejections:{result.get('rejected_old_old_D8',0)}.
Prediction for first rawedge{{1,141}} tested:{result.get('prediction_first_edge_newroot_tested',False)},
supported:{result.get('prediction_first_edge_newroot_supported',False)}.

Only this fixed source's literal single-edge subdivisions were considered. Each
candidate has361 vertices/541 edges, source raw1..360 maps to0..359, newroot360.
The primary literal had two parse attempts: an initial0candidate/0BFS attempt
incorrectly required increasing numeric neighbor labels, then this corrected
successful binding only requires each undirected edge occur once. The source
input is simple360/540 cubic; the prior2.419079713CPU cost is inherited. The
one successful normalized source input is saved; sourceD8 is not reverified.
There was only one HTTP source download. Every candidate receives actual final
newroot BFS, and only passes receive ordinary old-labelled BFS until failure.
No symmetry inference, random seed, hillclimb or second source is used.

The exact newroot gate is R7_(G-e)({{u,v}})=allold, equivalently R7_G({{u,v}})=allold;
old-old preservation is separate. A complete all540 negative excludes exactly
this source and edit rule. Incomplete budgets remain UNKNOWN. A complete hit
still requires root's fresh independent acceptance and latest baseline gate.
{detail}
One worker; prior readgate,preparation,compile,run and driver are charged under
the same20CPU case. No field,solver,Lean,ARIS,install or hash. Stop here; no
automatic continuation to another cut/source/template. Root alone updates
global graph counts and public claims.
'''
(OUT/'NOTE.md').write_text(note)
terminal=dict(status=result['status'],running=False,all_processes_terminal=True,worker_count=1,
    prior_readgate_CPU_seconds=READGATE,prior_case_CPU_seconds=PRIOR,
    source_literal_parses_cumulative=2,source_literal_successful_input_bindings=1,HTTP_download_calls_inherited=1,
    preparation_charge_seconds=PREP,
    actual_compile_CPU_seconds=compile_cpu,actual_run_child_CPU_seconds=run_cpu,
    driver_process_CPU_seconds=time.process_time()-START,
    cumulative_charged_CPU_seconds=charged(),cumulative_CPU_budget_seconds=CAP,
    no_timer_reset=True,no_automatic_continuation=True)
(OUT/'TERMINAL.json').write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(terminal,ensure_ascii=False,indent=2))

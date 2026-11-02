#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
SOURCE_DIR=ROOT/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single'
SOURCE=SOURCE_DIR/'source364.edges'
PORTS=json.loads((SOURCE_DIR/'PORT_BINDING.json').read_text())['eligible_ports']
BUDGET=20.0
PREP=0.2
initial=resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
def charged():return PREP+time.process_time()+child_cpu()
def save(name,value):(HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def limit(seconds):
    def setup():
        n=max(1,math.ceil(seconds));resource.setrlimit(resource.RLIMIT_CPU,(n,n+1))
    return setup
(HERE/'PORTS_INPUT.txt').write_text(' '.join(map(str,PORTS))+'\n')
save('INPUT.json',{'source':str(SOURCE.relative_to(ROOT)),'port_binding':str((SOURCE_DIR/'PORT_BINDING.json').relative_to(ROOT)),
                   'ports':PORTS,'source_n':364,'source_m':714,'source_D5':'INHERITED','source_degree_histogram':{'3':28,'4':336},
                   'source_or_port_ball_verification':False,'seed':202611010405,'sample_cap':10000,'CPU_budget_seconds':BUDGET})
save('HANDLE.json',{'pid':os.getpid(),'phase':'compile','running':True,'worker_count':1,'CPU_budget_seconds':BUDGET})
before=child_cpu()
with (HERE/'COMPILE.log').open('w') as log:
    p=subprocess.Popen(['g++','-O2','-std=c++17',str(HERE/'run.cpp'),'-o',str(HERE/'run')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(BUDGET-charged()-0.5))
    save('HANDLE.json',{'pid':os.getpid(),'child_pid':p.pid,'phase':'compile','running':True,'worker_count':1,'CPU_budget_seconds':BUDGET})
    code=p.wait()
compile_cpu=child_cpu()-before
if code:result={'status':'COMPILE_FAILED_NO_SAMPLE','exit_code':code}
else:
    remaining=BUDGET-charged()-0.6;before=child_cpu()
    with (HERE/'RUN.log').open('w') as log:
        p=subprocess.Popen([str(HERE/'run'),str(SOURCE),str(HERE/'PORTS_INPUT.txt'),str(HERE),str(remaining)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(remaining+0.2))
        save('HANDLE.json',{'pid':os.getpid(),'child_pid':p.pid,'phase':'one_fixed_seed_candidate_sample','running':True,'worker_count':1,'CPU_budget_seconds':BUDGET,'actual_compile_CPU_seconds':compile_cpu,'run_CPU_limit_seconds':remaining})
        code=p.wait()
    run_cpu=child_cpu()-before
    result=json.loads((HERE/'RAW_RESULT.json').read_text()) if code==0 else {'status':'PROCESS_INTERRUPTED_SAMPLE_UNKNOWN','exit_code':code}
    result['actual_run_child_CPU_seconds']=run_cpu
result.update({'prediction':'At least one sampled configuration passes newrootR5;oldold still separate.',
               'prediction_newroot_supported':result.get('newroot_R5_passed',0)>0,
               'source_n':364,'source_m':714,'source_degree_histogram':{'3':28,'4':336},
               'target_n':365,'target_m':730,'target_degree':4,'target_D':5,
               'oldsource_edges_retained':712,'oldsource_edges_deleted':2,'new_port_matching_edges':14,'newroot_core_edges':4,
               'exact_rule':'Perfectmatching of28oldports;two disjoint OLD core-coreedgecuts;one4star tothosefourendpoints.',
               'whole_rule_exclusion':False,'scope':'One fixedseed sample ofatmost10000distinct matching+two-cut configurations.',
               'source_validity_BFS_portballs_field_solver_Lean_ARIS_hash_remote':0,
               'preparation_charge_seconds':PREP,'actual_compile_CPU_seconds':compile_cpu,'driver_process_CPU_seconds':time.process_time(),
               'total_charged_CPU_seconds':charged(),'CPU_budget_seconds':BUDGET,'worker_count':1,
               'root_Wiki_modified':False,'new_graph_parameter_Lean_increment_before_root_acceptance':[0,0,0],
               'next':'STOP_REPORT_NO_MORECUTS_SEED_SAMPLES_OR_H14'})
if result.get('hit'):
    hit=json.loads((HERE/'HIT.json').read_text())
    save('PARAMETERS.json',{'n':365,'m':730,'degree':4,'actual_diameter':hit['actual_diameter'],
                           'source':str(SOURCE.relative_to(ROOT)),'port_binding':str((SOURCE_DIR/'PORT_BINDING.json').relative_to(ROOT)),
                           'new_label':364,'configuration':hit['configuration'],'source_edges_deleted':2,'original_edges_retained':712,
                           'added_old_port_matching_edges':14,'newroot_core_edges':4,'all_final_BFS_roots':365,
                           'actual_distance_witness':hit['actual_distance_witness'],'root_acceptance':'PENDING','priority':'UNKNOWN'})
    result['actual_diameter']=hit['actual_diameter']
    result['complete_final_BFS_roots']=365
save('RESULT.json',result)
note=f'''# Natural364 portmatching plus two corecut sample

Actual status:{result['status']}. Distinct finished configurations:{result.get('distinct_configurations_finished',0)}. NewrootR5 passes:{result.get('newroot_R5_passed',0)};rejected newroot:{result.get('rejected_newroot_R5',0)};subsequent old-old failures:{result.get('rejected_old_old',0)}. Each rejection is only a sampled configuration. ATTEMPTS.csv records stages;MATCHING_AND_CUTS.csv records everycomplete edit rule. RESULT saves firstactualdistance counterexamples and any winning parameters.

The old host is the natural364/714 polarity graph, not the public364/728 regular graph. SourceD5,degree/ports and spacing are inherited. Only theliteral source is parsed once as constructioninput;no sourceBFS orportballs/field/geometry checks are repeated. Old pureappend and≤13helper exclusions forbid botholdedge deletions andold-old additions;this rule changes both and is outside those scopes.

Degreeaccounting is exact:all28 ports gainone matchingedge;four distinctcore cutendpoints loseone andgainone via newlabel364. Everyothercore stays4,asdoes the4star center. Target365/730 retains exactly712 of714oldedges. Perfectmatching oldport pairs are inherited nonedges. Newold shortcuts can supplement lostoldroutes;newroot coverage andold-old preservation are tested separately on each finalcandidate. Fullsuccess requires newrootplusall364old-labelled ordinaryBFS roots,not a fewroot sample. Anyhit remainsroot-acceptancepending.

Prediction of some newrootR5pass was {'supported' if result.get('prediction_newroot_supported') else 'not supported in this sample'}. No-hitis sampleUNKNOWN,not an exhaustivefamilyNO. Sample/CPUcap has no continuationauthorization. This batch stops before othermatching/cut patterns,seedchanges orH14.

Totalcharged{charged():.9f}/20CPU includes preparation0.2,compiler{compile_cpu:.9f},runanddriver,oneworker. No solver,Lean,ARIS,remote,install,hash,root/Wiki edits. PAPER_INTERFACE.md supplies independent paper-only scope androute analysis.
'''
(HERE/'NOTE.md').write_text(note)
terminal={'status':result['status'],'running':False,'all_processes_terminal':True,'worker_count':1,
          'preparation_charge_seconds':PREP,'actual_compile_CPU_seconds':compile_cpu,'actual_run_child_CPU_seconds':result.get('actual_run_child_CPU_seconds',0),
          'driver_process_CPU_seconds':time.process_time(),'total_charged_CPU_seconds':charged(),'CPU_budget_seconds':BUDGET,
          'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal);save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False,indent=2))

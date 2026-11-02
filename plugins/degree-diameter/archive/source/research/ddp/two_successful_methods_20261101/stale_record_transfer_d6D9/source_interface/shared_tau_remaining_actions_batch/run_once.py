#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
DOMAIN=json.loads((HERE/'DOMAIN.json').read_text())
PRIOR=DOMAIN['prior_case_CPU_seconds']
PREP=DOMAIN['new_preparation_charge_seconds']
BUDGET=90.0
initial=resource.getrusage(resource.RUSAGE_CHILDREN)
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
def charged():return PRIOR+PREP+time.process_time()+child_cpu()
def save(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def limit(seconds):
    def setup():
        n=max(1,math.ceil(seconds));resource.setrlimit(resource.RLIMIT_CPU,(n,n+1))
    return setup
completed=[]
active=None
def checkpoint(phase,child_pid=None):
    pending=[p for p in DOMAIN['remaining_domains'] if p['representative_beta'] not in {r['beta'] for r in completed}]
    data={'pid':os.getpid(),'child_pid':child_pid,'phase':phase,'running':phase!='terminal',
          'worker_count':1,'prior_case_CPU_seconds':PRIOR,'cumulative_charged_CPU_seconds':charged(),
          'cumulative_CPU_budget_seconds':BUDGET,'active_domain':active,'completed_domain_receipts':completed,
          'uncompleted_domains':pending,'compilation_count':1}
    save(HERE/'HANDLE.json',data)
    save(HERE/'CHECKPOINT.json',data)

checkpoint('compile')
before=child_cpu()
with (HERE/'COMPILE.log').open('w') as log:
    p=subprocess.Popen(['g++','-O3','-std=c++17',str(HERE/'run.cpp'),'-o',str(HERE/'run_beta')],
                       stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(BUDGET-charged()-0.8))
    checkpoint('compile',p.pid)
    code=p.wait()
compile_cpu=child_cpu()-before
batchstatus='COMPILE_FAILED_NO_NEW_DOMAIN' if code else 'UNKNOWN_UNSTARTED_DOMAINS'
hit_path=None
if not code:
    for item in DOMAIN['remaining_domains']:
        remaining=BUDGET-charged()-0.8
        if remaining<1.0:
            batchstatus='UNKNOWN_CUMULATIVE_CPU_CAP'
            break
        beta=item['representative_beta'];inverse=item['inverse_beta']
        path=HERE/f'beta_{beta:04d}'
        path.mkdir(exist_ok=True)
        active={'beta':beta,'inverse_beta':inverse,'path':str(path.relative_to(HERE))}
        save(path/'INPUT.json',{'field':6959,'beta':beta,'inverse_action':inverse,'phase_modulus':49,
                               'positive_phases':[1,36,45],'new_representative_count':6959,
                               'old_tau1512_skipped':True,'zero_paper_only':True,
                               'runtime_program':'../run_beta','run_CPU_limit_seconds':remaining})
        before=child_cpu()
        with (path/'RUN.log').open('w') as log:
            process=subprocess.Popen([str(HERE/'run_beta'),str(path),str(remaining),str(beta)],
                                     stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit(remaining+0.25))
            checkpoint('runtime_action_domain',process.pid)
            save(path/'HANDLE.json',{'pid':process.pid,'driver_pid':os.getpid(),'running':True,
                                     'phase':'new_endpoint_form_domain','beta':beta,'worker_count':1,
                                     'cumulative_case_CPU_budget_seconds':BUDGET})
            ret=process.wait()
        run_cpu=child_cpu()-before
        if ret:
            result={'status':'PROCESS_INTERRUPTED_DOMAIN_UNKNOWN','exit_code':ret,'beta':beta,
                    'new_representatives_unresolved':'See any partial status;do not inferNO'}
        else:
            result=json.loads((path/'RAW_RESULT.json').read_text())
        p0=json.loads((path/'PHASE0_RESULT.json').read_text()) if (path/'PHASE0_RESULT.json').exists() else None
        p0summary={k:v for k,v in p0.items() if k!='survivors'} if p0 else None
        result.update({'inverse_action':inverse,'field':6959,'positive_phases':[1,36,45],
                       'phase0_actual_summary':p0summary,'actual_run_child_CPU_seconds':run_cpu,
                       'normalization':'Firstnormal0;P1(F6959) residual normal pair+zero;old1512 andzero inherited.',
                       'inverse_action_scope':'CompletefamilyNO transports beta→beta^-1;finite tau→tau*beta^-9 bijectively. Not a second numeric evaluation.',
                       'inverse_phase_scope':'U_-j=-beta^-j*U_j;phase0..24 suffice for a positiveallphase cover.',
                       'old_scalar1512_control_or_source_BFS_repeated':False,
                       'graph_BFS_solver_Lean_ARIS_hash_install':0,
                       'cumulative_case_CPU_seconds_after_domain':charged(),
                       'cumulative_case_CPU_budget_seconds':BUDGET,'worker_count':1})
        save(path/'RESULT.json',result)
        terminal={'status':result['status'],'running':False,'all_processes_terminal':True,
                  'beta':beta,'inverse_action':inverse,'actual_run_child_CPU_seconds':run_cpu,
                  'cumulative_case_CPU_seconds':charged(),'cumulative_case_CPU_budget_seconds':BUDGET,
                  'worker_count':1,'no_timer_reset':True}
        save(path/'TERMINAL.json',terminal)
        save(path/'HANDLE.json',terminal)
        outcome={'beta':beta,'inverse_beta':inverse,'status':result['status'],
                 'phase0_survivors':p0summary.get('phase0_survivor_count') if p0summary else None,
                 'new_representatives_rejected':result.get('new_representatives_rejected'),
                 'new_representatives_unresolved':result.get('new_representatives_unresolved'),
                 'representative_phase_evaluations':result.get('representative_phase_evaluations'),
                 'last_phase_domain_completed':result.get('last_phase_domain_completed'),
                 'actual_run_child_CPU_seconds':run_cpu,'receipt':str((path/'RESULT.json').relative_to(HERE))}
        completed.append(outcome)
        note=f'''# Runtime action{beta}, inverse-action partner{inverse}

Actual status:{result['status']}. New domain:6958 finite tau except1512 plus infinity, with old1512NO and allzero-disconnected inherited. Actual phase0 summary:{p0summary}. Every failed representative has its checkedphase mask and one complete missing-endpoint witness in REPRESENTATIVE_STATUS.csv. FORM_COUNTS.csv and COEFFICIENT_FORMS.u32 retain this action's newly generated homogeneous forms.

RIGHT update(A,B)→(A beta^a+A_d,B beta^a+B_d) and true inverse coefficients are used. One missingphase excludes a representative; a positiveallphase claim would use inverse-word coverage of±phases. A completefamilyNO transports to partner{inverse} via the paper inverse-action bijection; numeric computations were only performed for{beta}, not both actions. No conclusion is extended to otherfields orphase sets.

One shared executable was compiled once for this20-domain batch. This domain childCPU{run_cpu:.9f}; cumulativecase{charged():.9f}/90CPU, including oldcase, sharedprep/compile and precedingdomains. No oldsource/field/order/scalar1512 control, graphBFS, solver, ARIS, Lean or review was rerun. Root alone accepts graphs. See ../PRED.md and ../PAPER_BATCH_DOMAIN.md.
'''
        (path/'NOTE.md').write_text(note)
        print('DOMAIN_DONE '+json.dumps(outcome,separators=(',',':'))+' CUMULATIVE_CPU='+f'{charged():.9f}',flush=True)
        checkpoint('between_domains')
        if result.get('hit'):
            rep=result['hit_representative'];b,c=(0,1) if rep=='infinity' else (1,int(rep))
            positives=[[1,0],[36,b],[45,c]]
            inverses=[[(-a)%49,(-normal*pow(beta,(-a)%49,6959))%6959] for a,normal in positives]
            save(path/'PARAMETERS.json',{'n':340991,'m':1022973,'maximum_degree':6,'diameter_at_most':9,'exact_diameter':None,
                                         'field':6959,'phase_modulus':49,'beta':beta,'positive_generators':positives,
                                         'inverse_generators':inverses,'RIGHT_law':'(j,n)*(a,c)=(j+a,n*beta^a+c)',
                                         'label':'6959*j+n','word_cover_receipt':'RESULT.json','graph':'graph_d6_D9_n340991.edges',
                                         'BFS':0,'root_acceptance':'PENDING'})
            hit_path=str(path.relative_to(HERE));batchstatus='FIRST_COMPLETE_WORD_COVER_TARGET_PENDING_ROOT_ACCEPTANCE'
            print('GRAPH_READY '+str(path/'graph_d6_D9_n340991.edges'),flush=True)
            break
        if result['status']!='COMPLETE_NO_RUNTIME_ACTION_ALL_NORMAL_TRANSLATIONS_D9':
            batchstatus='UNKNOWN_PARTIAL_PROJECTIVE_OR_UNSTARTED_DOMAIN'
            break
    else:
        batchstatus='COMPLETE_NO_PRIMITIVE49_F6959_FIXED_PHASE_ALL_NORMAL_FAMILY'

completed_no=[r for r in completed if r['status']=='COMPLETE_NO_RUNTIME_ACTION_ALL_NORMAL_TRANSLATIONS_D9']
active=None
summary={'status':batchstatus,'new_representative_domains_completed':len(completed_no),
         'new_numeric_actions_run':len(completed),'planned_new_numeric_actions':20,
         'completed_domains':completed,'remaining_uncompleted_domains':[p for p in DOMAIN['remaining_domains'] if p['representative_beta'] not in {r['beta'] for r in completed}],
         'previous_closed_inverse_pair':DOMAIN['previous_complete_pair'],'hit_path':hit_path,
         'complete42_primitive_action_coverage':len(completed_no)==20,
         'new_numeric_representatives_rejected':sum(r.get('new_representatives_rejected',0) or 0 for r in completed),
         'old1512_andzero_inherited':True,'old_field_primitiveorder_or_sourceD9_rechecked':False,
         'exact_scope':'Only F6959,primitive exactorder49 actions,fixed positivephases1/36/45,all three normal translations modulo commonconjugation/scale.',
         'not_excluded':['action order7 or1','otherfields','otherphase triples/controllers','otherCayley connectionsets','general degree6/D9 graphs'],
         'compilation_count':1,'actual_compile_CPU_seconds':compile_cpu,
         'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
         'driver_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),
         'cumulative_CPU_budget_seconds':BUDGET,'worker_count':1,
         'source_BFS_solver_Lean_ARIS_hash_install':0,'root_Wiki_modified':False,
         'new_graph_parameter_Lean_increment_before_root_acceptance':[0,0,0],
         'next':'STOP_REASSESS_NO_AUTOMATIC_NEXT_Q_ACTION_OR_TEMPLATE'}
save(HERE/'RESULT.json',summary)
lines=['# Remaining primitive action batch','',f'Actualstatus:{batchstatus}.',
       f'Newnumeric domains:{len(completed)};completeNO domains:{len(completed_no)};onecompilation. Eachcompleted domain has itsownRESULT/NOTE/TERMINAL,perparameter failedphase witnesses,andfull homogeneous form data.',
       '', 'The saved42 primitiveactions are partitioned into21 inversepairs. The earlier complete5155/2789 pair is inherited. Each newrepresentative covers6959 newprojective normal choices,withtau1512NO/zeroNO inherited. A completefamilyNO covers itsinverse action through the provedtau bijection; actualnumeric work is never doubled in thecounts.',
       '', 'The parameterorder andphaseorder are fixed. No missing-point score selects anotheraction oradjustsatau. Everynegative representative has anactualcomplete missingphase,whilepartial/unvisited domains remainUNKNOWN. Anallphase word-cover hit permits onecandidate butstillrequiresroot independent acceptance. This is a finitefamily result,not a closureof general(6,9).',
       '',f'Budgetinherits{PRIOR:.9f};newsharedprep{PREP},compiler{compile_cpu:.9f},all childruntimesanddriverCPU included. Actual cumulative{charged():.9f}/90CPU. No timerreset,oldsource6763/D9 oroldfixed1512 controls,field/order validation,ramified6860,subdivision,BFS,solver,Lean,ARIS,hashorinstall wasrun.',
       '', 'The batch stops here. Order7/1 actions,otherfields/controllers/phases remainoutside;no newqueue is started.']
(HERE/'NOTE.md').write_text('\n\n'.join(lines)+'\n')
terminal={'status':batchstatus,'running':False,'all_processes_terminal':True,'worker_count':1,
          'compilation_count':1,'actual_compile_CPU_seconds':compile_cpu,'prior_case_CPU_seconds':PRIOR,
          'new_preparation_charge_seconds':PREP,'driver_process_CPU_seconds':time.process_time(),
          'cumulative_charged_CPU_seconds':charged(),'cumulative_CPU_budget_seconds':BUDGET,
          'new_numeric_action_count':len(completed),'no_timer_reset':True,'no_automatic_continuation':True}
save(HERE/'TERMINAL.json',terminal)
checkpoint('terminal')
print('BATCH_TERMINAL '+json.dumps(terminal,separators=(',',':')),flush=True)

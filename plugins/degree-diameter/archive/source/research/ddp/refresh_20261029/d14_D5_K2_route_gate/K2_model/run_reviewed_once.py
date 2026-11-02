#!/usr/bin/env python3
"""Root-review entry: one shared-budget CEGIS batch, never run by preparation."""
import argparse
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import time
from common import HERE,ROOT,N,K,load_context,dump,evaluate,save_hit,missing_labels,coverage_row

parser=argparse.ArgumentParser()
mode=parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--solve',action='store_true')
mode.add_argument('--resume-remaining-budget',action='store_true')
args=parser.parse_args()
resume=args.resume_remaining_budget
model=json.loads((HERE/'MODEL.json').read_text())
assert model['status']=='K2_CNF_PREPARED_NOT_SOLVED'
# Charge the entire new Python process CPU, including imports and input parsing.
start=0.0;wall=time.monotonic()
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
prior=None
if resume:
    history=HERE/'stage2_history'
    plan=json.loads((HERE/'RESUME_PLAN.json').read_text())
    prior=json.loads((history/'SOLVER_RESULT.json').read_text())
    checkpoint=json.loads((history/'CHECKPOINT.json').read_text())
    assert plan['same_original_batch'] and plan['first_resume_round']==3
    assert prior['running'] is False and prior['solver_calls']==2
    assert prior['status']=='UNKNOWN_SOLVER_RETURN' and prior['rounds'][0]['code']==10
    assert prior['rounds'][-1]['round']==2 and prior['rounds'][-1]['status']=='UNKNOWN'
    assert prior['solver_CPU_seconds']==plan['prior_solver_CPU_seconds']
    assert prior['whole_batch_CPU_seconds']==plan['prior_whole_batch_CPU_seconds']
    prior_calls=prior['solver_calls'];prior_solver=prior['solver_CPU_seconds']
    prior_whole=prior['whole_batch_CPU_seconds'];prior_driver=prior['driver_CPU_seconds']
    rounds=list(prior['rounds'])
    rows=sorted(tuple(r) for r in checkpoint['active_rows'])
    assert len(rows)==len(set(rows))==1188
    assert prior['rounds'][-1]['active_exact_coverage_rows']==len(rows)
    source_cnf=history/'round_02.cnf'
    names=dict(handle='RESUME_HANDLE.json',result='RESUME_SOLVER_RESULT.json',terminal='RESUME_SOLVER_TERMINAL.json',checkpoint='RESUME_CHECKPOINT.json',live='RESUME_LIVE_ROUND.json')
else:
    prior_calls=0;prior_solver=0.0;prior_whole=model['gate_and_prepare_CPU_seconds'];prior_driver=0.0
    rounds=[]
    rows=sorted(tuple(r) for r in json.loads((HERE/'INITIAL_ROWS.json').read_text())['rows'])
    source_cnf=HERE/'model_initial.cnf'
    names=dict(handle='HANDLE.json',result='SOLVER_RESULT.json',terminal='SOLVER_TERMINAL.json',checkpoint='CHECKPOINT.json',live='LIVE_ROUND.json')
assert not (HERE/names['handle']).exists() and not (HERE/names['terminal']).exists(), 'This invocation stage already has a handle or terminal.'
assert prior_calls<6 and prior_solver<60 and prior_whole<90
def new_solver_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def solver_cpu():return prior_solver+new_solver_cpu()
def total_cpu():return prior_whole+time.process_time()-start+new_solver_cpu()
def window_left():
    cap=float('inf') if resume else 15
    return math.floor(min(cap,60-solver_cpu()-1,90-total_cpu()-2))
ctx=load_context()
active=set(rows);cached_rows={}
with source_cnf.open() as f:
    assert next(f).strip()==f"p cnf {model['all_variables']} {model['base_clauses']+len(rows)}"
    for _ in range(model['base_clauses']):next(f)
    for row in rows:cached_rows[row]=next(f)
    assert not f.read().strip()
dump(names['handle'],dict(status='RUNNING_SAME_K2_BATCH_REMAINING_BUDGET' if resume else 'RUNNING_SOLE_K2_CEGIS_BATCH',pid=os.getpid(),maximum_total_calls=6,shared_solver_CPU_budget=60,whole_batch_CPU_budget=90,prior_solver_calls=prior_calls,prior_solver_CPU_seconds=prior_solver,prior_whole_batch_CPU_seconds=prior_whole,restored_active_rows=len(rows),first_round=prior_calls+1,first_input_cnf=str(source_cnf)))
calls=prior_calls;new_checks=0;status='UNKNOWN';hit=False;error=None
try:
    for number in range(prior_calls+1,7):
        # A whole-second reserve absorbs process startup and CPU-limit granularity.
        window=window_left()
        if window<1:
            status='UNKNOWN_SHARED_BUDGET_STOP';break
        if resume and number==prior_calls+1:
            # Exact same round2 CNF; no row is dropped or rebuilt for the continuation.
            cnf=source_cnf
        else:
            cnf=HERE/f'round_{number:02d}.cnf'
            with cnf.open('w') as out:
                out.write(f"p cnf {model['all_variables']} {model['base_clauses']+len(active)}\n")
                with (HERE/'base_cardinality.clauses').open() as f:
                    for chunk in iter(lambda:f.read(1024*1024),''):out.write(chunk)
                for row in sorted(active):out.write(cached_rows[row])
        # Regenerate the window after encoding, so file generation cannot consume
        # time that had already been allocated to a solver call.
        window=window_left()
        if window<1:
            status='UNKNOWN_ENCODING_BUDGET_STOP';break
        log=HERE/f'round_{number:02d}.solver.stdout'
        command=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t',str(window),str(cnf)]
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU,(window,window))
        before=solver_cpu();w0=time.monotonic();expired=False;observation_timeouts=0
        with log.open('w') as output:
            proc=subprocess.Popen(command,stdout=output,stderr=output,preexec_fn=limits)
            calls+=1
            dump(names['live'],dict(round=number,pid=proc.pid,command=command,window_seconds=window,solver_CPU_before=before,whole_CPU_before=total_cpu()))
            while True:
                try:
                    code=proc.wait(timeout=window+5)
                    break
                except subprocess.TimeoutExpired:
                    expired=True;observation_timeouts+=1
                    dump(names['live'],dict(status='OBSERVATION_TIMEOUT_SAME_PID_STILL_RUNNING',round=number,pid=proc.pid,command=command,window_seconds=window,observation_timeouts=observation_timeouts,solver_CPU_before=before))
        item=dict(round=number,code=code,window_seconds=window,solver_CPU_seconds=solver_cpu()-before,solver_CPU_cumulative=solver_cpu(),wall_seconds=time.monotonic()-w0,observation_expired=expired,observation_timeouts=observation_timeouts,active_exact_coverage_rows=len(active),full_target_model=len(active)==2*N,input_cnf=str(cnf),same_batch_resume=resume)
        if code==20:
            item['status']='RAW_UNSAT_UNCERTIFIED';rounds.append(item);status='RAW_UNSAT_UNCERTIFIED_K2_FAMILY';break
        if code!=10:
            item['status']='UNKNOWN';rounds.append(item);status='UNKNOWN_SOLVER_RETURN';break
        positive=set()
        for line in log.read_text().splitlines():
            if line.startswith('v '):positive.update(int(x) for x in line[2:].split() if int(x)>0)
        A=[j for j in range(K) if j+1 in positive]
        B=[j for j in range(K) if K+j+1 in positive]
        ev=evaluate(ctx,A,B)
        new_checks+=1
        assert all(not (ev['missing'][side]>>t&1) for side,t in active)
        item.update(status='SAT_COMPLETE_CACHED_CHECK',A=[ctx['free'][j] for j in A],B=[ctx['free'][j] for j in B],root_missing_counts=[m.bit_count() for m in ev['missing']],single_helper_R4_full=ev['single'])
        dump(f'round_{number:02d}.candidate.json',dict(item,root_missing_targets=[missing_labels(m) for m in ev['missing']],ordinary_graph_bad_pairs_not_computed=True))
        if save_hit(ctx,A,B,ev,f'SAT_round_{number}'):
            item['hit']=True;rounds.append(item);status='CACHED_PRODUCTION_HIT_PENDING_ROOT_ACCEPTANCE';hit=True;break
        added=[]
        for side in (0,1):
            violated=sorted(missing_labels(ev['missing'][side]),key=lambda t:(ctx['combined'][t],t))
            for t in violated[:256]:
                row=(side,t)
                assert row not in active
                active.add(row)
                cached_rows[row]=' '.join(map(str,coverage_row(ctx,side,t)))+' 0\n'
                added.append(row)
        assert added
        item['exact_violated_rows_added']=[list(r) for r in added]
        rounds.append(item)
        dump(names['checkpoint'],dict(status='CEGIS_COUNTEREXAMPLE_REFINED',rounds=rounds,active_rows=[list(r) for r in sorted(active)],solver_calls=calls,solver_CPU_seconds=solver_cpu(),whole_batch_CPU_seconds=total_cpu(),same_original_batch=True,prior_solver_calls=prior_calls))
        status='UNKNOWN_MAXIMUM_ROUNDS' if number==6 else 'UNKNOWN_PENDING_NEXT_ROUND'
except Exception as exc:
    status='STOPPED_IMPLEMENTATION_OR_INPUT_ERROR';error=repr(exc)
finally:
    driver_new=time.process_time()-start;solver_new=new_solver_cpu()
    result=dict(status=status,running=False,rounds=rounds,solver_calls=calls,solver_CPU_seconds=prior_solver+solver_new,driver_CPU_seconds=prior_driver+driver_new,gate_and_prepare_CPU_seconds=model['gate_and_prepare_CPU_seconds'],whole_batch_CPU_seconds=prior_whole+driver_new+solver_new,shared_solver_CPU_budget=60,whole_batch_CPU_budget=90,maximum_rounds=6,full_source_two_root_checks=(prior.get('full_source_two_root_checks',0) if prior else 0)+new_checks,source_reads=0,new_R3_runs=0,new_R4_runs=0,source_D5_BFS=0,graphs_exported=0,cached_full_cover_hit=hit,error=error,pending=['Root independent acceptance'] if hit else [],same_original_batch=True,resume_remaining_budget=resume,prior_solver_calls=prior_calls,new_solver_calls=calls-prior_calls,prior_solver_CPU_seconds=prior_solver,new_solver_CPU_seconds=solver_new,prior_whole_batch_CPU_seconds=prior_whole,new_driver_CPU_seconds=driver_new,old_stage2_records_preserved=resume)
    dump(names['result'],result);dump(names['terminal'],result)
    dump(names['handle'],dict(status='TERMINAL_SAME_K2_BATCH_REMAINDER' if resume else 'TERMINAL_SOLE_K2_BATCH',solver_calls=calls,new_solver_calls=calls-prior_calls,result=names['result']))
    print(json.dumps({k:result[k] for k in ['status','solver_calls','new_solver_calls','solver_CPU_seconds','whole_batch_CPU_seconds','new_driver_CPU_seconds','cached_full_cover_hit','error']}),flush=True)

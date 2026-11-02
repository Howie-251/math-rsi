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
parser.add_argument('--solve',action='store_true',required=True)
args=parser.parse_args()
assert args.solve
assert not (HERE/'HANDLE.json').exists() and not (HERE/'SOLVER_TERMINAL.json').exists(), 'The sole batch already has a handle or terminal.'
model=json.loads((HERE/'MODEL.json').read_text())
assert model['status']=='K2_CNF_PREPARED_NOT_SOLVED'
start=time.process_time();wall=time.monotonic()
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
def solver_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def total_cpu():return model['gate_and_prepare_CPU_seconds']+time.process_time()-start+solver_cpu()
ctx=load_context()
rows=[tuple(r) for r in json.loads((HERE/'INITIAL_ROWS.json').read_text())['rows']]
active=set(rows);cached_rows={}
with (HERE/'model_initial.cnf').open() as f:
    next(f)
    for _ in range(model['base_clauses']):next(f)
    for row in rows:cached_rows[row]=next(f)
    assert not f.read().strip()
dump('HANDLE.json',dict(status='RUNNING_SOLE_K2_CEGIS_BATCH',pid=os.getpid(),maximum_calls=6,shared_solver_CPU_budget=60,whole_batch_CPU_budget=90))
rounds=[];calls=0;status='UNKNOWN';hit=False;error=None
try:
    for number in range(1,7):
        remaining_solver=60-solver_cpu();remaining_total=90-total_cpu()
        # A whole-second reserve absorbs process startup and CPU-limit granularity.
        window=int(min(15,math.floor(remaining_solver-1),math.floor(remaining_total-2)))
        if window<1:
            status='UNKNOWN_SHARED_BUDGET_STOP';break
        cnf=HERE/f'round_{number:02d}.cnf'
        with cnf.open('w') as out:
            out.write(f"p cnf {model['all_variables']} {model['base_clauses']+len(active)}\n")
            with (HERE/'base_cardinality.clauses').open() as f:
                for chunk in iter(lambda:f.read(1024*1024),''):out.write(chunk)
            for row in sorted(active):out.write(cached_rows[row])
        # Regenerate the window after encoding, so file generation cannot consume
        # time that had already been allocated to a solver call.
        window=int(min(15,math.floor(60-solver_cpu()-1),math.floor(90-total_cpu()-2)))
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
            dump('LIVE_ROUND.json',dict(round=number,pid=proc.pid,command=command,window_seconds=window,solver_CPU_before=before))
            while True:
                try:
                    code=proc.wait(timeout=window+5)
                    break
                except subprocess.TimeoutExpired:
                    expired=True;observation_timeouts+=1
                    dump('LIVE_ROUND.json',dict(status='OBSERVATION_TIMEOUT_SAME_PID_STILL_RUNNING',round=number,pid=proc.pid,command=command,window_seconds=window,observation_timeouts=observation_timeouts,solver_CPU_before=before))
        item=dict(round=number,code=code,window_seconds=window,solver_CPU_seconds=solver_cpu()-before,solver_CPU_cumulative=solver_cpu(),wall_seconds=time.monotonic()-w0,observation_expired=expired,observation_timeouts=observation_timeouts,active_exact_coverage_rows=len(active),full_target_model=len(active)==2*N)
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
        dump('CHECKPOINT.json',dict(status='CEGIS_COUNTEREXAMPLE_REFINED',rounds=rounds,active_rows=[list(r) for r in sorted(active)],solver_CPU_seconds=solver_cpu(),whole_batch_CPU_seconds=total_cpu()))
        status='UNKNOWN_MAXIMUM_ROUNDS' if number==6 else 'UNKNOWN_PENDING_NEXT_ROUND'
except Exception as exc:
    status='STOPPED_IMPLEMENTATION_OR_INPUT_ERROR';error=repr(exc)
finally:
    result=dict(status=status,running=False,rounds=rounds,solver_calls=calls,solver_CPU_seconds=solver_cpu(),driver_CPU_seconds=time.process_time()-start,gate_and_prepare_CPU_seconds=model['gate_and_prepare_CPU_seconds'],whole_batch_CPU_seconds=total_cpu(),shared_solver_CPU_budget=60,whole_batch_CPU_budget=90,maximum_rounds=6,full_source_two_root_checks=sum(r.get('code')==10 for r in rounds),source_reads=0,new_R3_runs=0,new_R4_runs=0,source_D5_BFS=0,graphs_exported=0,cached_full_cover_hit=hit,error=error,pending=['Root independent acceptance'] if hit else [])
    dump('SOLVER_RESULT.json',result);dump('SOLVER_TERMINAL.json',result)
    dump('HANDLE.json',dict(status='TERMINAL_SOLE_K2_BATCH',solver_calls=calls,result='SOLVER_RESULT.json'))
    print(json.dumps(result),flush=True)

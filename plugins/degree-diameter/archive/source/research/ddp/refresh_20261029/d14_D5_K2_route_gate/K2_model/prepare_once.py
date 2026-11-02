#!/usr/bin/env python3
import json
import time
from common import HERE,BASE,N,K,FULL,load_context,dump,evaluate,save_hit,missing_labels,coverage_row

start=time.process_time()
assert not (HERE/'MODEL.json').exists() and not (HERE/'PREPARE_TERMINAL.json').exists()
ctx=load_context()
# One deterministic greedy control, including single-helper checks.
selected=[[],[]];used=[set(),set()];usage=[0]*K;own4=[0,0];own3=[0,0];trace=[];hit=False
for step in range(26):
    misses=[FULL&~(own4[0]|own3[1]),FULL&~(own4[1]|own3[0])]
    best=None
    for side in (0,1):
        if len(selected[side])==13:continue
        for j in range(K):
            if j in used[side] or usage[j]>=ctx['spare'][j]:continue
            own=(ctx['b4'][j]&misses[side]).bit_count()
            other=(ctx['b3'][j]&misses[1-side]).bit_count()
            item=(own+other,-side,-ctx['free'][j],side,j,own,other)
            if best is None or item[:3]>best[:3]:best=item
    if best is None or best[0]==0:break
    _,_,_,side,j,own,other=best
    selected[side].append(j);used[side].add(j);usage[j]+=1
    own4[side]|=ctx['b4'][j];own3[side]|=ctx['b3'][j]
    trace.append(dict(step=step+1,side='AB'[side],pin=ctx['free'][j],gain=own+other,own_R4_gain=own,opposite_R3_gain=other))
    ev=evaluate(ctx,*selected)
    if save_hit(ctx,*selected,ev,'unique_deterministic_greedy'):
        hit=True;break
ev=evaluate(ctx,*selected)
greedy=dict(status='HIT_PENDING_ROOT_ACCEPTANCE' if hit else 'ONE_GREEDY_CONTROL_NO_FULL_COVER',A=[ctx['free'][j] for j in selected[0]],B=[ctx['free'][j] for j in selected[1]],A_indices=selected[0],B_indices=selected[1],trace=trace,single_helper_full_R4=ev['single'],root_missing_counts=[m.bit_count() for m in ev['missing']],root_missing_targets=[missing_labels(m) for m in ev['missing']],root_missing_in_T0=[0,0],own_R4_missing_counts=[(FULL&~r).bit_count() for r in ev['own4']],missing_legacy9754_counts=[sum(bool(m>>t&1) for t in ctx['legacy']) for m in ev['missing']],ordinary_graph_bad_pairs_not_computed=True,greedy_restarts=0,local_swaps=0)
dump('GREEDY_CONTROL.json',greedy)
if hit:
    dump('PREPARE_TERMINAL.json',dict(status='GREEDY_HIT_STOP_BEFORE_CNF',CPU_seconds=time.process_time()-start,solver_calls=0,pending=['Root independent acceptance']))
    print(json.dumps({'status':'GREEDY_HIT_STOP_BEFORE_CNF','A':greedy['A'],'B':greedy['B'],'single':ev['single']}),flush=True)
    raise SystemExit

variables=2*K;clauses=0
with (HERE/'base_cardinality.clauses').open('w') as f:
    def fresh():
        global variables
        variables+=1;return variables
    def clause(xs):
        global clauses
        f.write(' '.join(map(str,xs))+' 0\n');clauses+=1
    for side in (0,1):
        previous=None
        for j in range(K):
            x=1+side*K+j;cur=[fresh() for _ in range(13)]
            clause([-x,cur[0]])
            if previous is None:
                for z in cur[1:]:clause([-z])
            else:
                for p,q in zip(previous,cur):clause([-p,q])
                for k in range(1,13):clause([-x,-previous[k-1],cur[k]])
                clause([-x,-previous[12]])
            previous=cur
    for j,cap in enumerate(ctx['spare']):
        if cap==1:clause([-(1+j),-(1+K+j)])
base_clauses=clauses
global_rare=sorted(range(N),key=lambda t:(ctx['combined'][t],t))[:256]
legacy_rare=sorted(ctx['legacy'],key=lambda t:(ctx['combined'][t],t))[:128]
targets=sorted(set(global_rare+legacy_rare+[min(ctx['legacy'])]))
rows=[(side,t) for side in (0,1) for t in targets]
dump('INITIAL_ROWS.json',dict(global_rare_targets=global_rare,legacy9754_rare_targets=legacy_rare,legacy_first_target=min(ctx['legacy']),unique_targets=targets,rows=[list(r) for r in rows],full_target_system=False))
with (HERE/'model_initial.cnf').open('w') as out:
    out.write(f'p cnf {variables} {base_clauses+len(rows)}\n')
    with (HERE/'base_cardinality.clauses').open() as inp:
        for chunk in iter(lambda:inp.read(1024*1024),''):out.write(chunk)
    for side,t in rows:out.write(' '.join(map(str,coverage_row(ctx,side,t)))+' 0\n')
elapsed=time.process_time()-start
gate=json.loads((BASE/'RESULT.json').read_text())
model=dict(status='K2_CNF_PREPARED_NOT_SOLVED',source_n=N,source_m=657452,free_count=K,selector_variables=2*K,all_variables=variables,base_clauses=base_clauses,initial_target_count=len(targets),initial_coverage_rows=len(rows),initial_total_clauses=base_clauses+len(rows),side_pin_limit=13,capacity1_ports=3670,capacity2_ports=15,complete_R3_cache=True,complete_R4_cache=True,full_target_system=False,initial_CNF='model_initial.cnf',solver_calls=0,greedy_control_calls=1,greedy_root_missing_counts=greedy['root_missing_counts'],greedy_single_R4_full=greedy['single_helper_full_R4'],prepare_CPU_seconds=elapsed,gate_and_prepare_CPU_seconds=gate['aggregate_CPU_seconds']+elapsed,future_solver_CPU_budget=60,future_whole_batch_CPU_budget=90,max_future_rounds=6,max_round_window_seconds=15,max_violated_rows_added_per_side_per_round=256,pending=['Root review before solver'])
dump('MODEL.json',model)
dump('PREPARE_TERMINAL.json',dict(model,running=False))
print(json.dumps(model),flush=True)

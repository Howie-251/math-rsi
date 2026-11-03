#!/usr/bin/env python3
"""Once-only bounded CEGIS. Writing this file does not authorize/run it."""
from pathlib import Path
from array import array
import argparse
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
CACHE=HERE.parent/'f5_induced_hyperplane3000/source_adjacency.u16.bin'
SOLVER=PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'
SOLVER_CPU_LIMIT=60.0
TOTAL_CPU_LIMIT=90.0
MAX_CALLS=6
MAX_CALL_SECONDS=15

def save(path,value):
    path.write_text(json.dumps(value,indent=2)+'\n')

class BudgetStop(Exception):
    pass

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--run',action='store_true',required=True)
    parser.parse_args()
    assert not (HERE/'CEGIS_HANDLE.json').exists(), 'This once-only batch has already started.'
    assert not (HERE/'CEGIS_TERMINAL.json').exists(), 'This batch has already terminated.'
    model=json.loads((HERE/'MODEL.json').read_text())
    assert model['status']=='PREPARED_NOT_SOLVED'
    assert (model['keep_variables'],model['n_at_least'])==(3750,1921)
    base=HERE/'model.cnf'
    assert base.is_file() and SOLVER.is_file()
    self_start=time.process_time();wall_start=time.monotonic()
    child_start=resource.getrusage(resource.RUSAGE_CHILDREN)
    child_start=child_start.ru_utime+child_start.ru_stime
    experiment=json.loads((HERE.parent/'f5_induced_hyperplane3000/RESULT.json').read_text())
    prior_CPU=model['CPU_seconds']+experiment['CPU_seconds']
    def child_cpu():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return r.ru_utime+r.ru_stime
    def total_cpu():
        return prior_CPU+time.process_time()-self_start+child_cpu()-child_start
    def checkpoint():
        if total_cpu()>=TOTAL_CPU_LIMIT-0.2:
            raise BudgetStop()
    def launch_limit(seconds):
        def apply():
            resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
        return apply
    rounds=[];solver_cpu=0.0;solver_calls=0
    total_variables=model['variables'];extra_clauses=0
    both_cache={};or_cache={};already_cut=set()
    cuts_path=HERE/'cegis_added_clauses.cnf'
    cuts_path.write_text('')
    keep_cache=array('H')
    with CACHE.open('rb') as f:keep_cache.fromfile(f,3750*20)
    adjacency=[list(keep_cache[v*20:v*20+20]) for v in range(3750)]
    adjacency_sets=[set(row) for row in adjacency]
    compiled=False
    current_round=None
    status='NOT_STARTED';hit=None
    initial={'status':'RUNNING','driver_pid':os.getpid(),
        'solver_CPU_budget':SOLVER_CPU_LIMIT,'total_CPU_budget':TOTAL_CPU_LIMIT,
        'max_calls':MAX_CALLS,'prior_charged_CPU_seconds':prior_CPU,'running':True}
    save(HERE/'CEGIS_HANDLE.json',initial)
    print(json.dumps(initial),flush=True)

    def run_child(command,stdout_path,seconds,kind,round_dir):
        nonlocal current_round,solver_calls
        checkpoint()
        before=child_cpu();wall=time.monotonic()
        with stdout_path.open('w') as out:
            process=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,
                                     preexec_fn=launch_limit(seconds))
            if kind=='SOLVER':solver_calls+=1
            handle={'status':kind,'driver_pid':os.getpid(),'pid':process.pid,
                'command':command,'round':current_round,'CPU_limit_seconds':seconds,
                'solver_CPU_used_before':solver_cpu,'total_CPU_before':total_cpu(),'running':True}
            save(HERE/'CEGIS_HANDLE.json',handle)
            save(round_dir/(kind.lower()+'.HANDLE.json'),handle)
            print(json.dumps(handle),flush=True)
            observation_timeout=False
            while True:
                try:
                    returncode=process.wait(timeout=5)
                    break
                except subprocess.TimeoutExpired:
                    # Observation windows do not end or restart live work.
                    # CaDiCaL's own timer and RLIMIT_CPU enforce the budget.
                    observation_timeout=True
        return {'returncode':returncode,'CPU_seconds':child_cpu()-before,
                'wall_seconds':time.monotonic()-wall,'observation_timeout':observation_timeout,
                'pid':process.pid,'command':command}

    def rewrite_working():
        checkpoint()
        with (HERE/'working.cnf').open('w') as out,base.open() as inp:
            header=inp.readline().split()
            assert header==['p','cnf',str(model['variables']),str(model['clauses'])]
            out.write(f'p cnf {total_variables} {model["clauses"]+extra_clauses}\n')
            for path,file in [(base,inp),(cuts_path,None)]:
                stream=file if file is not None else path.open()
                try:
                    while True:
                        block=stream.read(1024*1024)
                        if not block:break
                        out.write(block);checkpoint()
                finally:
                    if file is None:stream.close()

    def add_counterexample_cuts(pairs,kept,round_dir):
        nonlocal total_variables,extra_clauses
        records=[]
        with cuts_path.open('a') as out:
            def emit(literals):
                nonlocal extra_clauses
                out.write(' '.join(map(str,literals))+' 0\n');extra_clauses+=1
            def fresh():
                nonlocal total_variables
                total_variables+=1;return total_variables
            def both(a,b):
                if a==b:return a
                key=tuple(sorted((a,b)))
                if key not in both_cache:
                    z=fresh();both_cache[key]=z
                    emit([-z,a]);emit([-z,b]);emit([z,-a,-b])
                return both_cache[key]
            def either(terms):
                key=tuple(sorted(set(terms)))
                assert key, 'A source D3 pair must have a route.'
                if len(key)==1:return key[0]
                if key not in or_cache:
                    z=fresh();or_cache[key]=z
                    emit([-z,*key])
                    for term in key:emit([z,-term])
                return or_cache[key]
            for x,y in pairs:
                checkpoint()
                assert x<y and x in kept and y in kept
                assert (x,y) not in already_cut, 'SAT model violates an existing exact cut.'
                assert y not in adjacency_sets[x], 'An induced adjacent pair cannot be bad.'
                twos=sorted(adjacency_sets[x]&adjacency_sets[y])
                # Every a in N(x), b in N(y) with ab an edge is a source 3-walk.
                # Orientation duplicates have the same AND and can be merged.
                directed_threes=[(a,b) for a in adjacency[x] for b in adjacency[y]
                                  if b in adjacency_sets[a]]
                threes=sorted({tuple(sorted(pair)) for pair in directed_threes})
                assert not any(w in kept for w in twos)
                assert not any(a in kept and b in kept for a,b in threes)
                terms=[w+1 for w in twos]+[both(a+1,b+1) for a,b in threes]
                route=either(terms)
                emit([-(x+1),-(y+1),route])
                already_cut.add((x,y))
                records.append({'endpoints_old_ids':[x,y],
                    'all_source_two_path_middle_old_ids':twos,
                    'all_source_three_path_ordered_middle_pairs':directed_threes,
                    'distinct_three_path_AND_middle_pairs':threes,
                    'route_OR_variable_or_literal':route,
                    'endpoint_conditional_clause':[-(x+1),-(y+1),route]})
        save(round_dir/'EXACT_COUNTEREXAMPLE_CUTS.json',records)
        return len(records)

    try:
        for index in range(1,MAX_CALLS+1):
            current_round=index;checkpoint()
            seconds=math.floor(min(MAX_CALL_SECONDS,SOLVER_CPU_LIMIT-solver_cpu-0.05,
                                   TOTAL_CPU_LIMIT-total_cpu()-0.2))
            if seconds<1:
                status='CPU_BUDGET_STOP';break
            round_dir=HERE/f'cegis_round_{index:02d}'
            round_dir.mkdir()
            rewrite_working()
            # Account for CNF-writing cost before starting this call.
            seconds=math.floor(min(seconds,SOLVER_CPU_LIMIT-solver_cpu-0.05,
                                   TOTAL_CPU_LIMIT-total_cpu()-0.2))
            if seconds<1:
                status='CPU_BUDGET_BEFORE_SOLVER';break
            round_model={'round':index,'variables':total_variables,
                'clauses':model['clauses']+extra_clauses,'extra_clauses':extra_clauses,
                'existing_exact_bad_pair_cuts':len(already_cut),
                'solver_CPU_limit_this_call':seconds,'solver_CPU_remaining_before':SOLVER_CPU_LIMIT-solver_cpu,
                'global_keep_minimum':1921,'global_keep_exact':False,
                'base_CNF_rebuilt':False}
            save(round_dir/'MODEL.json',round_model)
            solution=round_dir/'candidate.sol'
            command=[str(SOLVER),'-q','-t',str(seconds),'-w',str(solution),str(HERE/'working.cnf')]
            solver=run_child(command,round_dir/'solver.stdout',seconds,'SOLVER',round_dir)
            solver_cpu+=solver['CPU_seconds']
            rec={'round':index,'solver':solver,'solver_CPU_cumulative':solver_cpu}
            rounds.append(rec)
            code=solver['returncode']
            if code==20:
                status='RAW_UNSAT_UNCERTIFIED';rec['status']=status
                save(round_dir/'RESULT.json',rec);break
            if code!=10:
                status='UNKNOWN';rec['status']=status
                save(round_dir/'RESULT.json',rec);break
            values={}
            for line in solution.read_text().splitlines():
                if line.startswith('v '):
                    for token in line[2:].split():
                        value=int(token)
                        if 1<=abs(value)<=3750:
                            assert abs(value) not in values or values[abs(value)]==(value>0)
                            values[abs(value)]=value>0
            assert len(values)==3750, 'The SAT result must assign every keep variable.'
            kept={v-1 for v,truth in values.items() if truth}
            assert len(kept)>=1921
            keep_file=round_dir/'KEEP_IDS.txt'
            keep_file.write_text(str(len(kept))+'\n'+'\n'.join(map(str,sorted(kept)))+'\n')
            rec['candidate_n']=len(kept)
            if not compiled:
                available=math.floor(TOTAL_CPU_LIMIT-total_cpu()-0.2)
                if available<1:raise BudgetStop()
                command=['g++','-O3','-std=c++17',str(HERE/'check_induced.cpp'),'-o',str(HERE/'check_induced')]
                compilation=run_child(command,round_dir/'compile.stdout',available,'COMPILE',round_dir)
                rec['compilation']=compilation
                if compilation['returncode']!=0:
                    status='COMPILE_FAILED_OR_BUDGET_STOP';rec['status']=status
                    save(round_dir/'RESULT.json',rec);break
                compiled=True
            available=math.floor(TOTAL_CPU_LIMIT-total_cpu()-0.2)
            if available<1:raise BudgetStop()
            command=[str(HERE/'check_induced'),str(CACHE),str(keep_file),str(max(0.1,available-0.1))]
            checking=run_child(command,round_dir/'check.stdout',available,'CANDIDATE_CHECK',round_dir)
            rec['checking']=checking
            if checking['returncode'] not in (0,1,3):
                status='CANDIDATE_CHECK_FAILED_OR_ENCODING_ERROR';rec['status']=status
                save(round_dir/'RESULT.json',rec);break
            validation=json.loads((round_dir/'check.stdout').read_text())
            rec['validation']=validation
            save(round_dir/'CANDIDATE_CHECK.json',validation)
            if validation['status']=='CHECK_BUDGET_STOP':
                status='CPU_BUDGET_DURING_CHECK';rec['status']=status
                save(round_dir/'RESULT.json',rec);break
            if validation['status']=='D3_HIT':
                accepted=validation['accepted_old_ids']
                label={v:i for i,v in enumerate(accepted)}
                edges=[(label[v],label[w]) for v in accepted for w in adjacency[v]
                       if v<w and w in label]
                accepted_degrees=[sum(w in label for w in adjacency[v]) for v in accepted]
                with (HERE/'HIT.edges').open('w') as out:
                    out.write(f'{len(accepted)} {len(edges)}\n')
                    for v,w in edges:out.write(f'{v} {w}\n')
                save(HERE/'HIT_KEEP_IDS.json',accepted)
                hit={'n':len(accepted),'m':len(edges),'max_degree':max(accepted_degrees),
                    'min_degree':min(accepted_degrees),
                    'diameter_at_most':3,'new_to_old_labels':accepted,'round':index,
                    'component_extraction':validation['component_extraction'],
                    'independent_final_pending':True}
                save(HERE/'HIT_PARAMETERS.json',hit)
                status='D3_HIT_AWAITS_ROOT_INDEPENDENT_CHECK';rec['status']=status
                save(round_dir/'RESULT.json',rec)
                print(json.dumps({'event':'HIT','n':hit['n'],'m':hit['m'],'round':index}),flush=True)
                break
            assert validation['status']=='R3_COUNTEREXAMPLES'
            pairs=validation['bad_pairs_old_ids']
            assert 1<=len(pairs)<=128
            if index==MAX_CALLS:
                status='MAX_CALLS_WITH_COUNTEREXAMPLE';rec['status']=status
                save(round_dir/'RESULT.json',rec);break
            rec['exact_bad_pair_cuts_added']=add_counterexample_cuts(pairs,kept,round_dir)
            rec['status']='SAT_CANDIDATE_REJECTED_EXACT_CUTS_ADDED'
            save(round_dir/'RESULT.json',rec)
        else:
            status='MAX_CALLS_REACHED'
    except BudgetStop:
        status='TOTAL_CPU_BUDGET_STOP'
    except Exception as exc:
        status='ERROR_STOP_NO_RETRY'
        error={'type':type(exc).__name__,'message':str(exc)}
        save(HERE/'CEGIS_ERROR.json',error)
    if rounds and 'status' not in rounds[-1]:
        rounds[-1]['status']=status
        save(HERE/f'cegis_round_{rounds[-1]["round"]:02d}'/'RESULT.json',rounds[-1])
    terminal={'status':status,'rounds':rounds,'actual_solver_calls':solver_calls,
        'solver_CPU_seconds':solver_cpu,'solver_CPU_budget':SOLVER_CPU_LIMIT,
        'total_CPU_seconds_including_prior_preparation':total_cpu(),
        'prior_charged_CPU_seconds':prior_CPU,'total_CPU_budget':TOTAL_CPU_LIMIT,
        'wall_seconds':time.monotonic()-wall_start,
        'last_round':current_round,'exact_bad_pair_cuts':len(already_cut),
        'extra_clauses':extra_clauses,'current_variables':total_variables,
        'base_CNF_rebuilt':False,'source_edge_text_reads':0,
        'hit':None if hit is None else {k:v for k,v in hit.items() if k!='new_to_old_labels'},
        'running':False,'automatic_resume_allowed':False,
        'UNSAT_certification':'none; raw solver outcome only',
        'pending':(['root_unique_independent_final'] if hit else [])}
    save(HERE/'CEGIS_TERMINAL.json',terminal)
    save(HERE/'CEGIS_HANDLE.json',terminal)
    print(json.dumps(terminal),flush=True)

if __name__=='__main__':
    main()

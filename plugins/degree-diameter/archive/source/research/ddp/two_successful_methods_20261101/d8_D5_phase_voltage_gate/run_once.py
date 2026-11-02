#!/usr/bin/env python3
"""One <=20CPU gate, with an algebraic collision test before any solver."""
import time
START=time.process_time()
import os
for var in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','HIGHS_THREADS']:
    os.environ[var]='1'
import csv, itertools, json, math, resource, signal, sys, warnings
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
ROOT=next(p for p in STAGE.parents if (p/'research').is_dir() and (p/'formal').is_dir())
OLD=ROOT/'research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate'
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
POS_PHASE=[1,12,11,16]
PHASE=[1,12,11,16,19,8,9,4]
INV=[4,5,6,7,0,1,2,3]
LEDGER=[]

def now():return datetime.now(timezone.utc).isoformat()
def dump(name,data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def mark(stage,**extra):
    row=dict(stage=stage,process_CPU_seconds=time.process_time()-START,**extra)
    LEDGER.append(row)
    dump('BUDGET_LEDGER.json',dict(total_CPU_budget_seconds=20,solver_CPU_budget_seconds=12,
        single_worker=True,stages=LEDGER))
    dump('HANDLE.json',dict(pid=os.getpid(),status=stage,updated_UTC=now(),
        total_CPU_budget_seconds=20,solver_CPU_budget_seconds=12,
        actual_process_started=True,one_worker=True,CPU_hard_limit_seconds=20))

def form(start,word):
    phase=start;coeff=[0]*80;terms=[];trace=[phase]
    for dart in word:
        assert 0<=dart<8
        if dart<4:
            source=phase;positive=dart;sign=1
            phase=(phase+POS_PHASE[positive])%20
        else:
            positive=dart-4;sign=-1
            phase=(phase-POS_PHASE[positive])%20
            source=phase
        slot=4*source+positive
        coeff[slot]=(coeff[slot]+sign)%5
        terms.append(dict(source_phase=source,positive_dart=positive,sign=sign,slot=slot))
        trace.append(phase)
    return dict(word=word,start_phase=start,end_phase=phase,
                signed_terms=terms,phase_trace=trace,coefficients_mod5=coeff)

def direct_value(theta,start,word):
    phase=start;value=0
    for dart in word:
        if dart<4:
            value+=theta[4*phase+dart]
            phase=(phase+POS_PHASE[dart])%20
        else:
            p=dart-4;phase=(phase-POS_PHASE[p])%20
            value-=theta[4*phase+p]
    return value%5

def finish(result,note,solver_calls=0,solver_CPU=0):
    result.update(total_CPU_budget_seconds=20,solver_CPU_budget_seconds=12,
        solver_calls=solver_calls,solver_CPU_seconds=solver_CPU,
        actual_PID=os.getpid(),single_worker=True,full_graph_generated=False,
        source_DP_or_BFS_reruns=0,old125_graph_reruns=0,
        field_rank_checks=0,Lean_compilations=0,network_or_paid_review_calls=0,
        root_counts_or_Wiki_or_old_files_modified=False)
    (HERE/'NOTE.md').write_text(note+'\n')
    result['CPU_seconds']=time.process_time()-START
    dump('RESULT.json',result)
    mark('TERMINAL',outcome=result['status'])
    dump('TERMINAL.json',dict(status=result['status'],running=False,
        all_processes_terminal=True,single_worker=True,CPU_seconds=time.process_time()-START,
        CPU_budget_seconds=20,solver_calls=solver_calls,solver_CPU_seconds=solver_CPU,
        no_automatic_continuation=True))
    print(json.dumps(dict(status=result['status'],pid=os.getpid(),
        CPU_seconds=time.process_time()-START,solver_calls=solver_calls,
        result_path=str(HERE/'RESULT.json')),ensure_ascii=False),flush=True)

def main():
    mark('BUILDING_SIGNED_PHASE_FORMS')
    old=json.loads((OLD/'FIVE_ROUTE_RESULT.json').read_text())
    assert old['source_target']==[11,1]
    assert [list(x) for x in old['darts']]==[[1,0],[12,33],[11,1],[16,19],[19,0],[8,22],[9,38],[4,26]]
    assert old['inverse_darts']==INV and len(old['five_words'])==5
    g3=old['five_words']
    families=[('identity',[[],[1]*5,[5]*5,[3]*5,[7]*5],[0,0]),
              ('g3',g3,[11,1]),
              ('g3_inverse',[[INV[p]for p in reversed(w)]for w in g3],[9,38])]
    tuples=[]
    for phase in range(20):
        for name,words,relative in families:
            rows=[form(phase,w)for w in words]
            assert all(r['end_phase']==(phase+relative[0])%20 for r in rows)
            tuples.append(dict(start_phase=phase,tight_fiber=name,
                relative_source_endpoint=relative,routes=rows))
    dump('SIGNED_PHASE_ROUTE_FORMS.json',dict(source='Fixed Loz1100 RIGHT law',
        inherited_g3_words=str((OLD/'FIVE_ROUTE_RESULT.json').relative_to(ROOT)),
        identity_five_word_completeness='Inherited prior exact route-count and fifth-cycle evidence; not recomputed.',
        positive_darts=[[1,0],[12,33],[11,1],[16,19]],
        slot_convention='slot=4*source_phase+positive_dart; reverse subtracts the positive edge at its original source phase',
        tuple_count=60,route_count=300,tuples=tuples))
    collisions=[]
    for row in tuples:
        for i,j in itertools.combinations(range(5),2):
            if row['routes'][i]['coefficients_mod5']==row['routes'][j]['coefficients_mod5']:
                collisions.append(dict(start_phase=row['start_phase'],tight_fiber=row['tight_fiber'],
                    relative_source_endpoint=row['relative_source_endpoint'],route_indices=[i,j],
                    first_route=row['routes'][i],second_route=row['routes'][j]))
    mark('SIGNED_FORM_COLLISION_TEST_COMPLETE',tuples=60,routes=300,
         coefficient_collisions=len(collisions))
    if collisions:
        witness=collisions[0]
        dump('UNIVERSAL_COLLISION_WITNESS.json',witness)
        note='''# Phase-only additiveF5 gate: universal route collision

The prediction was tested by constructing the new signed phase-edge forms, not by rerunning source DP, BFS or any of the old125 failed graphs. Within a tight source fiber, two different saved source words have exactly the same80 coefficient vector modulo5. Their lifted deck endpoints therefore agree for every possible phase-dependent theta, before any gauge choice.

The saved source certificate says that this tight fiber has exactly five reduced source words of length at most5. Immediate backtracks cancel both their source movement and their deck voltage. Thus every length-at-most5 lifted walk to this source fiber has one of those five deck values; an identical pair leaves at most four distinct values, while a five-sheet cover requires all five. At least one lifted target is necessarily unreachable within5 from the displayed root, so no assignment in this precise phase-only additive model can have D<=5. The unknown missing deck label may depend on theta; a uniform fixed missing label is not required for this impossibility proof.

SIGNED_PHASE_ROUTE_FORMS.json stores all300 actual signed forms and phase traces. UNIVERSAL_COLLISION_WITNESS.json gives the first colliding pair, its words, all signed original-positive-edge slots and its common modulo5 vector. RESULT.json records the complete collision count. No solver was called or needed.

This strictly closes only the fixedLoz1100 source, phase-dependent additiveF5 deck-voltage rule proposed in PRED. It does not classify arbitrary source-edge voltage functions that also depend on the normal coordinate, nontranslation deck permutations, other five-covers, or general(8,5) graphs. The earlier125 metacyclic failures and their scope remain unchanged. No new graph, parameter, Lean instance or global record is counted, and this run stops without another timer or new pattern.
'''
        finish(dict(status='STRICT_NO_PHASE_ONLY_ADDITIVE_F5_D5_UNIVERSAL_COLLISION',
            prediction='REFUTED',tuple_count=60,route_count=300,
            equal_coefficient_pairs=len(collisions),
            collision_tuple_count=len({(x['start_phase'],x['tight_fiber'])for x in collisions}),
            first_collision=witness,scope='Fixed Loz1100 source, F5 deck translations depending only on20phase and4positive darts, true reverse edges; every80-variable assignment excluded.',
            gauge_needed=False,mathematical_obstruction=True),note)
        return

    # One new finite feasibility model only, with the legitimate 19-edge gauge.
    mark('BUILDING_SINGLE_MODULAR_FEASIBILITY_MODEL')
    import numpy as np
    from scipy.optimize import milp, Bounds, LinearConstraint
    from scipy.sparse import coo_matrix
    fixed={4*j for j in range(19)}
    free=[j for j in range(80)if j not in fixed];indices={j:i for i,j in enumerate(free)}
    diffs=[]
    for row in tuples:
        for i,j in itertools.combinations(range(5),2):
            raw=[(a-b)%5 for a,b in zip(row['routes'][i]['coefficients_mod5'],row['routes'][j]['coefficients_mod5'])]
            canonical=[a if a<=2 else a-5 for a in raw]
            diffs.append([canonical[j]for j in free])
    assert len(free)==61 and len(diffs)==600
    if any(not any(x)for x in diffs):
        raise AssertionError('Unexpected gauge-only identical pair; report instead of altering the family.')
    ntheta=len(free);nvars=ntheta+2*len(diffs)
    ri=[];ci=[];data=[];lower=[0]*ntheta;upper=[4]*ntheta
    for k,row in enumerate(diffs):
        for j,value in enumerate(row):
            if value:ri.append(k);ci.append(j);data.append(value)
        # E(theta)-5*q-d=0 with integer d in1..4 is exactly E != 0 mod5.
        ri.extend([k,k]);ci.extend([ntheta+2*k,ntheta+2*k+1]);data.extend([-5,-1])
        min_e=4*sum(min(0,x)for x in row);max_e=4*sum(max(0,x)for x in row)
        lower.extend([math.floor((min_e-4)/5),1]);upper.extend([math.ceil((max_e-1)/5),4])
    A=coo_matrix((data,(ri,ci)),shape=(600,nvars)).tocsc()
    cpu_left=20-(time.process_time()-START)
    wall_cap=min(11.0,max(0.1,cpu_left-2.0))
    if cpu_left<=2:
        finish(dict(status='UNKNOWN_PREPARATION_CPU_LIMIT',prediction='UNKNOWN',tuple_count=60,route_count=300),
               '# Gate stopped before solver\nPreparation exhausted the allowed remaining budget. No continuation.')
        return
    mark('RUNNING_SINGLE_SOLVER',model_variables=nvars,model_rows=600,
         solver_wall_limit_seconds=wall_cap,remaining_total_CPU_seconds=cpu_left)
    solver_started=time.process_time()
    with warnings.catch_warnings(record=True)as caught:
        warnings.simplefilter('always')
        solved=milp(c=np.zeros(nvars),integrality=np.ones(nvars),
            bounds=Bounds(np.asarray(lower),np.asarray(upper)),
            constraints=LinearConstraint(A,np.zeros(600),np.zeros(600)),
            options=dict(time_limit=wall_cap,threads=1,mip_rel_gap=0.0))
    solver_cpu=time.process_time()-solver_started
    assert solver_cpu<=12,'Measured single solver exceeded its12CPU scope; do not retry.'
    raw=dict(status=int(solved.status),message=solved.message,success=bool(solved.success),
        solver_CPU_seconds=solver_cpu,solver_wall_limit_seconds=wall_cap,
        variables=nvars,rows=600,nonzeros=len(data),gauge_slots=sorted(fixed),
        warnings=[str(w.message)for w in caught])
    for name in ['mip_node_count','mip_dual_bound','mip_gap','fun']:
        value=getattr(solved,name,None)
        if value is not None:raw[name]=float(value)
    dump('SOLVER_RETURN.json',raw)
    if solved.x is not None:
        theta=[0]*80
        for slot,i in indices.items():theta[slot]=int(round(solved.x[i]))
        assert all(0<=t<=4 for t in theta)and all(theta[j]==0 for j in fixed)
        tested=[]
        for row in tuples:
            values=[direct_value(theta,row['start_phase'],r['word'])for r in row['routes']]
            dots=[sum(a*b for a,b in zip(theta,r['coefficients_mod5']))%5 for r in row['routes']]
            assert values==dots and sorted(values)==list(range(5))
            tested.append(dict(start_phase=row['start_phase'],tight_fiber=row['tight_fiber'],deck_values=values))
        dump('ACTUAL_THETA_AND_SIXTY_TUPLES.json',dict(theta_by_phase=[theta[4*j:4*j+4]for j in range(20)],
            type0_phase19_cycle_voltage=theta[76],tree_gauge_type0_phases=list(range(19)),
            tuples=tested,reverse_edge_rule='negative of theta at original positive-edge source phase',
            scope='Necessary tight-fiber test only; no complete5500 graph or D5 claim.'))
        finish(dict(status='SAT_SIXTY_TIGHT_FIBER_COMPATIBILITY_ONLY',prediction='SUPPORTED_NECESSARY_TEST_ONLY',
            tuple_count=60,route_count=300,model=raw),
            '# New phase rule passes only the tight-fiber gate\nThe actual theta and60 direct signed-word tuple evaluations are saved. Every tuple equals F5. Other source fibers remain completely unverified; no graph was generated or accepted. One solver call, no continuation.',1,solver_cpu)
    else:
        status='NUMERICAL_MIP_INFEASIBLE_NECESSARY_PHASE_MODEL'if solved.status==2 else'UNKNOWN_SINGLE_BOUNDED_SOLVER'
        finish(dict(status=status,prediction='REFUTED_AT_SOLVER_EVIDENCE_SCALE'if solved.status==2 else'UNKNOWN',
            tuple_count=60,route_count=300,model=raw,independent_UNSAT_proof=False),
            '# Single finite model terminal\nSOLVER_RETURN.json preserves the actual return. No independent infeasibility proof is claimed. The scope is only the fixed phase-dependent additiveF5 model, not all ordinary covers or generalN(8,5). No second timer or graph follows.',1,solver_cpu)

if __name__=='__main__':main()

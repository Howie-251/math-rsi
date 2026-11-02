"""Finite counter calibration only; no graph model or external solver."""
from itertools import product
import time
from counter_encoding import atmost_three


def unit_conflict(clauses,assignment):
    assignment=dict(assignment)
    while True:
        changed=False
        for clause in clauses:
            pending=[]
            for literal in clause:
                value=assignment.get(abs(literal))
                if value is None:
                    pending.append(literal)
                elif value==(literal>0):
                    break
            else:
                if not pending:
                    return True
                if len(pending)==1:
                    literal=pending[0]
                    assignment[abs(literal)]=literal>0
                    changed=True
        if not changed:
            return False


def check_pattern(bits):
    n=len(bits)
    inputs=list(range(1,n+1))
    clauses,meta=atmost_three(inputs,n+1)
    assigned={i+1:bool(value) for i,value in enumerate(bits)}
    expected=sum(bits)<=3
    conflict=unit_conflict(clauses,assigned)
    assert conflict==(not expected)
    if expected:
        prefix=0
        for i,value in enumerate(bits,1):
            prefix+=value
            for j in (1,2,3):
                assigned[meta['first_aux']+3*(i-1)+j-1]=prefix>=j
        assert all(any(assigned[abs(lit)]==(lit>0) for lit in clause) for clause in clauses)
    return expected


def calibrate():
    start=time.process_time()
    by_n=[]
    total=valid=invalid=0
    for n in range(1,9):
        count=0
        for bits in product((0,1),repeat=n):
            ok=check_pattern(bits)
            valid+=ok;invalid+=not ok;total+=1;count+=1
        by_n.append({'n':n,'patterns':count,'all_pass':True})
    controls=[(),(0,),(0,17),(0,17,53),(0,17,35,53),(50,51,52,53),tuple(range(54))]
    large=[]
    for positions in controls:
        bits=[int(i in positions) for i in range(54)]
        ok=check_pattern(bits)
        large.append({'n':54,'true_positions0based':list(positions),
                      'atmost3':ok,'check_pass':True})
    return {'status':'PASS_SMALL_EXHAUSTIVE_AND_54_INPUT_CONTROLS',
            'small_counter_n_range':[1,8],'exhaustive_input_patterns':total,
            'satisfiable_input_patterns':valid,'overflow_input_patterns':invalid,
            'small_checks':by_n,'actual_length_controls':large,
            'general_proof_required':'Forward clauses force every attained prefix threshold; fourth true input conflicts with overflow. Canonical prefix-count auxiliaries extend every input of weight<=3.',
            'external_solver_calls':0,'graph_model_calls':0,'graph_BFS':0,
            'CPU_seconds':time.process_time()-start}

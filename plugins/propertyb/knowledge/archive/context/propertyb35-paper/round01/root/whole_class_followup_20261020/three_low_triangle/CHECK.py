"""Exhaust only the six logical constraints, not H; verify exact coarse arithmetic."""
from itertools import product
from math import comb
from fractions import Fraction
from pathlib import Path
import json,time

start=time.process_time()
edges=((0,1),(1,2),(2,0))
assignments=tuple(product((0,1),repeat=3))
def sat(state):
    for x in assignments:
        if any(state[i] and x[i]!=state[i]-1 for i in range(3)):
            continue
        if any(state[3+j] and x[u]==x[v]==state[3+j]-1 for j,(u,v) in enumerate(edges)):
            continue
        return True
    return False
minimal=[]
unsat=0
for state in product(range(3),repeat=6):
    if sat(state):continue
    unsat+=1
    reductions=[]
    for i,v in enumerate(state):
        if v:
            t=list(state);t[i]=0;reductions.append(tuple(t))
    if all(sat(t) for t in reductions):
        pins=sum(bool(x) for x in state[:3])
        clauses=sum(bool(x) for x in state[3:])
        assert (pins,clauses) in ((2,1),(2,2),(1,3))
        minimal.append({'state':state,'pins':pins,'edge_clauses':clauses})
hist={str((p,e)):sum(x['pins']==p and x['edge_clauses']==e for x in minimal)
      for p,e in ((2,1),(2,2),(1,3))}
assert len(minimal)==18 and set(hist.values())=={6}
for state in product(range(3),repeat=6):
    if not sat(state):
        assert any(all(v==0 or v==state[i] for i,v in enumerate(core['state'])) for core in minimal)

N=comb(22,11)
C=12*comb(14,7)-24*comb(10,3)+6*comb(6,3)
allhigh=2*comb(17,6)
base=3*C+20*allhigh
assert (N,C,allhigh,base)==(705432,38424,24752,610312)

# Type I witness f(k), valid for every actual same-color private-block pair.
f=[comb(11+k,8) for k in range(5)]
assert f==[165,495,1287,3003,6435]
assert all(f[k]<=165+946*k+(2486 if k==4 else 0) for k in range(5))
typeI=2*(48*165+946*39+2486*3)

# Actual nonincident triple is partitioned by four private blocks: sum s_i=3.
alloc=[x for x in product(range(4),repeat=4) if sum(x)==3]
assert len(alloc)==20
typeII_one=max(sum(comb(8+s+t,4+t) for s in ss for t in tt) for ss in alloc for tt in alloc)
typeIII_one=max(sum(comb(9+s,5) for s in ss) for ss in alloc)
assert (typeII_one,typeIII_one)==(6042,1170)
typeII=6*typeII_one;typeIII=6*typeIII_one
extra=typeI+typeII+typeIII
result={
    'status':'PASS_FOR_CLASSIFICATION_AND_COARSE_COUNTS_NOT_A_COLORING_PROOF',
    'logical_states':729,'low_assignments_per_state':8,'unsatisfiable_states':unsat,
    'minimal_cores':minimal,'core_type_histogram':hist,
    'N':N,'private_conflict_per_center':C,'all_high_bad_per_edge':allhigh,
    'base_union_bound_numerator':base,'base_slack':N-base,
    'base_probability':str(Fraction(base,N)),
    'type_I_bound':typeI,'type_II_bound':typeII,'type_III_bound':typeIII,
    'extra_union_bound_numerator':extra,'total_coarse_numerator':base+extra,
    'excess_over_N':base+extra-N,'integer_improvement_needed_for_strictness':base+extra-N+1,
    'target_additional_failure_bound':N-base-1,
    'cpu_seconds':time.process_time()-start,
    'H_search':False,
}
(Path(__file__).resolve().parent/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='minimal_cores'}))

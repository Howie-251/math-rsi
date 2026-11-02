#!/usr/bin/env python3
"""One exact joint six-helper pin model on the prepared complete G0."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import array
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (119, 120))
base = Path(__file__).resolve().parent
started = resource.getrusage(resource.RUSAGE_SELF)

def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime-started.ru_utime-started.ru_stime

def save(name, value):
    p = base/name
    temp = p.with_suffix(p.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2)+'\n')
    temp.replace(p)

def checkpoint(stage, **extra):
    save('SOLVER_CHECKPOINT.json', {'stage':stage,'CPU_seconds':cpu(),
        'pid':os.getpid(),'running':True,**extra})

checkpoint('IMPORTS')
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csr_matrix, vstack

input_path = base/'G0_INPUT.npz'
inp = np.load(input_path)
indptr = inp['indptr']
indices = inp['indices']
pool = inp['pool']
spare = inp['spare']
n = int(inp['n'])
p = len(pool)
helpers = 6
assert n == 10070 and p == 1750
assert len(indptr)==n+1 and len(indices)==308780
assert np.all(spare == 31-np.diff(indptr)[pool])
assert np.all(spare>0) and np.max(np.diff(indptr))==31
pool_index = [-1]*n
for j,u in enumerate(pool):
    pool_index[int(u)] = j
adj = [indices[indptr[v]:indptr[v+1]].tolist() for v in range(n)]

# Coverage row 6*v+h uses the actual closed B2 of G0 for own pins and
# actual closed B1 for the other five helpers. The K6 makes these exactly
# the relevant short-route types; every old vertex, including all copies,
# appears as a target.
cols = array.array('i')
ptr = array.array('i', [0])
lower = []
upper = []
for v in range(n):
    one = {pool_index[w] for w in adj[v] if pool_index[w]>=0}
    if pool_index[v]>=0:
        one.add(pool_index[v])
    two = set(one)
    for w in adj[v]:
        two.update(pool_index[z] for z in adj[w] if pool_index[z]>=0)
    one = sorted(one)
    two = sorted(two)
    for h in range(helpers):
        for g in range(helpers):
            offset = g*p
            cols.extend(offset+j for j in (two if g==h else one))
        ptr.append(len(cols))
        lower.append(1.)
        upper.append(np.inf)
    if v%2000==0:
        checkpoint('MATRIX_COVERAGE',targets_prepared=v+1,
            rows=len(lower),nonzeros=len(cols))

coverage_rows = len(lower)
for j in range(p):
    cols.extend(h*p+j for h in range(helpers))
    ptr.append(len(cols))
    lower.append(-np.inf)
    upper.append(float(spare[j]))
for h in range(helpers):
    cols.extend(range(h*p,(h+1)*p))
    ptr.append(len(cols))
    lower.append(-np.inf)
    upper.append(26.)

col_array = np.frombuffer(cols,dtype=np.int32)
ptr_array = np.frombuffer(ptr,dtype=np.int32)
matrix = csr_matrix((np.ones(len(cols)),col_array,ptr_array),
    shape=(len(lower),helpers*p))

# Helper labels are interchangeable in K6. Sorting the weighted pin sums
# only selects a representative of a feasible helper permutation; it does
# not force any particular pin to be used.
sym_indices = array.array('i')
sym_data = array.array('d')
sym_ptr = [0]
for h in range(helpers-1):
    for j in range(p):
        sym_indices.append(h*p+j)
        sym_data.append(float(j+1))
    for j in range(p):
        sym_indices.append((h+1)*p+j)
        sym_data.append(-float(j+1))
    sym_ptr.append(len(sym_indices))
sym = csr_matrix((np.frombuffer(sym_data,dtype=np.float64),
    np.frombuffer(sym_indices,dtype=np.int32),np.array(sym_ptr,dtype=np.int32)),
    shape=(helpers-1,helpers*p))
matrix = vstack([matrix,sym],format='csc')
lower.extend([-np.inf]*(helpers-1))
upper.extend([0.]*(helpers-1))
model = {'base_n':n,'base_m':len(indices)//2,'helpers':helpers,
    'helper_graph':'K6','pool':p,'variables':helpers*p,
    'coverage_rows':coverage_rows,'rows':matrix.shape[0],
    'nonzeros':matrix.nnz,'all_old_targets_included':True,
    'coverage_row_label':'6*v+h','old_pin_capacities_actual':True,
    'helper_pin_limit':26,'closed_ball_graph':'actual prepared G0 with copy cycles and sigma peers',
    'helper_weighted_sum_order_is_only_permutation_symmetry':True,
    'objective':'zero, feasibility only','solver_time_limit_seconds':90,
    'total_CPU_budget_seconds':120,'workers':1,
    'matrix_preparation_and_import_CPU_seconds':cpu()}
save('MODEL.json',model)
checkpoint('MILP_RUNNING',**model)
result = milp(c=np.zeros(helpers*p),integrality=np.ones(helpers*p),
    bounds=Bounds(np.zeros(helpers*p),np.ones(helpers*p)),
    constraints=LinearConstraint(matrix,np.array(lower),np.array(upper)),
    options={'time_limit':90.,'threads':1,'mip_rel_gap':0.,'disp':True})

out = {'status_code':int(result.status),'message':str(result.message),
    'success':bool(result.success),'CPU_seconds':cpu(),
    'mip_node_count':getattr(result,'mip_node_count',None),
    'mip_dual_bound':getattr(result,'mip_dual_bound',None),
    'mip_gap':getattr(result,'mip_gap',None),
    'fixed_model_only':True,'whole_parameter_or_mechanism_excluded':False,
    'strict_infeasibility_proof_claimed':False,'feasible_integer_pins_saved':False,
    'next_candidate_or_timer_restart':False}
if result.x is not None:
    rounded = np.rint(result.x)
    integral = bool(np.max(np.abs(result.x-rounded))<=1e-5)
    residual = matrix@rounded
    feasible = integral and bool(np.all(residual>=np.array(lower)-1e-7)
        and np.all(residual<=np.array(upper)+1e-7))
    out.update({'incumbent_integral':integral,'rounded_model_feasible':feasible})
    if feasible:
        pins = [[int(pool[j]) for j in range(p) if rounded[h*p+j]>.5]
            for h in range(helpers)]
        save('PINS.json',{'status':'EXACT_BINARY_PIN_MODEL_FEASIBLE_PENDING_GRAPH_ACCEPTANCE',
            'old_n':n,'helper_labels':list(range(n,n+helpers)),
            'helper_edges':[[n+h,n+g] for h in range(helpers) for g in range(h+1,helpers)],
            'pins':pins,'pin_counts':list(map(len,pins)),
            'total_pins':sum(map(len,pins)),
            'target':[31,3,10076],'candidate_m':154390+15+sum(map(len,pins)),
            'old_old_inherited_source_interior_D3':True,
            'independent_acceptance':'PENDING','portfolio_increment':0})
        out['feasible_integer_pins_saved'] = True
if out['feasible_integer_pins_saved']:
    out['status']='FEASIBLE_PINS_PENDING_COMPLETE_GRAPH_AND_FRESH_ACCEPTANCE'
elif result.status==2:
    out['status']='FIXED_MODEL_NUMERICAL_INFEASIBLE_NOT_A_GENERAL_OR_FORMAL_EXCLUSION'
else:
    out['status']='UNKNOWN_NO_FEASIBLE_INTEGER_PINS_WITHIN_ONE_BUDGET'
save('SCIPY_MILP_RESULT.json',out)
save('SOLVER_CHECKPOINT.json',{'stage':'TERMINAL','running':False,**out})
print(json.dumps(out))

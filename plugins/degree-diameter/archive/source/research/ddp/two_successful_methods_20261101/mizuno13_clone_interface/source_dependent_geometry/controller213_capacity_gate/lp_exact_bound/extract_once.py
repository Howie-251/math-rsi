from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import os,time,json,resource,warnings
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
D=Path(__file__).resolve().parent;P=D.parent
START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(9,10))
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def fs(v):return str(v)
assert not (D/'LP_HANDLE.json').exists(),'One-call LP batch already started.'
handle={'PID':os.getpid(),'status':'PREPARING','started_UTC':datetime.now(timezone.utc).isoformat(),'LP_calls':0,'MIP_calls':0,'threads':1,'CPU_soft_limit':9,'CPU_hard_limit':10,'running':True};save('LP_HANDLE.json',handle)
model=json.loads((P/'MODEL.json').read_text());log=(P/'solver.stdout.log').read_text()
assert 'Status            Infeasible' in log and 'LP iterations     621' in log
save('ROOT_LOG_READOUT.json',{'raw_integer_status':'Infeasible','processed_nodes':1,'LP_iterations':621,'generated_cuts':0,'explicit_root_LP_status_reported':False,'interpretation':'The log alone does not certify the continuous LP bound.','input_log':'../solver.stdout.log'})
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
A=[[0]*364 for _ in range(364)]
for b,row in enumerate(model['row_sparse_coefficients']):
    for a,z in row:A[b][a]=z
cost=model['source_cost'];rows=A+[cost];rhs=[3]*364+[1092]
assert len(rows)==365 and all(sum(row)==5 for row in A)
save('LP_INPUT.json',{'input_model':'../MODEL.json','objective':'maximize sum x','rows':rows,'rhs':rhs,'bounds':[0,1],'variable_count':364,'constraint_count':365,'cardinality_lower_row_omitted':True})
handle.update(status='RUNNING',LP_calls=1,pre_solver_CPU_seconds=time.process_time()-START);save('LP_HANDLE.json',handle);st=time.process_time()
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter('always')
    ans=linprog(c=-np.ones(364),A_ub=csc_matrix(np.asarray(rows,dtype=float)),b_ub=np.asarray(rhs,dtype=float),bounds=(0,1),method='highs',options={'time_limit':6.,'threads':1,'disp':True})
solveCPU=time.process_time()-st
out={'status':'STOP_NO_SEPARATING_LP_BOUND','raw_status':int(ans.status),'raw_message':str(ans.message),'LP_calls':1,'MIP_calls':0,'PID':os.getpid(),'pre_solver_CPU_seconds':handle['pre_solver_CPU_seconds'],'solver_CPU_seconds':solveCPU,'numerical_max_sumx':None if ans.fun is None else float(-ans.fun),'warnings':[str(w.message) for w in ws],'accepted_exact_certificate':False,'running':False,'pending':[],'automatic_continuation':False,'BFS_runs':0,'graphs':0,'scope':'Continuous relaxation of necessary constraints for one full27 affine W-transverse block per selected source among364 original fibers.'}
if ans.status==0 and -ans.fun<213:
    ym=[max(F(0),F(-float(v)).limit_denominator(1000000)) for v in ans.ineqlin.marginals]
    zm=[max(F(0),F(-float(v)).limit_denominator(1000000)) for v in ans.upper.marginals]
    assert len(ym)==365 and len(zm)==364
    before=[sum(F(rows[b][a])*ym[b] for b in range(365))+zm[a] for a in range(364)]
    repair=[max(F(0),1-v) for v in before];z=[q+d for q,d in zip(zm,repair)]
    coefficients=[sum(F(rows[b][a])*ym[b] for b in range(365))+z[a] for a in range(364)]
    upper=sum(F(b)*y for b,y in zip(rhs,ym))+sum(z)
    nonnegative=all(y>=0 for y in ym+z);exactcols=all(v>=1 for v in coefficients);accepted=nonnegative and exactcols and upper<213
    cert={'status':'ACCEPTED_EXACT_DUAL_BOUND' if accepted else 'RATIONAL_DUAL_DID_NOT_SEPARATE','rationalization':'Fraction(value).limit_denominator(1000000), clipped only negative multipliers to0; per-column deficits added exactly to upper-bound multipliers','inequality_multipliers':[fs(x) for x in ym],'upper_bound_multipliers':[fs(x) for x in z],'upper_bound_multiplier_repairs':[fs(x) for x in repair],'exact_column_coefficients':[fs(x) for x in coefficients],'all_multipliers_nonnegative':nonnegative,'all364_column_coefficients_at_least1':exactcols,'minimum_column_coefficient':fs(min(coefficients)),'total_repair':fs(sum(repair)),'exact_dual_objective':fs(upper),'strict_margin_to213':fs(F(213)-upper),'integer_count_upper':upper.numerator//upper.denominator,'numerical_max_sumx':float(-ans.fun),'LP_input':'LP_INPUT.json'}
    save('EXACT_DUAL_CERTIFICATE.json',cert)
    out.update(status='EXACT_LINEAR_BOUND_EXCLUDES_213_BLOCKS' if accepted else 'STOP_RATIONAL_DUAL_UNSTABLE',accepted_exact_certificate=accepted,exact_upper_bound=fs(upper),strict_margin_to213=fs(F(213)-upper),integer_count_upper=upper.numerator//upper.denominator,certificate='EXACT_DUAL_CERTIFICATE.json')
    nz=[(i,fs(v)) for i,v in enumerate(ym) if v];out['nonzero_inequality_multiplier_histogram']=dict(Counter(fs(v) for v in ym if v));out['nonzero_inequality_multipliers']=len(nz);out['nonzero_upper_bound_multipliers']=sum(bool(v) for v in z)
out['process_CPU_seconds']=time.process_time()-START
for name in ['RESULT.json','TERMINAL.json','LP_HANDLE.json']:save(name,out)
print(json.dumps(out),flush=True)

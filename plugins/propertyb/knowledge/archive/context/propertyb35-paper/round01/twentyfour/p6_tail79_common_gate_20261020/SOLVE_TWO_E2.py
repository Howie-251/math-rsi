"""Only two old59 E2 raw-sum boundary rows; no new domain."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
import importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent
helper=HERE.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/joint_cover_lp/LP_DIAGNOSIS.py'
spec=importlib.util.spec_from_file_location('old_joint_helper',helper);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
data=json.loads((HERE/'CHECK_MIXED_EIGHT.json').read_text());out=[];start=time.process_time()
assert len(data['nongated_rows'])==2
for row in data['nongated_rows']:
 R,V,D,B,mat=old.build(row);B[0]=2;B[2]=21
 c=np.zeros(len(V)+1);c[-1]=-1
 res=linprog(c,A_ub=mat,b_ub=np.asarray([0.]*len(R)+B),bounds=[(0,1)]*len(V)+[(0,None)],method='highs',options={'time_limit':2.,'threads':1})
 r={'name':row['name'],'sets':row['sets'],'C3':row['C3'],'C4':row['C4'],'candidate_red_sets':R,'budgets':B,'negative_variables':len(V),'solver_status':int(res.status)}
 if res.success:
  r['maximum_common_coverage']=float(res.x[-1])
  if res.x[-1]<1-1e-8:r['dual_certificate']=old.dual_certificate(res,R,V,D,B)
  else:r['primal_witness']=old.primal_witness(res,R,V,D,B)
 out.append(r)
result={'scope':__doc__,'model':'T<=2,xneg<=4,totalnegative<=21,pointnegative<=7-remainingfivepositivefreq; no separateB19 bound (safe relaxation).','rows':out,'all_two_duals_strict':all(r.get('dual_certificate',{}).get('strict_below_one') for r in out),'cpu_seconds':time.process_time()-start}
(HERE/'SOLVE_TWO_E2.json').write_text(json.dumps(result,indent=2)+'\n')
print([(r['name'],r.get('maximum_common_coverage'),r.get('dual_certificate',{}).get('coverage_upper_bound')) for r in out]);print(result['cpu_seconds'])

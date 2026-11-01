"""Only four newly equal graph keys from the exact981 budget20->21 difference."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
import importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent
HELPER=HERE.parent/'six_label_pilot/joint_cover_lp/LP_DIAGNOSIS.py'
spec=importlib.util.spec_from_file_location('old_joint_model',HELPER);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
diff=json.loads((HERE/'CHECK.json').read_text())
source=json.loads((HERE.parent/'six_label_pilot/CENSUS_PROFILE.json').read_text())
lookup={tuple(r['vector']):r for r in source['rows']}
keys=[tuple(r['graph']) for r in diff['newly_nongated_records']];assert len(keys)==len(set(keys))==4
start=time.process_time();outrows=[]
for key in keys:
 row=lookup[key];R,V,D,B,mat=old.build(row);B[2]=21
 c=np.zeros(len(V)+1);c[-1]=-1
 res=linprog(c,A_ub=mat,b_ub=np.asarray([0.]*len(R)+B),bounds=[(0.,1.)]*len(V)+[(0.,None)],method='highs',options={'time_limit':2.,'threads':1})
 out={'graph':key,'sets':row['sets'],'C3':row['C3'],'C4':row['C4'],'candidate_red_sets':R,
      'budgets':B,'negative_variables':len(V),'source_binding':'One of four exact newly-nongated keys from CHECK.json; all in complete981 graph domain.',
      'solver_status':int(res.status),'solver_message':str(res.message)}
 if res.success:
  out['maximum_common_coverage']=float(res.x[-1])
  if out['maximum_common_coverage']<1-1e-8:out['dual_certificate']=old.dual_certificate(res,R,V,D,B)
  else:out['primal_witness']=old.primal_witness(res,R,V,D,B)
 outrows.append(out)
 print(key,out.get('maximum_common_coverage'),out.get('dual_certificate',{}).get('coverage_upper_bound'),out.get('primal_witness',{}).get('exact_feasible'),flush=True)
 assert time.process_time()-start<10
out={'status':'FOUR_NEW_KEYS_SOLVED','budget_total':21,'cpu_seconds':time.process_time()-start,
     'rows':outrows,'all_four_exact_duals_strict':all(r.get('dual_certificate',{}).get('strict_below_one') for r in outrows),
     'model_source':str(HELPER.relative_to(HERE.parents[6])) if len(HERE.parents)>6 else str(HELPER),
     'scope':'Shared-capacity fractional negative coverage, all targets; no negative-layout integer enumeration, no new graph domain.'}
(HERE/'SOLVE_FOUR.json').write_text(json.dumps(out,indent=2)+'\n');print(out['all_four_exact_duals_strict'],out['cpu_seconds'])

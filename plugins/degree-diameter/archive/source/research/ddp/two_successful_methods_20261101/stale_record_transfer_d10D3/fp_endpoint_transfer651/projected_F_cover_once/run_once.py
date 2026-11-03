import time
START=time.process_time()
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
import json,resource,math,warnings
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
HERE=Path(__file__).resolve().parent;PRIOR=24.028512182

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one-shot exact projected model already attempted')
save('ATTEMPT.json',{'status':'STARTED','prior_read_prep_CPU':PRIOR,'casecap':45,'solverlimit18':True})
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix,save_npz
old=json.loads((HERE.parent/'twin_class_packet_capacity_gate/COEFFICIENT_BINDING.json').read_text())
F=old['F_labels'];P=old['P_labels'];twins=old['twins'];fc={int(k):v for k,v in old['F_class'].items()};pc={p:c for c,pair in enumerate(twins)for p in pair}
Cf={int(k):int(v)for k,v in old['C_f_masks_decimal_strings'].items()};Dp={int(k):int(v)for k,v in old['D_p_masks_decimal_strings'].items()}
rr=[];cc=[];vv=[];labels=[];lo=[];hi=[]
def row(label,l=-np.inf,h=np.inf):
 labels.append(label);lo.append(l);hi.append(h);return len(labels)-1
quota=[row(['class_F_quota',c],h=2)for c in range(65)]
donor=[row(['class_star_requires_F',c],h=0)for c in range(65)]
fsum=row(['eight_F'],8,8);psum=row(['two_starP'],2,2)
cover=[row(['F_cover',f],l=1)for f in F]
def add(r,c,v=1):rr.append(r);cc.append(c);vv.append(v)
def ones(mask):
 while mask:
  bit=mask&-mask;yield bit.bit_length()-1;mask-=bit
for i,f in enumerate(F):
 add(quota[fc[f]],i);add(donor[fc[f]],i,-1);add(fsum,i)
 for t in ones(Cf[f]):add(cover[t],i)
for i,p in enumerate(P):
 col=520+i;add(donor[pc[p]],col);add(psum,col)
 for t in ones(Dp[p]):add(cover[t],col)
A=coo_matrix((np.asarray(vv,dtype=float),(np.asarray(rr,dtype=np.int32),np.asarray(cc,dtype=np.int32))),shape=(652,650)).tocsc()
assert A.shape==(652,650)and A.nnz==50440
save_npz(HERE/'MODEL_MATRIX.npz',A)
save('MODEL.json',{'variables':650,'rows':652,'nnz':A.nnz,'variable_labels':[['select_F',f]for f in F]+[['starP',p]for p in P],'row_labels':labels,'row_lower':[None if not math.isfinite(x)else x for x in lo],'row_upper':[None if not math.isfinite(x)else x for x in hi],'source':'COEFFICIENT_BINDING only;source/A2notread','scope':'exactoldFcoverprojection,notfullgraphD3','solver':'SciPy/HiGHS once18seconds threads1 allzeroobjective'})
save('HANDLE.json',{'PID':os.getpid(),'status':'SOLVING_ONE_EXACT_PROJECTED_F_COVER','solverlimit':18,'CPU_before_solve':time.process_time()-START,'prior':PRIOR})
s0=time.process_time()
with warnings.catch_warnings(record=True)as ws:
 sol=milp(np.zeros(650),integrality=np.ones(650,dtype=np.uint8),bounds=Bounds(np.zeros(650),np.ones(650)),constraints=LinearConstraint(A,np.asarray(lo),np.asarray(hi)),options={'time_limit':18.,'threads':1,'presolve':True})
solvercpu=time.process_time()-s0
raw={'status':int(sol.status),'message':str(sol.message),'CPU':solvercpu,'incumbent':None if sol.x is None else sol.x.tolist(),'nodes':None if getattr(sol,'mip_node_count',None)is None else int(sol.mip_node_count),'warnings':[str(w.message)for w in ws]}
save('SOLVER_RETURN.json',raw)
found=False
if sol.x is not None:
 x=np.rint(sol.x).astype(np.int8);vals=A@x
 assert np.max(np.abs(sol.x-x))<1e-5 and all(v>=l-1e-8 and v<=h+1e-8 for v,l,h in zip(vals,lo,hi))
 ys=[f for i,f in enumerate(F)if x[i]];zs=[p for i,p in enumerate(P)if x[520+i]]
 union=0
 for f in ys:union|=Cf[f]
 for p in zs:union|=Dp[p]
 assert len(ys)==8 and len(zs)==2 and union==(1<<520)-1
 found=True;save('ACTUAL_F_COVER_SELECTION.json',{'F_selected':ys,'star_P':zs,'class_F_counts':[sum(fc[f]==c for f in ys)for c in range(65)],'class_star_counts':[sum(pc[p]==c for p in zs)for c in range(65)],'exact_saved_coeff_F_coverage':520,'donor_assignments':'NOT_YET_FROZEN','PPpairings_newroot_oldold_BFS':0,'not_a_graph_yet':True})
status='ACTUAL_F_COVER_FEASIBLE_OBJECT_FOUND'if found else('NUMERICAL_INFEASIBLE_NO_CHECKED_CERTIFICATE'if sol.status==2 else'UNKNOWN_PROJECTED_F_COVER_NO_INCUMBENT')
r={'status':status,'solver_status':int(sol.status),'solver_calls_this_batch':1,'old_solver_not_resumed':True,'solver_CPU':solvercpu,'process_CPU':time.process_time()-START,'prior_read_prep_CPU':PRIOR,'wholecase_CPU':PRIOR+time.process_time()-START,'case_cap':45,'variables':650,'rows':652,'nnz':50440,'actual_F_cover_object':found,'source_adj_A2_A3_BFS_graph_Lean_ARIS':0,'new_graph_parameter_Lean':[0,0,0],'scope':'oneexactcompressedfeasibilitywindow,notcertifiedinfeasibility/full651','next':'constructexplicitdonorobjectsifFcoverfound;otherwiseSTOP_NO_THIRD_SOLVE_OR_SEED','terminal':True}
save('RESULT.json',r);save('TERMINAL.json',r)
print(json.dumps(r,ensure_ascii=False),flush=True)

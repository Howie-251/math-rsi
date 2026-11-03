from pathlib import Path
import json,math,os,time
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
D=Path(__file__).resolve().parent;start=time.process_time()
import numpy as np
from scipy import sparse
import scipy.optimize._highspy._core as h

def save(n,x):(D/n).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def clean(x):
 if isinstance(x,float) and not math.isfinite(x):return str(x)
 return x
B=np.fromfile(D.parent/'BASE_COVER_MASKS.u32',dtype='<u4');assert B.size==36**4
pop=np.array([x.bit_count() for x in range(256)],dtype=np.uint8)
m=pop[B.view(np.uint8)].reshape(-1,4).sum(axis=1,dtype=np.uint8).reshape(1296,1296)
(D/'M_POPCOUNTS.u8').write_bytes(m.tobytes())
target,choice=np.nonzero(m);vals=m[target,choice].astype(np.float64)
rows=np.concatenate([choice[:0],target+72,np.arange(36).repeat(36),np.tile(np.arange(36),36)+36,np.arange(1296)+72])
cols=np.concatenate([choice,np.arange(1296),np.arange(1296),np.full(1296,1296)])
data=np.concatenate([vals,np.ones(2592),-np.ones(1296)])
A=sparse.coo_matrix((data,(rows,cols)),shape=(1368,1297)).tocsc();A.sort_indices()
lower=np.concatenate([np.ones(72),np.zeros(1296)]);upper=np.concatenate([np.ones(72),np.full(1296,h.kHighsInf)])
cost=np.zeros(1297);cost[-1]=-1
np.savez(D/'ASSIGNMENT_MATRIX.npz',indptr=A.indptr,indices=A.indices,data=A.data,row_lower=lower,row_upper=upper,cost=cost)
model={'assignment_binary':1296,'integer_z':1,'rows':1368,'rowcol_equalities':72,'capacity_inequalities':1296,'nnz':int(A.nnz),'m_nonzeros':int(vals.size),'objective':'maximize min_i,j sum_r m(i,j;r,sigma_r)','time_limit':5,'threads':1,'matrix_layout':'row0..35out,36..71in,72+36i+jcapacity;col36r+s;lastz','source_DP_BFS_runs':0}
save('ASSIGNMENT_MODEL.json',model)
lp=h.HighsLp();lp.num_col_=1297;lp.num_row_=1368;lp.col_cost_=cost;lp.col_lower_=np.zeros(1297);lp.col_upper_=np.concatenate([np.ones(1296),np.array([684.])]);lp.row_lower_=lower;lp.row_upper_=upper;lp.integrality_=[h.HighsVarType.kInteger]*1297
lp.a_matrix_.num_col_=1297;lp.a_matrix_.num_row_=1368;lp.a_matrix_.format_=h.MatrixFormat.kColwise;lp.a_matrix_.start_=A.indptr.astype(np.int32);lp.a_matrix_.index_=A.indices.astype(np.int32);lp.a_matrix_.value_=A.data
highs=h._Highs()
for name,value in [('threads',1),('time_limit',5.0)]:assert highs.setOptionValue(name,value)==h.HighsStatus.kOk
assert highs.passModel(lp)==h.HighsStatus.kOk
warm=np.zeros(1297);warm[np.arange(36)*36+np.arange(36)]=1
warmcap=m[:,np.arange(36)*36+np.arange(36)].sum(axis=1,dtype=np.int32);warm[-1]=int(warmcap.min())
sol=h.HighsSolution();sol.col_value=warm.tolist();sol.row_value=(A@warm).tolist();sol.value_valid=True;sol.dual_valid=False;warmstatus=highs.setSolution(sol)
save('ASSIGNMENT_WARM.json',{'sigma':list(range(36)),'actual_min_capacity':int(warmcap.min()),'z':int(warm[-1]),'setSolution':str(warmstatus)})
assert warmstatus==h.HighsStatus.kOk
before=time.process_time();runstatus=highs.run();solvercpu=time.process_time()-before;info=highs.getInfo();ms=highs.getModelStatus();best=highs.getSolution();x=np.asarray(best.col_value)
raw={'run_status':str(runstatus),'model_status':str(ms),'message':highs.modelStatusToString(ms),'value_valid':bool(best.value_valid),'solver_CPU':solvercpu,'child_CPU_sofar':time.process_time()-start}
for key in ['objective_function_value','mip_node_count','mip_dual_bound','mip_gap','primal_solution_status','num_primal_infeasibilities']:raw[key]=clean(getattr(info,key,None))
save('ASSIGNMENT_RAW.json',dict(raw,col_values=[clean(float(v)) for v in x]))
valid=bool(best.value_valid) and x.size==1297
if valid:
 rounded=np.rint(x).astype(np.int32);valid=bool(np.all(np.abs(x-rounded)<=1e-6) and np.all(rounded[:1296]>=0) and np.all(rounded[:1296]<=1))
if valid:
 mat=rounded[:1296].reshape(36,36);valid=bool(np.all(mat.sum(axis=0)==1) and np.all(mat.sum(axis=1)==1))
sigma=None;minimum=None;capacities=None
if valid:
 sigma=np.argmax(mat,axis=1).astype(int).tolist();capacities=m[:,np.arange(36)*36+np.array(sigma)].sum(axis=1,dtype=np.int32);minimum=int(capacities.min())
 save('ASSIGNMENT_INTEGER_CHECK.json',{'status':'BINARY_SIGMA_AND_ALL1296_CAPACITIES_CHECKED','sigma':sigma,'minimum_capacity':minimum,'all1296_capacities':capacities.astype(int).tolist(),'raw_z':float(x[-1]),'not_point_coverage':True})
eligible=valid and minimum>=19
if eligible:
 save('FROZEN_SIGMA.json',{'sigma':sigma,'actual_min_capacity':minimum,'selected_once':True,'not_offset_or_graph_result':True})
 (D/'FROZEN_SIGMA.tsv').write_text(''.join(f'{r}\t{s}\n' for r,s in enumerate(sigma)))
save('ASSIGNMENT_RESULT.json',{'status':'FROZEN_ONE_ELIGIBLE_SIGMA' if eligible else 'UNKNOWN_STOP_NO_ELIGIBLE_ASSIGNMENT','eligible':bool(eligible),'sigma':sigma,'minimum_capacity':minimum,'raw':raw,'solver_calls':1,'child_actual_CPU':time.process_time()-start,'graph_generated':False})
print(json.dumps({'eligible':bool(eligible),'minimum_capacity':minimum,'raw':raw}),flush=True)

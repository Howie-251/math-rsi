"""One shared-budget sparse constraint-generation feasibility experiment."""
import json
import os
from pathlib import Path
import resource
import subprocess
import time
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
P=Path(__file__).resolve().parent;start=time.process_time();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
def localcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
def save(name,x):(P/name).write_text(json.dumps(x,indent=2)+'\n')
pre=json.loads((P/'PREFLIGHT.json').read_text());prior=pre['total_phase1_parent_children_CPU_seconds']
def remaining():return 10-prior-localcpu()
save('RUN_HANDLE.json',dict(status='ACTUAL_SHARED_BUDGET_CONSTRAINT_GENERATION_RUNNING',pid=os.getpid(),command='python solve.py',total_CPU_limit=10,phase1_CPU=prior))
result=dict(target_Delta=15,target_D=5,savedL=102060,source_n=102060,source_m=765045,hypothetical_n=102061,actual_n=None,actual_D=None,ordinary_bad_unordered_pairs=None,source_allroot_BFS=0,candidate_newroot_BFS=0)
if pre['status']!='ALL810_R4_COMPLETE':
    result.update(status='UNKNOWN_PHASE1_INCOMPLETE')
elif pre['all_union']<102060:
    result.update(status='ALL_ELIGIBLE_R4_UNION_MISS',witness=pre['union_missing_first20'][0])
else:
    import numpy as np
    from scipy.optimize import Bounds,LinearConstraint,linprog,milp
    from scipy.sparse import csc_matrix,vstack
    N=102060;R=810;W=1595;TW=13
    balls=np.memmap(P/'radius4.u64le.bin',dtype='<u8',mode='r',shape=(R,W))
    target=np.memmap(P/'target_rows.u64le.bin',dtype='<u8',mode='r',shape=(N,TW))
    support=np.memmap(P/'target_support.u16le.bin',dtype='<u2',mode='r',shape=(N,))
    # Exact byte comparisons determine duplicates; this is not a hash artifact.
    packed=target.view(np.dtype((np.void,TW*8))).reshape(N)
    unique_target_rows=len(np.unique(packed))
    rare=np.argsort(support,kind='stable')[:128].tolist()
    spread=np.linspace(0,N-1,128,dtype=int).tolist()
    active=list(dict.fromkeys(rare+spread));activepatterns=set();filtered=[]
    for t in active:
        pattern=bytes(target[t])
        if pattern not in activepatterns:activepatterns.add(pattern);filtered.append(t)
    active=filtered
    def sparse_rows(targets):
        ind=[];rr=[]
        for row,t in enumerate(targets):
            bits=int.from_bytes(target[t].tobytes(),'little')
            while bits:
                b=bits&-bits;col=b.bit_length()-1
                if col<R:ind.append(col);rr.append(row)
                bits^=b
        return csc_matrix((np.ones(len(ind)),(rr,ind)),shape=(len(targets),R))
    def fullcheck(selected):
        cov=np.bitwise_or.reduce(balls[selected],axis=0) if selected else np.zeros(W,dtype=np.uint64)
        holes=np.bitwise_not(cov);holes[-1]&=np.uint64((1<<(N%64))-1)
        ids=[]
        for k,x in enumerate(holes):
            v=int(x)
            while v:
                b=v&-v;ids.append(64*k+b.bit_length()-1);v^=b
        return ids
    initial=sparse_rows(active)
    lp=linprog(np.ones(R),A_ub=-initial,b_ub=-np.ones(len(active)),bounds=(0,1),method='highs',options={'time_limit':max(.01,remaining()-.55),'threads':1})
    save('LP_DIAGNOSTIC.json',dict(status=int(lp.status),message=lp.message,active_targets=active,fractional_minimum=None if lp.fun is None else float(lp.fun),row_dual=None if lp.ineqlin.marginals is None else list(map(float,lp.ineqlin.marginals)),scope='Initialvalidtargetsubset only; lowerbound is a necessary diagnostic for the fullproblem.',elapsed_total_CPU=prior+localcpu()))
    log=[];attempt=0
    result.update(status='UNKNOWN_SHARED_CPU_BUDGET',unique_target_support_rows=unique_target_rows,initial_target_constraints=len(active),sparse_constraint_generation=True,full_dense_matrix_allocated=False)
    while remaining()>.6:
        attempt+=1;A=sparse_rows(active)
        mat=vstack([A,csc_matrix(np.ones((1,R)))]).tocsc()
        constraints=LinearConstraint(mat,np.r_[np.ones(len(active)),-np.inf],np.r_[np.full(len(active),np.inf),15])
        limit=max(.01,remaining()-.5)
        solved=milp(c=np.zeros(R),integrality=np.ones(R),bounds=Bounds(np.zeros(R),np.ones(R)),constraints=constraints,options={'time_limit':limit,'threads':1,'mip_rel_gap':0.0})
        selected=[] if solved.x is None else [i for i,x in enumerate(solved.x) if x>.5]
        entry=dict(iteration=attempt,target_constraints=len(active),nonzeros=A.nnz,solver_status=int(solved.status),solver_message=solved.message,time_limit_seconds=limit,selected_count=len(selected),elapsed_total_CPU=prior+localcpu())
        if solved.status==2:
            entry['interpretation']='Validtargetsubsetalreadyinfeasible; numericalMIPstatus only, nointegerproofartifactgenerated.'
            log.append(entry);result.update(status='NUMERICAL_THRESHOLD15_MODEL_INFEASIBLE',strict_proof_status='NOT_GENERATED',MIP_status=2);break
        if solved.x is None or not selected or len(selected)>15:
            log.append(entry);result.update(status='UNKNOWN_NO_COMPLETE_INCUMBENT',MIP_status=int(solved.status));break
        missing=fullcheck(selected)
        entry.update(exact_fulltarget_missing_count=len(missing),exact_checked_old_targets=N)
        log.append(entry);save('CONSTRAINT_GENERATION_LOG.json',log)
        if not missing:
            pins=[pre['eligible_labels'][i] for i in selected]
            (P/'PINS.txt').write_text(''.join(str(x)+'\n' for x in pins))
            save('LITERAL_NEW_NEIGHBORS.json',dict(source_n=N,newlabel=N,pins=pins,olddegrees=[14]*len(pins),exact_selected_R4_union=N))
            check=subprocess.run([str(P/'cover'),'candidate',str(P.parent/'source102060.author.adjlist.txt'),str(P)],capture_output=True,text=True)
            (P/'candidate.log').write_text(check.stdout+check.stderr);check.check_returncode()
            native=json.loads((P/'CANDIDATE_CHECK.json').read_text())
            result.update(status=native['status'],actual_n=102061,actual_m=native['m'],actual_D=5,actual_Delta=15,pins=pins,old_pin_degrees=[14]*len(pins),exact_fulltarget_R4_coverage=N,candidate_newroot_BFS=1,newroot_eccentricity=native['newroot_eccentricity'],newroot_visited=native['newroot_visited'],old_edges_all_retained=True,simple=True,graph_file='graph_d15_D5_n102061.edges');break
        # Add genuine uncovered targets only; no pin/score neighborhood or seed reset.
        ordered=sorted(missing,key=lambda t:(int(support[t]),t))
        proposed=ordered[:256]
        proposed += [missing[i] for i in np.linspace(0,len(missing)-1,min(256,len(missing)),dtype=int)]
        added=0
        for t in proposed:
            pattern=bytes(target[t])
            if pattern not in activepatterns:activepatterns.add(pattern);active.append(t);added+=1
        assert added>0
        log[-1]['new_true_counterexample_constraints']=added
    result.update(MIP_calls=attempt,final_target_constraints=len(active),constraint_generation_log=log)
    save('CONSTRAINT_GENERATION_LOG.json',log)
result['phase2_parent_children_CPU_seconds']=localcpu();result['total_shared_CPU_seconds']=prior+localcpu();result['phase1_CPU_seconds']=prior
save('RESULT.json',result)
save('terminal.json',dict(status=result['status'],running=False,pending=[],total_shared_CPU_seconds=result['total_shared_CPU_seconds']))
save('RUN_HANDLE.json',dict(status=result['status'],running=False,pid=os.getpid(),total_shared_CPU_seconds=result['total_shared_CPU_seconds']))
print(json.dumps({k:v for k,v in result.items() if k!='constraint_generation_log'}))

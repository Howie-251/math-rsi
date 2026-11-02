import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import resource
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
import json
from pathlib import Path
import subprocess
import time
import warnings
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

HERE=Path(__file__).resolve().parent
CACHE=HERE.parent
SOURCE=CACHE.parent/'source1141.header.edges'
N=1141;M=7987
def aggregate_cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
def checkpoint(status,**kw):
    save('RUN_HANDLE.json',{'status':status,'pid':os.getpid(),'aggregate_CPU_seconds':aggregate_cpu(),**kw})
checkpoint('PREPARING_CACHED_GLOBAL_MODEL')
edges=np.loadtxt(SOURCE,dtype=np.int32,skiprows=1)
assert edges.shape==(M,2)
adj=[[] for _ in range(N)]
edge_id={}
for i,(u,v) in enumerate(edges):
    u=int(u);v=int(v);adj[u].append(v);adj[v].append(u);edge_id[(u,v)]=i;edge_id[(v,u)]=i
assert all(len(a)==14 for a in adj)
for a in adj:a.sort()
A=np.zeros((N,N),dtype=bool)
for u in range(N):A[u,adj[u]]=True
A2=np.fromfile(CACHE/'A2.u16le.bin',dtype='<u2').reshape(N,N)
A3=np.fromfile(CACHE/'A3.u16le.bin',dtype='<u2').reshape(N,N)
closed=[set(a)|{u} for u,a in enumerate(adj)]
rows=[];cols=[];data=[];lbs=[];ubs=[]
nv=N+M
lower=[0.0]*nv;upper=[1.0]*nv;integrality=[1]*nv
def row(entries,lo=-np.inf,hi=np.inf):
    r=len(lbs)
    for c,z in entries:rows.append(r);cols.append(int(c));data.append(float(z))
    lbs.append(float(lo));ubs.append(float(hi))
for u in range(N):row([(u,-1)]+[(N+edge_id[(u,v)],1) for v in adj[u]],0,0)
row([(N+i,1) for i in range(M)],7,7)
for t in range(N):
    covered=np.flatnonzero((A2[t]>0)|A[t])
    assert t in covered
    row([(int(v),1) for v in covered],1,np.inf)
critical_count=0
for line in (CACHE/'EDGE_CRITICAL_MATCHINGS.jsonl').open():
    e=json.loads(line);i=e['edge_id'];assert tuple(e['edge'])==tuple(map(int,edges[i]))
    for a,mask in enumerate(e['critical_row_masks']):
        for b in range(13):
            if mask>>b&1:
                row([(N+i,1),(e['L'][a],-1),(e['R'][b],-1)],-np.inf,0);critical_count+=1
assert critical_count==173821
H=np.fromfile(CACHE/'FIRST_SUPPORTS.u16le.bin',dtype='<u2').reshape(N,N)
first_loss_rows=0
for u in range(N):
    for k,v in enumerate(adj[u]):
        targets=np.flatnonzero(H[u]==1<<k)
        if targets.size:
            t=int(targets[0])
            row([(N+edge_id[(u,v)],1)]+[(s,-1) for s in sorted(closed[t])],-np.inf,0)
            first_loss_rows+=1
initial_dims={'binary_x':N,'binary_y':M,'initial_variables':nv,'initial_rows':len(lbs),'initial_nonzeros':len(data),'vertex_matching_equations':N,'sum_cut_equations':1,'closed_R2_cover_rows':N,'critical_middle_rows':critical_count,'first_loss_singleton_rows_at_most_one_lex_target_per_directed_edge':first_loss_rows,'source_BFS':0,'A2_A3_recomputation':0,'preparation_aggregate_CPU_seconds':aggregate_cpu()}
save('MODEL_DIMENSIONS.json',initial_dims)
rounds=[];seen=set();new_pair_constraints=[];status='UNKNOWN_CPU_LIMIT';hit=None
warnings.filterwarnings('ignore',message='Unrecognized options detected:.*')
for turn in range(10):
    remaining=59.5-aggregate_cpu()
    if remaining<0.2:break
    matrix=coo_matrix((np.asarray(data), (np.asarray(rows,dtype=np.int32),np.asarray(cols,dtype=np.int32))),shape=(len(lbs),nv)).tocsc()
    objective=np.zeros(nv);objective[:N]=1
    checkpoint('SOLVING_GLOBAL_MILP',round=turn,variables=nv,rows=len(lbs),remaining_CPU_seconds=remaining)
    solved=milp(objective,integrality=np.asarray(integrality),bounds=Bounds(lower,upper),constraints=LinearConstraint(matrix,lbs,ubs),options={'time_limit':max(0.05,59.25-aggregate_cpu()),'threads':1,'mip_rel_gap':0.0})
    solver_info={'round':turn,'status':int(solved.status),'message':str(solved.message),'objective':None if solved.fun is None else float(solved.fun),'aggregate_CPU_seconds':aggregate_cpu(),'mip_node_count':None if getattr(solved,'mip_node_count',None) is None else int(solved.mip_node_count),'variables':nv,'rows':len(lbs)}
    save('LAST_SOLVER_RESULT.json',solver_info)
    if solved.x is None:
        rounds.append(solver_info)
        status='MILP_MODEL_INFEASIBLE' if solved.status==2 else 'UNKNOWN_NO_INCUMBENT'
        break
    vals=np.asarray(solved.x);pins=np.flatnonzero(vals[:N]>0.5).tolist();cuts=np.flatnonzero(vals[N:N+M]>0.5).tolist()
    assert len(pins)==14 and len(cuts)==7
    cut_endpoints=[int(v) for i in cuts for v in edges[i]]
    assert len(set(cut_endpoints))==14 and set(cut_endpoints)==set(pins)
    assert tuple(cuts) not in seen;seen.add(tuple(cuts))
    prefix=HERE/f'candidate_{turn:02d}'
    (prefix.with_suffix('.cuts.txt')).write_text(' '.join(map(str,cuts))+'\n')
    candidate={'round':turn,'source_n':N,'source_m':M,'newlabel':N,'n':1142,'m':7994,'pins':pins,'cut_edge_ids':cuts,'cut_edges':edges[cuts].tolist(),'solver':solver_info}
    save(prefix.name+'.parameters.json',candidate)
    checkpoint('VERIFYING_ACTUAL_MODIFIED_GRAPH',round=turn,pins=pins,cut_edge_ids=cuts)
    run=subprocess.run([str(HERE/'verify'),str(SOURCE),str(prefix.with_suffix('.cuts.txt')),str(prefix)],capture_output=True,text=True)
    (prefix.with_suffix('.verify.log')).write_text(run.stdout+run.stderr)
    assert run.returncode==0
    verification=json.loads(prefix.with_suffix('.verify.json').read_text());candidate['verification']=verification;rounds.append(candidate)
    save('INCUMBENT_ROUNDS.json',rounds)
    if verification['status']=='COMPLETE_D3_HIT':
        status='PRODUCER_FULL_D3_HIT';hit=candidate;save('HIT.json',candidate);break
    # Paper proof was independently confirmed before this worker was run.
    bad_pairs=verification['bad_pairs_sample']
    assert 1<=len(bad_pairs)<=32
    checkpoint('ADDING_EXACT_BAD_PAIR_PATH_CONSTRAINTS',round=turn,bad_pairs=bad_pairs)
    for p,q in bad_pairs:
        assert p!=q and not A[p,q] and A2[p,q]==0 and A3[p,q]>0
        paths=[]
        for u in adj[p]:
            for v in adj[u]:
                if A[v,q]:paths.append([edge_id[(p,u)],edge_id[(u,v)],edge_id[(v,q)]])
        assert len(paths)==int(A3[p,q])
        aux=[]
        for path in paths:
            r=nv;nv+=1;lower.append(0.0);upper.append(1.0);integrality.append(0);aux.append(r)
            for e in path:row([(r,1),(N+e,1)],-np.inf,1)
        a=nv;b=nv+1;nv+=2
        lower.extend([0.0,0.0]);upper.extend([1.0,1.0]);integrality.extend([0,0])
        row([(a,1),(p,-1)],-np.inf,0)
        row([(a,1)]+[(s,-1) for s in sorted(closed[q])],-np.inf,0)
        row([(b,1),(q,-1)],-np.inf,0)
        row([(b,1)]+[(s,-1) for s in sorted(closed[p])],-np.inf,0)
        row([(r,1) for r in aux]+[(a,1),(b,1)],1,np.inf)
        new_pair_constraints.append({'round':turn,'pair':[p,q],'source3paths':paths,'route_aux_count':len(aux)})
    save('LAZY_PAIR_CONSTRAINTS.json',new_pair_constraints)
else:
    status='UNKNOWN_TEN_INCUMBENT_LIMIT'
result={'status':status,'prediction':'REFUTED_BY_NECESSARY_MODEL_INFEASIBILITY' if status=='MILP_MODEL_INFEASIBLE' and not seen else 'SUPPORTED_NECESSARY_MODEL_HAS_INCUMBENT' if seen else 'UNKNOWN_NO_INCUMBENT','target_Delta':14,'target_D':3,'savedL':1141,'hypothetical_n':1142,'actual_n':1142 if seen else None,'actual_global_D':3 if hit else None,'ordinary_bad_unordered_pairs':0 if hit else None,'actual_modified_graphs':len(seen),'native_verification_rounds':len(seen),'complete_full_D3_hit':bool(hit),'incumbent_rounds':len(seen),'lazy_bad_pairs_added':len(new_pair_constraints),'initial_dimensions':initial_dims,'final_variables':nv,'final_rows':len(lbs),'source_distance_BFS':0,'A2_A3_recomputation':0,'aggregate_parent_children_CPU_seconds':aggregate_cpu(),'hard_CPU_seconds':60,'remaining_unexplored':'none only if infeasible; otherwise finite model remains open after UNKNOWN, or search stopped at first hit','rounds':rounds}
save('RESULT.json',result)
save('terminal.json',{'status':status,'complete':status in ['MILP_MODEL_INFEASIBLE','PRODUCER_FULL_D3_HIT'],'pending':[],'aggregate_CPU_seconds':aggregate_cpu(),'actual_modified_graphs':len(seen)})
checkpoint(status,incumbents=len(seen),lazy_pairs=len(new_pair_constraints))
print(json.dumps({k:v for k,v in result.items() if k!='rounds'},indent=2))

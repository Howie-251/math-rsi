#!/usr/bin/env python3
"""Single specified dispersed-omission base; no balls, masks, solver or BFS."""
import os,resource
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
resource.setrlimit(resource.RLIMIT_CPU,(15,15))
usage0=resource.getrusage(resource.RUSAGE_SELF)
from pathlib import Path
from collections import Counter
import csv,json
import numpy as np

D=Path(__file__).resolve().parent;OLD=D.parent/'mixed_copy_cycle_sigma_31'
def read(p):return json.loads(p.read_text())
def save(name,value):
    p=D/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(value,indent=2)+'\n');os.replace(t,p)
def cpu():
    u=resource.getrusage(resource.RUSAGE_SELF)
    return u.ru_utime+u.ru_stime-usage0.ru_utime-usage0.ru_stime
assert not(D/'G0.edges').exists(),'Fixed dispersed base already exists; inspect receipt instead of rerunning.'
save('PRODUCER_HANDLE.json',dict(status='RUNNING',pid=os.getpid(),CPU_budget_seconds=15,worker_count=1))
prior=read(OLD/'PARAMETERS.json');groups=read(OLD/'INTEG_BLOCK_LOCAL_BINDING_RESULT.json')['groups']
ports=prior['B_absolute_labels'];sigpairs=prior['sigma_absolute_pairs']
omitted=[min(groups[str(y)])for y in range(1,6)]
assert omitted==[73,138,204,269,334]
assert read(OLD/'NEW_B_CUBE_CHECK.json')['status']=='PASS'
# Old cube/field/sigma/R2/Steiner properties are inherited, never recomputed.
S=[set()for _ in range(8775)];source_edges=[]
with(OLD/'S8775.edges').open()as f:
    header=list(map(int,f.readline().split()));assert header==[8775,118300]
    for line in f:
        u,v=map(int,line.split());S[u].add(v);S[v].add(u);source_edges.append((u,v))
assert len(source_edges)==118300
G=[set(row)for row in S];owner={};reps={};meta={}
for a in range(5):
    for bi,b in enumerate(ports):
        c=585*a+b;reps[a,b,0]=c;meta[c]=(a,b,bi,0,c)
        for v in S[c]:owner[v]=c
clones=[]
for copy in range(1,5):
    for a in range(5):
        for bi,b in enumerate(ports):
            if copy==4 and b==omitted[a]:continue
            c=585*a+b;v=len(G);G.append(set(S[c]));reps[a,b,copy]=v;meta[v]=(a,b,bi,copy,c)
            for u in S[c]:G[u].add(v)
            clones.append((v,copy,a,bi,b,c,len(S[c])))
assert len(G)==10070 and len(clones)==1295 and len(reps)==1620
assert all(row[-1]==26 for row in clones)
mandatory_m=sum(map(len,G))//2;assert mandatory_m==151970
peer_rows=[];skipped=[]
def peer(u,v,kind):
    assert u!=v and v not in G[u]and u not in G[v]
    G[u].add(v);G[v].add(u);peer_rows.append((kind,min(u,v),max(u,v)))
for a in range(5):
    for b in ports:
        copies=[j for j in range(5)if(a,b,j)in reps]
        for i in range(len(copies)):
            peer(reps[a,b,copies[i]],reps[a,b,copies[(i+1)%len(copies)]],'copy_cycle')
cycle_edges=len(peer_rows);assert cycle_edges==1620
for a in range(5):
    for copy in range(5):
        for b,bb in sigpairs:
            if(a,b,copy)in reps and(a,bb,copy)in reps:
                peer(reps[a,b,copy],reps[a,bb,copy],'sigma_matching')
            else:skipped.append((a,copy,b,bb))
matching_edges=len(peer_rows)-cycle_edges
assert matching_edges==795 and len(skipped)==5
degree=np.array([len(row)for row in G],dtype=np.int32)
hist=Counter(map(int,degree));assert hist==Counter({28:30,29:1590,30:130,31:8320})
pool_all=np.flatnonzero(degree<31).astype(np.int32)
spare_all=(31-degree[pool_all]).astype(np.int32)
assert len(pool_all)==1750 and Counter(map(int,spare_all))==Counter({1:130,2:1590,3:30})
freed=np.array([v for v in range(8775)if degree[v]==30 and v not in meta],dtype=np.int32)
assert len(freed)==130 and all(degree[v]==30 for v in freed)
restricted_spare=np.ones(130,dtype=np.int32)
assert sum(v in meta for v in pool_all)==1620
all_edges=[(u,v)for u,row in enumerate(G)for v in sorted(row)if u<v]
assert len(all_edges)==154385 and sum(map(len,G))==2*len(all_edges)
assert all(u!=v and u in G[v]for u,row in enumerate(G)for v in row)
with(D/'G0.edges').open('w')as f:
    f.write('10070 154385\n');f.writelines(f'{u} {v}\n'for u,v in all_edges)
indptr=np.zeros(10071,dtype=np.int64);indptr[1:]=np.cumsum(degree,dtype=np.int64)
indices=np.empty(int(indptr[-1]),dtype=np.int32)
for v,row in enumerate(G):indices[indptr[v]:indptr[v+1]]=sorted(row)
np.savez(D/'G0_INPUT.npz',indptr=indptr,indices=indices,pool=freed,spare=restricted_spare,n=np.int32(10070))

def data(v):
    if v in meta:
        a,b,bi,j,c=meta[v];kind='old_center'if j==0 else'clone';old=v if j==0 else-1
    else:
        c=owner[v];a,b=divmod(c,585);bi=ports.index(b);j=-1;old=v
        kind='freed_U'if degree[v]==30 else'saturated_U'
    return [kind,old,c,a,b,bi,j,int(degree[v]),31-int(degree[v])]
with(D/'ORDERED_LABEL_RECIPE.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['label','kind','source_vertex_label','source_center_label','class_a','class_b_label','class_b_index','copy','degree','spare'])
    w.writerows([v,*data(v)]for v in range(10070))
with(D/'ORDERED_CLONES.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['label','copy','class_a','class_b_index','class_b_label','source_center_label','mandatory_N_size']);w.writerows(clones)
for filename,pool in [('PIN_POOL_ALL.tsv',pool_all),('FREED_U130.tsv',freed)]:
    with(D/filename).open('w',newline='')as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['pool_index','label','kind','source_vertex_label','source_center_label','class_a','class_b_label','class_b_index','copy','degree','spare'])
        w.writerows([i,int(v),*data(int(v))]for i,v in enumerate(pool))
with(D/'OMITTED_COPY_CLASSES.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['class_a','class_b_label','source_center_label','omitted_copy']);w.writerows((a,b,585*a+b,4)for a,b in enumerate(omitted))
with(D/'PEER_EDGE_RECIPE.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['kind','u','v']);w.writerows(peer_rows)
with(D/'SKIPPED_SIGMA_MATCHINGS.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['class_a','copy','B_port_1','B_port_2']);w.writerows(skipped)

params=dict(source_S='../mixed_copy_cycle_sigma_31/S8775.edges',source_n=8775,source_m=118300,
    source_parse_count=1,inherited_evidence=['prior literalA³=4A+J','../mixed_copy_cycle_sigma_31/NEW_B_CUBE_CHECK.json',
        'prior sigma literal pairs and edge/order2 proof','saved old projection-group binding'],
    B_absolute_labels=ports,sigma_absolute_pairs=sigpairs,omission_B_labels_by_A=omitted,
    omission_selection='a0..4 take minimum of saved groups1..5, respectively',omitted_copy=4,
    source_label='585*x+y',copy_convention='0 original center; copies1..4, skip copy4 for the one selected b per a',
    clone_label_order='start8775; copy outer, a0..4, then saved increasing B-port label; skip exactly five selected classes',
    n=10070,mandatory_m=151970,cycle_edges=1620,matching_edges=795,m=154385,
    degree_histogram=dict(sorted(hist.items())),unrestricted_pool_size=1750,
    unrestricted_spare_histogram=dict(sorted(Counter(map(int,spare_all)).items())),
    restricted_solver_pool='ONLY130 freed original-U vertices; all spare1; all1620 eligible F vertices excluded from this submodel',
    npz='G0_INPUT.npz',npz_keys=dict(indptr='int64 shape10071',indices='int32 shape308770, sorted both directions',
        pool='int32 shape130 ascending freed-U labels ONLY',spare='int32 shape130 all1',n='int32 scalar10070'),
    unrestricted_pool_table='PIN_POOL_ALL.tsv',restricted_pool_table='FREED_U130.tsv',
    new_reach_group_prediction='NOT_CHECKED_HERE_ROOT_MASK_PREPARATION_SCOPE',
    root_future_model='six disjoint own-radius2 covers of all currentG0 targets, each at most26 pins',
    candidate_if_all130_assigned=dict(n=10076,m=154530,Delta=31,D='CONDITIONAL_NOT_GENERATED'),priority='UNKNOWN')
save('PARAMETERS.json',params)
proof='''# One dispersed-omission base, with a deliberately restricted pool

The actual source is the previously saved S8775/118300. Its literal A³ and
newly checked B³ synchronize three-walks; those receipts are inherited here,
not recomputed. This producer reads the S edge table once and retains every
source edge and vertex. No585 input, field, R2/Steiner, cube or sigma property
is rechecked.

Exactly copy4 of classes(a,b_a), a0..4,b_a=[73,138,204,269,334], is absent.
These are the minima of the saved groups1..5, not a new hole search. The1295
remaining clones have complete ORIGINAL S neighborhoods of26 vertices, so
mandatory n10070/m151970 follows. Every new/old Walk in this mandatory graph
uses only original S interior vertices; omission of other copies does not
remove those routes. Repeated centers meet through a common old neighbor.

Present-copy4/5 cycles add1620 edges. Saved same-copy sigma pairs add edges
only when BOTH endpoints exist. Exactly five pair occurrences are omitted,
recorded individually, so matching edges795 and total m154385. These extra
edges preserve old Walks and provide selected shorter routes; no BFS is run.

All1620 free class representatives have two cycle neighbors. Twenty-five
representatives over fixed B0 have no matching, and five copy4 sigma partners
lose their match due to the selected missing endpoint. Thus30 F have degree28
and1590 F have degree29. The five omitted full neighborhoods are disjoint
in the inherited source code:130 original U vertices now have degree30,
while8320 U stay31. The actual complete new graph degrees match these counts.

The unrestricted eligible pool remains1750 (spare3:30,2:1590,1:130) and is
preserved in PIN_POOL_ALL.tsv. The solver input is intentionally narrower:
G0_INPUT.npz.pool contains ONLY the130 original freed-U labels in ascending
order and spare is int32 ones. It does not contain any of the1620 eligible F
vertices. FREED_U130.tsv records every restricted label. Both-direction CSR
rows are sorted; indptr is int64, indices/pool/spare int32, n an int32 scalar.

The producer computes no B1/B2 balls, target masks or new reach/group
supports. Root owns that once-only mask preparation and the proposed exact
six-color own-radius2-cover model. Its coverage feasibility remains UNKNOWN
here. Conditional10076/154530 would require all130 pins assigned plus K6;
no helper or final candidate is generated by this base batch.

This is one effective change of rule after the old same-column scope was
closed. That older UNKNOWN solver history, rational LP witness and separate
integer exclusion are untouched. This batch starts no alternate hole/seed,
solver, field, BFS, Lean, paid review, archive or portfolio count. The86/98
expert draft and all frozen/root files remain unchanged.
'''
(D/'PROOF.md').write_text(proof)
total=cpu();assert total<15
result=dict(status='DISPERSED_OMISSION_BASE_PASS_RESTRICTED_U130_INPUT_READY',n=10070,m=154385,cap=31,
    source_n=8775,source_m=118300,source_parse_count=1,source_edges_retained=118300,
    mandatory_m=151970,clones=1295,omitted_copy_classes=5,omission_B_labels_by_A=omitted,
    cycle_edges=1620,sigma_matching_edges=795,sigma_matchings_skipped=5,
    degree_histogram=dict(sorted(hist.items())),unrestricted_eligible_pool_size=1750,
    unrestricted_spare_histogram=dict(sorted(Counter(map(int,spare_all)).items())),
    restricted_npz_pool_size=130,restricted_npz_spare_histogram={1:130},
    restricted_pool_is_ONLY_original_freed_U=True,eligible_F_excluded_from_npz_pool=1620,
    NPZ='G0_INPUT.npz',strictlex_simple_header=True,CSR_sorted_both_directions=True,
    new_group_reach_checks=0,solver_BFS_Lean_paid_review_runs=0,old_factor_sigma_geometry_R2_cube_checks_repeated=0,
    conditional10076_candidate_generated=False,CPU_seconds=total,CPU_budget_seconds=15,worker_count=1,
    portfolio_increment=0,new_parameter_increment=0,Lean_increment=0,root_expert_frozen_files_modified=False)
save('RESULT.json',result)
save('TERMINAL.json',dict(status=result['status'],running=False,active_processes=[],CPU_seconds=cpu(),CPU_budget_seconds=15,
    restricted_pool130=True,unrestricted_pool1750_separate=True,solver_or_reach_masks_not_run=True,
    no_second_hole_or_seed=True,portfolio_increment=0,Lean_increment=0))
save('PRODUCER_HANDLE.json',dict(status='TERMINAL',running=False,active_processes=[],CPU_seconds=cpu()))
print(json.dumps(dict(status=result['status'],n=10070,m=154385,degree_histogram=result['degree_histogram'],
    unrestricted_pool1750=True,restricted_npz_pool130=True,CPU_seconds=cpu())))

#!/usr/bin/env python3
"""The single specified mixed-copy/cycle/sigma base, without any solver/BFS."""
from pathlib import Path
from collections import Counter
import csv,json,os,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
started=time.process_time();usage0=resource.getrusage(resource.RUSAGE_SELF)
import numpy as np

D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
OLD=ROOT/'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction'
CAL=ROOT/'research/ddp/two_successful_methods_20261101/retained_edge_transfer/polarity_product2_8_helper_barrier/controlled_q2_square_clique5_230'
PART=ROOT/'research/ddp/polarity585_replication/SOURCE_PARTITION_CHECK.json'
def read(p):return json.loads(p.read_text())
def save(name,value):
    p=D/name;tmp=p.with_suffix(p.suffix+'.tmp')
    tmp.write_text(json.dumps(value,indent=2)+'\n');os.replace(tmp,p)
def cpu():
    u=resource.getrusage(resource.RUSAGE_SELF)
    return u.ru_utime+u.ru_stime-usage0.ru_utime-usage0.ru_stime
assert not(D/'G0.edges').exists(),'One fixed base already exists; inspect its receipt, do not rerun.'
save('PRODUCER_HANDLE.json',dict(status='RUNNING',pid=os.getpid(),CPU_budget_seconds=30,worker_count=1))
A=read(CAL/'PARAMETERS.json')['factor_rows']
oldA=read(CAL/'RESULT.json')
assert oldA['checks']['factor_cube_identity_all225_pairs']
ports=read(PART)['low_degree_vertices']
assert len(A)==15 and len(ports)==65 and ports[0]==0
portset=set(ports)
sigma=read(OLD/'involution_probe/sigma.json')
oldSigma=read(OLD/'involution_probe/RESULT.json')
assert oldSigma['status']=='VERIFIED_NONTRIVIAL_INVOLUTION'
# Inherit old sigma edge-preservation/order2; do not rerun either check.
sigpairs=sigma['port_transpositions']
assert sigma['fixed_port']==0 and len(sigpairs)==32
simpleB=[list(map(int,line.split())) for line in(OLD/'source585.implicit_adj.txt').read_text().splitlines()if line.strip()]
assert len(simpleB)==585
B=[sorted(row+([v]if v in portset else[]))for v,row in enumerate(simpleB)]

# The only new factor-relation check: sparse three-step counts, compared on
# every585^2 entry. No distance-ball, old source BFS or Steiner computation.
cube_bad=[];bad_count=0;walk_count=0
for v in range(585):
    count=[0]*585
    for x in B[v]:
        for y in B[x]:
            for z in B[y]:count[z]+=1;walk_count+=1
    rowset=set(B[v])
    for z,value in enumerate(count):
        expected=1+16*(z in rowset)
        if value!=expected:
            bad_count+=1
            if len(cube_bad)<20:cube_bad.append(dict(source=v,target=z,actual=value,expected=expected))
cube=dict(status='PASS'if not bad_count else'FAIL',identity='B_looped^3=16*B_looped+J',
    n=585,ordered_entries_checked=585*585,relation_walks_accumulated=walk_count,
    mismatch_count=bad_count,first_mismatches=cube_bad,
    A_cube_repeated=False,old_B_R2_Steiner_BFS_repeated=False,sigma_order2_or_edge_preservation_repeated=False)
save('NEW_B_CUBE_CHECK.json',cube)
if bad_count:
    save('RESULT.json',dict(status='NEW_B_CUBE_PREDICTION_FAILED_STOP',cube=cube,CPU_seconds=cpu(),portfolio_increment=0))
    save('TERMINAL.json',dict(status='NEW_B_CUBE_PREDICTION_FAILED_STOP',running=False,CPU_seconds=cpu(),no_solver_started=True))
    raise SystemExit(1)

S=[set()for _ in range(8775)]
for x in range(15):
    for y in range(585):
        v=585*x+y
        S[v].update(585*xx+yy for xx in A[x] for yy in B[y]if 585*xx+yy!=v)
source_hist=Counter(map(len,S))
assert source_hist==Counter({26:325,27:8450})
centers=[585*a+b for a in range(5)for b in ports]
owner=[-1]*8775
for c in centers:
    assert len(S[c])==26
    for v in S[c]:assert owner[v]<0;owner[v]=c
assert sum(c>=0 for c in owner)==8450
source_edges=[(u,v)for u,row in enumerate(S)for v in sorted(row)if u<v]
assert len(source_edges)==118300

G=[set(row)for row in S]
reps={};meta={}
for a in range(5):
    for bi,b in enumerate(ports):
        c=585*a+b;reps[a,b,0]=c;meta[c]=(a,b,bi,0,c)
clone_rows=[]
for copy in range(1,5):
    for a in range(5):
        for bi,b in enumerate(ports):
            if copy==4 and b==0:continue
            c=585*a+b;v=len(G);G.append(set(S[c]))
            reps[a,b,copy]=v;meta[v]=(a,b,bi,copy,c)
            for u in S[c]:G[u].add(v)
            clone_rows.append((v,copy,a,bi,b,c,26))
assert len(G)==10070 and len(clone_rows)==1295 and len(reps)==1620
mandatory_m=sum(map(len,G))//2
assert mandatory_m==151970
peer_rows=[]
def peer(u,v,kind):
    assert u!=v and v not in G[u]and u not in G[v]
    G[u].add(v);G[v].add(u);peer_rows.append((kind,min(u,v),max(u,v)))
for a in range(5):
    for b in ports:
        copies=list(range(4 if b==0 else 5))
        for j in range(len(copies)):
            peer(reps[a,b,copies[j]],reps[a,b,copies[(j+1)%len(copies)]],'copy_cycle')
cycle_edges=len(peer_rows)
assert cycle_edges==1620
for a in range(5):
    for copy in range(5):
        for b,bb in sigpairs:peer(reps[a,b,copy],reps[a,bb,copy],'sigma_matching')
assert len(peer_rows)-cycle_edges==800 and len(peer_rows)==2420

degree=np.array([len(row)for row in G],dtype=np.int32)
hist=Counter(map(int,degree))
assert hist==Counter({28:20,29:1600,30:130,31:8320})
assert all(degree[v]==(28 if data[1]==0 else 29)for v,data in meta.items())
pool=np.flatnonzero(degree<31).astype(np.int32)
spare=(31-degree[pool]).astype(np.int32)
assert len(pool)==1750 and Counter(map(int,spare))==Counter({1:130,2:1600,3:20})
assert sum(v<8775 and v not in meta for v in pool)==130
all_edges=[(u,v)for u,row in enumerate(G)for v in sorted(row)if u<v]
assert len(all_edges)==154390 and sum(map(len,G))==2*len(all_edges)
assert all(u!=v and u in G[v]for u,row in enumerate(G)for v in row)
def write_edges(name,n,body):
    with(D/name).open('w')as f:
        f.write(f'{n} {len(body)}\n')
        f.writelines(f'{u} {v}\n'for u,v in body)
write_edges('S8775.edges',8775,source_edges)
write_edges('G0.edges',10070,all_edges)

indptr=np.zeros(10071,dtype=np.int64);indptr[1:]=np.cumsum(degree,dtype=np.int64)
indices=np.empty(int(indptr[-1]),dtype=np.int32)
for v,row in enumerate(G):indices[indptr[v]:indptr[v+1]]=sorted(row)
np.savez(D/'G0_INPUT.npz',indptr=indptr,indices=indices,pool=pool,spare=spare,n=np.int32(10070))

with(D/'ORDERED_LABEL_RECIPE.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['label','kind','source_vertex_label','source_center_label','class_a','class_b_label','class_b_index','copy','degree','spare'])
    for v in range(10070):
        if v in meta:
            a,b,bi,j,c=meta[v];kind='old_center'if j==0 else'clone'
            old=v if j==0 else-1
        else:
            c=owner[v];a,b=divmod(c,585);bi=ports.index(b);j=-1;old=v
            kind='freed_U'if degree[v]==30 else'saturated_U'
        w.writerow([v,kind,old,c,a,b,bi,j,int(degree[v]),31-int(degree[v])])
with(D/'ORDERED_CLONES.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['label','copy','class_a','class_b_index','class_b_label','source_center_label','mandatory_N_size']);w.writerows(clone_rows)
with(D/'PIN_POOL.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['pool_index','label','kind','source_center_label','class_a','class_b_label','copy','degree','spare'])
    for i,(vv,ss)in enumerate(zip(pool,spare)):
        v=int(vv)
        if v in meta:a,b,bi,j,c=meta[v];kind='old_center'if j==0 else'clone'
        else:c=owner[v];a,b=divmod(c,585);j=-1;kind='freed_U'
        w.writerow([i,v,kind,c,a,b,j,int(degree[v]),int(ss)])
with(D/'PEER_EDGE_RECIPE.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['kind','u','v']);w.writerows(peer_rows)
with(D/'OMITTED_COPY_CLASSES.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['class_a','class_b_label','source_center_label','omitted_copy']);w.writerows((a,0,585*a,4)for a in range(5))

params=dict(source_A=str((CAL/'PARAMETERS.json').relative_to(ROOT)),
    source_B=str((OLD/'source585.implicit_adj.txt').relative_to(ROOT)),
    source_ports=str(PART.relative_to(ROOT)),source_sigma=str((OLD/'involution_probe/sigma.json').relative_to(ROOT)),
    A_literal_rows=A,B_absolute_labels=ports,sigma_absolute_pairs=sigpairs,
    inherited_A_cube='A^3=4A+J, prior actual230 calibration',
    new_B_cube_check='NEW_B_CUBE_CHECK.json',inherited_sigma='old actual2600-edge preservation/order2; not rerun',
    source_product_label='585*x+y',source_n=8775,source_m=118300,
    code='a=0..4 times saved B_absolute_labels in saved increasing order',
    copy_convention='0=original source center; copies1,2,3,4; copy4 absent at b0=0 for all five a',
    clone_label_order='start8775; copy outer1..4, then a0..4, then saved increasing B-port label; skip five holes',
    mandatory_n=10070,mandatory_m=151970,copy_cycles='all present class representatives in copy order, closing cycle',
    sigma_matching='same a and copy, actual saved32 nonfixed B-port pairs',
    cycle_edges=1620,sigma_peer_edges=800,peer_edges=2420,n=10070,m=154390,cap=31,
    predicted_degree_histogram={28:20,29:1600,30:130,31:8320},pool_size=1750,
    predicted_spare_histogram={1:130,2:1600,3:20},npz='G0_INPUT.npz',
    npz_keys=dict(indptr='int64 shape10071',indices='int32 shape308780, sorted each row, both directions',
        pool='int32 shape1750, ascending vertex labels',spare='int32 shape1750, exact31-degree',n='int32 scalar10070'),
    helpers_not_generated=True,root_joint_model='six helpers K6; each≤26 pins; root owns one exact MILP',
    final10076_feasibility='UNKNOWN_NOT_SOLVED_HERE',priority='UNKNOWN',portfolio_increment=0)
save('PARAMETERS.json',params)
total=cpu();assert total<30
result=dict(status='FIXED_G0_PRODUCER_PASS_READY_FOR_ROOT_EXACT_JOINT_MODEL',n=10070,m=154390,cap=31,
    source_n=8775,source_m=118300,mandatory_n=10070,mandatory_m=151970,
    new_clone_count=1295,omitted_copy_classes=5,F_representatives=1620,
    cycle_edges=1620,sigma_matching_edges=800,total_peer_edges=2420,
    degree_histogram=dict(sorted(hist.items())),pool_size=1750,exact_spare_histogram=dict(sorted(Counter(map(int,spare)).items())),
    source_S_edges_preserved=True,all1295_clone_mandatory_Ns_equal_original_source=True,
    source_code_N_union=8450,freed_U_vertices=130,all_original_source_vertices_retained=True,
    strictlex_simple_undirected_header=True,CSR_sorted_rows=True,CSR_both_directions=True,
    npz_file='G0_INPUT.npz',npz_keys=list(params['npz_keys']),new_B_cube=cube,
    inherited_not_repeated=['A_cube','585_R2','Steiner','old_BFS','sigma2600edges','sigma_order2','field_geometry'],
    CPU_seconds=total,CPU_budget_seconds=30,worker_count=1,
    solver_BFS_Lean_paid_review_runs=0,final10076_feasibility='UNKNOWN_NOT_SOLVED_HERE',
    base_experiment_only=True,portfolio_increment=0,new_parameter_increment=0,Lean_increment=0,
    root_counts_Wiki_frozen_expert_files_modified=False)
save('RESULT.json',result)
save('TERMINAL.json',dict(status=result['status'],running=False,active_processes=[],CPU_seconds=cpu(),CPU_budget_seconds=30,
    source_base_complete=True,root_solver_not_started_by_producer=True,solver_BFS_Lean_runs=0,
    output_graph='G0.edges',output_CSR='G0_INPUT.npz',no_second_hole_peer_pattern=True,
    portfolio_increment=0,root_expert86_98_DRAFT_untouched=True))
save('PRODUCER_HANDLE.json',dict(status='TERMINAL',running=False,active_processes=[],CPU_seconds=cpu()))
print(json.dumps(dict(status=result['status'],n=10070,m=154390,degree_histogram=result['degree_histogram'],
    pool_size=1750,spare_histogram=result['exact_spare_histogram'],CPU_seconds=cpu(),npz='G0_INPUT.npz')))

#!/usr/bin/env python3
"""One targeted local relation-binding test. No solver or BFS."""
import os,resource,time
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
usage0=resource.getrusage(resource.RUSAGE_SELF)
from pathlib import Path
from collections import Counter
from itertools import combinations
import csv,json
import numpy as np

D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
OLD=ROOT/'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction'
prior_cpu=95.905302
def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime-usage0.ru_utime-usage0.ru_stime
def save(name,value):
    p=D/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(value,indent=2)+'\n');os.replace(t,p)
assert not(D/'INTEG_BLOCK_LOCAL_BINDING_RESULT.json').exists(),'One local test already has a receipt; do not repeat.'
params=json.loads((D/'PARAMETERS.json').read_text());A=[set(row)for row in params['A_literal_rows']]
ports=params['B_absolute_labels'];nonzero=[b for b in ports if b!=0]
sigpairs=params['sigma_absolute_pairs']
with np.load(D/'G0_INPUT.npz')as z:
    indptr=z['indptr'];indices=z['indices'];pool=z['pool'];spare=z['spare'];n=int(z['n'])
assert n==10070 and len(pool)==1750
adj=[indices[int(indptr[v]):int(indptr[v+1])].tolist()for v in range(n)]
# Extract the original B-neighbor labels from the current G0 row of(a0,b0),
# filtering the first A-coordinate row. No old B adjacency file is reread.
Y=sorted(v for v in adj[0]if 0<v<585)
cached=json.loads((OLD/'PORT_R2.json').read_text())
cached_R2={int(row['port']):set(row['R2'])for row in cached}
groups={y:[]for y in Y};groupof={};group_bad=[]
for b in nonzero:
    found=[y for y in Y if y in cached_R2[b]]
    if len(found)!=1:group_bad.append(dict(b=b,saved_support_Y_intersection=found))
    else:groupof[b]=found[0];groups[found[0]].append(b)
sigma_partner={};pair_block_counts=Counter();pair_bad=[]
for b,bb in sigpairs:
    sigma_partner[b]=bb;sigma_partner[bb]=b
    if b not in groupof or bb not in groupof or groupof[b]!=groupof[bb]:pair_bad.append([b,bb])
    else:pair_block_counts[groupof[b]]+=1
group_ok=(len(Y)==8 and len(nonzero)==64 and not group_bad and
          all(len(g)==8 for g in groups.values())and not pair_bad and
          all(pair_block_counts[y]==4 for y in Y)and set(sigma_partner)==set(nonzero))

P=[set(z for y in A[x]for z in A[y])for x in range(15)]
row_bad=[dict(x=x,size=len(row))for x,row in enumerate(P)if len(row)!=7]
pair_bad_A=[];miss_bad=[];maximum_intersection=0;pair_tests=0;miss_tests=0
for x,z in combinations(range(15),2):
    union=P[x]|P[z];miss=set(range(15))-union;pair_tests+=1
    if len(union)!=11:pair_bad_A.append(dict(x=x,z=z,union_size=len(union)))
    for a in range(5):
        for c in range(5):
            count=len(miss&(A[a]|{c}));maximum_intersection=max(maximum_intersection,count);miss_tests+=1
            if count>3:miss_bad.append(dict(x=x,z=z,a=a,c=c,missed=sorted(miss),intersection=count))
abs_bad=[dict(a=a,absolute_support=sorted(P[a]&set(range(5))))for a in range(5)if P[a]&set(range(5))!={a}]
A_ok=not(row_bad or pair_bad_A or miss_bad or abs_bad)and pair_tests==105 and miss_tests==2625

target_labels=[585*x+b for x in range(15)for b in nonzero]
target_index={v:i for i,v in enumerate(target_labels)}
target_bits=[0]*n
for v,i in target_index.items():target_bits[v]=1<<i
# Boolean adjacency-relation composition to a fixed960-target set only.
# This is not an ordinary BFS or any old585 radius computation.
one=[]
for v in range(n):
    mask=target_bits[v]
    for w in adj[v]:mask|=target_bits[w]
    one.append(mask)
meta={}
with(D/'ORDERED_LABEL_RECIPE.tsv').open()as f:
    for row in csv.DictReader(f,delimiter='\t'):meta[int(row['label'])]=row
def column_mask(b,aa):return sum(1<<target_index[585*a+b]for a in aa)
def decode(mask,limit=12):
    out=[]
    while mask and len(out)<limit:
        bit=mask&-mask;out.append(target_labels[bit.bit_length()-1]);mask-=bit
    return out
summaries=Counter();failures=[];detail=[];b1total=b2total=0
for pool_i,vv in enumerate(pool):
    v=int(vv);r=meta[v];kind=r['kind'];b1=one[v];b2=b1
    for w in adj[v]:b2|=one[w]
    b1total+=b1.bit_count();b2total+=b2.bit_count()
    if kind=='freed_U':
        x,y=divmod(v,585)
        if y in groups:
            category='U_120_group_rows';upper1=0
            upper2=sum(column_mask(b,P[x])for b in groups[y]);equal2=True
        else:category='other_U_10';upper1=upper2=0;equal2=True
    else:
        a=int(r['class_a']);b=int(r['class_b_label'])
        if b==0:category='F_b0_20';upper1=upper2=0;equal2=True
        else:
            category='F_nonzero_1600';partner=sigma_partner[b]
            upper1=column_mask(b,A[a])|column_mask(partner,{a})
            upper2=column_mask(b,P[a])|column_mask(partner,A[a]);equal2=False
    good1=(b1&~upper1)==0;good2=(b2==upper2 if equal2 else(b2&~upper2)==0)
    summaries[category]+=1
    if not(good1 and good2):
        if len(failures)<30:
            failures.append(dict(pool_index=pool_i,label=v,kind=kind,category=category,
                B1_extra_target_labels=decode(b1&~upper1),B2_extra_target_labels=decode(b2&~upper2),
                B2_missing_target_labels=decode(upper2&~b2)if equal2 else[],
                B1_count=b1.bit_count(),B2_count=b2.bit_count()))
    detail.append([pool_i,v,category,b1.bit_count(),b2.bit_count(),upper1.bit_count(),upper2.bit_count(),good1,good2])
expected_categories=Counter(U_120_group_rows=120,other_U_10=10,F_b0_20=20,F_nonzero_1600=1600)
envelope_ok=not failures and summaries==expected_categories
checks=dict(saved_R2_groups_and_sigma_block_binding=group_ok,A_positive_two_supports=A_ok,
    current_G0_target_envelopes=envelope_ok)
with(D/'INTEGER_BLOCK_GROUP_BINDINGS.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['B_absolute_label','group_y','sigma_partner'])
    w.writerows((b,groupof.get(b,-1),sigma_partner.get(b,-1))for b in nonzero)
with(D/'CURRENT_G0_POOL_ENVELOPE_BINDINGS.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['pool_index','label','category','actual_B1_targets','actual_B2_targets','upper_B1_targets','upper_B2_targets','B1_within_upper','B2_matches_requirement']);w.writerows(detail)
total=cpu();assert total<5
result=dict(status='ALL_FIXED_INTEGER_BLOCK_LOCAL_BINDINGS_PASS'if all(checks.values())else'LOCAL_BINDING_COUNTEREXAMPLE_STOP',
    checks=checks,prediction='INTEG_BLOCK_LOCAL_BINDING_PRED.md',root_paper_prediction='INTEGER_BLOCK_BARRIER_PREDICTION.md',
    Y_from_current_G0_source_row=Y,groups=groups,group_sizes={y:len(g)for y,g in groups.items()},
    sigma_pairs_per_group=dict(pair_block_counts),group_counterexamples=group_bad,sigma_cross_group_pairs=pair_bad,
    A_support_rows=[sorted(p)for p in P],A_row_tests=15,A_pair_tests=pair_tests,A_pair_union_target=11,
    A_pair_abs_abs_tests=miss_tests,A_missed_intersection_maximum=maximum_intersection,
    A_absolute_support_tests=5,A_counterexamples=dict(rows=row_bad,pairs=pair_bad_A,missed=miss_bad,absolute=abs_bad),
    targeted_pool_vertices=1750,original_target_labels_count=960,current_G0_relation='closed B1 and B2 restricted to A15 x nonzero B absolutes',
    actual_categories=dict(summaries),envelope_counterexamples=failures,
    actual_B1_target_incidence_count=b1total,actual_B2_target_incidence_count=b2total,
    envelope_copy_positions='generous subset bounds for F; equality required only U/zero-reach categories',
    CPU_seconds=total,CPU_limit_seconds=5,prior_original_model_CPU_seconds=prior_cpu,
    combined_original_model_CPU_seconds=prior_cpu+total,original_model_CPU_budget_seconds=120,
    original_MILP_status='UNKNOWN_UNCHANGED_NO_INTEGER_POINT',integer_block_paper_conclusion='SEPARATE_INDEPENDENT_PAPER_ATTACK_NOT_ASSUMED_HERE',
    operations=dict(new_solver=0,BFS=0,old_585_R2_recomputed=0,Steiner_recomputed=0,
        sigma_edge_or_order2_recheck=0,A_cube_recheck=0,field_geometry=0,Lean=0,paid_review=0,
        new_base_graph=0,targeted_current_CSR_relation_binding=1),
    portfolio_increment=0,new_parameter_increment=0,Lean_increment=0,root_counts_frozen_expert_files_modified=False)
save('INTEG_BLOCK_LOCAL_BINDING_RESULT.json',result)
save('INTEG_BLOCK_LOCAL_BINDING_TERMINAL.json',dict(state=result['status'],running=False,active_processes=[],
    CPU_seconds=cpu(),CPU_limit_seconds=5,prior_original_model_CPU_seconds=prior_cpu,
    combined_original_model_CPU_seconds=prior_cpu+cpu(),original_model_CPU_budget_seconds=120,
    original_MILP_UNKNOWN_history_unchanged=True,no_second_solver_or_new_base=True,portfolio_increment=0,Lean_increment=0))
print(json.dumps(dict(status=result['status'],checks=checks,group_sizes=result['group_sizes'],
    A_pair_tests=pair_tests,A_pair_abs_abs_tests=miss_tests,A_missed_intersection_maximum=maximum_intersection,
    categories=dict(summaries),first_counterexamples=failures[:3],CPU_seconds=cpu(),combined_original_model_CPU_seconds=prior_cpu+cpu())))

#!/usr/bin/env python3
"""One exact six-color own-cover model after spreading the five omissions."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import array
from collections import Counter
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(59,60))
start=resource.getrusage(resource.RUSAGE_SELF)
base=Path(__file__).resolve().parent

def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime-start.ru_utime-start.ru_stime

def save(name,obj):
    p=base/name;t=p.with_suffix(p.suffix+'.tmp')
    t.write_text(json.dumps(obj,indent=2)+'\n');t.replace(p)

def checkpoint(stage,**kwargs):
    save('COLOR_CHECKPOINT.json',{'stage':stage,'running':True,
        'pid':os.getpid(),'CPU_seconds':cpu(),**kwargs})

checkpoint('IMPORTS')
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix
data=np.load(base/'G0_INPUT.npz')
offset=data['indptr'];ids=data['indices'];pool=list(map(int,data['pool']))
spare=data['spare'];n=int(data['n']);p=len(pool);H=6
assert n==10070 and p==130 and len(ids)==308770
assert np.all(spare==1) and all(offset[u+1]-offset[u]==30 for u in pool)
adj=[ids[offset[v]:offset[v+1]].tolist() for v in range(n)]
pool_index={u:j for j,u in enumerate(pool)}
repo=next(q for q in base.parents if (q/'formal').is_dir() and (q/'research-wiki').is_dir())
old_binding=json.loads((base.parent/'mixed_copy_cycle_sigma_31/INTEG_BLOCK_LOCAL_BINDING_RESULT.json').read_text())
old_groups={int(b):int(y) for y,bs in old_binding['groups'].items() for b in bs}
absolute=set(json.loads((base/'PARAMETERS.json').read_text())['B_absolute_labels'])
reach=[set() for _ in pool]
masks=[];example={}
for v in range(n):
    eligible={pool_index[w] for w in adj[v] if w in pool_index}
    if v in pool_index:eligible.add(pool_index[v])
    for w in adj[v]:
        eligible.update(pool_index[z] for z in adj[w] if z in pool_index)
    mask=sum(1<<j for j in eligible)
    masks.append(mask);example.setdefault(mask,v)
    if v<8775 and v%585 in old_groups:
        group=old_groups[v%585]
        for j in eligible:reach[j].add(group)
    if v%2500==0:checkpoint('COMPLETE_TARGET_MASKS',targets=v+1)

reach_rows=[{'pin':u,'B_coordinate':u%585,'B_is_absolute':u%585 in absolute,
    'old_groups_reached':sorted(reach[j]),'group_count':len(reach[j])} for j,u in enumerate(pool)]
checks={'nonabsolute_B_120_count':sum(not r['B_is_absolute'] for r in reach_rows)==120,
    'absolute_B_10_count':sum(r['B_is_absolute'] for r in reach_rows)==10,
    'all_nonabsolute_B_reach_at_least5_old_groups':all(r['group_count']>=5 for r in reach_rows if not r['B_is_absolute']),
    'all_absolute_B_reach_one_old_group':all(r['group_count']==1 for r in reach_rows if r['B_is_absolute'])}
save('SPREAD_REACH_PREDICTION_RESULT.json',{'checks':checks,'all_match':all(checks.values()),
    'actual_rows':reach_rows,'scope':'same mask preparation, no second neighborhood traversal'})

# Minimal masks are enough because every superset inherits every color.
# A literal subset witness is saved for each of all10070 old targets.
unique=sorted(example,key=lambda m:(m.bit_count(),m))
retained=[];dominates={}
for k,mask in enumerate(unique):
    parent=None
    for j,small in enumerate(retained):
        if small&mask==small:
            parent=j;break
    if parent is None:
        parent=len(retained);retained.append(mask)
    dominates[mask]=parent
    if k%2000==0:checkpoint('SUBSET_REDUCTION',unique_processed=k+1,retained=len(retained))
with (base/'ALL_OLD_TARGET_MASK_WITNESSES.tsv').open('w') as out:
    out.write('target\tmask_decimal\tcardinality\tretained_edge\tsubset_verified\n')
    for v,mask in enumerate(masks):
        j=dominates[mask];assert retained[j]&mask==retained[j]
        out.write(f'{v}\t{mask}\t{mask.bit_count()}\t{j}\ttrue\n')
edge_lists=[[j for j in range(p) if mask>>j&1] for mask in retained]
save('COVER_HYPERGRAPH.json',{'n_old_targets':n,'pool':pool,'unique_masks':len(unique),
    'retained_masks':len(retained),'all_old_target_subset_witnesses':'ALL_OLD_TARGET_MASK_WITNESSES.tsv',
    'edges':[{'id':j,'example_target':example[mask],'mask_decimal':str(mask),
        'pin_indices':edge_lists[j]} for j,mask in enumerate(retained)],
    'minimum_mask_cardinality':min(map(int.bit_count,unique))})
minimum=min(map(int.bit_count,unique))
if minimum<H:
    result={'status':'U_ONLY_OWN_COVER_SUBMODEL_IMPOSSIBLE_MASK_SMALLER_THAN_SIX',
        'minimum_mask_cardinality':minimum,'example_target':example[unique[0]],
        'strict_scope':'six disjoint own-radius2 covers using this130 pool only',
        'joint_U_or_F_repairs_excluded':False,'integer_pins_saved':False,
        'CPU_seconds':cpu(),'solver_runs':0}
    save('COLOR_RESULT.json',result);save('COLOR_CHECKPOINT.json',{'running':False,**result})
    print(json.dumps(result));raise SystemExit(0)

N=H*p+1;z=N-1
cols=array.array('i');values=array.array('d');ptr=array.array('i',[0]);lo=[];hi=[]
def row(entries,lower,upper):
    for col,value in entries:
        cols.append(col);values.append(value)
    ptr.append(len(cols));lo.append(lower);hi.append(upper)

for edge in edge_lists:
    for h in range(H):row(((h*p+j,1.) for j in edge),1.,np.inf)
for j in range(p):row(((h*p+j,1.) for h in range(H)),1.,1.)
for h in range(H):row([(h*p+j,1.) for j in range(p)]+[(z,-1.)],-np.inf,0.)

# Canonical first occurrences of colors on one edge remove only helper
# relabelings. No unrelated degree-count sorting is imposed.
first=edge_lists[0]
row([(first[0],1.)],1.,1.)
for k,j in enumerate(first[1:],1):
    for h in range(1,H):
        row([(h*p+j,1.)]+[((h-1)*p+old,-1.) for old in first[:k]],-np.inf,0.)
matrix=csr_matrix((np.frombuffer(values,dtype=np.float64),
    np.frombuffer(cols,dtype=np.int32),np.frombuffer(ptr,dtype=np.int32)),shape=(len(lo),N)).tocsc()
model={'variables':N,'binary_color_variables':H*p,'max_load_variable':z,'rows':len(lo),
    'nonzeros':matrix.nnz,'old_targets':n,'unique_masks':len(unique),
    'retained_masks':len(retained),'minimum_mask_cardinality':minimum,
    'every_old_target_has_subset_witness':True,'all130_pins_exactly_one_color':True,
    'per_helper_limit':26,'objective':'minimize max helper pin load; any feasible point accepted',
    'objective_optimality_required':False,'time_limit_seconds':45,'total_CPU_budget':60,
    'worker_count':1,'preparation_CPU_seconds':cpu(),'old_group_reach_prediction_checks':checks}
save('COLOR_MODEL.json',model);checkpoint('COLOR_MILP_RUNNING',**model)
c=np.zeros(N);c[z]=1
upper=np.ones(N);upper[z]=26
res=milp(c=c,integrality=np.ones(N),bounds=Bounds(np.zeros(N),upper),
    constraints=LinearConstraint(matrix,np.array(lo),np.array(hi)),
    options={'threads':1,'time_limit':45.,'mip_rel_gap':1.,'disp':True})
result={'status_code':int(res.status),'message':str(res.message),'CPU_seconds':cpu(),
    'integer_pins_saved':False,'solver_runs':1,'strict_infeasibility_proof_claimed':False,
    'whole_parameter_or_general_extension_excluded':False,
    'scope':'this spread-hole base,130 freed-U-only six OWN full-cover sets',
    'mip_node_count':getattr(res,'mip_node_count',None),
    'mip_gap':getattr(res,'mip_gap',None),'objective_optimality_claimed':False}
if res.x is not None:
    x=np.rint(res.x);activity=matrix@x
    integral=bool(np.max(np.abs(res.x-x))<=1e-5)
    valid=integral and bool(np.all(activity>=np.array(lo)-1e-7) and np.all(activity<=np.array(hi)+1e-7))
    result['rounded_integer_model_valid']=valid
    if valid:
        pins=[[pool[j] for j in range(p) if x[h*p+j]>.5] for h in range(H)]
        assert sum(map(len,pins))==130 and max(map(len,pins))<=26
        all_targets=all(any(mask>>j&1 and x[h*p+j]>.5 for j in range(p))
            for mask in masks for h in range(H))
        assert all_targets
        save('PINS.json',{'status':'SIX_INTEGER_OWN_COVERS_PENDING_FULL_GRAPH_AND_FRESH_ACCEPTANCE',
            'pins':pins,'pin_counts':list(map(len,pins)),'total_pins':130,
            'new_helper_labels':list(range(n,n+H)),'helper_graph':'K6',
            'target':[31,3,10076,154530],'all10070_targets_each_own_cover':True,
            'every_helper_prefix_proof':'own cover of fixedG0 plus direct adjacency to prior helpers',
            'independent_acceptance':'PENDING','portfolio_increment':0})
        result['integer_pins_saved']=True
if result['integer_pins_saved']:result['status']='FEASIBLE_OWN_COVERS_PENDING_LITERAL_GRAPH_FRESH_ACCEPTANCE'
elif res.status==2:result['status']='NUMERICALLY_INFEASIBLE_THIS_U_ONLY_OWN_COVER_SUBMODEL'
else:result['status']='UNKNOWN_NO_INTEGER_COLORING_WITHIN_ONE_BUDGET'
save('COLOR_RESULT.json',result);save('COLOR_CHECKPOINT.json',{'running':False,**result})
print(json.dumps(result))

import collections
import json
from pathlib import Path
import resource
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'research/ddp/more_graphs_20261027/d13_D5_h9_transfer'
assert not (HERE/'RESULT.json').exists(), 'This fixed gate already completed.'
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
start=time.process_time()
bound=json.loads((SOURCE/'RESULT.json').read_text())
assert bound['simultaneous_pair_swap_is_core_automorphism'] is True
core_n=bound['core_n'];n=bound['source_n'];m=bound['source_m']
assert (core_n,n,m)==(50554,51417,324451)
classes=json.loads((SOURCE/'fold13_classes.json').read_text())['classes']
swap=list(range(core_n));seen=[False]*core_n
for group in classes:
    assert len(group) in (1,2)
    for v in group:
        assert 0<=v<core_n and not seen[v]
        seen[v]=True
    if len(group)==2:
        a,b=group;swap[a],swap[b]=b,a
assert all(seen) and all(swap[swap[v]]==v for v in range(core_n))
core_neighbors=[set() for _ in range(n-core_n)]
degree=[0]*n;edges=[]
with (SOURCE/'source51417.edges').open() as inp:
    assert tuple(map(int,next(inp).split()))==(n,m)
    for line in inp:
        u,v=map(int,line.split());edges.append((u,v));degree[u]+=1;degree[v]+=1
        if u<core_n<=v:core_neighbors[v-core_n].add(u)
        elif v<core_n<=u:core_neighbors[u-core_n].add(v)
assert len(edges)==m
groups=collections.defaultdict(list)
for e,pins in enumerate(core_neighbors,core_n):groups[tuple(sorted(pins))].append(e)
ordered=sorted(groups,key=lambda s:groups[s][0])
signature_records=[{'core_neighbors':list(s),'peripheral_vertices':groups[s]} for s in ordered]
(HERE/'PERIPHERAL_SIGNATURES.json').write_text(json.dumps(signature_records,indent=2)+'\n')
result={'source_n':n,'source_m':m,'core_n':core_n,'peripheral_n':n-core_n,
        'core_swap_recovered_from':'fold13_classes.json','core_pair_count':sum(len(g)==2 for g in classes),
        'core_aut_check_inherited':True,'source_reads':1,'core_edge_rechecks':0,
        'peripheral_signature_groups':len(groups),'unique_signature_vertices':sum(len(g)==1 for g in groups.values()),
        'duplicate_signature_groups':sum(len(g)>1 for g in groups.values()),
        'signature_group_size_histogram':dict(sorted(collections.Counter(map(len,groups.values())).items())),
        'signature_groups_compared':0,'full_edge_checks':0,'BFS_runs':0,'solver_calls':0,'new_graphs':0}
mismatch=None
for sig in ordered:
    transformed=tuple(sorted(swap[v] for v in sig))
    result['signature_groups_compared']+=1
    if len(groups[sig])!=len(groups.get(transformed,[])):
        mismatch={'source_peripheral_vertices':groups[sig], 'source_core_neighbors':list(sig),
                  'transformed_core_neighbors':list(transformed),
                  'source_multiplicity':len(groups[sig]),'target_multiplicity':len(groups.get(transformed,[])),
                  'matching_target_peripheral_vertices':groups.get(transformed,[])}
        break
if mismatch is not None:
    result.update(status='SPECIFIED_CORE_SWAP_HAS_NO_FULL_AUTOMORPHISM_EXTENSION',first_multiplicity_mismatch=mismatch)
elif any(len(g)>1 for g in groups.values()):
    result.update(status='SIGNATURE_NECESSITY_PASSES_DUPLICATE_GROUPS_UNRESOLVED',
                  duplicate_groups=[row for row in signature_records if len(row['peripheral_vertices'])>1])
else:
    permutation=swap+list(range(core_n,n))
    for sig,vertices in groups.items():
        permutation[vertices[0]]=groups[tuple(sorted(swap[v] for v in sig))][0]
    assert sorted(permutation)==list(range(n))
    edge_set=set(edges);bad=None
    for u,v in edges:
        a,b=sorted((permutation[u],permutation[v]));result['full_edge_checks']+=1
        if (a,b) not in edge_set:
            bad={'edge':[u,v],'image':[a,b]};break
    (HERE/'FULL_PERMUTATION.json').write_text(json.dumps(permutation)+'\n')
    if bad:result.update(status='UNIQUE_SIGNATURE_EXTENSION_FAILS_EDGE_CHECK',first_nonedge_image=bad)
    else:result.update(status='FULL_AUTOMORPHISM_VERIFIED',moved_vertices=sum(i!=v for i,v in enumerate(permutation)))

# Separate candidate rule authorized by root: core swapped, peripheral IDs fixed.
cache=json.loads((HERE.parent/'d13_D5_static_pool_calibration/RESULT.json').read_text())
old_sets=[tuple(row['neighbors']) for row in cache['sets']]
old_pool=set(old_sets);candidates=[]
for i,old in enumerate(old_sets):
    candidate=tuple(sorted(swap[v] if v<core_n else v for v in old))
    assert len(candidate)==len(set(candidate))==len(old)
    blocked=[{'vertex':v,'base_degree':degree[v]} for v in candidate if degree[v]>=13]
    candidates.append({'index':i,'source_added_vertex':51417+i,'original_S':list(old),
                       'candidate_S':list(candidate),'different_from_own_S':candidate!=old,
                       'not_in_original40_pool':candidate not in old_pool,
                       'size':len(candidate),'individual_capacity_legal':len(candidate)<=13 and not blocked,
                       'blocked_ports':blocked,'coverage_checked':False})
new_unique={tuple(row['candidate_S']) for row in candidates if row['not_in_original40_pool']}
legal_new={tuple(row['candidate_S']) for row in candidates if row['not_in_original40_pool'] and row['individual_capacity_legal']}
candidate_result={'rule':'swap core split labels; keep literal peripheral guard IDs fixed',
                  'is_asserted_full_automorphism':False,'input_sets':40,
                  'different_from_own_set':sum(row['different_from_own_S'] for row in candidates),
                  'outside_original_pool_rows':sum(row['not_in_original40_pool'] for row in candidates),
                  'unique_new_sets':len(new_unique),'individual_capacity_legal_rows':sum(row['individual_capacity_legal'] for row in candidates),
                  'unique_new_capacity_legal_sets':len(legal_new),'coverage_checked':False,'candidates':candidates}
(HERE/'CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json').write_text(json.dumps(candidate_result,indent=2)+'\n')
result['candidate_diagnostic']={k:v for k,v in candidate_result.items() if k!='candidates'}
result['CPU_seconds']=time.process_time()-start
result['pending']=[]
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps({k:v for k,v in result.items() if k not in ['first_multiplicity_mismatch','duplicate_groups']},indent=2)+'\n')
print(json.dumps(result,indent=2))

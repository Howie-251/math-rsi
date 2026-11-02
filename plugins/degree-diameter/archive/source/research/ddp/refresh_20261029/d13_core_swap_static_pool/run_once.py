import collections
import itertools
import json
from pathlib import Path
import resource
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
assert not (HERE/'RESULT.json').exists(), 'This fixed three-candidate pool is already terminal.'
resource.setrlimit(resource.RLIMIT_CPU,(5,6));started=time.process_time()
old=json.loads((HERE.parent/'d13_D5_static_pool_calibration/RESULT.json').read_text())
candidate=json.loads((HERE.parent/'d13_core_swap_extension_signature/CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json').read_text())
assert old['failed_sets']==old['incompatible_pairs']==old['port_overloads']==0
O=[row['neighbors'] for row in old['sets']]
ids=[0,8,17]
new=[]
for i in ids:
    row=next(row for row in candidate['candidates'] if row['index']==i)
    assert row['individual_capacity_legal'] and row['not_in_original40_pool']
    new.append(row['candidate_S'])
source=ROOT/'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/source51417.edges'
with source.open() as inp:
    n,m=map(int,next(inp).split());assert(n,m)==(51417,324451)
    G=[[] for _ in range(n)];edges=[]
    for line in inp:
        u,v=map(int,line.split());G[u].append(v);G[v].append(u);edges.append((u,v))
assert len(edges)==m
capacity=[13-len(neighbors) for neighbors in G]
assert min(capacity)>=0
core_n=50554;W=(n+63)//64;distance_rows=[];new_to_old=[];new_to_new=[]
with (HERE/'R3.u64.bin').open('wb') as out3,(HERE/'R4.u64.bin').open('wb') as out4:
    for i,S in zip(ids,new):
        assert len(S)<=13 and len(set(S))==len(S) and all(capacity[v]>=1 for v in S)
        d=[-1]*n;q=list(S)
        for v in S:d[v]=0
        head=0
        while head<len(q):
            u=q[head];head+=1
            if d[u]==4:continue
            nextd=d[u]+1
            for v in G[u]:
                if d[v]<0:d[v]=nextd;q.append(v)
        core_missing=[v for v in range(core_n) if d[v]<0]
        peripheral_missing=[v for v in range(core_n,n) if d[v]<0]
        # Construct packed masks by bytes, avoiding repeated large-int shifts.
        b3=bytearray(W*8);b4=bytearray(W*8)
        for v in q:
            b4[v//8]|=1<<(v%8)
            if d[v]<=3:b3[v//8]|=1<<(v%8)
        out3.write(b3);out4.write(b4)
        def set_distance(T):return min((d[v] if d[v]>=0 else 5) for v in T)
        olddist=[set_distance(T) for T in O];newdist=[set_distance(T) for T in new]
        new_to_old.append(olddist);new_to_new.append(newdist)
        distance_rows.append({'candidate_index':i,'S':S,'R3_size':sum(x>=0 and x<=3 for x in d),'R4_size':len(q),
                              'core_missing_count':len(core_missing),'core_first_missing':core_missing[0] if core_missing else None,
                              'peripheral_missing_count':len(peripheral_missing),'peripheral_first_missing':peripheral_missing[0] if peripheral_missing else None,
                              'core_missing_targets':core_missing,'peripheral_missing_targets':peripheral_missing,
                              'full_B0_R4_cover':not core_missing and not peripheral_missing,
                              'distance_to_old40_capped_at5':olddist,'distance_to_three_new_capped_at5':newdist})
for a in range(3):
    for b in range(3):assert new_to_new[a][b]==new_to_new[b][a]
(HERE/'CANDIDATE_COVERAGE.json').write_text(json.dumps({'source_n':n,'core_n':core_n,'row_indices':ids,'words_per_row':W,'rows':distance_rows},indent=2)+'\n')
valid=[i for i,row in enumerate(distance_rows) if row['full_B0_R4_cover']]
base_usage=collections.Counter(v for S in O for v in S)
assert all(u<=capacity[v] for v,u in base_usage.items())
tested=0;rejected=collections.Counter();chosen=None;level_counts={}
for total in range(40+len(valid),40,-1):
    level_tests=0
    for a_count in range(1,len(valid)+1):
        drops=40+a_count-total
        if drops<0 or drops>a_count-1:continue
        for A in itertools.combinations(valid,a_count):
            for D in itertools.combinations(range(40),drops):
                tested+=1;level_tests+=1;drop=set(D)
                if any(new_to_new[a][b]>3 for a,b in itertools.combinations(A,2)) or any(new_to_old[a][j]>3 for a in A for j in range(40) if j not in drop):
                    rejected['set_distance']+=1;continue
                delta=collections.Counter(v for a in A for v in new[a])
                for j in D:delta.subtract(O[j])
                if any(base_usage[v]+change>capacity[v] for v,change in delta.items()):
                    rejected['port_capacity']+=1;continue
                chosen={'total_added':total,'new_indices':[ids[a] for a in A],'new_local_indices':list(A),'dropped_old_indices':list(D)}
                break
            if chosen:break
        if chosen:break
    level_counts[total]=level_tests
    if chosen:break
result={'status':'EXACT_POOL_MAXIMUM40' if chosen is None else 'COMPLETE_NEW_GRAPH_NEEDS_PARENT_INDEPENDENT_ACCEPTANCE',
        'scope':'original40 sets plus exactly core-swap fixed-peripheral candidates0,8,17, each once',
        'source_n':n,'source_m':m,'source_reads':1,'multisource_R4_runs':3,'source_D5_allroot_BFS':0,'solver_calls':0,
        'fully_covering_new_indices':[ids[i] for i in valid],'tested_improving_combinations':tested,'combinations_by_total':level_counts,
        'rejection_counts':dict(rejected),'pool_maximum_added_vertices':40 if chosen is None else chosen['total_added'],
        'new_graphs':0,'pending':[]}
if chosen:
    D=set(chosen['dropped_old_indices']);A=chosen['new_local_indices']
    family=[{'kind':'old','index':i,'S':S} for i,S in enumerate(O) if i not in D]+[{'kind':'new','index':ids[a],'S':new[a]} for a in A]
    order=n+len(family);size=m+sum(len(row['S']) for row in family)
    for j,row in enumerate(family):row['new_vertex']=n+j
    hit={**chosen,'base_source':str(source.relative_to(ROOT)),'base_n':n,'base_m':m,'n':order,'m':size,'max_degree_bound':13,
         'diameter_bound':5,'all_B0_edges_retained':True,'retains_all_current51457_edges':False,'family':family}
    graphpath=HERE/f'graph_d13_D5_n{order}.edges'
    with graphpath.open('w') as out:
        out.write(f'{order} {size}\n')
        for u,v in edges:out.write(f'{u} {v}\n')
        for row in family:
            for v in row['S']:out.write(f'{v} {row["new_vertex"]}\n')
    (HERE/'HIT.json').write_text(json.dumps(hit,indent=2)+'\n')
    result.update(new_graphs=1,n=order,m=size,hit_parameters='HIT.json',graph_file=graphpath.name)
result['CPU_seconds']=time.process_time()-started
assert result['CPU_seconds']<5
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
for row in distance_rows:
    print(json.dumps({k:row[k] for k in ['candidate_index','R3_size','R4_size','core_missing_count','core_first_missing','peripheral_missing_count','peripheral_first_missing']}))

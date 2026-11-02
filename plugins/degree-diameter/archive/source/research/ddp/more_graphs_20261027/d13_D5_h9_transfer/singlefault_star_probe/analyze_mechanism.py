"""One targeted original-source distance batch; no construction or revalidation."""
from pathlib import Path
from collections import Counter,deque
import json,time,resource,struct

OUT=Path(__file__).resolve().parent
GROUP=OUT.parent
ROOT=OUT.parents[4]
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
load=lambda p:json.loads(p.read_text())
prediction=load(OUT/'MECHANISM_PREDICTION.json');assert prediction['frozen_before_targeted_analysis']
hit=load(OUT/'first_hit.json');assert hit['root_accepted'] and hit['source_n']==51417
v,d,g=51013,11352,50577
assert (hit['prototype'],hit['deleted_saturated_pin'],hit['guards'])==(v,d,[g])
prep=load(ROOT/hit['mandatory_R4_file']);missing=prep['missing']
assert len(missing)==3614 and sum(x<50554 for x in missing)==3535
adj=[]
source=GROUP/'source51417.adjlist.txt'
with source.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):continue
        row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
assert len(adj)==51417
N={r:set(adj[r]) for r in [v,d,g]}
M=set(hit['mandatory_pins'])
assert N[v]==M|{d} and len(M)==9
shared=N[d]&N[g]
saved_mask_row=prep['representatives'].index(g)
words=prep['mask_words_per_row']
maskfile=Path(str(ROOT/hit['mandatory_R4_file']).replace('.json','.masks.u64.bin'))
with maskfile.open('rb') as f:
    f.seek(saved_mask_row*words*8);raw=f.read(words*8)
savedmask=struct.unpack('<'+'Q'*words,raw)
savedcount=sum(z.bit_count() for z in savedmask)
assert savedcount==len(missing)

def distances(root,branches=False):
    dist=[-1]*len(adj);dist[root]=0;q=deque([root]);parent=[-1]*len(adj) if branches else None
    supports=[0]*len(adj) if branches else None
    bit={w:1<<i for i,w in enumerate(sorted(adj[root]))} if branches else None
    while q:
        u=q.popleft();nd=dist[u]+1
        for w in adj[u]:
            if dist[w]<0:
                dist[w]=nd;q.append(w)
                if branches:parent[w]=u;supports[w]=bit[w] if u==root else supports[u]
            elif branches and dist[w]==nd:
                supports[w]|=bit[w] if u==root else supports[u]
    return dist,parent,supports

dv,_,_=distances(v)
dd,_,_=distances(d)
dg,pg,sg=distances(g,True)
guard_neighbors=sorted(adj[g]);sharedbits=sum(1<<i for i,w in enumerate(guard_neighbors) if w in shared)
splits={'core':[x for x in missing if x<50554],'extras':[x for x in missing if x>=50554]}
profiles={}
for layer,targets in splits.items():
    profiles[layer]=dict(count=len(targets),
        prototype_distance_histogram=dict(sorted(Counter(dv[x] for x in targets).items())),
        deleted_distance_histogram=dict(sorted(Counter(dd[x] for x in targets).items())),
        guard_distance_histogram=dict(sorted(Counter(dg[x] for x in targets).items())),
        joint_distance_histogram={','.join(map(str,k)):c for k,c in sorted(Counter((dv[x],dd[x],dg[x]) for x in targets).items())},
        guard_minus_deleted_histogram=dict(sorted(Counter(dg[x]-dd[x] for x in targets).items())),
        shortest_guard_route_with_shared_firststep=sum(bool(sg[x]&sharedbits) for x in targets))
branch_rows=[]
for i,w in enumerate(guard_neighbors):
    branch_rows.append(dict(neighbor=w,neighbor_degree=len(adj[w]),shared_with_deleted=w in shared,
        missing_with_this_shortest_firststep=sum(bool(sg[x]>>i&1) for x in missing),
        missing_with_unique_shortest_firststep=sum(sg[x]==1<<i for x in missing),
        core_unique_shortest_firststep=sum(sg[x]==1<<i for x in splits['core']),
        extra_unique_shortest_firststep=sum(sg[x]==1<<i for x in splits['extras'])))
examples=[]
for layer,targets in splits.items():
    keys={}
    for x in targets:keys.setdefault((dv[x],dd[x],dg[x]),x)
    for distances_key,x in sorted(keys.items()):
        path=[x]
        while path[-1]!=g:path.append(pg[path[-1]])
        path.reverse()
        examples.append(dict(layer=layer,target=x,distances=list(distances_key),guard_shortest_path=path,
            guard_firststep=path[1],guard_firststep_shared_with_deleted=path[1] in shared,
            prototype_route_via_deleted_length=1+dd[x]))
result=dict(status='TARGETED_SUCCESS_MECHANISM_ANALYSIS_COMPLETE',source=str(source.relative_to(ROOT)),
    source_n=51417,prototype=v,deleted_pin=d,guard=g,prototype_layer='sourceextra',deleted_layer='sourcecore',guard_layer='sourceextra',
    degrees={str(r):len(adj[r]) for r in [v,d,g]},
    neighborhoods={str(r):sorted(N[r]) for r in [v,d,g]},
    neighborhood_layers={str(r):dict(core=sum(x<50554 for x in N[r]),extras=sum(x>=50554 for x in N[r])) for r in [v,d,g]},
    shared_deleted_guard_neighbors=sorted(shared),shared_count=len(shared),
    guard_neighbors_subset_deleted=N[g]<=N[d],deleted_neighbors_subset_guard=N[d]<=N[g],
    deleted_only_neighbors=sorted(N[d]-N[g]),guard_only_neighbors=sorted(N[g]-N[d]),
    prototype_guard_common_neighbors=sorted(N[v]&N[g]),
    mandatory_guard_common_neighbors=sorted(M&N[g]),
    pairwise_distances={f'{a},{b}':dist[b] for a,dist in [(v,dv),(d,dd),(g,dg)] for b in [v,d,g]},
    mandatory=sorted(M),missing_count=len(missing),profiles=profiles,
    saved_target_mask_guard_row=saved_mask_row,saved_target_mask_popcount=savedcount,
    all_missing_guard_distance_at_most4=all(dg[x]<=4 for x in missing),
    all_missing_prototype_short_routes_need_deleted_firststep=True,
    private_firststep_proof='NoMpinhasdistance<=4toanymissingtarget;sourceprototypeD<=5forcesallprototype->target routes<=5tostartwithdeletedpin.',
    all_missing_have_shared_shortest_guard_firststep=all(sg[x]&sharedbits for x in missing),
    guard_shortest_branch_contributions=branch_rows,route_examples=examples,
    hypothesis_neighborhood_containment_supported=N[g]<=N[d],
    targeted_BFS_roots=[v,d,g],targeted_BFS_root_count=3,one_targeted_batch=True,
    source_allsource_BFS=0,newgraph_BFS=0,new_candidates=0,raw_mapping_used=False,
    CPU_seconds=time.process_time()-start)
(OUT/'MECHANISM.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','degrees','shared_count','guard_neighbors_subset_deleted',
    'deleted_only_neighbors','guard_only_neighbors','pairwise_distances','profiles',
    'all_missing_have_shared_shortest_guard_firststep','CPU_seconds']}))

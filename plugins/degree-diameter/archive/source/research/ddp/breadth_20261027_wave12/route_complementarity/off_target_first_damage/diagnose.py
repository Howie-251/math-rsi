"""One damaged controller slot; read new distances and cached old route algebra."""
from pathlib import Path
from collections import Counter
import json
import time

P=Path(__file__).resolve().parent
BASE=P.parent
ROOT=P.parents[4]
started=time.process_time()
wordfile=BASE/'binary_best_analysis/word_images.json'
pairfile=BASE/'binary_best_analysis/controller_pair_routes.json'
words=json.loads(wordfile.read_text())['words']
pairs=json.loads(pairfile.read_text())['pairs']
old=json.loads((ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json').read_text())
newfile=BASE/'controlled_edge_change/matrix_shear_parameters.json'
new=json.loads(newfile.read_text());adj=old['controller_out']
cachefile=BASE/'controlled_edge_change/matrix_shear_distances.u8.bin'
dist=cachefile.read_bytes();N=1152;assert len(dist)==N*N
chosen=None;checked=0
for i in range(N):
    u,x=divmod(i,16)
    for j in range(i+1,N):
        if dist[i*N+j]<=4:continue
        checked+=1;v,y=divmod(j,16);pr=pairs[u*72+v]
        covering=[words[k] for k in pr['route_ids']
                  if (y^words[k]['linear_map'][x]) in words[k]['image']]
        if covering:
            chosen=dict(source_vertex=i,target_vertex=j,source_controller=u,source_fiber=x,
                        target_controller=v,target_fiber=y,
                        old_distance_from_complete_route_data=min(w['length'] for w in covering),
                        new_distance_from_root_cache=dist[i*N+j],
                        old_covering_route_words=[w['word'] for w in covering],
                        lexicographic_newbad_candidates_checked=checked)
            break
    if chosen:break
assert chosen and (chosen['source_vertex'],chosen['target_vertex'])==(0,5)
def act(c,x):
    z=0
    for j in range(4):
        if x>>j&1:z^=c[j]
    return z
edge={}
for e in new['edges']:
    edge[e['u'],e['v']]=(e['T_columns'],e['b'],e['c'])
    edge[e['v'],e['u']]=(e['Tinv_columns'],e['reverse_b'],e['reverse_c'])
u=chosen['source_controller'];v=chosen['target_controller'];x=chosen['source_fiber'];y=chosen['target_fiber']
routes=[];oldunion=set();newunion=set();changed=[]
for k in pairs[u*72+v]['route_ids']:
    w=words[k];at=u;path=[u];columns=[];m=list(range(16));offset=0
    for t in w['word']:
        nxt=adj[at][t];c,b,off=edge[at,nxt]
        columns=[act(c,z) for z in columns]+[b]
        m=[act(c,z) for z in m];offset=act(c,offset)^off
        at=nxt;path.append(at)
    assert at==v
    image={0}
    for z in columns:image|={a^z for a in list(image)}
    od=w['linear_map'][x];nd=m[x]^offset
    oldpoints={z^od for z in w['image']};newpoints={z^nd for z in image}
    oldunion|=oldpoints;newunion|=newpoints
    item=dict(word=w['word'],length=w['length'],controller_path=path,
        old=dict(rank=w['rank'],columns=w['columns'],linear_image=w['image'],
                 total_linear_map=w['linear_map'],drift_at_selected_input=od,
                 endpoint_set_at_selected_input=sorted(oldpoints),covers_selected_target=y in oldpoints),
        new=dict(rank=len(image).bit_length()-1,columns=columns,linear_image=sorted(image),
                 total_linear_map=m,offset=offset,drift_at_selected_input=nd,
                 endpoint_set_at_selected_input=sorted(newpoints),covers_selected_target=y in newpoints))
    routes.append(item)
    if w['image']!=sorted(image) or w['linear_map']!=m or offset:changed.append(item)
assert len(routes)==33 and oldunion==set(range(16)) and newunion==set(range(16))-{5}
assert all(r['old']['total_linear_map']==list(range(16)) and r['new']['total_linear_map']==list(range(16)) for r in routes)
result=dict(status='FIRST_NEW_DAMAGE_EXPLAINED_BY_SELF_ROUTE_COMPLEMENTARITY_LOSS',
    diagnosis_type='POSTHOC_SINGLE_SLOT_MECHANISM_NOT_NEW_SEARCH',selected_pair=chosen,
    controller_slot=[u,v],all_controller_route_count=len(routes),
    route_length_histogram=dict(Counter(r['length'] for r in routes)),
    old_rank_histogram=dict(Counter(r['old']['rank'] for r in routes)),
    new_rank_histogram=dict(Counter(r['new']['rank'] for r in routes)),
    old_union_at_selected_input=sorted(oldunion),new_union_at_selected_input=sorted(newunion),
    new_missing_at_selected_input=[5],all_closed_route_linear_maps_remain_identity=True,
    all_selected_input_drifts_remain_zero=True,changed_routes=changed,routes=routes,
    mechanism='0123 remains rank2 but rotates from{0,5,8,13}to{0,4,8,12}; only old route containing5 loses it, while4/12 are redundant.0213 separately dropsrank2to1 but its lost points are covered by other routes. No rank4 route existed in this self slot, and no drift changed.',
    source_inputs=dict(old_word_images=str(wordfile.relative_to(ROOT)),
                       old_pair_routes=str(pairfile.relative_to(ROOT)),
                       new_parameters=str(newfile.relative_to(ROOT)),
                       new_distance_cache=str(cachefile.relative_to(ROOT))),
    old_BFS_rerun=False,new_BFS_rerun=False,new_candidates=0,
    other_damaged_slots_analyzed=0,other_passers_analyzed=0,
    current_global_results_reused=dict(old_bad_unordered=12384,matrix_shear_bad_unordered=12800),
    attribution_scope='This concrete loss explains an off-target failure mechanism; no full migration accounting or attribution of all416net additional bad pairs.',
    CPU_seconds=time.process_time()-started)
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(selected_pair=chosen,old_union_size=len(oldunion),new_union_size=len(newunion),changed_words=[r['word'] for r in changed],CPU_seconds=result['CPU_seconds'])))

"""Cached bestID68 only: route-image algebra, no graph generation or BFS."""
from pathlib import Path
from collections import Counter
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(1,1))
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
started=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
data=json.loads(source.read_text());p=data['global_label_parameters']
assert p['passer_id']==68 and p['offsets']==[0,0,0,0]
adj=data['controller_out'];cols=p['matrix_columns'];bs=p['b_codes'];inv=data['inverse_labels']
def action(c,x):
    y=0
    for j in range(4):
        if x&(1<<j):y^=c[j]
    return y
maps=[[action(c,x) for x in range(16)] for c in cols]
for t in range(4):
    assert all(maps[inv[t]][maps[t][x]]==x for x in range(16))
    assert maps[inv[t]][bs[t]]==bs[inv[t]]

words=[]
def build(word,parent,last,map0,columns0,image):
    i=len(words);mask=sum(1<<x for x in image);rank=(len(image)).bit_length()-1
    assert 1<<rank==len(image)
    normals=[n for n in range(1,16) if all((n&x).bit_count()%2==0 for x in image)]
    words.append(dict(id=i,parent=parent,last_label=last,word=word,length=len(word),
                      linear_map=map0,columns=columns0,image=image,image_mask=mask,
                      rank=rank,nonzero_normal_vectors=normals))
    if len(word)<4:
        for t in range(4):
            image1=sorted({maps[t][x]^(l*bs[t]) for x in image for l in (0,1)})
            build(word+[t],i,t,[maps[t][x] for x in map0],
                  [maps[t][x] for x in columns0]+[bs[t]],image1)
build([],-1,-1,list(range(16)),[],[0])
assert len(words)==341
pairs=[];candidates=[];no_full=0;zero_bad=0;zero_missing=0
for u in range(72):
    ends=[u]*len(words);routes=[[] for _ in range(72)]
    for w in words:
        if w['parent']>=0:ends[w['id']]=adj[ends[w['parent']]][w['last_label']]
        routes[ends[w['id']]].append(w['id'])
    for v,ids in enumerate(routes):
        mask=0
        for i in ids:mask|=words[i]['image_mask']
        maxrank=max((words[i]['rank'] for i in ids),default=-1)
        missing=16-mask.bit_count();nofull=maxrank<4
        no_full+=nofull;zero_bad+=bool(missing);zero_missing+=missing
        rec=dict(source=u,target=v,route_ids=ids,route_count=len(ids),
                 rank_histogram=dict(Counter(words[i]['rank'] for i in ids)),
                 single_full_rank_route_present=not nofull,
                 zero_origin_offset0_union_mask=mask,zero_origin_offset0_missing=missing)
        pairs.append(rec)
        if missing:
            expanded=[{k:words[i][k] for k in ['id','word','length','linear_map','columns','image','image_mask','rank','nonzero_normal_vectors']} for i in ids]
            cert=None;priority=3
            if len(ids)==2 and all(words[i]['rank']==3 for i in ids) and words[ids[0]]['image_mask']!=words[ids[1]]['image_mask']:
                cert=dict(kind='TWO_NONPARALLEL_HYPERPLANES',maximum_union=12,
                          proof='Each affine hyperplane has8 points. Different normals are independent overF2, so any two translates intersect in exactly4. Union8+8-4=12.')
                priority=0
            elif sum(1<<words[i]['rank'] for i in ids)<16:
                cert=dict(kind='SUM_OF_ROUTE_CAPACITIES',maximum_union=sum(1<<words[i]['rank'] for i in ids))
                priority=1
            candidates.append(dict(priority=priority,**rec,routes=expanded,certificate=cert))
candidates.sort(key=lambda x:(x['priority'],x['source'],x['target']))
chosen=candidates[0] if candidates else None
prediction=('CONFIRMED_BY_TRANSLATION_ROBUST_LOCAL_CERTIFICATE' if chosen and chosen['certificate'] else
            'UNRESOLVED_NEEDS_INDEPENDENT_TRANSLATION_UPPER_BOUND')
summary=dict(status='CACHED_BEST_ROUTE_STRUCTURE_COMPLETE',prediction_id='P1_FIXED_BEST_DIRECTIONS_HAVE_TRANSLATION_ROBUST_LOCAL_GAP',
    prediction_result=prediction,input=str(source.relative_to(ROOT)),passer_id=68,
    controller_pairs=5184,walks_per_controller_root=341,walks_all_roots=24552,
    slots_without_single_rank4_route=no_full,zero_origin_offset0_bad_controller_slots=zero_bad,
    zero_origin_offset0_missing_ordered_fiber_targets=zero_missing,
    count_scopes='controller slots and72zero-origin input rows only; not the12384 allgraph unordered bad pairs',
    all_walks_including_backtracking=True,selected_slot=chosen,
    actual_D_reused=5,cached_allgraph_bad_unordered_pairs_reused=12384,
    other1023_passers_analyzed=False,offset_search_performed=False,
    graph_generated=False,BFS_performed=False,CPU_seconds_before_serialization=time.process_time()-started,
    workers=1)
(OUT/'word_images.json').write_text(json.dumps(dict(inverse_labels=inv,word_count=341,words=words),indent=2)+'\n')
(OUT/'controller_pair_routes.json').write_text(json.dumps(dict(count=5184,pairs=pairs),indent=2)+'\n')
(OUT/'candidate_slots.json').write_text(json.dumps(dict(candidates=candidates[:16]),indent=2)+'\n')
summary['CPU_seconds']=time.process_time()-started
(OUT/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['prediction_result','slots_without_single_rank4_route','zero_origin_offset0_bad_controller_slots','CPU_seconds']},ensure_ascii=False))
if chosen:print(json.dumps(chosen,ensure_ascii=False))

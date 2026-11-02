"""Assign cached word images to the other agent's fixed C19 controller.

No graph construction, image recomputation, or BFS is performed.
"""
from collections import Counter,defaultdict
from pathlib import Path
import json
import time

START=time.process_time()
OUT=Path(__file__).resolve().parent
OTHER=OUT.parent/'c19_controller_transfer'
records=json.loads((OUT/'WORD_IMAGES.json').read_text())['records']
lines=(OTHER/'input.txt').read_text().splitlines()
assert list(map(int,lines[0].split()))==[76,256,4]
trans=[list(map(int,line.split())) for line in lines[1:77]]
groups=defaultdict(list)
for r in records:
    g=0
    for s in r['word_types']:
        g=trans[g][s]
    groups[g].append(r)
slots=[]
all_missing={}
for g in range(76):
    rows=groups[g]
    cover=set().union(*(set(r['fibers']) for r in rows))
    missing=sorted(set(range(256))-cover)
    if missing:
        all_missing[g]=missing
        unique=defaultdict(list)
        for r in rows:
            unique[tuple(r['fibers'])].append(r['word'])
        slots.append({'target_controller':g,'target_base':g//19,'target_phase':g%19,
                      'source_controller':0,'source_fiber':0,
                      'route_count':len(rows),'rank_histogram':dict(Counter(r['rank'] for r in rows)),
                      'reduced2_words':[r['word'] for r in rows if r['length']==2 and r['is_reduced']],
                      'covered_count':len(cover),'missing_count':len(missing),'missing_fibers':missing,
                      'routes':[{k:r[k] for k in ['word','word_types','length','is_reduced','rank','image_size','image_basis','missing_direction_normals_basis']} for r in rows],
                      'distinct_image_rank_histogram':dict(Counter(next(r['rank'] for r in rows if r['word']==words[0]) for words in unique.values())),
                      'distinct_image_groups':[{'words':words,'image_size':len(image),'image_fibers':list(image)} for image,words in unique.items()]})
other=json.loads((OTHER/'RESULT.json').read_text())
native_missing=other['missing_by_controller']
if isinstance(native_missing,dict):
    native_missing={int(k):v for k,v in native_missing.items() if v}
else:
    native_missing={r['controller']:r['missing_fiber_ids'] for r in native_missing if r['missing_count']}
assert native_missing==all_missing
assert sum(map(len,all_missing.values()))==963

slot=next(s for s in slots if s['target_controller']==61)
hyper=[set(g['image_fibers']) for g in slot['distinct_image_groups'] if g['image_size']==64]
assert len(hyper)==4
core=set.intersection(*hyper)
union=set.union(*hyper)
assert len(core)==16 and len(union)==208
assert union==set(range(256))-set(slot['missing_fibers'])
contained_small=all(set(r['fibers'])<=union for r in groups[61] if r['rank']<3)
assert contained_small
slot['pencil_certificate']={'distinct_hyperplanes':4,'hyperplane_size':64,
                            'common_core_size':16,'common_core_fibers':sorted(core),
                            'union_size':208,'all_lower_rank_routes_contained':True,
                            'formula':'16+4*(64-16)=208; PG(1,4) has5 directions, so four members of this pencil leave48 points'}
selfslot=next(s for s in slots if s['target_controller']==0)
result={'status':'COMPLETE_CACHED_WORD_ENDPOINT_CLASSIFICATION_MATCHES_NATIVE_FIRST_ROOT',
        'controller_input':str(OTHER/'input.txt'),'producer_result':str(OTHER/'RESULT.json'),
        'word_image_cache':str(OUT/'WORD_IMAGES.json'),'words_including_backtracks':341,
        'source_controller':0,'source_fiber':0,'missing_slots':len(slots),'total_missing_fibers':963,
        'all_missing_fibers_match_other_agent':True,'slots':slots,
        'unique_rank3_route_slots':[{'controller':s['target_controller'],'word':s['routes'][0]['word'],
                                   'normal':s['routes'][0]['missing_direction_normals_basis'],'covered':64,'missing':192}
                                  for s in slots if s['route_count']==1 and s['routes'][0]['rank']==3],
        'unique_route_offset_scope':'For these fixed controller slots and fixed linear line-relation parts, any choice of affine offsets leaves the unique <=4 route image cardinality64, so D4 remains impossible; no offset search needed.',
        'self_slot_summary':{'route_count':selfslot['route_count'],'rank_histogram':selfslot['rank_histogram'],
                             'covered':selfslot['covered_count'],'missing':selfslot['missing_count']},
        'new_graphs':0,'graph_BFS':0,'word_image_recomputations':0,'controller_search':False,
        'CPU_seconds':time.process_time()-START,'pending':[]}
(OUT/'C19_SLOT_ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='slots'},indent=2))

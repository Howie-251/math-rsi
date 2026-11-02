"""Independent attack of one actual bestID68 slot,0->10, only.

Re-enumerate its controller walks, simulate binary branches directly, then use
the independent coset DP. No other slot, candidate, offset model, or BFS.
"""
from pathlib import Path
from itertools import product
import json
import time
from translation_cover import maximum_translated_union, translation_cosets

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
PARAMS=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
SCOUT=HERE.parent/'binary_best_analysis/RESULT.json'


def run():
    started=time.process_time()
    params=json.loads(PARAMS.read_text())
    expected=json.loads(SCOUT.read_text())['selected_slot']
    assert expected['source']==0 and expected['target']==10
    global_params=params['global_label_parameters']
    assert global_params['passer_id']==68
    maps=global_params['matrix_columns']
    vectors=global_params['b_codes']
    out=params['controller_out']
    routes=[]
    visits=0
    def walk(u,word,path):
        nonlocal visits
        visits+=1
        if u==10:
            routes.append((tuple(word),tuple(path)))
        if len(word)==4:
            return
        for label,v in enumerate(out[u]):
            walk(v,word+[label],path+[v])
    walk(0,[],[0])
    assert visits==341
    assert sorted(w for w,p in routes)==[(0,0,2,0),(3,2,2)]
    def apply(columns,x):
        y=0
        for i,c in enumerate(columns):
            if x>>i&1:
                y ^= c
        return y
    def endpoint(x,word,branch):
        for t,choice in zip(word,branch):
            x=apply(maps[t],x) ^ (vectors[t] if choice else 0)
        return x
    route_data=[]
    for word,path in routes:
        columns=[]
        for j in range(len(word)):
            branch=[0]*len(word);branch[j]=1
            columns.append(endpoint(0,word,branch))
        image=sorted({endpoint(0,word,branch) for branch in product([0,1],repeat=len(word))})
        normals=[n for n in range(1,16) if all((n&v).bit_count()%2==0 for v in image)]
        source_route=next(r for r in expected['routes'] if tuple(r['word'])==word)
        assert columns==source_route['columns'] and image==source_route['image']
        assert len(image)==8 and len(normals)==1
        route_data.append(dict(word=word,controller_path=path,columns=columns,image=image,normal=normals[0]))
    assert [r['normal'] for r in route_data]==[6,9]
    bound=maximum_translated_union([r['image'] for r in route_data],2,4)
    assert bound['exact_max_union']==12
    intersection_sizes=[];union_sizes=[]
    for a,sa in translation_cosets(route_data[0]['image'],2,4):
        for b,sb in translation_cosets(route_data[1]['image'],2,4):
            intersection_sizes.append((a&b).bit_count())
            union_sizes.append((a|b).bit_count())
    assert intersection_sizes==[4]*4 and union_sizes==[12]*4
    fibers=[]
    for x in range(16):
        images=[]
        for route in route_data:
            word=route['word']
            reachable={endpoint(x,word,branch) for branch in product([0,1],repeat=len(word))}
            shift=endpoint(x,word,[0]*len(word))
            assert reachable=={v^shift for v in route['image']}
            images.append(reachable)
        covered=images[0]|images[1]
        assert len(images[0]&images[1])==4 and len(covered)==12
        fibers.append(dict(source_fiber_state=x,offset0_union_size=12,
                           offset0_missing_states=sorted(set(range(16))-covered),
                           independent_translate_upper=12,all_offset_missing_at_least=4))
    result=dict(status='ACTUAL_BEST68_SLOT0_TO10_INDEPENDENT_TRANSLATION_BOUND12_CONFIRMED',
                candidate_id=68,source_base=0,target_base=10,
                source_parameters=str(PARAMS.relative_to(ROOT)),
                source_scout_result=str(SCOUT.relative_to(ROOT)),
                controller_walk_length_limit=4,controller_walks_from_base0_checked=341,
                controller_route_count=2,all_actual_routes=route_data,
                independently_recomputed_images_match_source_scout=True,
                exact_independent_translation_bound=bound,
                all_four_distinct_coset_pair_intersections=intersection_sizes,
                all_four_distinct_coset_pair_union_sizes=union_sizes,
                all16_source_fiber_states=fibers,
                proof='Two distinct nonzero F2 normals6,9 are independent. Every pair of affine hyperplanes has8+8-4=12 union, for every sourcex and even independently arbitrary route translations.',
                conclusion='With this fixed72 controller and fixedbest68 maps/vectors,no inverse-consistent offsets,including edge-local offsets,can achieveD4. Linear maps or branchvectors or controller routes must change.',
                conditional_unordered_bad_pairs_between_basefibers0_and10_at_least=64,
                conditional_count_type='Derived64=16*4 between these two fibers,not a full-graphBFS measurement.',
                actual_slots_analyzed=1,other1023_candidates_analyzed=0,
                global_or_edge_local_offset_searches=0,graph_BFS_count=0,
                new_graphs=0,new_lower_bounds=0,CPU_seconds=time.process_time()-started)
    (HERE/'ACTUAL_SLOT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','controller_route_count','conditional_unordered_bad_pairs_between_basefibers0_and10_at_least','CPU_seconds']}))
    return result


if __name__=='__main__':
    run()

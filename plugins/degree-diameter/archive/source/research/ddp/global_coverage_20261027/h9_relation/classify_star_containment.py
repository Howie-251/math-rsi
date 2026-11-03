"""One broad full-star certificate classification; no distances or optimization."""
from pathlib import Path
from collections import Counter
import json,time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
started=time.process_time();K=41356
prediction=json.loads((OUT/'P_STAR_PREDICTION.json').read_text())
assert prediction['frozen_before_star_containment_classification']
raw=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
core=[]
with raw.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):continue
        vals=list(map(int,line.split()));u=vals[0]
        if u>=K:break
        assert u==len(core);core.append({v for v in vals[1:] if v<K})
assert len(core)==K and all(core)
extras=json.loads((OUT/'current_extra_signatures.json').read_text())['records']
assert len(extras)==986
records=[];exact=[];strict=[];none=[];multi=[];with_any_strict=[]
candidate_sizes=[]
for old in extras:
    i=old['vertex'];Ai=set(old['N_core']);candidates=set()
    for a in Ai:candidates.update(core[a])
    candidate_sizes.append(len(candidates))
    parents=sorted(v for v in candidates if len(core[v])<=len(Ai) and core[v]<=Ai)
    equal=[v for v in parents if core[v]==Ai]
    proper=[v for v in parents if core[v]<Ai]
    assert bool(equal)==old['copy_like']
    category='exact-neighborhood' if equal else 'strict-superset-star-containing' if parents else 'non-star'
    rec=dict(vertex=i,A_i=sorted(Ai),candidate_parent_pool_size=len(candidates),
             all_star_parents=parents,exact_star_parents=equal,strict_star_parents=proper,
             prototype_multiplicity=len(parents),category=category)
    records.append(rec)
    if equal:exact.append(i)
    elif parents:strict.append(i)
    else:none.append(i)
    if proper:with_any_strict.append(i)
    if len(parents)>1:multi.append(i)
assert len(exact)==176 and len(exact)+len(strict)+len(none)==986
star=len(exact)+len(strict)
reps={k:next((r for r in records if r['category']==k),None)
      for k in ['exact-neighborhood','strict-superset-star-containing','non-star']}
result=dict(status='COMPLETE_FULL_STAR_CONTAINMENT_CLASSIFICATION',prediction_id='P_star',
    prediction_frozen_file='P_STAR_PREDICTION.json',prediction_outcome='CONFIRMED' if len(none)>=643 else 'FALSIFIED',
    common_core_n=K,current_extras=986,
    containment_direction='N_K(v) subseteqA_i; A_i=N_current(extra_i) intersectK',
    star_containing_count=star,exact_neighborhood_count=len(exact),
    strict_superset_only_count=len(strict),non_star_count=len(none),
    any_strict_parent_count_including_possible_exact_categories=len(with_any_strict),
    star_prototype_multiplicity_histogram=dict(Counter(r['prototype_multiplicity'] for r in records)),
    multiple_prototype_extra_ids=multi,max_candidate_parent_pool=max(candidate_sizes),
    candidate_pool_formula='Union_{a inA_i}N_K(a),thenactualsubsettest; max144fromDelta12',
    exact_extra_ids=exact,strict_superset_extra_ids=strict,non_star_extra_ids=none,
    representatives=reps,records=records,
    source_core_adjacency=str(raw.relative_to(ROOT)),
    source_extra_neighbor_sets='current_extra_signatures.json',
    external_bare_star_packing_bound=343,external_bound_rechecked=False,
    consistent_with_external_packing_bound=star<=343,
    macro_interpretation='Star-containing extras already admit ordinary-twin spanning routes onthecore; extraanchors/new-newedges cannotremove thatcertificate. Non-star extras require another global attachment argument, not necessarilypencilgeometry.',
    geometric_H3copy_or_pencil_types_assigned=False,
    distances_computed=False,BFS_performed=False,optimization_performed=False,
    new_candidates_generated=0,embedding_search_performed=False,
    CPU_seconds=time.process_time()-started,pending=[],next_automatic_action='NONE')
(OUT/'star_containment.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['prediction_outcome','star_containing_count','exact_neighborhood_count','strict_superset_only_count','non_star_count','star_prototype_multiplicity_histogram','max_candidate_parent_pool','CPU_seconds']},indent=2))
print('representatives',json.dumps(reps,ensure_ascii=False))

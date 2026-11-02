#!/usr/bin/env python3
"""Select existing pilot certificates and bind only small input/label tables.

No route/rank/coset recomputation, graph access, BFS or Lean execution.
"""
import time
START=time.process_time()
from pathlib import Path
import csv, json
from collections import Counter

HERE=Path(__file__).resolve().parent
CASE=HERE.parent
GATE=CASE.parent
ROOT=next(p for p in GATE.parents if (p/'formal').is_dir() and (p/'research').is_dir())
AFFINE=ROOT/'research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json'

def read(p):return json.loads(p.read_text())
def ref(p):return str(p.relative_to(ROOT))
def table(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))

def main():
    groups=read(GATE/'GLOBAL_COSET4_GROUPS.json')
    pairdata=read(GATE/'GLOBAL_COSET4_PAIR_CERTIFICATES.json')
    words=read(GATE/'GLOBAL_COSET4_WORDS781.json')
    oldwords=read(GATE/'NEW_ROUTE4_WORDS625.json')
    types=read(GATE/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json')
    old=read(AFFINE)
    params=read(CASE/'PARAMETERS.json')
    used={p['group_index'] for p in pairdata['pairs'] if p['kind']=='coset'}
    complete=[g for g in groups if g['group_index'] in used and g['complete']]
    selected=min(complete,key=lambda g:(-len(g['column_certificates']),g['group_index']))
    selected_pair=min(selected['controller_pairs'])
    assert selected['group_index']==0 and len(selected['column_certificates'])==25
    assert selected_pair==[0,0]
    assert selected['actual_offset_coset_union_size']==81
    assert set(selected['coset_vector_route_noise_witnesses'])==set(map(str,range(81)))
    offset=pairdata['fullrank_word_global_index_offset']
    rank4=[(i,w) for i,w in enumerate(words) if w.get('rank')==4]
    rank_index,rank_word=min(rank4,key=lambda pair:pair[0])
    assert rank_index==182 and rank_index-offset==26
    assert {k:v for k,v in rank_word.items() if k!='word_index'}==oldwords[rank_index-offset]
    endpoint=0;trace=[endpoint]
    for typ in rank_word['word']:
        endpoint=types['transition'][endpoint][typ];trace.append(endpoint)
    row0=sorted((p for p in pairdata['pairs'] if p['a']==0),key=lambda p:p['b'])
    assert [p['b'] for p in row0]==list(range(192))
    row0coset=[p for p in row0 if p['kind']=='coset']
    row0full=[p for p in row0 if p['kind']=='fullrank']
    assert len(row0coset)==19 and len(row0full)==173
    assert len({p['group_index'] for p in row0coset})==19

    # Equality binding to the recovered 960 literal arcs; no arithmetic/rank check.
    literal=types['types'];transition=types['transition']
    assert [t['type'] for t in literal]==list(range(5))
    assert len(transition)==192 and all(len(row)==5 for row in transition)
    def key(obj):return json.dumps([obj['B'],obj['v'],obj['c']],separators=(',',':'))
    lookup={key(t):t['type'] for t in literal}
    assert len(lookup)==5 and len(old['arcs'])==960
    seen=set()
    for arc in old['arcs']:
        typ=lookup[key(arc)];slot=(arc['from'],typ)
        assert slot not in seen and transition[arc['from']][typ]==arc['to']
        seen.add(slot)
    assert len(seen)==960

    # Only labels and N-size metadata are compared. The full physical-N claim
    # remains the existing fresh result; this script does not reread graph rows.
    prodpath=CASE/'ALL837_ROLE_BINDINGS.tsv'
    freshpath=CASE/'independent_acceptance/ALL837_ACTUAL_ROLE_BINDINGS.tsv'
    prod=table(prodpath);fresh=table(freshpath)
    assert len(prod)==len(fresh)==837
    labels=[]
    controllers=params['selected_controller_labels'];offsets=params['ordered_offsets']
    assert len(controllers)==31 and len(offsets)==27
    for j,(p,f) in enumerate(zip(prod,fresh)):
        i,q=divmod(j,27);a=controllers[i];local=offsets[q]
        center=81*a+local;new=15552+j
        assert [int(p[k]) for k in ['j','controller_index','controller','local_offset','source_center_label','new_label']]==[j,i,a,local,center,new]
        assert [int(f[k]) for k in ['j','controller','offset','old_center_label','new_label']]==[j,a,local,center,new]
        degree=int(p['literal_source_degree'])
        assert degree==int(f['actual_simple_N_size'])
        assert f['full_N_equal']=='true' and f['old_center_excluded']=='true'
        labels.append(dict(j=j,controller_index=i,controller=a,local_offset=local,
                           source_center_label=center,new_label=new,literal_simple_N_size=degree))
    assert [r['source_center_label'] for r in labels]==params['source_center_labels']
    assert Counter(r['literal_simple_N_size'] for r in labels)=={14:36,15:801}

    selection=dict(status='PILOT_DATA_SELECTED_EXISTING_CERTIFICATES_NOT_KERNEL_PROOF',
        selection_rule='Largest used complete group by column_certificates count; tie smallest group_index; lexicographically first controller pair.',
        selected_group_index=selected['group_index'],selected_controller_pair=selected_pair,
        selected_group_column_certificates=25,selected_group_cover_vectors=81,
        selected_group=selected,
        selected_group_word_records=[words[i] for i in selected['endpoint_word_indices']],
        selected_group_reference_word=words[selected['reference_word_index']],
        selected_fullrank_witness=dict(global_word_index=rank_index,
            inherited_length4_word_index=rank_index-offset,from_controller=0,
            to_controller=endpoint,actual_controller_trace=trace,word_record=rank_word),
        word_type_order=types['type_order'],literal_five_types=literal,
        actual_controller_transition=transition,
        row0_controller_order=192,row0_coset_pair_count=19,row0_fullrank_pair_count=173,
        row0_nineteen_group_ids=[p['group_index'] for p in row0coset],
        row0_coset_pairs=row0coset,row0_fullrank_pairs=row0full,
        row0_distinct_fullrank_word_indices=sorted({p['word_index'] for p in row0full}),
        ordered_837_role_label_binding=labels,
        sources=dict(groups=ref(GATE/'GLOBAL_COSET4_GROUPS.json'),
            pairs=ref(GATE/'GLOBAL_COSET4_PAIR_CERTIFICATES.json'),
            words=ref(GATE/'GLOBAL_COSET4_WORDS781.json'),
            inherited_rank4_words=ref(GATE/'NEW_ROUTE4_WORDS625.json'),
            type_table=ref(GATE/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json'),
            recovered_affine_arcs=ref(AFFINE),producer_roles=ref(prodpath),
            fresh_roles=ref(freshpath),fresh_result=ref(CASE/'independent_acceptance/RESULT.json')),
        scope='Existing coefficients and cover witnesses copied, not recomputed. No source or clone FinalClaim is proved by this preparation.')
    out=HERE/'PILOT_DATA_SELECTION.json'
    out.write_text(json.dumps(selection,ensure_ascii=False,indent=2)+'\n')
    result=dict(status='PASS_SMALL_LITERAL_INPUT_AND_ORDERED_ROLE_LABEL_BINDING_PILOT_DATA_READY',
        selected_group_index=selected['group_index'],selected_controller_pair=selected_pair,
        selected_group_column_certificates=25,selected_group_cover_witnesses=81,
        selected_fullrank_global_word_index=rank_index,
        selected_fullrank_original_length4_word_index=rank_index-offset,
        selected_fullrank_word=rank_word['word'],selected_fullrank_from=0,selected_fullrank_to=endpoint,
        row0_coset_groups=19,row0_fullrank_pairs=173,
        literal_global_types_bound=5,literal_controller_type_arcs_bound=960,
        ordered_role_labels_bound=837,center_degree_histogram={14:36,15:801},
        source_vertex_count=15552,clone_vertex_count=16389,source_reproduction_not_new_graph=True,
        neighborhood_equality='Inherited actual fresh full-N binding; only ordered labels and N-size metadata compared here.',
        copied_cover_certificates_recomputed=False,field_or_atomic_rank_tests=0,
        complete_graph_reads=0,BFS_runs=0,Lean_compilations=0,solver_runs=0,
        queries=0,paid_reviews=0,old_PASS_or_root_Wiki_files_modified=False,
        code_preparation_CPU_seconds=time.process_time()-START,
        CPU_measurement_boundary='Single preparation process including imports, small-cache parsing, selections, equality binding and selection JSON write.',
        selection_file='PILOT_DATA_SELECTION.json',selection_bytes=out.stat().st_size,
        formal_claim_completed=False)
    (HERE/'PILOT_BINDING_PREPARATION_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()

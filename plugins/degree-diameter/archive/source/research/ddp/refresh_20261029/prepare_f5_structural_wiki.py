"""Prepare additive existing-row notes from saved F5 structural results.

No Wiki mutation, experiment, graph, BFS, path enumeration, solver, compiler,
external review or hash is performed by this preparer.
"""
from pathlib import Path
import copy
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
import capture_filter

ledger=json.loads((ROOT/'research-wiki/DDP_METHOD_LEDGER.json').read_text())
assert ledger['record_count']==368
ids={
    'full':'ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029',
    'source':'ddp-wave4-mizuno-d3-source',
    'noise':'ddp-f5-fixed3750-restricted-noise-d10d4-two100-families-20261029'}
rows={key:copy.deepcopy(next(r['source_record'] for r in ledger['rows'] if r['id']==rid))
      for key,rid in ids.items()}
edge=HERE/'f5_d20_edge_criticality_20261029'
quotient=HERE/'f5_fiber_quotient_transfer'
cycle=HERE/'f5_d10_closed_route_diagnosis'
e=json.loads((edge/'RESULT.json').read_text())
q=json.loads((quotient/'RESULT.json').read_text())
qw=json.loads((quotient/'QUOTIENT_AND_COVER_WITNESS.json').read_text())
c=json.loads((cycle/'CYCLE_RESULT.json').read_text())
assert e['covered_darts']==120 and e['undirected_edges']==37500
assert qw['h']==[0,3,1] and qw['ordinary_cover_D3_sheet_bound']==5
assert c['all_vertices_require_opposite_external_gap_shapes']

def rel(p):return str(p.relative_to(ROOT))
def paths(folder,names):
    result=[rel(folder/name) for name in names]
    assert all((ROOT/p).exists() for p in result)
    return result
def add(key,variant,evidence):
    row=rows[key]
    row['matched_existing_id']=ids[key]
    row['variants']=[v for v in row.get('variants',[]) if v.get('label')!=variant['label']]+[variant]
    row['report_paths']=list(dict.fromkeys(row.get('report_paths',[])+evidence))

ep=paths(edge,['PREDICTION_AND_SCOPE.md','RESULT.json','EDGE_CRITICALITY.md',
              'CONTROLLER_CERTIFICATE.json','PENCIL_REDUNDANCY.json'])
add('full',dict(label='all37500_edges_D3critical_under_pure_deletion_20261029',
    status=e['status'],source_n=3750,source_m=37500,target_degree_controls=[19,18],target_D=3,
    prediction='SUPPORTED',
    exact_scope='Keep all3750 vertices of this fixed20regular graph and delete any nonempty subset of existing edges; no added edge or rewiring.',
    oriented_controller_darts=120,covered_darts=120,unique_distance3_controller_pairs=258,
    invertible_noise_word_classes=36,all37500_undirected_edges_critical=True,
    proof_mechanism='Unique length3 control path and bijective noise3tuple endpoint map give a distant unique<=3path through every specified lifted edge.',
    explicit_witness=e['explicit_witness'],
    source_BFS_runs=0,edge_deletion_graphs_generated=0,new_solver_calls=0,
    producer_controller_and_rank_CPU_seconds=e['single_worker_CPU_controller_and_rank'],
    producer_pencil_summary_CPU_seconds=e['single_worker_CPU_pencil_summary'],
    formalized_in_Lean=False,new_Lean_graph_instances=0,
    not_excluded=e['scope_not_excluded'],evidence_paths=ep),ep)
rows['full'].setdefault('other_metrics',{})['all_edges_critical_under_pure_deletion']=True
rows['full']['other_metrics']['edge_criticality_Lean_proved']=False

qp=paths(quotient,['PREDICTION.md','READ_SCOPE.md','REPORT.md','RESULT.json',
    'TRANSLATION_SYSTEM.json','QUOTIENT_AND_COVER_WITNESS.json',
    'check_local.py','quotient_route_witness.py','TERMINAL.json'])
add('source',dict(label='fixed_F5_translation_quotient750_and_ordinary_cover_ceiling_20261029',
    status=qw['status'],prediction_no_compatible_translation='REFUTED',
    translation_equations=120,translation_variables=90,translation_rank=89,
    translation_nullity=1,common_h=[0,3,1],
    relation_compatibility='h_b-T_p h_a lies in the target noise line; not necessarily T_p h_a=h_b.',
    formula_quotient=dict(n=750,degree=20,diameter_exact=3,
        actual_exported_edge_list=False,diameter_proof='source path projection plus Moore bound401',
        ordinary_source_cover_sheets=5),
    quotient_is_not_new_lower_bound=True,
    cached_controller_word=dict(root=0,target=3,vertices=[0,2,1,3],ports=[2,0,2],
        unique_length3_path=True,no_shorter_path=True,projected_noise_rank=2,
        exact_quotient_walks_to_each_target=5),
    ordinary_cover_D3_sheet_bound=5,
    cover_scope='Only ordinary covers of this exact750-point quotient; not other bases, altered relations, D>=4 or a complete automorphism classification.',
    other_fixed_controls=dict(e0_linear_quotient_degree=60,
        scalar_order2=dict(n=1890,maxdegree=20,D=3),
        scalar_order4=dict(n=960,maxdegree=20,D=3)),
    whole_graphs_generated=0,new_BFS_runs=0,new_path_enumerations=0,
    fixed_local_CPU_seconds=q['CPU_seconds'],
    cached_witness_CPU_seconds=qw['CPU_seconds'],
    total_diagnostic_CPU_seconds=q['CPU_seconds']+qw['CPU_seconds'],
    new_validated_record_instances=0,new_Lean_graph_instances=0,evidence_paths=qp),qp)

cp=paths(cycle,['PREDICTION.md','INITIAL_ANALYSIS_RESULT.json','analyze_initial.py',
    'SECOND_PREDICTION.md','RESULT.json','analyze.py','LOCAL_SHAPE_CASES.json',
    'ALL_TRIANGLE_LOCAL_CASES.json','COMPLEMENT_RESULT.json','COMPLEMENT_SHAPES.json',
    'triangle_complement.py','CYCLE_PREDICTION.md','CYCLE_RESULT.json','cycle_gate.py',
    'PROOF_PACKAGE.md']+[f'CYCLE_ROOT_{r}.json' for r in [0,20,28,22,9]])
add('noise',dict(label='edgewise_independent_tri3_ext2_fixed_matrices_oddC5_obstruction_20261029',
    status='EXACT_ALGEBRA_SUPPORTED_PENDING_TARGETED_REVIEW',review_status='PENDING',
    review_disposition=None,
    object_level='finite_exact_algebra_over_fixed_rules_not_generated_graph_batch',
    source_controller_vertices=30,fiber_size=125,hypothetical_graph_n=3750,
    hypothetical_graph_degree=10,target_D=4,
    parameter_domain='One independent3-subset per30 triangle edges and one independent2-subset per30 external edges of F5, reverse set negated, fixedT and directions, independent of x.',
    literal_parameter_settings='10^60',actual_full_settings_enumerated=0,
    actual_candidate_graphs_generated=0,new_BFS_runs=0,new_solver_calls=0,
    external_odd_cycle=[0,20,28,22,9],
    each_root_closed_word_counts={'0':1,'1':0,'2':4,'3':2,'4':28},
    external_shapes_per_root=256,triangle_set_triples_per_root=1000,
    all_source_holonomy_image_sizes=[5,25,25,25,5],
    relaxed_shape_pass_counts=[16,16,4,4,6],
    necessary_root_external_gap_pairs=[[1,2],[2,1]],
    prediction='SUPPORTED_BY_SAVED_FINITE_CERTIFICATES_PENDING_EXTERNAL_DISPOSITION',
    proof_mechanism='All-source same-fiber coverage; union over triangle choices is a necessary relaxation; opposite two gap shapes at all five roots would2-edge-color an odd5cycle.',
    correction='Initial code used one difference set for traversing one edge fourtimes; corrected to two difference-set sums before finalcycle. Correct root0 has8 fullbacktrack shapes; backtrack fullness is not a necessary condition.',
    final_five_root_cycle_CPU_seconds=c['CPU_seconds'],
    formalized_in_Lean=False,new_Lean_graph_instances=0,
    excluded_only_after_review='Specified controlleredge-dependent but fiber-coordinate-independent coefficient sets with fixed matrices/directions.',
    not_excluded=['coordinate-dependent coefficient rules','changed matrices or controller',
                  'different branch allocations','general3750-point degree10/D4 graphs'],
    evidence_paths=cp),cp)

for row in rows.values():
    assert not capture_filter.screen(json.dumps(row,ensure_ascii=False))
draft=HERE/'F5_STRUCTURAL_PENDING_REVIEW_WIKI_ROWS.json'
draft.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n')
scope='''# Pending-review additive F5 Wiki preparation

Only three existing experiment/source rows are prepared: complete3750 graph gains the pure-edge-deletion criticality diagnostic; original Mizuno source gains fixed algebraic quotient/cover data; old restricted-noise experiment gains the independently-per-edge fixed-subset oddcycle obstruction, pending one targeted review. No new ledger row, verified claim or complete Lean instance is prepared.

The edge argument uses control distance exactly3 and unique control word, followed by bijective3noise endpoint coordinates. This proves actual remote witnesses for every specific lifted edge, rather than merely invalidating one route certificate.

The translation preserves line relations modulo the target noise line, rather than requiring a common invariant matrix line. The750-point formula quotient has local covering bijections. Its cached controller0-to3 route and projected noise rank2 give exactly5 walks to each target; ordinary-cover path lifting then excludes more than5 sheets atD3. It is dominated by the existing3750 graph and is not counted as a new improved example.

The oddcycle proof uses the exact intersection over all source holonomy images, then unions over triangle choices as a sound relaxation. The image-space intersection bound by3^r is valid by an injective r-coordinate projection of the r-dimensional affine space. Only the final corrected fourtraversal difference-set sum is used. It is finite exact algebra, not Lean, and10^60 counts literal assignments rather than actual generated or nonisomorphic graphs. External review has not yet been incorporated; no accepted new mathematical claim is born here.

This preparer does not alter the Wiki or root-owned brief/plan/HTML and does not run algebra, graph generation, BFS, path enumeration, a solver, compiler or external reviewer. Existing counts remain368 ledger records,104 valid examples/4 parameters,103 confirmed public-table examples/3 cells, complete formula Lean1, current-global noveltypending1.
'''
assert not capture_filter.screen(scope)
(HERE/'F5_STRUCTURAL_PENDING_REVIEW_WIKI_SCOPE.md').write_text(scope)
print(json.dumps(dict(status='PREPARED_ONLY_WAITING_FOR_REVIEW_DISPOSITION',
    existing_ids=list(ids.values()),new_ledger_rows=0,new_claims=0,
    raw=rel(draft),Wiki_written=False,new_experiments=0),ensure_ascii=False))

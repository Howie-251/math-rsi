#!/usr/bin/env python3
"""Read existing finite certificates; no adjacency or R2/geometry recomputation."""
from pathlib import Path
import json,resource
P=Path(__file__).resolve().parent;R=P.parents[4]
OLD=R/'research/ddp/more_graphs_20261027/d3d4_transfer'
j=json.loads((OLD/'RESULT.json').read_text())['source715']
sources=json.loads((OLD/'SOURCES.json').read_text())
credit=next(x for x in sources if x['file']=='source715.implicit_adj.txt')
interface={'date':'2026-11-01','basis':'Copied from previous actual source715 degree/class/R2 certificate; not rechecked.',
 'source':str((OLD/'source715.implicit_adj.txt').relative_to(R)),'source_primary':credit,
 'n':j['n'],'m':j['m'],'degree_histogram':j['degree_histogram'],'classes':j['classes'],
 'classes_hit_by_each_eligible_R2':j['classes_hit_by_each_eligible_R2'],
 'eligible_targets_hit_per_R2':j['eligible_targets_hit_per_R2'],
 'per_pin_evidence':str((OLD/'RESULT.json').relative_to(R))+'#source715.per_pin_target_certificate',
 'unused_source585_binding':'No saved certificate that deleting130 copy vertices from715 gives the separate saved585 literal with exactly the same labels; no such comparison is needed for the class obstruction.'}
(P/'SOURCE_CLASS_INTERFACE.json').write_text(json.dumps(interface,indent=2)+'\n')
u=resource.getrusage(resource.RUSAGE_SELF);cpu=u.ru_utime+u.ru_stime
result={
 'date':'2026-11-01','status':'SUPPORTED_FIXED_PETERSEN10_CLASS_OBSTRUCTION_STOP',
 'source_prediction_status':'REFUTED_INDEPENDENT_DEGREE8_TRIPLE_MODEL',
 'actual_source':{'path':interface['source'],'n':715,'m':3770,'maximum_degree':11,
   'degree_histogram':j['degree_histogram'],'eligible_vertices':195,'core_vertices':520,
   'class_count':65,'class_size':3,'class_internal_graph':'P3','class_common_core_neighbors':8,
   'class_spare_degrees':[1,2,2],'total_spare_per_class':5,
   'source_acceptance':'inherited published literal and previous actual structural certificate; no BFS or adjacency recheck',
   'credit':credit['credit'],'primary_URL':credit['url'],'retrieved_UTC_date':credit['retrieved_UTC_date']},
 'initial_prediction_correction':'The source is not the bare independent fullN-twin replication. The actual715 has130 internal class edges, forming65 P3s. The independent degree8 triple model would have3640edges; actualm3770.',
 'bound_to_saved585_literal':False,'saved585_binding_gap':'No existing deletion/label-equality certificate found. Core-only use of the separately saved585 Steiner masks is therefore kept conditional, not silently applied.',
 'inherited_finite_premises':[
  '195 eligible vertices form65 three-point classes; each has the same8 saturated core neighbors.',
  'No eligible-old edge goes between different classes; each core vertex has all3 eligible neighbors in one class.',
  'For every eligible pin, its old closed radius2 intersects the195 eligible targets in exactly its own3-point class.',
  'All520 core vertices have degree11 and cannot receive new edges at cap11.'
 ],
 'old_closed_scope':'Singlehelper and any arbitrary internally connected/arranged helper block of size<=5 at cap11; larger blocks were not excluded by that previous65-spoke count.',
 'new_fixed_rule':{'helpers':10,'helper_graph':'Petersen','internal_degree_per_helper':3,'old_pins_per_helper':8,'total_old_new_edges':80,'source_old_edges':'all retained','additional_old_old_edges':0,'proposed_order_only_not_generated':725},
 'class_route_lemma':{'notation':'e(C)=number of helper-to-class spokes, X(C)=helpers having a pin inC',
  'low_attachment_case':'If e(C)<=2, some one of its3 vertices f has no helper neighbor.',
  'route_claim':'For such unpinned f, every helper h at distance<=3 from f lies in closed N_H[X(C)].',
  'return_through_oldpin_attack':'A route h--oldpin--helper--f or h--helper--helper--f is impossible since f has no helper neighbor. Other routes enter old with at most2 remaining old steps, so the old entry pin is inC by the saved separation certificate.',
  'reachable_helpers_upper_bound_if_e_at_most2':8,'required_helpers':10,
  'minimum_spokes_per_class':3,'required_total_spokes':195,'available_total_spokes':80},
 'full_Petersen10_D3_extension':'STRICTLY_EXCLUDED_FOR_STATED_APPEND_ONLY_RULE',
 'core_only_cover_status':'NOT_SOLVED_OR_EXCLUDED_BY_CLASS_TARGET_ARGUMENT',
 'core_necessary_cover':{'A_h':'classes with an old pin at helperh','T_a':'core vertices in old radius2 of classa pins','N_a':'the8 core neighbors of classa',
  'exact_route_cover':'core subset union(a in A_h)T_a union union(g adjacent h) union(a in A_g)N_a',
  'missing_owner_classes':'For every classa containing a core target missed by h ownT union, some Petersen neighbor ofh must pin classa.',
  'own_class_count_at_most':8,'neighbor_class_union_at_most':24,
  'conditional_saved585_Steiner_application_only':{'requires':'bind actual715 class quotient/labels to the separately saved585 R2/Steiner certificate','own8_core_upper_bound':380,'missed_core_lower_bound':140,'external_owner_classes_lower_bound':18,'applied_to_actual715':False}},
 'Petersen_specificity':'The upper bound uses only10 helpers and maximum internal degree3. It excludes any10-vertex maximum-degree3 helper graph with at most80 spokes under the same source/edge rules, not all possible helpergraphs or rewiring.',
 'stop':True,'not_excluded':['the core-only covering subproblem','changing old edges or adding old-old edges','different source715 variants','other helper counts/degrees/pin budgets','general(11,3) graphs above715'],
 'CPU':{'this_metadata_preparation_process_seconds':cpu,'budget_seconds':20,'scope':'old JSON metadata imports/export and write; brief prior local report/source-code reads not separately metered'},
 'source_adjacency_parses':0,'source_BFS_runs':0,'old_R2_or_Steiner_recomputations':0,
 'solver_runs':0,'Lean_runs':0,'remote_reviews':0,'new_graphs':0,'new_parameters':0,'new_Lean_instances':0}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'TERMINAL.json').write_text(json.dumps({'date':result['date'],'status':result['status'],'active_processes':0,'stop':True,'new_graphs':0,'new_parameters':0,'new_Lean_instances':0,'measured_metadata_CPU_seconds':cpu,'CPU_seconds_budget':20,'source_adjacency_parses':0,'source_BFS_runs':0,'old_R2_or_Steiner_recomputations':0,'solver_runs':0},indent=2)+'\n')
print(json.dumps({'status':result['status'],'actual_source':result['actual_source'],'class_bound':result['class_route_lemma'],'CPU':result['CPU']},indent=2))

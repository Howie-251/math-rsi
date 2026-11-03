#!/usr/bin/env python3
"""Read-only coefficient-domain gate; no graph, field-law, rank or BFS calculation."""
import json
import resource
from pathlib import Path
R=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
SOURCE=R/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
j=json.loads(SOURCE.read_text())
counts={str(x):0 for x in range(4)}
first=None
for u,row in enumerate(j['matrices']):
    for port,M in enumerate(row):
        for ri,rr in enumerate(M):
            for ci,v in enumerate(rr):
                counts[str(v)]=counts.get(str(v),0)+1
                if v not in (0,1) and first is None:
                    first={'controller':u,'port':port,'target_controller':j['controller'][u][port],
                           'matrix_GF4_codes':M,'input':[int(k==ci) for k in range(3)],
                           'noise':0,'output_GF4_codes':[M[k][ci] for k in range(3)]}
# Multiplication by a standard basis vector only selects a stored column.
# No field law or old matrix/rank certificate is recomputed here.
assert (j['q'],j['dimension'],j['lift_order'])==(4,3,1920)
assert first is not None
r=resource.getrusage(resource.RUSAGE_SELF)
cpu=r.ru_utime+r.ru_stime
result={
 'date':'2026-11-01','status':'STOP_LITERAL_F2_SPECIALIZATION_NOT_DEFINED',
 'prediction':'If the accepted literal C30 rule is valid on F2^3, count <=4 nonbacktracking walks as a necessary five-cover gate.',
 'result':'The saved GF4 affine maps do not preserve the standard binary subspace; no accepted literal q2/240 input was located in the specified cache. The walk-count gate is therefore not run.',
 'source_rule':{'path':str(SOURCE.relative_to(R)),'q':j['q'],'dimension':j['dimension'],
                'controller_order':j['controller_order'],'edge_local_directed_matrices':120,
                'GF4_encoding':{'0':'0','1':'1','2':'alpha','3':'alpha+1'},
                'GF4_relation':'alpha^2+alpha+1=0','coefficient_counts':counts},
 'degree':8,'n':240,'target_n':1200,
 'requested_parameters_are_conditional':True,
 'inherited_accepted_source':{'q':4,'degree':16,'n':1920,'status':'previously accepted; not regenerated or revalidated',
      'evidence':['research/ddp/breadth_20261027_wave4/mizuno_d3_source/PROOF_ja.md',
                  'research/ddp/breadth_20261027_wave4/mizuno_d3_source/local_check.json',
                  'research/ddp/breadth_20261027_wave4/mizuno_d3_source/original_independent_certificate.json']},
 'binary_source_status':'not supplied/accepted; no claim of a degree8/order240 graph',
 'witness':first,
 'domain_obstruction':'At noise 0 the stored map takes binary e2 to (alpha,0,alpha+1), outside F2^3. There is no unital F4-to-F2 field homomorphism: alpha^2+alpha+1 has no F2 root. Integer mod2 recoding is a different construction and inherits none of the stored inverse identities.',
 'minimum_le4_nonbacktracking_walk_count':None,'actual_pair':None,
 'walk_count_status':'NOT_RUN_NO_VALID_LITERAL_BINARY_BASE',
 'prior_exclusion':{'report':'research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md',
     'terminal':'research/ddp/breadth_20261027_wave5/binary_route_chart3/terminal.json',
     'exact_scope':'four global inverse-label matrices over F2^3 with every one of 36 reduced three-letter words individually full rank',
     'does_not_exclude':['edge-local binary matrices','multiple-route union coverage','a different binary C30 affine construction','general degree8,D4 five-covers']},
 'unrelated_old_scope':'f4_degree19_retained_vertices_gate/check_controller.py uses GF4/C60/5ports and a retained-vertex deletion gate; it gives no C30/q2 exclusion.',
 'CPU':{'this_saved_gate_process_seconds':cpu,'earlier_metadata_inspection_seconds':0.001626606,
        'measured_process_total_seconds':cpu+0.001626606,'limit_seconds':10,
        'read_only_shell_and_manual_preparation':'brief local reads, file preparation and first path-resolution failure; not separately metered; this is a measured process subtotal rather than an exact cumulative CPU receipt'},
 'new_graphs':0,'new_parameters':0,'new_Lean_instances':0,
 'next_step':'Stop this literal-rule transfer. A new actual F2 edge-local chart plus its inverse/direction and source-legality evidence would be required before a five-cover route-count gate; this batch does not search for it.'
}
OUT.joinpath('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
OUT.joinpath('TERMINAL.json').write_text(json.dumps({'date':'2026-11-01','status':result['status'],'active_processes':0,
    'completed':True,'budget_CPU_seconds':10,'measured_process_CPU_seconds':cpu+0.001626606,
    'new_graphs':0,'route_count_run':False,'stop_scope':'this accepted literal GF4-to-standard-F2 restriction only'},indent=2)+'\n')
print(json.dumps({'status':result['status'],'CPU':result['CPU'],'witness':first}))

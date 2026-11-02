import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;Q=R/'formal/DegreeDiameter/Portfolio';t=time.process_time()
p=json.loads((P/'PARAMETERS.json').read_text());s=(Q/'F9Graph56862.lean').read_text();f=(Q/'F9Graph56862Field.lean').read_text()
def rhs(name):return re.search(r'^def '+name+r' .*? := (.+)$',s,re.M).group(1)
controller=json.loads(rhs('controllerData').replace('#',''));charts=json.loads(rhs('chartData').replace('#',''))
matrices=json.loads(re.sub(r'F\.c(\d)',r'\1',rhs('matrixPool')).replace('!',''))
directions=json.loads(re.sub(r'F\.c(\d)',r'\1',rhs('direction')).replace('!',''))
assert controller==p['controller'] and charts==p['dart_chart_index'] and matrices==p['matrices'] and directions==p['directions']
assert p['inverse_ports']==[1,0,3,2,4,5] and rhs('inversePort')=='![1,0,3,2,4,5]'
for u in range(78):
 for port in range(6):assert charts[u][port]==(port if port<4 else 2*port-4+(u>controller[u][port]))
addpart=f.split('def add :',1)[1].split('def mul :',1)[0];mulpart=f.split('def mul :',1)[1].split('def neg :',1)[0]
at={(int(a),int(b)):int(c) for a,b,c in re.findall(r'\| c(\d),c(\d) => c(\d)',addpart)}
mt={(int(a),int(b)):int(c) for a,b,c in re.findall(r'\| c(\d),c(\d) => c(\d)',mulpart)}
assert len(at)==len(mt)==81
for a in range(9):
 for b in range(9):
  assert at[a,b]==(a%3+b%3)%3+3*((a//3+b//3)%3)
  assert mt[a,b]==p['field']['multiplication'][a][b]
nt={int(a):int(b) for a,b in re.findall(r'\| c(\d) => c(\d)',f.split('def neg :',1)[1].split('instance : Add',1)[0])}
assert all(nt[a]==(-a%3)%3+3*((-(a//3))%3) for a in range(9))
header=(P/'independent_acceptance/literal_inputs.h').read_text()
def header_flat(name):
 row=next(x for x in header.splitlines() if re.search(r'\b'+name+r'=',x));return list(map(int,re.findall(r'\d+',row.split('=',1)[1])))
def flatten(x):return sum((flatten(y) if isinstance(y,list) else [y] for y in x),[])
assert header_flat('declared_controller')==flatten(controller)
assert header_flat('matrices')==flatten(matrices) and header_flat('directions')==flatten(directions)
ind=json.loads((P/'independent_acceptance/SUMMARY.json').read_text())
assert ind['status']=='PASS_COMPLETE_LITERAL_GRAPH_AND_ALL_PAIR_ROUTE_PROOF' and ind['n']==56862 and ind['m']==1535274
assert ind['all_literal_edges_formula_bound']==1535274 and ind['all_literal_vertex_degrees_checked']==56862 and ind['strict_global_order_and_simple']
assert ind['used_true_inverse_chart_types']==8 and ind['controller_ordered_pairs']==6084
out=dict(status='PASS_TYPED_GF9_CONTROLLER_CHART_LABEL_FORMULA_BOUND_TO_FRESH_LITERAL_ACCEPTANCE',
 field='GF3[w]/(w²+1),codea+3b',literal_addition_entries=81,literal_multiplication_entries=81,literal_negation_entries=9,
 typed_controller_entries_bound=468,typed_dart_chart_entries_bound=468,typed_matrix_entries_bound=72,typed_direction_entries_bound=18,
 actual_used_chart_types=8,graph_carrier='Fin56862',vertex_label='729*u+x0+9*x1+81*x2',
 edge_formula='forward: y=matrixPool[chart(u,p)]*x+t*direction[inversePort(p)]',reverse_noise='-t in characteristic3',
 independent_literal_inputs_match_typed_controller_matrices_directions=True,
 independent_summary='../independent_acceptance/SUMMARY.json',independent_status=ind['status'],literal_edges_bound_by_fresh_checker=1535274,
 independent_all_vertices_degree54=True,independent_actual_BFS_roots=ind['actual_literal_BFS_roots'],independent_all_graph_roots_BFS=False,
 concrete_all_pairs_kernel_status='CHECK_FINAL_COMPILE_RESULT_SEPARATELY',large_edgefiles_read_by_formalization=0,BFS_runs_by_formalization=0,
 ASCII_parser_formalized=False,old_modules_changed_or_recompiled=False,CPU_seconds=time.process_time()-t)
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','typed_controller_entries_bound','typed_dart_chart_entries_bound','literal_edges_bound_by_fresh_checker','CPU_seconds']}))

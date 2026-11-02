import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;t=time.process_time();x=json.loads((P/'PARAMETERS.json').read_text());source=(R/'formal/DegreeDiameter/Portfolio/OppositeGQ44SpreadDefinitions.lean').read_text()
def nums(name):
 m=re.search(r'^def '+name+r' .*? := (.+)$',source,re.M);assert m
 return list(map(int,re.findall(r'\d+',m.group(1))))
ls=[l['points'] for l in x['lines']];pl=x['point_incident_lines'];sp=x['spread_line_labels'];own=x['point_spread_owner']
assert nums('linePoint')==sum(ls,[]) and nums('pointLine')==sum(pl,[]) and nums('spread')==sp and nums('spreadOwner')==own
assert all(0<=v<85 for v in sum(ls,[])+sum(pl,[])+sp) and all(0<=v<17 for v in own)
assert [l['line'] for l in x['lines']]==list(range(85)) and len(x['points'])==85
assert pl==[[l for l in range(85) if p in ls[l]] for p in range(85)]
steps=json.loads((P/'EXTENSION_STEPS.json').read_text())['steps'];assert len(steps)==17
pins=[]
for j,s in enumerate(steps):
 z=[85*p+l for p in ls[sp[j]] for l in pl[p]]
 assert z==s['pins'] and s['new_vertex']==7225+j
 # The literal spread line field is producer metadata, not the new index.
 assert s['spread_line']==sp[j]
 pins.append(z)
formula=set()
for p in range(85):
 for l in range(85):
  u=85*p+l
  for q in ls[l]:
   for m in pl[p]:
    v=85*q+m
    if u!=v:formula.add((min(u,v),max(u,v)))
for j,z in enumerate(pins):
 for u in z:formula.add((u,7225+j))
f=(P/'graph_d25_D3_n7242.edges').open();head=tuple(map(int,next(f).split()));literal=[tuple(map(int,s.split())) for s in f if s.strip()];assert head==(7242,90525) and len(literal)==90525 and set(literal)==formula
out={'status':'PASS_EXACT_TYPED_LITERAL_AND_ORDERED_PIN_EDGE_BINDING','point_label_rule':x['point_normalization'],'point_coordinate_order':x['point_coordinates'],'point_count':85,'all_typed_numeral_inputs_in_bounds':True,'line_labels_order_equal_0_through84':True,'typed_linePoint_entries_readback_equal':425,'typed_pointLine_entries_readback_equal':425,'typed_spread_labels_readback_equal':sp,'typed_owner_entries_readback_equal':85,'through_lines_equal_actual_literal_incidence':True,'ordered_new_step_count':17,'ordered_pins_readback_equal':425,'all_step_pins_equal_at_same_index':True,'new_vertex_labels_equal_7225_plus_index':True,'old_label_equal_85_times_point_plus_line':True,'literal_header':list(head),'formula_edge_count':len(formula),'literal_edge_count':len(literal),'literal_edges_equal_formula_edges':True,'carrier':'Fin7225 ⊕ Fin17','Fin7242_equivalence':'label with label_old and label_new proved rfl','ASCII_parser_theorem':False,'distance_BFS_runs':0,'solver_calls':0,'CPU_seconds':time.process_time()-t}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;t=time.process_time()
x=json.loads((P/'PARAMETERS.json').read_text());source=(R/'formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadDefinitions.lean').read_text()
def read_flat(name):
 m=re.search(r'def '+name+r' : Array Nat := #\[([^\]]*)\]',source)
 assert m
 return [int(n) for n in re.findall(r'\d+',m.group(1))]
lines=[l['points'] for l in x['lines']];through=x['point_incident_lines'];lf=read_flat('linePointData');pf=read_flat('pointLineData')
assert lf==sum(lines,[]) and pf==sum(through,[])
assert [l['line'] for l in x['lines']]==list(range(96))
assert x['points']==[[n%4,n//4%4,n//16] for n in range(64)]
assert x['spread_line_labels']==list(range(16))
steps=json.loads((P/'EXTENSION_STEPS.json').read_text())['steps'];assert len(steps)==16
ordered_pins=[]
for j,s in enumerate(steps):
 pins=[96*p+l for p in lines[j] for l in through[p]]
 assert pins==s['pins'] and s['new_vertex']==6144+j and s['spread_line']==j
 ordered_pins.append(pins)
# Direct adjacency/label binding only. No distance traversal or graph search.
formula_edges=set()
for p in range(64):
 for l in range(96):
  u=96*p+l
  for q in lines[l]:
   for m in through[p]:
    v=96*q+m
    if u!=v:formula_edges.add((min(u,v),max(u,v)))
for j,pins in enumerate(ordered_pins):
 for v in pins:formula_edges.add((v,6144+j))
f=(P/'graph_d24_D3_n6160.edges').open();header=tuple(map(int,next(f).split()));literal=[tuple(map(int,s.split())) for s in f if s.strip()]
assert header==(6160,73920) and len(literal)==73920 and set(literal)==formula_edges
out={'status':'PASS_EXACT_LITERAL_DEFINITION_AND_EDGE_BINDING','point_labels_checked':64,'point_encoding':'a+4*b+16*c; binary GF4 labels0,1,w,w+1','ordered_line_labels_checked':96,'original_linePoint_literal_entries_readback_equal':384,'original_pointLine_literal_entries_readback_equal':384,'spread_order_exact':list(range(16)),'ordered_steps_checked':16,'ordered_pin_labels_checked':384,'each_step_ordered_pins_equal':True,'new_labels_equal_6144_plus_step_index':True,'old_label_equal_96_times_point_plus_line':True,'literal_edge_header':list(header),'literal_edge_count':len(literal),'formula_edge_count':len(formula_edges),'literal_edges_equal_formula_edges':True,'carrier':'Fin6144 ⊕ Fin16','label_equivalence':'OppositeGQ35Spread.label : Vertex ≃ Fin6160','label_old_theorem':'label_old','label_new_theorem':'label_new','ASCII_parser_theorem':False,'distance_BFS_runs':0,'solver_calls':0,'independent_acceptance':'separate independent_acceptance/INDEPENDENT_ACCEPTANCE.json; all6160roots PASS','CPU_seconds':time.process_time()-t}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

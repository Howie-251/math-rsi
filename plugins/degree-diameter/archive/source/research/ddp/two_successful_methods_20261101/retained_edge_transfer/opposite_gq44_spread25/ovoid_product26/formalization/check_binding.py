import json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parent;t=time.process_time()
source=(R/'formal/DegreeDiameter/Portfolio/OvoidProduct26Definitions.lean').read_text();m=re.search(r'^def ovoid .*? := (.+)$',source,re.M);assert m;ov=list(map(int,re.findall(r'\d+',m.group(1))))
g=json.loads((P/'OVOID_GEOMETRY_CHECK.json').read_text());p=json.loads((S/'PARAMETERS.json').read_text());sp=p['spread_line_labels'];assert ov==g['ovoid_point_ids'] and len(ov)==17 and all(0<=x<85 for x in ov)
# The parent source formula-to-edge binding is already complete and unchanged.
parent_binding=json.loads((S/'formalization/INPUT_BINDING_CHECK.json').read_text());assert parent_binding['literal_edges_equal_formula_edges'] and parent_binding['formula_edge_count']==90525
f=(S/'graph_d25_D3_n7242.edges').open();head=tuple(map(int,next(f).split()));source_edges=[tuple(map(int,z.split())) for z in f if z.strip()];assert head==(7242,90525) and len(source_edges)==90525
adj=[set() for _ in range(7242)]
for u,v in source_edges:adj[u].add(v);adj[v].add(u)
centers=json.loads((P/'ORDERED_CENTERS.json').read_text())['centers'];snap=json.loads((P/'IMMUTABLE_SOURCE_PINS.json').read_text());rows=snap['rows'];steps=json.loads((P/'EXTENSION_STEPS.json').read_text())['steps'];assert len(centers)==len(rows)==len(steps)==289
formula=set(source_edges);ordered_owners=[]
for k,(c,r,s) in enumerate(zip(centers,rows,steps)):
 i,j=divmod(k,17);owner=85*ov[i]+sp[j];pins=sorted(adj[owner]);assert len(pins)==25 and all(v<7242 for v in pins)
 assert c['index']==r['index']==s['step']==k and c['point']==r['point']==ov[i] and c['spread_index']==r['spread_index']==j and c['spread_line']==r['spread_line']==sp[j]
 assert c['old_center_label']==r['center']==s['center']==owner
 assert c['source_full_neighborhood_ordered']==r['original_source_pins']==s['pins']==pins and s['immutable_pin_row']==k and s['new_vertex']==7242+k
 ordered_owners.append(owner)
 for u in pins:formula.add((u,7242+k))
f=(P/'graph_d26_D3_n7531.edges').open();head=tuple(map(int,next(f).split()));literal=[tuple(map(int,z.split())) for z in f if z.strip()];assert head==(7531,97750) and len(literal)==97750 and set(literal)==formula
out={'status':'PASS_ORDERED_PRODUCT_CENTERS_AND_IMMUTABLE_ORIGINAL_SOURCE_PIN_BINDING','ovoid17_readback_exact':ov,'original_spread17_order_inherited':sp,'center_product_order':'ovoid index outer, original spread index inner','ordered_owners_checked':289,'ordered_owner_labels_equal_all_three_actual_tables':True,'cloneIndex_equivalence':'Fin17×Fin17 ≃ Fin289; k=17*i+j','new_labels_equal_7242_plus_17_i_plus_j':True,'source_label_preserved':True,'pins_checked':7225,'each_pin_list_order_equal_original_source_neighborhood':True,'source_n':7242,'source_m':90525,'source_formula_binding_reused':'../../formalization/INPUT_BINDING_CHECK.json (actual7242source, unchanged)','all_pins_original_source_labels_below7242':True,'current_center_neighborhoods_used':False,'old_edges_retained_exactly':90525,'new_new_edges':0,'literal_header':list(head),'literal_edges_equal_formula_edges':True,'formula_edge_count':len(formula),'literal_edge_count':len(literal),'carrier':'(Fin7225⊕Fin17)⊕(Fin17×Fin17)','Fin7531_equivalence':'label; old=Source.label; new7242+17*i+j','center_independence_assumed':False,'center_injectivity_assumed':False,'ASCII_parser_theorem':False,'BFS_runs':0,'solver_calls':0,'CPU_seconds':time.process_time()-t}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

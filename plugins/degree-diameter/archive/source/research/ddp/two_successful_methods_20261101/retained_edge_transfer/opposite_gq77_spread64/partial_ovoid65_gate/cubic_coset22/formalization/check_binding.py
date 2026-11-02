import heapq,json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parents[1]
t=time.process_time()
source=(R/'formal/DegreeDiameter/Portfolio/GQ77Cubic22Clone65Definitions.lean').read_text()
def rhs(name):
 m=re.search(r'^def '+name+r' .*? := (.+)$',source,re.M);assert m,name;return m.group(1)
ov=list(map(int,re.findall(r'\d+',rhs('ovoid'))))
g=json.loads((P/'PRECHECK_RESULT.json').read_text());p=json.loads((S/'PARAMETERS.json').read_text())
actual=json.loads((P/'PARAMETERS.json').read_text());centers=json.loads((P/'CENTERS.json').read_text())
assert ov==g['point_ids']==actual['partial_ovoid_point_ids'] and len(ov)==22
sp=p['spread_line_labels'];lp=[r['points'] for r in p['lines']];pl=p['point_incident_lines'];own=p['point_spread_owner']
parsed_owner=[None if x=='none' else int(i) for x,i in re.findall(r'\b(none|some (\d+))\b',rhs('ovoidOwnerBlocks'))]
expected_owner=[ov.index(x) if x in ov else None for x in range(400)]
assert parsed_owner==expected_owner
parsed_line=list(map(int,re.findall(r'\d+',rhs('lineOvoidIndexBlocks'))));assert len(parsed_line)==400
for l,pts in enumerate(lp):
 hits=[ov.index(x) for x in pts if x in ov]
 assert len(hits)<=1 and parsed_line[l]==(hits[0] if hits else 0)
parent=json.loads((S/'formalization/INPUT_BINDING_CHECK.json').read_text())
assert parent['literal_edges_compared_one_by_one']==5121600 and parent['linePoint_entries_exact']==3200 and parent['ordered_spread_labels_exact']==50
assert len(centers)==1100 and actual['source_center_labels_original_order']==[r['center'] for r in centers]
owners=[];formula_pins=[];by_owner={}
for k,c in enumerate(centers):
 i,j=divmod(k,50);owner=400*ov[i]+sp[j]
 assert c['index']==k and c['point_index']==i and c['point_id']==ov[i] and c['spread_index']==j and c['spread_line']==sp[j] and c['center']==owner
 assert c['flag']==(ov[i] in lp[sp[j]]) and c['source_degree']==64
 pins=sorted(400*q+m for q in lp[sp[j]] for m in pl[ov[i]] if 400*q+m!=owner)
 if c['flag']:
  assert own[ov[i]]==j;pins.append(160000+j)
 assert len(pins)==len(set(pins))==64 and all(x<160050 for x in pins)
 assert owner not in by_owner;by_owner[owner]=k;owners.append(owner);formula_pins.append(sorted(pins))
literal_pins=[[] for _ in centers]
def edge_reader(path,n,m):
 with path.open() as f:
  assert tuple(map(int,next(f).split()))==(n,m)
  count=0;last=(-1,-1)
  for row in f:
   u,v=map(int,row.split());assert 0<=u<v<n and last<(u,v);last=(u,v);count+=1;yield u,v
  assert count==m
for u,v in edge_reader(S/'graph_d64_D3_n160050.edges',160050,5121600):
 if u in by_owner:literal_pins[by_owner[u]].append(v)
 if v in by_owner:literal_pins[by_owner[v]].append(u)
for a,b in zip(literal_pins,formula_pins):assert sorted(a)==b
added=sorted((v,160050+k) for k,pins in enumerate(formula_pins) for v in pins)
assert len(added)==len(set(added))==70400 and len({u for u,v in added})==70400
expected=heapq.merge(edge_reader(S/'graph_d64_D3_n160050.edges',160050,5121600),added)
count=0
for a,b in zip(edge_reader(P/'graph_d65_D3_n161150.edges',161150,5192000),expected,strict=True):
 assert a==b;count+=1
assert count==5192000
out=dict(status='PASS_LITERAL_FIN1100_LABELS_ORDERED_CENTERS_IMMUTABLE_PINS_ALL_EDGES',ovoid22_readback_exact=ov,original_spread50_order_inherited=sp,
 owner_point_entries=400,line_index_entries=400,line_position_certificate_checks=3200,center_product_order='point index outer; original spread index inner',
 ordered_center_labels_bound=1100,owners_all_distinct=True,center_label_formula='400*ovoid[i]+originalSpread[j]',clone_index='k=50*i+j : Fin1100',
 new_label_formula='160050+k',source_label_preserved=True,source_n=160050,source_m=5121600,pins_bound=70400,pin_rows_bound=1100,pin_row_size=64,
 pins_equal_literal_original_source_neighbors=True,pins_equal_bound_source_formula=True,source_pins_immutable=True,current_center_neighborhood_used=False,
 all_pins_original_source_labels_below160050=True,old_edges_retained_exactly=5121600,new_edges_bound=70400,new_new_edges=0,
 literal_edges_equal_fixed_source_clone_formula=True,literal_edges_compared_one_by_one=5192000,carrier='(Fin160000⊕Fin50)⊕Fin1100',
 explicit_equivalence='label : Vertex ≃ Fin161150',center_independence_assumed=False,center_injectivity_required_by_generic=False,
 source_formula_binding_reused='../../../formalization/INPUT_BINDING_CHECK.json',ASCII_parser_formalized=False,BFS_runs=0,solver_calls=0,
 independent_acceptance_claim=False,CPU_seconds=time.process_time()-t)
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

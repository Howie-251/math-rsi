import csv,json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parent
t=time.process_time()
q=R/'formal/DegreeDiameter/Portfolio'
text=(q/'GQ77Cubic22Clone70Definitions.lean').read_text()
assert 'abbrev CloneIndex := Fin 6600' in text and 'abbrev Vertex := Source.Vertex ⊕ CloneIndex' in text
assert 'def cloneLabel : (Fin 6 × Fin 1100) ≃ CloneIndex := finProdFinEquiv' in text
assert 'def center (k : CloneIndex) : Source.Vertex := GQ77Cubic22Clone65.center (clonePair k).2' in text
assert 'FullNeighborhoodClones.graph OppositeGQ77Spread.graph center' in text
assert 'def label : Vertex ≃ Fin 166650' in text
base=(q/'GQ77Cubic22Clone65Definitions.lean').read_text()
ov=list(map(int,re.findall(r'\d+',re.search(r'^def ovoid .*? := (.+)$',base,re.M).group(1))))
params=json.loads((P/'PARAMETERS.json').read_text());source=json.loads((S/'PARAMETERS.json').read_text())
sp=source['spread_line_labels'];points=source['points'];centers=json.loads((P/'BASE_CENTERS.json').read_text())
assert len(centers)==1100 and params['source_n']==160050 and params['source_m']==5121600 and params['source_degree']==64
assert params['multiplicity']==6 and params['clones']==6600 and params['partial_ovoid_point_ids']==ov and params['spread_line_ids_original_order']==sp
assert [points[x] for x in ov]==params['partial_ovoid_points']
for b,c in enumerate(centers):
 i,j=divmod(b,50);assert c['index']==b and c['point_index']==i and c['point_id']==ov[i] and c['spread_index']==j and c['spread_line']==sp[j]
 assert c['center']==400*ov[i]+sp[j] and c['source_degree']==64
assert params['source_base_center_labels_original_order']==[c['center'] for c in centers]
base_binding=json.loads((S/'partial_ovoid65_gate/cubic_coset22/formalization/INPUT_BINDING_CHECK.json').read_text())
assert base_binding['pins_equal_literal_original_source_neighbors'] and base_binding['source_pins_immutable'] and base_binding['ordered_center_labels_bound']==1100
expected=[]
for copy in range(6):
 for b,c in enumerate(centers):
  i,j=divmod(b,50);k=1100*copy+b
  expected.append(dict(clone_index=k,copy=copy,base_index=b,point_index=i,spread_index=j,source_center=400*ov[i]+sp[j],new_vertex=160050+k))
prefix=list(csv.DictReader((P/'PREFIX_LOADS.csv').open()));assert len(prefix)==len(expected)==6600
for e,row in zip(expected,prefix):
 row={k:int(v) for k,v in row.items()}
 for k,v in e.items():assert row[k]==v,(k,e,row)
 assert row['current_n_after']==e['new_vertex']+1 and row['pin_degree_before']==64+e['copy'] and row['pin_degree_after']==65+e['copy']
 assert row['new_vertex_degree']==64 and row['new_edges_so_far']==64*(e['clone_index']+1)
with (D/'FORMAL_ORDERED_CLONE_RECIPE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(expected[0]));w.writeheader();w.writerows(expected)
out=dict(status='PASS_TYPED_FIN6600_COPY_BASE_ORDER_AND_PRODUCER_PREFIX_RECIPE',
 carrier='(Fin160000⊕Fin50)⊕Fin6600',label='label : Vertex ≃ Fin166650',clone_pair='Fin6600 ≃ Fin6×Fin1100',
 clone_index_formula='k=1100*copy+50*i+j',new_label_formula='160050+k',source_center_formula='center65(k%1100)',
 source_is_original160050=True,source_is_current161150=False,source_label_preserved=True,base_centers_bound=1100,
 ordered_clone_centers_and_labels_bound=6600,producer_prefix_rows_bound=6600,typed_formula_export='FORMAL_ORDERED_CLONE_RECIPE.csv',
 original_point_order=ov,original_spread_order=sp,base_immutable_pins_binding_reused='../../partial_ovoid65_gate/cubic_coset22/formalization/INPUT_BINDING_CHECK.json',
 independent_literal_summary='PENDING_ROOT_FRESH_INDEPENDENT_ACCEPTANCE',large_edgefiles_read_by_this_checker=0,
 new_or_old_graph_BFS_runs=0,ASCII_parser_formalized=False,independent_acceptance_claim=False,CPU_seconds=time.process_time()-t)
if (P/'independent_acceptance/SUMMARY.json').exists():
 ind=json.loads((P/'independent_acceptance/SUMMARY.json').read_text());inp=json.loads((P/'independent_acceptance/INDEPENDENT_INPUTS.json').read_text())
 assert inp['point_ids_outer']==ov and inp['spread_line_ids_inner']==sp
 assert inp['source_edgefile']==str(S/'graph_d64_D3_n160050.edges') and inp['candidate_edgefile']==str(P/'graph_d70_D3_n166650.edges')
 assert ind['status']=='PASS' and ind['vertices']==166650 and ind['edges']==5544000
 assert ind['old_literal_body_exact'] and ind['all6600_newlabel_source_full_N_bindings_exact'] and ind['all6copies_individually_checked']
 assert ind['new_edges']==422400 and ind['new_new_edges']==0 and ind['full_source_neighborhood_exact_each']==64
 out.update(independent_literal_summary='../independent_acceptance/SUMMARY.json',independent_literal_status='PASS',
  independent_recipe_matches_typed_O22_spread_and_clone_order=True,independent_old_edges_retained_exactly=5121600,
  independent_all6600_source_full_neighborhoods_exact=True,independent_new_edges_bound=422400,
  independent_literal_edges_bound=5544000,independent_new_new_edges=0,
  independent_summary_read_only=True,independent_BFS_runs=ind['new_root_BFS_runs'],independent_old_root_BFS_runs=ind['old_root_BFS_runs'])
 out['CPU_seconds']=time.process_time()-t
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','ordered_clone_centers_and_labels_bound','producer_prefix_rows_bound','large_edgefiles_read_by_this_checker','CPU_seconds']}))

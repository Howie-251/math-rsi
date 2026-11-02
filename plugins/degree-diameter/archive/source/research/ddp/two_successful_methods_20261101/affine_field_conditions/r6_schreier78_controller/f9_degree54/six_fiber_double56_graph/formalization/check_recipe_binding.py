import csv,json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parent;t=time.process_time()
source=(R/'formal/DegreeDiameter/Portfolio/F9SixFiberDouble56Definitions.lean').read_text()
U=list(map(int,re.findall(r'\d+',re.search(r'^def chosenFiber .*? := (.+)$',source,re.M).group(1))))
assert U==[0,1,2,3,9,15] and 'abbrev BaseIndex := Fin 486' in source and 'abbrev CloneIndex := Fin 972' in source
assert 'abbrev Vertex := Fin 56862 ⊕ CloneIndex' in source and 'FullNeighborhoodClones.graph F9Graph56862.graph center' in source
assert 'def label : Vertex ≃ Fin 57834 := finSumFinEquiv' in source
p=json.loads((P/'PARAMETERS.json').read_text());sp=json.loads((S/'PARAMETERS.json').read_text());mul=sp['field']['multiplication']
assert p['source_n']==56862 and p['source_m']==1535274 and p['source_degree']==54 and p['selected_controllers']==U
assert p['immutable_original_source_only'] and not p['source_is_new55_graph'] and p['copies']==2
base=[729*u+a+9*b+81*mul[4][a] for u in U for a in range(9) for b in range(9)]
assert base==p['base_center_labels'] and len(set(base))==486
prefix={int(r['j']):{k:(int(v) if v.isdigit() else v) for k,v in r.items()} for r in csv.DictReader((P/'PREFIX_LOADS.csv').open())}
assert set(prefix)==set(range(972))
actual_base=[]
for line in (P/'ORDERED_SOURCE_PINS.tsv').read_text().splitlines():
 vals=list(map(int,line.split()));i,c,*pins=vals;assert i==len(actual_base) and c==base[i] and len(pins)==len(set(pins))==54;actual_base.append(c)
assert len(actual_base)==486
ind=json.loads((P/'independent_acceptance/SUMMARY.json').read_text())
assert ind['status']=='PASS_COMPLETE_57834_GRAPH_DOUBLE_IMMUTABLE_FULLN_EXTENSION' and ind['n']==57834 and ind['m']==1587762
assert ind['U']==U and ind['base_centers']==486 and ind['copies_each']==2 and ind['all_972_new_literal_N54_bound_to_immutable_source_N']
assert ind['source_old_edges_preserved_exact']==1535274 and ind['new_old_edges']==52488 and ind['new_new_edges']==0
indrows={int(r['j']):{k:int(v) for k,v in r.items()} for r in csv.DictReader((P/'independent_acceptance/CENTER_PIN_BINDING.tsv').open(),delimiter='\t')}
assert set(indrows)==set(range(972))
rows=[]
for j in range(972):
 copy,bidx=divmod(j,486);ui,a,b=bidx//81,(bidx%81)//9,bidx%9;c=base[bidx];new=56862+j;r=prefix[j];z=indrows[j]
 assert r['copy']==z['copy']==copy and r['base_index']==z['base']==bidx and r['u_index']==z['uIndex']==ui
 assert r['controller']==z['u']==U[ui] and r['a']==z['a']==a and r['b']==z['b']==b
 assert r['new_label']==z['newlabel']==new and r['center_old_label']==z['center']==c and z['source_degree']==54
 assert r['pins']==54 and r['min_old_pin_degree_before']==r['max_old_pin_degree_before']==54+copy and r['max_old_pin_load_after']==copy+1
 assert r['current_vertices']==new+1 and r['current_edges']==1535274+54*(j+1)
 rows.append(dict(j=j,copy=copy,base_index=bidx,u_index=ui,controller=U[ui],a=a,b=b,source_center=c,newlabel=new))
with (D/'FORMAL_ORDERED_CLONE_RECIPE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
out=dict(status='PASS_TYPED_U6_FIN972_LABELS_RECIPE_AND_FRESH_LITERAL_SUMMARY_BINDING',chosen_fibers=U,base_index='81*uIndex+9*a+b',
 clone_index='486*copy+baseIndex',new_label='56862+cloneIndex',carrier='Fin56862⊕Fin972',label_equivalence='Fin57834',
 original_source='F9Graph56862.graph',source_is_new55_graph=False,base_center_labels_bound=486,clone_center_labels_bound=972,
 producer_prefix_rows_bound=972,independent_rows_bound_by_explicit_j=972,independent_row_order_assumed=False,
 independent_summary='../independent_acceptance/SUMMARY.json',independent_status=ind['status'],independent_literal_edges_bound=1587762,
 independent_original_edges_retained=1535274,independent_new_edges_bound=52488,independent_new_new_edges=0,
 independent_all972_immutable_N54_exact=True,source_fullN_row_size=54,typed_recipe_export='FORMAL_ORDERED_CLONE_RECIPE.csv',
 large_edgefiles_read_here=0,old_field_finite_checks_repeated=False,BFS_runs_here=0,ASCII_parser_formalized=False,
 independent_new_root_BFS_runs=ind['new_literal_R3_BFS_roots'],independent_old_R3_BFS_runs=ind['source_R3_BFS_roots'],
 CPU_seconds=time.process_time()-t)
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','clone_center_labels_bound','independent_rows_bound_by_explicit_j','CPU_seconds']}))

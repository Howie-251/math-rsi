import csv,json,re,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;S=P.parent;t=time.process_time()
text=(R/'formal/DegreeDiameter/Portfolio/F9U10PlaneCloneFamilyDefinitions.lean').read_text()
U=list(map(int,re.findall(r'\d+',re.search(r'^def chosenFiber .*? := (.+)$',text,re.M).group(1))))
assert U==[31,32,44,45,59,60,61,72,73,74]
assert 'abbrev BaseIndex := Fin 810' in text and 'Fin 56862 ⊕ (Fin k × BaseIndex)' in text
assert 'FullNeighborhoodClones.graph F9Graph56862.graph (center k)' in text and 'Vertex k ≃ Fin (56862+810*k)' in text
p=json.loads((P/'PARAMETERS.json').read_text());source=json.loads((S/'PARAMETERS.json').read_text());mul=source['field']['multiplication']
assert p['selected_controllers']==U and p['source_n']==56862 and p['source_m']==1535274 and not p['source_is_new55_graph'] and not p['k6_produced']
base=[729*u+a+9*b+81*mul[4][a] for u in U for a in range(9) for b in range(9)]
assert base==p['base_center_labels'] and len(set(base))==810
actual=[]
for line in (P/'ORDERED_SOURCE_PINS.tsv').read_text().splitlines():
 i,c,*pins=map(int,line.split());assert i==len(actual) and c==base[i] and len(pins)==len(set(pins))==54;actual.append(c)
assert len(actual)==810
prefix={int(r['j']):{k:(int(v) if v.isdigit() else v) for k,v in r.items()} for r in csv.DictReader((P/'PREFIX_LOADS.csv').open())}
assert set(prefix)==set(range(4050))
ind=json.loads((P/'independent_acceptance/SUMMARY.json').read_text())
assert ind['status']=='PASS_ALL_FIVE_COMPLETE_U10_ENDPOINT_GRAPHS' and ind['selected_k']==[1,2,3,4,5] and not ind['k6_generated_or_validated']
outcases=[];allrows=[]
for c in p['cases']:
 k,n,degree,m=c['k'],c['n'],c['degree_cap'],c['m'];name=f'd{degree}_n{n}'
 summary=json.loads((P/'independent_acceptance/cases'/name/'SUMMARY.json').read_text())
 assert summary['status']=='PASS_COMPLETE_U10_IMMUTABLE_FULLN_CASE' and summary['k']==k and summary['n']==n and summary['m']==m
 assert summary['U']==U and summary['old_edges_retained']==1535274 and summary['new_old_edges']==43740*k and summary['new_new_edges']==0
 assert summary['all_new_literal_N54_exact_to_immutable_source'] and summary['complete_old_edge_body_exact']
 rows={int(r['j']):{key:int(value) for key,value in r.items()} for r in csv.DictReader((P/'independent_acceptance/cases'/name/'ORDERED_CLONE_BINDING.tsv').open(),delimiter='\t')}
 assert set(rows)==set(range(810*k))
 for j in range(810*k):
  copy,bidx=divmod(j,810);ui,a,b=bidx//81,(bidx%81)//9,bidx%9;c0=base[bidx];new=56862+j;r=prefix[j];z=rows[j]
  assert r['copy']==z['copy']==copy and r['base_index']==z['base']==bidx and r['u_index']==ui and r['controller']==U[ui]
  assert r['a']==a and r['b']==b and r['center']==z['center']==c0 and r['newlabel']==z['newlabel']==new and z['source_degree']==54
  assert r['pins']==54 and r['pin_degree_before']==54+copy and r['pin_degree_after']==55+copy and r['old_pin_load_after']==copy+1
  assert r['current_vertices']==new+1 and r['current_edges']==1535274+54*(j+1)
  allrows.append(dict(k=k,degree=degree,j=j,copy=copy,base_index=bidx,u_index=ui,a=a,b=b,source_center=c0,newlabel=new))
 outcases.append(dict(k=k,degree=degree,n=n,m=m,ordered_rows_bound=810*k,independent_immutable_N54_rows_exact=810*k,
  original_edges_retained=1535274,new_old_edges=43740*k,new_new_edges=0,independent_summary=f'../independent_acceptance/cases/{name}/SUMMARY.json',
  literal_graph=c['graph_file'],old_load_histogram=summary['old_load_histogram'],degree_histogram=summary['degree_histogram'],
  independent_new_root_BFS_runs=summary['new_literal_R3_BFS_roots'],independent_old_R3_BFS_runs=summary['source_R3_BFS_calls']))
with (D/'FORMAL_ORDERED_CASE_RECIPE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(allrows[0]));w.writeheader();w.writerows(allrows)
out=dict(status='PASS_ALL_FIVE_TYPED_U10_CENTERS_LABELS_RECIPE_TO_FRESH_LITERAL_BINDING',selected_controllers=U,base_center_labels_bound=810,
 base_index='81*uIndex+9*a+b',clone_index='810*copy+baseIndex',newlabel='56862+cloneIndex',carrier='Fin56862⊕(Fin k×Fin810)',
 label_equivalence='Fin(56862+810*k)',source='OriginalF9Graph56862.graph',source_is_new55_or_U6_graph=False,
 max_producer_prefix_rows_bound=4050,total_endpoint_recipe_rows_bound=len(allrows),independent_rows_indexed_by_explicit_j=True,
 cases=outcases,case_count=5,k6_original_target_or_file=False,export='FORMAL_ORDERED_CASE_RECIPE.csv',
 independent_summary='../independent_acceptance/SUMMARY.json',independent_total_new_BFS_roots=12150,independent_old_R3_BFS_roots=0,
 large_edgefiles_read_here=0,old_field_controller_checks_repeated=False,BFS_runs_here=0,ASCII_parser_formalized=False,CPU_seconds=time.process_time()-t)
assert len(allrows)==12150
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','case_count','total_endpoint_recipe_rows_bound','CPU_seconds']}))

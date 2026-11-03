import ast,csv,json,re,time
from pathlib import Path

start=time.process_time()
D=Path(__file__).resolve().parent
G=D.parent
audit=(D/'F9PlaneClone55Audit.log').read_text()
m=re.search(r'\("CLONE55_ORDERED_BINDING",\s*(\[.*?\])\)',audit,re.S)
assert m,'Actual compiled Audit ordered-center output missing'
formal=ast.literal_eval(m.group(1))
assert len(formal)==81
declared=json.loads((G/'PARAMETERS.json').read_text())
independent=json.loads((G/'independent_acceptance/SUMMARY.json').read_text())
assert independent['status']=='PASS_COMPLETE_NEW_GRAPH_IMMUTABLE_FULLN_EXTENSION'
pins=list(csv.DictReader((G/'independent_acceptance/CENTER_PIN_BINDING.tsv').open(),delimiter='\t'))
assert len(pins)==81
for j,(i,c,n) in enumerate(formal):
    assert i==j
    assert c==declared['center_old_labels'][j]
    assert n==56862+j
    p=pins[j]
    assert (int(p['j']),int(p['center']),int(p['newlabel']),int(p['source_degree']))==(j,c,n,54)
with (D/'FORMAL_ORDERED_CLONE_RECIPE.csv').open('w') as out:
    w=csv.writer(out);w.writerow(['j','immutable_source_center_label','new_label'])
    w.writerows(formal)
result={'status':'PASS_ACTUAL_COMPILED_TYPED_ORDERED_RECIPE_BOUND','ordered_centers_and_newlabels_checked':81,'actual_Lean_Audit_eval_used':True,'typed_label_theorems':['clone_label','center_source_label','label_old','label_new'],'graph_definition':'FullNeighborhoodClones.graph F9Graph56862.graph center','all_new_literal_fullN54_bound_by_fresh_independent_acceptance':True,'independent_complete_edge_binding':'../independent_acceptance/SUMMARY.json','complete_large_edgefile_reads_here':0,'BFS_here':0,'source_modules_recompiled':0,'CPU_seconds':time.process_time()-start}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

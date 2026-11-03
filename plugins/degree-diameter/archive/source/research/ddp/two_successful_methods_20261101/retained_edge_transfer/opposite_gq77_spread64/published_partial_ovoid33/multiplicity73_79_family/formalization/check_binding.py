"""Bind upper fresh recipes to already compiled parent symbolic labels only."""
import csv,json,re
from pathlib import Path
from time import process_time

start=process_time();D=Path(__file__).resolve().parent;family=D.parent;P33=family.parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
P='GQ77Published33CloneFamily';U=P+'Upper'
for suffix in ['Exact','Audit']:
    receipt=json.loads((D/(U+suffix+'_RESULT.json')).read_text());assert receipt['exit_code']==0
parent_binding=P33/'multiplicity65_72_family/formalization/INPUT_BINDING_CHECK.json'
lower=json.loads(parent_binding.read_text());assert lower['independent_rows_all_eight_cases']==59400
defs=(R/'formal/DegreeDiameter/Portfolio'/(P+'Definitions.lean')).read_text()
match=re.search(r'def ovoid\s*:[^\n]*:= !\[([^\]]+)\]',defs);assert match
ids=[int(x.strip())for x in match.group(1).split(',')]
actual=json.loads((P33/'ACTUAL_POINTS.json').read_text());assert ids==actual['point_ids']and len(ids)==33
source=json.loads((P33.parent/'PARAMETERS.json').read_text())
assert [source['points'][i]for i in ids]==actual['points_mod7']
spread=source['spread_line_labels'];centers=[400*p+l for p in ids for l in spread]
producer=list(csv.DictReader((family/'ORDERED_CLONE_RECIPE.tsv').open(),delimiter='\t'));assert len(producer)==24750
for j,row in enumerate(producer):
    copy,base=divmod(j,1650);point,sp=divmod(base,50)
    assert int(row['j'])==j and int(row['copy'])==copy and int(row['base_index'])==base
    assert int(row['point_index'])==point and int(row['spread_index'])==sp
    assert int(row['point_label'])==ids[point]and int(row['spread_line'])==spread[sp]
    assert int(row['source_center_label'])==centers[base]
    assert int(row['new_label'])==160050+j and int(row['immutable_source_degree'])==64
fresh=family/'independent_acceptance';receipt=json.loads((fresh/'RESULT.json').read_text())
assert str(receipt['status']).startswith('PASS'),receipt['status']
cases=[];total=0
for k in range(9,16):
    degree,n=64+k,160050+1650*k
    path=fresh/'cases'/f'd{degree}_n{n}'/'ORDERED_CLONE_BINDING.tsv';count=0
    with path.open()as f:
        for j,row in enumerate(csv.DictReader(f,delimiter='\t')):
            copy,base=divmod(j,1650);assert 0<=copy<k and 0<=base<1650
            assert int(row['j'])==j and int(row['copy'])==copy and int(row['base'])==base
            assert int(row['source_center_label'])==centers[base]
            assert int(row['new_label'])==160050+j and int(row['literal_N_size'])==64
            count+=1
    assert count==1650*k;total+=count
    cases.append({'k':k,'degree':degree,'n':n,'ordered_rows_bound':count,'path':str(path)})
assert total==138600
result={'status':'PASS_UPPER_EXTERNAL_BINDING_TO_CLOSED_PARENT_SYMBOLIC_LABELS',
        'parent_compiled_theorems':['base_label','clone_label','center_source_label','label_old','label_new','label_new_coordinates'],
        'parent_lower_binding_receipt_preserved':str(parent_binding),'parent_lower_rows_not_reread':59400,
        'point_ids':ids,'base_center_order_rows':1650,'producer_max_recipe_rows':24750,
        'independent_upper_rows':total,'cases':cases,'independent_actual_status':receipt['status'],
        'source_or_new_graph_literal_reads':0,'BFS_runs':0,'parent_modules_recompiled':0,
        'Lean_ASCII_parser_claim':False,'Audit_eval138600_claim':False,
        'CPU_seconds':process_time()-start,'running':False,'active_processes':[]}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

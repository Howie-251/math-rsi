"""External binding of compiled label formulas to all fresh ordered recipes.

This is not a Lean parser theorem or a revalidation of large edge tables.
"""
import csv
import json
from pathlib import Path
import re
from time import process_time

start=process_time();D=Path(__file__).resolve().parent;family=D.parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
prefix='GQ77Published33CloneFamily'
for suffix in ['Definitions','Inputs','Exact','Audit']:
    receipt=json.loads((D/(prefix+suffix+'_RESULT.json')).read_text())
    assert receipt['exit_code']==0
text=(R/'formal/DegreeDiameter/Portfolio'/f'{prefix}Definitions.lean').read_text()
match=re.search(r'def ovoid\s*:[^\n]*:= !\[([^\]]+)\]',text)
assert match
ids=[int(x.strip())for x in match.group(1).split(',')]
actual=json.loads((family.parent/'ACTUAL_POINTS.json').read_text())
assert ids==actual['point_ids'] and len(ids)==33
source=json.loads((family.parent.parent/'PARAMETERS.json').read_text())
assert [source['points'][i]for i in ids]==actual['points_mod7']
spread=source['spread_line_labels'];assert len(spread)==50
centers=[400*p+line for p in ids for line in spread]
producer=list(csv.DictReader((family/'ORDERED_CLONE_RECIPE.tsv').open(),delimiter='\t'))
assert len(producer)==13200
for j,row in enumerate(producer):
    copy,base=divmod(j,1650);point,sp=divmod(base,50)
    assert int(row['j'])==j and int(row['copy'])==copy and int(row['base_index'])==base
    assert int(row['point_index'])==point and int(row['spread_index'])==sp
    assert int(row['point_label'])==ids[point] and int(row['spread_line'])==spread[sp]
    assert int(row['source_center_label'])==centers[base]
    assert int(row['new_label'])==160050+j and int(row['immutable_source_degree'])==64
fresh=family/'independent_acceptance'
receipt=json.loads((fresh/'RESULT.json').read_text())
assert str(receipt['status']).startswith('PASS'),receipt['status']
cases=[];total=0
for k in range(1,9):
    degree,n=64+k,160050+1650*k
    path=fresh/'cases'/f'd{degree}_n{n}'/'ORDERED_CLONE_BINDING.tsv'
    count=0
    with path.open()as f:
        for j,row in enumerate(csv.DictReader(f,delimiter='\t')):
            copy,base=divmod(j,1650)
            assert 0<=copy<k and 0<=base<1650
            assert int(row['j'])==j and int(row['copy'])==copy and int(row['base'])==base
            assert int(row['source_center_label'])==centers[base]
            assert int(row['new_label'])==160050+j and int(row['literal_N_size'])==64
            count+=1
    assert count==1650*k
    total+=count;cases.append({'k':k,'degree':degree,'n':n,'ordered_rows_bound':count,'path':str(path)})
assert total==59400
result={'status':'PASS_EXTERNAL_BINDING_COMPILED_LABELS_TO_FRESH_ORDERED_RECIPES',
        'compiled_label_theorems':['base_label','clone_label','center_source_label','label_old','label_new','label_new_coordinates'],
        'point_ids':ids,'points_bound_to_original400_order':33,'base_center_order_rows':1650,
        'producer_max_recipe_rows':13200,'independent_rows_all_eight_cases':total,'cases':cases,
        'independent_actual_status':receipt['status'],
        'source_literal_edgefile_reads':0,'new_literal_edgefile_reads':0,'BFS_runs':0,
        'Lean_ASCII_parser_theorem_claim':False,'Audit_eval59400_claim':False,
        'CPU_seconds':process_time()-start,'running':False,'active_processes':[]}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

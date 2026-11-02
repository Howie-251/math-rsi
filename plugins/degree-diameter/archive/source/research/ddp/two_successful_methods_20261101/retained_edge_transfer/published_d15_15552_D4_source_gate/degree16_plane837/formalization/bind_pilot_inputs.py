import ast,csv,json,re,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
gate=D.parent.parent
text=(R/'formal/DegreeDiameter/Portfolio/F3Graph15552Definitions.lean').read_text()
def array(name):
    m=re.search(r'^def '+name+r'\s*:[^\n]*:=\s*(.*)$',text,re.M);assert m,name
    return ast.literal_eval(m[1].replace('#[','['))
bound=json.loads((gate/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json').read_text())
assert array('controllerData')==bound['transition']
assert array('matrixData')==[[v for row in t['B']for v in row]for t in bound['types']]
assert array('directionData')==[t['v']for t in bound['types']]
assert array('constantData')==[t['c']for t in bound['types']]
params=json.loads((D.parent/'PARAMETERS.json').read_text());I=array('layerData')
assert I==params['selected_controller_labels']
freshdir=D.parent/'independent_acceptance'
fresh=json.loads((freshdir/'RESULT.json').read_text())
assert fresh['status']=='PASS_COMPLETE_LITERAL_AND_ALL16389_FINAL_ROOTS_EXACT_D4'
rows=list(csv.DictReader((freshdir/'ALL837_ACTUAL_ROLE_BINDINGS.tsv').open(),delimiter='\t'))
assert len(rows)==837
for j,row in enumerate(rows):
    x0=j%3;x2=j//3%3;x3=j//9%3;offset=x0+9*x2+27*x3
    center=81*I[j//27]+offset
    assert (int(row['j']),int(row['controller']),int(row['offset']),int(row['old_center_label']),int(row['new_label']))==(j,I[j//27],offset,center,15552+j)
    assert row['full_N_equal']=='true'and row['old_center_excluded']=='true'
    assert int(row['actual_simple_N_size'])in[14,15]
    assert int(row['actual_simple_N_size'])==int(row['actual_edge_count'])
result=dict(status='PASS_NEW_TYPED_SOURCE_LITERAL_AND837_ORDERED_RECIPE_SMALL_BINDING',
    controller_entries=960,matrix_code_entries=80,direction_entries=20,constant_entries=20,
    source_label='81*a+localoffset; localoffset=x0+3*x1+9*x2+27*x3',
    ordered_clone_labels=837,new_label='15552+j',center_label='81*I[j//27]+j%3+9*(j//3%3)+27*(j//9%3)',
    plane='x1=0',simple_source_N_excludes_oldcenter=True,
    kernel_label_interface='Definitions label_old/label_new plus source encode/decode inverses PASS; no new837-center ASCII/parser theorem',
    source_affine_literal_binding_inherited=str((R/bound['source']).relative_to(R)),
    independent_actual837_fullN_binding=str((freshdir/'RESULT.json').relative_to(R)),
    large_graph_reads=0,BFS=0,old_field_rank_checks=0,Lean_ASCII_parser_claim=False,
    CPU_seconds=time.process_time()-started)
(D/'EXTERNAL_BINDING_PREPARATION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

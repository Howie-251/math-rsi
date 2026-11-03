"""Bind new Lean literals to author parameters and completed fresh small receipts.
This does not parse a graph or re-run the field, rank, diameter, or pencil checks.
"""
import ast,csv,json,re,time
from pathlib import Path
start=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
C=D.parent;F=R/'formal/DegreeDiameter/Portfolio'
author_path=R/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
author=json.loads(author_path.read_text());text=(F/'F4Graph1920Definitions.lean').read_text()
def array(name):
    match=re.search(r'^def '+name+r'\s*:[^\n]*:=\s*(.*)$',text,re.M)
    assert match,name
    return ast.literal_eval(match[1].replace('#[','['))
controllers=array('controllerData');pool=array('matrixPool');index=array('matrixIndex')
directions=array('directionData')
assert controllers==author['controller']
assert directions==author['outgoing_return_directions']
matrix_entries=0
for a in range(30):
    for p in range(4):
        expected=[v for row in author['matrices'][a][p] for v in row]
        assert pool[index[a][p]]==expected
        matrix_entries+=9
inddir=C/'independent_acceptance'
fresh=json.loads((inddir/'RESULT.json').read_text())
terminal=json.loads((inddir/'TERMINAL.json').read_text())
assert fresh['status']=='PASS_COMPLETE_LITERAL_D17_N2016_EXACT_D3'
assert fresh['source_full_body_bound_to_independent_actual_author_formula']
assert fresh['old_edges_retained_exact']==15360 and fresh['new_roles_bound']==96
rows=list(csv.DictReader((inddir/'ACTUAL_LITERAL_ROLE_BINDINGS.tsv').open(),delimiter='\t'))
assert len(rows)==96
layers=[0,3,5,7,9,16]
assert re.search(r'def layer[^\n]*:= !\[0,3,5,7,9,16\]',text)
labels=[];pins=[]
for j,row in enumerate(rows):
    a=(j%16)//4;b=j%4;layer=layers[j//16]
    center=64*layer+a+4*b+16*(a^b)
    assert {key:int(row[key]) for key in ['j','controller','a','b','source_center_label','new_label','literal_N_size']}==dict(
        j=j,controller=layer,a=a,b=b,source_center_label=center,new_label=1920+j,literal_N_size=16)
    assert row['actual_N_equal']=='True'
    actual=list(map(int,row['actual_parent_neighbors'].split()))
    assert len(actual)==16
    labels.append(center);pins.extend(actual)
assert len(set(pins))==1536
# These new label declarations will be checked by the kernel in CloneExact;
# they tie every ordered external row to the actual center function.
exact=F/'F4Graph1920CloneExact.lean';source=exact.read_text()
marker='theorem card_vertex'
if 'def orderedCenterLabelData' not in source:
    additions=('def orderedCenterLabelData : Array Nat := #'+repr(labels)+'\n'
      'theorem center_ordered_label : ∀j:Fin 96, (center j).val =\n'
      '    orderedCenterLabelData.getD j.val 0 := by decide +kernel\n'
      'theorem label_old (v : Fin 1920) : (label (.inl v)).val=v.val := rfl\n')
    assert marker in source
    exact.write_text(source.replace(marker,additions+marker,1))
result=dict(status='PASS_SMALL_EXTERNAL_LITERAL_AND_ORDERED_LABEL_BINDING',
    source_author_parameters=str(author_path.relative_to(R)),
    Lean_source='formal/DegreeDiameter/Portfolio/F4Graph1920Definitions.lean',
    exact_controller_entries=120,exact_matrix_code_entries=matrix_entries,exact_direction_entries=12,
    ordered_clone_rows=96,unique_original_pins=1536,new_label_formula='1920+j',
    clone_center_formula='64*I[j//16]+a+4*b+16*(a XOR b), a=(j%16)//4,b=j%4',
    fresh_source_full15360edge_binding_inherited=True,fresh_all96_fullN_binding_inherited=True,
    inherited_fresh_result=str((inddir/'RESULT.json').relative_to(R)),
    inherited_fresh_terminal=str((inddir/'TERMINAL.json').relative_to(R)),
    whole_graph_reads=0,BFS_runs=0,old_field_rank_pencil_runs=0,
    Lean_ASCII_edge_parser_theorem=False,
    center_ordered_label_kernel_status='PENDING_NEW_CLONE_EXACT_COMPILATION',
    CPU_seconds=time.process_time()-start)
(D/'EXTERNAL_BINDING_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

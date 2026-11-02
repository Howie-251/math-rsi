import ast,csv,json,re,time
from pathlib import Path
started=time.process_time()
D=Path(__file__).resolve().parent; C=D.parent;G=C.parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
P=R/'formal/DegreeDiameter/Portfolio'
def rel(p):return str(p.relative_to(R))
params=json.loads((C/'PARAMETERS.json').read_text())
fresh=json.loads((C/'independent_acceptance/RESULT.json').read_text())
terminal=json.loads((C/'independent_acceptance/TERMINAL.json').read_text())
old=json.loads((G/'degree16_plane837/formalization_full/EXTERNAL_BINDING_RESULT.json').read_text())
assert old['status'].startswith('PASS_')
assert fresh['status']=='PASS_COMPLETE_LITERAL_AND_ALL16416_FINAL_ROOTS_EXACT_D4'
assert terminal['all_processes_terminal'] and not terminal['running']
definition=(P/'F3Graph15552Clone16416Definitions.lean').read_text()
typed=ast.literal_eval(re.search(r'def layerData : Array Nat := #(.*?)\ndef layer',definition,re.S).group(1))
selected=json.loads((G/'controller_pack32_gate/SELECTED_BLOCKS.json').read_text())['selected_controllers']
assert typed==selected==params['selected_controller_labels']==fresh['selected_I32_controllers']
assert params['source_n']==15552 and params['source_m']==116316
assert params['n']==fresh['n']==16416 and params['m']==fresh['m']==129240
assert params['no_newclone_label_refilter'] and fresh['all_virtualself_entries_excluded_at_oldcenter']
assert fresh['all_source_edges_retained_exact']==116316 and fresh['maximum_old_pin_load']==1
def rows(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
actual=rows(C/'independent_acceptance/ALL864_ACTUAL_ROLE_BINDINGS.tsv')
producer=rows(C/'ALL864_ROLE_BINDINGS.tsv')
assert len(actual)==len(producer)==864
pins=0;hist={}
for j,(a,b) in enumerate(zip(actual,producer)):
    oi=j%27; offset=oi%3+9*(oi//3%3)+27*(oi//9%3)
    center=81*typed[j//27]+offset
    assert int(a['j'])==int(b['j'])==j
    assert int(a['controller'])==int(b['controller'])==typed[j//27]
    assert int(a['offset'])==offset and int(b['local_offset'])==offset
    assert int(a['old_center_label'])==int(b['source_center_label'])==center
    assert int(a['new_label'])==int(b['new_label'])==15552+j
    na=[int(x) for x in a['actual_old_simple_neighbors'].split()]
    nb=[int(x) for x in b['frozen_full_source_N'].split()]
    degree=int(a['actual_simple_N_size'])
    assert na==nb and len(na)==degree==int(a['actual_edge_count'])==int(b['literal_source_degree'])
    assert a['full_N_equal']==a['old_center_excluded']=='true'
    assert center not in na and all(0<=v<15552 for v in na)
    pins+=degree;hist[str(degree)]=hist.get(str(degree),0)+1
assert pins==12924 and hist=={'14':36,'15':828}
result=dict(status='PASS_NEW_TYPED_I32_LABELS_AND_FRESH864_LITERAL_FULL_NEIGHBORHOODS',
    inherited_source_binding=rel(G/'degree16_plane837/formalization_full/EXTERNAL_BINDING_RESULT.json'),
    source_reuse_boundary='Only fixed literal source15552 and its typed affine label binding are inherited; no old clone16389 graph PASS is used for this target.',
    source_literal=params['source_literal'],source_type='Fin 15552',clone_type='Fin 15552 ⊕ Fin 864',label_target='Fin 16416',
    typed_I32_equal_producer_and_independent=True,ordered_role_rows=864,ordered_pins=12924,
    old_edges_retained=116316,new_edges=12924,newnew_edges=0,
    source_label='81*a+x0+3*x1+9*x2+27*x3',
    center_label='81*I32[j//27]+j%3+9*(j//3%3)+27*(j//9%3)',new_label='15552+j',
    kernel_label_theorems=['Clone16416.label_old','Clone16416.label_new','Clone16416.center_label'],
    kernel_load_theorems=['Clone16416.owner_forward','Clone16416.pinOwner_forward','Clone16416.common_pin_index_unique','Clone16416.load_le_one'],
    independent_receipt=rel(C/'independent_acceptance/RESULT.json'),
    independent_terminal=rel(C/'independent_acceptance/TERMINAL.json'),
    independent_actual_role_table=rel(C/'independent_acceptance/ALL864_ACTUAL_ROLE_BINDINGS.tsv'),
    external_boundary='This is a small external equality/ordered-recipe binding, not a Lean ASCII parser theorem or #eval of the864 external rows.',
    old_field_rank_rechecks=0,large_graph_reads=0,BFS=0,old_Lean_recompiles=0,
    CPU_seconds=time.process_time()-started)
(D/'EXTERNAL_BINDING_RESULT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':result['status'],'rows':864,'pins':pins,'CPU_seconds':result['CPU_seconds']}))

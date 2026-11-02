import csv,json,time
from collections import Counter
from pathlib import Path
started=time.process_time()
D=Path(__file__).resolve().parent;P=D.parent.parent
parent=json.loads((P/'formalization/FINAL.json').read_text())
assert parent['status'].endswith('_PASS')
base=json.loads((P/'multiplicity2_degree83/formalization/EXTERNAL_INPUT_BINDING.json').read_text())
assert base['status']=='PASS_ALL_NEW_ROLE_CENTER_AND_NEW_LABEL_BINDINGS'
templates=P/'multiplicity9_13_independent_acceptance/PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv'
sizes={}
with templates.open()as f:
    for row in csv.DictReader(f,delimiter='\t'):
        h=int(row['role']);assert h==len(sizes)and 0<=h<4226
        assert int(row['source_center_label'])==342290+h
        sizes[h]=int(row['Nsize'])
assert len(sizes)==4226 and Counter(sizes.values())==Counter({65:1,80:65,81:4160})
assert sizes[4225]==65
results=[]
for cap,r,n,directory in [(90,8,380324,'multiplicity9_degree90'),(94,12,397228,'multiplicity13_degree94')]:
    case=P/directory;fresh=json.loads((case/'independent_acceptance/RESULT.json').read_text())
    assert fresh['status']=='PASS'and fresh['source_is_actual_G1_not83']
    assert fresh['parent_edges_retained_exact']==14204970 and fresh['new_roles_bound']==r*4226
    assert fresh['source_role_N_pairwise_disjoint']and fresh['source_role_N_union']==342225
    assert fresh['additional_blocks']==r and fresh['max_new_load']==r
    count=0
    with(case/'independent_acceptance/ALL_NEW_ROLE_BINDINGS.tsv').open()as f:
        for row in csv.DictReader(f,delimiter='\t'):
            j=int(row['j']);b=int(row['copy']);h=int(row['role'])
            assert j==count and 0<=b<r and 0<=h<4226 and j==4226*b+h
            assert int(row['source_center_label'])==342290+h
            assert int(row['new_label'])==346516+j
            assert int(row['literal_N_size'])==int(row['actual_edge_count'])==sizes[h]
            assert row['complete_parent_N_equal']=='true'
            assert int(row['actual_parent_N_template_row'])==h
            if h<4225:
                i,s=divmod(h,65)
                assert h==65*i+s and 0<=i<65 and 0<=s<65
            else:assert h==4225
            count+=1
    assert count==r*4226
    result=dict(status='PASS_ALL_TYPED_COPY_ROLE_AND_PHYSICAL_LABEL_BINDINGS',degree=cap,r=r,
        target=f'DegreeDiameter.Portfolio.Q8DiagonalFill{cap}.d{cap}_{n}',
        row_count=count,base_role_template_rows=4226,source='frozen G1/346516, never83',
        source_center_formula='342290+h',copy_formula='j=4226*b+h',new_label_formula='346516+j',
        role_expansion='h=65*i+j for first clones; h4225 is first hub',
        source_center_and_label_theorems=f'Q8DiagonalFill{cap}.source_center_label/copy_label/label_new/label_copy/label_hub',
        parent_typed_role_binding_inherited=True,
        fresh_result=str(case/'independent_acceptance/RESULT.json'),
        literal_complete_N_binding_inherited_from_actual_fresh_acceptance=True,
        literal_fullN_binding_method=fresh['binding_method'],
        all_G1_body_edges_exact=fresh['parent_edges_retained_exact'],
        actual_new_BFS_roots=fresh['actual_lastblock_new_BFS_roots'],
        unmeasured_new_roots=fresh['unmeasured_new_roots'],
        allpair_and_prefix_genuine_Walk_proof=True,
        large_graph_reads=0,BFS=0,field_geometry_finite_rechecks=0,
        Lean_ASCII_parser_claim=False,Audit_eval_all_rows_claim=False)
    (case/'formalization/EXTERNAL_INPUT_BINDING.json').write_text(json.dumps(result,indent=2)+'\n')
    results.append(result)
report=dict(status='BOTH_TARGETS_ALL84520_TYPED_NEW_ROLE_LABEL_ROWS_BOUND',
    CPU_seconds=time.process_time()-started,total_rows=sum(x['row_count']for x in results),cases=results,
    large_graph_reads=0,BFS=0,old_geometry_field_finite_rechecks=0,
    Lean_ASCII_parser_claim=False,old_PASSED_modules_recompiled=False)
(D/'EXTERNAL_INPUT_BINDING.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(status=report['status'],CPU_seconds=report['CPU_seconds'],total_rows=report['total_rows'])))

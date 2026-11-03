import csv,json,time
from pathlib import Path
D=Path(__file__).resolve().parent;P=D.parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());BASE=R/'research/ddp/two_successful_methods_20261101/retained_edge_transfer'
parent=json.loads((BASE/'diagonal_fill_reallocation_formalization/Q8_FINAL.json').read_text());assert parent['status'].endswith('_PASS')
typed=json.loads((BASE/'even_q8_gq_source80_81/balanced_full_ovoid_copy82/formalization/EXTERNAL_INPUT_BINDING.json').read_text());O=typed['actual_ovoid_ids']
w=list(map(int,(BASE/'even_q8_gq_source80_81/balanced/TABLES_INPUT.txt').read_text().split()));at=10+585*9+585*9;spread=w[at:at+65]
fresh=json.loads((P/'independent_acceptance/RESULT.json').read_text());assert fresh['status']=='PASS'and fresh['accepted346516_oldbody_exact']==14204970 and fresh['all8450_both_block_original_U_N_bindings']
seen=[set(),set()]
with(P/'independent_acceptance/ALL_8450_BOTH_BLOCK_TRUE_U_N_BINDINGS.tsv').open()as f:
 for row in csv.DictReader(f,delimiter='\t'):
  copy=int(row['copy']);h=int(row['h']);i,j=divmod(h,65)
  assert copy in(0,1)and h not in seen[copy]and 0<=h<4225;seen[copy].add(h)
  assert int(row['ovoid_index'])==i and int(row['spread_index'])==j
  assert int(row['center'])==585*O[i]+spread[j]
  assert int(row['clone'])==(342290+h if copy==0 else 346516+h)
assert seen[0]==seen[1]==set(range(4225))
params=json.loads((P/'PARAMETERS.json').read_text());assert(params['source_n'],params['first_hub'],params['second_hub'])==(346516,346515,350741)
hub=json.loads((P/'independent_acceptance/HUB_CLONE_STRUCTURE_WITNESS.json').read_text());assert hub['literal_hub_neighbors_only_F']and hub['literal_clone_neighbors_only_U']
result=dict(status='PASS_ALL_NEW_ROLE_CENTER_AND_NEW_LABEL_BINDINGS',CPU_seconds=time.process_time(),source_graph='actual accepted346516 G1',role_center_rows=4226,clone_rows_linked=8450,source_role_labels='342290+h,h0..4225',new_role_labels='346516+h,h0..4225',new_hub=350741,source_hub=346515,full_new_role_N_binding_inherited_from_fresh_both_blocks_and_hub=True,old_k1_typed_label_binding_inherited=True,large_graph_reads=0,BFS=0,field_geometry_projection_new_finite_checks=0,Lean_ASCII_parser_claim=False)
(D/'EXTERNAL_INPUT_BINDING.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

import csv,json,re,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());B=D.parent/'opposite_gq44_spread25';P=B/'ovoid_product26/diagonal_fill_reallocation'
old=(R/'formal/DegreeDiameter/Portfolio/OvoidProduct26Definitions.lean').read_text()
O=list(map(int,re.findall(r'\d+',old.split('def ovoid',1)[1].split(':= ![',1)[1].split(']',1)[0])))
assert len(O)==17
params=json.loads((B/'PARAMETERS.json').read_text());spread=params['spread_line_labels'];owners=params['point_spread_owner'];lp=[row['points']for row in params['lines']]
code=(R/'formal/DegreeDiameter/Portfolio/Q4DiagonalFillDefinitions.lean').read_text();payload=int(re.search(r'def coverPayload : Nat := (\d+)',code)[1]);slots=[(payload//16**p)%16%5 for p in range(85)]
assert slots==json.loads((D/'Q4_BRIDGE_INPUT.json').read_text())['cover_slots']
assert all(lp[spread[owners[p]]][slots[p]]==p for p in range(85))
fresh=json.loads((P/'independent_acceptance/RESULT.json').read_text());assert fresh['status']=='PASS'
count=0;diagonal=0
with(P/'independent_acceptance/ALL_289_CLONE_BINDINGS.tsv').open()as f:
 for row in csv.DictReader(f,delimiter='\t'):
  idx=int(row['index']);i,j=divmod(idx,17);assert idx==count
  assert int(row['point'])==O[i]and int(row['spread_index'])==j
  assert int(row['center'])==85*O[i]+spread[j]and int(row['clone'])==7242+idx
  diag=row['diagonal']=='True';assert diag==(owners[O[i]]==j)
  assert int(row['pin_count'])==(24 if diag else 25)
  if diag:assert int(row['deleted_filler'])==7225+j;diagonal+=1
  count+=1
assert count==289 and diagonal==17
result=dict(status='PASS_ACTUAL_TYPED_CENTER_ORDER_NEW_LABELS_HUB_AND_COVER_PAYLOAD_BINDING',CPU_seconds=time.process_time(),case='Q4',clone_rows=count,diagonal_rows=diagonal,cover_slots=85,source_ovoid_ids=O,center_formula='85*O[i]+S[j]',new_clone_label='7242+17*i+j',hub=7531,label_target='Fin7532',fresh_full_U_pin_binding_inherited=True,large_graph_reads=0,BFS=0,old_field_geometry_projection_rechecks=0,Lean_ASCII_parser_theorem_claimed=False)
(D/'Q4_EXTERNAL_INPUT_BINDING.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

import csv,json,re,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());B=D.parent/'even_q8_gq_source80_81';P=B/'balanced_full_ovoid_copy82/diagonal_fill_reallocation'
old=json.loads((B/'balanced_full_ovoid_copy82/formalization/EXTERNAL_INPUT_BINDING.json').read_text());assert old['status'].startswith('PASS_');O=old['actual_ovoid_ids']
code=(R/'formal/DegreeDiameter/Portfolio/Q8DiagonalFillDefinitions.lean').read_text();assert 'abbrev ovoid := EvenQ8BalancedFullOvoidCopy82.ovoid'in code
w=list(map(int,(B/'balanced/TABLES_INPUT.txt').read_text().split()));np,nl,a,b,j=w[:5];at=10;lp=[w[at+k*a:at+(k+1)*a]for k in range(nl)];at+=nl*a+np*b;spread=w[at:at+j];owner=w[at+j:at+j+np]
payload=int(re.search(r'def coverPayload : Nat := (\d+)',code)[1]);slots=[(payload//16**p)%16%9 for p in range(585)];assert slots==json.loads((D/'Q8_BRIDGE_INPUT.json').read_text())['cover_slots'];assert all(lp[spread[owner[p]]][slots[p]]==p for p in range(585))
fresh=json.loads((P/'independent_acceptance/RESULT.json').read_text());assert fresh['status']=='PASS'and fresh['all4225_true_U_clone_neighborhoods_bound']
count=0;diagcount=0
with(P/'independent_acceptance/ALL_4225_TRUE_U_N_BINDINGS.tsv').open()as f:
 for row in csv.DictReader(f,delimiter='\t'):
  h=int(row['h']);i,j=divmod(h,65);assert h==count and int(row['ovoid_index'])==i and int(row['spread_index'])==j
  assert int(row['center'])==585*O[i]+spread[j]and int(row['newlabel'])==342290+h
  diagonal=bool(int(row['diagonal']));assert diagonal==(owner[O[i]]==j)
  assert int(row['pin_count'])==(80 if diagonal else 81)
  diagcount+=diagonal;count+=1
assert count==4225 and diagcount==65
with(P/'independent_acceptance/EXACT_65_REMOVED_65_ADDED.tsv').open()as f:delta=list(csv.DictReader(f,delimiter='\t'))
added={(int(row['u']),int(row['v']))for row in delta if row['operation']=='added'};removed={(int(row['u']),int(row['v']))for row in delta if row['operation']=='removed'}
assert added=={(342225+j,346515)for j in range(65)}
assert removed=={(342225+owner[O[i]],342290+65*i+owner[O[i]])for i in range(65)}
result=dict(status='PASS_ACTUAL_TYPED_CENTERS_LABELS_HUB_AND_COVER_PAYLOAD',CPU_seconds=time.process_time(),case='Q8',clone_rows=count,diagonal_rows=diagcount,cover_slots=585,typed_ovoid_binding_inherited=True,center_formula='585*O[i]+S[j]',clone_label='342290+65*i+j',hub=346515,label='Fin346516',fresh_all_raw_U_pin_binding_inherited=True,large_graph_reads=0,BFS=0,old_field_geometry_projection_rechecks=0,Lean_ASCII_parser_theorem_claimed=False)
(D/'Q8_EXTERNAL_INPUT_BINDING.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

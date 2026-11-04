import json,hashlib,pathlib
P=pathlib.Path(__file__).resolve().parent
j=lambda n:json.loads((P/n).read_text(encoding='utf-8-sig'))
h=lambda n:hashlib.sha256((P/n).read_bytes()).hexdigest()
# Reconcile independent legacy text tables against the four source-bound packed sets.
odd=[x for x in range(32) if x.bit_count()%2]
for typ in ('T26','T15','T17','T63'):
 converted=set()
 for line in (P/f'HIGHER_Q5_FULL_REUSE_REVIEW_{typ}.txt').read_text().splitlines():
  m,J,O=map(int,line.split())
  if typ=='T26':
   delta=(m^1).bit_length()-1
   jm=sum(((J>>x)&1)<<i for i,x in enumerate(odd));om=sum(((O>>x)&1)<<i for i,x in enumerate(odd))
   converted.add(delta|(jm<<5)|(om<<21))
  elif typ=='T63':converted.add(J|(O<<32))
  else:converted.add(O|((J&~O)<<32))
 assert converted==set(map(int,(P/f'HIGHER_Q5_FULL_{typ}_lookup.txt').read_text().split())),typ
 print(typ,'legacy reconciliation',len(converted))
# Every formal review import is bound to its present direct reviewed sources.
cat=j('FOURTEEN_REUSE_catalog.json');gates=list(cat['gate_hashes'])+['HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json','TWELVE_HOLE_FULL_REVIEW.json']
checks=0
for n in gates:
 r=j(n);assert r['verdict']=='PASS',n
 for f,expected in r['audited_input_hashes'].items():
  path=P/f
  assert path.exists(),(n,f)
  assert hashlib.sha256(path.read_bytes()).hexdigest()==expected.removeprefix('sha256:'),(n,f)
  checks+=1
print('formal direct source hashes',checks)
res1=j('FOURTEEN_REUSE_REVIEW_application_result.json');res2=j('FOURTEEN_CACHED_REVIEW_application_result.json');loc=j('FOURTEEN_CACHED_REVIEW_local_result.json')
assert (res1['input'],res1['positive'],res1['remaining'])==(9484443,9436232,48211)
assert (res2['input'],res2['positive'],res2['remaining'],res2['hits'])==(48211,35665,12546,278524)
assert (loc['rows_checked'],loc['forests_checked'],loc['connectivity_bits_checked'])==(20,38912,77594624)
scopes={n:j(n).get('summary','') for n in gates}
base={'audit_skill':'proof-checker','verdict':'PASS','reviewer_agent_id':'/root/fourteen_reuse_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high','model_override_source':'Explicit user route relayed by parent overrides skill default','executor_family':'openai','reviewer_family':'openai','review_independence':'same-family','acceptance_status':'provisional','formalization':'No Lean or cross-family formal acceptance','generated_at':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat()}
for stage,res in [('REUSE',res1),('CACHED',res2)]:
 manifest=j(f'FOURTEEN_{stage}_MANIFEST.json')
 names=set(manifest['input_hashes'])|set(manifest['output_hashes'])|{f'FOURTEEN_{stage}_MANIFEST.json', 'FOURTEEN_REVIEW_prepare.py','FOURTEEN_REVIEW_application_check.cpp','FOURTEEN_REVIEW_import_check.py'}|set(gates)
 names|={f'HIGHER_Q5_FULL_REUSE_REVIEW_{t}.txt' for t in ('T26','T15','T17','T63')}
 names|={'Q5_T17_RANK_BATCH_PROOF.md','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md'}
 if stage=='CACHED':names|={'FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW_local_check.cpp','FOURTEEN_CACHED_REVIEW_geometries.txt','FOURTEEN_CACHED_REVIEW_local_result.json','FOURTEEN_CACHED_REVIEW_all_registry.txt','FOURTEEN_CACHED_REVIEW_selected_registry.txt'}
 else:names.add('FOURTEEN_REUSE_REVIEW_registry.txt')
 names.add(f'FOURTEEN_{stage}_REVIEW_application_result.json')
 names.add(f'FOURTEEN_{stage}_REVIEW.md')
 r=dict(base,reason_code='all_exact_marked_local_and_actual_application_obligations_closed_modulo_explicit_accepted_imports',summary=('Accepted-registry fourteen-hole application verifies all9436232 positive witnesses and48211 exact exhaustive residuals.' if stage=='REUSE' else 'Twenty new exact local universal inputs and complete actual cached application PASS;35665 positives leave12546 exact residuals. Full14/P6 remain open.'),trace_path=f'FOURTEEN_{stage}_REVIEW.md',audited_input_hashes={n:h(n) for n in sorted(names)},formal_imports=[{'file':n,'sha256':h(n),'actual_scope':scopes[n]} for n in gates],details={'issues':[],'source_reduction_conditional_on_full_twelve_hole':False,'full_twelve_hole_predecessor_gate':'TWELVE_HOLE_FULL_REVIEW.json','full_twelve_hole_predecessor_sha256':h('TWELVE_HOLE_FULL_REVIEW.json'),'full_twelve_hole_proved':True,'full_fourteen_hole_proved':False,'full_P6_proved':False,'remaining_covered_target_geometries':47893 if stage=='REUSE' else 12528,'remaining_free_target_geometries':318 if stage=='REUSE' else 18,'all_positive_witnesses_independently_replayed':True,'exact_raw_residual_partition':True,'every_realizing_original_short_matching_quantifier':True,'formal_import_direct_source_hash_comparisons':checks,'producer_or_RUN_STATE_modified':False,'finite_application':res})
 if stage=='CACHED':r['details'].update(selected_local_inputs=20,local_certificate_checks=loc,selected20_candidate403_geometry_predicate_unions_equal=True,nonselected383_local_rank_inputs_required=False,all_hit_witnesses_checked=278524,chosen_witnesses_checked=35665);r['accepted_marked_inputs']=[{'index':g['local_id'],'family':g['family'],'prefix':g['prefix'],'type':g['type'],'minority':g['minority'],'majority':g['majority'],'omitted':g['omitted'],'local_independently_accepted':True} for g in j('FOURTEEN_CACHED_greedy_registry.json')['rows']]
 (P/f'FOURTEEN_{stage}_REVIEW.json').write_text(json.dumps(r,indent=2)+'\n')
print('reports JSON written')

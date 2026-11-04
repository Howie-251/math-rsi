from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).resolve().parent
read=lambda n:json.loads((P/n).read_text())
sha=lambda n:hashlib.sha256((P/n).read_bytes()).hexdigest()
cat=read('FOURTEEN_CACHED_catalog.json');scan=read('FOURTEEN_CACHED_result.json');greedy=read('FOURTEEN_CACHED_greedy_registry.json')
assert sha('FOURTEEN_REUSE_MANIFEST.json')==cat['source_manifest_sha256']
inputs={'FOURTEEN_REUSE_MANIFEST.json':sha('FOURTEEN_REUSE_MANIFEST.json'),**cat['input_summary_hashes'],**{n:r['sha256'] for n,r in cat['sources'].items()}}
cert=[]
for r in greedy['rows']:
 pre=r['prefix']
 for suffix in ['.json','_config.txt','_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin']:
  name=pre+suffix;assert (P/name).exists(),name;inputs[name]=sha(name);cert.append(name)
outputs=['FOURTEEN_CACHED_prepare.py','FOURTEEN_CACHED_catalog.json','FOURTEEN_CACHED_registry.txt','FOURTEEN_CACHED_scan.cpp','FOURTEEN_CACHED_scan.exe','FOURTEEN_CACHED_result.json','FOURTEEN_CACHED_greedy.py','FOURTEEN_CACHED_greedy_registry.json','FOURTEEN_CACHED_PROOF.md','FOURTEEN_CACHED_freeze.py']
for r in scan['reports']:
 tag=f"h14_v{r['v']}_{'free' if r['free_target'] else 'covered'}"
 for kind in ['all_hits','selected_witness','remaining']:
  n=f'FOURTEEN_CACHED_{kind}_{tag}.bin';assert (P/n).exists();outputs.append(n)
 assert (P/f'FOURTEEN_CACHED_selected_witness_{tag}.bin').stat().st_size==28*r['candidate_covered']
 assert (P/f'FOURTEEN_CACHED_remaining_{tag}.bin').stat().st_size==13*r['remaining']
manifest={'status':'PRODUCER_CACHED_CANDIDATE_APPLICATION_AND_TWENTY_LOCAL_INPUTS_PENDING_FRESH_REVIEW','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'holes':14,'input':48211,'candidate_covered':35665,'remaining':12546,'remaining_covered':12528,'remaining_free':18,'selected_local_inputs':20,'selected_codes':greedy['selected_codes'],'selected_type_counts':greedy['selected_type_counts'],'new_local_forest_checks_needed':38912,'new_local_connectivity_bits_needed':77594624,'local_inputs_accepted':False,'independent_application_acceptance':False,'source_first_stage_application_gate_pending':True,'source_reduction_conditional_on_full_twelve_hole':True,'reports':scan['reports'],'input_hashes':inputs,'output_hashes':{n:sha(n) for n in outputs},'output_sizes':{n:(P/n).stat().st_size for n in outputs},'full_twelve_hole_proved':False,'full_fourteen_hole_proved':False,'full_P6_proved':False,'production_or_main_state_modified':False}
for n,h in inputs.items():assert sha(n)==h,n
(P/'FOURTEEN_CACHED_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'manifest_sha256':sha('FOURTEEN_CACHED_MANIFEST.json'),'proof_sha256':sha('FOURTEEN_CACHED_PROOF.md'),'selected_certificate_files':len(cert),'input_hash_count':len(inputs),'output_hash_count':len(outputs),'candidate_covered':35665,'remaining':12546},indent=2))

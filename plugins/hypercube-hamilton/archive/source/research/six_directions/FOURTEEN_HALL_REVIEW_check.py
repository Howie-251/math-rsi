"""Fresh direct Hall-neighborhood/partition audit, no producer code imported."""
import collections,hashlib,json,pathlib,struct
R=pathlib.Path(__file__).resolve().parent
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
manifest=read('FOURTEEN_HALL_MANIFEST.json')
assert sha('FOURTEEN_HALL_PROOF.md')=='bdd7d357556cd0eb7a66d4dcab21b0e860754092c5ec6e957e64af27124f0fa4'
for n,v in manifest['files'].items():assert sha(n)==v['sha256'] and (R/n).stat().st_size==v['bytes'],n
gates=['HIGHER_Q5_FULL_REVIEW.json','TWELVE_HOLE_FULL_REVIEW.json','FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW.json']
expected={'FOURTEEN_REUSE_REVIEW.json':'5ef0a4a66f55b37ef150dff76eabc4fa1d009224a66f27e0e927aa4636b44027','FOURTEEN_CACHED_REVIEW.json':'bcb5a06d7b76467717b45ae1e7bafb415b30d00d2cc4e313f78e7c863847eef8'}
checked={};bindings={}
for n in gates:
 d=read(n);assert d['verdict']=='PASS';bindings[n]=sha(n)
 if n in expected:assert sha(n)==expected[n]
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for k,v in d.get(field,{}).items():
   if k not in checked:checked[k]=sha(k)
   assert checked[k]==v.removeprefix('sha256:'),(n,field,k)
assert read('TWELVE_HOLE_FULL_REVIEW.json')['details']['full_twelve_hole_proved']
assert read('HIGHER_Q5_FULL_REVIEW.json')['details']['residual_totals']['14']['free']==232042
for n in gates[2:]:
 d=read(n)['details'];assert not d['source_reduction_conditional_on_full_twelve_hole'] and d['every_realizing_original_short_matching_quantifier'] and d['exact_raw_residual_partition']
 assert d['full_twelve_hole_predecessor_sha256']==bindings['TWELVE_HOLE_FULL_REVIEW.json']
assert read('FOURTEEN_CACHED_REVIEW.json')['audited_input_hashes']['FOURTEEN_REUSE_REVIEW.json']==bindings['FOURTEEN_REUSE_REVIEW.json']
even={x for x in range(64) if x.bit_count()%2==0};odd=set(range(64))-even
sources={};holes={};raws={};chain=[]
for v in (1,7,31):
 for free,status in enumerate(['covered','free']):
  key=(v,free);n=f'FOURTEEN_CACHED_remaining_h14_v{v}_{status}.bin';raw=(R/n).read_bytes();assert len(raw)%13==0
  assert read('FOURTEEN_CACHED_REVIEW.json')['audited_input_hashes'][n]==sha(n)
  records=[raw[j:j+13] for j in range(0,len(raw),13)];assert len(records)==len(set(records));sources[key]=records;raws[key]=raw;holes[key]=[]
  for rec in records:
   z=list(rec[:6]);w=list(rec[6:]);assert z==sorted(set(z)) and w==sorted(set(w)) and len(z)==6 and len(w)==7
   assert set(z)<even and 0 not in z and set(w)<=odd and ((v in w)==bool(free))
   assert all((x^y).bit_count()!=1 for x in z for y in w)
   if free:assert all(y.bit_count()!=1 for y in w)
   H={0,*z,*w};E=even-H;O=odd-H;assert len(H)==14 and len(E)==len(O)==25;holes[key].append((E,O))
  # Source streams at each accepted interface are bound in both adjacent gates.
  prev=f'FOURTEEN_REUSE_remaining_h14_v{v}_{status}.bin'
  assert read('FOURTEEN_REUSE_REVIEW.json')['audited_input_hashes'][prev]==sha(prev)
  assert read('FOURTEEN_CACHED_REVIEW.json')['audited_input_hashes'][prev]==sha(prev)
  initial=f'HIGHER_Q5_FULL_residual_h14_v{v}_{status}.bin'
  assert read('HIGHER_Q5_FULL_REVIEW.json')['audited_input_hashes'][initial]==sha(initial)
  assert read('FOURTEEN_REUSE_REVIEW.json')['audited_input_hashes'][initial]==sha(initial)
  chain.append({'v':v,'free':free,'initial':(R/initial).stat().st_size//13,'reuse_remaining':(R/prev).stat().st_size//13,'cached_remaining':len(records)})
removed=collections.defaultdict(set);hist=collections.Counter();witness=(R/'FOURTEEN_HALL_witnesses.bin').read_bytes();assert len(witness)%22==0
for v,free,i,Sm,Tm in struct.iter_unpack('<BBIQQ',witness):
 key=(v,free);assert key in sources and i<len(sources[key]) and i not in removed[key]
 E,O=holes[key][i];S={x for x in range(64) if Sm>>x&1};T={x for x in range(64) if Tm>>x&1}
 assert S and S<=E
 actual={x^(1<<d) for x in S for d in range(6)}&O
 assert T==actual and len(T)<len(S)
 removed[key].add(i);hist[f'{len(S)}:{len(T)}']+=1
reports=[]
for key,records in sources.items():
 v,free=key;status='free' if free else 'covered';remain=b''.join(rec for i,rec in enumerate(records) if i not in removed[key]);n=f'FOURTEEN_HALL_remaining_v{v}_{status}.bin'
 assert remain==(R/n).read_bytes(),n
 reports.append({'v':v,'free':free,'input':len(records),'Hall_excluded':len(removed[key]),'remaining':len(remain)//13,'remaining_sha256':sha(n)})
assert sum(x['input'] for x in reports)==12546 and sum(x['Hall_excluded'] for x in reports)==8623
assert [x['remaining'] for x in reports]==[840,0,1188,0,1895,0]
assert sum(x['initial'] for x in chain if x['free'])==232042
assert sum(x['reuse_remaining'] for x in chain if x['free'])==318
assert sum(x['cached_remaining'] for x in chain if x['free'])==18
out={'status':'PASS','manifest_bound_files_rehashed':len(manifest['files']),'formal_gate_source_bindings_rehashed':len(checked),'formal_gate_hashes':bindings,'all_source_records_legal_and_unique':True,'source_records_checked':12546,'Hall_certificates_verified':len(witness)//22,'Hall_size_histogram':dict(hist),'all_S_nonempty_covered_even':True,'all_T_exact_entire_covered_neighbor_sets':True,'all_strict_Hall_deficiencies':True,'all_witness_indices_unique_and_in_range':True,'all_six_remaining_streams_byte_exact':True,'reports':reports,'free_chain':chain,'fourteen_hole_free_targets_proved':True,'remaining_covered_target_geometries':3923,'remaining_free_target_geometries':0,'full_fourteen_hole_proved':False,'full_P6_proved':False,'producer_code_executed':False,'production_or_state_modified':False}
(R/'FOURTEEN_HALL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))

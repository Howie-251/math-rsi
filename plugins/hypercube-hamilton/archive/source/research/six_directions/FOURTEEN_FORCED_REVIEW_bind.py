import hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
expected={'FOURTEEN_FORCED_PROOF.md':'1b6c96f21cd7b3c36be3ffddbcf0a88e839df59f2222f12e62e4cdfba9b74873','FOURTEEN_FORCED_APPLICATION.md':'2bb6975e6992475ecbcc95b6e60603f24fffeeac204707b74de677a681d2d25a','FOURTEEN_FORCED_MANIFEST.json':'2d995aab73f5aea810ffd8dccf503ce0353599cc56cb700e317c247280162f03'}
for n,h in expected.items():assert sha(n)==h
m=read('FOURTEEN_FORCED_MANIFEST.json')
for n,h in m['hashes'].items():assert sha(n)==h and (R/n).stat().st_size==m['sizes'][n],n
checked={};gates={}
for n in m['hashes']:
 if n.endswith('_REVIEW.json'):
  d=read(n);assert d['verdict']=='PASS';gates[n]=sha(n)
  for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
   for k,v in d.get(field,{}).items():
    if k not in checked:checked[k]=sha(k)
    assert checked[k]==v.removeprefix('sha256:'),(n,k)
hall=read('FOURTEEN_HALL_REVIEW.json');assert hall['details']['fourteen_hole_free_targets_proved'] and hall['details']['remaining_covered_target_geometries']==3923
for v in (1,7,31):
 n=f'FOURTEEN_HALL_remaining_v{v}_covered.bin';assert sha(n)==hall['audited_input_hashes'][n]
generic=read('HIGHER_FORCED_CHERRY_REVIEW.json')['details']
assert generic['local_criterion']=='labeled F+R acyclic' and generic['automatic_gap']=='j<=floor(c/2)<d'
assert generic['root_excluded_from_R'] and generic['R_endpoints_same_parity_as_Y'] and generic['universal_forced_R_required']
# Independent arithmetic pressure on the automatic-gap lemma, complementing
# the complete symbolic proof imported from the accepted generic transfer.
gapcases=0
for c in range(1,33):
 for s in (3,4,5):
  for delta in (0,1):
   num=c+s-(1-delta)
   if num%2:continue
   assert num//2>c//2
   for j in range(c//2+1):assert num//2>j;gapcases+=1
out={'status':'PASS','frozen_hashes':expected,'manifest_files_verified':len(m['hashes']),'formal_PASS_gates':gates,'formal_direct_source_bindings_verified':len(checked),'source_Hall_gate_and_all_three_raw_outputs_bound':True,'fourteen_hole_free_targets_proved':True,'automatic_gap_arithmetic_cases':gapcases,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_FORCED_REVIEW_bind.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))

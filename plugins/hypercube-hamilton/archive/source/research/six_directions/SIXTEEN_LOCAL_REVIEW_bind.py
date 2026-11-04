import hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
expected={'SIXTEEN_LOCAL_PROOF.md':'cfeb0b77395b7bde03933ca6aebe8d544bca7196d0111e2447d592d232bbeb85','SIXTEEN_LOCAL_APPLICATION.md':'61a4cdd922e737e4c9cf5c67506a236ede1adbb6e0a4580fff41e41d567e8c0d','SIXTEEN_LOCAL_MANIFEST.json':'f72ed41d6a71c8634c287fa3078abd81fc95a293ec227eb196babd9ef34d6e6e'}
for n,h in expected.items():assert sha(n)==h
m=read('SIXTEEN_LOCAL_MANIFEST.json')
for n,h in m['hashes'].items():assert sha(n)==h and (R/n).stat().st_size==m['sizes'][n],n
checked={};gates={}
for n in m['hashes']:
 if n.endswith('_REVIEW.json'):
  d=read(n);assert d['verdict']=='PASS';gates[n]=sha(n)
  for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
   for k,v in d.get(field,{}).items():
    if k not in checked:checked[k]=sha(k)
    assert checked[k]==v.removeprefix('sha256:'),(n,k)
source=read('HIGHER_POST12_T39_REVIEW.json');assert source['details']['sixteen_remaining_covered_target_geometries']==1012 and source['details']['sixteen_remaining_free_target_geometries']==0
assert not m['predecessor_requirement_discharged_here'] and m['complete_fourteen_hole_theorem_required_for_complete_sixteen_domain']
for v in (1,7,31):
 n=f'SIXTEEN_POST12_FORCED_remaining_v{v}_covered.bin';assert sha(n)==source['audited_input_hashes'][n]
generic=read('HIGHER_FORCED_CHERRY_REVIEW.json')['details']
assert generic['local_criterion']=='labeled F+R acyclic' and generic['automatic_gap']=='j<=floor(c/2)<d'
assert generic['root_excluded_from_R'] and generic['R_endpoints_same_parity_as_Y'] and generic['universal_forced_R_required']
# Independent arithmetic pressure on the automatic-gap lemma, complementing
# the complete symbolic proof imported from the accepted generic transfer.
gapcases=0
for c in range(1,33):
 for s in (4,6):
  for delta in (0,1):
   num=c+s-(1-delta)
   if num%2:continue
   assert num//2>c//2
   for j in range(c//2+1):assert num//2>j;gapcases+=1
out={'status':'PASS','frozen_hashes':expected,'manifest_files_verified':len(m['hashes']),'formal_PASS_gates':gates,'formal_direct_source_bindings_verified':len(checked),'source_conditional_T39_gate_and_all_three_raw_outputs_bound':True,'complete14_predecessor_condition_retained':True,'full_sixteen_hole_proved':False,'automatic_gap_arithmetic_cases':gapcases,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'SIXTEEN_LOCAL_REVIEW_bind.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))

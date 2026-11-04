"""Accept higher implications without promoting unmet predecessor assumptions."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
cache={}
def sha(p):
 p=p.resolve();s=p.stat();key=(str(p),s.st_size,s.st_mtime_ns)
 if key not in cache:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
  cache[key]=h.hexdigest()
 return cache[key]
def checked(name):
 p=R/name
 if not p.exists():return None
 d=json.loads(p.read_text(encoding='utf-8'))
 if d.get('verdict')!='PASS':return None
 assert d.get('audited_input_hashes')
 for k in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','audit_artifact_hashes','producer_comparison_hashes','accepted_import_source_bindings','evidence_hashes'):
  for n,h in d.get(k,{}).items():
   q=Path(n)
   if not q.is_absolute():q=R/q
   assert sha(q)==h.removeprefix('sha256:'),(name,n)
 if d.get('report_hash'):assert sha(R/name.replace('.json','.md'))==d['report_hash'].removeprefix('sha256:')
 return d
names=['HIGHER_POST12_REUSE_REVIEW.json','HIGHER_POST12_T39_REVIEW.json','SIXTEEN_LOCAL_REVIEW.json']
reviews={n:checked(n) for n in names};assert reviews[names[0]] and reviews[names[1]]
ad=reviews[names[1]]['details'];assert ad['complete16_implies_complete18_proved']
assert ad['sixteen_remaining_covered_target_geometries']==1012
assert ad['sixteen_remaining_free_target_geometries']==0
assert ad['eighteen_remaining_covered_target_geometries_conditional_on_full16']==0
assert not ad['full_sixteen_hole_proved'] and not ad['full_eighteen_hole_proved'] and not ad['full_P6_proved']
remaining=1012;bytarget={'1':100,'7':282,'31':630};latest=names[1]
if reviews[names[2]]:
 ld=reviews[names[2]]['details'];assert ld['remaining_covered_target_geometries']==148 and ld['remaining_free_target_geometries']==0
 assert ld['full_sixteen_hole_proved'] is False and ld['full_P6_proved'] is False
 remaining=148;bytarget={'1':0,'7':18,'31':130};latest=names[2]
for n in ('RUN_STATE.json','PROOF_CHECK_STATE.json'):
 p=R/n;d=json.loads(p.read_text(encoding='utf-8'));assert not d['full_p6_proved']
 d['higher_conditional_accepted_reviews']={n:sha(R/n) for n in names if reviews[n]}
 d['complete_sixteen_hole_implies_complete_eighteen_hole_proved']=True
 d['eighteen_hole_conditional_closure']={'review':names[1],'required_predecessor':'Complete sixteen-hole prescribed-endpoint theorem','predecessor_discharged':False,'covered_remaining_conditional':0,'free_remaining_conditional':0}
 d['sixteen_hole_conditional_geometry_residual']={'review':latest,'required_predecessor':'Complete fourteen-hole prescribed-endpoint theorem','predecessor_discharged':False,'covered_remaining':remaining,'covered_by_target':bytarget,'free_remaining':0}
 d['full_sixteen_hole_proved']=False;d['full_eighteen_hole_proved']=False
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'complete16_implies_complete18_proved':True,'sixteen_conditional_remaining':remaining,'full16':False,'full18':False,'fullP6':False}))

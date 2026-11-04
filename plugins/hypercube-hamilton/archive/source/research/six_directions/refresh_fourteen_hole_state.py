"""Promote only hash-bound independent fourteen-hole reviews."""
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
 assert d.get('audited_input_hashes'),name
 for key in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','audit_artifact_hashes','producer_comparison_hashes','accepted_import_source_bindings','evidence_hashes'):
  for n,h in d.get(key,{}).items():
   q=Path(n)
   if not q.is_absolute():q=R/q
   assert sha(q)==h.removeprefix('sha256:'),(name,n)
 for imp in d.get('formal_imports',[]):
  assert sha(R/imp['file'])==imp['sha256'].removeprefix('sha256:'),(name,imp['file'])
 if d.get('report_hash'):assert sha(R/name.replace('.json','.md'))==d['report_hash'].removeprefix('sha256:')
 return d
names=['TWELVE_HOLE_FULL_REVIEW.json','FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW.json','FOURTEEN_HALL_REVIEW.json','FOURTEEN_FORCED_REVIEW.json','FOURTEEN_MAXIMAL_A_REVIEW.json','FOURTEEN_STAR_EXPANDED_REVIEW.json','FOURTEEN_STAR_B_GLOBAL35_REVIEW.json','FOURTEEN_MID_SELECTED_REVIEW.json']
reviews={n:checked(n) for n in names}
full,reuse,cached,hall,forced,maximal,expanded,global35,mid=(reviews[n] for n in names)
assert full and full['details']['full_twelve_hole_proved']
assert reuse and cached
for x in (reuse,cached):
 assert not x['details']['source_reduction_conditional_on_full_twelve_hole']
 assert not x['details']['full_fourteen_hole_proved'] and not x['details']['full_P6_proved']
assert cached['details']['remaining_covered_target_geometries']==12528
assert cached['details']['remaining_free_target_geometries']==18
remaining=12528;free=18;bytarget={'1':3105,'7':3613,'31':5810};latest=names[2];free_proved=False
if hall:
 hd=hall['details']
 assert hd['remaining_covered_target_geometries']==3923 and hd['remaining_free_target_geometries']==0
 assert hd['fourteen_hole_free_targets_proved'] is True
 assert hd['full_fourteen_hole_proved'] is False and hd['full_P6_proved'] is False
 remaining=3923;free=0;bytarget={'1':840,'7':1188,'31':1895};latest=names[3];free_proved=True
if forced:
 assert hall
 fd=forced['details'];assert fd['remaining_covered_target_geometries']==2587
 assert fd['remaining_free_target_geometries']==0 and fd['fourteen_hole_free_targets_proved'] is True
 assert fd['full_fourteen_hole_proved'] is False and fd['full_P6_proved'] is False
 remaining=2587;bytarget={'1':240,'7':702,'31':1645};latest=names[4]
if maximal:
 assert forced
 md=maximal['details'];assert md['remaining_covered_target_geometries']==2527 and md['remaining_free_target_geometries']==0
 assert md['full_fourteen_hole_proved'] is False and md['full_P6_proved'] is False
 remaining=2527;bytarget={'1':240,'7':702,'31':1585};latest=names[5]
for report,predecessor,count,counts,gate in (
 (expanded,maximal,2407,{'1':240,'7':702,'31':1465},names[6]),
 (global35,expanded,2287,{'1':240,'7':702,'31':1345},names[7]),
 (mid,global35,25,{'1':0,'7':0,'31':25},names[8])):
 if report:
  assert predecessor
  rd=report['details'];assert rd['remaining_covered_target_geometries']==count and rd['remaining_free_target_geometries']==0
  assert rd['full_fourteen_hole_proved'] is False and rd['full_P6_proved'] is False
  remaining=count;bytarget=counts;latest=gate
for name in ('RUN_STATE.json','PROOF_CHECK_STATE.json'):
 p=R/name;d=json.loads(p.read_text(encoding='utf-8'))
 assert d['full_twelve_hole_proved'] and not d['full_p6_proved']
 d.update(full_fourteen_hole_proved=False,fourteen_hole_free_targets_proved=free_proved,
  fourteen_hole_covered_targets_proved=False,remaining_full_p6_hole_levels=[14,16,18],
  fourteen_hole_accepted_reviews={n:sha(R/n) for n,x in reviews.items() if x},
  fourteen_hole_geometry_residual={'review':latest,'covered_remaining':remaining,'covered_by_target':bytarget,
    'free_remaining':free,'full_free_branch_assembly_accepted':free_proved,
    'status':'Exact residual under accepted sufficient routes; not a set of counterexamples'})
 if name=='RUN_STATE.json':
  d['last_goal_turn_classification']='progress'
  d['latest_proof_package']='FOURTEEN_RESIDUAL_STRUCTURE_PROOF.md' if maximal else ('FOURTEEN_FORCED_APPLICATION.md' if forced else ('FOURTEEN_HALL_PROOF.md' if hall else 'FOURTEEN_CACHED_PROOF.md'))
  if expanded:d['latest_proof_package']='FOURTEEN_STAR_EXPANDED_PROOF.md'
  if global35:d['latest_proof_package']='FOURTEEN_STAR_B_GLOBAL35_PROOF.md'
  if mid:d['latest_proof_package']='FOURTEEN_MID_SELECTED_PROOF.md'
  d['active_research_priority']='Close fourteen-hole covered-target residual, then discharge complete sixteen/eighteen-hole layers.'
  d['remaining_structure']=f'Full2/4/6/8/10/12 accepted. Fourteen-hole free branch {"accepted" if free_proved else "OPEN"}; covered residual {remaining}. Full14/16/18 and fullP6 OPEN.'
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'full12':True,'fourteen_free_proved':free_proved,'fourteen_covered_remaining':remaining,'fourteen_free_remaining':free,'full_P6_proved':False}))

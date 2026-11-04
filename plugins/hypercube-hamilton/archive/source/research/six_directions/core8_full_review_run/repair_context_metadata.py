"""Correct context/proof hash classification; never write parent state."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent.parent
review_path=R/'T15_CORE8_FULL_REVIEW.json'
review=json.loads(review_path.read_text(encoding='utf-8'))
context_keys=['eight_current_core_ledger.json','eight_after_balanced_bridge_candidates.json']+[f'remaining_eight_current_{t}.bin' for t in (1,7,31)]
original=dict(review['audited_input_hashes'])
original_artifacts=dict(review['audit_artifact_hashes'])
context={p:original[p] for p in context_keys}
metadata={
 'recorded_in_original_review_at_utc':review['date'],
 'sampling_time_note':'Snapshot was sampled before the original review report; precise separate sampling time was not logged.',
 'role':'Optional read-only parent ledger recount, not a core8 theorem dependency.',
 'later_parent_integration_may_change_files':True,
 'original_recount':review['current_ledger_read_only_recount'],
 'original_hypothetical_after_core8':review['hypothetical_after_core8']}
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return 'sha256:'+h.hexdigest()
for target in [review,R/'core8_full_review_run/fresh_supplement.json']:
 data=target if isinstance(target,dict) else json.loads(target.read_text(encoding='utf-8'))
 for p,h in context.items():assert data['audited_input_hashes'].pop(p)==h
 data['context_snapshot_hashes']=context
 data['context_snapshot_metadata']=metadata
 if not isinstance(target,dict):target.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
assert review['audited_input_hashes']=={p:h for p,h in original.items() if p not in context}
assert len(original)-len(review['audited_input_hashes'])==5
for p,h in review['audited_input_hashes'].items():assert sha(R/p)==h,p
assert review['verdict']=='PASS'
changed_artifacts=['T15_CORE8_FULL_REVIEW.md','core8_full_review_run/fresh_supplement.py','core8_full_review_run/fresh_supplement.json']
for p in changed_artifacts:review['audit_artifact_hashes'][p]=sha(R/p)
review['audit_artifact_hashes']['core8_full_review_run/repair_context_metadata.py']=sha(Path(__file__))
for p,h in review['audit_artifact_hashes'].items():assert sha(R/p)==h,p
assert all(review['audit_artifact_hashes'][p]==h for p,h in original_artifacts.items() if p not in changed_artifacts)
review['metadata_correction']={
 'corrected_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reason':'Read-only parent census snapshots were mistakenly classified as theorem input dependencies.',
 'moved_to_context_snapshot_hashes':context_keys,
 'all_actual_proof_certificate_checker_hashes_retained':True,
 'theorem_input_hashes_rechecked':len(review['audited_input_hashes']),
 'audit_artifact_hashes_rechecked':len(review['audit_artifact_hashes']),
 'main_ledger_modified':False,'verdict_changed':False}
review_path.write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
print(json.dumps(review['metadata_correction']))

import json,hashlib
from pathlib import Path
R=Path('.')
small=json.loads((R/'t15_alternative_small_verification.json').read_text());assert small['status']=='PASS'
block=json.loads((R/'t15_alternative_core25_blockers_verification.json').read_text());assert block['status']=='PASS' and block['c5_target_common_null_count']==0
rows=[]
for k,n in ((18,405405),(21,270270),(25,2702700)):
 a=json.loads((R/f't15_alternative_core{k}_c1_residual.json').read_text());b=json.loads((R/f't15_alternative_core{k}_c1_residual_verification.json').read_text())
 assert a['total']==a['positive']==b['records']==n and a['unknown']==a['negative']==0 and b['status']=='PASS'
 f=R/f't15_alternative_core{k}_c1_residual.bin';assert f.stat().st_size==n*56
 rows.append({'core':k,'verified_residual_certificates':n,'witness_bytes':f.stat().st_size,'witness_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'c3_B_ordered_inputs':1621620,'c1_B_inputs':135135,'large_crossing_method':'single-negative bridge12' if k!=25 else 'complete inverse blockers transported from core23 B geometry'})
out={'status':'PASS','scope':'All listed new finite obligations and residual positives for full T15 cores18,21,25; fresh semantic audit pending, no global eight-hole closure claimed','rows':rows,'residual_certificates_total':sum(t['verified_residual_certificates'] for t in rows)}
(R/'t15_alternative_group_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

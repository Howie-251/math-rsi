"""Producer batch over the 55 actual marked projection orbits; no ledger writes."""
from pathlib import Path
import subprocess,json,hashlib
P=Path(__file__).resolve().parent
profile=json.loads((P/'Q5_T26_RANK_profile.json').read_text())['rows'];reports=[]
for i,row in enumerate(profile):
 if i==0:
  meta=json.loads((P/'Q5_T26_RANK_first.json').read_text());prefix='Q5_T26_RANK_first'
 else:
  prefix=f'Q5_T26_RANK_batch_{i:02d}'
  config=P/(prefix+'_config.txt');config.write_text(' '.join(map(str,row['minority']+row['majority']+row['omitted']))+'\n')
  run=subprocess.run([str(P/'Q5_T26_RANK_search.exe'),str(config),str(P/prefix),'100000'],capture_output=True,text=True)
  (P/(prefix+'.log')).write_text(run.stdout+run.stderr)
  if run.returncode:raise RuntimeError((i,run.returncode,run.stderr))
  meta=json.loads((P/(prefix+'.json')).read_text())
 reports.append({'orbit_index':i,'prefix':prefix,'geometry':row,'rank_GF2':meta['rank_GF2'],
  'full_rank':meta['full_rank'],'forests_examined':meta['forests_examined'],'status':'PRODUCER_FULL_RANK_REVIEW_PENDING' if meta['full_rank'] else 'OPEN_DEFICIENT_OR_CAPPED'})
 out={'status':'PRODUCER_BATCH_IN_PROGRESS' if len(reports)<len(profile) else 'PRODUCER_BATCH_FINISHED',
  'completed_orbits':len(reports),'total_orbits':len(profile),'full_rank_orbits':sum(r['full_rank'] for r in reports),
  'reports':reports,'full_T26_proved':False,'full_ten_hole_proved':False,'full_P6_proved':False}
 (P/'Q5_T26_RANK_batch_summary.json').write_text(json.dumps(out,indent=2)+'\n')
 print(i,meta['rank_GF2'],meta['forests_examined'],flush=True)

"""Independent-prefix producer4096-rank runs on all15 actual T15 marked orbits."""
from pathlib import Path
import json,subprocess
P=Path(__file__).resolve().parent
profile=json.loads((P/'Q5_T15_RANK_profile.json').read_text())['rows'];reports=[]
for i,g in enumerate(profile):
 pre=f'Q5_T15_RANK_orbit_{i:02d}';cfg=P/(pre+'_config.txt')
 cfg.write_text(' '.join(map(str,g['minority']+list(g['majority'])+list(g['omitted'])))+'\n')
 run=subprocess.run([str(P/'Q5_T15_RANK_search.exe'),str(cfg),str(P/pre),'150000'],capture_output=True,text=True)
 (P/(pre+'.log')).write_text(run.stdout+run.stderr)
 if run.returncode:raise RuntimeError((i,run.returncode,run.stdout,run.stderr))
 rank=json.loads((P/(pre+'.json')).read_text());reports.append({'orbit_index':i,'prefix':pre,'geometry':g,**rank})
 out={'status':'PRODUCER_IN_PROGRESS' if len(reports)<len(profile) else 'PRODUCER_FINISHED','completed':len(reports),
  'total':len(profile),'rank_full':sum(r['full_rank'] for r in reports),'reports':reports,'full_T15_proved':False,'full_ten_hole_proved':False,'full_P6_proved':False}
 (P/'Q5_T15_RANK_batch_summary.json').write_text(json.dumps(out,indent=2)+'\n')
 print(i,rank['rank_GF2'],rank['forests_examined'],flush=True)

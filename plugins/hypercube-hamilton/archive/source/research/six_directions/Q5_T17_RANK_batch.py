"""Producer rank batch on every unforced actual4096-domain T17 orbit."""
from pathlib import Path
import json,subprocess,hashlib
R=Path(__file__).resolve().parent
profile=json.loads((R/'Q5_T17_RANK_candidate_profile.json').read_text())
summary=[]
for row in profile['rows']:
 if row['full_rank_obstructed_by_triangle']:continue
 pre=f"Q5_T17_RANK_batch_{row['id']:02d}"
 cfg=R/(pre+'_config.txt');cfg.write_text(' '.join(map(str,[0,*row['majority'],*row['omitted']]))+'\n')
 run=subprocess.run([str(R/'Q5_T17_RANK_search.exe'),str(cfg),str(R/pre),'2000000'],capture_output=True,text=True,check=True)
 (R/(pre+'.log')).write_text(run.stdout+run.stderr)
 a=json.loads((R/(pre+'.json')).read_text())
 summary.append({'id':row['id'],'prefix':pre,'marked_geometry':row,'rank':a['rank_GF2'],'full_rank':a['full_rank'],'forests_examined':a['forests_examined']})
 print(pre,a['rank_GF2'],a['forests_examined'],flush=True)
out={'status':'PRODUCER_BATCH_FRESH_REVIEW_PENDING','orbits':summary,'full_rank_count':sum(x['full_rank'] for x in summary),'full_P6_proved':False}
(R/'Q5_T17_RANK_batch_summary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

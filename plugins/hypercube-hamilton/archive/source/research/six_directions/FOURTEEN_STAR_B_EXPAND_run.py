from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parent
rows=json.loads((R/'FOURTEEN_STAR_B_EXPAND_profile.json').read_text())['rows'];reports=[]
for row in rows:
 i=row['index'];pre=R/f'FOURTEEN_STAR_B_EXPAND_orbit_{i:03d}'
 cfg=Path(str(pre)+'_config.txt');cfg.write_text(' '.join(map(str,sorted(row['minority']+row['majority'])+row['omitted']))+'\n')
 with Path(str(pre)+'.log').open('w') as f:
  run=subprocess.run([str(R/'TWELVE_NEW_T19_search.exe'),str(cfg),str(pre),'100000'],stdout=f,stderr=f)
 assert run.returncode==0,(i,run.returncode)
 info=json.loads(Path(str(pre)+'.json').read_text())
 reports.append({'index':i,'prefix':pre.name,'geometry':row,'rank':info['rank_GF2'],'forced_target_rank':512,'forced_rank_reached':info['rank_GF2']==512,'forests_examined':info['forests_examined']})
 (R/'FOURTEEN_STAR_B_EXPAND_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'total':len(rows),'reports':reports},indent=2)+'\n')
 print(i,info['rank_GF2'],info['forests_examined'],flush=True)

"""Bounded positive-certificate production for all 64 independent T37 orbits."""
import json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
rows=json.loads((R/'Q5_T37_INDEPENDENT_geometry.json').read_text())['rows'];reports=[]
for row in rows:
    i=row['index'];pre=R/f'Q5_T37_INDEPENDENT_orbit_{i:02d}'
    cfg=Path(str(pre)+'_config.txt');cfg.write_text(' '.join(map(str,sorted(row['minority']+row['majority'])+row['omitted']))+'\n')
    with Path(str(pre)+'.log').open('w') as f:
        run=subprocess.run([str(R/'Q5_T37_INDEPENDENT_search.exe'),str(cfg),str(pre),'200000'],stdout=f,stderr=f)
    assert run.returncode==0,(i,run.returncode)
    info=json.loads(Path(str(pre)+'.json').read_text())
    reports.append({'index':i,'prefix':pre.name,'geometry':row,'rank':info['rank_GF2'],'full_rank':info['full_rank'],'forests_examined':info['forests_examined']})
    (R/'Q5_T37_INDEPENDENT_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'total':len(rows),'full_rank_orbits':sum(x['full_rank'] for x in reports),'reports':reports},indent=2)+'\n')
    print(i,info['rank_GF2'],info['forests_examined'],flush=True)

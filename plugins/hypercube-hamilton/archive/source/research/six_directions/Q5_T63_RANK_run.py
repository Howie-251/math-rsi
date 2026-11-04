"""Bounded positive-witness generation for seven actual T63 marked orbits."""
import json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
rows=json.loads((R/'Q5_T63_RANK_profile.json').read_text())['rows'];reports=[]
for i,row in enumerate(rows):
    prefix=R/f'Q5_T63_RANK_orbit_{i:02d}'
    cfg=Path(str(prefix)+'_config.txt');cfg.write_text(' '.join(map(str,row['holes']+row['omitted']))+'\n')
    with Path(str(prefix)+'.log').open('w') as log:
        result=subprocess.run([str(R/'Q5_T63_RANK_search.exe'),str(cfg),str(prefix),'200000'],stdout=log,stderr=log)
    assert result.returncode==0,(i,result.returncode)
    report=json.loads(Path(str(prefix)+'.json').read_text())
    reports.append({'orbit_index':i,'prefix':prefix.name,'geometry':row,'rank':report['rank_GF2'],'full_rank':report['full_rank'],'forests_examined':report['forests_examined']})
    (R/'Q5_T63_RANK_batch_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'reports':reports},indent=2)+'\n')
    print(i,report['rank_GF2'],report['forests_examined'],flush=True)

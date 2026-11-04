"""Search prioritized actual local geometries; all output remains producer-only."""
from pathlib import Path
import json,subprocess,sys
R=Path(__file__).resolve().parent
rows=json.loads((R/'TWELVE_NEW_TYPES_profile.json').read_text())['rows']
limit=int(sys.argv[1]) if len(sys.argv)>1 else 30
summary_path=R/'TWELVE_NEW_TYPES_summary.json'
reports=json.loads(summary_path.read_text())['reports'] if summary_path.exists() else []
assert all(r['index']==i and r['geometry']==rows[i] for i,r in enumerate(reports))
for row in rows[len(reports):limit]:
    i=row['index'];typ=row['type'];pre=R/f'TWELVE_NEW_TYPES_orbit_{i:03d}'
    cfg=Path(str(pre)+'_config.txt');cfg.write_text(' '.join(map(str,sorted(row['minority']+row['majority'])+row['omitted']))+'\n')
    with Path(str(pre)+'.log').open('w') as f:
        run=subprocess.run([str(R/f'TWELVE_NEW_{typ}_search.exe'),str(cfg),str(pre),'100000'],stdout=f,stderr=f)
    assert run.returncode==0,(i,typ,run.returncode)
    info=json.loads(Path(str(pre)+'.json').read_text())
    reports.append({'index':i,'prefix':pre.name,'geometry':row,'rank':info['rank_GF2'],'full_rank':info['full_rank'],'forests_examined':info['forests_examined']})
    (R/'TWELVE_NEW_TYPES_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'requested':limit,'total_geometries':len(rows),'full_rank_orbits':sum(x['full_rank'] for x in reports),'reports':reports},indent=2)+'\n')
    print(i,typ,row['actual_records'],info['rank_GF2'],info['forests_examined'],flush=True)

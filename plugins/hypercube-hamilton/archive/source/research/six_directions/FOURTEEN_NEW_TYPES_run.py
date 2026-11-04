from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parent
rows=json.loads((R/'FOURTEEN_NEW_TYPES_profile.json').read_text())['rows'];reports=[]
assert all(r['type']!='T48' for r in rows)
for row in rows:
    i=row['index'];pre=R/f'FOURTEEN_NEW_TYPES_orbit_{i:03d}'
    cfg=Path(str(pre)+'_config.txt');cfg.write_text(' '.join(map(str,sorted(row['minority']+row['majority'])+row['omitted']))+'\n')
    with Path(str(pre)+'.log').open('w') as f:
        run=subprocess.run([str(R/f'FOURTEEN_NEW_{row["type"]}_search.exe'),str(cfg),str(pre),'100000'],stdout=f,stderr=f)
    assert run.returncode==0,(i,run.returncode)
    info=json.loads(Path(str(pre)+'.json').read_text())
    reports.append({'index':i,'prefix':pre.name,'geometry':row,'rank':info['rank_GF2'],'full_rank':info['full_rank'],'forests_examined':info['forests_examined']})
    (R/'FOURTEEN_NEW_TYPES_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'total':len(rows),'full_rank_orbits':sum(r['full_rank'] for r in reports),'reports':reports},indent=2)+'\n')
    print(i,row['type'],row['actual_records'],info['rank_GF2'],info['forests_examined'],flush=True)

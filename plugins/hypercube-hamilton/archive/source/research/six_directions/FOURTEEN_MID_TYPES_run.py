from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parent
def key(g):return tuple(tuple(sorted(g[k])) for k in ('minority','majority','omitted'))
cache={}
for name in ('TWELVE_NEW_TYPES_summary.json','TWELVE_EXTRA_TYPES_summary.json','Q5_T37_INDEPENDENT_summary.json'):
 for row in json.loads((R/name).read_text())['reports']:cache.setdefault(key(row['geometry']),row)
exes={(8,2):'Q5_T26_RANK_search.exe',(8,3):'Q5_T17_RANK_search.exe',(10,2):'Q5_T37_INDEPENDENT_search.exe',(10,3):'TWELVE_NEW_T28_search.exe',(10,4):'TWELVE_NEW_T19_search.exe',(10,5):'TWELVE_NEW_T105_search.exe'}
rows=json.loads((R/'FOURTEEN_MID_TYPES_profile.json').read_text())['rows'];reports=[]
for row in rows:
 i=row['index'];old=cache.get(key(row))
 if old:
  report={'index':i,'prefix':old['prefix'],'geometry':row,'rank':old['rank'],'full_rank':old['full_rank'],'forests_examined':old['forests_examined'],'reused_cache':True}
 else:
  pre=R/f'FOURTEEN_MID_TYPES_orbit_{i:03d}';cfg=Path(str(pre)+'_config.txt');cfg.write_text(' '.join(map(str,sorted(row['minority']+row['majority'])+row['omitted']))+'\n')
  with Path(str(pre)+'.log').open('w') as f:
   run=subprocess.run([str(R/exes[row['holes'],row['omit_count']]),str(cfg),str(pre),'100000'],stdout=f,stderr=f)
  assert run.returncode==0,(i,run.returncode)
  info=json.loads(Path(str(pre)+'.json').read_text());report={'index':i,'prefix':pre.name,'geometry':row,'rank':info['rank_GF2'],'full_rank':info['full_rank'],'forests_examined':info['forests_examined'],'reused_cache':False}
 reports.append(report)
 (R/'FOURTEEN_MID_TYPES_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'total':len(rows),'reports':reports},indent=2)+'\n')
 print(i,row['type'],row['actual_records'],report['rank'],'cached' if old else 'new',flush=True)

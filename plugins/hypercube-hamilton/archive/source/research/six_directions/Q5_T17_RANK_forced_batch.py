"""Producer conditional rank certificates after removing forced cherry pair."""
from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parent
profile=json.loads((R/'Q5_T17_RANK_candidate_profile.json').read_text());out=[]
for row in profile['rows']:
 if not row['full_rank_obstructed_by_triangle']:continue
 pre=f"Q5_T17_RANK_forced_{row['id']:02d}";cfg=R/(pre+'_config.txt')
 cfg.write_text(' '.join(map(str,[0,*row['majority'],*row['omitted'],*row['forced_cherry_pair']]))+'\n')
 run=subprocess.run([str(R/'Q5_T17_RANK_reduced_search.exe'),str(cfg),str(R/pre),'2000000'],capture_output=True,text=True,check=True)
 (R/(pre+'.log')).write_text(run.stdout+run.stderr)
 a=json.loads((R/(pre+'.json')).read_text())
 out.append({'id':row['id'],'prefix':pre,'marked_geometry':row,'reduced_endpoint_count':22,'rank':a['rank_GF2'],'full_reduced_rank':a['full_rank'],'forests_examined':a['forests_examined']})
 print(pre,a['rank_GF2'],a['forests_examined'],flush=True)
(R/'Q5_T17_RANK_forced_summary.json').write_text(json.dumps({'status':'CONDITIONAL_LOCAL_CLASSIFICATION_PRODUCER_REVIEW_PENDING','orbits':out,'all_full_reduced_rank':all(x['full_reduced_rank'] for x in out),'Q6_completion_avoidance_proved':False,'full_P6_proved':False},indent=2)+'\n')

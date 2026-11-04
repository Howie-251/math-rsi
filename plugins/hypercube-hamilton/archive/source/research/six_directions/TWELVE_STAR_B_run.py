"""Producer reduced-rank conditional local B certificates; no Q6 star conclusion."""
from pathlib import Path
import subprocess,json
P=Path(__file__).resolve().parent
profile=json.loads((P/'TWELVE_STAR_B_profile.json').read_text());reports=[]
for g in profile['rows']:
 index=g['index'];pre=f'TWELVE_STAR_B_orbit_{index:02d}';cfg=P/(pre+'_config.txt')
 cfg.write_text(' '.join(map(str,sorted(g['minority']+g['majority'])+g['omitted']+g['forced_pair']))+'\n')
 run=subprocess.run([str(P/'TWELVE_STAR_B_rank.exe'),str(cfg),str(P/pre),'100000'],capture_output=True,text=True)
 (P/(pre+'.log')).write_text(run.stdout+run.stderr);assert run.returncode==0,(index,run.returncode,run.stdout,run.stderr)
 rank=json.loads((P/(pre+'.json')).read_text());reports.append({'index':index,'prefix':pre,'geometry':g,**rank})
 out={'status':'PRODUCER_ONLY_LOCAL_CONDITIONAL_CERTIFICATES_PENDING_REVIEW','completed':len(reports),'total':10,'reduced_fullrank_cases':sum(r['full_rank'] for r in reports),'reports':reports,'star_Q6_closed':False,'A_mixed_opening_interface_proved':False,'full_P6_proved':False}
 (P/'TWELVE_STAR_B_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(index,rank['rank_GF2'],rank['forests_examined'],flush=True)

"""Probe five nonadjacent-q,b mixed opening inputs; no coverage claim."""
from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parent
cases=[(3,4,7),(3,4,11),(15,1,14),(15,1,7),(15,16,7)]
reports=[]
for i,(q,b,t) in enumerate(cases):
    pre=R/f'TWELVE_ROOT_STAR_OPENING_case_{i:02d}';cfg=Path(str(pre)+'_config.txt')
    cfg.write_text(' '.join(map(str,sorted([0,q,31,b])+[0,31,q,t]))+'\n')
    with Path(str(pre)+'.log').open('w') as f:
        result=subprocess.run([str(R/'TWELVE_ROOT_STAR_OPENING_probe_search.exe'),str(cfg),str(pre),'200000'],stdout=f,stderr=f)
    assert result.returncode==0,(i,result.returncode)
    info=json.loads(Path(str(pre)+'.json').read_text())
    reports.append({'index':i,'prefix':pre.name,'q':q,'b':b,'t':t,'rank':info['rank_GF2'],'full_rank':info['full_rank'],'forests_examined':info['forests_examined']})
    (R/'TWELVE_ROOT_STAR_OPENING_batch_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','completed':len(reports),'total':len(cases),'reports':reports,'full_twelve_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
    print(reports[-1],flush=True)

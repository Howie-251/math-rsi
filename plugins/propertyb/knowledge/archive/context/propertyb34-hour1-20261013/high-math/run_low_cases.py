from pathlib import Path
import json,time
from mixed_six import run,json_value
cases=[(1,[]),(1,[6]),(2,[]),(2,[12]),(2,[3]),(2,[3,12]),(3,[]),(3,[3]),(4,[]),(4,[3]),(4,[3,12]),(5,[]),(5,[3]),(5,[3,12]),(6,[]),(6,[3]),(6,[3,12]),(6,[3,12,48])]
start=time.perf_counter();summary=[]
for low,bad in cases:
 print('START LOW',low,'BAD',bad,flush=True)
 r=run(24,[6]*low+[7]*(6-low),bad,budget=4)
 p=Path(__file__).with_name(f'MIXED_SIX_v24_low{low}_bad'+('_'.join(map(str,bad)) or 'none')+'.json');p.write_text(json.dumps(json_value(r),indent=2)+'\n')
 summary.append(dict(low=low,bad=bad,file=p.name,passed=r['passed'],groups=r['groups'],seconds=r['elapsed_seconds']))
 print('SUMMARY',summary[-1],flush=True)
Path(__file__).with_name('V24_LOW_CASES_SUMMARY.json').write_text(json.dumps(dict(elapsed=time.perf_counter()-start,results=summary),indent=2)+'\n')

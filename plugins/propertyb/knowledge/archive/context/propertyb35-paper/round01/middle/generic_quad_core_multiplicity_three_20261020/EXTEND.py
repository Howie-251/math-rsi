"""Continue only new four-core representatives; preserve frozen first pilot."""
from pathlib import Path
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();domain=json.loads((P/'DOMAIN.json').read_text());old=json.loads((P/'RESULT.json').read_text());cases=old['cases'].copy();done={(tuple(c['degrees']),tuple(c['counts'])) for c in cases};queue=[(tuple(j['degrees']),tuple(ns)) for j in domain['jobs'] for ns in j['representative_keys']];queue.sort(key=lambda z:(z[1][15]!=4,max(z[0]),z[0],z[1]));new=[]
for d,ns in queue:
 if (d,ns) in done:continue
 e=SubsetEngine(21,4,{m:v for m,v in enumerate(ns) if v});original=e.inv.copy();e.inv={p:(0,0,[]) for p in original};z=e.solve();mode='zero'
 if z['bound']>=1:e.inv=original;z=e.solve();mode='nested_total_pure'
 c=dict(degrees=d,counts=ns,mode=mode,positions=z['positions'],bound=z['bound'],strict=z['bound']<1);new.append(c);cases.append(c)
 if z['bound']>=1:print('NEW_NONSTRICT',d,str(z['bound']),ns,flush=True);break
 if time.process_time()-st>15:print('CPU_STOP',flush=True);break
out=dict(scope=__doc__,complete=len(cases)==len(queue),total_orbits=len(queue),case_count=len(cases),new_cases=len(new),cases=cases,nonstrict=[c for c in cases if not c['strict']],mode_counts=dict(Counter(c['mode'] for c in cases)),cpu_seconds=time.process_time()-st)
(P/'EXTENDED_RESULT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print('EXTENDED',out['case_count'],len(queue),'new',len(new),'cpu',out['cpu_seconds'],flush=True)

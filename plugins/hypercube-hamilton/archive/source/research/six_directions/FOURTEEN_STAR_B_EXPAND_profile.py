from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json
R=Path(__file__).resolve().parent
structure=json.loads((R/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text())
maps=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
geos={};options=[];units={1,2,4,8,16};J=units|{14}
for orbit in (79,87):
 row=structure['orbit_rows'][orbit];T={z^32 for z in row['Z']};assert len(T)==6 and not T&J
 for t in sorted(T-{31}):
  for w in sorted(units):
   for b in sorted(units-{w}):
    U=J-{w,b};major=(T-{t})|U;assert len(major)==9
    key,pi=min(((tuple(sorted(tr[x] for x in major)),tuple(sorted(tr[x] for x in U)),tuple(sorted((tr[w],tr[b])))),i) for i,tr in enumerate(maps))
    if key not in geos:geos[key]=len(geos)
    options.append({'orbit':orbit,'t':t,'w':w,'b':b,'sources':sorted(U),'index':geos[key],'permutation':pi})
rows=[]
for (major,U,pair),i in sorted(geos.items(),key=lambda x:x[1]):
 rows.append({'index':i,'minority':[0],'majority':major,'omitted':U,'forced_pair':pair})
(R/'FOURTEEN_STAR_B_EXPAND_profile.json').write_text(json.dumps({'status':'PRODUCER_ONLY','rows':rows,'actual_options':options},indent=2)+'\n')
print('local classes',len(rows),'actual options',len(options))
